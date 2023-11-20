# Fundamental notions and properties:

Let $(a_k)_{k\in\mathbb N}$ be a [[Sequences#Limit of a sequence|sequence]]. Then the sequence of partial sums $(s_n)_{n\in\mathbb N}$ is defined as:$$\Huge S_n=\sum_{k=1}^na_k=a_1+\dots+a_n$$
This sequence is called the series of $(a_k)_{k\in\mathbb N}$ . If the sequence $(S_n)_{n\in\mathbb N}$ is convergent, then the series is convergent. In this case we write:$$\Huge \sum_{k=1}^\infty a_k=\lim_{n\to\infty}s_n$$
Otherwise it is called divergent. Sometimes series start at $k=0$, this will affect the limit, however convergence is not. That is to say:$$\Huge \sum_{k=1}^\infty a_k\,\,\text{converges}\iff\sum_{k=N}^\infty a_k\,\,\text{converges}$$
## Geometric series:

Take $q\in\Re$, then define:$$\Huge S_n=\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q},\,\,q\neq 1$$$$\Huge \lim_{n\to\infty}S_n=\lim_{n\to\infty}\frac{1-q^{n+1}}{q-1}=\begin{cases}\displaystyle{\frac{1}{1-q}}&\text{for}\,\,|q|<1\\\text{unbounded}&\text{for}\,\,|q|>1\end{cases}$$ 
The special cases where $q=\pm1$ are defined as follows:$$\Huge S_n=\sum_{k=0}^n1^k=1+1+\dots+1=n,\,\lim_{n\to\infty}S_n=\text{unbounded}$$
$$\large S_n=\sum_{k=0}^n(-1)^k=1-1+\dots+(-1)^n=\begin{cases}1&\text{if $n$ is even}\\0&\text{if $n$ is odd}\end{cases},\,\lim_{n\to\infty}S_n\,\text{is not convergent}$$
So we have:$$\Huge \sum_{k=0}^\infty q^k=\frac{1}{1-q}\iff|q|<1$$
If $\sum_{k=0}^\infty a_k$ is convergent, then $\lim_{k\to\infty}a_k=0$. This is proven as follows:![[series divergence criteria]]
Just because the sequence converges to zero, the series does not necessarily converge. This is shown in the following example:![[Series .excalidraw]]