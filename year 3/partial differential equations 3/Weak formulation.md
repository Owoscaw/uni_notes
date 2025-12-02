
We saw that in "simple" settings, we can find [[year 3/partial differential equations 3/Conservation laws#Breakdown of classical solutions|classical solutions to conservation laws]] up to some critical time. We would like to extend our solutions past this critical time and get some notion of a solution in $\Re\times(0,\infty)$. One issue with this is the derivatives blowing up at critical time, so we try to find a way to circumvent them. 

To do this, we can try to recast the PDE in an integral form and move the derivatives to some other function. Such functions must belong to a well behaved class in order to retain PDE information. 

Let $X\subseteq\Re^n$ and let $\varphi:X\rightarrow\Re$. The support of $\varphi$, denoted by $\text{supp}(\varphi)$, is the set defined by:$$\Huge \text{supp}(\varphi)=\overline{\{\underline{x}\in X:\varphi(\underline{x})\neq0\}}$$We say that a function $\varphi$ has compact support if this set if compact. In a sense, this function captures all of the points on which $\varphi\neq0$. Let $X\subseteq\Re^n$ and let $k\in\mathbb{N}\cup\{0\}\cup\{\infty\}$. The set $C_c^k(X)$ is defined as the set of all compactly supported functions that belong to $C^k(X)$.

For any $\epsilon>0$ we define the standard mollifier as:$$\Huge \varphi_\epsilon(x)=\begin{cases}\exp(-\frac{1}{1-(x/\epsilon)^2})&|x|<\epsilon \\
0&|x|\geq\epsilon\end{cases}$$Then $\varphi_\epsilon\in C_c^\infty(\Re)$ for all $\epsilon>0$ and $\text{supp}(\varphi_\epsilon)=[-\epsilon,\epsilon]$.

Let $u:\Re\times[0,\infty)\rightarrow\Re$ be a classical solution to the conservation law:$$\Huge\begin{cases}\partial_tu(x,t)+\partial_xf(u(x,t))=0&(x,t)\in\Re\times(0,\infty) \\
u(x,0)=u_0(x)&x\in\Re\end{cases}$$where $f:\Re\rightarrow\Re$ is continuously differentiable. Then for any $\varphi\in C_c^1(\Re\times[0,\infty))$ we have that:$$\large\int_0^\infty\int_\Re(u(x,t)\partial_t\varphi(x,t)+f(u(x,t))\partial_x\varphi(x,t))dx\,dt+\int_\Re u_0(x)\varphi(x,0)dx=0$$Proof:
> Multiplying our PDE by $\varphi(x,t)$ and integrating yields:$$\Huge\int_0^\infty\int_\Re(\partial_tu(x,t)+\partial_xf(u(x,t)))\varphi(x,t)dx\,dt=0$$Note that as $\varphi\in C_c^1(\Re\times[0,\infty))$, we can find some $\mu,t_1>0$ such that:$$\Huge\text{supp}(\varphi)\subset[-\mu,\mu]\times[0,t_1]$$
> Using integration by parts:$$\begin{align*}
0&=\int_0^\infty\int_\Re(\partial_tu(x,t)+\partial_xf(u(x,t)))\varphi(x,t)dx\,dt\\
&=\int_0^{2t_1}\int_{-2\mu}^{2\mu}(\partial_tu(x,t)+\partial_xf(u(x,t)))\varphi(x,t)dx\,dt\\
&=\int_{-2\mu}^{2\mu}[u(x,2t_1)\varphi(x,2t_1)-u(x,0)\varphi(x,0)]-\int_0^{2t_1} u(x,t)\partial_t\varphi(x,t)dt\,dx\\
&+\int_0^{2t_1}[f(u(2\mu,t))\varphi(2\mu,t)-f(u(-2\mu,t))\varphi(-2\mu,t)]-\int_{-2\mu}^{2\mu}f(u(x,t))\partial_x\varphi(x,t)dx\,dt\\
&=-\int_0^\infty\int_\Re u(x,t)\partial_t\varphi(x,t)+f(u(x,t))\partial_x\varphi(x,t)dx\,dt-\int_\Re u(x,0)\varphi(x,0)dx
\end{align*}$$Concluding the proof.

This motivates the weak formulation of conservation laws. A bounded function $u:\Re\times[0,\infty)\rightarrow\Re$ is called a weak integral solution of the scalar conservation law$$\Huge\begin{cases}\partial_tu(x,t)+\partial_xf(u(x,t))&(x,t)\in\Re\times(0,\infty) \\
u(x,0)=u_0&x\in\Re\end{cases}$$if for any $\varphi\in C_c^1(\Re\times[0,\infty))$ we have that:$$\large \int_{t=0}^\infty\int_\Re(u(x,t)\partial_t\varphi(x,t)+f(u(x,t))\partial_x\varphi(x,t))dx\,dt+\int_\Re u_0(x)\varphi(x,0)dx=0$$We refer to the functions $\varphi$ as test functions.

Considering our conservation law, if $u$ is a bounded classical solution then it is a weak integral solution to the conservation law. Conversely if $u$ is a weak integral solution to the conservation law that is continuously differentiable on $\Re\times(0,\infty)$, then it is a classical solution to the conservation law.

## The fundamental lemma of the calculus of variations:
Let $g:\Omega\rightarrow\Re$ be a continuous function on an open set $\Omega\subseteq\Re^n$. If$$\Huge\int_\Omega g(\underline{x})\psi(\underline{x})d\underline{x}=0,\,\,\forall\psi\in C_c^\infty(\Omega)$$then $g=0$. Proof (sketch):
> Assume $g\neq0$, then $\exists x_0\in\Omega$ such that $g(x_0)\neq0$. WLOG assume $g(x_0)>0$.
> As $g$ is continuous, $\exists\epsilon>0$ such that $g(x)>\frac{g(x_0)}{2}$ for all $x\in B_\epsilon(x_0)$.
> Consider $\psi(x)=\varphi_\epsilon(|x-x_0|)$ where $\varphi_\epsilon$ is the standard mollifier. Then $\psi\geq0,\psi\in C_c^\infty(\Re^n)$ and $\text{supp}(\psi)=\overline{B_\epsilon(x_0)}$.
> We find that:$$\Huge0=\int_\Omega g(x)\psi(x)dx=\int_{B_\epsilon(x_0)}g(x)\psi(x)dx>\frac{g(x_0)}{2}\int_{B_\epsilon(x_0)}\psi(x)dx>0$$This is a contradiction, so $g=0$, as required.

We saw that if $u$ is a classical solution, then it satisfies the integral equation of weak solutions. If, in addition, $u$ is bounded then by definition it is a weak integral solution.

Assume $u$ is a weak solution that is $C^1$ in $\Re\times(0,\infty)$ and continuous on $\Re\times[0,\infty)$. Then for any $\varphi\in C_c^1(\Re\times(0,\infty))$ (that is $\varphi|_{\Re\times\{0\}}=0$), using integration by parts and the fact that $\varphi$ is completely supported in $\Re\times(0,\infty)$ we get that:$$\Huge\begin{align*} 
0&=\int_0^\infty\int_\Re u(x,t)\partial_t\varphi(x,t)+f(u(x,t))\partial_x\varphi(x,t)dx\,dt+0\\
&=\int_\Re u(x,t)\varphi(x,t)|_{t=0}^{t=\infty}dx-\int_0^\infty\int_\Re\partial_tu(x,t)\varphi(x,t)dx\,dt\\
&+\int_0^\infty f(u(x,t))\varphi(x,t)|_{t=0}^{t=\infty}dt-\int_0^\infty\int_\Re\partial_x f(u(x,t))\varphi(x,t)dx\,dt\\
&=-\int_0^\infty\int_\Re(\partial_tu(x,t)+\partial_xf(u(x,t)))\varphi(x,t)dx\,dt
\end{align*}$$Now using the fact that $\Re\times(0,\infty)$ is open and that $u_t+f(u)$ is continuous, we have that the above holds for any $\varphi\in C_c^\infty(\Re\times(0,\infty))$. We can therefore use the fundamental lemma of calculus of variations that:$$\Huge\partial_tu(x,t)+\partial_x f(u(x,t))=0,\,\,\forall(x,t)\in\Re\times(0,\infty)$$One can also recover boundary conditions by using the same argument for the case where $\varphi\in C_c^1(\Re\times[0,\infty))$. Note that we could have chosen $C_c^\infty(\Re\times[0,\infty))$ as the test function space, and is in fact an equivalent definition.

# Existence of weak solutions:

Let $f\in C^\infty(\Re)$. Assume that $f$ is uniformly convex, which for twice differentiable $f$, is equivalent to saying that there exists some $\lambda>0$ such that:$$\Huge f''(x)\geq\lambda>0,\,\,x\in\Re$$Let $u_0\in L^\infty(\Re)$. Then there exists a weak solution $u\in L^\infty(\Re\times[0,\infty))$ of the conservation law:$$\Huge\begin{cases}\partial_tu(x,t)+\partial_xf(u(x,t))=0&(x,t)\in\Re\times(0,\infty) \\
u(x,0)=u_0(x), & x\in\Re\end{cases}$$
## Example:
Take for example the conservation law:$$\Huge\begin{cases}\partial_tu(x,t)+u(x,t)\partial_xu(x,t)=0&(x,t)\in\Re\times(0,\infty) \\
u(x,0)=e^{-x^2}&x\in\Re\end{cases}$$Here we have $f(u)=u^2/2$ with $f\in C^\infty(\Re)$ and $f''(u)=1>0$. Therefore there exists a weak solution on $\Re\times[0,\infty)$, the classical solution will show that $t_c<\infty$. That is, there is a classical solution on $\Re\times[0,t_c)$ however we get a weak solution on a larger range.

# Rankine-Hugoniot condition and shocks:

We want to find a potential weak integral solution for a general conservation law. One possibility is to find a classical solution in two regions but somehow breaks down in the interface between the two domains. One example would be regions defined by characteristics before they meet:
![[Weak formulation 2025-12-02 17.52.39.excalidraw]]

Here, we have two domains $U_l,U_r$ where the solution behaves classically, but there is a discontinuity/breakdown along $C$, the border on which they meet. We ask what the weak solution would look like in this case.

Let $U\subset\Re\times(0,\infty)$ be an open set and let $\sigma:(t_1,t_2)\rightarrow\Re$ be continuously differentiable. Define the curve $C=\{(\sigma(t),t):t\in(t_1,t_2)\}$ and let:$$\Huge\begin{align*}
U_l&=\{(x,t)\in U:x<\sigma(t)\}\\
U_r&=\{(x,t)\in U:x>\sigma(t)\}
\end{align*}$$That is, $U_l\subset U$ is the region to the left of $C$ and $U_r\subset U$ is the region to the right of $C$. Let $u\in L^\infty(\Re\times[0,\infty))$ be a weak solution of the conservation law:$$\Huge\begin{cases}\partial_tu(x,t)+\partial_xf(u(x,t))=0&(x,t)\in\Re\times(0,\infty) \\
u(x,0)=u_0(x)&x\in\Re\end{cases}$$where $f\in C^1(\Re)$ and $u_0\in L^\infty(\Re)$. Assume that $u$ is continuously differentiable in $U_l,U_r$, $u$ is uniformly continuous in $U_l,U_r$, but discontinuous across $C$. For $(x,t)\in C$, let $u_l(x,t)$ and $u_r(x,t)$ denote the limit of $u$ as $(x,t)$ is approached from the left and from the right:$$\Huge\begin{align*}
u_l(x,t)&=\lim_{(y,s)\to(x,t),\,\,(y,s)\in U_l}u(y,s)\\
u_r(x,t)&=\lim_{(y,s)\to(x,t),\,\,(y,s)\in U_r}u(y,s)
\end{align*}$$Define $[[u]]:C\rightarrow\Re$  and $[[f(u)]]:C\rightarrow\Re$ by:$$\Huge\begin{align*}
[[u]]&=u_l-u_r=\text{jump in }u\text{ across }C\\
[[f(u)]]&=f(u_l)-f(u_r)=\text{jump in }f(u)\text{ across }C
\end{align*}$$Then $u$ satisfies the PDE:$$\Huge \partial_tu(x,t)+\partial_xf(u(x,t))=0$$in $U_l,U_r$ and on $C$ it satisfies the jump condition:$$\Huge [[f(u)]](\sigma(t),t)=\dot\sigma(t)[[u]](\sigma(t),t)$$This is known as the Rankine-Hugoniot condition. The curve $C$ is called a shock. Note that the fact $u$ is uniformly continuous on $U_l,U_r$ imposes that $u_l(x,t),u_r(x,t)$ exist. A simple, equivalent, condition would be that the derivatives of $u$ in each region are bounded. Proof:
> We have that $u$ is a weak solution, so $\forall\varphi\in C_c^\infty(\Re\times[0,\infty))$ we have:$$\large\iint(u(x,t)\partial_t\varphi(x,t)+f(u(x,t))\partial_x\varphi(x,t))dx\,dt+\int u_0(x)\varphi(x,0)dx=0$$with appropriate limit conditions that I have omitted. Therefore for any $\varphi\in C_c^1(U)$ we have the above as we can decompose $U$$$\Huge U=U_l\cup U_r\cup (C\cap U)$$into adjoint sets, $C\cap U$ is a one dimensional curve, and $u\partial_t\varphi+f(u)\partial_x\varphi$ is bounded. This last condition implies:$$\Huge \iint_{C\cap U}u\partial_t\varphi+f\partial_x\varphi\,dx\,dt=0$$We therefore find that:$$\Huge\begin{align*} 0&=\iint_Uu(x,t)\partial_t\varphi(x,t)+f(u(x,t))\partial_x\varphi(x,t)dx\,dt+\int_\Re0\,dx\\
&=\iint_{U_l}u\partial_t\varphi+f\partial_x\varphi\,dx\,dt+\iint_{U_r}u\partial_t\varphi+f\partial_x\varphi\,dx\,dt
\end{align*}$$
> Focusing on $U_l$, we aim to use the fact that $u\in C_1(U_l)$ to integrate by parts (in a higher dimension using [[Integral theorems#Divergence theorem|divergence theorem]]):$$\Huge\begin{align*} u\partial_t\varphi+f(u)\partial_x\varphi&=\underline{\nabla}_{(x,t)}\varphi\cdot(f(u),u)\\
&=\text{div}_{(x,t)}((f(u),u)\varphi)-(\text{div}_{(x,t)}(f(u),u))\varphi\\
&=\text{div}_{(x,t)}((f(u),u)\varphi)-\varphi(\partial_tu+\partial_xf(u))
\end{align*}$$So using divergence theorem we find that:$$\Huge\begin{align*}
I&=\iint_{U_l}u(x,t)\partial_t\varphi(x,t)+f(u(x,t))\partial_x\varphi(x,t)\,dx\,dt\\
&=-\iint_U(\partial_tu(x,t)+\partial_xf(u(x,t)))\varphi(x,t)\,dx\,dt\\
&+\int_{\partial U_l}(f(u(y,s)),u(y,s))\varphi(y,s)\cdot\underline{\hat{n}}(y,s)\,dL(y,s)
\end{align*}$$where $\underline{\hat{n}}$ is outward normal along $C$ from $U_l$ (points towards $U_r$). Here, $\partial U_l=(\partial U\cap\overline U_l)\cup(C\cap U)$. Then as $\varphi\in C_c^1(U)$ we must have $\varphi|_{\partial U}=0$, which makes the integral bounds:$$\Huge \int_{\partial U_l}\dots dL(y,s)=\int_{C\cap U}\dots dL(y,s)$$
> The curve $C$ is parametrised by $(\sigma(t),t)$ for $t\in(t_1,t_2)$, so a tangent vector is $(\dot\sigma(t),1)$. As such, the unit normal vector has form:$$\Huge\underline{\hat{n}}=\frac{\pm1}{\sqrt{1+\dot\sigma(t)^2}}(1,-\dot\sigma(t))$$