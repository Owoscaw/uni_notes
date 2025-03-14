Green's method describes how to solve an inhomogeneous [[Eigenfunction methods#Boundary conditions|BVP]] of the form:$$\Huge Ly=f$$

# Form of the eigenfunction expansion:

A solution to the [[Eigenfunction methods#The operator|PDE model]] takes form:$$\Huge y(x)=\sum_{k=1}^\infty\frac{\langle f,w_k\rangle}{\lambda_k \langle y_k,w_k\rangle}y_k(x)$$when expanded across a range of eigenfunctions $y_k(x)$. We write $n_k=\langle y_k,w_k\rangle$, the normalisation constant, and get:$$\Huge\begin{align}
y(x)&=\sum_{k=1}^\infty\frac{1}{\lambda_kn_k}\int_a^bf(t)w_k(t)dt\,y_k(x)\\
&=\int_a^b\sum_{k=1}^\infty\frac{1}{\lambda_kn_k}w_k(t)y_k(x)\,f(t)\,dt\\
&=\int_a^bg(x,t)f(t)dt
\end{align}$$This $g(x,t)$ is known as the green's function. Note if $L=L^*$ (and therefore $w_k=y_k$) then we have $g(x,t)=g(t,x)$. In this case we call green's function symmetric.

## Inverse of a differential operator:
In linear algebra we have that $A\underline x=\underline b\implies\underline x=A^{-1}\underline b$. We have $Lx=f$ for a differential operator $L$. It is intuitive that the solution via green's function should therefore be an integral. Green's method describes how to "invert" a differential operator.

Take for example $Ly=-y''=f(x)$ for $0<x<1$ subject to Dirichlet boundary conditions  ($y(0)=y(1)=0$). This has corresponding greens function:$$\Huge g(x,\xi)=\begin{cases}(1-\xi)x&0<x<\xi\\(1-x)\xi&\xi<x<1\end{cases}$$which solves:$$\Huge y(x)=\int_0^1g(x,\xi)f(\xi)d\xi $$which can be shown via differentiation twice. To do this we use the Leibniz rule:$$\large \frac{d }{dx}\int_{a(x)}^{b(x)}f(x,\xi)d\xi=\int_{a(x)}^{b(x)}\frac{\partial f}{\partial x}(x,\xi)f(\xi)d\xi +\frac{db}{dx}(x)f(x,b)-\frac{da}{dx}(x)f(x,a)$$To get:$$\large\begin{align}
y(x)&=\int_0^1g(x,\xi)f(\xi)d\xi\\
&=\int_0^x(1-x)\xi f(\xi)d\xi+\int_x^1(1-\xi)xf(\xi)d\xi\\
\frac{dy}{dx}&=-\int_0^x\xi f(\xi)d\xi+(1-x)xf(x)+\int_x^1(1-\xi)f(\xi)d\xi-(1-x)xf(x)\\
&=-\int_0^x\xi f(\xi)d\xi+\int_x^1(1-\xi)f(\xi)d\xi\\
\frac{d^2y}{dx^2}&=-xf(x)-(1-x)f(x)=-f(x)
\end{align}$$So this indeed solves the differential equation. Note that it would be easier to differentiate $g(x,\xi)$ directly with:$$\Huge \frac{d y}{dx}=\int_0^1\frac{\partial g}{\partial x}(x,\xi)f(\xi)d\xi,\,\,\frac{d^2y}{dx^2}=\int_0^1\frac{\partial^2g}{\partial x^2}(x,\xi)f(\xi)d\xi$$however this would require a function $\delta(x,\xi)$ that satisfies:$$\Huge\int_0^1\delta(x,\xi)f(\xi)d\xi=-f(x)$$and $$\Huge \frac{\partial^2 g}{\partial x^2}=-\delta(x,\xi)$$This is known as green's equation.