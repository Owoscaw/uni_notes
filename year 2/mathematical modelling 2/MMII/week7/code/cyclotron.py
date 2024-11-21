import ode_rk4
import numpy as np
import matplotlib.pyplot as plt

class CyclotronRK4(ode_rk4.ODE_RK4):
  """A class to compute the trajectory of an electron in an 
     electro-magnetic field non-zero only inside a circle.
  """
  def __init__(self, V0=[], dt=1e010, t0=0, B=0, dV=0):
      """Set the electron ODE parameters
      : param V0     : initial value (as an array or a list) 
      : param dt     : integration time step
      : param t0     : initial time
      : param B      : magnetic field
      : param dV     : Potential difference between the Ds in Volts
      """  
      super().__init__(V0,dt,t0) 
      self.B=B

      self.q=1.602e-19        # Electric charge in Coulomb for a proton
      self.m=1.672e-27        # In kg for a proton
      self.qom=self.q/self.m  # No need to compute q/m each time: do it once
      self.r_D=1              # Radius of the Ds
      self.w = 0.02           # GAp between the Ds
      self.dV=dV  
      self.E = self.dV/self.w # electric field between the Ds
      
  def F(self, t, v):
      """ equation to solve: 
          v: v[0]: x;  v[1]: y;  v[2]: vx;  v[3]: vy; 
        : param t : current time 
        : param v : current function as a vector
        : return : Lorentz force
      """
      x= v[0]; y=v[1];  vx=v[2]; vy=v[3]
      r = np.sqrt(x*x+y*y)

      # No field outside cyclotron
      Ex = 0
      Bz = 0
      Ey = 0

      if (-self.w/2 < y and y < self.w/2) and (abs(x) < self.r_D):  
        if x > 0:
          Ey = -self.E
        else:
          Ey = self.E


      if(r < self.r_D):
        Bz = self.B
      
      eq1 = vx
      eq2 = vy
      eq3 = self.qom*(Ex+Bz*vy)
      eq4 = self.qom*(Ey-Bz*vx)
      return(np.array([eq1, eq2, eq3, eq4]))


  def draw_Ds(self):
      # Upper part
      xl = []
      yl = []
      for theta in np.linspace(0, np.pi, 100):
        x = self.r_D*np.cos(theta)
        y = self.r_D*np.sin(theta)
        if (y > self.w*0.5): # Ignore points below D base
          xl.append(x)
          yl.append(y)
      xl.append(xl[0])       # Add last point to draw gase of D 
      yl.append(yl[0])
      plt.plot(xl, yl, "g-")
      # Lower part
      xl = []
      yl = []
      for theta in np.linspace(0, np.pi, 100):
        x = self.r_D*np.cos(theta)
        y = -self.r_D*np.sin(theta)
        if (y < -self.w*0.5): # Ignore points below D base
          xl.append(x)
          yl.append(y)
      xl.append(xl[0])       # Add last point to draw gase of D 
      yl.append(yl[0])
      plt.plot(xl, yl, "g-")

  def iterate_max(self, fig_dt=-1):
    """ Solve the system of equations DN/dt = F(N) until t=tmax.
        Save N and t in lists N_list and t_list every fig_dt.

      : param tmax   : integration upper bound
      : param fig_dt : interval between data point for figures (use dt if < 0)
    """
      
    if(fig_dt < 0) : fig_dt = self.dt*0.99 # Save all data
    
    next_fig_t = self.t*(1-1e-15) # Ensure we save the initial values

    # Save initial values for figures
    self.V_list.append(np.array(self.V)) # Force a copy of V!
    self.t_list.append(self.t)
    
    while (abs(self.V[0]) < 2*self.r_D) and (abs(self.V[1] < 2*self.r_D)):       # Integrate until out of box
      self.one_step()
      if(self.t >= next_fig_t): # Save fig when next_fig_t is reached       
        self.V_list.append(np.array(self.V)) # Force a copy of V!
        self.t_list.append(self.t)
        next_fig_t += fig_dt    # Set the next figure time

              
