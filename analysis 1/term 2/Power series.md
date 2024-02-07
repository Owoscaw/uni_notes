A real power series is an expression of the form:$$\Huge \sum_{k=0}^\infty a_kx^k$$This may or may not [[Series#Convergence criteria|converge]] for various $x$. Note that if $\sum_{k=0}a_k$ converges, then $\lim_{k\to\infty}a_k=0$. We use various results from [[Series|series]].

# Radius of Convergence:

A power series is an infinite series of form:$$\Huge \sum_{k=0}^\infty a_kx^k$$With $a_k\in\Re$ and $x\in\Re$. The Cauchy-Hadamard theorem states that for such a power series, there exists a constant $R\in[0,\infty]$ such that:
> If $R=0$, then the series converges only for $x=0$
> If $R>0$, then the series converges absolutely for $x\in(-R,R)$, and diverges for $|x|>R$

For the latter case, we write $c=\limsup_{k\to\infty}\sqrt[k]{|a_k|}\in[0,\infty]$, then $R=\frac{1}{c}$. We then call $R$ the radius of convergence of the power series. To prove this:![[Cauchy-Hadamard]]In practice, the ration test also works:$$\Huge \frac{|a_{k+1}x^{k+1}|}{|a_kx^k|}=\left|\frac{a_{k+1}}{a_k}\right|x,\text{ assume}\lim_{k\to\infty}\left|\frac{a_{k+1}}{a_k}\right|=c\text{ exists}$$Then we get absolute convergence for $|x|<\frac{1}{c}$ and divergence for $|x|>\frac{1}{c}$.

The cases where $x=\pm R$ need to be checked separately. Every polynomial $a_kx^k+\dots+a_0$ is a power series with $a_n=0$ when $n>k$, in this case $c=0\implies R=\infty$. For every geometric series, $a_k=1$, causing the radius of convergence to be $1$.

Assume $\sum_{k=0}^\infty a_kc^k$ converges for some $c\neq0$, then $\sum_{k=0}^\infty a_kx^k$ converges absolutely for all $|x|<|c|$. To prove this, consider that $R>0$ since the first series converges for some $c\neq0$, then we have $c\in[-R,R]$, then we have absolute convergence on $(-|c|,|c|)\subset(-R,R)$ apparently this is a proof?

Let $\sum_{k=0}^\infty a_kx^k$ be a power series with radius of convergence $R$, then the formal derivative is given by:$$\Huge \left(\sum_{k=0}^\infty a_kx^k\right)'=\sum_{k=1}^\infty a_kkx^{k-1}=\frac{1}{x}\sum_{k=1}^\infty a_kx^k$$And the formal antiderivative:$$\Huge \int\sum_{k=0}^\infty a_kx^kdx=\sum_{k=0}^\infty\frac{a_k}{k+1}x^{k+1}=\sum_{k=1}^\infty\frac{a_{k+1}}{k}x^k$$Both of these are themselves power series and have radius of convergence equal to $R$. To prove this, set $c=\limsup_{k\to\infty}\sqrt[k]{}$