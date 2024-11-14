import numpy as np
import matplotlib.pyplot as plt

class PDE_1D_fast:
  """ A class to solve dv/dt=F(t,v) where F is a differential
      operator acting on the vector 'v'."""

  def __init__(self, v0, L=1):
    """
      : param v0         : initial condition as an array or a list
      : param L          : length of domain
    """
    self.reset(v0,L)
    

  def reset(self, v0, L=1, dt=1, t0=0):
    """ Set the initial parameters.
    
      : param v0         : initial condition
      : param L          : length of domain
      : param dt         : integration time step
      : param t0         : initla time
    """
    self.t = t0             # Initial time
    self.v = np.array(v0, dtype='float64') # ensure we use floats!
    self.Np = len(v0)       # Total number of points
    self.L = L              # Domain size
    self.dx = L/(self.Np-1) # Lattice size
     
    self.n = 0              # Time iteration number
    self.l_t = []           # List of t values for plots
    self.l_x = []           # List of x values for figures
    self.l_f = []           # List of array f values (arrays) for figures
    self.boundary(self.v)   # Make sure the boundary condition is set
    
  def F(self, v):
    """ Returns update for v as an array except for the first and last points 
        To be implemented in subclass boundary.
        See the example below the class definition
    
      : param v : current function value (a vector).
      : return  : update for v at position i.
    """
    pass

  def boundary(self, v):
    """ Enforce the boundary conditions. To be implemented in subclass.
    """
    pass
  
  def RK4_one_step(self):
      """ Perform a single integration step of the 4th order Runge Kutta method
.
      """

      k1 = self.F(self.t, self.v)
      K = self.v+0.5*self.dt*k1
      self.boundary(K)

      k2 = self.F(self.t+0.5*self.dt, K)
      K = self.v+0.5*self.dt*k2
      self.boundary(K)

      k3 = self.F(self.t+0.5*self.dt, K)
      K = self.v+self.dt*k3
      self.boundary(K)
 
      k4 = self.F(self.t+self.dt, K)

      # self.v -> v(t+dt)
      self.v += self.dt/6.0*(k1+2.0*(k2+k3)+k4)      
      self.boundary(self.v)
      self.t += self.dt;

  def extra_data(self):
    """ Called each time data are saved for figures
        to use to generate more data
    """
    return
      
  def iterate(self, tmax, dt, fig_dt=-1):
    #relax_RK4(self, err, dt=0.1,nmax=-1,n_fig=0):
    """ Relax until largest update is smaller than err.
    
      : param tmax :  iterate until tmax.
      : param dt  : integration time step.
      : param fig_dt  : time step between figure data.
    """
    self.dt = dt

    if(fig_dt < 0) : fig_dt = self.dt*0.99 # Save all data

    next_fig_t = self.t*(1-1e-15)     # Ensure we save the initial values

    self.l_f.append(np.array(self.v)) # Save inital condition
    self.l_t.append(np.array(self.t)) # Save inital condition
    self.extra_data()

    while(self.t < tmax):
      self.RK4_one_step()
      
      if(self.t >= next_fig_t):       # Save fig when next_fig_t is reached
        self.l_f.append(np.array(self.v))
        self.l_t.append(self.t)
        self.extra_data()
        next_fig_t += fig_dt          # Set the next figure time
      
    # Set plot data
    self.l_x = np.linspace(0,self.Np-1, self.Np)   
    self.l_f.append(np.array(self.v))
    self.l_t.append(self.t)
    self.extra_data()

  def plot(self, n=-1, style="k-"):
    """ Plot the vector 'v'.

      : param n: index of function to plot.
      : param style: format for the plot function.
    """
    plt.plot(self.l_x, self.l_f[n], style);


# Tests follow; only run when not importing the module.

if __name__ == "__main__":

  class diff(PDE_1D_fast):
    """ A class to relax to static solutions of the diffusion equation. """
    def F(self, t, v):
       """ Diffusion equation
         : param t : current time
         : param v : current function
       """       
       eq = np.zeros(self.Np)
       # Eval equation except for end points for which eq=0
       eq[1:self.Np-1] = (v[2:self.Np] + v[:self.Np-2] -2*v[1:self.Np-1])\
                         /self.dx**2
       return(eq)
   
    def boundary(self, v):
       """ Enforce the boundary conditions. 
           Left: 1 (large pool). Right 0 (empty pool)
       """
       v[0] = 1
       v[-1] = 0

    def best_dt(self, coef):
       """ Best dt for this equation
       : param coef : adjustment coeficient
       """
       return(coef*self.dx**2)
    
  Np=50
  diff_eq = diff(np.zeros([Np]), 1)
  n = diff_eq.iterate(1, diff_eq.best_dt(0.5), fig_dt=0.1)
  print("No of iterations: ",n) 
  for nf in range(len(diff_eq.l_f)):
    print(diff_eq.l_t[nf])
    diff_eq.plot(nf)
    plt.show()
