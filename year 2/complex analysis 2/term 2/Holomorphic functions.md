
# Cauchy-Taylor theorem:

Let $f:U\rightarrow\mathbb{C}$ be [[Complex differentiation#Holomorphicity|holomorphic]] on some open set $U$ and let $B_r(a)$ be some open ball in $U$. Then $f$ can be represented by a [[Power series|power series]] on $B_r(a)$ given by:$$\Huge f(z)=\sum_{n=0}^\infty c_n(z-a)^n,\,\,c_n=\frac{1}{2\pi i}\int_{|z-a|=\rho}\frac{f(z)}{(z-a)^{n+1}}dz$$for any $0<\rho<r$. This is known as the Taylor series of $f$. To prove this, fix some $0<\rho<r$, then for any $|\omega-a|<\rho$ we have by [[Cauchy's theorem#Cauchy's Integral Theorem|CIF]] that:$$\Huge f(\omega)=\frac{1}{2\pi i}\int_{|z-a|=\rho}\frac{f(z)}{z-\omega}dz$$Then by uniform convergence we have:$$\Huge\begin{align}
f(\omega)&=\frac{1}{2\pi i}\int_{|z-a|=\rho}f(z)\sum_{n=0}^\infty\frac{(\omega-a)^n}{(z-a)^{n+1}}dz\\
&=\sum_{n=0}^\infty\frac{1}{2\pi i}\int_{|z-a|=\rho}\frac{f(z)}{(z-a)^{n+1}}dz\,(\omega-a)^n\\
&=\sum_{n=0}^\infty c_n(\omega-a)^n
\end{align}$$So we get the power series in $\omega$, proving the result as required. One can show that $c_n$ is indeed well defined. Using the result for the [[Convergence and Power series#Differentiation and Integration of Power series|derivative of a power series]]:$$\Huge c_n=\frac{f^{(n)}(a)}{n!}$$We see that $c_n$ is indeed well defined.

# CIF for derivatives:

Let $f:U\rightarrow\mathbb{C}$ be holomorphic on an open set $U$ and $B_r(a)\subset U$. Then for any $0<\rho<r$ we have:$$\Huge \int_{|z-a|=\rho}\frac{f(z)}{(z-a)^{n+1}}dz=\frac{2\pi i}{n!}f^{(n)}(a)$$This comes immediately from comparing the formulae for $c_n$. Note that if $f$ is holomorphic on $B_r(a)$ we can write for all $z$:$$\Huge f(z)=\sum_{n=0}^\infty\frac{f^{(n)}(a)}{n!}(z-a)^n$$
Also there exist real functions that cannot be represented by a power series, for example:$$\Huge f(x)=\begin{cases}e^{-1/x}&x>0\\0&x\leq0\end{cases}$$The derivative of this at $0$ for all $n$ is $0$, so we get that $f(x)=0$ but this is not true for $x>0$.

When using CIF for derivatives, one may need to use partial fraction decomposition to find a suitable form:![[CIF deriv example]]
## Holomorphic power series
If $f:U\rightarrow\mathbb{C}$ is holomorphic on an open set $U$, then $f$ has derivatives of all orders and each derivative is itself holomorphic. To prove this, choose some $a\in U$ and some $r>0$ such that $B_r(a)\subset U$. Then by Cauchy-Taylor theorem we have that $f(z)$ can be represented by a power series for all $z\in B_r(a)$. Then by the [[Convergence and Power series#Differentiation and Integration of Power series|differentiation of power series]] we can differentiate the power series on $B_r(a)$:$$\Huge f'(z)=\sum_{n=1}^\infty nc_n(z-a)^{n-1}$$This is itself a power series, so can be further differentiated infinitely. This shows that each derivative of $f$ exists and is holomorphic.

# Morera's theorem:

Let $f:D\rightarrow\mathbb{C}$ be continuous on a domain $D$. If $\int_\gamma f(z)dz=0$ for all closed [[Complex integration#Contours|contours]] $\gamma$ then $f$ is holomorphic on $D$. To prove this, let $f$ be continuous on $D$ and assume that $\int_\gamma f(z)dz=0\forall\gamma\subset D$ such that $\gamma$ is closed. Then the [[Complex integration#Complex Fundamental Theorem of Calculus|converse FTC]] states that there exists a holomorphic $F:D\rightarrow\mathbb{C}$ such that $F'(z)=f(z)$. By the [[Holomorphic functions#Holomorphic power series|above]] corollary, $F'=f$  must be holomorphic, proving the statement as required.

# Liouville's theorem:

Every bounded entire function is constant. To prove this, assume $f$ is entire and there exists some $M$ with $|f(z)|\leq M$ for all $z\in\mathbb{C}$. Now fix some $\omega\in\mathbb{C}$, to prove the theorem we will show that $f(\omega)=f(0)$. Choose some $\rho$ such that $0<|\omega|<\rho$, then by [[Cauchy's theorem#Cauchy's Integral Theorem|CIF]]:$$\Huge
\begin{align}
|f(\omega)-f(0)|&=\left|\frac{1}{2\pi i}\int_{|z|=\rho}\frac{f(z)}{z-\omega}dz-\frac{1}{2\pi i}\int_{|z|=\rho}\frac{f(z)}{z}dz\right|\\
&=\frac{1}{2\pi}\left|\int_{|z|=\rho}f(z)\left(\frac{1}{z-\omega}-\frac{1}{z}\right)dz\right|\\
&=\frac{1}{2\pi}\left|\int_{|z|=\rho}f(z)\frac{\omega}{(z-\omega)z}dz\right|\\
&=\frac{|\omega|}{2\pi}\left|\int_{|z|=\rho}f(z)\frac{1}{(z-\omega)z}dz\right|\\
&\leq\frac{|\omega|}{2\pi}\cdot2\pi\rho\cdot\sup_{|z|=\rho}\frac{|f(z)|}{|z(z-\omega)|}
\end{align}$$By the estimation lemma. We then have:$$\Huge\begin{align}
|f(\omega)-f(0)|&\leq|\omega|\rho\sup_{|z|=\rho}\frac{|f(z)|}{|z(z-\omega)|}\\
&\leq M|\omega|\rho\sup_{|z|=\rho}\frac{1}{|z(z-\omega)|}\\
&\leq M|\omega|\sup_{|z|=\rho}\frac{1}{\rho-|\omega|}=\frac{M|\omega|}{\rho-|\omega|}\to0 
\end{align}$$Where we notice that $|z|=\rho$ along the contour and use the reverse triangle inequality on the denominator. As $\rho\to\infty$ we see that this tends to $0$, we can do this as the contour and $\omega$ were arbitrary. This leaves us with:$$\Huge |f(\omega)-f(0)|=0\implies f(\omega)=f(0)$$Since $\omega$ was arbitrary we have that this function is constant, and since the function was arbitrary we have proven the theorem as required.

# Fundamental theorem of algebra:

Every non-constant polynomial with complex coefficients has a root in $\mathbb{C}$. This is proven by contradiction, so assume that a polynomial $P$ has no roots in $\mathbb{C}$ so $|P(z)|\neq0\forall z\in\mathbb{C}$. Then we set $f(z)=1/P(z)$ which will be holomorphic on $\mathbb{C}$. Note that $|P(z)|\to\infty$ as $|z|\to\infty$. Therefore there must exist some $R>0$ such that when $|z|>R$ we have $|P(z)|>1$. Then on this region $|f(z)|<1$, that is $f$ is bounded. Now by the [[Metric spaces#Extreme Value Theorem|EVT]] we have that $f$ must be bounded on the compact set $\overline B_R(0)$, which is the complement of the set where we have also shown that $f$ is bounded. Therefore we can conclude that $f(z)=1/P(z)$ is bounded on the whole plane, making $P(z)$ bounded on the whole plane. Now by Liouville's theorem we have that $P(z)$ must be a constant polynomial, a contradiction. Therefore the assumption that $P(z)$ has no roots in $\mathbb{C}$ is false, proving the theorem as required.

# The Maximum Modulus principle (MMT):
## Local version:
Let $B=B_r(a)$ and $f:B\rightarrow\mathbb{C}$ be holomorphic. If for every $z\in B$ we have $|f(z)|\leq|f(a)|$ then $f$ is constant on $B$.

We first show that $|f(z)|$ must be constant. To do this, fix any $\omega\in B_r(a)$ and let $\rho=|\omega-a|<r$. We parametrise the curve $|z-a|=\rho$ through $\omega$ by $\gamma(t)=a+\rho e^{2\pi it}$ for $t\in[0,1]$. Applying CIF and the [[Complex integration#Estimation lemma and contour length|estimation lemma]]:$$\Huge\begin{align}
|f(a)|&=\frac{1}{2\pi}\left|\int_\gamma\frac{f(z)}{z-a}dz\right|\\
&=\frac{1}{2\pi}\left|\int_0^1\frac{f(\gamma(t))}{\gamma(t)-a}\gamma'(t)dt\right|\\
&=\frac{1}{2\pi}\left|\int_0^1\frac{f(\gamma(t))}{\rho e^{2\pi it}}2\pi i\rho e^{2\pi it}dt\right|\\
&=\left|\int_0^1f(\gamma(t))dt\right|\\
&\leq\int_0^1|f(\gamma(t))|dt\leq\int_0^1|f(a)|dt=|f(a)|
	\end{align}$$So we have $|f(a)|\leq\int_0^1f(\gamma(t))=|f(z)|\leq|f(a)|$, that is $|f(z)|=|f(a)|$ for all $z$ with $|z-a|=\rho$, in particular $|f(\omega)|=|f(a)|$. This proves that the modulus is constant.

We now use this to prove the theorem. Since $|f(z)|=c$ for some $c\in\mathbb{C}$ and all $z\in B$, take $c=0$ to show that $|f(z)|=0\implies f(z)=0=\text{constant}$. So assume $c\neq0$, allowing us to write $f(z)\overline{f(z)}=c^2$ and so $\overline{f(z)}=\frac{c^2}{\overline{f(z)}}$. This means that both $f$ and $\bar f$ are holomorphic. Applying the [[Complex differentiation#Cauchy-Riemann equations|C-R equations]] shows that $u_x=v_x=0\implies f'(z)=u_x+iv_x=0$, which implies that $f$ is constant, completing the proof.

## General version:
We can now extend this theorem to any domain. Let $D$ be a domain and $f:D\rightarrow\mathbb{C}$ holomorphic. If there exists some $a\in D$ such that $|f(z)|\leq|f(a)|$ for all $z\in D$, then $f$ is constant. Let $U_1$ be the set of points on $D$ where $f(z)=f(a)$, then $U_1\neq\emptyset$. Given $z\in U_1$, there must exists a disc $B_r(z)\in D$ since $D$ is an open set. Choose some $\omega\in B_r(z)$, then since $|f(\omega)|\leq|f(a)|=|f(z)|$ and $z$ is the center of $B_r(z)$ we can apply the local version of the Maximum Modulus Principle. This states that $f$ is constant on $B_r(z)$, implying that $|f(\omega)|=|f(z)|$ and so $B_r(z)\subset U_1$. This makes $U_1$ open. Now let $U_2=D\setminus U_1$ and write $U_2=f^{-1}(\mathbb{C}\setminus\{f(a)\})$, which must be open since $f$ is holomorphic and $\mathbb{C}\setminus\{f(a)\}$ is open. Since $D$ is a domain, it is path connected, which means that $U_2$ must be empty. This means that $U_1=D$, so we have $f(z)=f(a)$ for all $z\in D$, proving the theorem.

For example take $f(z)=z^2+2z-3$. We ask if it attains its maximal value on $\overline{B_1(0)}$ and if so, what value does it take?![[MMT example]]
# Analytic continuation:

Given a holomorphic function $f:B_r(a)\rightarrow\mathbb{C}$ we ask when can we find a holomorphic function $g$ on some domain $D$ with $B_r(a)\subset D$ such that $f(z)=g(z)$ for $z\in B_r(a)$. Assume $\exists z_0\in B_r(a):f(z_0)\neq0$ and suppose that $f(a)=0$. By Cauchy-Taylor we have:$$\Huge f(z)=\sum_{n=0}^\infty c_n(z-a)^n\text{ on }B_r(a)$$Let $m=\min\{n\geq0:c_n\neq0\}$, then:$$\Huge f(z)=(z-a)^m\sum_{n=m}^\infty c_n(z-a)^{n-m}=(z-a)^m\sum_{k=0}^\infty c_{m+k}(z-a)^k$$By the ratio test, the sum converges when:$$\Huge\lim_{k\to\infty}\left|\frac{c_{m+k+1}(z-a)^{k+1}}{c_{m+k}(z-a)^k}\right|<1$$Which is the same limit as:$$\Huge\lim_{n\to\infty}\left|\frac{c_{n+1}}{c_n}\right||z-a|<1$$
## Order of a zero:
This motivates the definition of the order of a zero. We say that $f:B_r(a)\rightarrow\mathbb{C}$ has a zero at $z=a$ if $f(a)=0$. For $m>0$ we say that this is a zero of order $m$ if there exist a holomorphic function $h:B_r(a)\rightarrow\mathbb{C}$ such that $f(z)$ can be written in the form:$$\Huge f(z)=(z-a)^mh(z)$$ Also $h(a)\neq0$.

One can show that $f$ has a zero of order $m$ at $z=a$ if and only if:$$\Huge f(a)=f'(a)=f''(a)=\dots=f^{(m-1)}(a)=0$$But $f^{(m)}(a)\neq0$.

Take for example $f(z)=(e^z-1)z$. Then $f'(z)=e^z-1+e^zz=ze^z+e^z-1$ and $f''(z)=ze^z+2e^z$. $f$ has zeroes at $z=0$ and $z=2\pi ni$. $f'(0)=0$ and $f''(0)=z$ so we have that the order of $z=0$ is $2$. Alternatively we can replace $e^z$ with its power series to get $f(z)=z\sum_{n=1}^\infty\frac{z^n}{n!}=\sum_{n=1}^\infty\frac{z^{n+1}}{n!}=z^2\sum_{k=0}^\infty\frac{z^k}{(k+1)!}$ so by our above definition the zero $z=0$ has order $2$.

## Principle of isolated zeros (PIZ):
Let $f:B_r(a)\rightarrow\mathbb{C}$ be holomorphic and not identically zero. If $f(a)=0$ then there exists $0<\rho\leq r$ such that:$$\Huge f(z)\neq0\,\forall z\in B_\rho(a)\setminus\{a\}$$That is, there exists a small neighbourhood that is not zero around a given zero.

To prove this, assume $f(a)=0$. Then there exists $k>0$ and a holomorphic $h:B_r(a)\rightarrow\mathbb{C}$ such that $\forall z\in B_r(a)$ we have that $f(z)=(z-a)^kh(z)$ and $h(a)\neq0$. By continuity, we can find some $0<\rho\leq r$ such that $h(z)\neq0$ for all $z\in B_\rho(a)$. Note that $(z-a)^k\neq0$ on $B_\rho(a)\setminus\{a\}$. Therefore $f(z)$, which is the product of these terms, must not be zero on $B_\rho(a)\setminus\{a\}$.

## Uniqueness of Analytic Continuation:
Let $D',D$ be two domains such that $D'\subset D$. Then suppose that $f:D'\rightarrow\mathbb{C}$ is holomorphic. Then there exists at most one $g:D\rightarrow\mathbb{C}$ such that $g$ is holomorphic that satisfies:$$\Huge f(z)=g(z)\,\forall z\in D'$$We call such $g$ the analytic continuation of $f$ from $D'$ to $D$. For example, the function $g(z)=\frac{1}{1-z}$ is the analytic continuation of $\sum_{n=0}^\infty z^n$ from $B_1(0)$ to $\mathbb{C}\setminus\{1\}$.

This has a corollary where for two holomorphic functions $f,g$ on a domain $D$, if we have $f(z)=g(z)$ for all $z\in B_r(a)$ we then have $f(z)=g(z)$ for all $z\in D$.

To prove the uniqueness of analytic continuation, assume $g_1,g_2$ are both analytic continuations of the same function. Let $h(z)=g_1(z)-g_2(z)$. We then define the sets:$$\Huge\begin{align}
D_0&=\{\omega\in D:\exists r>0:h(z)=0\forall z\in B_r(\omega)\}\\
D_1&=\{\omega\in D:h^{(n)}(\omega)\neq0\text{ for some }n\geq0\}
\end{align}$$The proof involves showing that $D_0$ is open and nonempty, $D_1$ is open, then that $D=D_0\cup D_1$ is a disjoint union.

## Isolated points and Identity theorem:
Given a set $S\subset\mathbb{C}$ we say that a point $\omega\in S$ is:
> An isolated point of $S$ if there exists $\epsilon>0$ such that $B_\epsilon(\omega)\cap S=\{\omega\}$
> A non-isolated point of $S$ if for every $\epsilon>0$ there exists $z\neq\omega\in S$ such that $B_\epsilon(\omega)\cap S$ contains $z$

Let $f,g:D\rightarrow\mathbb{C}$ be holomorphic on a domain $D$. If $\exists\omega\in D$ such that $\omega$ is a non-isolated point of $S=\{z\in D:f(z)=g(z)\}$ then $f(z)=g(z)$ on $D$.

For example let $f:\mathbb{C}\rightarrow\mathbb{C}$ be holomorphic and assume $f\left(\frac{1}{n}\right)=\sin\left(\frac{1}{n}\right)$ for all $n\geq1$. We aim to identify the function $f$. Since $f$ was assumed to be continuous, and by the sequential definition of continuity we can write:$$\Huge f(0)=f\left(\lim_{n\to\infty}\frac{1}{n}\right)=\lim_{n\to\infty}f\left(\frac{1}{n}\right)=\lim_{n\to\infty}\sin\left(\frac{1}{n}\right)=\sin(0)=0$$Then $S=\{z\in\mathbb{C}:f(z)=\sin z\}\subset\{0\}\cup\{\frac{1}{n}:n\geq1\}$ and the point $z=0$ is a non-isolated point of $S$. Therefore $f(z)=\sin(z)$ on $\mathbb{C}$.

We now prove the identity theorem. Let $\omega\in D$ be the non-isolated point in $S=\{z\in D:f(z)=g(z)\}$. Let $h(z)=f(z)-g(z)$ so that $h$ is holomorphic on $D$ and $h(\omega)=0$. By the principle of isolated zeros, there exists a ball $B_\rho(\omega)$ such that $h\neq0$ on $B_\rho(\omega)\setminus\{\omega\}$. Since $\omega$ is a non-isolated point, there must exist some $z\in B_\rho(\omega)$ such that $z\in S$, a contradiction. Therefore $h(z)=0$ for all $z\in D$, proving the theorem as required.

# Harmonic functions:

A real valued function $u:D\rightarrow\Re$ on some domain $D$ is called harmonic if $u(x,y)$ has continuous second order partial derivatives that satisfy:$$\Huge u_{xx}+u_{yy}=0$$for all $\underline x\in D$. This is known as Laplace's equation.

Let $f:D\rightarrow\mathbb{C}$ be holomorphic on a domain $D$. Then writing $f=u+iv$ we have:$$\Huge u_{xx}+u_{yy}=0,\,\,v_{xx}+v_{yy}=0$$That is, the real and imaginary parts of $f$ are harmonic. We have seen that all holomorphic functions have partial derivatives of all orders and each are continuous. Since these are continuous, we have $f_{xy}=f_{yx}$. Using the [[Complex differentiation#Cauchy-Riemann equations|Cauchy-Riemann equations]] we can obtain:$$\Huge\begin{align}
u_{xx}=v_{yx}&,\,\,u_{yy}=-v_{xy}=-(v_{yx})=-u_{xx}\\
v_{yy}=-u_{xy}&,\,\,v_{xx}=-u_{yx}=-(u_{xy})=-v_{yy}
\end{align}$$So we see that the real and imaginary parts of $f$ are each harmonic, making the function $f$ harmonic.

## Harmonic conjugates:
Let $u:D\rightarrow\Re$ be harmonic on a starlike domain $D$. Then there exists harmonic $v:D\rightarrow\Re$ such that $f=u+iv$ is holomorphic on $D$. Such function $v$ is called the harmonic conjugate of $u$, which is unique up to a real constant. To prove this, we need the following proposition:

Let $f:D\rightarrow\mathbb{C}$ be holomorphic on a starlike domain $D$. Then $f$ has a holomorphic anti-derivative on $D$. The proof is by [[Cauchy's theorem]], which states $\int_\gamma fdz=0$ for all closed $\gamma\subset D$. By the converse FTOC, there exists a holomorphic antiderivative as required.

To prove the existence of the harmonic conjugate, consider the function:$$\Huge g(z)=A(x,y)+iB(x,y)$$with $A=u_x,B=-u_y$. Assuming $u$ is harmonic, we now verify the C-R equations for $g$: $$\Huge\begin{align}
A_x&=u_{xx}=-u_{yy}=B_y\\
A_y&=u_{xy}=-(-u_{yx})=-B_x
\end{align}$$therefore $g$ is holomorphic. By the above proposition, $g$ has a holomorphic antiderivative $F:D\rightarrow\mathbb{C}$ such that $F'(z)=g(z)$ for all $z\in D$. Let $F=A+iB$, then $F'=A_x-iA_y=g$. This is only true when $A_x=u_x$ and $A_y=u_y$, which implies $A=u+c$ for some real $c$. Now let $f=u+iB=(A-C)+iB=F-c$, so we have the proof as required. One can also show that such $f$ is unique.

## The Dirichlet problem:
Let $D$ be a domain in $\mathbb{C}$. Let $g:\partial D\rightarrow\Re$ be continuous. The Dirichlet problem aims to find a continuous function $\mu:\bar D\rightarrow\Re$ such that $\mu$ is harmonic on $D$ and matches $g$ on $\partial D$.