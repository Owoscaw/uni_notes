import numpy as np
import matplotlib.pyplot as plt
import time

class RelaxJacobi1D:
  """ A class to solve F(v)=0, where F is a differential
      operator acting on the vector 'v', using Jacobi relaxation."""

  def __init__(self, v0):
    """
      : param v0         : initial condition as an array or a list
    """
    self.reset(v0)
    

  def reset(self, v0):
    """ Set the initial parameters.
    
      : param v0         : initial condition
    """
    self.v = np.array(v0, dtype='float64') # Ensure we use floats!
    self.Np = len(v0) # Total number of points
     
    self.n = 0        # Time iteration number
    self.l_x = []     # List of t values for figures
    self.l_f = []     # List of f values (arrays) for figures
    self.boundary()   # Make sure the boundary condition is set
    
  def F(self, v, i):
    """ Returns update for v as an array except for the first and last points 
        To be implemented in subclass.
        See the example below the class definition
    
      : param v : current function value (a vector).
      : param i : spatial index.
      : return  : update for v at position i.
    """
    pass

  def boundary(self):
    """ Enforce the boundary conditions. To be implemented in subclass.
    """
    pass
    
  def relax_1_step(self, nu=0.5):
    """ Perform a single Jacobi relaxation iteration.
    
      : param nu : relaxation parameter.
      : return   : the largest update.
    """
    w = np.array(self.v)
    dvmax = 0
    for i in range(1, self.Np-1):
      dv = nu*self.F(self.v, i)
      if(np.fabs(dv) > dvmax) : dvmax = np.fabs(dv)
      w[i] = self.v[i] + dv
      
    self.v = w
    return(dvmax)
    
  def relax(self, err, nu=0.5):
    """ Relax until largest update is smaller than err.
    
      : param err : target "error".
      : param nu  : relaxation parameter.
      : return    : number of iterations required.
    """
    e = 1e64          # Absurdly large
    n = 1
    while(e > err):
      e = self.relax_1_step(nu)
      self.boundary()
      n += 1
      if(n % 1000==0): print("n=",n)
      
    # Set plot data
    self.l_x = np.linspace(0,self.Np-1,self.Np)   
    self.l_f = np.array(self.v)
    return(n)
   
  def plot(self, style="k-"):
    """ Plot the vector 'v'.

      : param style: format for the plot function.
    """
    plt.plot(self.l_x, self.l_f, style);


# Tests follow; only run when not importing the module.

if __name__ == "__main__":

  class RelaxDiffusion(RelaxJacobi1D):
    """ A class to relax to static solutions of the diffusion equation. 
    """
    def F(self, v, i):
      """ Diffusion equation
        : param v : current function value (a vector).
        : param i : spatial index.
        : return  : update for v at position i.
      """
      return((v[i+1]+v[i-1]-2*v[i])) 

    def boundary(self):
      """ Enforce the boundary conditions. 
          Left: 1 (large pool). Right 0 (empty pool)
      """
      self.v[0] = 1
      self.v[-1] = 0;
      
  t_start = time.time()    
  Np=200
  relax = RelaxDiffusion(np.zeros([Np]))
  n = relax.relax(err=1e-5,nu=0.5)
  t_end = time.time()    
  print("Durtation (s): ",t_end-t_start)
  print("No of iterations: ",n) 
  relax.plot()             
  plt.show()
