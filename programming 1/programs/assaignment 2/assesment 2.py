import math as m
import numpy as np
from matplotlib import pyplot as plt 

#task1b
def draw_line(m,c,x0,ell):
    leftPoint = [x0, m*x0+c]
    rightPoint = [x0+ell/((1+m**2)**0.5), m*x0+m/((1+m**2)**0.5)+c]
    plt.plot([leftPoint[0], rightPoint[0]], [leftPoint[1], rightPoint[1]])

#task2
def draw_unit_circle(thecolour):
    theta = np.linspace(0, 2*m.pi, 10000)
    plt.plot([m.sin(t) for t in theta], [m.cos(t) for t in theta], color=thecolour)

draw_unit_circle("red")
plt.gca().set_aspect("equal","box")
plt.show()