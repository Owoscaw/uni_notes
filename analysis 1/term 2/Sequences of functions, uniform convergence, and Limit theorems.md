
# Convergence of functions:

Let $(f_n)_{n\in \mathbb{N}}$ be a sequence of functions $f_n:I\mapsto\Re$ for some interval $I$. This sequence has a pointwise limit if for all $x\in I$, the limit $\lim_{n\to\infty}f_n(x)$ exists. We can describe this formally as follows. For all $x\in I$ and all $\epsilon>0$ there exists $N\in \mathbb{N}$ such that for all $n\geq N$, we have that $|f_n(x)-f(x)|<\epsilon$. Here, $N$ depends on both $\epsilon$ and $x$. 

Example: Let $f_n:[0,1]\mapsto\Re$ be defined as $f_n(x)=x^n$. Note if $x=1$, $f_n(x)=1$ for all $n\in \mathbb{N}$ and $f(x)=1$. However if $x\in[0,1)$, $x^n\to 0$, and $f(x)=0$. The limit function is then given by:$$\Huge f(x)=\begin{cases}0&x\in[0,1)\\1&x=1\end{cases}$$
Let $(f_n)_{n\in \mathbb{N}}$ be a sequence of functions $f_n:I\mapsto\Re$. We say that $f_n$ converges uniformly to $f:I\mapsto\Re$ if for every $\epsilon>0$ there exists $N\in \mathbb{N}$ such that for all $n\geq N$ and all $x\in I$ we have that $|f_n(x)-f(x)|<\epsilon$. This is different to pointwise convergence since $N$ no longer depends on $x$, it must hold for all $n\geq N$ and $x\in I$.