
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
Let $(f_n)_{n\in\mathbb{N}}$ be a sequence of continuous functions which converge locally uniformly on $X$ to a limit function $f$. Then $f$ is continuous on $X$. To prove this, let $x_0\in X$. By assumption there exists $U_{x_0}$ open with $x_0\in U_{x_0}$ such that $(f_n)_{n\in\mathbb{N}}$ converges uniformly to $f$ on $U_{x_0}$. Since each $f_n$ are continuous and convergence is uniform on $U_{x_0}$, $f$ must be continuous on $U_{x_0}$. Consequently, $f$ is uniform continuous at $x_0$. Since $x_0$ was arbitrary, $f$ must be continuous on $X$.

## Local $M$-test:
Let $X$ be a metric space and let $f_n:X\mapsto\mathbb{C}$ be a sequence of continuous functions such that for any $x_0\in X$, there is an open $U_{x_0}\subset X$ containing $x_0$ and constant $M_n(U_{x_0})>0$ such that $|f_n(x)|\leq M_n(U_{x_0})$ for all $x\in U_{x_0}$, and $\sum_{n=1}^\infty M_n(U_{x_0})<\infty$. Then $\sum_{n=1}^\infty f_n$ converges locally uniformly to a continuous function on $X$. 

To prove this, consider $x_0\in X$. Then there exists an open set $U_{x_0}\subset X$ and a sequence $(M_n(U_{x_0}))_{n\in\mathbb{N}}$ such that $M_n(U_{x_0})>0$ and $\sum_{n=1}^\infty M_n(U_{x_0})<\infty$. Then there exists for all $x\in U_{x_0}$ such that $|f_n(x)|\leq M_n(U_{x_0})$. This implies that by the Weierstrass $M$-test $\sum_{n=1}^\infty f_n(x)$ converges uniformly on $U_{x_0}$. Moreover as $f_n(x)$ are each continuous, so the sum must also be continuous on $U_{x_0}$. By definition $\sum_{n=1}^\infty f_n(x)$ converges locally uniformly on $X$. Also since $\sum_{n=1}^\infty f_n(x)$ is continuous at every $x_0$, it is continuous. Example:![[local M test]]
# Power series:

A complex [[Power series|power series]] is an expression of the form:$$\Huge \sum_{n=0}^\infty a_n(z-c)^n$$Where $(a_n)_{n\in\mathbb{N}}$ is a sequence of complex numbers and $c\in\mathbb{C}$.

For any sequence of complex numbers $(a_n)_{n\in\mathbb{C}}$ we can define $S(z)$ as the above sum. Then there exists $R\in\Re_{\geq0}\cup\{\infty\}$ such that:
>$S(z)$ converges only for $z=c$ when $R=0$. In such case $S(c)=a_0$
>$S(z)$ converges absolutely for all $|z-c|<R$ when $R>0$. If $R=+\infty$ this condition holds for any $z$.
>$S(z)$ diverges for $|z-c|>R$ when $R>0$. If $R=\pm\infty$ this condition never holds.

$R$ is called the radius of convergence of a power series and $B_R(c)$ is called the disc of convergence. This can be found by:$$\Huge R=\frac{1}{\limsup_{n\to\infty}\sqrt[n]{|a_n|}}$$When the limit exists, $\sup$ is not needed. When the following limit exists, we have the formula:$$\Huge R=\lim_{n\to\infty}\frac{|a_n|}{|a_{n+1}|}$$ A power series $\sum_{n=0}^\infty a_n(x-c)^n$ with radius of convergence $0<R\leq\infty$ converges uniformly on any ball $B_r(c)$ with $0<r<R$, implying that the power series is locally uniformly convergent on its disc of convergence. To prove this, let $z\in B_r(c)$. Then $|a_n(z-c)^n|=|a_n||z-c|^n\leq|a_n|r^n=M_n(r)$. Then the sum $\sum_{n=0}^\infty |a_n|r^n<\infty$ converges if and only if the original sum converges uniformly on $B_r(c)$. We know that the original sum converges absolutely for any $z\in B_R(c)$. By choosing $z=c+r\in B_R(c)$ we get that the sum $\sum_{n=0}^\infty|a_n||z-c|^n=\sum_{n=0}^\infty|a_n||c+r-c|^n=\sum_{n=0}^\infty|a_n|r^n<\infty$ converges. Therefore we have that the power series is locally uniformly convergent on its disc of convergence.

Take for example the power series $\sum_{n=0}^\infty\frac{z^n}{n!}$. We ask if this converges locally uniformly on $\mathbb{C}$. This result will follow if we show that the radius of convergence for the sum is $R=\infty$. We therefore must compute the radius of convergence:$$\Huge R=\lim_{n\to\infty}\frac{\frac{1}{n!}}{\frac{1}{(n+1)!}}=\lim_{n\to\infty}n+1=\infty$$Therefore the power series converges on $\mathbb{C}$. 

# Differentiation and Integration of Power series:

Let $\sum_{n=0}^\infty a_n(z-c)^n$ be a power series with radius of convergence $0<R\leq\infty$. Then the format derivatives and anti-derivatives of the power series are:$$\Huge \sum_{n=1}^\infty na_n(z-c)^{n-1}\,\,\text{and}\,\,\sum_{n=0}^\infty\frac{a_n}{n+1}(z-c)^{n+1}$$Which both have the same power series as the original. Letting $f:B_R(c)\mapsto\mathbb{C}$ be the resulting limiting function, then $f$ is holomorphic on $B_R(c)$ with:$$\Huge f'(z)=\sum_{n=1}^\infty na_n(z-c)^{n-1}$$This has a corollary where a power series of this form can be differentiated infinitely many times in $B_R(c)$:$$\large f^{(k)}(z)=\sum_{n=k}^\infty n(n-1)\dots(n-k+1)a_n(z-c)^{n-k}=\sum_{n=k}^\infty k!{n\choose k}(z-c)^{n-k}$$For $z\in B_R(c)$, which implies $f^{(k)}(c)=k!a_k$ and:$$\Huge a_n=\frac{f^{(n)}(a)}{n!}$$
We also get that the power series has a holomorphic antiderivative $F:B_R(c)\mapsto\mathbb{C}$ that is a holomorphic function $F$ on $B_R(c)$ such that $F'(z)=f(z)$. $F$ is then given as above.

Note that if a power series converges uniformly on $B_r(a)$ then:$$\Huge \int_{\gamma}\sum_{n=0}^\infty c_n(z-a)^ndz=\sum_{n=0}^\infty\int_\gamma c_n(z-a)^ndz$$For any [[Complex integration#Contour integrals|contour]] $\gamma\in B_R(a)$.