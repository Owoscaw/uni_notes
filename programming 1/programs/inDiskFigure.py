from radius import Point, inDisk, inIntersection
from matplotlib import pyplot as plt
import random as r

point1 = Point(0.5, 0.5)
point2 = Point(1/3, 1/3)
point3 = Point(2/3, 2/3)

print(inIntersection(point2, 1/3, point3, 1/3, point1))

circ1 = plt.Circle((point2.x, point2.y), 1/3, fill=False)
circ2 = plt.Circle((point3.x, point3.y), 1/3, fill=False)

