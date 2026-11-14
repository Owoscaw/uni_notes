import numpy as np
import pygame

class Film:

    def __init__(self, refIndex=1.0, dt=1.0, size=500, dx=1.0):
        self.refIndex = refIndex
        self.dt = dt
        self.dx = dx

        self.x, self.y = np.meshgrid(np.arange(size, dtype=np.float32),
                                      np.arange(size, dtype=np.float32),
                                      indexing="ij")
        
        self.u = np.zeros((size,size), dtype=np.float32)
        self.v = np.zeros((size,size), dtype=np.float32)
        self.h = np.zeros((size,size), dtype=np.float32)

    def _advect(self, func):
        # return \nabla\cdot(func\underline{v})

        f = (
            func(self.x, self.y)
            if callable(func)
            else np.asarray(func)
        )

        return  np.gradient(f*self.u, self.dx, axis=0) + np.gradient(f*self.v, self.dx, axis=1)

    def update(self):

        # update momentum equation first
        self.u, self.v = self.dt*(-9.81*np.gradient(self.h) - (self.u, self.v)*self._advect(1))

if __name__ == "__main__":
    test = Film()
    test.update()