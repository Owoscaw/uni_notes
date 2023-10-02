class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)
    
    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)
    
    def displayPoint(self):
        print("({}, {})".format(self.x, self.y))

    def getDistTo(self, point):
        distVector = self - point
        return (distVector.x**2 + distVector.y**2)**0.5
    
def closeEnough(point1, point2, radius):
    return point1.getDistTo(point2) <= radius

point1 = Point(2,3)
point2 = Point(1.4,4)

print(closeEnough(point1, point2, 1.5))