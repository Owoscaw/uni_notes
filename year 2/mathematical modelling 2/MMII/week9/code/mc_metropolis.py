import numpy as np
import math
from matplotlib import pyplot as plt
import random as r

def P(x):
    return math.exp(-x**2)

def f(x):
    return x**2

N  = 1000

xprev = -0.2
xlist =[[xprev , f(xprev)]]
fsum = f(xprev)
Pprev = P(xprev)
dx = 0.5
for i in range(N):
    xnew = xprev + r.uniform(-dx, dx)
    Pnew = P(xnew)

    # Reject if Pnew < Pprev and Metropolis criterion does not hold.
    if Pnew < Pprev and r.random() > Pnew/Pprev:
        xnew = xprev
    xlist.append([xnew ,P(xnew)*f(xnew)])
    xprev=xnew
    Pprev=Pnew
    fsum += f(xnew)

xvals , pfvals = zip(*xlist)

print(fsum/N)

plt.plot(xvals, pfvals, "b.")
plt.show()

hist , bins = np.histogram(xvals , 20)
hist = hist *1.0/N
width = 0.7 * (bins [1] - bins [0])
center = (bins [:-1] + bins [1:]) / 2
plt.bar(center , hist , align='center', width=width)
plt.show()