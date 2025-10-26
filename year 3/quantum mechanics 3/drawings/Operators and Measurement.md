
# Hermitian Operators and the Eigenvalue problem:

We defined Quantum states to belong to a [[QM linear algebra#Hilbert space|Hilbert space]]. States can evolve over time when not being observed, however we still expect to measure one of the original possible outcomes. That is, the measured state must still be in the original Hilbert space. Therefore measuring an observable must correspond to something that maps a vector in Hilbert space into another vector in the SAME space. That is:$$\Huge \begin{align*}
\hat O&:\mathcal{H}\rightarrow\mathcal{H}\\
&:\hat O |\psi\rangle\rightarrow |\psi'\rangle
\end{align*}$$One of the main assumptions we made was that if we prepare a state by measuring something, and then immediately measuring again, we should get the same result. Suppose we had an operator $\hat A$ and measure its value for state $|\psi\rangle$, we would expect:$$\Huge \hat A |\psi\rangle=a |\psi'\rangle\implies\hat A |\psi'\rangle=a |\psi'\rangle$$This implies that any measurement reduces to an eigenvalue problem. The eigenvalue problem for $\hat\Omega$ is the set of all $\omega\in\mathbb{C}$ and $|\omega\rangle\in\mathcal{H}$ such that $\hat\Omega |\omega\rangle=\omega |\omega\rangle$ where $\omega$ is the eigenvalue and $|\omega\rangle\neq0$.



The eigenvectors of a given value $\omega$ then form a linear subspace of Hilbert space, $V_\omega$. This is the eigenspace corresponding to the eigenvalue $\omega$:
> If $\dim V_\omega>1$ then we call $\dim V_\omega$ the degeneracy of the eigenvalue $\omega$
> If $\dim V_\omega$, then $\omega$ is non-degenerate 

Eigenvalues can have degenerate subspaces of eigenstates where eigenvalues are the same. Note that [[QM linear algebra#Linear operators|Hermitian]] operators have real eigenvalues, so we would like physically measurable observables to correspond to Hermitian operators:
> The eigenvalues of Hermitian $\hat\Omega=\hat\Omega^\dagger$ are real numbers
> The different eigenvalues of $\omega$ are orthonormal, that is for $\omega_1\neq\omega_2$ and $|\omega_1\rangle\in V_{\omega_1},|\omega_2\rangle\in V_{\omega_2}$ we have $\langle \omega_1|\omega_2\rangle=0$
> The eigenvalues of $\hat\Omega$ can be used to construct an orthonormal basis of $\mathcal{H}$. If $V_{\omega_i}$ are the different eigenspaces of $\hat\Omega$ then:$$\Huge\mathcal{H}=\bigoplus_{i=1}^nV_{\omega_i}$$this is known as the completeness of eigenvectors of Hermitian Operators.

We must prove that if $\hat\Omega |\omega\rangle=\omega |\omega\rangle$ then $\omega=\omega^*$:$$\Huge\begin{align*}
\langle \omega|\hat\Omega |\omega\rangle^*&=\langle \omega|\hat\Omega^\dagger |\omega\rangle=\omega \langle \omega|\omega\rangle\\
&=\langle \omega|\omega |\omega\rangle^*=\omega^* \langle \omega|\omega\rangle^*\\
\implies\omega&=\omega^*
\end{align*}$$as well as orthogonality of eigenvalues. Consider $\langle \omega_1|\hat O |\omega_2\rangle$:$$\Huge\begin{align*}
\langle \omega_1|\hat\Omega |\omega_2\rangle&=\omega_2 \langle \omega_1|\omega_2\rangle\implies \langle \omega_1|\hat\Omega |\omega_2\rangle^*=\omega_2 \langle \omega_2|\omega_1\rangle\\
\langle \omega_ 1|\hat\Omega |\omega_2\rangle^*&=\langle \omega_2|\hat\Omega^\dagger |\omega_1\rangle=\langle \omega_2|\hat\Omega |\omega_1\rangle=\omega_1 \langle \omega_2|\omega_1\rangle
\end{align*}$$Since these are equivalent expressions, we can subtract the two to compare to $0$:$$\Huge (\omega_2-\omega_1)\langle \omega_2|\omega_1\rangle=0$$and so we get the implications of either:
> Degeneracy, $\omega_2=\omega_1=0$
> Orthogonality, $\langle \omega_2|\omega_1\rangle=0$

## Solving the eigenvalue problem:
To solve the eigenvalue problem here, we aim to solve:$$\Huge (\hat\Omega-\omega \hat{\mathbb{I}})|\omega\rangle=0$$