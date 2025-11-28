
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
\end{align*}$$Now using the fact that $\Re\times(0,\infty)$ is open and that $u_t+f(u)$ is continuous, we have that the above holds for any $\varphi\in C_c^\infty(\Re\times(0,\infty))$. We can therefore use the fundamental lemma of calculus of variations that:$$\Huge\partial_tu(x,t)+\partial_x f(u(x,t))=0,\,\,\forall(x,t)\in\Re\times(0,\infty)$$One can also recover boundary conditions by using the same argument for the case where $\varphi\in C_c^1(\Re\times[0,\infty))$.