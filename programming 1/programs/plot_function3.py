from math import pi, sin, cos
from matplotlib import pyplot as plt

# The next five lines are the part of the program which does the real
# work. But don't try to understand them for now.
def plot_function(f, startx, endx, nx):
    deltax = (endx-startx)/(nx-1)
    xlst = [startx + i*deltax for i in range(nx)]
    ylst = [f(x) for x in xlst]
    plt.plot(xlst, ylst, '-+')
    plt.show()

# The next three lines define the Python version of the mathematical
# function for which the plot will be drawn
def q(x):
    return 2 + 3*x + 4*x**2

# The next line actually causes the plot to be drawn
plot_function(q, -4, 4, 200)

