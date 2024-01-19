import math as m
import numpy as np
from matplotlib import pyplot as plt 

#task1b
def draw_line(m,c,x0,ell):
    leftPoint = [x0, m*x0+c]
    rightPoint = [x0+ell/((1+m**2)**0.5), m*x0+(m*ell)/((1+m**2)**0.5)+c]
    plt.plot([leftPoint[0], rightPoint[0]], [leftPoint[1], rightPoint[1]])

def draw_line_with_colour(m,c,x0,ell,colour):
    leftPoint = [x0, m*x0+c]
    rightPoint = [x0+ell/((1+m**2)**0.5), m*x0+(m*ell)/((1+m**2)**0.5)+c]
    plt.plot([leftPoint[0], rightPoint[0]], [leftPoint[1], rightPoint[1]], color=colour)

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
    xVals = np.linspace(n-a, n+a, 1000)
    plt.plot(np.concatenate((xVals, xVals[::-1]), axis=0), [m+b*(1-(1/a**2)*(x-n)**2)**0.5 for x in xVals] + [m-b*(1-(1/a**2)*(x-n)**2)**0.5 for x in xVals[::-1]])

#task6b
def draw_tangent(circ, xy, d, thecolour):
    if round((xy[0]-circ[0][0])**2 + (xy[1]-circ[0][1])**2, 2) != round(circ[1]**2, 2):
        raise ArithmeticError
    
    draw_line((circ[0][0]-xy[0])/(xy[1]-circ[0][1]), (xy[0]-circ[0][0])/(xy[1]-circ[0][1])*xy[0]+xy[1], xy[0]-(d/2)*(1/(1+((circ[0][0]-xy[0])/(xy[1]-circ[0][1]))**2))**0.5, d)

def box_the_circle(circ, angle, thecolour):

    tVals = np.linspace(0, 2*m.pi, 1000)
    plt.plot([circ[1]*m.cos(t)+circ[0][0] for t in tVals],[circ[1]*m.sin(t)+circ[0][1] for t in tVals], color=thecolour)

    for i in range(0,4):
        point = [circ[1]*m.cos(i*(m.pi/2)+angle)+circ[0][0],circ[1]*m.sin(i*(m.pi/2)+angle)+circ[0][1]]
        draw_tangent(circ, point, 2*circ[1], thecolour)

#task7
def show_tangent_example():
    draw_circle([[-1,3], 2], "red")
    draw_tangent([[-1,3], 2], [0.2, 4.6], 4, "blue")

#task8b
def xcircles_and_radicalaxis(r, R, c, thecolours):
    draw_circle([[0, 0], r], thecolours[0])
    draw_circle([[c, 0], R], thecolours[1])

    if r > c - R:
        p1 = [(r**2+c**2-R**2)/(2*c), (r**2-((r**2+c**2-R**2)/(2*c))**2)**0.5]
        p2 = [(r**2+c**2-R**2)/(2*c), -(r**2-((r**2+c**2-R**2)/(2*c))**2)**0.5]
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color=thecolours[2])

#task9b
def gencircles_and_radicalaxis(circ1, circ2, thecolours):
    draw_circle(circ1, thecolours[0])
    draw_circle(circ2, thecolours[1])

    distBetweenCentres = ((circ1[0][0]-circ2[0][0])**2+(circ1[0][1]-circ2[0][1])**2)**0.5

    if distBetweenCentres < circ1[1] + circ2[1]:

        #points from task 8b
        p1 = [(circ1[1]**2-circ2[1]**2+distBetweenCentres**2)/(2*distBetweenCentres), (circ1[1]**2-((circ1[1]**2-circ2[1]**2+distBetweenCentres**2)/(2*distBetweenCentres))**2)**0.5]
        p2 = [(circ1[1]**2-circ2[1]**2+distBetweenCentres**2)/(2*distBetweenCentres), -(circ1[1]**2-((circ1[1]**2-circ2[1]**2+distBetweenCentres**2)/(2*distBetweenCentres))**2)**0.5]

        if circ1[0][1] == circ2[0][1]:
            #avoiding division by 0 in case where they lie on a straight line
            rotation = 0
        else:
            rotation = m.atan(abs((circ2[0][1] - circ1[0][1])/(circ2[0][0] - circ1[0][0])))

        #rotating to account for gradient
        rotationMatrix = [[m.cos(rotation),-m.sin(rotation)],[m.sin(rotation),m.cos(rotation)]]

        p1Rotated = [rotationMatrix[0][0]*p1[0]+rotationMatrix[0][1]*p1[1], rotationMatrix[1][0]*p1[0]+rotationMatrix[1][1]*p1[1]]
        p2Rotated = [rotationMatrix[0][0]*p2[0]+rotationMatrix[0][1]*p2[1], rotationMatrix[1][0]*p2[0]+rotationMatrix[1][1]*p2[1]]

        #translating
        offset = [circ1[0][0], circ1[0][1]]
        plt.plot([p1Rotated[0] + offset[0], p2Rotated[0] + offset[0]], [p1Rotated[1] + offset[1], p2Rotated[1] + offset[1]], thecolours[2])


#task10b
def single_bumper(theta, circ, ell, circ_col, line_col):
    draw_circle(circ, circ_col)

    if circ[1]**2 > (m.sin(theta)*circ[0][0] - m.cos(theta)*circ[0][1])**2:
        
        #coordinates of segment intersection
        px = m.cos(theta)*(m.cos(theta)*circ[0][0]+m.sin(theta)*circ[0][1]-(circ[1]**2 - (m.sin(theta)*circ[0][0] - m.cos(theta)*circ[0][1])**2)**0.5)
        py = m.sin(theta)*(m.cos(theta)*circ[0][0]+m.sin(theta)*circ[0][1]-(circ[1]**2 - (m.sin(theta)*circ[0][0] - m.cos(theta)*circ[0][1])**2)**0.5)

        #line reaches circle
        if ell > (px**2 + py**2)**0.5:
            plt.plot([0, px], [0, py], color=line_col)

            remainingEll = ell - (px**2 + py**2)**0.5
            draw_line()
    else:
        draw_line(m.tan(theta), 0, 0, ell)
            


single_bumper(m.pi/4, [[2,4],2], 5, "blue", "red")
plt.gca().set_aspect("equal","box")
plt.show() 