from code.ode_euler import ODE_Euler
import numpy as np
class Schaefer(ODE_Euler):

    def __init__(self, N, dt, t0, Y):

        super().__init__(N, dt, t0)
        self.Y = Y

    def F(self, t, N):
        return N*(1-N) - self.Y

if __name__ == "__main__":

    YVals = np.linspace(0,0.25*(1-0.25),5)

    for Y in YVals:
        pop = Schaefer(0.25, 0.01, 0, Y)
        pop.R = -0.5     # We change the value of R
        pop.iterate(20)  # We perform 20 steps of integration
        pop.plot()       # and display the result

