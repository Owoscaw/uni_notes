
Suppose that we have two [[Partial differential equations#Linearity operator|linear operators]] $A,B$. The commutator is then defined as:$$\Huge [A,B]:=AB-BA$$which has the following properties:
> $[A,B]=-[B,A]$
> $[\alpha_1A_1+\alpha_2A_2,B]=\alpha_1[A_1,B]+\alpha_2[A_2,B]$
> $[A,BC]=B[A,C]+[A,B]C$
> $[A[B,C]]+[B,[C,A]]+[C,[A,B]]$

The commutator plays an important role in quantum mechanics due to the theorem:

Two commuting matrices are simultaneously diagonalisable. That is, if $A,B$ are [[Hilbert space#Hermitian operators|Hermitian operators]] with $[A,B]=0$, it is possible to find an [[Norms and orthogonality#Orthonormal basis|orthonormal basis]] of [[Wave function|wave functions]] that are simultaneous [[Eigenvalues, Eigenvectors, and Diagonalisation|eigenfunctions]] of $A$ and $B$.

To prove this, we assume that the spectrum of eigenvalues $\{a_j\}$ of $A$ is [[Hilbert space#Discrete spectra|discrete]] and non-degenerate. That is, there is a unique solution to $A\phi_j(x)=a_j\phi_j(x)$ for each eigenvalue $a_j$ (up to normalisation). Such normalisation can be chosen to make the basis orthonormal, $\langle \phi_i,\phi_j\rangle=\delta_{ij}$. We have:$$\Huge AB=BA\implies A(B\phi_j)=B(A\phi_j)=B(a_j\phi_j)=a_j(B\phi_j)$$so $B\phi_j$ is also an eigenfunction of $A$ with eigenvalue $a_j$. However such wave function is unique up to normalisation, so we have:$$\Huge B\phi_j(x)=b_j\phi_j(x)$$for some $b_j\in\Re$. Therefore $\phi_j(x)$ is simultaneously an eigenfunction of $B$, as required. This is useful since:![[eigenstates]]we see that the system is collapsed to an eigenstate of both $A,B$. If $[A,B]\neq0$ one would need to decompose $\phi_j^A$ onto an eigenbasis $\phi_k^B$ before finding an eigenvalue corresponding to $\phi_k^B$. 

Suppose that we measure $A$ and find the eigenvalue $a_j$, then the wave function immediately after measurement is $\phi_j(x)$:
> If $A$ is measured next then $a_j$ will again be found since $\phi_j(x)$ is an eigenfunction of $A$. We see that the uncertainty of a normalised eigenfunction vanishes:$$\Huge\begin{align}
(\Delta A)^2&=\langle A^2\rangle-\langle A\rangle^2\\
&=\langle \phi_j,A^2\phi_j\rangle-\langle \phi_jA,\phi_j\rangle^2\\
&=a_j^2 \langle \phi_j,\phi_j\rangle-(a_j \langle \phi_j,\phi_j\rangle)^2\\
&=a_j^2-a_j^2=0
\end{align}$$so the probability of finding this eigenvalue is indeed $1$.
> If $B$ is measured next, then:
> > If $[A,B]=0$ we have that $\phi_j(x)$ is also an eigenfunction of $B$ with eigenvalue $b_j$. Therefore a measurement of $B$ will find $b_j$ with probability $1$ and we get $\Delta B=0$. That is, we can simultaneously determine the value of $A$ and $B$.
> > If $[A,B]\neq0$ then $\phi_j(x)$ is not an eigenfunction of $B$. Suppose that the measurement yields an eigenvalue $b$. Then the wave function jumps to the corresponding eigenfunction of $B$ with $\Delta B=0$, however now we have changed the function, which makes $\Delta A>0$.

Note that measurements are made simultaneously, as general eigenstates do not remain eigenstates under time evolution. Only eigenstates of the [[Hamiltonian Formalism#Hamiltonian flows|Hamiltonian operator]] remain eigenstates over time.

# General Uncertainty Principle:

If $[A,B]\neq0$ we cannot find simultaneous eigenfunctions of $A,B$ with both $\Delta A=\Delta B=0$. There is a fundamental limit in quantum mechanics that determines how small the product of uncertainties is, known as the generalised uncertainty principle, which states:$$\Huge \Delta A\Delta B\geq\frac{1}{2}|\langle [A,B]\rangle|$$
To prove this, we assume that $\langle A\rangle=\langle B\rangle=0$. With this, uncertainty in $A$ is expressed as:$$\Huge (\Delta A)^2=\langle A^2\rangle=\langle \psi,A^2\psi\rangle=\langle A\psi,A\psi\rangle=\langle \psi_A,\psi_A\rangle$$where $\psi_a=A\psi$. Using a similar statement for $B$ we write:$$\Huge (\Delta A)^2(\Delta B)^2=\langle \psi_A,\psi_A\rangle \langle \psi_B,\psi_B\rangle$$Now using the [[Norms and orthogonality#Complex Cauchy-Schwarz inequality|Cauchy-Schwarz]] inequality we have:$$\Huge \langle \psi_A,\psi_A\rangle \langle \psi_B,\psi_B\rangle\geq|\langle \psi_A,\psi_B\rangle|^2$$which holds for any Hermitian inner product. We now write:$$\Huge \begin{align}
\langle \psi_A,\psi_B\rangle&=\langle AB\rangle\\
&=\frac{1}{2}\langle AB-BA\rangle+\frac{1}{2}\langle AB+BA\rangle\\
&=\frac{1}{2}\langle [A,B]\rangle+\frac{1}{2}\langle \{A,B\}\rangle
\end{align}$$where $\{A,B\}$ is the anti-commutator. One can show that $[A,B]$ being anti-Hermitian implies that $\langle [A,B]\rangle\in i\Re$ and $\{A,B\}$ being Hermitian implies that $\langle \{A,B\}\rangle\in R$. Therefore the commutator and anti-commutator provide the real and imaginary parts of $\langle \psi_A,\psi_B\rangle$ respectively. We can therefore take the modulus squared:$$\Huge\begin{align}
|\langle \psi_A,\psi_B\rangle|&=\frac{1}{4}|\langle [A,B]\rangle|^2+\frac{1}{2}|\langle \{A,B\}\rangle|^2\\
&\geq\frac{1}{4}|\langle [A,B]\rangle|^2
\end{align}$$so we have the proof as required.

Note that for position and momentum operators, we get [[Uncertainty Principles|Heisenburg's uncertainty principle]].