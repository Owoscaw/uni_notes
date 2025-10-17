from matplotlib import pyplot as plt
import math as m

def showplots(funcs, start, end, detail):

    xVals = [start + i*((end-start)/detail) for i in range(detail)]
    yValList = [[func(xVal) for xVal in xVals] for func in funcs]
    lineType = ["-r","-b","+r","+b"]

    for i in range(len(funcs)):
        plt.plot(xVals, yValList[i], lineType[i])
    
    plt.axhline(y=0, color="blue", ls="--")
    plt.show()


def sin_squared(x):
    return (m.sin(x))**2

def e_to_the_x(x):
    return m.e**x

def x_to_the_n(x, n=10):
    return x**n

def divisors_of_x(x):
    return sum([i for i in range(1,int(x)//2+1) if int(x)%i == 0 ])

def fib(x):
    return (1/m.sqrt(5))*(((1+m.sqrt(5))/2)**int(x)-((1-m.sqrt(5))/2)**int(x))

def fib_n_plus_one_over_fib_n(x):
    return fib(x+1)/fib(x)

#showplots([sin_squared, m.cos], 0, 4*m.pi, 50)
#showplots([e_to_the_x], 0, 5, 100)
#showplots([x_to_the_n], 0, 1, 100)
#showplots([divisors_of_x], 0, 100, 100)
showplots([fib_n_plus_one_over_fib_n], 1, 100, 100)


    