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

      Bz = 0                  # No field outside cyclotron
      Ex = 0
      Ey = 0
      if(r < self.r_D):
        Bz = self.B
       
      eq1 =                   # TO DO: equation for dx/dt
      eq2 =                   # TO DO: equation for dy/dt
      eq3 =                   # TO DO: equation for dvx/dt
      eq4 =                   # TO DO: equation for dvy/dt
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
                
