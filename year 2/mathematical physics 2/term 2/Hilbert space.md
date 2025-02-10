
Consider a finite dimensional complex [[Vector space definitions|vector space]] $V\cong\mathbb{C}^N$. We choose an orthonormal basis $\{ \underline e_j\}$ such that $\langle e_i,e_j\rangle$, where $\langle \cdot,\cdot\rangle$ represents the [[Inner product spaces#Complex inner products|Hermitian inner product]]. This allows any vector to be expressed as:$$\Huge \underline v=\sum_{j=0}^N v_j\underline e_j$$The Hermitian inner product can then be expressed as:$$\Huge \langle \underline v,\underline w\rangle=\sum_{j=0}^N\overline v_jw_j$$The square norm of a vector is then given by $|\underline v|^2=\langle \underline v,\underline v\rangle$. Solutions to [[Schrodinger's equation]] obey the principle of superposition, so can be thought of as members of an infinite dimensional vector space with inner product:$$\Huge \langle \psi_1,\psi_2\rangle=\int_{-\infty}^\infty\psi_1^*(x,t)\psi_2(x,t)dx$$One can show that this obeys the definition of the complex inner product. We aim to decompose  a solution $\psi$ to the equation onto some basis. We assume that the solutions can be counted, that is $\psi_n(x,t)$ form the basis and any solution is written as:$$\Huge\psi(x,t)=\sum_{n=0}^\infty c_n\psi_n(x,t)$$[[Fourier Series#Parseval's Theorem|Parseval's theorem]] then states that:$$\Huge \langle \psi,\psi\rangle=\sum_{n=0}^\infty|c_n|^2$$
## Example: particle in a box:
Take the boundary condition $\psi(x=0)=\psi(x=l)=0$ with the solution:$$\Huge\phi_n(x)=\sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$$Which obeys $\langle \phi_n,\phi_m\rangle=\delta_{nm}$. The solution is then given by:$$\Huge\psi(x)=\sum_{n=0}^\infty c_n\phi_n(x)=\sum_{n=0}^\infty c_n\sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$$The coefficients $c_n$ are then found by taking the Hermitian inner product with $\phi_n(x)$:$$\Huge c_n=\langle \phi_n,\psi\rangle=\sqrt{\frac{2}{L}}\int_0^L\sin\left(\frac{n\pi x}{L}\right)dx$$

# Hermitian operators:

The notion of [[Inner product spaces#Complex inner products|Hermitian operators]] can be applied to Hilbert space. The regular properties hold, however since the Hilbert space is infinite dimensional, an operator need not act on the whole of Hilbert space and the domain of an operator $A$ need not be the domain of $A^\dagger$, the adjoint operator.

Note that the [[Momentum and Planck's constant#Momentum|momentum, position, and energy]] operators are all Hermitian, that is:$$\Huge \langle v_1,Av_2\rangle=\langle Av_1,v_2\rangle$$for $A=\hat x,\hat p,\hat H$. The action of applying an operator is akin to multiplying by a matrix, in fact matrix element can be calculated using:$$\Huge A_{mn}=\langle \phi_m,A\phi_n\rangle=\int\overline{\phi_m(x)}(A\phi_n(x))dx$$

Taking the particle in a box for example, we have:$$\Huge \phi_n(x)=\sqrt\frac{2}{L}\sin\left(\frac{n\pi x}{L}\right)\,\,\forall n\in\mathbb{Z}_{\geq0}$$Then we can compute elements of the position operator:$$\Huge\begin{align}
x_{mn}&=\langle \phi_m,\hat x\cdot\phi_n\rangle\\
&=\int_0^Lx\overline{\phi_m(x)}\phi_n(x)dx\\
&=\frac{2}{L}\int_0^Lx\sin\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)dx\\
&=\frac{1}{L}\int_0^Lx\left[\cos\left(\frac{(m-n)\pi x}{L}\right)-\cos\left(\frac{(m+n)\pi x}{L}\right)\right]
\end{align}$$We introduce $y=\pi x/L$ and use $\int_0^\pi y\cos(ny)dy=\frac{(-1)^n-1}{n^2}$ to get:$$\Huge x_{mn}=\begin{cases}\frac{L}{2}&m=n\\\frac{4L}{\pi^2}\frac{mn}{(m^2-n^2)^2}((-1)^{m+n}-1)&m\neq n\end{cases}$$Which is a [[Inner product spaces#Complex inner products|Hermitian matrix]]. One can also derive expressions for $\hat p$ and $\hat H$.

# Spectrum of Hermitian operators:

For a Hermitian operator $A$ that is an eigenstate ($A\psi_a(x)=a\psi_a(x)$) we observe that the expectation is:$$\Huge \langle A\rangle_{\psi_a}=\int\overline{\psi_a(x)}A\psi_a(x)=a\int P(x)dx=a$$

We propose that eigenvalues of a Hermitian operator are real, and that distinct eigenvalues correspond to orthogonal eigenfunctions. 

## Discrete spectra:
When a wave function is not an eigenfunction of some operator, it can be decomposed into a linear combination of basis eigenfunctions. We have:$$\Huge\begin{align}
\langle \phi_m,\phi_n\rangle&=\delta_{mn}\\
\psi(x)&=\sum_nc_n\phi_n(x)\\
\langle \phi_m,\psi\rangle&=\sum_nc_n \langle \phi_m,\phi_n\rangle=c_m\\
\langle \psi,\psi\rangle&=\sum_{m,n}\overline{c_m}c_n \langle \phi_m,\phi_n\rangle=\sum_n|c_n|^2=1 
\end{align}$$
Returning to the particle in a box example we have that the basis is formed by $\phi_n$ as before and:$$\Huge\hat H=\frac{\hat p^2}{2m}=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}$$We then see that:$$\Huge \hat H\phi_n(x)=E_n\phi_n(x)=\frac{\hbar^2}{2m}\left(\frac{n\pi}{L}\right)^2\phi_n(x)$$So we see that there is a discrete spectrum of eigenfunctions for this operator. Here, $|c_n|^2$ is the probability that the measurement of energy is given by $E_n$.

## Continuous spectra:
We have the similar equations to the discrete case given as follows:$$\large\begin{align}
\langle \phi_a,\phi_{a'}\rangle&=\delta(a-a')\\
\psi(x)&=\int_\Re c(a)\phi_a(x)da\\
\langle \phi_a,\psi\rangle=\int_\Re c(a')\langle \phi_a,\phi_{a'}\rangle da'&=\int_\Re c(a')\delta(a-a')da'=c(a)\\
\langle \psi,\psi\rangle=\int_\Re \overline{c(a)}c(a')\langle \phi_a,\phi_{a'}\rangle da\,da'&=\int_\Re\overline{c(a)}c(a')\delta(a-a')da\,da'=\int_\Re|c(a)|^2da=1
\end{align}$$where $\delta$ represents the [[Partial differential equations#Elliptic PDEs|dirac delta]] function.