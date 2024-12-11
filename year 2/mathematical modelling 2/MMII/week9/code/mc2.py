import numpy as np
import math
from matplotlib import pyplot as plt
import random as r
import copy

def P(x):
    return math.exp(-x[0]**2 - x[1]**2)

def f(x):
    return x[0]**2 + x[1]**2

N  = 1000

xprev = [-0.2, -0.2]
xlist =[[xprev , f(xprev)]]
fsum = f(xprev)
Pprev = P(xprev)
dx = 0.5
for i in range(N):
    xnew = [xprev[0] + r.uniform(-dx, dx), xprev[1] + r.uniform(-dx, dx)]
    Pnew = P(xnew)

    # Reject if Pnew < Pprev and Metropolis criterion does not hold.
    if Pnew < Pprev and r.random() > Pnew/Pprev:
        xnew = copy.copy(xprev)
    xlist.append([xnew ,P(xnew)*f(xnew)])
    xprev = copy.copy(xnew)
    Pprev = copy.copy(Pnew)
    fsum += f(xnew)

xvals , pfvals = zip(*xlist)

print(fsum/N)

xpts = [xval[0] for xval in xvals]
ypts = [xval[1] for xval in xvals]

plt.plot(xpts, ypts, "bo", markersize=0.1)
plt.show()

# hist , bins = np.histogram(xvals , 20)
# hist = hist *1.0/N
# width = 0.7 * (bins [1] - bins [0])
# center = (bins [:-1] + bins [1:]) / 2
# plt.bar(center , hist , align='center', width=width)
# plt.show()