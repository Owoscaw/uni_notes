from math import pi, sin
from matplotlib import pyplot as plt

# The next five lines are the part of the program which does the real
# work. But don't try to understand them for now.
def plot_function(f, startx, endx, nx):
    deltax = (endx-startx)/(nx-1)
    xlst = [startx + i*deltax for i in range(nx)]
    ylst = [f(x) for x in xlst]
    plt.plot(xlst, ylst, '-xr')
    plt.axvline(x=pi/2, color="r", linestyle="dashed")
    plt.axvline(x=5*pi/2, color="r", linestyle="dashed")
    plt.axvline(x=3*pi/2, color="g", linestyle="dashed")
    plt.axvline(x=7*pi/2, color="g", linestyle="dashed")
    plt.xlabel("x")
    plt.ylabel("f(x)=sin(x)")
    plt.xticks([pi*i/2 for i in range(0, 8)], labels=[str(0.5*i) + "π" for i in range(0, 8)])
    plt.title("f(x)=sin(x)")
    plt.show()

# The next three lines define the Python version of the mathematical
# function for which the plot will be drawn
def my_fun(x):
    y = sin(x)
    return y


# The next line actually causes the plot to be drawn
plot_function(my_fun, 0, 4*pi, 200)

