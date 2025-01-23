
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