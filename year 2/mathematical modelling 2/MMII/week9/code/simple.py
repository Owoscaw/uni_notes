import numpy as np
import math

def P(x):
    return math.exp(-x**2)/math.sqrt(math.pi)

def f(x):
    return x**2

N  = 100
xL = -10.  # 10 is close enough to infinity
xR =  10.

xvals = np.linspace(xL, xR, N)
fsum  = 0
for x in xvals:
    fsum += f(x)*P(x)

print(fsum/N*(xR-xL))
