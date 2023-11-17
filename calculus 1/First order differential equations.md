
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

The general first order ODE can be written as:$$\Huge M(x,y)dx+N(x,y)dy=0$$
Then rearranging for $\frac{dy}{dx}$:$$\Huge \frac{dy}{dx}=-\frac{M(x,y)}{N(x,y)}$$
Note that both $M$ and $N$ can be multiplied by an arbitrary function, as $f(x,y)$ is only characterised by their ratio, not their exact functions. So each ODE in the above form has a unique $f(x,y)$, but a function $f(x,y)$ will not have a unique function in the form above.

## Total differential:

Given a function $g(x,y)$, the total differential, $dg$, is defined as:$$\Huge dg=\frac{\partial g}{\partial x}dx+\frac{\partial g}{\partial y}dy$$
$dg$ can be thought of as the change in the function $g(x,y)$ when moving from $(x,y)$ to $(x+dx,y+dy)$. If $dg=0$, then $g(x,y)$ is constant.

The standard ODE in the rewritten form is exact if there exists a function $g(x,y)$ such that $M(x,y)dx+N(x,y)dy$ is total differential $dg$, that is:$$\Huge M=\frac{\partial g}{\partial x},\,N=\frac{\partial g}{\partial y}$$
If so, the ODE is equivalent to $dg=0$, so $g(x,y)$ is constant, a solution to the ODE.

## Test for exactness:

The equality of the [[EVT, MVT, boundedness and monotonicity#Partial derivatives|partial derivatives]] allows for an exactness test to be derived:
$$\Huge \frac{\partial^2g}{\partial y\partial x}=\frac{\partial^2g}{\partial x\partial y}\iff\frac{\partial}{\partial y}\left(\frac{\partial g}{\partial x}\right)=\frac{\partial}{\partial x}\left(\frac{\partial g}{\partial y}\right)\iff\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}$$
So the ODE $M(x,y)dx+N(x,y)dy=0$ is exact, if and only if it satisfies the above equality. Example:
![[first order exact example]]

## Non-Exact ODEs:

If an ODE of form $M(x,y)dx+N(x,y)dy=0$ is not exact, multipling by $I(x,y)$ gives an equivalent ODE, $M(x,y)I(x,y)dx + N(x,y)I(x,y)dy=0$. If this new form of the ODE is exact, then $I(x,y)$ is the integrating factor.