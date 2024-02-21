
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

