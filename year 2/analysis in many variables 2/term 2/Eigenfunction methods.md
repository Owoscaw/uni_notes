
Consider PDEs of the form:$$\Huge \frac{\partial u}{\partial t}=Lu+h(x,t)$$Where $L$ is some [[Differential operators|differential operator]] in $x$. We consider $u(x,t)$ to be a one dimensional scalar model on a domain $x\in[a,b]$ and $t>0$.

We have many degrees of freedom in this model:

## The operator:
One such is the operator $L$. The differential operator $L$ must satisfy linearity. That is $L(u_1+u_2)=L(u_1)+L(u_2)$, implying the [[Partial differential equations#Linear equations and superposition|principle of superposition]].

## Source term:
Another parameter is the "source" term given by $h(x,t)$. This has no $u$ dependence and provides some external change in $\frac{\partial u}{\partial t}$. If $h(x,t)=0$, the problem is called homogenous, if it is non-zero the problem is called inhomogeneous. If $u_h$ solves $h(x,t)=0$ and $u_{ih}$ solves $h(x,t)\neq0$ then $u=u_h+u_{ih}$ solves the problem.

## Boundary conditions:
Boundary conditions (BC) are also required. If $L$ is an $n$th order operator, then $n$ BCs are also required. We denote each boundary condition as a linear operator:$$\Huge BC_i([u,a,b])=0$$For example, we could denote a BC as follows:$$\Huge BC_1([u,a,b])=\frac{\partial u}{\partial x}\vert_{x=a}=0$$A homogenous BC requires $u$ or its derivatives to be $0$ on the boundary. An inhomogeneous BC required $u$ or its derivatives to be some other value at the boundary.

## Initial conditions:
Finally, the problem requires a start point called the initial condition. That is, $u(x,0)$ is given by some function:$$\Huge u(x,0)=g(x)$$
# Solution:

We make the following assumptions that are justified later:
> Our solution can be written in separable form:$$\Huge u(x,t)=\sum_{n=0}^\infty c_n(t)y_n(x),\,\,h(x,t)=\sum_{n=0}^\infty h_n(t)y_n(x)$$Which makes the model:$$\Huge \sum_{n=0}^\infty\frac{dc_n}{dt}y_n(x)=\sum_{n=0}^\infty c_n(t)Ly_n(x)+\sum_{n=0}^\infty h_n(t)y_n(x)$$
> The functions $y_n(x)$ satisfy:$$\Huge Ly_n(x)=-\lambda_ny_n(x)$$Where $L$ is acting as a spatial operator only. This allows the sums to be written in the form:$$\Huge \sum_{n=0}^\infty\left(\frac{d c_n}{dt}+\lambda_nc_n(t)-h_n(t)\right)y_n(x)=0$$
> Each $y_n(x)$ are linearly independent, the sum can only be zero when each individual term is zero

So for each $n$ we require that:$$\Huge\frac{d c_n(t)}{dt}+\lambda_nc_n(t)-h_n(t)=0$$Which can always be solved for $c_n(t)$, as $h_n(t)$ is always known. We solve this using the [[First order differential equations#Test for exactness|integrating factor]] method to get the solution:$$\Huge c_n(t)=e^{-\lambda_nt}\left(a_n+\int_1^te^{\lambda_nt'}h_n(t')dt'\right)$$The homogenous solution is given by the term with constants $a_n$, while the inhomogeneous solution is given by the integral term. To determine the constants of integration $a_n$ we must use the initial condition:$$\Huge u(x,0)=\sum_{n=0}^\infty c_n(0)y_n(x)=g(x)$$Now since the boundary conditions were linear we have:$$\Huge BC_iu=\sum_{n=0}^\infty c_n(t)BC_iy_n(x)=0\implies BC_iy_n(x)=0$$This is because the boundary conditions act only on the spatial variables. So in order to fully solve the equation, one must solve the eigenvalue equation:$$\Huge Ly_n=-\lambda_ny_n,\,\,BC_iy_n=0$$

# Example via Fourier series:

Taking:$$\Huge L=\frac{\partial^2 }{\partial x^2},\,\,BC_1=\frac{\partial }{\partial x}\vert_{x=a}=0,\,\,BC_2=\frac{\partial }{\partial x}\vert_{x=b}=0$$This must solve:$$\Huge \frac{d^2y_n}{dx^2}=-\lambda_n y_n,\,\,\frac{d y_n}{dx}\vert_{x=a}=\frac{d y_n}{dx}\vert_{x=b}=0$$A specific solution to this is given by:$$\Huge y_n(x)=a_n\cos\left(\frac{n\pi(x-a)}{b-a}\right),\,\,\lambda_n=\frac{n^2\pi^2}{(b-a)^2}$$For arbitrary $n\in\mathbb{N}$. The argument above states that the solution to:$$\Huge \frac{\partial u}{\partial t}=\frac{d^2u}{dx^2}+h(x,t)$$Is given by:$$\Huge u(x,t)=\sum_{n=0}^\infty c_n(t)\cos\left(\frac{n\pi(x-a)}{b-a}\right)$$Note that for fixed $t$ this is simply a [[Fourier Series]]. This motivates us to represent the forcing function, $h(x,t)$, as the following:$$\Huge h(x,t)=\sum_{n=0}^\infty h_n(t)\cos\left(\frac{n\pi(x-a)}{b-a}\right)$$With:$$\Huge h_n(t)=\frac{l}{b-a}\int_a^bh(x,t)\cos\left(\frac{n\pi(x-a)}{b-a}\right)dx$$With $l=2$ for $n\neq0$ and $l=1$ for $n=0$. We can also do the same for initial conditions:$$\Huge g(x)=\sum_{n=0}^\infty c_n(0)\cos\left(\frac{n\pi(x-a)}{b-a}\right)$$With:$$\Huge c_n(0)=\frac{l}{b-a}\int_a^bg(x)\cos\left(\frac{n\pi(x-a)}{b-a}\right)dx$$