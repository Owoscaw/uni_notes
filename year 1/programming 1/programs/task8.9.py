from matplotlib import pyplot as plt
import numpy as np

def derivative(f, x, h):
    return (f(x+h)-f(x))/h

def h(x):
    return np.e**np.sin(x)/(x**3+1)

xVals = np.linspace(0, 2*np.pi, 100)
plt.plot(h(xVals))
plt.plot(derivative(h, xVals, 0.0000001))
plt.axhline(y=0, color="blue", ls="--")
plt.axvline(x=0, color="blue", ls="--")
plt.show()