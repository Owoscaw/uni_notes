
We aim to determine whether it is true that for [[Complex differentiation#Holomorphicity|holomorphic]] function $f$ on a domain $D$ then the [[Complex integration#Contour integrals|contour integral]] $\int_\gamma f(z)dz=0$ for all [[Complex integration#Contours|closed contours]] in $D$.

Recall that $\int_{|z|=1}\frac{1}{z}dz=2\pi i\neq0$, and that $|z|=1$ defines a closed contour. This function is holomorphic on $\mathbb{C}^*$, which contains the contour. The problem arises from the anti-derivative $\text{Log}(z)=\ln|z|+i\text{Arg}(z)$, which is not holomorphic on $\mathbb{C}^*$.

# Starlike domains:

A [[Complex differentiation#Paths and connectedness|domain]] $D$ is called starlike if there exists a central point $a_0\in D$ such that for all $b\in D$ the straight line connecting $b$ and $a_0$ is fully contained within $D$. Note that $\mathbb{C}$ is starlike with $a_0=0$, and any [[Metric spaces#Open and closed sets|ball]] ($B_r(a)$) is starlike with $a_0=a$. Note that $a_0$ does not need to be unique.

# Cauchy's Integral Theorem:

Let $f:D\mapsto\mathbb{C}$ be holomorphic on a starlike domain $D$. Then for any closed contour $\gamma\subset D$ we have:$$\Huge\int_\gamma f(z)dz=0$$
Note that the same statement holds if $f$ is holomorphic on some $D\setminus S$ where $S$ is a finite set of points at which $D$ is continuous. We first prove this for triangular contours.

Let $f:U\mapsto\mathbb{C}$ be holomorphic on an open set $U$. Then for any triangular region $\Delta\subset U$:$$\Huge \int_{\partial\Delta}f(z)dz=0$$To prove this, we subdivide the triangle as follows:![[cauchy proof]]Now we have:$$\Huge\int_{\partial\Delta}f(z)dz=\sum_{i=1}^4\int_{\partial\Delta_i}f(z)dz$$This is true for the same reason used in the proof for [[Integral theorems#Proof|Stoke's theorem]]. Through the triangle inequality we have:$$\Huge\left|\int_{\partial\Delta}f(z)dz\right|\leq\sum_{i=1}^4\left|\int_{\partial\Delta_i}f(z)dz\right|\leq4\left|\int_{\partial\Delta_1}f(z)dz\right|$$Where we assume (WLOG) that $\Delta_1$ is the triangle with greatest integration. Note that $L(\partial\Delta_1)=\frac{1}{2}L(\partial\Delta)$. Continue subdividing this way to get the sequence of triangular regions:$$\Huge \Delta\subset\Delta_1\subset\Delta_2\subset\dots$$Such that the following is true:$$\Huge \left|\int_{\partial\Delta}f(z)dz\right|\leq4^n\left|\int_{\partial\Delta_n}f(z)dz\right|,\,\,L(\partial\Delta_n)=2^{-n}L(\partial\Delta)$$Note that as $n\to\infty$ there exists some point $\omega\in U$ such that:$$\Huge \bigcap_{i=1}^\infty\Delta_i=\{\omega\}$$Also by the [[Complex integration#Complex year 1/analysis 1/term 2/Integration Fundamental theorem of Calculus FTOC|FTOC]] we have $\int_\gamma cdz=0=\int_\gamma zdz$ so we have:$$\Huge\int_{\partial\Delta_n}f(\omega)dz=\int_{\partial\Delta_n}zf'(\omega)dz=\int_{\partial\Delta_n}\omega f'(\omega)dz=0$$Which allows us to write the integral as:$$\large\begin{align}
\int_{\partial\Delta_n}f(z)dz=\int_{\partial\Delta_n}f(z)dz+0+0+0&=\int_{\partial\Delta_n}f(z)-f(\omega)-(z-w)f'(\omega)dz\\
&=\int_{\partial\Delta_n}(z-w)\left(\frac{f(z)-f(\omega)}{z-w}-f'(\omega)\right)dz
\end{align}$$Also define:$$\Huge g(z)=\begin{cases}\frac{f(z)-f(\omega)}{z-\omega}-f'(\omega)&z\in U\setminus\{\omega\}\\0&z=\omega\end{cases}$$Note that $\lim_{z\to\omega}g(z)=0=g(\omega)$, so $g$ is a continuous function. Now we have:$$\Huge\begin{align}
4^n\left|\int_{\partial\Delta_n}f(z)dz\right|&=4^n\left|\int_{\partial\Delta_n}(z-\omega)g(z)dz\right|\\
&\leq\frac{4^n}{2^n}L(\partial\Delta)\sup_{z\in\partial\Delta_n}|z-\omega|\sup_{z\in\partial\Delta_n}|g(z)|
\end{align}$$By the estimation lemma. Clearly we have $\sup_{z\in\partial\Delta_n}|z-w|\leq L(\partial\Delta_n)=\frac{1}{2^n}L(\partial\Delta)$ so we have:$$\Huge\left|\int_{\partial\Delta}f(z)dz\right|\leq L(\partial\Delta)^2\sup_{z\in\partial\Delta_m}|g(z)|$$