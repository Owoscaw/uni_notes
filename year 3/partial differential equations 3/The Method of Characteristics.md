
In this note we discuss the method of characteristics, used to solve first order [[Introduction to PDEs#Quasi-linear PDEs|quasi-linear]] scalar PDEs. Consider the PDE:$$\Huge \begin{cases}\underline{a}(\underline{x},u(\underline{x}))\cdot\underline{\nabla}u(\underline{x})+a_0(\underline{x},u(\underline{x}))=0&x\in\Omega \\
\text{boundary condition}&x\in\Gamma\end{cases}$$where $\Gamma$ is a lower dimension subset of $\bar\Omega$. Usually, we prescribe information on $\Gamma$ and aim to understand how it "propagates" from $\Omega$.

# Motivation:

Consider a given material and assume it is made up of particles that are being carried by an advection field $\underline{\beta}$. This can be expressed with the system of ODEs:$$\Huge \frac{d\underline{X}_i}{dt}(t)=\underline{\beta}(\underline{X}_i(t))$$where $\underline{X}_i$ represents the position of the $i$th particle in the system. If we assume the particles cannot change shape and fill the volume that consists of the material (incompressible matter), the density of the matter remains the same along the particle trajectories:$$\Huge \frac{d\underline{X}}{dt}(t)=\underline{\beta}(\underline{X}(t)),\,\,\underline{X}(0)=\underline{X}_0$$which represents the paths particles take that started at $\underline{X}_0$ at time $t=0$. That is, if $\rho$ is the density of the matter then:$$\Huge \rho(\underline{X}_0,0)=\rho(\underline{X}(t),t)$$Differentiating wrt $t$ gives:$$\Huge\begin{align*}
0=\frac{d}{dt}\rho(\underline{X}_0,0)&=\frac{d}{dt}\rho(\underline{X}(t),t)\\
&=\underline{\nabla}_x\rho(\underline{X}(t),t)\cdot \frac{d\underline{X}}{dt}(t)+\partial_t\rho(\underline{X}(t),t)\\
&=\partial_t\rho(\underline{X}(t),t)+\underline{\beta}(\underline{X}(t))\cdot\underline{\nabla}_x\rho(\underline{X}(t),t)
\end{align*}$$which resembles the quasi-linear PDE $\partial_t\rho(\underline{x},t)+\underline{\beta}(\underline{x})\cdot\underline{\nabla}_x\rho(\underline{x},t)=0$ on the particle paths which are determined by $\underline{\beta}$. This hints at a solution to:$$\Huge\begin{cases}\partial_t\rho(\underline{x},t)+\underline{\beta}(\underline{x})\cdot\underline{\nabla}_x\rho(\underline{x},t)=0&(\underline{x},t)\in\Lambda\times(0,\infty) \\
\rho(\underline{x},0)=\rho_0(\underline{x})&x\in\Lambda\end{cases}$$now by associating particle paths to the PDE:
> We look for a particle path $\underline{X}(\tau)$ that solves the system of ODEs:$$\Huge \begin{cases}\frac{d\underline{X}}{d\tau}(\tau)=\underline{\beta}(\underline{X}(\tau))&\tau\in(0,t) \\
\underline{X}(0)=\underline{X}_0\end{cases}$$where $\underline{X}_0$ is some fixed vector.
>We have the implication:$$\Huge\begin{align*}
\frac{d}{d\tau}\rho(\underline{X}(\tau),\tau)&=\partial_t\rho(\underline{X}(\tau),\tau)+\underline{\beta}(\underline{X}(\tau))\cdot\underline{\nabla}_x\rho(\underline{X}(\tau),\tau)=0\\
\implies&\rho(\underline{X}(\tau),\tau)=\rho(\underline{X}(0),0)=\rho_0(\underline{X}_0)
\end{align*}$$for all $\tau\in[0,t]$.
>For a given $(\underline{x},t)$ we look for $\underline{X}_0$ that depends on $\underline{x},t$ such that the path $\underline{X}(\tau)$ we found satisfies:$$\Huge \underline{X}(t)=\underline{x}$$That is, we found the initial condition using the terminal condition. We can conclude that:$$\Huge \rho(\underline{x},t)=\rho(\underline{X}(t),t)=\rho_0(\underline{X}_0(\underline{x},t))$$

Here, we used the given advection field $\underline{\beta}$ to find particle paths on which density is constant due to the PDE, then we traced information back to the initial datum:![[The Method of Characteristics 2025-10-21 05.01.56.excalidraw]]

Let us look at another PDE that appears similar, but different, to this. Take for example the transport equation:$$\Huge\begin{cases}\partial_t\rho(x,t)+c\partial_x\rho(x,t)=0&(x,t)\in\Re\times(0,\infty) \\
\rho(x,0)=\rho_0(x)&x\in\Re\end{cases}$$where $c\in\Re$ is constant. In this case $\beta(x)=c$ and the ODE system becomes:$$\Huge\begin{cases}\frac{dx}{d\tau}(\tau)=c&\tau\in(0,t) \\
x(0)=x_0\end{cases}$$which has solution $x(\tau)=x_0+c\tau$. Consequently if $x(t)=x$ then $x_0=x_0(x,t)=x-ct$ and we find that:$$\Huge\rho(x,t)=\rho_0(x_0(x,t))=\rho_0(x-ct)$$

Some matter has "gaps" between its elements, making it compressible. In which case the appropriate PDE for the density is based on the idea of mass conservation, known as Euler's continuity equation:$$\Huge\partial_t\rho(\underline{x},t)+\text{div}_{\underline{x}}(\underline{\beta}(\underline{x})\rho(\underline{x},t))=0$$which can be rewritten as:$$\Huge \partial_t\rho(\underline{x},t)+\underline{\beta}(\underline{x})\cdot\underline{\nabla}_{\underline{x}}\rho(\underline{x},t)=-\text{div}_{\underline{x}}(\underline{\beta}(\underline{x}))\rho(\underline{x},t)$$which fits the incompressible matter case when $\text{div}_{\underline{x}}(\underline{\beta}(\underline{x}))=0$. All of the conceptual tools we have developed can be used to solve this equation. Using the general continuity equation with our understanding of the tau-derivative of particle paths:$$\Huge \frac{d}{d\tau}\rho(\underline{X}(\tau),\tau)=-\text{div}_{\underline{x}}(\underline{\beta}(\underline{x}(\tau)))\rho(\underline{X}(\tau),\tau)$$now defining $z(\tau)=\rho(\underline{X}(\tau),\tau)$ we can see that the PDE implies the ODE:$$\Huge \frac{dz}{d\tau}(\tau)=-\text{div}_{\underline{x}}(\underline{\beta}(\underline{X}(\tau)))z(\tau)$$We can now update the previous methodology to solve the more general equation:$$\Huge\begin{cases}\partial_t\rho(\underline{x},t)+\underline{\beta}(\underline{x})\cdot\underline{\nabla}_{\underline{x}}\rho(\underline{x},t)=-\text{div}_{\underline{x}}(\underline{\beta}(\underline{x}))\rho(\underline{x})&(\underline{x},t)\in\Lambda\times(0,\infty) \\
\rho(\underline{x},0)=\rho_0(\underline{x})&\underline{x}\in\Lambda\end{cases}$$We then look for a particle path $\underline{X}(\tau)$ that solves the system:$$\Huge\begin{cases}\frac{d\underline{X}}{d\tau}(\tau)=\underline{\beta}(\underline{X}(\tau))&\tau\in(0,\tau) \\
\underline{X}(0)=\underline{X}_0\end{cases}$$for fixed vector $\underline{X}_0$. Defining $z(\tau)=\rho(\underline{X}(\tau),\tau)$ we aim to solve:$$\Huge\begin{cases}\frac{dz}{d\tau}(\tau)=-\text{div}_{\underline{x}}(\underline{\beta}(\underline{X}(\tau))z(\tau)&\tau\in(0,t) \\
z(0)=\rho_0(\underline{X}_0)\end{cases}$$the initial condition comes from the fact that $z(0)=\rho(\underline{X}(0),0)=\rho(\underline{X}_0,0)=\rho_0(\underline{X}_0)$. For given $(\underline{x},t)$ we look for $\underline{X}_0$ dependent on $\underline{x},t$ such that the path $\underline{X}(\tau)$ we found satisfies $\underline{X}(t)=\underline{x}$. We conclude that:$$\Huge \rho(\underline{x},t)=\rho(\underline{X}(t),t)=z(t)$$To modify the homogeneous continuity equation for incompressible matter (the first solution), we must add an additional ODE. This methodology marks the basis for the method of characteristics.

# General setting:

We consider the general quasi-linear equation:$$\Huge\begin{cases}\underline{a}(\underline{x},u(\underline{x}))\cdot\underline{\nabla}_xu(\underline{x})=b(\underline{x},u(\underline{x})&x\in\Omega \\
u(\underline{x})=u_0(\underline{x})&x\in\Gamma\end{cases}$$where $\Omega\subseteq\Re^n$ is an open set and $\Gamma\subset\bar\Omega$ is an $n-1$ dimensional parametrised hypersurface in $\Re^n$. This is known as the Cauchy problem. $\Gamma$ is called a Cauchy curve, and $u_0$ is called the Cauchy data. $\underline{a}$ is called the leading vector field and $b$ is called the source term. We further assume that the Cauchy curve is parametrised by:$$\Huge\underline{s}=(s_1,\dots,s_{n-1})\rightarrow\underline{x}_0(s_1,\dots,s_{n-1})=\underline{x}_0(\underline{s})\in\Gamma$$where $\underline{s}=(s_1,\dots,s_{n-1})\in I\subseteq\Re^{n-1}$. The method of characteristics then consists of the steps:
> Solve the $n-1$ parameter family of ODEs for $\underline{X}(\tau,\underline s)$ and $z(\tau,\underline{s})=u(\underline{X}(\tau,\underline{s}))$:$$\Huge\begin{cases}\partial_\tau\underline{X}(\tau,\underline{s})=\underline{a}(\underline{X}(\tau,\underline{s}),z(\tau,\underline{s})) \\
\partial_\tau z(\tau,\underline{s})=b(\underline{X}(\tau,\underline{s}),z(\tau,\underline{s})\end{cases}$$with boundary conditions:$$\Huge\begin{cases}\underline{X}(0,\underline{s})=\underline{x}_0(\underline{s})&\underline{s}\in I \\
z(0,\underline{s})=u_0(\underline{x}_0(\underline{s}))&\underline{s}\in I\end{cases}$$where $\underline{X}(\tau,\underline{s})$ are called the characteristics of the equation. This is motivated from the fact that if we found such $\underline{X}(\tau,\underline{s})$:$$\large\partial_\tau u(\underline{X}(\tau,\underline{s}))=\underline{\nabla}u(\underline{X}(\tau,\underline{s}))\cdot\partial_\tau\underline{X}(\tau,\underline{s})=a(\underline{X}(\tau,\underline{s}),u(\underline{X}(\tau,\underline{s}))\cdot\underline{\nabla}u(\underline{X}(\tau,\underline{s})))$$from which we infer that:$$\Huge z(\tau,\underline{s})=u(\underline{X}(\tau,\underline{s}))$$satisfies:$$\Huge\partial_\tau z(\tau,\underline{s})=b(\underline{X}(\tau,\underline{s}),u(\underline{X}(\tau,\underline{s})))$$Here, $\underline{X}(0,\underline{s})$ and $z(0,\underline{s})$ capture the boundary conditions. $z(\tau,\underline{s})$ stipulates the value of $u$ on $\underline{X}(\tau,\underline{s})$.
>Reverse the flow, $(\tau,\underline{s})\rightarrow\underline{X}(\tau,\underline{s})$. That is, we find $\tau(\underline{x}),\underline{s}(\underline{x})$ such that:$$\Huge\underline{X}(\tau(\underline{x}_0),\underline{s}(\underline{x}))=\underline{x}$$
>The solution then becomes:$$\Huge u(\underline{x})=z(\tau(\underline{x}),\underline{s}(\underline{x}))$$


## Transport equation example:
Take for example the transport equation:$$\Huge\begin{cases}\partial_tu(x,t)+c\partial_xu(x,t)=0&(x,t)\in\Re\times(0,\infty) \\
u(x,0)=u_0(x)&x\in\Re\end{cases}$$The characteristics are then as follows:
> Leading vector field $\underline{a}(x,t,u)=(c,1)$
> Source term $b(x,t,u)=0$
> Domain $\Omega=\Re\times(0,\infty)$
> Boundary $\Gamma=\{(x,0):x\in\Re\}$ parametrised by $s\to (x_0(s),t_0(s))=(s,0)$ for $s\in\Re$

Now we follow our methodology:$$\Huge\begin{cases}\partial_\tau X(\tau,s)=c \\
\partial_\tau T(\tau,s)=1 \\
\partial_\tau z(\tau,s)=0\end{cases}$$and:$$\Huge\begin{cases}X(0,s)=s \\
T(0,s)=0 \\
z(0,s)=u(x_0(s),t_0(s))=u_0(s)\end{cases}$$which is easily solved:$$\Huge\begin{align*}
X(\tau,\underline{s})&=c\tau+X(0,s)=s+c\tau\\
T(\tau,\underline{s})&=\tau+T(0,s)=\tau\\
z(\tau,\underline{s})&=z(0,\tau)=u_0(s)
\end{align*}$$We now reverse the flow:$$\Huge\begin{align*}
x&=s+c\tau\\
t&=\tau\\
\implies\tau&=t\\
s&=x-ct
\end{align*}$$Then we can write the solution:$$\Huge u(x,t)=z(\tau(x,t),s(x,t))=u_0(x-ct)$$
## More complex example:
Take the Cauchy problem:$$\Huge\begin{cases}(t+u(x,t))\partial_xu(x,t)+t\partial_tu(x,t)=x-t&(x,t)\in\Re\times(0,\infty) \\
u(x,1)=1+x&x\in\Re\end{cases}$$Here, the characteristics are:
> Leading vector field $\underline{a}(x,t,u)=(t+u,t)$
> Source term $b(x,t,u)=x-t$
> Domain $\Omega=\Re\times(0,\infty)$
> Boundary $\Gamma=\{(x,1):x\in\Re\}$ parametrised by $\underline s\to (x_0(s),t_0(s))=(s,1)$

Following the methodology:$$\Huge\begin{align*}
\partial_\tau X(\tau,s)&=T(\tau,s)+z(\tau,s)\\
\partial_\tau T(\tau,s)&=T(\tau,s)\\
\partial\tau z(\tau,s)&=X(\tau,s)-T(\tau,s)
\end{align*}$$with, for $s\in\Re$:$$\Huge\begin{align*}
X(0,s)&=x_0(s)=s\\
T(0,s)&=t_0(s)=1\\
z(0,s)&=u(x_0(s),t_0(s))=u(s,1)=u_0(s)
\end{align*}$$