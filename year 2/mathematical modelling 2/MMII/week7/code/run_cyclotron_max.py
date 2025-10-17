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
dV = 2e6 # 2MV

ode = CyclotronRK4([x0, y0, vx0, vy0], dt, t0, B, dV) 

ode.iterate_max()

plt.axes().set_aspect('equal') # Ensure same unit along x and y
plt.xlabel("x", fontsize=22) # Set horizontal label 
plt.ylabel("y", fontsize=22) # Set vertical label   
ode.plot(2, 1, "b-")         # Plot y(x) in blue
ode.draw_Ds()                # Draw the 2 Ds on toip of the trajectory
#plt.savefig("cyclotron.pdf")
plt.show()

