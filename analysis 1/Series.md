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
Just because the sequence converges to zero, the series does not necessarily converge. This is shown in the following example:![[harmonic divergence]]
Assume that $\sum_{k=0}^\infty a_k$ and $\sum_{k=0}^\infty b_k$ both converge to $a$ and $b$ respectively. Then we can define a sort of [[Sequences#Calculus of limits theorem ( Limits and Continuity Consequences of continuity COLT )|COLT]] for series:
> $\displaystyle{\sum_{k=0}^\infty}a_k+b_k$ converges to $a+b$
> $\displaystyle{\sum_{k=0}^\infty \lambda a_k}$ converges to $\lambda a$ with $\lambda\in\Re$

# Convergence criteria:

Let $N\in\mathbb N$, and $(a_k)_{k\geq N},(b_k)_{k\geq N}$ be sequences with $0\leq a_k\leq b_k$ for all $k\geq N$ (comparison test):
> If $\displaystyle{\sum_{k=N}^\infty b_k}$ is convergent with limit $b$, then $\displaystyle{\sum_{k=N}^\infty a_k}$ is also convergent with limit $a\leq b$
> If $\displaystyle{\sum_{k=N}^\infty a_k}$ is divergent, then so is $\displaystyle{\sum_{k=N}^\infty b_k}$

This is proven as follows. Let $s_n=\sum_{k=N}^na_k$ and $t_n=\sum_{k=N}^n$. We have $0\leq s_n\leq t_n\leq b$, since $(t_n)$ is monotonically increasing with a limit $b$. $(s_n)$ is also monotonically increasing and bounded above by $b$, so must be convergent to a limit $a$. $s_n\leq t_n$ implies:$$\Huge a=\lim_{n\to\infty}s_n\leq\lim_{n\to\infty}t_n=b
$$
Notice that $a_k\geq0$ is bounded by the limit of $t_n$. So if $s_n$ is not convergent, it is not bounded by the limit of $t_n$, so this limit cannot exist. Therefore $t_n$ must also be divergent.

Let $\alpha\in\Re$, then:$$\Huge \sum_{k=1}^\infty\frac{1}{k^\alpha}\,\,\text{converges}\iff\alpha>1$$
If $\alpha=1$, we get the harmonic series, which has been shown to diverge. If we take $\alpha\leq1$, we get that the series is still divergent by the above theorem. So now assume $\alpha>1$:
![[Series .excalidraw]]

# Alternating series:

A series $\displaystyle{\sum_{k=1}^\infty a_k}$ is alternating if:
> $a_{2k}\geq0$ and $a_{2k-1}\leq 0$ for all $k\in\mathbb N$
> or $a_{2k}\leq0$ and $a_{2k-1}\geq0$ for all $k\in\mathbb N$

## Alternating sign test:

Let $(a_k)_{k\in\mathbb N}$ be a monotonically decreasing sequence of positive numbers with $\lim_{n\to\infty} a_k=0$, then the alternating series $\displaystyle{\sum_{k=1}^\infty(-1)^{k+1}a_k}$ is also convergent. Considering the sequence of partial sums, we have:$$\Huge s_2\leq s_4\leq\dots\leq\sum_{k=1}^\infty(-1)^{k+1}a_k\leq\dots\leq s_3\leq s_1$$
$$\Huge \left|s_n-\sum_{k=1}^\infty(-1)^{k+1}a_k\right|\leq a_{n+1}$$
Since $a_k$ is monotonically increasing, we get $a_k-a_{k-1}\geq0$, which implies $a_{2n+1}-a_{2n+2}\geq0$. Adding the partial sum $s_{2n}$, we get $s_{2n+2}=s_{2n}+a_{2n+1}-a_{2n+2}\geq s_{2n}$, so the subsequence $(s_{2n})_{n\in\mathbb N}$ is monotonically increasing. Similarly, we can show $(s_{2n-1})_{n\in\mathbb N}$ 