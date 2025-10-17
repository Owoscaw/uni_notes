import numpy as np
import matplotlib.pyplot as plt

import diffusion_tube as dt

def avT(diff):
    """ Compute the average value of T
        diff : an object of type diffusion.
        diff.v are all the values of T along the segment
        : return : average <T> and standard deviation <(T-<T>)**2>
    """

    Tav = sum(diff.v)/len(diff.v)
    Var = sum((diff.v - Tav)**2)/len(diff.v)
    return(Tav, Var)  

# We create an array of 500 nodes to solve the diffusion equation 
Np=500
difftube = dt.diffusion_tube(np.zeros(Np),1.,2.)

# and relax the solution
n = difftube.relax(1e-5,0.5)

# We compute the temperature relative to the average temperature: T/<T> 
diffAvg, diffVar = avT(difftube)
Tvals = difftube.v/diffAvg

print("<T>=", diffAvg, "<(T-<T>)**2>=", diffVar)

plt.plot(Tvals, "b-")
plt.ylabel("T", fontsize=22)
plt.show()
