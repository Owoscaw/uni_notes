
# Cauchy-Taylor theorem:

Let $f:U\rightarrow\mathbb{C}$ be [[Complex differentiation#Holomorphicity|holomorphic]] on some open set $U$ and let $B_r(a)$ be some open ball in $U$. Then $f$ can be represented by a [[Power series|power series]] on $B_r(a)$ given by:$$\Huge f(z)=\sum_{n=0}^\infty c_n(z-a)^n,\,\,c_n=\int_{|z-a|=\rho}\frac{f(z)}{(z-a)^{n+1}}dz$$for any $0<\rho<r$. This is known as the Taylor series of $f$. To prove this, fix some $0<\rho<r$, then for any $|\omega-a|<\rho$ we have by [[Cauchy's theorem#Cauchy's Integral Theorem|CIF]] that:$$\Huge f(\omega)=\frac{1}{2\pi i}\int_{|z-a|=\rho}\frac{f(z)}{z-\omega}dz$$Then by uniform convergence we have:$$\Huge\begin{align}
f(\omega)&=\frac{1}{2\pi i}\int_{|z-a|=\rho}f(z)\sum_{n=0}^\infty\frac{(\omega-a)^n}{(z-a)^{n+1}}dz\\
&=\sum_{n=0}^\infty\frac{1}{2\pi i}\int_{|z-a|=\rho}\frac{f(z)}{(z-a)^{n+1}}dz\,(\omega-a)^n\\
&=\sum_{n=0}^\infty c_n(\omega-a)^n
\end{align}$$So we get the power series in $\omega$, proving the result as required. One can show that $c_n$ is indeed well defined. Using the result for the [[Convergence and Power series#Differentiation and Integration of Power series|derivative of a power series]]:$$\Huge c_n=\frac{f^{(n)}(a)}{n!}$$We see that $c_n$ is indeed well defined.

# CIF for derivatives:

Let $f:U\rightarrow\mathbb{C}$ be holomorphic on an open set $U$ and $B_r(a)\subset U$. Then for any $0<\rho<r$ we have:$$\Huge \int_{|z-a|=\rho}\frac{f(z)}{(z-a)^{n+1}}dz=\frac{2\pi i}{n!}f^{(n)}(a)$$This comes immediately from comparing the formulae for $c_n$. 