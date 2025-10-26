
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
To solve the eigenvalue problem here, we aim to solve:$$\Huge (\hat\Omega-\omega \hat{\mathbb{I}})|\omega\rangle=0$$For non-trivial $|\omega\rangle$ we require that $\hat\Omega-\omega\hat{\mathbb{I}}$ is non-invertible (zero determinant). Hence the roots of $p(\omega)=\det(\hat\Omega-\omega\hat{\mathbb{I}})$ are the eigenvalues. Since $p(\omega)$ has degree $\dim\mathcal{H}$ we say:$$\Huge p(\omega)=\prod_{i=1}^m(\omega-\omega_i)^{\lambda_i}$$where we have $m$ different eigenvalues with corresponding multiplicity $\lambda_i$ and $\sum_{i=1}^m\lambda_i=\dim\mathcal{H}$. The dimensions of the orthogonal subspaces of $\mathcal{H}$, $V_\omega$ are then given by $\dim V_{\omega_i}=\lambda_i$.

# Rules for probabilities:
The probability for an observation is given by the square of the coefficients. Suppose that we have a quantum coin $|\psi\rangle=a |H\rangle+b |T\rangle$. The probabilities of observing $H$ or $T$ are given by:$$\huge P(H)=|a|^2,\,\,P(T)=|b|^2$$For the probability to be unitary, we require that these quantities sum to $1$. We can then define the normalised state $|\psi\rangle$ as that with $\langle \psi|\psi\rangle=1$. This translates to:$$\Huge\begin{align*}
\langle \psi|\psi\rangle&=(\langle H|a^*+\langle T|b^*)(a |H\rangle+b |T\rangle)\\
&=|a^2|\langle H|H\rangle+|b^2|\langle T|T\rangle+b^*a \langle T|H\rangle+a^*b \langle H|T\rangle=1
\end{align*}$$It makes sense to define $|H\rangle$ to be orthogonal to $|T\rangle$. There must be some observable that gives different values for a head or a tail result. We call such operator $\hat\Omega_\text{head}$ that satisfies:$$\Huge\begin{align*}
\hat\Omega_\text{head}|H\rangle&=|H\rangle\\
\hat\Omega_\text{head}|T\rangle&=-|T\rangle
\end{align*}$$Since each state obviously has different $\Omega_\text{head}$ eigenvalues, it is an immediate consequence of defining this operator that $H$ and $T$ are orthogonal. We can also normalise the individual states so that when a state is pure head it is normalised ($\langle H|H\rangle=\langle T|T\rangle=1$), so we require:$$\Huge |a|^2+|b^2|=1$$More generally if $|\psi\rangle=\sum_ic_i|i\rangle$ for orthonormal basis $|i\rangle$, then $|c_i|^2=1$. Note that in a larger system with degenerate eigenvalues, the basis does not have to be orthonormal. Also, after measurement the coin is in state $|\psi'\rangle$, so will need to be re-normalised.

Take for example the three state system with basis $|1\rangle,|2\rangle,|3\rangle$ with defining matrix:$$\Huge \Omega_{ij}=\begin{pmatrix}1 & 0 & 0 \\ 0 & 0 & 1/2 \\ 0 & 1/2 & 0\end{pmatrix}$$which is obviously Hermitian. This has characteristic polynomial $(1-\lambda)(\lambda^2-1/4)=0$ and hance $\lambda=1,\pm1/2$ are the possible measurements. As $\hat\Omega$ has three non-degenerate eigenvalues there should be three orthogonal eigenvectors that span three orthogonal subspaces. We see that:$$\large \mathcal{H}_{\omega=1}=\left\{\begin{pmatrix}1 \\ 0 \\ 0\end{pmatrix}\right\},\,\,\mathcal{H}_{\omega=1/2}=\left\{\frac{1}{\sqrt 2}\begin{pmatrix}0 \\ 1 \\ 1\end{pmatrix}\right\},\,\,\mathcal{H}_{\omega=-1/2}=\left\{\frac{1}{\sqrt 2}\begin{pmatrix}0 \\ 1 \\ -1\end{pmatrix}\right\}$$
We can force the wave function to be in a particular state, for example $|\psi\rangle_{\omega=1/2}$, by another measurement. For example the $s=1$ eigenstate of $\hat S$ with:$$\Huge S_{ij}=\begin{pmatrix}0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 2\end{pmatrix}$$gives such a state. Now that we are starting in this state, we can ask of the probabilities of measuring each $\omega=1,\pm1/2$. We proceed by finding each $c_i$:
> Let $P(\omega=1)=\langle \underline{1}|\psi\rangle^2$ where $|\underline{1}\rangle$ denotes the eigenstate with eigenvalue $1$. Therefore we require:$$\Huge \langle \underline{1}|\psi\rangle=(1,0,0)\frac{1}{\sqrt 2}\begin{pmatrix}1 \\ 1 \\ 0\end{pmatrix}=\frac{1}{\sqrt 2}$$this gives $P(\omega=1)=1/2$.
> Likewise $P(\omega=1/2)=\langle \underline{1/2}|\psi\rangle^2$ and we find:$$\Huge \langle \underline{1/2}|\psi\rangle=\frac{1}{\sqrt 2}(0,1,1)\begin{pmatrix}1 \\ 1 \\ 0\end{pmatrix}=\frac{1}{2}$$this gives $P(\omega=1/2)=1/4$
> Finding $P(\omega=-1/2)$ is then trivial.

# Operator multiplication:

We can define the product between two linear operators $\hat A,\hat B$ through the composition $\hat A\hat B |\psi\rangle=\hat A(\hat B |\psi\rangle)$, which simply results in matrix multiplication of the operators defining matrices. We can also define the commutator of two operators as:$$\Huge [\hat A,\hat B]=\hat A\hat B-\hat B\hat A$$which obeys the identities:
> $[\hat A,\hat B]=-[\hat B,\hat A]$
> $[\hat A,\hat B\hat C]=[\hat A,\hat B]\hat C+\hat B[\hat A,\hat C]$
> $[\hat A\hat B,\hat C]=\hat A[\hat B,\hat C]+[\hat A,\hat C]\hat B$

# Simultaneous diagonalisation of Hermitian Operators:

If $\hat\Omega$ and $\hat\Lambda$ are two commuting Hermitian Operators ($[\hat O,\hat\Lambda]=0$), then there exists a common eigenbasis or common eigenspace decomposition. Suppose that $|\omega\rangle\in\mathcal{H}_\omega$, then:$$\Huge\hat\Omega\hat\Lambda |\omega\rangle=\hat\Lambda\hat\Omega |\omega\rangle=\omega\hat\Lambda |\omega\rangle$$which means that $\hat\lambda |\omega\rangle\in\mathcal{H}_\omega$ and that $\hat\Lambda:\mathcal{H}_\omega\rightarrow\mathcal{H}_\omega$. Hence:$$\Huge\mathcal{H}_{\omega_i}=\bigoplus_{j=1}^{d_i}\mathcal{H}_{\omega_i,\lambda_{i,j}}$$where $d_i$ is the number of distinct eigenvalues $\lambda_{i,j}$ of $\hat\Lambda$ appearing in the $i$th eigenspace of $\hat\Omega$. This allows for the systematic decomposition of the Hilbert space into smaller and smaller subspaces. That is, we have decomposed $\mathcal{H}$ using eigenvalues of $\hat\Omega(\omega_i)$, a commuting operator $\hat\Lambda$ can then be used to further decompose $\mathcal{H}_{\omega_i}$ into the eigenspaces of $\hat\Lambda$. 

Take for example:$$\Huge \hat O=\begin{pmatrix}1 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 1\end{pmatrix},\,\,\hat\Lambda=\begin{pmatrix}2 & 1 & 1 \\ 1 & 0 & -1 \\ 1 & -1 & 2\end{pmatrix}$$which are both obviously Hermitian. One can check that these are commuting operators. We are given that $\hat O$ has $2$ eigenvalues with corresponding eigenspaces:$$\Huge\mathcal{H}_{\omega=2}=\left\{\frac{1}{\sqrt 2}\begin{pmatrix}1 \\ 0 \\ 1\end{pmatrix}\right\},\,\,\mathcal{H}_{\omega=0}=\left\{\frac{1}{\sqrt 2}\begin{pmatrix}-1 \\ 0 \\ 1\end{pmatrix},\begin{pmatrix}0 \\ 1 \\ 0\end{pmatrix}\right\}$$We do not need to decompose $\mathcal{H}_{\omega=2}$ as it is already non-degenerate. We now want to show that we can solve the eigenvalue problem of $\hat\Lambda$ in the eigenspace $\mathcal{H}_{\omega=0}$ in order to write a decomposition:$$\Huge \mathcal{H}_{\omega=0}=\left\{\frac{1}{\sqrt 2}\begin{pmatrix}-1 \\ 0 \\ 1\end{pmatrix},\begin{pmatrix}0 \\ 1 \\ 0\end{pmatrix}\right\}=\{|\omega=0,1\rangle\}\oplus\{|\omega=0,2\rangle\}$$In order to do this, we need the new matrix form of $\hat\Lambda$ constrained in the space. This is found as follows:$$\Huge\begin{align*}
(\Lambda_{2\times2})_{ij}&=\langle \omega=0,i|\hat\Lambda |\omega=0,j\rangle\\
\hat\Lambda |\omega=0,1\rangle&=\Lambda\frac{1}{\sqrt 2}\begin{pmatrix}-1\\
0\\
1\end{pmatrix}\\
&=\frac{1}{\sqrt 2}\begin{pmatrix}-1\\
-2\\
-1\end{pmatrix}\\
&=|\omega=0,1\rangle-\sqrt 2|\omega=0,2\rangle\\
\hat\Lambda |\omega=0,2\rangle&=\Lambda\begin{pmatrix}0\\
1\\
0\end{pmatrix}\\
&=\begin{pmatrix}1\\
0\\
-1\end{pmatrix}\\
=-\sqrt 2 |\omega=0,1\rangle\\
\implies\Lambda_{2\times 2}&=\begin{pmatrix}1 & -\sqrt 2\\
-\sqrt 2 & 0\end{pmatrix}
\end{align*}$$Now we simply solve for the eigenvectors of $\Lambda_{2\times2}$, giving values $-1,2$ with corresponding vectors $\frac{1}{\sqrt3}\begin{pmatrix} 1\\ \sqrt 2\end{pmatrix},\frac{1}{\sqrt 3}\begin{pmatrix}-\sqrt 2 \\ 1\end{pmatrix}$. Putting these back together we can reconstruct the eigenstates in the original basis:$$\Huge\begin{align*}
|\omega=0,\lambda=-1\rangle&=\frac{1}{\sqrt 3}(|\omega=0,1\rangle+\sqrt2 |\omega=0,2\rangle)\\
&=\frac{1}{\sqrt6}\begin{pmatrix}-1\\
2\\
1\end{pmatrix}\\
|\omega=0,\lambda=-2\rangle&=\frac{1}{\sqrt3}(-\sqrt 2|\omega=0,1\rangle+|\omega=0,2\rangle)\\
&=\frac{1}{\sqrt 3}\begin{pmatrix}1\\
1\\
-1\end{pmatrix}
\end{align*}$$Hence we have the required decomposition:$$\Huge\mathcal{H}_{\omega=0}=\mathcal{H}_{\omega=0,\lambda=-1}\oplus\mathcal{H}_{\omega=0,\lambda=-2}=\left\{\frac{1}{\sqrt6}\begin{pmatrix}-1 \\ 2 \\ 1\end{pmatrix}\right\}\oplus\left\{\frac{1}{\sqrt3}\begin{pmatrix}1 \\ 1 \\ -1\end{pmatrix}\right\}$$

We propose that operators that do not commute cannot be measured simultaneously. Let $\hat\Omega$ and $\hat\Lambda$ be two operators with eigenvalues $\omega,\lambda$ respectively. Assume that $\hat\Omega$ and $\hat\Lambda$ CAN be measured simultaneously. This implies that there exists a common eigenvector $|\psi\rangle$ such that:$$\Huge \hat\Omega |\psi\rangle=\omega |\psi\rangle,\,\,\hat\Lambda |\psi\rangle=\lambda |\psi\rangle$$Now consider the commutator $[\hat\Omega,\hat\Lambda]$:$$\Huge\begin{align*}
[\hat\Omega,\hat\Lambda]|\psi\rangle&=(\hat\Omega\hat\Lambda-\hat\Lambda\hat\Omega)|\psi\rangle\\
&=\hat\Omega(\hat\Lambda |\psi\rangle)-\hat\Lambda(\hat\Omega |\psi\rangle)\\
&=\hat\Omega(\lambda |\psi\rangle)-\hat\Lambda(\omega |\psi\rangle)\\
&=\lambda(\hat\Omega |\psi\rangle)-\omega(\hat\Lambda |\psi\rangle)\\
&=\lambda \omega |\psi\rangle-\omega\lambda |\psi\rangle\\
&=(\lambda\omega-\omega\lambda)|\psi\rangle=0
\end{align*}$$This implies $[\hat\Omega,\hat\Lambda]=0$, however we started with the assumption that they do not commute, we have found a contradiction. Therefore the operators cannot be measured simultaneously.

# Projection Operators:

An operator $\hat P$ satisfying $\hat P^2=\hat P$ is called a projection operator and satisfies the following properties:
> Idempotence, $\hat P_{\omega_i}^2=\hat P_{\omega_i}$
> Hermiticity, $\hat P_{\omega_i}^\dagger=\hat P_{\omega_i}$
> Orthogonality, $\hat P_{\omega_i}\hat P_{\omega_j}=0$ for $i\neq j$
> Completeness, $\sum_i\hat P_{\omega_i}=\hat{\mathbb{I}}$

These projection operators play a crucial role in describing measurements and the collapse of wavefunctions. Consider a two dimensional Hilbert space and visualise how a projection operator would work. Imagine a quantum state $|\psi\rangle$ in a two dimensional space spanned by orthonormal basis vectors $|x\rangle,|y\rangle$. The projection operator $\hat P_x$ projects this state onto the $x$-basis:$$\Huge\hat P_x=|x\rangle \langle x|$$When $\hat P_x$ acts on $|\psi\rangle$ it projects the state onto the $x$-axis, giving the component of $|\psi\rangle$ along $|x\rangle$:$$\Huge \hat P_x |\psi\rangle=(|x\rangle \langle x|)|\psi\rangle=\langle x|\psi\rangle |x\rangle$$The resulting state $\hat P_x |\psi\rangle$ is then parallel to $|x\rangle$ and its magnitude represents the probability amplitude for measuring the system in the $x$-basis:![[Operators and Measurement 2025-10-26 06.03.57.excalidraw]]
It is key to remember that $\hat P_x$ collapses the state into the $x$-axis, and that the length of $\hat P_x |\psi\rangle$ will always be less than or equal to the length of $|\psi\rangle$. The probability of measuring the system in the $x$-basis i then given by the square of the length of $\hat P_x |\psi\rangle$. After projection, the state is an eigenstate of the $x$-basis observable.

We can make this definition more precise. Consider $\mathcal{H}=\mathcal{H}_1\oplus\mathcal{H}_2$. We can then decompose any $|\psi\rangle\in\mathcal{H}$ such that $|\psi\rangle=|\psi_1\rangle+|\psi_2\rangle$ where $|\psi_1\rangle\in\mathcal{H}_1,|\psi_2\rangle\in\mathcal{H}_2$. We therefore define $\hat P_1,\hat P_2$:$$\Huge\begin{align*}
\hat P_{\mathcal{H}_1}|\psi\rangle=|\psi_1\rangle,&\,\,\hat P_{\mathcal{H}_2}|\psi\rangle=|\psi_2\rangle\\
\hat P_{\mathcal{H}_2}\hat P_{\mathcal{H}_2}&=0\\
\hat P_{\mathcal{H}_1}+\hat P_{\mathcal{H}_2}&=\hat{\mathbb{I}}
\end{align*}$$Which generalises nicely to arbitrary Hilbert space $\mathcal{H}$. Suppose $\mathcal{H}=\bigoplus_{i=1}^n\mathcal{H}_i$, we then define $\hat P_{\mathcal{H}_i}$ such that:$$\Huge\begin{align*}
\hat P_{\mathcal{H}_i}^2&=\hat P_{\mathcal{H}_i}\\
\hat P_{\mathcal{H}_i}\hat P_{\mathcal{H}_j}&=\delta_{ij}\hat P_{\mathcal{H}_i}\\
\sum_{i=1}^n\hat P_{\mathcal{H}_i}&=\hat{\mathbb{I}}
\end{align*}$$
For example, if the subspace $V\subset\mathcal{H}$ is spanned by the orthonormal basis $\{|i\rangle\}$ for $i=1,\dots,\dim V$ then:$$\Huge\hat P_V=\sum_{j=1}^{\dim V}|j\rangle \langle j|$$To prove this, consider the complement $V^c$ where $V^c$ is spanned by $\{|\alpha\rangle\}$ by:$$\Huge \langle i|j\rangle=\delta_{ij},\,\,\langle \alpha|\beta\rangle=\delta_{\alpha\beta},\,\,\langle i|\alpha\rangle=0$$That is, $\{|i\rangle,|\alpha\rangle\}$ form an orthonormal basis for $\mathcal{H}$ and we can therefore express and $|\psi\rangle\in\mathcal{H}$ as:$$\Huge\begin{align*}
|\psi\rangle&=\sum_{j=1}^{\dim V}c_j |j\rangle+\sum_{\alpha=1}^{\dim V^c}d_\alpha |\alpha\rangle\\
\implies\hat P_V |\psi\rangle&=\sum_{j=1}^{\dim V}c_j |j\rangle\\
&=\sum_{j=1}^{\dim V}\langle j|\psi\rangle |j\rangle\\
&=\sum_{j=1}^{\dim V}|j\rangle \langle j|\psi\rangle\\
\implies \hat P_V\hat P_V&=\sum_{i,j=1}^{\dim V}|i\rangle \langle i| |j\rangle \langle j|\\
&=\sum_{i,j=1}^{\dim V}\delta_{ij}|i\rangle \langle j|\\
&=\sum_{i=1}^{\dim V}|i\rangle \langle i|=\hat P_v
\end{align*}$$

An obvious but trivial example of a projection operator is the identity itself. In this case we have $V=\mathcal{H}$, and:$$\Huge\hat P_{\mathcal{H}}=\hat{\mathbb{I}}=\sum_{i=1}^{\dim\mathcal{H}}|i\rangle \langle i|$$We can now use the projection operators to find probabilities of observing a specific state.

Take for example the quantum coin with $\mathcal{H}=\{|H\rangle, |T\rangle\}$. In this case, a projection onto the heads subspace will look like $P_H=|H\rangle \langle H|$. Then for $|\psi\rangle=a |H\rangle+b |T\rangle$ we have:$$\Huge P(H)=\langle \psi|\hat P_H |\psi\rangle=\langle \psi|H\rangle \langle H|\psi\rangle=|\langle H|\psi\rangle|^2=|a|^2$$
# Spectral Decomposition:

If $\hat\Omega$ is Hermitian and $\omega_i$ are its eigenvalues, then the Spectral Decomposition theorem dictates that:$$\Huge\hat\Omega=\sum_{i=1}^m\omega_i\hat P_{\omega_i}$$where $\hat P_{\omega_i}$ is the projection operator on the eigenspace $\mathcal{H}_{\omega_i}$. Spectral decomposition induces a decomposition of the Hilbert space $\mathcal{H}$ into orthogonal subspaces:$$\Huge\mathcal{H}=\bigoplus_i\mathcal{H}_i$$where $\mathcal{H}_i$ is the eigenspace associated with eigenvalue $\omega_i$ and $\oplus$ denotes the direct sum of the subspaces:![[Operators and Measurement 2025-10-26 07.38.17.excalidraw]]We prove the Spectral Decomposition theorem simply by inserting a copy of $\hat{\mathbb{I}}$. For any $|\psi\rangle\in\mathcal{H}$:$$\Huge \hat O |\psi\rangle=\hat O\hat{\mathbb{I}} |\psi\rangle=\hat O\sum_{i=1}^m\hat P_{\omega_i}|\psi\rangle=\sum_{i=1}^m\hat O(\hat P_{\omega_i}|\psi\rangle)=\sum_{i=1}^m\omega_i\hat P_{\omega_i}|\psi\rangle$$which implies:$$\Huge\implies\hat O=\sum_{i=1}^m\omega_i\hat P_{\omega_i}$$

We propose that if $f(x)$ is a function $f:\mathbb{C}\rightarrow\mathbb{C}$ that admits a [[Taylor series|Taylor expansion]], then:$$\Huge \hat f(\hat O)=\sum_{i=1}^mf(\omega_i)\hat P_{\omega_i}$$To prove this, we observe the properties of orthogonal eigenspaces:$$\Huge\hat P_{\omega_i}\hat P_{\omega_j}=\delta_{ij}\hat P_{\omega_i}$$and more generally we have:$$\Huge(\hat P_{\omega_i})^n(\hat P_{\omega_j})^m=\delta_{ij}\hat P_{\omega_i}$$for any two natural numbers $m,n$. Therefore inserting operators into the Taylor series for $f$ gives:$$\Huge\begin{align*}
\hat f(\hat O)&=\sum_{i=0}^\infty c_i\hat O^i\\
&=\sum_{i=1}^\infty c_i\left(\sum_{j=1}^m\omega_j\hat P_{\omega_j}\right)^i\\
&=\sum_{i=1}^\infty c_i\sum_{j=1}^m\omega_j^i\hat P_{\omega_j}\\
&=\sum_{j=1}^m\left(\sum_{i=1}^\infty c_i\omega_j^i\right)\hat P_{\omega_j}\\
&=\sum_{j=1}^mf(\omega_j)\hat P_{\omega_j}
\end{align*}$$as required. Note that $V_{\omega_i}$ are also eigenspaces of $\hat f(\hat O)$ with corresponding eigenvalues $f(\omega_i)$.

# Unitary Operators:

A unitary operator $\hat U$ satisfies $\hat U^\dagger\hat U=\hat U\hat U^\dagger=\hat{\mathbb{I}}$, where $\hat U^\dagger$ is the [[QM linear algebra#Adjoints|adjoint]] of $\hat U$. These operators are often expressed in terms of exponentials of Hermitian operators. That is, if $\hat T$ is self adjoint then $\hat U=e^{i\theta\hat T}$ is unitary for constant $\theta\in\Re$. To prove this, notice that:$$\Huge \hat U^\dagger=e^{-i\theta\hat T^\dagger}=e^{-i\theta\hat T}\implies\hat U^\dagger\hat U=e^{-i\theta\hat T}e^{i\theta\hat T}=\hat{\mathbb{I}}=\hat U\hat U^\dagger$$making $\hat U$ unitary by definition.

A common form for a unitary operator is given by the exponential of a Hermitian operator multiplied by $i$ and some real parameter $\theta$. Take for example the [[Lie groups and Lie Algebras#Pauli matrices|Pauli matrices]] $\tau_2,\tau_3$:$$\Huge \tau_2=\begin{pmatrix}0 & -i \\ i & 0\end{pmatrix},\,\,\tau_3=\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$$
We can then define the unitary operator:$$\Huge\hat U_3(\theta)=e^{-i\theta\hat\tau_3}=\cos(\theta)\hat{\mathbb{I}}-i\sin(\theta)\hat\tau_3\implies U_3(\theta)=\begin{pmatrix}e^{-i\theta} & 0 \\ 0 & e^{i\theta}\end{pmatrix}$$One can check this result using the Taylor series definition of the exponential. Similarly, we define:$$\Huge\hat U_2(\theta)=e^{-i\theta\hat\tau_2}=\cos(\theta)\hat{\mathbb{I}}-i\sin(\theta)\hat\tau_2$$which, using the same methodology as above shows us that:$$\Huge\hat U_2(\theta)=\begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{pmatrix}$$

We propose that an operator is unitary if and only if it preserves the inner product between any two states. Suppose that $|\psi_1\rangle'=\hat U |\psi_1\rangle,|\psi_2\rangle'=\hat U|\psi_2\rangle$, then:$$\Huge \langle \psi_2'|\psi_1'\rangle=\langle \psi_2|\hat U^\dagger\hat U |\psi_1\rangle=\langle \psi_2|\hat{\mathbb{I}}|\psi_1\rangle=\langle \psi_2|\psi_1\rangle$$So we have forward implication. For the reverse, we choose $|\psi_1\rangle=|i\rangle,|\psi_2\rangle=|j\rangle$ for any two basis states. Then the statement about inner product preservation becomes:$$\Huge \langle j'|i'\rangle=\langle j|\hat U^\dagger\hat U |i\rangle=\langle j|i\rangle$$which implies that elements of $\hat U^\dagger\hat U$ are given as:$$\Huge(\hat U^\dagger\hat U)_{ij}=\delta_{ij}$$
A particular consequence of this is that the norm $\langle \psi|\psi\rangle$ is preserved under unitary transformations of $|\psi\rangle$.

# Degeneracies as Symmetries:

An important observation is the link between unitary operators that leave a state unchanged and symmetries. Consider the unitary operator:$$\Huge\hat R_{\Lambda_s}=e^{i\theta\hat\Lambda_s},\,\,\Lambda_s=\begin{pmatrix}-2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}$$The matrix $\Lambda_s$ is Hermitian and diagonal, simplifying the eigenproblem. The eigenvalues are simply $\lambda_s=-2,1,1$. We can take the eigenvectors of $\Lambda_s$ to be the standard basis vectors of $\Re^3$:$$\Huge\lambda_s=-2\leftrightarrow |1\rangle=\begin{pmatrix}1 \\ 0 \\ 0\end{pmatrix},\,\,\lambda_s=1\leftrightarrow |2\rangle=\begin{pmatrix}0 \\ 1 \\ 0\end{pmatrix},\,\,\lambda_s=1\leftrightarrow |3\rangle=\begin{pmatrix}0 \\ 0 \\ 1\end{pmatrix}$$Note that the Hilbert space has two degenerate eigenvalues and thus $\mathcal{H}=\mathcal{H}_{\lambda_s=-2}\oplus\mathcal{H}_{\lambda_s=1}$ where $\mathcal{H}_{\lambda_s=1}$ is two dimensional. We now have the freedom to choose a different basis to span $\mathcal{H}_{\lambda_s=1}$. The system is equivalent if we choose a basis spanning $\mathcal{H}_{\lambda_s=1}$ formed of linear combinations of $|2\rangle,|3\rangle$. There is another operator that we could measure that breaks $\mathcal{H}_{\lambda_s=1}$ into non-degenerate subspaces. As an example, consider defining:$$\Huge\hat\Lambda_2=\begin{pmatrix}1 & 0 & 0 \\ 0 & 0 & -i \\ 0 & i & 0\end{pmatrix}$$which clearly commutes with $\hat\Lambda_s$. The corresponding unitary operator is then:$$\Huge \hat R_{\Lambda_2}=e^{i\phi\hat\Lambda_2}$$This operator generates transformations that can be interpreted as rotations around a specific axis in the space spanned by the eigenstates of $\hat\Lambda_2$. We saw this exact matrix in the two dimensional Pauli matrix example:$$\Huge\hat R_{\Lambda_2}=\begin{pmatrix}1 & 0 & 0 \\ 0 & \cos\phi & -\sin\phi \\ 0 & \sin\phi & \cos\phi\end{pmatrix}$$then clearly the system remains invariant under the transformations generated by $\hat R_{\Lambda_2}$ because this just generates change in the degenerate basis spanning $\mathcal{H}_{\lambda_s=1}$:$$\Huge\begin{align*}
|1\rangle&\rightarrow\cos\phi |1\rangle-\sin\phi |2\rangle\\
|2\rangle&\rightarrow\cos\phi |2\rangle+\sin\phi |1\rangle
\end{align*}$$which remains a symmetry of the theory unless the degeneracy is broken. The form of $\Lambda_2$ suggests a relationship with [[Lie groups and Lie Algebras#$SU(2)$|SU(2)]] as the three Pauli matrices are generators for that group. In fact, unitary rotations $\hat R_{\Lambda_1},\hat R_{\Lambda_2},\hat R_{\Lambda_3}$ with$$\Huge\hat\Lambda_1=\begin{pmatrix}1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix},\,\,\hat\Lambda_3=\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1\end{pmatrix}$$are all rotations under which the system is symmetric. Once a measurement of any of these observables is made, the symmetry is broken due to the collapse of the wavefunction into an eigenstate. 