from matplotlib import pyplot as plt
import numpy as np
import time as t

def nth_partition_of_b(n, b, c):
    pVals = [b**(i/n) for i in range(0,n+1)]

    for i in range(0,len(pVals)-1):
        plt.plot([pVals[i], pVals[i+1]], [b**((i*c)/(n-1))]*2)

def increase_partition(limit, b, c):
    xVals = np.linspace(1,b,1000)
    plt.plot(xVals, [x**c for x in xVals])

    plt.ion()
    for i in range(1,limit):
        nth_partition_of_b(i+1, b, c)
        t.sleep(1000)

    plt.show()


increase_partition(10, 5, 2)