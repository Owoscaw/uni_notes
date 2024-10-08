import math as m
import sympy as sp

def is_close_to(a,b,eps):
    return abs(a-b)<eps

def find_a_b(func, ran):
    a = ran
    b = -ran

    for i in range(ran):
        if m.copysign(1, func(a)) != -m.copysign(1, func(b)):
            b -= 1
        else:
            break

    return [a,b]


def find_root_bisection(func,a,b,eps):
    m = 0
    while not is_close_to(a,b,eps):
        m = (a+b)/2
        if func(m) > 0:
            a = m
        else:
            b = m

    return [m,a,b]

def get_newton_iter(func, x_n):
    x = sp.Symbol("x")
    sp_func = func(x).evalf()
    func_prime = sp.lambdify(x, sp_func.diff(x))
    return x_n-(func(x_n)/func_prime(x_n))


def find_root_newton(func,start,eps):
    x_n_0 = start
    x_n_1 = get_newton_iter(func, x_n_0)

    while not is_close_to(x_n_0, x_n_1, eps):
        x_n_0 = x_n_1
        x_n_1 = get_newton_iter(func, x_n_0)

    return [x_n_0, x_n_1]


def test_function(x):
    return (m.e)**(-x)-x

print(find_root_newton(test_function, 3, 1e-15))
