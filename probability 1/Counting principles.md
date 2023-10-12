
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
This is because there are $(m)_r$ distinct ordered lists of $r$ objects. There are $r!$ ways of arranging $r$ objects, so each unordered subset is counted $r!$ times. This is why we divide $(m)_r$ by $r!$ to give the result above.

# Multinomial coefficient:

When dividing $m$ distinguishable objects into $k>2$ groups of sizes $r_1,r_2,\dots,r_k$ each, where $r_1+r_2+\dots r_k=m$:
$$\Huge \begin{pmatrix}m\\r_1\end{pmatrix}\times\begin{pmatrix}m-r_1\\r_2\end{pmatrix}\times\begin{pmatrix}m-r_1-r_2\\r_3\end{pmatrix}\times\dots\times\begin{pmatrix}m-r_1-\dots-r_{k-1}\\r_k\end{pmatrix}$$
$$\Large \frac{m!}{(m-r_1)!r_1!}\times\frac{(m-r_1)!}{(m-r_1-r_2)!r_2!}$$