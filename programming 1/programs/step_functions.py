from matplotlib import pyplot as plt
import numpy as np

def nth_partition_of_b(n, b, c):
    pVals = [b**(i/n) for i in range(0,n+1)]

    for i in range(0,len(pVals)-1):
        plt.plot([pVals[i], pVals[i+1]], [b**((i*c)/(n-1))]*2, "blue")

    xVals = np.linspace(1,b,1000)
    plt.plot(xVals, [x**c for x in xVals], "red")
    plt.pause(0.001)
    plt.clf()

def increase_partition(limit, b, c):
    plt.ion()
    for i in range(1,limit):
        nth_partition_of_b(i+1, b, c)
        
    



increase_partition(5000, 5, 2)