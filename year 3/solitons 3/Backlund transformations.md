
We have previously constructed solutions for moving solitons as [[Travelling Waves#The Basic properties of Solitons The KdV equation KdV soliton|travelling waves]] by reducing a PDE into multiple ODEs. Now that we aim to describe the solution for multiple colliding solitons, we must use a different method. In these cases, it will not be possible to reduce the PDE into ODEs, so we introduce the method known as the Backlund transformation.

There are two main uses of the Backlund transformation:
> To generate solutions of a more complex PDE using a simpler PDE
> To generate new solutions of a given PDE from already known solutions of the same PDE


# Definition:

Consider two functions $u,v$ with two differential equations $P[u]=0,Q[v]=0$ where $P,Q$ are two differential operators. If there is a pair of relations, $R_1[u,v]=0,R_2[u,v]=0$, between $u,v$ such that:
> If $P[u]=0$ then the relations can be solved for $v$, giving a solution of $Q[v]=0$
> If $Q[v]=0$ then the relations can be solved for $u$, giving a solution of $P[u]=0$

Then the relations are called a Backlund transformation (BT). Furthermore if $P=Q$, then the relations are called an auto-Backlund transformation (a-BT). This is useful if the relation is easier to solve than either differential equation, which can be used to generate solutions to the differential equations.
> $P[u]=0,Q[v]=0$ are known as integrability conditions
> $R_1[u,v]=0,R_2[u,v]=0$ can be integrated for $v,u$ if the integrability condition $P[u]=0,Q[v]=0$ respectively are statisfied
> 

## Simple example:
Take the two dimensional Laplace operator $P=Q=\partial_x^2+\partial_y^2$ and the Backlund transformation $R_1[u,v]=u_x-v_y=0,R_2[u,v]=u_y+v_x=0$. We can check that these are valid integrability conditions by differentiating them wrt $x,y$ and summing/subtracting:$$\Huge\begin{align*}
0=\partial_xR_1+\partial_yR_2&=u_{xx}-v_{yx}+v_{xy}+u_{yy}=u_{xx}+u_{yy}\\
0=-\partial_yR_1+\partial_xR_2&=-u_{xy}+v_{yy}+u_{yx}+v_{xx}=u_{xx}+u_{yy}
\end{align*}$$Therefore the relations imply the differential operator, showing that it is an auto-Backlund transformation.

$v(x,y)=2xy$ solves the Laplace equation, we can use the a-BT to find another solution, $u$, of the same equation:$$\Huge\begin{cases}u_x=v_y=2x \\
u_y=-v_x=-2y\end{cases}\implies\begin{cases}u=x^2+f(y) \\
f'(y)=-2y\end{cases}\implies f(y)=-y^2+C$$so we find that $u(x,y)=x^2-y^2+C$ for some constant $C$ is another solution. Note that the equations $R_1[u,v]=R_2[u,v]=0$ are simply the [[Complex differentiation#Cauchy-Riemann equations|C-R equations]] for the holomorphic function $w=u+iv$ of the complex variable $z=x+iy$. In our example, $w(z)=z^2+C$. Two functions $u,v$ that solve the Laplace equation are often called harmonic conjugates.