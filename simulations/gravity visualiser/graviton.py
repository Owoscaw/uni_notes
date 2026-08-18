
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.01
fx = np.arange(-1.0, 1.0, delta)
fy = np.arange(-1.0, 1.0, delta)
X, Y = np.meshgrid(fx, fy)

G = 1 #6.67*10e-11
r = 0.75
M_S = 10 #1.99*10e30
M_E = 1 #5.97*10e24
pi_S = M_S/(M_S + M_E)
pi_E = M_E/(M_S + M_E)

fig, ax = plt.subplots(1,1)

def potential(x,y):
    D_S = M_S/np.sqrt((x + pi_E*r)**2 + y**2)
    D_E = M_E/np.sqrt((x - pi_S*r)**2 + y**2)
    return -G*(D_S + D_E)

Z = potential(X,Y)
CS = ax.contour(X, Y, Z, [-n*10 for n in range(0,10)].reverse())
plt.show()
