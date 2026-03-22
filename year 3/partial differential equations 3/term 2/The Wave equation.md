
The wave equation has form$$\Huge u_{tt}=c^2\Delta u+f$$where $c>0$ is the wave speed. The unknown $u(\underline{x},t)$ can represent the displacement of a string, an elastic membrane, etc. The source term $f(\underline{x},t)$ represents a driving force. This equation is suitable for modelling deformable bodies undergoing small displacements. The wave equation is the prototypical [[Partial differential equations#Hyperbolic PDEs|hyperbolic PDE]]. Linear, second-order, scalar, hyperbolic PDEs have the form $u_{tt}+Lu=f$ with$$\Huge Lu=-\sum_{i,j=1}^na_{ij}u_{x_ix_j}+\sum_{j=1}^nb_ju_{x_j}+du=-A:D^2u+\underline{b}\cdot\underline{\nabla} u+du$$where $a_{ij},b_j,d,f$ are given functions and $A(\underline{x},t)$ is a symmetric uniformly positive definite matrix. Note that for fixed $t$, $L$ reduces to an elliptic operator. In the case of the wave equation we have:$$\Huge L=-c^2\Delta,\,\,A=c^2\mathbb{1},\,\,\underline{b}=\underline{0},\,\,d=0$$
# The wave equation in $\Re$:

For the wave equation it is necessary to impose initial conditions on both $u$ and $u_t$. We consider the one-dimensional wave equation on the whole real line:$$\Huge\begin{align*}
u_{tt}&=c^2u_{xx}\text{ for }(x,t)\in\Re\times(0,\infty)\\
u(x,0)&=g(x)\text{ for }x\in\Re\\
u_t(x,0)&=h(x)\text{ for }x\in\Re
\end{align*}$$We derive d'Alembert's solution of this equation by decomposing this into a pair of transport equations.

Recall that the homogeneous transport equation$$\Huge\begin{align*}
u_t+cu_x&=0\text{ for }(x,t)\in\Re\times(0,\infty)\\
u(x,0)&=u_0(x)\text{ for }x\in\Re
\end{align*}$$is satisfied by:$$\Huge u(x,t)=u_0(x-ct)$$Considering the transport equation starting at some time $t=s$:$$\Huge\begin{align*}
u_t+cu_x&=0\text{ for }(x,t)\in\Re\times(s,\infty)\\
u(x,s)&=f(x)\text{ for }x\in\Re
\end{align*}$$We see that it is satisfied by:$$\Huge u(x,t)=f(x-c(t-s))$$Which we use to write down the solution of the inhomogeneous transport equation. Duhamel's principle dictates that we can write the solution of the inhomogeneous equation as the solution of the homogeneous equation plus the superposition of solutions with initial data $f(x)=F(x,s),s\in[0,t]$:$$\Huge u(x,t)=u_0(x-ct)+\int_0^t F(x-c(t-s),s)ds$$
