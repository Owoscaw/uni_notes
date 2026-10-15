import matplotlib.pyplot as plt
import time as t
import numpy as np
import scipy as sci
from matplotlib.animation import FuncAnimation

class Surface:

    def __init__(self, J, gamma, res):
        self.J = J
        self.gamma = gamma
        self.N = 2**res

        self.k_grid = np.linspace(-np.pi*self.N/2, np.pi*self.N/2, self.N, endpoint=False)
        self.dk = self.k_grid[1] - self.k_grid[0]

        x_grid = np.fft.fftshift(np.fft.fftfreq(self.N, d=self.dk/(2*np.pi)))

        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(x_grid, np.zeros(self.N))
        self.data_ref = self.line.get_ydata()

        self.ax.set_xlim(-1.0,1.0)
        self.ax.set_ylim(-1.0,1.0)
        self.ax.set_aspect("equal", adjustable="box")
        self.ax.grid(True, which='both')
        self.ax.axhline(y=0, color='k')
        self.ax.axvline(x=0, color='k')

    def F(self, k, t):
        k_safe = np.where(np.abs(k) < 1e-3, 1e-3, np.abs(k))
        omega = np.sqrt(self.gamma * k_safe**3)

        k_max = np.max(self.k_grid)
        cutoff_width = k_max * 0.05
        lpf = np.exp(-(k/cutoff_width)**2)

        return self.J * np.sin(omega * t) * lpf / (np.sqrt(self.gamma * k_safe))

    def update(self, frame):
        t = frame * 0.05

        F_k = self.F(self.k_grid, t)

        F_k_shifted = np.fft.ifftshift(F_k)

        f_x_raw = np.fft.ifft(F_k_shifted) * self.N * self.dk / (2*np.pi)

        f_x_centered = np.fft.fftshift(f_x_raw)

        self.data_ref[:] = np.real(f_x_centered)

        self.line.set_ydata(self.data_ref)

        self.line.recache()

        return self.line,

            
    def run(self):
        self.ani = FuncAnimation(self.fig, self.update, frames=200, interval=25, blit=True)
        

if __name__ == "__main__":
    test = Surface(0.1, 1, 8)
    test.run()
    plt.show()