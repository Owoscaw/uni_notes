
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
z(0,\underline{s})=u_0(\underline{x}_0(\underline{s}))&\underline{s}\in I\end{cases}$$where $\underline{X}(\tau,\underline{s})$ are called the characteristics of the equation. Here, $\tau$ represents the parameter "intrinsic time" of the characteristics, and $\underline s$ represents a general point on the boundary. This is motivated from the fact that if we found such $\underline{X}(\tau,\underline{s})$:$$\large\partial_\tau u(\underline{X}(\tau,\underline{s}))=\underline{\nabla}u(\underline{X}(\tau,\underline{s}))\cdot\partial_\tau\underline{X}(\tau,\underline{s})=a(\underline{X}(\tau,\underline{s}),u(\underline{X}(\tau,\underline{s}))\cdot\underline{\nabla}u(\underline{X}(\tau,\underline{s})))$$from which we infer that:$$\Huge z(\tau,\underline{s})=u(\underline{X}(\tau,\underline{s}))$$satisfies:$$\Huge\partial_\tau z(\tau,\underline{s})=b(\underline{X}(\tau,\underline{s}),u(\underline{X}(\tau,\underline{s})))$$Here, $\underline{X}(0,\underline{s})$ and $z(0,\underline{s})$ capture the boundary conditions. $z(\tau,\underline{s})$ stipulates the value of $u$ on $\underline{X}(\tau,\underline{s})$.
>Reverse the flow, $(\tau,\underline{s})\rightarrow\underline{X}(\tau,\underline{s})$. That is, we find $\tau(\underline{x}),\underline{s}(\underline{x})$ such that:$$\Huge\underline{X}(\tau(\underline{x}_0),\underline{s}(\underline{x}))=\underline{x}$$Here, $\tau(x),s(x)$ represent the evolved time and the boundary starting point respectively.
>The solution then becomes:$$\Huge u(\underline{x})=u(\underline{X}(\tau(x),s(x)))=z(\tau(\underline{x}),\underline{s}(\underline{x}))$$


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
z(0,s)&=u(x_0(s),t_0(s))=u(s,1)=1+s
\end{align*}$$Solving for $T$ gives:$$\Huge T(\tau,s)=T(0,s)e^{\tau}=e^\tau$$so we can write:$$\Huge\begin{cases}\partial_\tau X(\tau,s)=e^\tau+z(\tau,s)&X(0,s)=s \\
\partial_\tau z(\tau,s)=X(\tau,s)-e^\tau&z(0,s)=1+s\end{cases}$$we can see that:$$\Huge\begin{cases}\partial_\tau(X(\tau,s)+z(\tau,s))=X(\tau,s)+z(\tau,s) \\
\partial_\tau(X(\tau,s)-z(\tau,s))=-(X(\tau,s)-z(\tau,s)+2e^\tau\end{cases}$$$$\Huge\begin{cases}X(0,s)+z(0,s)=1+2s \\
X(0,s)-z(0,s)=-1\end{cases}$$From this we can find $(X+z)(\tau,s)$ and $(X-z)(\tau,s)$ and consequently:$$\Huge\begin{align*}
X(\tau,s)&=(1+s)e^\tau-e^{-\tau}\\
z(\tau,s)&=se^\tau+e^{-\tau}\\
T(\tau,s)&=e^\tau
\end{align*}$$We have solved the system of ODEs, now we must reverse the flow:$$\Huge\begin{align*}
\tau&=\log(T)\\
X(\tau,s)&=(1+s)T-\frac{1}{T}\\
\implies s&=\frac{X+\frac{1}{T}}{T}-1
\end{align*}$$Finally we can write the solution:$$\Huge\begin{align*}
u(x,t)&=z(\tau(x,t),s(x,t))\\
&=s(x,t)e^{\tau(x,t)}+e^{-\tau(x,t)}\\
&=\left(x+\frac{1}{t}-t\right)+\frac{1}{t}=x+\frac{2}{t}-t
\end{align*}$$
## Review of the method:
This is all fine and dandy, however we ask:
> Does the method hold?
> How long do the characteristics last?
> Can all points be reached using characteristics?
> How many characteristics start at the same point?
> Can characteristics cross?
> Are characteristics stable wrt to the boundary variable?

# Review of ODE theory:

Let $A\subseteq\Re^n$ and let $\underline{f}:A\rightarrow\Re^m$. We say that $\underline{f}$ is Lipschitz continuous on $A$ if there exists $L>0$ such that for any $\underline{x},\underline{y}\in A$ we have:$$\Huge |\underline{f}(\underline{x})-\underline{f}(\underline{y})|_{\Re^m}\leq L|\underline{x}-\underline{y}|_{\Re^n}$$We say that $\underline{f}$ is locally Lipschitz on $A$ if for any $\underline{x_0}\in A$, there exists an open set $U_{\underline{x}_0}$ such that $\underline{f}$ is Lipschitz on $A\cap U_{\underline{x}_0}$. That is, for any $\underline{x}_0\in A$ there exists an open set $U_{\underline{x}_0}$ and $L(U_{\underline{x}_0})>0$ such that for any $\underline{x},\underline{y}\in A\cap U_{\underline{x}_0}$:$$\Huge |\underline{f}(\underline{x})-\underline{f}(\underline{y})|_{\Re^m}\leq L(U_{\underline{x}_0})|\underline{x}-\underline{y}|_{\Re^n}$$Note that this condition is weaker than the general Lipschitz condition. Writing $\underline{f}=(f_1,\dots,f_m)$ we have that:
> $\underline{f}$ is Lipschitz on $A$ if and only if $f_i:\Re^n\rightarrow\Re$ is Lipschitz on $A$ for any $i=1,\dots,m$.
> $\underline{f}$ is locally Lipschitz on $A$ if and only if $f_i:\Re^n\rightarrow\Re$ is locally Lipschitz on $A$ for any $i=1,\dots,m$

For example, $f:\Re\rightarrow\Re$ given by $f(x)=|x|$ is Lipschitz. For any $x,y\in\Re$:$$\Huge|f(x)-f(y)|=||x|-|y||\leq|x-y|=L|x-y|,\,\,L=1$$Also, $f:\Re\rightarrow\Re$ given by $f(x)=x^2$ is not Lipschitz, but locally Lipschitz on $\Re$:$$\large |f(x)-f(y)|=|x^2-y^2|=|x-y||x+y|\leq(|x|+|y|)|x-y|\leq2R|x-y|$$for $x,y\in B_R(0)$ for any $R\in\Re$.

Let $U\subseteq\Re^n$ be an open set such that for any $\underline{x},\underline{y}\in U$ and any $\theta\in[0,1]$. We have that:$$\Huge\theta\underline{x}+(1-\theta)\underline{y}\in U$$That is, if $\underline{x},\underline{y}\in U$ then so is the straight line between them. Sets that allow this are called convex sets. $\underline{f}:U\rightarrow\Re^m$ be differentiable, then:
>If $$\Huge L=\sup_{x\in U}\max_{i,j}|D\underline{f}(\underline{x})_{ij}|<\infty$$then $\underline{f}$ is Lipschitz on $U$ and:$$\Huge |\underline{f}(\underline{x})-\underline{f}(\underline{y})|\leq\sqrt{nm}L|\underline{x}-\underline{y}|_{\Re^n}$$
>If for every $\underline{x}_0\in U$ there exists an open ball $B_\epsilon(\underline{x}_0)\subseteq U$ such that:$$\Huge L(B_\epsilon(\underline{x}_0))=\sup_{x\in B_\epsilon(\underline{x}_0)}\max_{i,j}|D\underline{f}(\underline{x})_{ij}|<\infty$$then $\underline{f}$ is locally Lipschitz on $U$.

We can prove the above statements: Given $x,y\in U$ define $g:[0,1]\rightarrow\Re$ by:$$\Huge g(t)=f(tx+(1-t)y)$$Using the MVT we can find $t_0\in[0,1]$ such that:$$\Huge |g(1)-g(0)|=|g'(t_0)|=|Df(t_0x+(1-t_0)y)(x-y)|\leq\sqrt{n}L|x-y|_{\Re^n}$$Hence $|f(x)-f(y)|=|g(1)-g(0)|$ fits the definition of Lipschitz. The same is true of the local case.

Let $U\subseteq\Re^n$ be open and convex. If $\underline{f}:U\rightarrow\Re^m$ is continuously differentiable, then $\underline{f}$ is locally Lipschitz.

## Cauchy-Lipschitz/Picard-Lindelöf theorem:
Consider the system of ODEs:$$\Huge\begin{cases}\frac{d\underline{X}}{d\tau}(\tau)=\underline{f}(\tau,\underline{X}(\tau)) \\
\underline{X}(t_0)=\underline{X}_0\end{cases}$$where $\underline{f}:\Re\times\Re^n\rightarrow\Re^n$, $t_0\in\Re$, and $\underline{X}_0\in\Re^n$ are given. Assume that there exists $\delta>0$ and $M>0$ such that $\underline{f}$ is continuous in its first variable on $[t_0-\delta,t_0+\delta]\times\overline{B_M(\underline{X}_0)}$ and that there exists $L(\underline{X}_0)$ such that:$$\Huge|\underline{f}(\tau, \underline{X})-\underline{f}(\tau,\underline{Y})|\leq L(\underline{X}_0)|\underline{X}-\underline{Y}|$$for all $(\tau,\underline{X})\in[t_0-\delta,t_0+\delta]\times\overline{B_M(\underline{X}_0)}$. Then there exists $\epsilon>0$ and a unique continuously differentiable function $\underline{X}:(t_0-\delta,t_0+\delta)\rightarrow\Re^n$ that solves the system of ODEs.

This problem is equivalent to finding a continuous map $\underline{X}:(t_0-\epsilon,t_0+\epsilon)\rightarrow\Re^n$ such that:$$\Huge \underline{X}(t)=\underline{X}_0+\int_{t_0}^t\underline{f}(\tau,\underline{X}(\tau))d\tau$$We can also define an operator on functions from $(t_0-\delta,t_0+\delta)\rightarrow\Re^n$ to the same space by:$$\Huge T(g)(t)=\underline{X}_0+\int_{t_0}^t\underline{f}(\tau,g(\tau))d\tau$$then we want to find $\underline{X}$ such that:$$\Huge \underline{X}=T(\underline{X})$$Note that:$$\Huge |T(h)-T(g)|\leq\int_{t_0}^t|f(\tau,h(\tau))-f(\tau,g(\tau))|d\tau$$so we can define a sequence:$$\Huge\begin{align*}
\underline{X}_1(t)&=\underline{X_0}\\
\underline{X}_{n+1}(t)&=T(\underline{X}_n)(t)
\end{align*}$$Then for small enough $\epsilon>0$ we will get that:$$\Huge \underline{X}_n\to X,\,\,T(\underline{X}_n)\to T(\underline{X})$$

For example, consider the ODE $\frac{dx}{dt}=x^{1/2}$ with $x(0)=0$. Here, $x=0$ is a solution. Assuming $x(t)\neq0$ in a small neighbourhood of $(-\epsilon,\epsilon)\setminus\{0\}$ we can separate the equation:$$\Huge\begin{align*}
\frac{dx}{\sqrt{x}}&=dt\\
\implies 2\sqrt{x}&=t+c\\
\implies x(t)&=\frac{(t+c)^2}{4}\\
x(0)=0\implies x(t)&=\frac{t^2}{4}
\end{align*}$$As the left and right derivatives of $1/4t^2$ agree with $x=0$, we can stitch them together to form a global (exists for all time) solution.

This is not always the case, take for example:$$\Huge\begin{cases}\frac{dx}{d\tau}=x^2 \\
x(0)=0\end{cases}$$If $x(\tau)\neq0$ in a small neighbourhood of $\tau=0$, then:$$\Huge\begin{align*}
\frac{dx}{x^2}&=d\tau\\
\implies-\frac{1}{x}&=\tau+c\\
x(\tau=0)=1\implies-\frac{1}{1}&=c\\
\implies c&=-1\\
\implies x(\tau)&=\frac{1}{1-\tau}
\end{align*}$$and we see that the solution is only defined on $(-\infty,1)$.

## Local existence and uniqueness with continuous dependence in parameters:

Consider the system:$$\Huge\begin{cases}\partial_\tau\underline{X}(\tau,\underline{s})=\underline{f}(\tau,\underline{X}(\tau,\underline{s})) \\
\underline{X}(0,\underline{s})=\underline{x}_0(\underline{s})&\underline{s}\in I\end{cases}$$where $\underline{f}:[-\delta,\delta]\times\bar U\rightarrow\Re^n$ is continuously differentiable with $\delta>0$ given, $U\subseteq\Re^n$ is an open set, and $\underline{x}_0:I\rightarrow\bar U$ is continuously differentiable where $I\subseteq\Re^{n-1}$ is an open set. Then for any $\underline{s}_0\in I$ we can find $\epsilon(\underline{s}_0)>0$ and $M(\underline{s}_0)>0$ such that there exists a unique continuously differentiable function $\underline{X}:(-\epsilon(\underline{s}_0),\epsilon(\underline{s}_0))\times B_{M(\underline{s}_0)}(\underline{s}_0)\rightarrow\Re^n$ that solves the system. Consequently, if $K\subset I$ is a compact set, there exists $\epsilon(K)>0$ and an open set $V_k$ with $K\in V_k$ such that there exists a unique continuously differentiable function $\underline{X}:(-\epsilon(K),\epsilon(K))\times V_k\rightarrow\Re^n$ that solves the system. We can extend the result to $\bar I$ when $I$ is bounded and $\underline{x}_0$ is continuously differentiable on $\bar I$. In such case we can find a unique continuously differentiable solution $\underline{X}:(-\epsilon,\epsilon)\times\bar I\rightarrow\Re^n$ for some $\epsilon>0$.

# Local well posedness of first order quasi-linear PDEs:

The local existence and uniqueness with continuous dependence in parameters theorem above allows us to see that the first step in the method of characteristics is possible when $\underline{a},b$ are $C^1$ as well as $\underline{x}_0(\underline{s})$.

Consider the quasi-linear PDE:$$\Huge\begin{cases}\underline{a}(\underline{x},u(\underline{x}))\cdot\underline{\nabla}u(\underline{x})=b(\underline{x},u(\underline{x}))&\underline{x}\in\Omega \\
u(\underline{x})=u_0(\underline{x})&\underline{x}\in\Gamma\end{cases}$$where $\Omega\subseteq\Re^n$ is an open set and $\Gamma\subset\bar\Omega$ is an $n-1$ dimensional curve/surface parametrised by:$$\Huge\underline{s}:I\subseteq\Re^{n-1}\rightarrow\Gamma,\,\,\underline{s}\rightarrow\underline{x}_0(\underline{s})$$Assume in addition that $\underline{x}_0$ is continuously differentiable on $I$. The point $\underline{x}_0(\underline{s}_0)$ with $\underline{s}_0\in I$ is called non-characteristic if:$$\Huge\det\begin{pmatrix}a_1(\underline{x}_0(\underline{s}_0),u(\underline{x}_0(\underline{s}_0)))& \\ \vdots&D_{\underline{s}}\underline{x}_0(\underline{s}_0) \\ a_n(\underline{x}_0(\underline{s}_0),u(\underline{x}_0(\underline{s}_0)))&\end{pmatrix}\neq0$$Note that if we write $\underline{x}_0=(x_{0,1},\dots,x_{0,n})$, the tangent hyperplane to $\underline{x}_0(\underline{s}_0)$ is spanned by:$$\Huge\begin{pmatrix}\frac{\partial x_{0,1}}{\partial s_1}(\underline{s}_0) \\ \vdots \\ \frac{\partial x_{0,m}}{\partial s_1}(\underline{s}_0)\end{pmatrix},\begin{pmatrix}\frac{\partial x_{0,1}}{\partial s_2}(\underline{s}_0) \\ \vdots \\ \frac{\partial x_{0,m}}{\partial s_2}(\underline{s}_0)\end{pmatrix},\dots,\begin{pmatrix}\frac{\partial x_{0,1}}{\partial s_{n-1}}(\underline{s}_0) \\ \vdots \\ \frac{\partial x_{0,m}}{\partial s_{n-1}}(\underline{s}_0)\end{pmatrix}$$which are exactly the columns of $D_{\underline{s}}\underline{x}_0(\underline{s}_0)$. Consequently, being non-characteristic means that the leading vector field is not a linear combination of the basis of the hyperplane to $\Gamma$ at $\underline{x}_0(\underline{s}_0)$ and as such the leading vector field takes out of $\Gamma$ at $\underline{x}_0(\underline{s}_0)$. This condition ensures that characteristics can reach inside of $\Omega$ from the boundary, $\Gamma$.

Take the setting of the above quasi-linear PDE. Furthermore, assume that $\underline{x}_0$ is bijective and continuously differentiable. Also, let $\underline{s}_0\in I$ and assume that there exists $M(\underline{s}_0)>0$ such that $u_0\circ\underline{x}_0:I\rightarrow\Re$ is continuously differentiable on $B_{M(\underline{s}_0)}(\underline{s}_0)$ and that there exists $\delta(\underline{s}_0)>0$ and $M_1(\underline{x}_0(\underline{s}_0))>0$ such that:$$\Huge \underline{a}:\bar\Omega\times\Re\rightarrow\Re^n,\,\,b:\bar\Omega\times\Re\rightarrow\Re$$are continuously differentiable on $\overline{B_{M_1(\underline{x}_0(\underline{s}_0))}(\underline{x}_0(\underline{s}_0))\cap\Omega}\times[u_0(\underline{x}_0(\underline{s}_0))-\delta(\underline{s}_0),u_0(\underline{x}_0(\underline{s}_0))+\delta(\underline{s}_0)]$. If $\underline{x}_0(\underline{s}_0)$ is non-characteristic then there exists $R(\underline{x}_0(\underline{s}_0))>0$ and a unique continuously differentiable function:$$\Huge u:B_{R(\underline{x}_0(\underline{s}_0))}(\underline{x}_0(\underline{s}_0))\cap\Omega\rightarrow\Re$$that is continuous on $B_{R(\underline{x}_0(\underline{s}_0))}(\underline{x}_0(\underline{s}_0))\cap\bar\Omega$ and satisfies the PDE. If $\underline{a}$ and $b$ are continuously differentiable on $\bar\Omega\times\Re$, and $u_0\circ\underline{x}_0$ is continuously differentiable on $I$ and every point on $\Gamma$ is non-characteristic, then there exists an open set $\tilde\Omega\subseteq\Omega$ such that $\Gamma\subset\overline{\tilde\Omega}$ and a unique continuously differentiable function $u:\tilde\Omega\rightarrow\Re$ that is continuous on $\overline{\tilde\Omega}$ and satisfies the system. Under similar conditions, one can extend to $\bar I$ when $I$ is bounded.

## Inverse Function Theorem:
Let $U\subset\Re^n$ be an open set, and $\underline{f}:U\rightarrow\Re^n$ be continuously differentiable. Let $\underline{x}_0\in U$, if:$$\Huge D\underline{f}(\underline{x}_0)=\begin{pmatrix}\frac{\partial f_1}{\partial x_1} & \dots & \frac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_n}{\partial x_1} & \dots & \frac{\partial f_n}{\partial x_n}\end{pmatrix}|_{\underline{x}=\underline{x}_0}$$is invertible then $\underline{f}$ is invertible in a neighbourhood of $\underline{x}_0$. This means that there exist open sets $V\subset U,W\subset\Re^n$ such that $\underline{x}_0\in\ V,\underline{f}(\underline{x}_0)\in W$, and $\underline{f}:V\rightarrow W$ is a bijection and hence invertible. Moreover, the inverse $\underline{f}^{-1}:W\rightarrow W$ is continuously differentiable with:$$\Huge D\underline{f}^{-1}(\underline{y})=(D\underline{f}(\underline{f}^{-1}(y)))^{-1}$$
## Proof of local well-posedness:
Consider the family of ODEs:$$\Huge\begin{cases}\partial_\tau\underline{X}(\tau,\underline{s})=\underline{a}(\underline{X}(\tau,\underline{s}),z(\tau,\underline{s}))\\
\partial_\tau z(\tau,\underline{s})=b(\underline{X}(\tau,\underline{s}),z(\tau,\underline{s}))\end{cases}$$with initial conditions:$$\Huge\begin{cases}\underline{X}(0,\underline{s})=\underline{x}_0(\underline{s}) & s\in I \\
z(0,\underline{s})=u_0(\underline{x}_0(\underline{s})) & s\in I\end{cases}$$Since $\underline{a},b,\underline{x}_0,u_0\circ\underline{x}_0$ are $C^1$ in a neighbourhood of $(0,\underline{x}_0)$ there exists some $\tilde\epsilon(\underline{s}_0)>0$ and $\tilde M(\underline{s}_0)>0$ such that there exists a unique solution to the family:$$\Huge\underline{X}:(-\tilde\epsilon(\underline{s}_0),\tilde\epsilon(\underline{s}_0))\times B_{\tilde M(\underline{s}_0)}(\underline{s}_0)\rightarrow B_{M_1(\underline{x}_0(\underline{s}_0))}(\underline{x}_0(\underline{s}_0))$$with corresponding $z$ function. This is due to the local existence and uniqueness with continuous dependence in parameters. Next, we would like to invert:$$\Huge(\tau,\underline{s})\rightarrow\underline{X}(\tau,\underline{s})$$To do this, we use the inverse function theorem stated above:$$\Huge D_{(\tau,\underline{s})}\underline{X}(\tau,\underline{s})=\begin{pmatrix}\partial_\tau\underline{X}(\tau, \underline{s})) & D_\underline{s}\underline{X}(\tau,\underline{s})\end{pmatrix}=\begin{pmatrix}\underline{a}(\underline{X}(\tau,\underline{s})) & D_\underline{s}\underline{X}(\tau,\underline{s)}\end{pmatrix}$$So for the boundary conditions:$$\large D_{(\tau,\underline{s})}\underline{X}(0,\underline{s}_0)=\begin{pmatrix}\underline{a}(\underline{X}(0,\underline{s}_0)) & D_\underline{s}(\underline{X}(0,\underline{s}_0)\end{pmatrix}=\begin{pmatrix}\underline{a}(\underline{x}_0(\underline{s}_0)) & D_\underline{s}(\underline{x}_0(\underline{s}_0))\end{pmatrix}$$This is invertible, as $\underline{x}_0(\underline{s}_0)$ is a non-characteristic point. Therefore by the inverse function theorem we can find $\epsilon(\underline{s}_0)<\tilde\epsilon(\underline{s}_0)$ and $M_1(\underline{s}_0)<\tilde M(\underline{s}_0)$ such that:$$\Huge \underline{X}(\tau,\underline{s}_0):(-\epsilon(\underline{s}_0),\epsilon(\underline{s}_0))\times B_{M_1(\underline{s}_0)}(\underline{s}_0)\rightarrow U$$is a $C^1$ bijection for some open set $U\subset B_{M_1(\underline{x_0}(\underline{s}_0))}(\underline{x}_0(\underline{s}_0))$ with $\underline{x}_0(\underline{s}_0)$ within it. Therefore there exists some $R(\underline{x}_0(\underline{s}_0))$ such that:$$\Huge B_{R(\underline{x}_0(\underline{s}_0))}(\underline{x}_0(\underline{s}_0))\subseteq U$$and:$$\Huge (\tau(\underline{x}),\underline{s}(\underline{x}))=\underline{X}^{-1}(\underline{x})\in B_{R(\underline{x}_0(\underline{s}_0))}(\underline{x}_0(\underline{s}_0))$$is well defined and $C^1$. We then define $u:B_{R(\underline{x}_0(\underline{s}_0))}(\underline{x}_0(\underline{s}_0))\rightarrow\Re$ by $u(\underline{x})=z(\tau(\underline{x}),\underline{s}(\underline{x}))$ which is $C^1$ as it is a composition of $C^1$ maps. 

It remains to check that this solutions satisfies the ODEs as well as boundary conditions. First we aim to check that $u|_{\Gamma\cap B_{R(\underline{x}_0(\underline{s}_0))}(\underline{x}_0(\underline{s}_0))}=u_0|_{\dots}$. Since the ball is in the domain where characteristics are defined, there exists some characteristic $\underline{X}(\tau,\underline{s})$:$$\Huge \underline{X}(0,\underline{s}_1)=\underline{x}_0(\underline{s}_1)=\underline{x}$$By invertibility of the flow, we have that $\tau(\underline{x})=0$ and $\underline{s}(\underline{x})=\underline{s}_1$. This implies that:$$\Huge u(\underline{x})=z(\tau(\underline{x}),\underline{s}(\underline{x}))=z(0,\underline{s}_1)=u_0(\underline{x}_0(\underline{s}_1))=u_0(\underline{x})$$This shows that general points on the boundary hold.

We now show that the PDE holds. To do this, we need to differentiate $u$ wrt $\underline{x}$ and as such $\tau,\underline{s}$ wrt to $\underline{x}$. By the inverse function theorem:$$\Huge D(\tau,\underline{s})|_\underline{X}\cdot D\underline{X}|_{(\tau(\underline{x}),\underline{s}(\underline{x}))}=\mathbb{I}$$which can be shown trivially. Next:$$ \underline{a}(\underline{x},u(\underline{x}))\cdot\underline{\nabla}u(\underline{x})=\sum_{l=1}^na_l(\underline{x},u(\underline{x}))\cdot\left(\partial_\tau z\left(\tau(\underline{x}),\underline{s}\left(\underline{x}\right)\right)\frac{\partial \tau}{\partial x_l}(\underline{x})+\sum_{i=1}^{n-1}\partial_{s_i}z(\tau(\underline{x}),\underline{s}(\underline{x}))\cdot\frac{\partial s_i}{\partial x_l}(\underline{x})\right)$$which is simply:$$\large\begin{align*}
\underline{a}(\underline{x},u(\underline{x}))\cdot\underline{\nabla}u(\underline{x})&=b(\underline{x},u(\underline{x}))\cdot\sum_{l=1}^na_l(\underline{x},u(\underline{x}))\cdot\frac{\partial z}{\partial x_l}(\underline{x})\\
&+\sum_{i=1}^{n-1}\partial_{s_i}z(\tau(x),\underline{s}(x))\sum_{l=1}^na_l(x,u(x))\frac{\partial s_i}{\partial x_l}(x)\\
&=b(\underline{x},u(\underline{x}))\cdot\sum_{l=1}^na_l(X(\tau(x),\underline{s}(x)))\cdot\frac{\partial z}{\partial x_l}(X(\tau(x),\underline{s}(x)))+0\\
&=b(\underline{x},u(\underline{x}))
\end{align*}$$Therefore a solution exists. This must be the unique solution in $B_{R(\underline{x}_0)(\underline{s}_0)}(\underline{x}_0(\underline{s}_0))$ since we know that $z$ is uniquely there and $(\tau,\underline{s})\rightarrow\underline{X}$ is invertible. This concludes the proof for the local result. The global result holds following the global well posedness of ODE systems and the fact that $\Gamma$ is non characteristic.

This non characteristic condition is essential, to show this we consider the example:$$\Huge\begin{cases}\partial_xu(x,y)+\partial_yu(x,y)=1&(x,y)\in\Re^2 \\
u(x,x)=x&x\in\Re\end{cases}$$We have $\Omega=\Re^2$ and the Cauchy curve $\Gamma=\{(x,x):x\in\Re\}$ which is parametrised by $x_0(s)=s,y_0(s)=s$ and $s\in\Re$. The leading vector field is $\underline{a}(x,y,u)=(1,1)$ and the source term is $b(x,y,u)=1$:![[The Method of Characteristics 2025-11-11 19.04.51.excalidraw]]We see that the leading vector field keeps us on the boundary, and we cannot escape it into the domain. The points are all non characteristic:$$\Huge\begin{align*}
a_1(x_0(s),y_0(s))\partial_sy_0(s)-a_2(x_0(s),y_0(s))\partial_sx_0(s)&=1\cdot1-1\cdot1\\
&=0
\end{align*}$$for all $s\in\Re$. Writing the equation with the method of characteristics gives:$$\Huge\begin{cases}\partial_\tau X(\tau,s)=1 \\
\partial_\tau Y(\tau,s)=1 \\
\partial_\tau z(\tau,s)=1\end{cases},\,\,\begin{cases}X(0,s)=x_0(s)=s \\
Y(0,s)=y_0(s)=s \\
z(0,s)=u(x_0(s),y_0(s))=s\end{cases}$$Therefore $X(\tau,s)=Y(\tau,s)=z(\tau,s)=\tau+s$, which is not invertible as you cannot reconstruct expressions for $\tau,s$ individually. 