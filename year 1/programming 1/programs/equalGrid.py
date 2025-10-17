
def grid(a,b,npts):
    spacedPoints = list(range(npts))
    factoredPoints = [i/(b-a) for i in spacedPoints]
    rangedPoints = [i + a for i in factoredPoints]

    return [(i/(b-a) + a) for i in range(npts)]

print(grid(-1,1,5))