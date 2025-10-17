
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
> $f$ has a pole of order $k>0$ if $c_{-k}\neq0$ and $c_n=0$ for all $n<-k$, so $f(z)=\sum_{n=-k}^\infty c_n(z-a)^n$ there are finitely many non-zero terms in the principal part.
> $f$ has an essential singularity at $z=a$ if $c_{-n}\neq0$ for infinitely many $n>0$. That is, the principal part contains infinitely many non-zero terms.

Take for example $f(z)=\frac{1}{z^2}+2+z$. This clearly has a pole of order $2$ at $z=0$, as the largest negative power in the Laurent series is $-2$.

Take for example $f(z)=\frac{e^z-1}{z^2}=\sum_{n=1}^\infty\frac{z^{n-2}}{n!}=\sum_{m=-1}^\infty\frac{z^m}{(m+2)!}$. This clearly has a pole of order $1$ at $z=0$.

Take for example $f(z)=e^{1/z}=\sum_{n=0}^\infty\frac{(1/z)^n}{n!}=\sum_{n=0}^\infty\frac{z^{-n}}{n!}=\sum_{m=-\infty}^0\frac{z^m}{(-m)!}$. This has an essential singularity, there are infinitely many negative power of $z$ in the Laurent series.

# Removable singularities:

Let $f:B_R^*(a)\rightarrow\mathbb{C}$ be holomorphic. Then $f$ has a removable singularity at $z=a$ if and only if $f$ can be extended to a holomorphic function on $B_R(a)$.

To prove this, assume $f$ can be extended to a holomorphic function $\tilde f$ on $B_R(a)$. By Cauchy-Taylor theorem $\tilde f$ has a convergent Taylor series on $B_R(a)$. In particular this power series matches $f$ on $B_R^*(a)$. This must be the Laurent series of $f$ by uniqueness. Now assume that $f$ has a removable singularity. Therefore on $B_R^*(a)$ $f$ can be written as $f(z)=\sum_{n=0}^\infty c_n(z-a)^n$, however power series converge on discs of convergence, so we must have that $\tilde f$ is equivalent to this power series, completing the proof.

Let $f:B_R^*(a)\rightarrow\mathbb{C}$ be holomorphic. Then $f$ has a removable singularity at $z=a$ if and only if:$$ \Huge\lim_{z\to a}(z-a)f(z)=0$$
Assume that $f$ has a removable singularity at $z=a$. Then it can be extended to $\tilde f:B_R(a)\rightarrow\mathbb{C}$, which is continuous at $z=a$. Then:$$\large \lim_{z\to a}(z-a)f(z)=\lim_{z\to a}(z-a)\tilde f(z)=\lim_{z\to a}(z-a)\cdot\lim_{z\to a}\tilde f(z)=0\cdot\lim_{z\to a}\tilde f(z)=0$$Now assume $\lim_{z\to a}(z-a)f(z)=0$. Since $f$ is holomorphic on the annulus $B_R^*(a)$ it must have a Laurent series $f(z)=\sum_{n=-\infty}^\infty c_n(z-a)^n$ with $c_n=\frac{1}{2\pi i}\int_{|z-a|=\rho}\frac{f(z)}{(z-a)^{n+1}}dz$, which is true for any $0<\rho<R$. We aim to show that $c_n=0$ for all $n\leq-1$, that is $f$ has a power series on $B_R(a)$, which is equivalent to having a removable singularity. We have:$$\large 0\leq|c_n|=\left|\frac{1}{2\pi i}\int_{|z-a|=\rho}\frac{f(z)}{(z-a)^{n+1}}dz\right|\leq\frac{1}{2\pi}\cdot L(|z-a|=\rho)\cdot\sup_{|z-a|=\rho}\left|\frac{f(z)}{(z-a)^{n+1}}\right|$$by the estimation lemma. This is equivalent, since the contour is circular, to:$$\Huge 0\leq|c_n|\leq\rho\sup_{|z-a|=\rho}\frac{|(z-a)f(z)|}{|z-a|^{n+2}}=\frac{1}{\rho^{n+1}}\sup_{|z-a|=\rho}|(z-a)f(z)|$$Then letting $\rho\to0$ we can see that the rightmost term tends to $0$ for $n\leq-1$. That is to say, $c_n=0$ for all $n\leq-1$, which means that:$$\Huge f(z)=\sum_{n=0}^\infty c_n(z-a)^n$$and has a removable singularity at $z=a$.

# Riemann Extension theorem:

Let $f:B_R^*(a)\rightarrow\mathbb{C}$ be holomorphic and bounded, then $f$ has a removable singularity. The proof comes from the limit $\lim_{z\to a}(z-a)f(z)=0$, which is equivalent to a removable singularity at $a$, proven above. We assume $\exists M>0$ such that $|f(z)|\leq M$ on $B_R^*(a)$, that is $f$ is bounded. Then:$$\Huge\begin{align} 
\lim_{z\to a}0&\leq\lim_{z\to a}|(z-a)f(z)|\lim_{z\to a}\leq M|z-a|\\
0&\leq\lim_{z\to a}|(z-a)f(z)|\leq0
\end{align}$$Therefore the limit is $0$, so $f$ has a removable singularity.

# Poles:

Let $f:B_R^*(a)\rightarrow\mathbb{C}$ be holomorphic, then the following are equivalent:
1. $f$ has a pole of order $k$ at $z=a$
2. $f(z)=\frac{g(z)}{(z-a)^k}$ where $g$ is holomorphic on $B_R(a)$ and $g(a)\neq0$
3. There exists some $0<r\leq R$ and $h:B_r(a)\rightarrow\mathbb{C}$ holomorphic such that $h$ has a zero of order $k$ at $z=a$ where $f(z)=1/h(z)$ on $B_r^*(a)$

Proofs:
> $1\implies 2$: Assume $f$ has a pole of order $k$ at $z=a$, then $f(z)=\sum_{n=-k}^\infty c_n(z-a)^n$ with $c_{-k}\neq0$. Let $g(z)=(z-a)^kf(z)=\sum_{-k}^\infty c_n(z-a)^{n+k}$, rewriting $m=n+k$ shows that $g(z)=\sum_{m=0}^\infty c_{m+k}(z-a)^m$, which is a power series and is holomorphic on $B_R(a)$. Thus $g$ is the extension of $f$ from $B_R^*(a)$ to $B_R(a)$ and $f$ must therefore have a removable singularity.
> $2\implies 3$: Assume $g$ is holomorphic on $B_R(a)$ and $g(a)\neq0$. So there exists some $0<r\leq R$ such that $g(z)\neq0$ on $B_r(a)$ by the [[Holomorphic functions#Principle of isolated zeros (PIZ)|principle of isolates zeros]]. In particular $h(z)=\frac{(z-a)^k}{g(z)}$ is therefore a quotient of two holomorphic functions with $g(z)\neq0$ on $B_r(a)$. We now have $1/h(z)=f(z)$ as required.
> $3\implies 1$: trivial.

Take for example $f(z)=\tan z/z$. We aim to classify the zeros and isolated singularities of this function:![[poole example]]
Let $f:B_R^*(a)\rightarrow\mathbb{C}$ be holomorphic. Then $f$ has a pole at $z=a$ if and only if:$$\Huge \lim_{z\to a}|f(z)|=\infty$$
To prove this, assume $f$ has a pole at $z=a$. Then $f(z)=g(z)/(z-a)^k$ where $g$ is holomorphic at $z=a$:$$\Huge \lim_{z-\infty}|f(z)|=\lim_{n\to \infty}\frac{|g(z)|}{(z-a)^k}=\infty$$
Assume $\lim_{|z-a|=0}$. There must exists some $r>0$ $f(z)\neq0$ on $B_R3*$ such that $h(z)=1/f(a)$ is holomorphic on $B_r^*(a)$. Note that through the ]]

# Casorati Weierstrass:

Let $f:B_r(a)$ be holomorphic with essential singularity at $z=a$. Then for every $\omega\in G$ and every $0<r\leq R$ and every $\epsilon>0$ there exists some $z\in B_r^*(a)$ such that:$$\Huge f(z)\in B_\epsilon(\omega)$$We argue this by contradiction, so assume the statement is false. Assume there exists some $\omega\in\mathbb{C}$, $0<r\leq R$, and $\epsilon>0$ such that $z=B_r*A(a)$ and $f(z)\neq B_\epsilon(\omega)$ . Therefore:$$\Huge\begin{align}
|f(z)-\omega|\geq\epsilon>0\\

\end{align}$$Now let $g(z)=\frac{1}{f(x)-\omega}$, which is holomorphic in $B_r(a)$. $g$ is bounded here as $\left|\frac{1}{f(z)-\omega}\right|\leq 1/\epsilon$. By the Riemann extension theorem we have that $g$ has a removable singularity at $z=a$ and hence can be extended to some holomorphic function on $B_r(a)$. Now we have for $z\in B_r^*(a)$:$$\Huge f(z)=\omega+\frac{1}{g(z)}=\frac{\omega g(z)+1}{g(z)}$$So if $g(a)\neq0$ we have that $g$ has a removable singularity at $a$. If $g(a)=0$ however, the function $h(z)=1/f(z)$ is holomorphic at $z=a$ and has a zero at $z=a$, therefore $f$ has a pole at $z=a$. This is a contradiction so we have the proof as required.

## Big Picard theorem:
This theorem is an extension of the above, the proof of which is beyond the scope of these notes. Let $f:B_R^*(a)\rightarrow\mathbb{C}$ be holomorphic with an essential singularity at $z=a$. Then there is some $b\in\mathbb{C}$ such that for all $r$ with $0<r<R$:$$\Huge f(B_r^*(a))\supset\mathbb{C}\setminus\{b\}$$