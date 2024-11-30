import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import sys
import scipy.optimize
from scipy.io import wavfile
import matplotlib
import matplotlib.cm as cm
import math
import random as rnd
import timeit
import time
import pylab 
import struct
from sympy import *
from scipy import linalg
##########################################################
# Spyder configuration (on windows):
#  Tools->Preferences->IPython console-> Graphics
#   Support fro graphics : Activate Support
#   Graphics Backend : Qt5
#   Inline backend : format PNG  
##########################################################

print("So far so good, all the modules have been loaded!")
print("We now try to do some dynamic graphics")

Nturns = 4
theta_max = Nturns*2*np.pi
N_theta = 1000
dtheta= theta_max/N_theta
angles = np.linspace(dtheta, theta_max, N_theta-1)

# prepare graphics
plt.close("all")
live = plt.figure(figsize=(5, 5))
plt.axis('square')
plt.ion()
plt.axis('off')
plt.show()
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

def f(th):
    x = A1*np.sin(th)+A2*np.cos(R*th)
    y = A1*np.cos(th)+A2*np.sin(R*th) 
    return(x,y)

A1 = 1
A2 = 0.2
R = 7.25
xlast, ylast = f(0)

for th in angles:
    xnew, ynew = f(th)
    #th = np.linspace(0,n*dtheta,n+1)
    #x = A1*np.sin(th)+A2*np.cos(R*th)
    #y = A1*np.cos(th)+A2*np.sin(R*th) 
    plt.plot([xlast, xnew],[ylast, ynew], "b-")
    plt.draw()
    plt.pause(0.01)
    xlast = xnew
    ylast = ynew
    #plt.axis('square')
plt.show()

input("Press Enter to stop: ")
