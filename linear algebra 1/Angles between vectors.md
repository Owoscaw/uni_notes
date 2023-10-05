For two vectors in the [[Vector space definitions|vector space]], $\Re^2$, the angle between them can be found through the use of the [[Scalar Product|scalar product]]. This angle is derived by consider the vectors using [[Polar coordinates in R2|polar coordinates]]:
$$\Huge let\,\, \underline u,\underline v\in\Re^2,\,where\,\,\underline u,\underline v\neq\underline 0$$
$$\Large \underline u=\begin{pmatrix}r_1cos\,\alpha\\r_1sin\,\alpha\end{pmatrix},\,\underline v=\begin{pmatrix}r_2cos\,\beta\\r_2sin\,\beta\end{pmatrix}$$
$$\Large |\underline u|=r_1,\,|\underline v|=r_2,\,where\,\,r_1,r_2\gt0$$
$$\Large arg(\underline u)=\alpha,\,arg(\underline v)=\beta,\,where\,\,\alpha,\beta\in[0,2\pi)$$
Using the scalar product:
$$\large \underline u\cdot\underline v=\begin{pmatrix}r_1cos\,\alpha\\r_1sin\,\alpha\end{pmatrix}\cdot\begin{pmatrix}r_2cos\,\beta\\r_2sin\,\beta\end{pmatrix}=r_1r_2cos\,\alpha\,cos\,\beta+r_1r_2sin\,\alpha\,sin\,\beta$$
$$\large \underline u\cdot\underline v=r_1r_2\left(cos\,\alpha\,cos\,\beta+sin\,\alpha\,sin\,\beta\right)=r_1r_2(cos(\alpha-\beta))$$
Here, $\alpha -\beta$ is the angle between $\underline u$ and $\underline v$, so:
$$\Huge \underline u\cdot\underline v=|\underline u||\underline v|\,cos\,\theta$$
$$\Huge \forall\underline u,\underline v\in\Re^2,\,and\,\,\theta\in[0,2\pi)$$

# Cauchy-Schwarz inequality:

Given $\underline u, \underline v \in \Re^n$:
$$\Huge |\underline u\cdot\underline v|\leq|\underline u||\underline v|$$
This comes from the fact that $cos\,\theta$ has a range of $-1\leq cos\,\theta\leq1$, and $0\leq|cos\,\theta|\leq1$.

# Generalisation to $\Re^n$:

If $\underline u, \underline v \in\Re^n$, and that $\underline u, \underline v \neq \underline 0$, the angle that $\underline u$ makes with $\underline v$, $\theta \in[0,\pi]$ is defined to be:
$$\Huge cos\,\theta=\frac{\underline u\cdot\underline v}{|\underline u||\underline v|}$$
Vectors are perpendicular when they make an angle of $\frac{\pi}{2}$:
$$\Huge \underline u\cdot\underline v=0$$