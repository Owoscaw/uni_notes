
Given a finite sample space, and assuming that all outcomes are equally likely ([[Classical probability]]), counting can become the major part of a problem.

# Multiplication principle:

Suppose that $k$ choices are made in succession, where there are:
> $m_1$ possibilities for the first choice
> $m_2$ possibilities for the second choice
> $m_k$ possibilities for the $k$th choice

The number of possible arrangements is given by:
$$\Huge m_1\times m_2\times\dots\times m_k=\prod_{i=1}^km_i$$
# Ordered choice with replacement:

Suppose a collection of $m$ distinct objects and $r$ of them are selected without replacement. The number of different ordered lists is given by:
$$\Huge m\times\dots\times m=m^r$$
# Ordered choice w/o replacement:

Suppose a collection of $m$ distinct objects and $r\leq m$ are taken without replacement. The number of different ordered lists is given by:
$$\Huge (m)_r:=m\times(m-1)\times(m-2)\times\dots\times(m-r+1)=\frac{m!}{(m-r)!}$$
This is known as the falling factorial of $m$.

# Unordered choice w/o replacement:

Suppose a collection of $m$ distinct objects and $r\leq m$ are taken without replacement. The number of distinct subsets of size $r$ is given by:
$$\Huge \begin{pmatrix}m\\r\end{pmatrix}:=\frac{(m)_r}{r!}=\frac{m!}{r!(m-r)!}$$