def calcDistance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

print(calcDistance(2, 3, 1.4, 4) <= 1.5)


class Point():

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)
    
    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)

    
    def displayPoint(self):
        print("({}, {})".format(self.x, self.y))

    def getDistTo(self, point):
        return