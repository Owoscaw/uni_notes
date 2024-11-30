from sympy import *

x,y = var('x, y')
num = integrate( (x**2+y**2)*exp(-x**2-y**2), (x,-oo,oo), (y,-oo,oo))
den = integrate( exp(-x**2-y**2), (x,-oo,oo), (y,-oo,oo))

print("numerator   = " + str(num))
print("denominator = " + str(den))
print("integral    = " + str(num/den))
