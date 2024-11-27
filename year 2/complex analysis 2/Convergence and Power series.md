
We aim to show that [[Complex differentiation#Holomorphicity|holomorphic]] functions in a domain $D$ are analytic (i.e. have a [[Power series|power series]] expansion). In order to do this, we need to redefine the notion of convergence for sequences and series of functions.

# Pointwise convergence:

Let $(X,d_X),(Y,d_Y)$ be two [[Metric spaces|metric spaces]]. A sequence of functions $(f_n)_{n\in \mathbb{N}}:X\mapsto Y$ converges pointwise on $X$ to $f$ if for every $x\in X$ the limit function:$$\Huge f(x)=\lim_{n\to\infty}f_n(x)$$Exists in $Y$. That is to say for any $x\in X$ and any $\epsilon>0$ there exists $N(\epsilon,x)\in\mathbb{N}$ such that if $n>N(\epsilon,x)$ we have that $d_Y(f_n(x),f(x))<\epsilon$. Note that $N(\epsilon,x)$ depends on $\epsilon$ and $x\in X$ in general.

Take for example $f_n:\mathbb{C}\mapsto\mathbb{C}$ defined by $f_n(z)=z^n$. Then:$$\Huge \lim_{n\to\infty}f_n(z)=\begin{cases}0&|z|<1\\1&z=1\\\text{no limit}&|z|=1,z\neq1\\\text{unbounded, no limit in }\mathbb{C}&|z|>1\\\end{cases}$$Note that $f_n(z)$ is continuous on $\mathbb{C}$, however the limit is not as there is a jump discontinuity at $1$. So we make the remark that pointwise convergence does not necessarily preserve continuity.

# Uniform convergence:

We say that a sequence of functions $(f_n)_{n\in\mathbb{N}}:X\mapsto Y$ converges uniformly on $X$ to the limit function $f$ if we have:$$\Huge \sup_{x\in X}d_Y(f_n(x),f(x))\to_{n\to \infty}0$$That is to say for any $\epsilon>0$ there exists $N(\epsilon)\in\mathbb{N}$ such that if $n>N(\epsilon)$:$$\Huge d(f_n(x),f(x))<\epsilon\,\,\forall x\in X$$Note that $N$ depends only on $\epsilon$, not $x$. Therefore we can say that uniform convergence implies pointwise convergence.

Let $(X,d_X),(Y,d_Y)$ be two metric spaces and $(f_n)_{n\in\mathbb{N}}:X\mapsto Y$ be a sequence of functions that converges uniformly on $X$ to $f$. The proof of which is analogous to [[Convergence and Power series|the proof]] with the Euclidean metric space.

## Test for convergence:
Let $f_n:X\mapsto\mathbb{C}$ be a sequence of functions converging pointwise to a limit function $f$:
> If $|f_n(x)-f(x)|\leq s_n$ for every $x\in X$, where $(s_n)_{n\in\mathbb{N}}$ is some sequence in $\Re_{\geq0}$ with $\lim_{n\to\infty}s_n=0$, then $f_n$ converges uniformly on $X$ to $f$.
> If there exists a sequence $x_n\in X$ such that $|f_n(x_n)-f(x_n)|\geq c$ for some positive constant $c$, then $f_n$ does not converge uniformly on $X$ to $f$.

To prove the first statement, observe $|f_n(x)-f(x)|\leq s_n$ for all $x$ we have:$$\Huge\begin{align}
0\leq\sup_{x\in X}|f_n(x)-f(x)|&\leq s_n\\
\lim_{n\to\infty}0\leq\lim_{n\to\infty}\sup_{x\in X}|f_n(x)-f(x)|&\leq\lim_{n\to\infty}s_n\\
0\leq\lim_{n\to\infty}\sup_{x\in X}|f_n(x)-f(x)|&\leq0
\end{align}$$So we have uniform convergence to $f$ on $X$ by definition. To prove the second statement, notice:$$\Huge \sup_{x\in X}|f_n(x)-f(x)|\geq|f_n(x_n)-f(x_n)|\geq c>0$$Which implies that $\sup_{x\in X}|f_n(x)-f(x)|\not{\to_{n\to\infty}}0$, meaning that the convergence cannot be uniform.

# Weierstrass M-test:

Let $f_n:X\mapsto\mathbb{C}$ be a sequence of functions such that $|f_n(x)|\leq M_n$ for all $x\in X$ and some sequence of non-negative numbers $(M_n)_{n\in\mathbb{N}}$ such that:$$\huge \sum_{n=1}^\infty M_n<\infty$$Then $S_N(x)=\sum_{n=1}^Nf_n(x)$ converges uniformly on $X$ to some limit function $S:X\mapsto\mathbb{C}$ denoted by:$$\Huge S(x)=\sum_{n=1}^\infty f_n(x)$$In particular, if all the original $f_n$ were continuous, then $S(x)$ is continuous. The proof for this is analogous to the [[Convergence and Power series#Weierstrass M-test|real proof]]. The continuity of $S(x)$ follows from the fact that the sum of any number of continuous functions is function and that the convergence to $S(x)$ is uniform.

# Integrations:

Assume a sequence of functions $f_n:[a,b]\mapsto\Re$ converge uniformly on an interval $[a,b]$ to some function $f$ and that each $f_n$ are continuous. Then for any $c\in[a,b]$ we have:$$\Huge \lim_{n\to\infty}\int_a^cf_n(x)dx=\int_a^cf(x)dx$$In particular if $\sum_{n=1}^\infty f_n(x)$ converges uniformly on an interval $[a,b]$ and if $f_n$ are continuous for all $n\in\mathbb{N}$ then for any value $c\in[a,b]$:$$\Huge \int_a^c\left(\sum_{n=1}^\infty f_n(x)\right)dx=\sum_{n=1}^\infty\int_c^af_n(x)dx$$
# Local uniform convergence:

Let $(f_n)_{n\in\mathbb{N}}$ be sequence of functions defined on a metric space $X$. We say that $f_n$ converges locally uniformly on $X$ to the limit function $f$ if for every $x\in X$ there exists an open set $U_x\subset X$ containing $x$ on which $(f_n)_{n\in \mathbb{N}}$ converges uniformly to $f$. This is the notion of uniform convergence for open sets since it allows to avoid the boundary. Take $f_n(z)=z^n$ for example:![[local uniform example]]
Let $(f_n)_{n\in\mathbb{N}}$ be a sequence of continuous functions which converge locally uniformly on $X$ to a limit function $f$. Then $f$ is continuous on $X$. To prove this, let $x_0\in X$. By assumption there exists $U_{x_0}$ open with $x_0\in U_{x_0}$ such that $(f_n)_{n\in\mathbb{N}}$ converges uniformly to $f$ on $U_{x_0}$. Since each $f_n$ are continuous and convergence is uniform on $U_{x_0}$, $f$ must be continuous on $U_{x_0}$.