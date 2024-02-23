The [[Linear Differential Equations#Principle of Superposition|principle of superposition]] holds when considering linear PDEs, so we restrict our focus to such linear PDEs. This allows our solution space to be a vector space, however in this case the vector space is infinite dimensional.

# Second order linear PDEs:

A second order linear PDE of two independent variables where $u(x,t)$ takes form:$$\Huge Au_{xx}+2Bu_{xt}+Cu_{tt}+Du_x+Eu_t+F_u=0$$$A,B,C,D,E,F$ can be arbitrary functions of $x,t$. There are three broad categories of PDE according to the sign of $\det(M)$ where:$$\Huge M=\begin{pmatrix}A&B\\C&D\end{pmatrix}$$
>$\det(M)<0\implies$ PDE is hyperbolic. The main example of a hyperbolic PDE is the wave equation, given by:$$\Huge u_{xx}-\frac{1}{c^2}u_{tt}=0$$Here $A=c^2,B=0,C=-1,D=0$, so $M=\begin{pmatrix}c^2&0\\0&-1\end{pmatrix}\implies\det(M)=-c^2<0$ for all $c$. The general solution to the wave equation is $u(x,t)=F(x-ct)+G(x+ct)$ for arbitrary functions $F,G$.
>$\det(M)=0\implies$ PDE is parabolic. The main example of a parabolic PDE is the heat equation, given by:$$\Huge u_t=k^2u_{xx}$$Here, $A=k^2,B=C=D=0$, so $M=\begin{pmatrix}k^2&0\\0&0\end{pmatrix}\implies\det(M)=0$
>$\det(M)>0\implies$ PDE is elliptic. The main example of an elliptic PDE is Laplace's (French) equation:$$\Huge u_{xx}+u_{yy}=0$$Here, $t$ has been replaced by $y$ since this equation does not really describe any change in time. We have $A=C=1, B=D=0$, so $M=\begin{pmatrix}1&0\\0&1\end{pmatrix}\implies\det(M)=1>0$.

# Boundary conditions:

A well-posed problem satisfies:
> $\exists$ a solution
> The solution is unique
> The solution depends continuously on initial conditions
> $n$-th order linear ODEs have an $n$-dimensional solution space which is a vector space
> linear PDEs solution space is an infinite dimensional vector space, this can take form:$$\Huge u(x,t)=\sum_i \alpha_iu_i(x,y)$$This will need an infinite number of variables to specify $\lambda_i$

Example: IVP for the heat/wave equation on the whole line $-\infty<x<\infty$. $u_t=k^2u_{xx}$, specify $u(x,0)=R(x)$ at $t=0$. $u_{tt}=c^2u_{xx}$, specify $u(x,0)=R(x)$ at $t=0$, specify $u_t(x,0)=S(x)$ at $t=0$.

Example: IVP for heat/wave equation on a finite interval $a\leq x\leq b$. Specify the same functions as above, however we require a boundary condition at each endpoint. We can set $u(b,t)=0$ (Dirichlet), this implies the end of the metal bar is at $0^oC$, and that the displacement of the wave at the end is $0$. We can also set $u_x(b,t)=0$ (Neumann), this implies an insulated end for the heat equation or a free end to the wave.

Example: Laplace's equation

# Method of separation of variables:

The solution to a linear PDE takes form:$$\Huge u(x,t)=\sum_ia_iu_i(x,t)$$Each $u_i(x,t)$ can be thought of as a basis vector for the solution space to the PDE. So we look for basis vectors in the form $u_i(x,t)=X(x)T(t)$. Consider the example:![[Linear PDEs .excalidraw]]
 