import numpy as np
import matplotlib.pyplot as plt
import relax_jacobi_1d as rj1d

class RelaxGS1D(rj1d.RelaxJacobi1D):
  """ A class to solve F(v)=0, where F is a differential
      operator acting on the vector 'v', using Gauss Seidel relaxation."""

  def __init__(self, v0):
    """
      : param v0         : initial condition as an array or a list
    """
    super().__init__(v0) # Parent class initialiser
  
  def relax_1_step(self, nu=0.5):
    """ Perform a single Jacobi relaxation iteration.
    
      : param nu : relaxation parameter.
      : return   : the largest update.
    """
    w = np.array(self.v)
    dvmax = 0
    for i in range(1, self.Np-1):
      dv = nu*self.F(self.v, i)
      self.v[i] += dv
      if(np.fabs(dv) > dvmax) : dvmax = np.fabs(dv)
      
    return(dvmax)


# Tests follow; only run when not importing the module.

if __name__ == "__main__":

  class RelaxDiffusion(RelaxGS1D):
    """ A class to relax to static solutions of the diffusion equation. """
    def F(self, v, i):
      """ The diffusion equation
        : param v : the function function v
        : param i : index of the equation to evaluate
      """
      return((v[i+1]+v[i-1]-2*v[i])) 

    def boundary(self):
      """ Enforce the boundary conditions. 
          Left: 1 (large pool). Right 0 (empty pool)
      """
      self.v[0] = 1
      self.v[-1] = 0;
      
    
  Np=200
  relax = RelaxDiffusion(np.zeros([Np]))
  n = relax.relax(1e-5)
  print("No of iterations: ",n) 
  relax.plot()             
  plt.show()
