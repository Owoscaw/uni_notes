
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
from matplotlib.colors import LogNorm

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.01
G = 6.67*10e-11
r = 1
M_S = 1.99*10e30
M_E = 5.97*10e24
pi_S = M_S/(M_S + M_E)
pi_E = M_E/(M_S + M_E)

x_E = np.geomspace(pi_S*r-5*delta, pi_S*r+5*delta, 1000)
x_S = np.geomspace(-pi_E*r-5*delta, 5*delta-pi_E*r, 500)
fx = np.unique(np.concatenate([x_E, x_S]))
fy = np.arange(-1.0, 1.0, delta)
X, Y = np.meshgrid(fx, fy)

fig, ax = plt.subplots(1,1)

def potential(x,y):
    D_S = M_S/np.sqrt((x + pi_E*r)**2 + y**2 + delta)
    D_E = M_E/np.sqrt((x - pi_S*r)**2 + y**2 + delta)
    return -G*(D_S + D_E)

Z = potential(X,Y)

CS = ax.contour(X, Y, Z)
plt.show()