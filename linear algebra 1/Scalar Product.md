
The scalar product is a function that maps two vectors in $\Re^n$ to a real value. This can be written as:
$$\Huge \cdot :\Re^n\times\Re^n\mapsto\Re$$
$$\Huge \left(\underline u,\underline v\right)\mapsto\underline u\cdot\underline v$$
This can also be expressed through matrix multiplication by transposing the vector $\underline u$:
$$\Huge \underline u\cdot\underline v=\underline u^{\top}\times\underline v=\begin{pmatrix}u_1&\dots&u_n\end{pmatrix}\begin{pmatrix}v_1\\\vdots\\v_n\end{pmatrix}\,\,\forall\underline u,\underline v\in\Re^n$$
This process results in a 1x1 matrix, so the result of the scalar product between two vectors is taken to be the sole entry in this matrix.

Scalar product satisfies the following axioms:
> Symmetry ($I$): $$\Huge \underline u\cdot\underline v=\underline v\cdot\underline u,\,\,\forall\underline u,\underline v\in\Re^n$$
> Linearity in the first factor ($II$):$$\Large (\underline u+\underline v)\cdot\underline w=\underline u\cdot\underline w+\underline v\cdot\underline w,\,\,(\lambda\underline v)\cdot\underline w=\lambda(\underline v\cdot\underline w)$$$$\Huge \forall\underline u,\underline v,\underline w\in\Re^n,\,\,\forall\lambda\in\Re$$
> Linearity in the second factor ($III$):$$\Large \underline u\cdot(\underline v+\underline w)=\underline u\cdot\underline v+\underline u\cdot\underline w,\,\,\underline u\cdot(\lambda\underline v)=\lambda(\underline u\cdot\underline v)$$$$\Huge \forall\underline u,\underline v,\underline w\in\Re^n,\,\,\forall\lambda\in\Re$$
> Positivity ($IV$):$$\Large \underline v\cdot\underline v\geq0,\,\,\underline v\cdot\underline v=\sum_{i=1}^{n}v_i\times v_i=\sum_{i=1}^{n}(v_i)^2$$
> Here, each element of $\underline v$, $v_{1\dots i}$, is squared so must all be positive. Since we are summing over only positive numbers, the resulting sum must always be positive.$$\Huge \forall\underline v\in\Re^n$$$$\Huge \underline v\cdot\underline v=0\,\,only\,\,when\,\,\underline v=\underline 0$$
# Cauchy-Schwarz inequality:

Given $\underline u, \underline v \in \Re^n$:
$$\Huge |\underline u\cdot\underline v|\leq|\underline u||\underline v|$$
This comes from the fact that $cos\,\theta$