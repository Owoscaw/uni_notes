from math import sin,cos,sqrt

def is_close_to(a,b,eps):
    return abs(a-b)<eps

def equationroot():
    m=0
    a=3
    b=4
    while not is_close_to(a,b,10e-11):
        m=(a+b)/2
        if sin(m) + sin((6)**(0.5)*m) > 0:
            a=m
        else:
            b=m
    return m
    
def strequationroot():
    return "{:.8f}".format(equationroot())

print(strequationroot())