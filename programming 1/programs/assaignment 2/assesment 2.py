import math as m
import numpy as np
from matplotlib import pyplot as plt 

#task1b
def draw_line(m,c,x0,ell):
    leftPoint = [x0, m*x0+c]
    rightPoint = [x0+ell/((1+m**2)**0.5), m*x0+(m*ell)/((1+m**2)**0.5)+c]
    plt.plot([leftPoint[0], rightPoint[0]], [leftPoint[1], rightPoint[1]])

#task2
def draw_unit_circle(thecolour):
    theta = np.linspace(0, 2*m.pi, 10000)
    plt.plot([m.cos(t) for t in theta], [m.sin(t) for t in theta], color=thecolour)

#task3b
def draw_circle(circ, thecolour):
    theta = np.linspace(0, 2*m.pi, 10000)
    plt.plot([m.cos(t)*circ[1] + circ[0][0] for t in theta], [m.sin(t)*circ[1] + circ[0][1] for t in theta], color=thecolour)

#task4
def show_six_circles_example():
    for j in range(0,6):
        draw_circle([[m.cos(j*(m.pi/3)), m.sin(j*(m.pi/3))], 0.5], "red")

#task5b
def draw_ellipse(n,m,a,b):
    xVals = [np.linspace(n-a, n+a, 1000)]
    plt.plot(xVals + xVals, [m+(b/a)*((a/b)**2-(x-n)**2)**0.5 for x in xVals] + [m-(b/a)*((a/b)**2-(x-n)**2)**0.5 for x in xVals])

#task6b
def draw_tangent(circ, xy, d, thecolour):
    if round((xy[0]-circ[0][0])**2 + (xy[1]-circ[0][1])**2, 2) != round(circ[1]**2, 2):
        raise ArithmeticError
    
    tVals = np.linspace(0,2*m.pi,10000)
    draw_line((circ[0][0]-xy[0])/(xy[1]-circ[0][1]), (xy[0]-circ[0][0])/(xy[1]-circ[0][1])+xy[1], xy[0], d/2)
    draw_line((circ[0][0]-xy[0])/(xy[1]-circ[0][1]), (xy[0]-circ[0][0])/(xy[1]-circ[0][1])+xy[1], xy[0]-(d/2)*(1/(1+((circ[0][0]-xy[0])/(xy[1]-circ[0][1]))**2))**0.5, d/2)

    plt.plot([circ[1]*m.cos(t)+xy[0] for t in tVals],[circ[1]*m.sin(t)+xy[0] for t in tVals])

    

draw_tangent([[1, 1], 1], [1, 1], 2, "red")
plt.gca().set_aspect("equal","box")
plt.show()