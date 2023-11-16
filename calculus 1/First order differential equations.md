
A differential equation is an equation that relates an unknown function to one or more of it's derivatives. The order of a differential equation is the order of the highest derivative that appears. A function that satisfies a differential equation is known as a solution, if this function can be expressed in terms of a single variable, then it is an ordinary differential equation (ODE). Functions involving partial derivatives and many independent variables are called partial differential equations (PDE). The generic first order differential equation is:$$\Huge \frac{dy}{dx}=f(x,y)$$
The general solution to this is a family of functions, containing an arbitrary constant. When the constant is given a value, the solution becomes particular. This could require $y(x_0)=y_0$, in which the problem is called an initial value problem.

# Separable ODEs:

The standard ordinary differential equation is separable if $f(x,y)=X(x)Y(y)$, which can then be solved with direct integration:$$\Huge \int\frac{1}{Y(y)}dy=\int X(x)dx$$

# First order homogeneous ODEs:

The standard ODE is homogeneous if $f(tx,ty)=f(x,y),\,\forall t\in\Re$. In this case, the substitution $y=xv$ produces a separable ODE in terms of  $v(x)$. Example:
![[first order homogeneous example]]

# First order linear ODEs:

The standard ODE is linear if $f(x,y)=-p(x)y+q(x)$, in which case the standard ODE can be written as:$$\Huge \frac{dy}{dx}+py=q$$
Here, $p$ and $q$ can be any functions of $x$. This is solved using an integrating factor, $I(x)$, which gives the solution:$$\Huge y=\frac{1}{I(x)}\int I(x)q(x)dx,\,\text{where}\,\,\,I(x)=e^{\int p(x)dx}$$
This is proven as follows:![[integrating factor]]

# First order exact ODEs:



