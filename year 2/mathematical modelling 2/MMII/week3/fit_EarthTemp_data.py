import numpy as np
import math as m
import matplotlib.pyplot as plt
import scipy.optimize 

gdata = np.genfromtxt("MMII\week3\code\TA.txt", delimiter=",", comments="#")
years = gdata[:,0]
deltaT = gdata[:,1]
index = np.where(years == 1960)[0]
years = years[int(index):]
deltaT = deltaT[int(index):]

def func(Y, a, b):
    return a + b*Y

popt, pcov = scipy.optimize.curve_fit(func, years, deltaT, p0=[1, 1])

criticalYear = m.floor((1.5 - popt[0])/popt[1])
print("a, b = ", popt)
print("1.5 degree will be reached in ", criticalYear)

plt.plot(years, deltaT, "b+")
plt.plot(years, func(years, *popt), "r--")
plt.show()
