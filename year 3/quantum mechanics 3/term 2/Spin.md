
In classical theory, any object admits two kinds of motion; orbital, and spinning. These correspond to the notion of center of mass and rotation around an axis:![[Spin 2026-02-02 19.52.26.excalidraw]]
In quantum theory, quantum particles have no "size", but a notion of internal angular momentum (spin).  describes the spinning of a particle in some internal mathematical space, and hence parts of a wave function $f_n$ describing spin will not be in the [[QM in R3#Eigenfunctions of angular momentum|$(r,\theta,\varphi)$]] space but some internal space.

Algebraically, theory of spin is identical to the theory of [[QM in R3#Quantum angular momentum|angular momentum]] $\hat L_i$, with replacement of [[Representations#$SO(3),SU(2)$, and spin|spin]]$$\Huge \hat L_i\rightarrow \hat S_i$$defining the spin operators. We also have$$\Huge\begin{align*}
[\hat S_i,\hat S_j]&=i\epsilon_{ijk}\hat S_k\\
[\hat S^2,\hat S_i]&=0
\end{align*}$$and other results applicable to angular momentum. Our eigenstates then become$$\Huge |l,m\rangle\rightarrow |S,S_z\rangle,\,\,S_z\in\{-S,\dots,S\}$$, as expected. We also get some extra relations between spin and the other operators:$$\Huge [\hat S_i,\hat L_j]=0,\,\,[\hat S_i,\hat x_j]=0,\,\,[\hat S_i,\hat p_j]=0$$
The wave function for a particle with a given spin $S$ then obeys$$\Huge\Psi(x,y,z;S,S_z)=\psi(x,y,z)|S,S_z\rangle$$where $\psi(x,y,z)$ is the standard wave function describing the propagation of a particle in $\Re^3$ and $|S,S_z\rangle$ is the eigenstate describing spin in the internal space. Note that the wave function $\Psi$ does not stay invariant under a $2\pi$ rotation:$$\Huge\Psi(r,\theta,\varphi+2\pi;S,S_z)=\pm\Psi(r,\theta,\varphi;S,S_z)$$where the equation takes the positive route for bosons, and negative for fermions. It turns out:
> $S=n$ implies $\Psi$ does not change sign, so $\Psi$ describes a bosonic particle
> $S=n/2$ implies $\Psi$ changes sign, so $\Psi$ describes a fermionic particle

The reason for such strange behaviour is that the full space in which the particle exists is not simply $\Re^3$, but the product of internal spinning space and $\Re^3$, which has unusual [[Topological spaces#Topologies|topology]]:![[Spin 2026-02-02 20.08.43.excalidraw]]
Hence, since $\varphi\rightarrow\varphi+2\pi$ flips sign:$$\Huge\begin{align*}
e^{i(\varphi+2\pi)S_z}&=\pm1\\
\implies S_z&\in\mathbb{N}/2\\
\implies S&\in\mathbb{N}/2
\end{align*}$$
Let us consider the example of a spin $S=1/2$ particle. Our Hilbert space is then spanned by$$\Huge\begin{align*}
|1/2,1/2\rangle&=|\text{up}\rangle=\begin{pmatrix}1\\
0\end{pmatrix}\\
|1/2,-1/2\rangle&=|\text{down}\rangle=\begin{pmatrix}1\\
1\end{pmatrix}
\end{align*}$$and the wave function takes form:$$\Huge \Psi=\psi_+(x,y,z)\begin{pmatrix}1 \\ 0\end{pmatrix}+\psi_-(x,y,z)\begin{pmatrix}0 \\ 1\end{pmatrix}=\begin{pmatrix}\psi_+ \\ \psi_-\end{pmatrix}$$Our spin operators then behave as:$$\Huge\begin{cases}\hat S_z |\text{up}\rangle=\frac{1}{2}|\text{up}\rangle \\
\hat S_z |\text{down}\rangle=-\frac{1}{2}|\text{down}\rangle\end{cases}\implies\hat S_z=\frac{1}{2}\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}=-\frac{1}{2}\hat\sigma_z$$where $\sigma_z$ is the $z$-Pauli matrix. Note that the Pauli matrices have the properties:
> $$\Huge \hat S_y=\begin{pmatrix}0 & -i/2 \\ 1/2 & 0\end{pmatrix}=\frac{1}{2}\hat\sigma_y,\,\,\hat S_x=\begin{pmatrix}0 & 1/2 \\ 1/2 & 0\end{pmatrix}=\frac{1}{2}\hat\sigma_x$$
> $\hat\sigma_i^\dagger=\hat\sigma_i$
> $\hat\sigma_i\hat\sigma_j=\delta_{ij}+i\epsilon_{ijk}\hat\sigma_k$
> $[\hat\sigma_i,\hat\sigma_j]=i\epsilon_{ijk}\sigma_k,\,\,\{\hat\sigma_i,\hat\sigma_j\}=\delta_{ij}$

