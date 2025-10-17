from cyclotron import *
import numpy as np
import matplotlib.pyplot as plt
import sys

x_off = -0.02        # To better center the spiral
x0= -4.56901e-2 +x_off  # Initial x position
y0=0.0               # Initial y position
vx0=0.0              # Initial speed along the x axis
vy0= 4.377518e6         # Initial speed along the y axis
dt = 1e-11           # Time step in second. Much smaller than the frequency
t0 = 0
tmax = 5e-7
B = 1
dV = 2.1168e6 + 100# 2MV
dTarget = 1e6
eps = 1e-3

while dTarget > eps:
    dV -= 100
    ode = CyclotronRK4([x0, y0, vx0, vy0], dt, t0, B, dV) 
    ode.iterate_max()
    dTarget = np.sqrt((2 - ode.V[0])**2 + (1 - ode.V[1])**2)
    print("potential: {}\nx:{}\ny:{}\nDistance to target:{}".format(dV, ode.V[0], ode.V[1], dTarget))

print("=============================")
v0 = np.sqrt(vx0**2 + vy0**2)
vF = np.sqrt(ode.V[2]**2 + ode.V[3]**2)
print("Initial speed:{}\nFinal speed:{}\nFactor:{}".format(v0, vF, vF/v0))

plt.axes().set_aspect('equal') # Ensure same unit along x and y
plt.xlabel("x", fontsize=22) # Set horizontal label 
plt.ylabel("y", fontsize=22) # Set vertical label   
ode.plot(2, 1, "b-")         # Plot y(x) in blue
ode.draw_Ds()                # Draw the 2 Ds on toip of the trajectory
#plt.savefig("cyclotron.pdf")
plt.show()

