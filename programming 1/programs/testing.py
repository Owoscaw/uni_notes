from matplotlib import pyplot as plt
import math as m

def showplots(funcs, start, end, detail):

    xVals = [start + i*((end-start)/detail) for i in range(detail)]
    yValList = [[func(xVal) for xVal in xVals] for func in funcs]
    lineType = ["-r","-b","+r","+b"]

    for i in range(len(funcs)):
        plt.plot(xVals, yValList[i], lineType[i])
    
    plt.axhline(y=0, color="blue", ls="--")
    plt.xlabel("x")
    plt.ylabel("cos(x^3)")
    plt.show()

def cosine_x_cubed(x):
    return m.cos(x**3)

showplots([cosine_x_cubed], -0.5, 4, 10000)