
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

## Burgers equation example:
Consider Burgers equation:$$\Huge\begin{cases}\partial_tu(x,t)+\partial_xf(u(x,t))=0&(x,t)\in\Re\times(0,\infty) \\
u(x,0)=u_0(x)&x\in\Re\end{cases}$$where:$$\Huge u_0(x)=\begin{cases}1&x\leq0 \\
1-x&0<x\leq1 \\
0&x>1\end{cases}$$Here we have:$$\Huge c(u_0(s))=1,\,\,\partial_sc(u_0(s))=0,\,\,I_{(-\infty,0)}=\emptyset,\,\,t_c^{(-\infty,0)}=\infty$$Implying that:$$\Huge\implies\mathcal{D}_{(-\infty,0)}=\{(x,t)\in\Re\times(0,\infty):-\infty<x<t\}$$where the characteristics are of form $x=s+c(u_0(s))t=s+t$. Considering the problem on $(0,1)$ and $(1,\infty)$ we find characteristics:$$\Huge\begin{align*}
x_{(-\infty,0)}&=s+t\\
x_{(0,1)}&=s(1-t)+t\\
x_{(1,\infty)}&=s
\end{align*}$$As long as $t\in[0,1)$ we can stitch these solutions together in a continuous way, but not $C^1$ on the joint boundaries of $\mathcal{D}_{(-\infty,0)},\mathcal{D}_{(0,1)},\mathcal{D}_{(1,\infty)}$:$$\Huge u(x,t)=\begin{cases}1&x\leq t&t\in[0,1) \\
\frac{1-x}{1-t}&t\leq x\leq1&t\in[0,1) \\
0&x\geq1&t\in[0,1)\end{cases}$$![[Weak formulation 2025-12-11 03.48.04.excalidraw]]So we ask how we can create a weak solution on $\Re\times(0,\infty)$. We can try this by extending the non-terminating characteristics:![[Weak formulation 2025-12-11 03.52.12.excalidraw]]We expect a discontinuity of $u$ as from the left we see $1$ and from the right $0$. We can utilise the Rankine-Hugoniot theorem as $f(u)=u^2/2$ we get:$$\Huge \frac{1^2-0^2}{2}=\dot\sigma(t)(1-0)\implies\dot\sigma(t)=\frac{1}{2}$$As our shock will start at the point characteristics begin to cross, $(-1,1)$, we have $\sigma(1)=1$. This makes $\sigma$ take form:$$\Huge \sigma(t)=1+\frac{t}{2}$$The characteristics of our new function become:![[Weak formulation 2025-12-11 03.58.08.excalidraw]]with:$$\Huge u(x,t)=\begin{cases}t&t\leq x&t\in[0,1) \\
\frac{1-x}{1-t}&t\leq x\leq 1&t\in[0,1) \\
0&x\geq1&t\in[0,1) \\
1&x<\frac{1+t}{2}&t\geq1 \\
0&x>\frac{1+t}{2}&t\geq1\end{cases}$$As $u\in C^1$ in domains between connecting characteristics, including the boundary of $\mathcal{D}$, and the Rankine-Hugoniot conditions are satisfied. We have therefore found a weak solution. Note that shocks need not form at some $t>0$, they can form at $t=0$ instantaneously.

# Non-uniqueness of weak integral solutions:

The price for weakening the condition for existence is lack of uniqueness. Note that a conservation law where the initial datum is a piecewise constant function with one discontinuity is known as a Riemann problem.

Consider the example:$$\Huge\begin{cases}\partial_tu(x,t)+u(x,t)\partial_xu(x,t)&(x,t)\in\Re\times(0,\infty) \\
u(x,0)=u_0(x)&x\in\Re\end{cases},\,\,u_0(x)=\begin{cases}0&x<0 \\
1&x>0\end{cases}$$Here, $f(u)=u^2/2,c(u)=u,c(u_0(s))=u_0(s)$ which is not in $C^1(\Re)$. Therefore we cannot use the classical solution theorem on $\Re$, however we can use it on $(-\infty,0),(0,\infty)$ as $c\circ u_0$ is bounded with a bounded derivative. We then get the following characteristics:$$\Huge\begin{align*}
x_{(-\infty,0)}&=s\\
x_{(0,\infty)}&=s+t
\end{align*}$$which we combine. We are however left with a void on $t>x$ for $x>0$, which we have two ways of "filling":
> We can extend $u$ on parallel characteristics, causing them to immediately cross. We are in the setting to try the Rankine-Hugoniot condition for a shock emerging from $(0,0)$. Here, $u_l=0,u_r=1$ and $f(u)=u^2/2$ so we find $\dot\sigma(t)=1/2$ and using the fact $\sigma(0)=0$ we find $\sigma(t)=t/2$, making our weak solution:$$\Huge u(x,t)=\begin{cases}0&x<t/2 \\
1&x>t/2\end{cases}$$![[Weak formulation 2025-12-11 04.34.37.excalidraw]]
> Another option would be to form a Rarefaction wave. When we have a classical solution it is:$$\Huge u(x,t)=u_0(s(x,t))=c(u_0(s(x,t)))$$where $u(x,t)$ is therefore the reciprocal of the slope of the characteristics in the $(x,t)$ plane. We can try to create artificial characteristics that connect between the rightmost characteristic of $\mathcal{D}_{(-\infty,0)}$ where $x=0$ and the leftmost on $\mathcal{D}_{(0,\infty)}$ with $x=t$ in any continuous way and set $u$ to depend only on the reciprocal slope. 

## Rarefaction waves:
We try a solution of the form:$$\Huge u(x,t)=h\left(\frac{x-0}{t}\right)$$where $h$ is a single valued function. We need $u$ to satisfy:$$\Huge\begin{align*}
\partial_tu+u\partial_xu&=0\\
\partial_tu(x,t)&=-\frac{x}{t^2}h'\left(\frac{x}{t}\right)\\
\partial_xu(x,t)&=\frac{1}{t}h'\left(\frac{x}{t}\right)\\
0=\partial_tu(x,t)-u(x,t)\partial_xu(x,t)&=\frac{h'(x/t)}{t}\left(-\frac{x}{t}+h\left(\frac{x}{t}\right)\right)
\end{align*}$$There are two obvious options:
> $h'(z)=0$ implies $h$ is constant, but there $u$ is also constant which does not connect between $x=0$ and $x=t$.
> $h(z)=z$ works.

We therefore define the continuous function:$$\Huge u(x,t)=\begin{cases}0&x<0 \\
\frac{x}{t}&0\leq x\leq t \\
1&x>1\end{cases}$$with $t>0$. Then we have $u\in C^1$ in $\mathcal{D}_{(-\infty,0)}\cup\mathcal{D}_{(0,\infty)}\cup V$ is a weak solution:![[Weak formulation 2025-12-11 04.51.24.excalidraw]]
Note that Rarefaction waves will always be a possibility in Burger's equation with increasing piecewise constant functions $u_0$. At any point of discontinuity $x_0$ where $u_{x_0,l}=\lim_{x\to x_0^-}u_0(x)<\lim_{x\to x_0^+}u_0(x)=u_{u_0,r}$, a void will be created in the domain:$$\Huge V_{x_0}=\{(x,t)\in\Re\times(0,\infty):x_0+u_{x_0,l}t<x<x_0+u_{x_0,r}t\}$$The function:$$\Huge u(x,t)=\frac{x-x_0}{t},\,\,(x,t)\in V_{x_0}$$will solve our PDE and act as a continuous extension of our solution to $V_{x_0}$.

Moreover, rarefaction waves are also possible when $c(u)=\gamma u^n$ with $\gamma>0$ and $n\in\mathbb{N}$. In this case wen considering a piecewise constant function $u_0$, we will have that at any point of discontinuity $x_0$ where:$$\Huge u_{x_0,l}^n=\lim_{x\to x_0^-}u_0(x)^n<\lim_{x\to x_0^+}u_0(x)^n=u_{x_0,r}^n$$a void will be created in the domain:$$\Huge V_{x_0}=\{(x,t)\in\Re\times(0,\infty):x_0+\gamma u_{x_0,l}^nt<x<x_0+\gamma u_{x_0,r}^nt\}$$and the function:$$\Huge u(x,t)=\left(\frac{x-x_0}{\gamma t}\right)^{1/n},\,\,(x,t)\in V_{x_0}$$will solve our PDE and act as a continuous extension of our solution to $V_{x_0}$. It is worth to note that the above is well defined as when $n$ is even we have that:$$\Huge 0\leq\gamma u_{x_0,l}^nt<x-x_0$$
## Combinations:
We have one more option for filling the void, mixing both techniques. We can create a rarefaction wave from one or both sides and then extend parallelly and create a shock. For any $0<\gamma<1$ we define:$$\Huge u_\alpha(x,t)=\begin{cases}0&x<\frac{\alpha t}{2} \\
\alpha&\frac{\alpha t}{2}<x<\alpha t \\
\frac{x}{t}&\alpha t<x<t \\
1&x>t\end{cases}$$where we get a rarefaction wave in:$$\Huge \{(x,t)\in\Re\times(0,\infty):\alpha t<x<t\}$$and a shock curve along:$$\Huge C=\left\{\left(\frac{\alpha t}{2},t\right):t>0\right\}$$![[Weak formulation 2025-12-11 05.04.45.excalidraw]]
# Entropy conditions:

A selection criterion for weak integral solution was proposed by Peter Lax in the 1960s:

A shock $C$ is said to satisfy Lax' entropy condition if:$$\Huge c(u_r(\sigma(t),t))<\dot\sigma(t)<c(u_l(\sigma(t),t)),\,\,\forall(\sigma(t),t)\in C$$A weak integral solution for a conservation law is said to satisfy Lax' entropy condition if all of its shocks satisfy the above.

The geometric interpretation of this condition is equivalent to the notion that characteristics cannot emerge from shocks. This fits our physical intuition that we cannot trace back along characteristics to a discontinuity:![[Weak formulation 2025-12-27 15.03.50.excalidraw]]
Take for example Burger's equation:$$\Huge \begin{cases}\partial_tu(x,t)+u(x,t)\partial_xu(x,t)=0&(x,t)\in\Re\times(0,\infty) \\
u(x,0)=u_0(x)&x\in\Re\end{cases}$$with $u_0(x)=\begin{cases}0&x<0 \\1&x>0\end{cases}$. The only weak integral solution out of the infinitely many we presented that satisfies Lax' entropy condition is the one involving only a rarefaction wave. As this had no shock curves, it automatically satisfies the condition.

Assume that the flux function $f$ of our conservation law is in $C^2(\Re)$ and is uniformly convex. Then a shock curve $C$ will satisfy Lax' entropy condition if and only if:$$\Huge u_l(\sigma(t),t)>u_r(\sigma(t),t),\,\,\forall(\sigma(t),t)\in C$$Proof:
> A shock curve is defined by the Rankine-Hugoniot condition:$$\Huge f(u_l(\sigma(t),t))-f((\sigma(t),t))=\dot\sigma(t)(u_l(\sigma(t),t)-u_r(\sigma(t),t))$$When $f$ is continuously differentiable we can use the mean value theorem for any given $t$ to find some $u_*(\sigma(t),t)$ between $u_l,u_r$ such that:$$\large f'(u_*(\sigma(t),t))(u_l(\sigma(t),t)-u_r(\sigma(t),t))=\dot\sigma(t)(u_l(\sigma(t),t)-u_r(\sigma(t),t))$$From which we can conclude that:$$\Huge c(u_*(\sigma(t),t))=f'(u_*(\sigma(t),t))=\dot\sigma(t)$$Since by definition $u_l\neq u_r$. In addition we notice that as $c'=f''\geq\lambda>0$, $c$ must be strictly increasing. If $u_l>u_r$ we can use the monotonicity of $c$ and the fact that:$$\Huge u_r(\sigma(t),t)<u_*(\sigma(t),t)<u_l(\sigma(t),t)$$to conclude:$$\Huge c(u_r(\sigma(t),t))<c(u_*(\sigma(t),t))=\dot\sigma(t)<c(u_l(\sigma(t),t))$$as required.
> Conversely if the entropy condition is satisfied then:$$\Huge c(u_r(\sigma(t),t))<c(u_l(\sigma(t),t))\implies u_l>u_r$$as $c$ is monotone.

While Lax' entropy condition usually limits the number of weak integral solutions, it is not enough to guarantee uniqueness. To achieve uniqueness we must look at a more refined notion of entropy solutions introduced by Stanislav Kruzhkov.

We say that a weak integral solution to the conservation law:$$\Huge\begin{cases}\partial_tu(x,t)+\partial_xf(u(x,t))=0&(x,t)\in\Re\times(0,\infty) \\
u(x,0)=u_0(x)&x\in\Re\end{cases}$$is an entropy solution if there exists some constant $C>0$ such that $u$ satisfies the one-sided jump condition:$$\Huge u(x+z,t)-u(x,t)\leq C\left(1+\frac{1}{t}\right)z$$for all $(x,t)\in\Re\times(0,\infty)$ and $z>0$. It can be shown that if $u$ is an entropy solution to a conservation law with a uniformly convex flux function $f$, then $u$ automatically satisfies Lax' entropy condition. These solutions are the "right" solutions to look for in many cases.

## Existence and uniqueness of entropy solutions:
Consider the conservation law:$$\Huge\begin{cases}\partial_tu(x,t)+\partial_xf(u(x,t))&(x,t)\in\Re\times(0,\infty) \\
u(x,0)=u_0(x)&x\in\Re\end{cases}$$and assume that $f\in C^\infty(\Re)$ is uniformly convex and that $u_0\in L^\infty(\Re)$. Then there exists a unique entropy solution to the conservation law. The proof of this is beyond the scope of these notes.

Recall that we showed that:$$\Huge u(x,t)=\begin{cases}0 & x<0 \\
x/t & 0\leq x<t,t>0 \\
1 & x>t\end{cases}$$is a continuous weak integral solution to the conservation law above with $f(u)=u^2/2$ and $u_0(x)=\begin{cases}0 & x<0\\1 & x>0\end{cases}$. As $f\in C^2(\Re)$ is uniformly convex and $u_0\in L^\infty(\Re)$ we must have a unique entropy solution. For any $x\in\Re,t>0,z>0$ we have:$$ u(x+z,t)-u(x,t)=\begin{cases}0 & x+z<0\text{ or }x>t \\
\frac{x+z}{t} & x<0\text{ and }0<x+z<t \\
1 & x<0\text{ and }x+z>t \\
\frac{x+z}{t}-\frac{x}{t} & 0<x<x+z<t \\
1-\frac{x}{t} & 0<x<t<x+z\end{cases}\leq\begin{cases}0 \\
z/t \\
\frac{x+z}{t} \\
z/t \\
\frac{x+z}{t}-\frac{x}{t}\end{cases}\leq z/t\leq\left(1+\frac{1}{t}\right)z$$so $u(x,t)$ satisfies the condition with the bound $C=1$.