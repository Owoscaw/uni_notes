import numpy as np
import matplotlib.pyplot as plt

import diffusion_tube as dt

def avT(diff):
    """ Compute the average value of T
        diff : an object of type diffusion.
        diff.v are all the values of T along the segment
        : return : average <T> and standard deviation <(T-<T>)**2>
    """
    Var = 0
    for i in range(len(diff.v)):
      Tav = 0                                # Average value of T 
      for j in range(len(diff.v)):
        Tav += diff.v[j]/len(diff.v)
      Var += (diff.v[i]- Tav)**2/len(diff.v) # <(x-<x>)^2>
    return(Tav, Var)  

# We create an array of 500 nodes to solve the diffusion equation 
Np=500
difftube = dt.diffusion_tube(np.zeros([Np]),1.,2.)
# and relax the solution
n = difftube.relax(1e-9,0.5)

# We compute the temperature relative to the average temperature: T/<T> 
Tvals = np.zeros([len(difftube.v)], dtype=np.float64)
for i in range(len(Tvals)):
  Tvals[i] = difftube.v[i]/avT(difftube)[0]

print("<T>=", avT(difftube)[0], "<(T-<T>)**2>=", avT(difftube)[1])

plt.plot(Tvals, "b-")
plt.ylabel("T", fontsize=22)
plt.show()
