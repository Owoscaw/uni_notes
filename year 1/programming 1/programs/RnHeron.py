
def areaN(p1, p2, p3):
    dim = len(p1)
    vec12 = [p2[i] - p1[i] for i in range(dim)]
    vec23 = [p3[i] - p2[i] for i in range(dim)]
    vec31 = [p1[i] - p3[i] for i in range(dim)]

    lenA = sum([i**2 for i in vec12])
    lenB = sum([i**2 for i in vec23])
    lenC = sum([i**2 for i in vec31])

    semiPerimeter = (lenA + lenB + lenC)/2

    return (semiPerimeter*(semiPerimeter - lenA)*(semiPerimeter - lenB)*(semiPerimeter - lenC))**0.5