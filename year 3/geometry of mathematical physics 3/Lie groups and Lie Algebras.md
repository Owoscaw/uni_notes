
# Motivating examples:

## $U(1)$:
The group $U(1)$ derives its name from unitary complex $1\times1$ matrices. Acting with $g$ on a complex number $c$ we define a map:$$\Huge z\rightarrow gz,\,\,g\in U(1),\,\,z\in\mathbb{C}$$where we require that the inner form $|z|^2$ remains unchanged as:$$\Huge |z|^2=\bar zz\rightarrow\bar z\bar ggz=|g|^2|z|^2$$which implies that $g$ is a complex number of modulus one ($|g|^2=1$), therefore we can write $g=e^{i\varphi}$. Hence $U(1)$ is the group of complex numbers of unit modulus with multiplication as the group operation. We can prove this using the definition of a group. $g=1$ acts as the identity element for this group. The product of two complex numbers with unit modulus also has unit modulus, so we satisfy $x,y\in G\implies x\circ y\in G$. Complex numbers are associative under multiplication, so we satisfy associativity automatically. For $g=e^{i\varphi}$ we write $g^{-1}=e^{-i\varphi}$ and we see that $g\circ g^{-1}=e^{i\varphi}e^{-i\varphi}=e^0=1$, satisfying the inverse requirement for a group. Hence $U(1)$ is indeed a group under multiplication. We saw that a map from $\Re$ to $U(1)$ by writing $g=e^{i\varphi}$ is not an isomorphism. That is, we cannot simply do calculus on $\Re$ and map that to $U(1)$, this is an example of a manifold. When $\varphi\to0$ we can approximate the exponential map to linear order to get:$$\Huge z\rightarrow(1+i\varphi)z$$Note that this approximation is tangent to $U(1)$ at $g=1$. We can try to reconstruct finite elements of $U(1)$ by repeated infinitesimal transformations. Considering $(1+i\varphi/n)^n$ as our map, we see that as $n\to\infty$ the map is reconstructed. More formally:$$\Huge\begin{align}
\lim_{n\to\infty}(1+i\varphi/n)^n&=\lim_{n\to\infty}\sum_{k=0}^n\frac{(i\varphi)^k}{n^k}{n\choose k}\\
&=\lim_{n\to\infty}\sum_{k=0}^n\frac{(i\varphi)^k}{n^k}\frac{n!}{(n-k)!k!}\\
&=\lim_{n\to\infty}\sum_{k=0}^n\frac{(i\varphi)^k}{k!}=e^{i\varphi}
\end{align}$$where we have used the fact that the term $\frac{n!}{(n-k)!n^k}$ will tend to one in the limiting case.

## $SU(2)$
We now aim to generalise the above notions to matrices, particularly $M_n(\mathbb{C})$. To do this we must recall [[Index notation|Einstein's summation notation]] as well as the Hermitian conjugate $(A^\dagger)_{ij}=(\bar A)_{ji}$.  We can write the trace and determinant of a matrix using index notation:$$\Huge\begin{align}
\det A&=\epsilon_{i_1i_2,\dots,i_n}A_{1i_1}A_{2i_2}\dots A_{ni_n}\\
\text{Tr }A&=A_{ii}
\end{align}$$where $\epsilon$ is the Levi-Civita symbol, a completely antisymmetric tensor. We can then define the general unitary groups:$$\Huge\begin{align}
U(n)&=\{g\in M_n(\mathbb{C}):g^\dagger g=gg^\dagger=\mathbb{1}\}\\
SU(n)&=\{g\in U(n):\det g=1\}
\end{align}$$Focusing on $SU(2)$ we can check if this is indeed a group wrt matrix multiplication:$$\Huge\begin{align}
e&=\mathbb{1}\implies g\mathbb{1}=\mathbb{1}g=g,\,\,\forall g\in SU(2)\\
\mathbb{1}\mathbb{1}^\dagger&=\mathbb{1}^\dagger\mathbb{1}=\mathbb{1}\implies e\in\ SU(2)\\
g,g'\in SU(2)&\implies(gg')^\dagger gg'=g'^\dagger g^\dagger gg'=g'^\dagger\mathbb{1}g'=\mathbb{1}\\
\det(gg')&=\det g\deg g'=1\times1=1\\
g\in SU(2)&\implies (g^{-1})^\dagger g^{-1}=(g^\dagger)^\dagger g^{-1}=gg^{-1}=1\\
\det(g^{-1})&=\frac{1}{\det g}=1
\end{align}$$And as matrix multiplication is associative, we have that $SU(2)$ is indeed a group. Note that we can think of $U(2)$ as the group of transformations $U$ on $\mathbb{C}^2$, $\underline z\rightarrow U\underline z=\underline w$, which will leave the inner product $|\underline z|$ invariant:$$\Huge |\underline z|=\begin{pmatrix}\bar z_1&\bar z_2\end{pmatrix}\mathbb{1}\begin{pmatrix}z_1\\z_2\end{pmatrix}=\underline z^\dagger\cdot\underline z$$so when we apply the transformation:$$\Huge \begin{align}
\underline z&\rightarrow U\underline z\\
\underline z^\dagger&\rightarrow(U\underline z)^\dagger=\underline z^\dagger U^\dagger\\
\underline z^\dagger\underline z&\rightarrow \underline z^\dagger U^\dagger U\underline z=\underline z^\dagger\underline z
\end{align}$$so we see that the inner product is indeed unchanged. We can also take the notion of parametrisation we saw in $U(1)$ to $U(2)$. 

For any invertible matrix in $M_2(\mathbb{C})$ we can write:$$\Huge g=\begin{pmatrix}a & b \\ c & d\end{pmatrix}\implies g^{-1}=\frac{1}{\det g}\begin{pmatrix}d & -b \\ -c & a\end{pmatrix}$$Now as $g\in SU(2)$ we have $\det g=1$ and $g^{-1}=g^\dagger$, so:$$\Huge \begin{pmatrix}d & -b \\ -c & a\end{pmatrix}=\begin{pmatrix}\bar a & \bar c \\ \bar b & \bar d\end{pmatrix}$$So the most general matrix in $SU(2)$ can be written as:$$\Huge g=\begin{pmatrix}a & b \\ -\bar b & \bar  a\end{pmatrix}$$now $\det g=1\implies|a|^2+|b|^2=1$. As these are complex numbers, we write $a=x_1+ix_2,b=x_3+ix_4$, so we have:$$\Huge SU(2)=\{\underline{x}\in\Re^4:x_1^2+x_2^2+x_3^2+x_4^2=1\}$$This is the defining equation of the three sphere. That is, $SU(2)$ is a space that looks like a three sphere $S^3$ and we have defined an embedding of $S^3$ into $\Re^4$.

When working with $U(1)$ we saw that we could write the group using the complex exponential. We aim to introduce a similar notion by writing:$$\Huge g=e^{iA}$$where $A$ is a matrix and $g\in SU(2)$. The exponential of a matrix has to be defined using the series definition:$$\Huge e^{iA}=\sum_{}^{#tab}$$