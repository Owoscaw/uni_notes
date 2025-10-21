
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
Acting with $\langle k\vert$ gives:$$\Huge \langle k\vert\hat\Omega\vert i\rangle=\sum_{j=1}^n\Omega_{ji}\langle k\vert j\rangle=\sum_{j=1}^n\Omega_{ji}\delta_{kj}=\Omega_{ki}$$which we can check using the completeness relation that we defined:$$\Huge \sum_j\Omega_{ji}|j\rangle=\sum_j|j\rangle \langle j|\hat \Omega |i\rangle=\hat{\mathbb{I}}\hat\Omega |j\rangle=\hat\Omega|j\rangle$$recovering the original mapping. Hence we obtain the results:$$\Huge\begin{align*}
\Omega_{ij}&=\langle i|\hat\Omega |j\rangle\\
\hat\Omega&=\sum_{ij}\Omega_{ij} |i\rangle \langle j|
\end{align*}$$we can observe the result of this operator on the "coordinates" of a state vector $|\psi\rangle$. For any $|\psi\rangle\in\mathcal{H}$ we have:$$\Huge\hat\Omega |\psi\rangle=\sum_{i,j=1}^n\Omega_{ji}c_i |j\rangle$$Therefore we can consider the operator as rotating the basis vectors, or use the same basis but absorb the action of $\hat\Omega$ into a change in the $c_i$ coefficients:$$\Huge \hat\Omega |\psi\rangle=\sum_jc'_j |j\rangle=\sum_ic_i |i\rangle'$$where:$$\Huge |i\rangle'=\sum_j\Omega_{ji} |j\rangle,\,\,c_j'=\sum_i\Omega_{ji}c_i=\begin{pmatrix}\Omega_{11}&\dots & \Omega_{1n} \\ \vdots & \ddots & \vdots \\ \Omega_{n1} & \dots & \Omega_{nn}\end{pmatrix}\begin{pmatrix}c_1 \\ \vdots \\ c_n\end{pmatrix}$$Note that Dirac notation makes this manipulation easy as factors of $\hat{\mathbb{I}}=\sum_j |j\rangle \langle k|$ can be inserted. Recalling that $c_i=\langle i|\psi\rangle$ and that $c_i'=\langle i|\hat\Omega |\psi\rangle$ are the coefficients of the new state $|\psi'\rangle=\hat\Omega |\psi\rangle$ we have:$$\Huge c_i'=\langle i|\hat\Omega |\psi\rangle=\sum_j\langle i|\hat\Omega |j\rangle \langle j|\psi\rangle=\sum_j\Omega_{ij}c_j$$

For example, consider a pair of quantum coin states $|H\rangle,|T\rangle$, represented as vectors:$$\Huge |H\rangle=\begin{pmatrix}1 \\ 0\end{pmatrix},\,\, |T\rangle=\begin{pmatrix}0 \\ 1\end{pmatrix}$$We then define a quantum operator, called the Hadamard operator $\hat H$:$$\Huge\hat H=\frac{1}{\sqrt 2}\begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$$and observe how it acts on our states:$$\Huge\begin{align*}
\hat H |H\rangle&=\frac{1}{\sqrt 2}\begin{pmatrix}1 & 1\\
1 & -1\end{pmatrix}\begin{pmatrix}1\\
0\end{pmatrix}=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\
1\end{pmatrix}=\frac{1}{\sqrt 2}(|H\rangle+|T\rangle)\\
\hat H |T\rangle&=\frac{1}{\sqrt 2}\begin{pmatrix}1 & 1\\
1 & -1\end{pmatrix}\begin{pmatrix}0\\
1\end{pmatrix}=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\
-1\end{pmatrix}=\frac{1}{\sqrt 2}(|H\rangle-|T\rangle)
\end{align*}$$The operator has created superpositions of the quantum states. The following are operators commonly used in quantum computing:
> Pauli Gates, defined using the [[Lie groups and Lie Algebras#Pauli matrices|Pauli matrices]]. These come in $3$ flavours, the Pauli-X Gate $(\hat\tau_1)$, the Pauli-Y Gate $(\hat\tau_2)$, and (you guessed it!) the Pauli-Z Gate $(\hat\tau_3)$:$$\Huge \tau_1=\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix},\,\,\tau_2=\begin{pmatrix}0 & -i \\ i & 0\end{pmatrix},\,\,\tau_3=\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$$
> Phase Shift Gates, defined using complex exponentials. The Phase Gate $(\hat S)$ represents a $\pi/2$ phase shift, and the T Gate $(\hat T)$ represents a $\pi/4$ phase shift:$$\Huge S=\begin{align*}
\begin{pmatrix}1 & 0\\
0 & i\end{pmatrix},\,\,T=\begin{pmatrix}1 & 0\\
0 & e^{i\pi/4}\end{pmatrix}
\end{align*}$$
>Rotation Gates, representing rotations around each axis:$$ R_x(\theta)=\begin{pmatrix}\cos(\frac{\theta}{2}) & -i\sin(\frac{\theta}{2}) \\ -i\sin(\frac{\theta}{2}) & \cos(\frac{\theta}{2})\end{pmatrix},\,\,R_y(\theta)=\begin{pmatrix}\cos(\frac{\theta}{2}) & -\sin(\frac{\theta}{2}) \\ \sin(\frac{\theta}{2}) & \cos(\frac{\theta}{2})\end{pmatrix},\,\,R_z(\theta)=\begin{pmatrix}e^{-i\pi/2} & 0 \\ 0 & e^{i\pi/2}\end{pmatrix}$$


Consider the operator $\hat R$, representing an actual rotation in three dimensional space, namely a counterclockwise rotation by $\pi/2$ about $|3\rangle$ on $\mathcal{H}$ such that $|1\rangle,|2\rangle,|3\rangle$ represent the $x,y,z$ axis respectively. First we determine the action $\hat R$ on each basis vector:$$\Huge\begin{align*}
\hat R |1\rangle=|2\rangle,\,\,\hat R |2\rangle&=-|1\rangle,\,\,\hat R |3\rangle=|3\rangle\\
\implies\hat R |\psi\rangle&=c_1 |2\rangle-c_2 |1\rangle+c_3 |3\rangle
\end{align*}$$![[QM linear algebra 2025-10-21 05.52.45.excalidraw]]Using this information, we can reconstruct the matrix form of $\hat R$:$$\large\begin{align*}
\langle i|\hat R |j\rangle&=R_{ij}\\
R_{11}=\langle 1|\hat R |1\rangle=0,\,\,R_{21}=\langle 2|\hat R |1\rangle=1,\,\,&R_{12}=\langle 1|\hat R |2\rangle=-1,\,\,R_{33}=\langle 3|\hat R |3\rangle=1\\
\implies R_{ij}&=\begin{pmatrix}0 & -1 & 0\\
1 & 0 & 0\\
0 & 0 & 1\end{pmatrix}
\end{align*}$$It follows that the inverse of this operator $\hat R^{-1}$ would undo any action done by $\hat R$, leading to the definition:

The inverse $\hat R^{-1}$ of an operator $\hat R$ obeys:$$\Huge \hat R^{-1}\hat R=\hat R\hat R^{-1}=\hat{\mathbb{I}}$$Inserting factors of $\hat{\mathbb{I}}$ allows us to observe the properties of $\hat R^{-1}$'s matrix:$$\Huge\begin{align*}
\mathbb{I}_{ij}=\langle i|\mathbb{I} |j\rangle=\langle i|j\rangle=\delta_{ij}&=\langle i|\hat R^{-1}\hat R |j\rangle\\
&=\sum_k \langle i|\hat R |k\rangle \langle k|\hat R |j\rangle\\
&=\sum_k(R^{-1})_{ik}R_{kj}
\end{align*}$$It is clear that the operator has an inverse if and only if its defining matrix has an inverse. 

We can operate in a different manner using the fact that for any $|i\rangle,|j\rangle\in\mathcal{H}$ we can define a linear operator as a sum of ket-bra products $\hat O=O_{ij} |i\rangle \langle j|$. That is, $\hat R$ could be written as $\hat R=-|1\rangle \langle 2|+|2\rangle \langle 1|+|3\rangle \langle 3|$

# Adjoints:

Adjoints are the complex conjugates so that $\langle \psi'|=\sum_i=(c_i') \langle i|$ and so we can find the coefficients of the adjoint after action become:$$\Huge(c_i')^*=\sum_j\Omega_{ij}^*c_j^*=\sum_jc_j^*(\Omega^\dagger)_{ji}$$where $\Omega^\dagger$ is the complex conjugate of the transpose of $\Omega$, that is:$$\Huge (c_i')^*=\sum_j \langle \psi|j\rangle \langle j|\hat\Omega^\dagger |i\rangle$$where we require that the adjoint $\hat\Omega^\dagger$ of the operator $\hat\Omega$ obeys:$$\Huge \langle V_1|\hat\Omega^\dagger |V_2\rangle=\langle V_2|\hat\Omega |V_1\rangle^*,\,\,\forall V_1,V_2\in\mathcal{H}$$and hance in matrix form as an operator expansion:$$\Huge\hat\Omega^\dagger=\sum_{ij}(\Omega^\dagger)_{ij} |i\rangle \langle j|$$
By linearity of both $\mathcal{H},\mathcal{H}^*$ if $\hat A=c_1\hat B+c_2\hat C$ then $\hat A^\dagger=c_1^*\hat B^\dagger+c_2^*\hat C^\dagger$. It can be shown that $\hat\Omega^\dagger$ is the complex conjugate of the transpose matrix of $\hat\Omega$ as:$$\Huge(\Omega^\dagger)_{ij}= \langle i|\hat\Omega^\dagger |j\rangle=\langle j|\hat\Omega |i\rangle^*=\Omega_{ji}^*$$Therefore if $|\psi'\rangle=\hat A\hat B\hat C |\psi\rangle$ then:$$\Huge (c_i')^*=\sum_jc_j^*(C^\dagger\cdot B^\dagger\cdot A^\dagger)_{ji}$$we can then translate this into Dirac notation:$$\Huge\begin{align*}
(c_i')^*&=\sum_{j,k,l}\langle \psi|j\rangle \langle j|\hat C^\dagger |k\rangle \langle k|\hat B^\dagger |l\rangle \langle l|\hat A^\dagger |i\rangle\\
&=\langle \psi|\hat{\mathbb{I}}\hat C^\dagger\hat{\mathbb{I}}\hat B^\dagger\hat{\mathbb{I}}\hat A^\dagger |i\rangle\\
&=\langle \psi|\hat C^\dagger\hat B^\dagger\hat A^\dagger |i\rangle
\end{align*}$$That is to say if $|\psi'\rangle=\hat A\hat B\hat C |\psi\rangle$ then:$$\Huge \langle \psi'|=\langle \psi|\hat C^\dagger\hat B^\dagger\hat A^\dagger$$