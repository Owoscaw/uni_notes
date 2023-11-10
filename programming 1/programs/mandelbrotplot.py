from matplotlib import pyplot as plt
import random as r

def is_mandelbrot(c):
    z = c
    for niter in range(1000): # 1000 is 'forever'
        z = z*z + c
        if abs(z) > 500:      # |z| > 500 goes to infinity
            return False
    return True

def genVals(n):
    cNums = [complex(r.random()*3-2, r.random()*2-1) for i in range(n)]
    cBrot = [i for i in cNums if is_mandelbrot(i)]
    return [[i.real for i in cBrot], [i.imag for i in cBrot]]

def plotMandelbrot(n):

    XYVals = genVals(n)
    plt.plot(XYVals[0], XYVals[1], "r+")
    plt.show()

plotMandelbrot(100000)