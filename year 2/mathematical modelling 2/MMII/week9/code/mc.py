import numpy as np
import math
from matplotlib import pyplot as plt

def P(x):
    return math.exp(-x**2)

def f(x):
    return x**2

N  = 100
xL = -10.  # 10 is close enough to infinity
xR =  10.

xvals = np.linspace(xL, xR, N)
fvals = []
prodSum  = 0
PSum = 0
for x in xvals:
    prod = f(x)*P(x)
    fvals.append(prod)
    prodSum += prod
    PSum += P(x)

print("Integral of f(x)P(x):{}\nIntegral of P(x):{}\nIntegral I:{}".format(prodSum, PSum, prodSum/PSum))

plt.plot(xvals, fvals, "b.")
plt.show()
