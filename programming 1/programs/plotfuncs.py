from matplotlib import pyplot as plt
import numpy as np

def plot_functions(funcs, xVals):

    for func in funcs:
        plt.plot(func(xVals))
    plt.axhline(y=0, color="blue", ls="--")
    plt.axvline(x=0, color="blue", ls="--")
    plt.show()

def derivative(f, h):
    return lambda x: (f(x+h)-f(x))/h

def nth_derivative(f, h, n):
    if n > 0:
        diff = derivative(f, h)
        for i in range(n-1):
            diff = derivative(diff, h)
        return diff
    return f

plot_functions([nth_derivative(lambda x: (np.e-1)**x, 0.001, n) for n in range(0,4)], np.linspace(0, 2*np.pi, 10000))