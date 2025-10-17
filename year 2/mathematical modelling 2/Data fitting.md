
A collection of data $D_i$ for $i\in\{1,\dots,n\}$ each measured at the specific time $t_i$. A model with function $F(t,p_1,\dots,p_n)$ is expected to describe the data where each $p_j$ is a parameter. Data fitting is the method of finding such $\bar p_j$ such that $F(t,\bar p_1,\dots,\bar p_n)$ fits the data $D_i$ as close as possible. To do this, we aim to minimise:$$\Huge S=\sum_{i=1}^n(D_i-F(t_i,p_1,\dots,p_n))^2$$This is called the least square method.


# Least square method:

One way to find the best fitting curve to a set of data $H$ with $|H|=n$ is to use the least square method. Here we assume that the data follows a curve of the form $f(x)$ and aim to minimise:$$\Huge S=\sum_{i=1}^n(H_i-f(x_i))$$Where you choose $x_i$ corresponding to each $y_i\in H$. When $f(x)=a+bx$ we can do this in python easily:
```python
import numpy as np
import scipy.optimise

X = np.array()
Y = np.array()

def func(x, a, b):
	return a + b*x

popt, pcov = scipy.optimise.curve_fit(func, X, Y, p0=[0, 0.1])
print("a=",popt[0],"b=",popt[1])
```
Here, the last parameter for the scipy function are the starting values of $a$ and $b$.

# Fitting exponential data:

Suppose we have a set of data $t,d(t):(0,d_0),(1,d_1),\dots,(n,d_n)$ where we try to fit the exponential function $D(t)=Ae^{kt}$ for some parameters $A,k$. We can take the logarithm of the function:$$\Huge \ln(Ae^{kt})=\ln A+kt$$Treating this as a linear function and using the curve fitting described above will not work since the data corresponding to the largest value will have much greater impact on the curve fitting algorithm than it should.