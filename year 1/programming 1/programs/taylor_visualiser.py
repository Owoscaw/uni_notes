from matplotlib import pyplot as plt
import math as m
# from math import *
import sympy as sp

def showplots(funcs, start, end, detail):

    xVals = [start + i*((end-start)/detail) for i in range(detail)]
    yValList = [[func(xVal) for xVal in xVals] for func in funcs]

    plt.plot(xVals, yValList[0], linestyle="-", color="red")
    for i in range(1, len(funcs)):
        plt.plot(xVals, yValList[i], linestyle="--")
    
    plt.axhline(y=0, color="blue", ls="-")
    plt.axvline(x=0, color="blue", ls="-")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.ylim(-max(start,end), max(start,end))
    plt.show()
    plt.ion()

def get_nth_derivative(func, n):
    x = sp.Symbol("x")
    func_prime_n = func(x).evalf()

    for i in range(n):
        func_prime_n = func_prime_n.diff(x)

    return sp.lambdify(x, func_prime_n)

def get_taylor_coefs(func, n, a):
    diff_over_fact = [get_nth_derivative(func, i)(a)/m.factorial(i) for i in range(n)]
    expansion = [sum([(-a)**(j-i)*m.comb(j, i) if i <= j else 0.0 for j in range(n)]) for i in range(n)]
    return [diff_over_fact[i]*expansion[i] for i in range(n)]

def get_taylor_func(func, n, a):
    coefs = get_taylor_coefs(func, n, a)
    x = sp.Symbol("x")

    if len(coefs) == 0:
        taylor_string = "0*x"
    else:
        taylor_string = "{}*x**{}".format(coefs[0], 0)
        for i in range(1, n):
            taylor_string += "+{}*x**{}".format(coefs[i], i)

    sp_func = sp.sympify(taylor_string)
    return sp.lambdify(x, sp_func)

def test_func(x):
    return 1

def show_taylor_to_n(func, n, a, start, end, detail):
    showplots([func] + [get_taylor_func(func, i, a) for i in range(1, n)], start, end, detail)

show_taylor_to_n(sp.tan, 10, 1, -m.pi, m.pi, 1000)