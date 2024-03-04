from matplotlib import pyplot as plt

def show_nth_partition_of_b(n, b, c):
    xVals = [b**(i/n) for i in range(0,n+1)]

    for i in range(0,len(xVals)-1):
        plt.plot([xVals[i], xVals[i+1]], [b**((i*c)/(n-1))]*2)

    plt.show()

show_nth_partition_of_b(3,5,2)