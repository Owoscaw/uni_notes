A real power series is an expression of the form:$$\Huge \sum_{k=0}^\infty a_kx^k$$This may or may not [[Series#Convergence criteria|converge]] for various $x$. Note that if $\sum_{k=0}a_k$ converges, then $\lim_{k\to\infty}a_k=0$. We use various results from [[Series|series]].

# Radius of Convergence:

A power series is an infinite series of form:$$\Huge \sum_{k=0}^\infty a_kx^k$$With $a_k\in\Re$ and $x\in\Re$. The Cauchy-Hadamard theorem states that for such a power series, there exists a constant $R\in[0,\infty]$ such that:
> If $R=0$, then the series converges only for $x=0$
> If $R>0$, then the series converges absolutely for $x\in(-R,R)$, and diverges for $|x|>R$

For the latter case, we write $c=\limsup_{k\to\infty}\sqrt[k]{|a_k|}\in[0,\infty]$, then $R=\frac{1}{c}$. We then call $R$ the radius of convergence of the power series. To prove this:![[Cauchy-Hadamard]]In practice, the ration test also works:$$\Huge \frac{|a_{k+1}x^{k+1}|}{|a_kx^k|}=\left|\frac{a_{k+1}}{a_k}\right|x,\text{ assume}\lim_{k\to\infty}\left|\frac{a_{k+1}}{a_k}\right|=c\text{ exists}$$Then we get absolute convergence for $|x|<\frac{1}{c}$ and divergence for $|x|>\frac{1}{c}$.

The cases where $x=\pm R$ need to be checked separately. Every polynomial $a_kx^k+\dots+a_0$ is a power series with $a_n=0$ when $n>k$, in this case $c=0\implies R=\infty$. For every geometric series, $a_k=1$, causing the radius of convergence to be $1$.

Assume $\sum_{k=0}^\infty a_kc^k$ converges for some $c\neq0$, then $\sum_{k=0}^\infty a_kx^k$ converges absolutely for all $|x|<|c|$. To prove this, consider that $R>0$ since the first series converges for some $c\neq0$, then we have $c\in[-R,R]$, then we have absolute convergence on $(-|c|,|c|)\subset(-R,R)$ apparently this is a proof?

Let $\sum_{k=0}^\infty a_kx^k$ be a power series with radius of convergence $R$, then the formal derivative is given by:$$\Huge \left(\sum_{k=0}^\infty a_kx^k\right)'=\sum_{k=1}^\infty a_kkx^{k-1}=\frac{1}{x}\sum_{k=1}^\infty a_kx^k$$And the formal antiderivative:$$\Huge \int\sum_{k=0}^\infty a_kx^kdx=\sum_{k=0}^\infty\frac{a_k}{k+1}x^{k+1}=\sum_{k=1}^\infty\frac{a_{k+1}}{k}x^k$$Both of these are themselves power series and have radius of convergence equal to $R$. To prove this, set $c=\limsup_{k\to\infty}\sqrt[k]{|a_k|}$ so that $R=1/c$. Then observe the limes supremum of the RHS of both equations (we show derivative): $\limsup_{k\to\infty}\sqrt[k]{|k\times a_k|}=\limsup{k\to\infty}\sqrt[k]{|a_k|}\times\limsup_{k\to\infty}\sqrt[k]{k}=c\times 1=c$, so both have the same radius of convergence.

# Power series as a function:

When considering a power series as a series, every $x\in(-R,R)$ converges to a value and therefore gets assigned a real value, so we can think of it as a function, $f:(-R,R)\mapsto\Re$ with:$$\Huge f(x)=\sum_{k=0}^\infty a_kx^k=\lim_{n\to\infty}\left(\sum_{k=0}^n a_kx^k\right)$$
## Power series are continuous:
Let $\sum_{k=0}^\infty a_kx^k$ be a power series with radius of convergence $R>0$ that defines $f$ as above. Then $f$ is continuous on $(-R,R)$, in fact $f$ is locally Lipschitz continuous on $(-r,r)$ where $0<r<R$. To prove this, pick $n\in\mathbb N$ and define $f_n=\sum_{k=0}^n a_kx^k$, then:$$\large |f_n(x)-f_n(y)|=\left|\sum_{k=1}^na_k(x^k-y^k)\right|=\left|\sum_{k=1}^n a_k(x-y)(x^{k-1}+x^{k-2}y+x^{k-3}y^2+\dots+y^{k-1})\right|$$$$\large |f_n(x)-f_n(y)|=|x-y|\left|\sum_{k=1}^na_k(x^{k-1}+\dots+y^{k-1})\right|\leq|x-y|\sum_{k=1}^n|a_k|(|x^{k-1}|+\dots+|y^{k-1}|)$$$$\Huge |f_n(x)-f_n(y)|\leq|x-y|\sum_{k=1}^n|a_k|kr^{k-1}$$Suppose that the RHS converges to a constant $M$, then the LHS functions converge to $f(x),f(y)$ respectively:$$\Huge |f(x)-f(y)|\leq|x-y|\sum_{k=1}^\infty|a_k|kr^{k-1}=M|x-y|$$Therefore, $f$ is Lipschitz continuous and therefore continuous.

## Power series are differentiable:
Let $f(x)=\sum_{k=0}^\infty a_kx^k$ be a power series with $R\in(0,\infty]$ be its radius of convergence. Then $f$ is infinitely differentiable on $(-R,R)$, and the derivative is given by:$$\Huge f'(x)=\sum_{k=1}^\infty ka_kx^{k-1}$$Furthermore:$$\Huge f^{(n)}(0)=n!\,a_n$$For all $n\geq0$. To prove this, we need to show that the first derivative exists, since this is i