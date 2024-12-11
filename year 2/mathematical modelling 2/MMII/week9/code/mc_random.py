import numpy as np
import math
from matplotlib import pyplot as plt
import random as r

def P(x):
    return math.exp(-x**2)

def f(x):
    return x**2

N  = 1000
xL = -10.  # 10 is close enough to infinity
xR =  10.

xvals = np.array([r.random()*(xR - xL) + xL for n in range(N)])
fvals = []
prodSum  = 0
PSum = 0
for x in xvals:
    prod = f(x)*P(x)
    fvals.append(prod)
    prodSum += prod
    PSum += P(x)

print("Integral of f(x)P(x):{}\nIntegral of P(x):{}\nIntegral I:{}".format(prodSum, PSum, prodSum/PSum))

#plt.plot(xvals, fvals, "b.")

hist , bins = np.histogram(xvals , 20)
hist = hist *1.0/N
width = 0.7 * (bins [1] - bins [0])
center = (bins [:-1] + bins [1:]) / 2
plt.bar(center , hist , align='center', width=width)
plt.show()