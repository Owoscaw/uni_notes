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
Let $f(x)=\sum_{k=0}^\infty a_kx^k$ be a power series with $R\in(0,\infty]$ be its radius of convergence. Then $f$ is infinitely differentiable on $(-R,R)$, and the derivative is given by:$$\Huge f'(x)=\sum_{k=1}^\infty ka_kx^{k-1}$$Furthermore:$$\Huge f^{(n)}(0)=n!\,a_n$$For all $n\geq0$. To prove this, we need to show that the first derivative exists, since this is itself a power series with the same radius of convergence. Let $c\in(-\infty,\infty)$, then:$$\Huge f(x)-f(c)=\sum_{k=1}^\infty a_k(x-c)(x^{k-1}+x^{k-2}c+\dots+xc^{k-2}+c^{k-1})$$$$\Huge f(x)=f(c)+(x-c)\sum_{k=1}^\infty a_k(x^{k-1}+\dots+c^{k-1}),\,\,f_1(x)=\sum_{k=1}^\infty a_k(\dots)$$$$\Huge f_1(c)=\sum_{k=1}^\infty a_kkc^{k-1}$$We want to use first order Taylor with $f(x)=f(x)+(x-c)f_1(c)$, so we require that $f_1$ is continuous at $c$. The formula for the $n$-th derivative at $0$ is proven by induction:$$\large f^{(n)}(x)=\sum_{k=n}^\infty k(k-1)\dots(k-n+1)a_kx^{k-n}=\sum_{k=0}^\infty (k+1)(k+2)\dots(k+n)a_{k+n}x^k$$Evaluating this at zero:$$\Huge f^{(n)}(0)=n!a_n$$
Let $\sum_{k=0}^\infty a_kx^k,\sum_{k=0}^\infty b_kx^k$ be two power series with radii of convergence $R_a,R_b$ respectively. If both agree as functions on $(-r,r)$ with $0<r<\min\{R_a,R_b\}$ then we have $a_k=b_k$ for all $k$. To prove this, let $f(x)=\sum_{k=0}^\infty a_kx^k$ and $g(x)=\sum_{k=0}^\infty a_kx^k$, since $f=g$ on $(-r,r)$ then:$$\Huge k!a_k=f^{(k)}(0)=g^{(k)}(0)=k!b_k$$It is trivial to see that then $a_k=b_k$.

# Abel's limit theorem:

Let $f(x)=\sum_{k=0}^\infty a_kx^k$ be a power series with radius of convergence $R$ and assume that the power series converges at the endpoint $x=R$:$$\Huge \sum_{k=0}^\infty a_kR^k\,\,\text{converges}$$Then if $f$ is left continuous at $x=R$, that is:$$\Huge \lim_{x\to R^-}f(x)=\sum_{k=0}^\infty a_kR^k$$One can use this to establish Leibniz's formulae for $\log2$ and $\arctan1= \frac{\pi}{4}$.

# Exponentials, logarithms, and trig:

We define the exponential function $\exp x$ by:$$\Huge e^{x}=\sum _{k=0}^{\infty} \frac{x^k}{k!}=1+x+\frac{1}{2}x^2+\frac{1}{6}x^3+\dots$$We deduce the following properties:
>$\exp0=1$ 
>The exponential function is inifnitely differentiable on $\Re$ with $(\exp x)'=\exp x$
>For all $x,y\in\Re$ we have $\exp(x+y)=\exp x\exp y$ and $\exp(-x)= \frac{1}{\exp x}$
>$\exp x>0$ for all $x\in\Re$
>$\exp x$ is strictly monotone increasing
>$\lim_{x\to\infty}\exp x=\infty$ and $\lim_{x\to -\infty}\exp x=0$

To prove this, differentiate termwise to get:$$\Huge \exp'x=\sum_{k=1}^{\infty}k \frac{x^{k-1}}{k!}=\sum_{k=0}^{\infty}(k+1)\frac{x^k}{(k+1)!}=\sum_{k=0}^{\infty}\frac{x^k}{k!}=\exp{x}$$Then for the third result consider $f(t)=\exp(x+t)\exp(y-t)$. Note that this is differentiable on $\Re$ with $f(0)=\exp(x)\exp(y)$ and $f(y)=exp(x+y)$, then:$$\Huge f'(t)=\exp(x+t)\exp(y-t)-\exp(x+t)\exp(y-t)=0$$Therefore $f$ is constant, so $f(0)=f(y)$, proving the statement.

## Euler's number:
We define:$$\Huge e=\exp(1)=\sum_{k=0}^{\infty} \frac{1}{k!}=1+\frac{1}{2}+\frac{1}{6}+\dots$$We also have