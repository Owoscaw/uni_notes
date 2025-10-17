
# Hilbert space:

A Hilbert space is a [[Vector space definitions|vector space]] defined over complex numbers with an [[Inner product spaces#Complex inner products|inner product]]. Kets are quantum states represented as vectors in a Hilbert space. Taking $\psi$ to represent the roll of a die, $\vert\psi\rangle=c_1\vert1\rangle+\dots+c_6\vert6\rangle$ is a vector in a $6$-dimensional Hilbert space. A state is defined by a vector in Hilbert space. Axioms:
> A null vector $\vert⊘\rangle$ represents $\vert\psi\rangle=0$
> Additivity:$$\Huge\begin{align}
\vert V\rangle+\vert W\rangle&=\vert W\rangle+\vert V\rangle\\
\vert V\rangle+\vert⊘\rangle&=\vert V\rangle\\
-\vert V\rangle+\vert V\rangle&=\vert⊘\rangle\\
(\vert V\rangle+\vert W\rangle)+\vert Z\rangle&=\vert V\rangle+(\vert W\rangle+\vert Z\rangle)
\end{align}$$Inner product $(\vert V\rangle,\vert W\rangle)=\langle V\vert W\rangle$
   Multiplicativity:$$\Huge\begin{align}
0\vert V\rangle&=\vert⊘\rangle\\
1\vert V\rangle&=\vert V\rangle\\
cd\vert V\rangle&=dc\vert V\rangle
\end{align}$$

Some properties of the inner product are as follows:
> $\langle W\vert V\rangle^*=\langle V\vert W\rangle$ anti Hermitian
> $\langle V\vert V\rangle\geq0$ non negative norms
> $\langle V\vert V\rangle=0\implies\vert V\rangle=\vert⊘\rangle$
> $\vert X\rangle=a\vert W\rangle+b\vert Z\rangle\implies\langle V\vert X\rangle=a\langle V\vert W\rangle+b\langle V\vert Z\rangle$ and $\langle X\vert V\rangle=a^*\langle W\vert V\rangle+b^*\langle Z\vert V\rangle$

Initially, our state $\vert \psi\rangle$ is in superposition, $\vert \psi\rangle=c_1\vert 1\rangle+c_2\vert 2\rangle+\dots$, and say we measure $\vert \psi\rangle\rightarrow\vert 1\rangle$ with probability $|c_1|^2$. Once measured, $\vert \psi\rangle=\vert 1\rangle$, and subsequent measurements will always yield $\vert \psi\rangle\rightarrow\vert 1\rangle$ with probability $|1|^2=1$. 

Taking adjoints defines a dual Hilbert space $\mathcal{H}^*$ with $\dim\mathcal{H}^*=\dim\mathcal{H}$:$$\Huge \vert \psi\rangle=\sum_{i=1}^nc_i\vert i\rangle\implies\langle \psi\vert=\sum_{i=1}^nc_i^*\langle i\vert$$A physical state $\vert \psi\rangle$ has $\langle \psi\vert \psi\rangle=1$.

# Orthonormal basis expansion:

We can expand the state $\vert \psi\rangle=\sum_{i=1}^nc_i\vert i\rangle$ with $\langle i\vert i\rangle=1$ and $\langle i\vert j\rangle=\delta_{ij}$, where $\vert i\rangle,\vert j\rangle$ represent orthonormal basis vectors. We can recover the $c_i$ coefficients from the state using the following method:$$\Huge \langle j\vert \psi\rangle=\sum_{i=1}^nc_i\langle j\vert i\rangle=\sum_{i=1}^nc_i\delta_{ij}=c_j$$We can also take the inner product of $\vert \psi\rangle$ with $\vert⊘\rangle=\sum_{i=1}^nd_i\vert i\rangle$:$$\Huge\begin{align}
\langle⊘\vert \psi\rangle&=\left(\sum_{i=1}^nd_i^*\langle i\vert\right)\left(\sum_{j=1}^nc_j\vert j\rangle\right)\\
&=\sum_{i=1}^n\sum_{j=1}^n\langle i\vert j\rangle d_i^*
c_j\\
&=\sum_{i=1}^n\sum_{j=1}^n\delta_{ij}d_i^*c_j=\sum_{i=1}^nd_i^*c_i
\end{align}$$Therefore it makes sense to think of states as column vectors and adjoints as row vectors, as this behaves similarly to the vector [[Inner product spaces#Complex inner products|inner product]]. Consider that we can write a state as:$$\Huge \vert \psi\rangle=\sum_{i=1}^nc_i\vert i\rangle=\sum_{i=1}^n\langle i\vert \psi\rangle\vert i\rangle=\left(\sum_{i=1}^n\vert i\rangle\langle i\vert\right)\vert \psi\rangle=\hat{\mathbb{I}}\vert \psi\rangle$$Where we have defined:$$\Huge \hat{\mathbb{I}}=\sum_{i=1}^n\vert i\rangle\langle i\vert$$as the identity. A basis is considered complete if the sum over all $\vert i\rangle$ is the identity. For example, we have in $\Re^2$ $\vert 1\rangle=\begin{pmatrix}1\\0\end{pmatrix},\vert 2\rangle=\begin{pmatrix}0\\1\end{pmatrix}$, then:$$\Huge\ \hat{\mathbb{I}}=\vert 1\rangle\langle 1\vert+\vert 2\rangle\langle 2\vert=\begin{pmatrix}1\\0\end{pmatrix}\begin{pmatrix}1 & 0\end{pmatrix}+\begin{pmatrix}0\\1\end{pmatrix}\begin{pmatrix}0 & 1\end{pmatrix}= \hat{\mathbb{I}}$$Formally, we write this as the "outer product":$$\Huge (\underline u\otimes\underline v^*)_{ij}=u_iv_j^*$$All of these notions carry through to the continuous case:$$\Huge \vert \psi\rangle=\int_{-\infty}^\infty\vert x\rangle\langle x\vert \psi\rangle dx,\,\, \hat{\mathbb{I}}=\int_{-\infty}^\infty\vert x\rangle\langle x\vert dx$$
Recalling the previous example, we can consider the calculation in another orthonormal basis:$$\Huge\begin{align}
\vert 1'\rangle&=\frac{1}{\sqrt 2}\begin{pmatrix}1\\1\end{pmatrix},\,\,\vert 2'\rangle=\frac{1}{\sqrt 2}\begin{pmatrix}1\\-1\end{pmatrix}\\
\vert 1'\rangle\langle 1'\vert+\vert 2'\rangle\langle 2'\vert&=\frac{1}{2}\begin{pmatrix}1 & 1\\1 & 1\end{pmatrix}+\frac{1}{2}\begin{pmatrix}1 & -1\\1 & 1\end{pmatrix}= \hat{\mathbb{I}}
\end{align}$$
# Linear operators:

An operator maps states in the Hilbert space to other states in the same space, $\hat\Omega:\mathcal{H}\rightarrow\mathcal{H}$. In general, operators are written as matrices. For example, consider the mapping:$$\Huge \hat\Omega\vert i\rangle=\vert i'\rangle=\sum_{j=1}^n\Omega_{ji}\vert j\rangle$$
Acting with $\langle k\vert$ gives:$$\Huge \langle k\vert\hat\Omega\vert i\rangle=\sum_{j=1}^n\Omega_{ji}\langle k\vert j\rangle=\sum_{j=1}^n\Omega_{ji}\delta_{kj}=\Omega_{ki}$$