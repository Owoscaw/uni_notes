def dist2(x1, y1, x2, y2):
    dx = x1-x2
    dy = y1-y2
    dist = (dx**2+dy**2)**0.5
    return dist

def perimeter4(x1, y1, x2, y2, x3, y3, x4, y4):
    l12 = dist2(x1, y1, x2, y2)
    l23 = dist2(x2, y2, x3, y3)
    l34 = dist2(x3, y3, x4, y4)
    l41 = dist2(x4, y4, x1, y1)
    total = l12 + l23 + l34 + l41
    return total

def area3(x1,y1,x2,y2,x3,y3):
    l12 = dist2(x1,y1,x2,y2)
    l23 = dist2(x2,y2,x3,y3)
    l31 = dist2(x3,y3,x1,x1)

    semiPerimeter = (l12 + l23 + l31)/2
    return (semiPerimeter*(semiPerimeter - l12)*(semiPerimeter - l23)*(semiPerimeter - l31))**0.5


print(perimeter4(0,0,3,0,3,1,0,5))
print(area3(0,0,0,1,1,0))
 
