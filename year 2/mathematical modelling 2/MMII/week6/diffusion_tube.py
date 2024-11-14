import numpy as np
import matplotlib.pyplot as plt
import relax_GS_1d as gs1d

class diffusion_tube(gs1d.RelaxGS1D):
    D = []

    def __init__(self, v0, dMin, dMax):
        super().__init__(v0)
        
        self.D = np.linspace(dMin, dMax, len(v0))

    def F(self, v, i):
        return self.D
    
    def boundary(self):
        self.v[0] = 1
        self.v[-1] = 0

if __name__ == "__main__":
    Np = 200
    relax = diffusion_tube(np.zeros([Np]) ,1.,2.)
    n = relax.relax(1e-9 ,0.5)
    print("No of iterations: ",n)
    relax.plot()
    plt.savefig("diff -tube.pdf")
    plt.show()