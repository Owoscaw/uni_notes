
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

