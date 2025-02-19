
# Laurent series:

A Laurent series is an infinite series of form:$$\Huge \sum_{n=-\infty}^\infty c_n(z-a)^n$$where $c_n,a\in\mathbb{C}$. The point $a$ is called the center of the Laurent series. Given a Laurent series, one can break it down into the principal part and the analytic part:$$\Huge \sum_{n=-\infty}^\infty c_n(z-a)^n=\sum_{n=-\infty}^{-1}c_n(z-a)^n+\sum_{n=0}^\infty c_n(z-a)^n$$respectively. A Laurent series converges at a point $z\in\mathbb{C}$ if and only if it's principle and analytic parts converge at $z\in\mathbb{C}$. It now makes sense to ask where a given Laurent series converges.

For $0\leq r<R\leq\infty$ and $a\in\mathbb{C}$, the set:$$\Huge A_{r,R}(a):=\{z\in\mathbb{C}:r<|z-a|<R\}$$is called the annulus with center $a$, internal radius $r$, and external radius $R$. Since $r=0$ and $R=\infty$ are allowed, one can define $B_R^*(a),\mathbb{C}^*$, and $\mathbb{C}\setminus\overline{B_r(a)}$ in terms of an annulus.

Given a Laurent series $\sum_{n=-\infty}^\infty c_n(z-a)^n$ that is not a [[Power series|power series]] ($c_n\neq0$ for some $n<0$), then either:
> The Laurent series never converges
> There exists $0\leq r<R\leq\infty$ such that the series [[Series#Convergence criteria|converges absolutely]] when $r<|z-a|<R$ and diverges when either $|z-a|<r$ or $|z-a|>R$. In this case, the annulus $A_{r,R}(a)$ is called the annulus of convergence of the Laurent series.

This is true since by definition, a Laurent series converges absolutely if and only if both:$$\Huge F_1(z)=\sum_{n=0}^\infty c_n(z-a)^n,\,\,F_2(z)=\sum_{n=-\infty}^{-1}c_n(z-a)^n$$converge absolutely. The analytic part $F_1(z)$ is a power series. If $F_1(z)$ only converges at $z=a$ then the Laurent series never converges since $F_2$ is not defined at $a$. Otherwise, let $0<R\leq\infty$ be the [[Power series#Radius of Convergence|radius of convergence]] of $F_1$. For the principle part $F_2$, we introduce $w=(z-a)^{-1}$, which makes the series:$$\Huge F_2(z)=\sum_{n=-\infty}^{-1}c_n(z-a)^n=\sum_{n=1}^\infty c_{-n}w^n=\tilde F(w)$$This is a power series in the variable $w$ with center $0$. If this only converges for $w=0$ then $F_2$ never converges. Assume $w\neq0$ and let $0<R'\leq\infty$ be the radius of convergence of this power series. Now let:$$\Huge r=\begin{cases}1/R'&0<R'<\infty\\0&R'=\infty\end{cases}$$Then the series $F_2(z)$ converges absolutely when $0<|w|<R'$ and diverges when $|w|>R'$, thus proving the proposition.

This has a corollary where a given Laurent series with annulus of convergence $A_{r,R}(a)$ will converge uniformly on any annulus $A_{\rho_1,\rho_2}(a)$ with $r<\rho_1<\rho_2<R$. In particular, the series converges [[Convergence and Power series#Local uniform convergence|locally uniformly]] on its annulus of convergence and represents a [[Complex differentiation#Holomorphicity|holomorphic]] function on $A_{r,R}(a)$. This can be proven using the tools defined above. 

## Uniqueness of Laurent series:
Let $f(z)=\sum_{n=-\infty}^\infty c_n(z-a)^n$ be a Laurent series with annulus of convergence containing $A_{r_R}(a)$ for some $a\in\mathbb{C}$ and $0\leq r<R\leq\infty$. Then the constants $c_n$ are unique and are given, for any $\rho\in(r,R)$:$$\Huge c_m=\frac{1}{2\pi i}\int_{|z-a|=\rho}\frac{f(z)}{(z-a)^{m+1}}dz$$for some $m\in\mathbb{Z}$. In particular, the Laurent series representation of $f$ in $A_{r,R}(a)$ is unique.

To prove this, observe that for $m\in\mathbb{Z}$ we have:$$\Huge\begin{align}
\int_{|z-a|=\rho}\frac{f(z)}{(z-a)^{m+1}}dz&=\int_{|z-a|=\rho}\sum_{n=-\infty}^\infty c_n(z-a)^{n-m-1}dz\\
&=\sum_{n=-\infty}^\infty c_n\int_{|z-a|=\rho}(z-a)^{n-m-1}dz
\end{align}$$where summation and integration have been interchanged as the sum converges absolutely on $|z-a|=\rho$. By the usual application of [[Cauchy's theorem]] and [[Cauchy's theorem#Cauchy's Integral Theorem|CIF]] we get:$$\Huge \int_{|z-a|=\rho}(z-a)^{n-m-1}dz=\begin{cases}2\pi i&n=m\\0&n\neq m\end{cases}$$therefore every element of the sum is zero except for the case where $n=m$:$$\Huge \int_{|z-a|=\rho}\frac{f(z)}{(z-a)^{m+1}}dz=2\pi i c_m$$this shows that the integral does not depend on $\rho$ and that coefficient are unique to the Laurent series.

## Holomorphic functions on annuli:
Let $f:A\rightarrow\mathbb{C}$ be holomorphic on some annulus $A=A_{r,R}(a)$. Then there exist unique $c_n\in\mathbb{C}$ such that:$$\Huge f(z)=\sum_{n=-\infty}^\infty c_n(z-a)^n$$for $z\in A$. The annulus of convergence of this Laurent series then contains $A$. This is called the Laurent series of $f$ on $A$.

The strategy for proof is to show that $f$ has a Laurent series on $A_{\rho_1,\rho_2}(a)$ where $r<\rho_1<\rho_2<R$. Assume that there exists another Laurent series on a larger annulus $A_{\rho_1',\rho_2'}(a)$ where $r<\rho_1'<\rho_1<\rho_2<\rho_2'<R$, then by [[Holomorphic functions#Analytic continuation|Analytic continuation]] we must have that the Laurent series are identical. Consider the contours defined by:$$\Huge\begin{align}
\gamma_1(t)&=a+\rho_1e^{-2\pi t}\\
\gamma_2(t)&=a+\rho_2e^{2\pi t}
	\end{align}$$![[annuli]]Fix some $\omega\in A_{\rho_1,\rho_2}(a)$. We will then show that $f$ has Laurent series at $\omega$. By the general CIF theorem, we have:$$\Huge 2\pi iI(\Gamma;\omega)f(\omega)=\int_\Gamma\frac{f(z)}{z-\omega}dz$$For such $\omega$, the winding number is $1$ for the larger contour and $0$ for the smaller contour, so $I(\Gamma;\omega)=1$. That is to say:$$\Huge f(\omega)=\frac{1}{2\pi i}\int_\Gamma\frac{f(z)}{z-\omega}dz=\frac{1}{2\pi i}\int_{\gamma_1}\frac{f(z)}{z-\omega}+\frac{1}{2\pi i}\int_{\gamma_2}\frac{f(z)}{z-\omega}dz$$One can show that:$$\Huge \frac{1}{z-\omega}=\frac{1}{z-a}\sum_{n=0}^\infty\left(\frac{\omega-a}{z-a}\right)^n$$which is valid since $\left|\frac{\omega-a}{z-a}\right|=\frac{|\omega-a|}{\rho_2}<1$. Then following the proof of the [[Cauchy's theorem#Cauchy's Integral Theorem|C-T]] theorem we can show that:$$\Huge f_2(z)=\sum_{n=0}^\infty c_n(z-a)^n$$The problem then arises from the fact that on $\gamma_1$ we have $\left|\frac{\omega-a}{z-a}\right|=\frac{|\omega-a|}{\rho_1}>1$. Note that:$$\Huge \frac{1}{z-\omega}=-\frac{1}{\omega-z}=-\frac{1}{\omega-a+a-z}=-\frac{1}{\omega-a}\frac{1}{1-\frac{z-a}{\omega-a}}$$therefore:$$\Huge\begin{align} 
f_1(\omega)&=\frac{1}{2\pi i}\int_{\gamma_1}\frac{f(z)}{z-\omega}dz\\
&=\frac{1}{2\pi i}\int_{\gamma_1}f(z)\left(-\frac{1}{\omega-a}\right)\sum_{m=0}^\infty\left(\frac{z-a}{\omega-a}\right)^ndz\\
&=\sum_{m=0}^\infty\left(-\frac{1}{2\pi i}\int_{\gamma_1}f(z)(z-a)^mdz\right)(\omega-a)^{-(m+1)}\\
&=\sum_{n=-\infty}^{-1}\left(-\frac{1}{2\pi i}\int_{\gamma_1}\frac{f(z)}{(z-a)^{n+1}}dz\right)(\omega-a)^n\\
&=\sum_{n=-\infty}^{-1}c_n(\omega-a)^n
\end{align}$$This shows that the function can be written as a Laurent series.

# Classification of Isolated singularities:

We say that a holomorphic function $f:B_R^*(a)\rightarrow\mathbb{C}$ has an isolated singularity at $z=a$. Given such a function, exactly one of the following is true:
> $f$ has a removable singularity at $z=a$ if the principal part is empty, that is $c_n=0$ for $n<0$.