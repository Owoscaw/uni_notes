
# Convergence of functions:

Let $(f_n)_{n\in \mathbb{N}}$ be a sequence of functions $f_n:I\mapsto\Re$ for some interval $I$. This sequence has a pointwise limit if for all $x\in I$, the limit $\lim_{n\to\infty}f_n(x)$ exists. We can describe this formally as follows. For all $x\in I$ and all $\epsilon>0$ there exists $N\in \mathbb{N}$ such that for all $n\geq N$, we have that $|f_n(x)-f(x)|<\epsilon$. Here, $N$ depends on both $\epsilon$ and $x$. 

Example: Let $f_n:[0,1]\mapsto\Re$ be defined as $f_n(x)=x^n$. Note if $x=1$, $f_n(x)=1$ for all $n\in \mathbb{N}$ and $f(x)=1$. However if $x\in[0,1)$, $x^n\to 0$, and $f(x)=0$. The limit function is then given by:$$\Huge f(x)=\begin{cases}0&x\in[0,1)\\1&x=1\end{cases}$$
Let $(f_n)_{n\in \mathbb{N}}$ be a sequence of functions $f_n:I\mapsto\Re$. We say that $f_n$ converges uniformly to $f:I\mapsto\Re$ if for every $\epsilon>0$ there exists $N\in \mathbb{N}$ such that for all $n\geq N$ and all $x\in I$ we have that $|f_n(x)-f(x)|<\epsilon$. This is different to pointwise convergence since $N$ no longer depends on $x$, it must hold for all $n\geq N$ and $x\in I$. This makes uniform convergence much stronger than pointwise convergence. Note that uniform convergence implies pointwise convergence. Assume $(f_n)_{n\in \mathbb{N}}$ converges uniformly to $f$, then $(f_n)_{n\in \mathbb{N}}$ converges pointwise to $f$. 

To prove this, choose any $x\in I,\epsilon>0$. Then we require $N\in \mathbb{N}$ such that $|f_n(x)-f(x)|<\epsilon$ for all $n\geq N$. Since $(f_n)$ converges uniformly to $f$, choose $N$ for the choice of $\epsilon>0$.

Returning to $f_n(x)=x^n$, note that this does not converge to the proposed function uniformly. Take $\epsilon=\frac{1}{4}$. If we have uniform convergence, then there exists $N\in \mathbb{N}$ with $|f_n(x)-f(x)|<\frac{1}{4}$ for all $n\geq N$ and $x\in[0,1]$. Choose $x=x_n=\sqrt[n]{\frac{1}{2}}<1\implies f(x_n)=0$, then $|f_n(x_n)-f(x_n)=f_n(x_n)(\sqrt[n]{\frac{1}{2}})^n=\frac{1}{2}>\frac{1}{4}$, so the limit definition is not satisfied and $f_n(x)=x^n$ does not converge to $f$ uniformly.

Let $f_n$ be a sequence of functions on an interval $I$ converging pointwise to a limit function $f:I\mapsto\Re$. We say that $f_n$ converges uniformly to $f$ on all compact subintervals $[a,b]\subset I$:
> If there exists a sequence $(a_n)_{n\in \mathbb{N}}$ of positive real numbers with $\lim_{n\to \infty}a_n=0$ such that $|f_n(x)-f(x)|\leq a_n$ for all $x\in I$, then $f_n$ converges uniformly to $f$.
> If there exists $\epsilon>0$ and a sequence $x_n\in I$ such that for all $n$ sufficiently large: $|f(x_n)-f_n(x_n)|\geq\epsilon$, then $f_n$ does not converge uniformly to $f$.

We now prove each criterion. Take $\epsilon>0$, since $a_n\to0$ there exists $N\in \mathbb{N}$ such that $a_n<\epsilon$ for all $n\geq N$. Now $|f(x)-f_n(x)|\leq a_n<\epsilon$ for all $n\geq N$ and all $x\in I$, so we have uniform convergence.

Take $\epsilon'>0$, we need $N$ such that $|f(x)-f_n(x)|<\epsilon'$ for all $x\in I$ and all $n\geq N$. This cannot work for $\epsilon'<\epsilon$ since we can observe at $x=x_n$ this is untrue.

# Uniform convergence preserves continuity:

Let $f_n$ be a sequence of continuous functions on an interval $I$ such that $f_n$ converges uniformly to $f:I\mapsto\Re$, then $f$ is also continuous. Let $c\in I,\epsilon>0$. Since $f_n\to f$ uniformly, there exists $N\in \mathbb{N}$ such that $|f(x)-f_n(x)|<\frac{\epsilon}{3}$ for all $x\in I$ and $n\geq N$. We can use the continuity of $f_N$ at $c$ so that there exists $\delta>0$ such that $|f_N(x)-f_N(c)|<\frac{\epsilon}{3}$ for all $x$ with $|x-c|<\delta$:$$\Huge |f(x)-f(c)|=|f(x)-f_N(x)+f_N(x)-f_N(c)+f_N(c)-f(c)|$$Now we use the triangle inequality:$$\large |f(x)-f(c)|\leq|f(x)-f_N(x)|+|f_N(x)-f_N(c)|+|f_N(c)-f(c)|<\frac{\epsilon}{3}+\frac{\epsilon}{3}+\frac{\epsilon}{3}=\epsilon$$Therefore $f$ is continuous at $c$. Since $c$ was arbitrary, then $f$ is also continuous on the interval $I$.

Let $f_n$ be a sequence of continuous functions on an interval $I$ such that $f_n$ converges uniformly on all compact subsets of $I$, then the limit function is continuous. Because continuity is a local property, for $c\in I$ look at $c\in[ab]\subset I$. Now apply the above theorem to the function limited to the new interval $f_n|_{[a,b]}$ and we get the result as required.

Let $f_n$ be a sequence of continuously differentiable functions on an interval $I$ and assume:
>the sequence converges pointwise to $f$
>the sequence $f_n'$ converges uniformly to $g$

Then $f$ is continuously differentiable on $I$ with:$$\Huge f'(x)=g(x)=\lim_{n\to\infty}f_n'(x)$$

# Weierstrass M-test:

Let $I\subset\Re$ be an interval and $(f_k)$ a sequence of functions $f_k:I\mapsto\Re$. Let $M_k$ be a sequence of real numbers satisfying:
> $|f_k(x)|\leq M_k$ for all $x\in I$
> $\sum_{k=0}^\infty M_k$ is convergent

Then $\sum_{k=0}^\infty f_k(x)$ converges uniformly and absolutely to a limit function $f:I\mapsto\Re$. This is because for each $x\in I$ the series $\sum f_k(x)$ converges absolutely by the comparison test. So define:$$\Huge f(x)=\sum_{k=0}^\infty f_k(x)$$To show $F_n(x)=\sum_{k=0}^nf_k(x)$ converges uniformly to $f$ let $\epsilon>0,L=\sum_{k=0}^\infty M_k$. Then there exists $N\in \mathbb{N}$ with:$$\Huge \sum_{k=n+1}^\infty M_k=\left|L-\sum_{k=0}^nM_k\right|<\epsilon$$For all $n\geq N$. This implies for all $x\in I,n\geq N$ that:$$\large |f(x)-F_n(x)|=\left|f(x)-\sum_{k=0}^nf_k(x)\right|=\left|\sum_{k=n+1}^\infty f_k(x)\right|\leq\sum_{k=n+1}^\infty|f_k(x)|\leq\sum_{k=N+1}^\infty M_k<\epsilon$$So we get that $F_n$ converges uniformly to $f$ on the interval $I$. This provides a useful tool to determine the continuity of infinite series of functions.

Let $f(x)=\sum_{k=0}^\infty a_kx^k$ be a real power series with radius of convergence $R>0$, then:
> The power series $\sum_{k=0}^\infty a_kx^k$ converges uniformly in compact subsets of $(-R,R)$
> $f(x)$ is infinitely differentiable on $(-R,R)$ with $f'(x)=\sum_{k=0}^\infty(k+1)a_{k+1}x^k$ 

To prove this, let $[a,b]$ be a compact interval in $(-R,R)$. Then we can find $0<r<R$ such that $[a,b]\subseteq[-r,r]\subset(-R,R)$. We then apply the M test for $f_k(x)=a_kx^k$ for the interval $I=[-r,r]$. Take $M_k=|a_k|r^k$, then $|f_k(x)|\leq M_k$ for all $x\in I$ and $\sum_{k=0}^\infty|a_k|r^k$ converges since power series converge absolutely within their interval of convergence. So we have that $\sum_{k=0}^\infty a_kx^k$ converges uniformly in $[-r,r]$, particularly in $[a,b]$. This shows the first statement.

To prove the second statement, set $g_1(x)=\sum_{k=1}^\infty a_k(x^{k-1}+x^{k-2}c+\dots+xc^{k-2}+c^{k-1})$. Note that $g_1(c)=\sum_{k=1}^\infty a_kkc^{k-1}$. Considering the first order Taylor expansion, what remains to be shown to obtain differentiability is that $g_1(x)$ is continuous at $x=c$. As before, apply the M test for $f_k(x)=a_k(x^{k-1}+x^{k-2}c+\dots+xc^{k-2}+c^{k-1})$ for the interval $I=[-r,r]$, containing $c$ as an inner point. Take $M_k=|a_k|rr^{k-1}$. Then we have $|f_k(x)|\leq|a_k|(|x|^{k-1}+|x|^{k-2}|c|+\dots+|x||c|^{k-2}+|c|^{k-1})\leq|a_k|(r^{k-1}+r^{k-2}r+\dots+rr^{k-2}+r^{k-2})=|a_k|kr^{k-1}=M_k$, for all $x\in I$. But now $\sum_{k=1}^\infty|a_k|r^{k-1}$ converges since the formal derivative $\sum_{k=0}^\infty(k+1)a_{k+1}x^k$ converges absolutely within their interval of convergence. Hence $g_1(x)$ is continuous and therefore $f(x)$ is differentiable at $c$ with $f'(c)=\sum_{k=1}^\infty a_kkc^{k-1}$ as required.

Let $I\subset\Re$ be an interval and $(f_k)$ be a sequence of differentiable functions $f_k:I\mapsto\Re$. Assume $\sum_{k=0}^\infty f_k(x)$ converges pointwise in $I$ to a function $f(x)$ and $\sum_{k=0}^\infty f_k'(x)$ converges uniformly in all compact subsets of $I$. Then we say that if $f(x)=\sum_{k=0}^\infty f_k(x)$ is a differentiable function on $I$, then:$$\Huge f'(x)=\sum_{k=0}^\infty$$