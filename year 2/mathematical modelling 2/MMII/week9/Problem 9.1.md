
The code:
```python
import numpy as np
import math

def P(x):
    return math.exp(-x**2)/math.sqrt(math.pi)

def f(x):
    return x**2

N  = 100
xL = -10.  # 10 is close enough to infinity
xR =  10.

xvals = np.linspace(xL, xR, N)
fsum  = 0
for x in xvals:
    fsum += f(x)*P(x)

print(fsum/N*(xR-xL))
```
Computes the integral:$$\Huge \int_{-\infty}^\infty x^2\frac{e^{-x^2}}{\sqrt{\pi}}dx$$Since the above code is equivalent to:$$\Huge \frac{1}{N(b-a)}\sum_{i=1}^Nf(x_i)P(x_i)$$Where $a=x_L,b=x_R$ and $x_i=a=\Delta x\cdot i$. This can be written as:$$\Huge \sum_{i=1}^N\Delta x\,f(x_i)P(x_i)$$In the limiting case as $N\to\infty$ we get:$$\Huge \lim_{N\to\infty}\sum_{i=1}^N\Delta x(f(x_i)P(x_i))=\int_{a}^b(f(x)P(x))dx=\int_{a}^bx^2\frac{e^{-x^2}}{\sqrt{\pi}}dx$$Then as $a\to-\infty$ and $b\to-\infty$ we get the integral as required.