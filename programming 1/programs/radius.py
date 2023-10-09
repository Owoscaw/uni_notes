class Point():

    def __init__(self, x=0, y=0):
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
    
def inDisk(point1, point2, radius):
    return point1.getDistTo(point2) <= radius

def inIntersection(centre1, radius1, centre2, radius2, point):
    return (centre1.getDistTo(point) <= radius1) and (centre2.getDistTo(point) <= radius2)
