#ax + by + c = 0 to (x1,y1)
def distToLine(a,b,c,x1,y1):
    shortX = (-(b**2)*x1 + a*c + a*b*y1)/(a**2+b**2)
    shortY = (a*(b**2)*x1 - (a**2)*c - (a**2)*b*y1 - (a**2)*c - (b**2)*c)/((a**2)*b + b**3)
    return ((shortX - x1)**2 + (shortY - y1)**2)**0.5

#y=mx+c
def lineIntersection(m1, c1, m2, c2):
    intersectionX = (c2-c1)/(m1-m2)
    intersectionY = m1*intersectionX + c1

    return (intersectionX, intersectionY)

#(y-y1)**2 + (x-x1)**2 = r**2 to (x0,y0)
def distToCircle(x0, y0, x1, y1, r):
    distToCentre = ((x0 - x1)**2 + (y0 - y1)**2)**0.5
    return abs(distToCentre - r)

print(distToLine(1,1,0,0,0))
print(lineIntersection(1,0,-1,0))
print(distToCircle(-1,-1,0,0,1))