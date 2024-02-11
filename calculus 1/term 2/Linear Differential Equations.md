An $n$-th order linear differential equation can be written in the form:$$\Huge \frac{d^ny}{dx^n}+p_1(x)\frac{d^{n-1}y}{dx^{n-1}}+p_2(x)\frac{d^{n-2}y}{dx^{n-2}}+\dots+p_{n-1}(x)\frac{dy}{dx}+p_n(x)y=c(x)$$If $c(x)=0$, then the equation is homogeneous, if not then it is inhomogeneous. Linearity constrains the dependent variable, $y$, such that only of it's derivatives can appear in each term, there is no such constraint for the independent variable, $x$.

# Principle of Superposition:

If $y_1(x),y_2(x)$ solve a linear homogeneous ODE, then $y=\alpha y_1+\beta y_2$ is also a solution for constants $\alpha,\beta\in\Re$. This can be easily proven by considering the linearity of the derivative. Since any linear combination of solutions is also a solution, the solution space of the differential equation is a [[Vector space definitions|vector space]]. An $n$-th order differential equations has a general solution with $n$ parameters, if there is a basis of $n$ linearly independent solutions $\{y_1,\dots,y_n\}$ then:$$\Huge y=\alpha_1y_1+\alpha_2y_2+\dots+\alpha_ny_n$$Has $n$ arbitrary parameters $(\alpha_1,\dots,\alpha_n)$ and is a general solution.

The general solution to an $n$-th order linear inhomogeneous differential equation is given by:$$\Huge y=y_{PI}+\alpha_1y_1+\dots+\alpha_ny_n$$Where $y_{PI}$ is the solution to the inhomogeneous part, and the latter terms form the general solution fo the homogeneous equation, the solutions space is an affine space.

# Series solutions:

Consider a second order ODE of form:$$\Huge \frac{d^2y}{dx^2}+p(x)\frac{dy}{dx}+q(x)y=0$$We look for solutions in the form of a [[Power series|power series]], $y(x)=\sum_{n=0}^\infty a_n(x-x_0)^n$. It is provided that a solution exists if $x_0$ is a regular point of the differential equation. $x_0$ is a regular point of the differential equation if and only if $p(x),q(x)$ are analytic at $x_0$, that is they can be represented by their [[Taylor series]] in a neighbourhood around $x_0$.


# Legendre's equation:
![[Legendre's equation]]In general, a power series about $x_0$ will only converge in a [[Power series#Radius of Convergence|Radius of convergence]], $R$, where:$$\Huge R=\min|x_0-x_i|$$For all singular points of a function, $x_i$. For Legendre's equation, we can look at the [[Series#Convergence criteria|ratio test]] to prove that it has $R=1$:$$\Huge \lim_{n\to\infty}\left|\frac{a_{n+2}x^{n+2}}{a_xx^n}\right|=\lim_{n\to\infty}\left|\frac{a_{n+2}}{a_n}\right|x^2=\lim_{n\to\infty}\left|\frac{n(n+1)-\lambda}{(n+1)(n+2)}\right|x^2=x^2$$So the series from $y_e$ will diverge for $x^2>1$ and converge for $x^2<1$. Note that when $\lambda=m(m+1)$, all $a_{m+2}$ terms will vanish, so when $m$ is even, all $a_nx^n$ terms will vanish for $n>m$. So for even $n$, $y_e$ is an $m$-th order polynomial and $y_o$ is still an infinite series. Similarly for odd $n$, the reverse happens. The polynomials that come from this process are called Legendre polynomials. We denote the $m$
-th Legendre polynomial as $P_m$ and fix $P_m(1)=1$:

| $m$ | $\lambda=m(m+1)$ | $y_e$    | $y_0$    | $P_m(x)$              |
| --- | ---------------- | -------- | -------- | --------------------- |
| $0$ | $0$              | $1$      | $\infty$ | $1$                   |
| $1$ | $2$              | $\infty$ | $x$      | $x$                   |
| $2$ | $6$              | $1-3x^2$ | $\infty$ | $\frac{1}{2}(3x^2-1)$ |
| 3   | 12               | $\infty$ | $x-\frac{5}{3}x^3$         | $\frac{1}{2}(5x^3-3x)$                      |

# Frobenius' Method:

The radius of convergence for a power series about $x_0$ is determined by the closest singular point of the series to said value of $x$. Frobenius' method allows for a modified power series that can be used at a singular point, provided the singular point behaves nicely. Take the differential equation $y''+p(x)y'+q(x)y=0$, then we classify points as follows:
>$x_0$ is a regular point of the differential equation if both $p,q$ can be represented by a [[Taylor series#Taylor's theorem|Taylor expansion]] about the point $x_0$
>$x_0$ is a regular single point of the differential equation if $(x-x_0)p(x),(x-x_0)^2q(x)$ can be represented by a Taylor expansion about $x_0$
>$x_0$ is an irregular single point of the differential equation if none of the above conditions are met

Frobenius' method allows for the expansion of a series solution at these regular single points. In certain cases, this can allow for a series solution to be defined for all $x$. We look for a solution of the form:$$\Huge y(x)=\sum_{n=0}^\infty a_n(x-x_0)^{n+r}$$Where $r$ is a constant to be determined. The method is best demonstrated in an example:![[Frobenius' method]]
# Differential Operators:

Legendre's equation can be written in another form:$$\Huge \mathcal L_{L}y(x)=\left[(x^2-1)\frac{d^2y}{dx^2}+2x\frac{dy}{dx}\right]=\lambda y(x)$$