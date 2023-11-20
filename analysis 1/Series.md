# Fundamental notions and properties:

Let $(a_k)_{k\in\mathbb N}$ be a [[Sequences#Limit of a sequence|sequence]]. Then the sequence of partial sums $(s_n)_{n\in\mathbb N}$ is defined as:$$\Huge S_n=\sum_{k=1}^na_k=a_1+\dots+a_n$$
This sequence is called the series of $(a_k)_{k\in\mathbb N}$ . If the sequence $(S_n)_{n\in\mathbb N}$ is convergent, then the series is convergent. In this case we write:$$\Huge \sum_{k=1}^\infty a_k=\lim_{n\to\infty}s_n$$
Otherwise it is called divergent. Sometimes series start at $k=0$, this will affect the limit, however convergence is not. That is to say:$$\Huge \sum_{k=1}^\infty a_k\,\,\text{converges}\iff\sum_{k=N}^\infty a_k\,\,\text{converges}$$
## Geometric series:

Take $q\in\Re$, then define:$$\Huge S_n=\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q},\,\,q\neq 1$$$$\Huge $$