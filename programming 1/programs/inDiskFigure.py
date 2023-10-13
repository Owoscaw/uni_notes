from radius import Point, inDisk, inIntersection
from matplotlib import pyplot as plt
import random as r

point2 = Point(1/3, 1/3)
point3 = Point(2/3, 2/3)

circ1 = plt.Circle((point2.x, point2.y), 1/3, fill=False)
circ2 = plt.Circle((point3.x, point3.y), 1/3, fill=False)

axes = plt.gca()
axes.add_patch(circ1)
axes.add_patch(circ2)
axes.set_aspect(1)
plt.plot(0.5, 0.5)
plt.ion()

while True:
    rPoint = Point(r.random(), r.random())
    colour = "black"

    if inIntersection(point2, 1/3, point3, 1/3, rPoint):
        colour = "green"
    elif inDisk(point2, rPoint, 1/3):
        colour = "yellow"
    elif inDisk(point3, rPoint, 1/3):
        colour = "blue"

    plt.plot(rPoint.x, rPoint.y, "+", color=colour)
    plt.pause(0.0001)


