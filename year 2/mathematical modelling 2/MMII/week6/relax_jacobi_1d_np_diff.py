import numpy as np
import matplotlib.pyplot as plt
from relax_jacobi_1d_np import RelaxJacobi1D_np
import time

class RelaxDiffusion(RelaxJacobi1D_np):
    """ A class to relax to static solutions of the diffusion equation. """
    def F(self, v):
       
       result = np.roll(v, 1) + np.roll(v, -1) - 2*v
       return result[1:-1]
      
    

    def boundary(self):
      """ Enforce the boundary conditions. 
          Left: 1 (large pool). Right 0 (empty pool)
      """
      self.v[0] = 1
      self.v[-1] = 0
      
t_start = time.time()    
Np=200
relax = RelaxDiffusion(np.zeros([Np]))
n = relax.relax(err=1e-5,nu=0.5)
t_end = time.time()    
print("Durtation (s): ",t_end-t_start)
print("No of iterations: ",n) 
relax.plot()             
plt.show()
