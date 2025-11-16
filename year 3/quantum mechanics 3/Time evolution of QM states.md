
# Schrodinger equation motivation:

The time evolution of quantum mechanical states is governed by the Schrodinger equation. Central to this evolution is the Hamiltonian operator $\hat H$, which encapsulates the total energy of the system. In QM this plays a crucial role as it dictates the dynamics and temporal progression of QM states.

One can find motivation for the equation through symmetries and their generators. [[QM linear algebra#Linear operators|Recall]] the operator $\hat R_{\Lambda_2}=e^{i\phi\hat\tau_2}$ that represented a rotational symmetry of the system. We noted that expectation values of $\hat\tau_2$ would not change under rotation because of this symmetry. Now consider the same situation for shifts in time. We would like the system to not lose energy, that is we expect the expectation of the energy to stay the same. We can write this in terms of a single unitary evolution operator for the wave function $\psi$:$$\Huge |\psi(t)\rangle=e^{-i\frac{\bar Ht}{\hbar}}|\psi_0\rangle$$where $\psi_0$ is the wave function at $t=0$ and $\hat H$ is the Hamiltonian. In this way we can motivate the form of time-evolution by a direct link with energy conservation. It is useful to compute the time derivative:$$\Huge \frac{d}{dt}|\psi(t)\rangle=-i\frac{\hat H}{\hbar}e^{-i\frac{\hat Ht}{\hbar}}|\psi(t)\rangle$$Which then defines the Schrodinger equation:$$\Huge i\hbar \frac{d}{dt}|\psi(t)\rangle=\hat H |\psi(t)\rangle$$which is a more useful way of describing time evolution. 

# Time evolution and the importance of the $\hat H$ eigenbasis:

Given a particular form for $\hat H$, we ask for the best way of solving for the time evolution of a wave function $|\psi\rangle$. Firstly, we aim to represent $|\psi(t)\rangle$ in terms of the eigenbasis of $\bar H$. There are two common methods:
 > In the first method we use spectral decomposition of $\bar H$ which has generic eigenvalues given by $E_\alpha$ for $\alpha=1,\dots,m$ and $\hat P_{E_\alpha}$ as the respective projection operators. In other words, $\alpha$ labels the $\mathcal{H}_\alpha$ subspaces of the original Hilbert space organised by energy eigenvalues. These are often called the "principle quantum number" of the state. Using the expansion of any operator in terms of its projection operators, we can write the unitary evolution operator as:$$\Huge \hat U_t=e^{-i\frac{\hat H}{\hbar}t}=\sum_{\alpha=1}^me^{-i\frac{E_\alpha}{\hbar}t}\hat P_{E_\alpha}$$If $|E_\alpha,j\rangle$ is an orthonormal basis of $\mathcal{H}_{E_\alpha}$ then as we have seen it takes the form:$$\Huge\begin{align*}
\hat P_{E_\alpha}&=\sum_{j=1}^{\dim(\mathcal{H}_{E_\alpha})}|E_\alpha,j\ \langle E_\alpha,j|\\
\implies |\psi(t)\rangle&=\sum_{\alpha=1}^m\sum_{j=1}^{\dim(\mathcal{H}_{E_\alpha})}e^{-i\frac{E_\alpha}{\hbar}t}|E_\alpha,j\rangle \langle E_\alpha,j|\psi_0\rangle
\end{align*}$$That is to say, we must first express the wave function at $t=0$ as an expansion over the energy eigenstates:$$\Huge |\psi_0\rangle=\sum_{\alpha,j}c_{\alpha,j} |E_\alpha,j\rangle$$such that the coefficients are given by $c_{\alpha,h}=\langle E_\alpha,j|\psi_0\rangle$. Then we have:$$\Huge |\psi(t)\rangle=\sum_{\alpha=1}^m\sum_{j=1}^{\dim(\mathcal{H}_{E_\alpha})}e^{-i\frac{E_\alpha}{\hbar}t}c_{\alpha,j}|E_\alpha,j\rangle$$
> The second method involves operation more directly. The initial state $|\psi(t=0)\rangle$ can be written as a linear combination of the eigenbasis:$$\Huge\begin{align*}
|\psi_0\rangle&=\sum_{\alpha=1}^m\sum_{j=1}^{\dim(\mathcal{H}_{E_\alpha})}c_{\alpha,j}|E_\alpha,j\rangle\\
\implies |\psi(t)\rangle&=e^{-i\frac{\hat H}{\hbar}t}\sum_{\alpha=1}^m\sum_{j=1}^{\dim(\mathcal{H}_{E_\alpha})}\\
&=\sum_{\alpha=1}^m\sum_{j=1}^{\dim(\mathcal{H}_{E_\alpha})}c_{\alpha,j}e^{-i\frac{\hat H}{\hbar}t}|E_\alpha,j\rangle\\
&=\sum_{\alpha=1}^m\sum_{j=1}^{\dim(\mathcal{H}_{E_\alpha})}c_{\alpha,j}e^{-i\frac{\hat H}{\hbar}t}|E_\alpha,j\rangle
\end{align*}$$

Therefore, in general, a state evolves by all its energy eigenstate components evolving with a phase given by the energy. We also observe that if the initial state $|\psi_0\rangle$ is itself an eigenvector of $\hat H$ with eigenvalue $E$, then $|\psi(t)\rangle=e^{-i\frac{E}{\hbar}t}|\psi_0\rangle$. This overall phase is not measurable so in effect the system remains constant if it happens to be an energy eigenstate. To show that the expectation of energy is constant requires more work, which we do later.

## Example:
Take for example a quantum system characterised by the Hamiltonian and $t=0$ state:$$\Huge\hat H=\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix},\,\,|\psi(0)\rangle=\begin{pmatrix}1 \\ 0\end{pmatrix}$$We aim to determine the time evolution, and ask how long it will take for the system to end up in the $|2\rangle=\begin{pmatrix}0 \\ 1\end{pmatrix}$ state:
> First we must find the energy Eigenbasis. To do this, we find the eigenvalues of $\hat H$ which are $\pm1$. We then find that the eigenvectors are:$$\Huge|v_\pm\rangle=\frac{1}{\sqrt 2}\begin{pmatrix}1 \\ \pm1\end{pmatrix}$$
> Now we must find the time dependence in the energy Eigenbasis. To do this, we must express the initial state $|\psi(0)\rangle$ in the energy eigenbasis:$$\Huge\begin{align*}
|\psi(0)\rangle&=\alpha |v_+\rangle+\beta |v_-\rangle\\
\begin{pmatrix}1\\
0\end{pmatrix}&=\alpha\frac{1}{\sqrt 2}\begin{pmatrix}1\\
1\end{pmatrix}+\beta\frac{1}{\sqrt 2}\begin{pmatrix}1\\
-1\end{pmatrix}\\
&=\frac{\alpha+\beta}{\sqrt 2}\begin{pmatrix}1\\
0\end{pmatrix}+\frac{\alpha-\beta}{\sqrt 2}\begin{pmatrix}0\\
1\end{pmatrix}
\end{align*}$$Which we can solve for $\alpha,\beta$ to find that $\alpha=\beta=\frac{1}{\sqrt 2}$. Now we can express the time evolution in the energy eigenbasis:$$\Huge\begin{align*}
|\psi(t)\rangle&=\alpha e^{-i\frac{t}{\hbar}\lambda_+}|v_+\rangle+\beta e^{-i\frac{t}{\hbar}\lambda_-}|v_-\rangle\\
&=\frac{1}{\sqrt 2}e^{-i\frac{t}{\hbar}\lambda_+}|v_+\rangle+\frac{1}{\sqrt{2}}e^{-i\frac{t}{\hbar}\lambda_-}|v_-\rangle
\end{align*}$$
> Finally, we must convert back into the original basis. To do this, we simply insert the explicit forms of the energy eigenstates:$$\Huge\begin{align*}
|\psi(t)\rangle&=\frac{1}{\sqrt 2}e^{-i\frac{t}{\hbar}(1)}\begin{pmatrix}\frac{1}{\sqrt 2}\\
\frac{1}{\sqrt 2}\end{pmatrix}+\frac{1}{\sqrt 2}e^{-i\frac{t}{\hbar}(-1)}\begin{pmatrix}\frac{1}{\sqrt 2}\\
-\frac{1}{\sqrt 2}\end{pmatrix}\\
&=\frac{1}{2}\begin{pmatrix}e^{-i\frac{t}{\hbar}}+e^{i\frac{t}{\hbar}}\\
e^{-i\frac{t}{\hbar}}-e^{i\frac{t}{\hbar}}\end{pmatrix}\\
&=\begin{pmatrix}\cos(\frac{t}{\hbar})\\
-i\sin(\frac{t}{\hbar})\end{pmatrix}
\end{align*}$$And we see that this state becomes $|2\rangle$ when $t=\pi/2\hbar$

This kind of behaviour is generic when a state is not a pure energy eigenstate but instead a mixture of energy eigenstates. We see that the state oscillates between the eigenstates that would build up a pure energy eigenstate.  

## Expectation value behaviour:
We expect that the expectation value for the $\hat H$ operator should be constant:$$\Huge\langle\hat H\rangle=\left(\cos\left(\frac{t}{\hbar}\right),i\sin\left(\frac{t}{\hbar}\right)\right)\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}\begin{pmatrix}\cos\left(\frac{t}{\hbar}\right) \\ -i\sin\left(\frac{t}{\hbar}\right)\end{pmatrix}=0$$On the other hand we see that operators that do not commute have a time dependent expectation value. Consider the "head-ness" operator $\Omega_\text{head}=\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$:$$\Huge\begin{align*}
\langle\Omega_\text{head}\rangle&=\left(\cos\left(\frac{t}{\hbar}\right),i\sin\left(\frac{t}{\hbar}\right)\right)\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}\begin{pmatrix}\cos\left(\frac{t}{\hbar}\right) \\ -i\sin\left(\frac{t}{\hbar}\right)\end{pmatrix}\\
&=\cos^2\left(\frac{t}{\hbar}\right)-\sin^2\left(\frac{t}{\hbar}\right)\\
&=\cos\left(\frac{2t}{\hbar}\right)
\end{align*}$$
# Time evolution of expectation values:

We now consider the expectation value of energy:$$\Huge \begin{align*}
\langle \psi|\hat H |\psi\rangle&=\langle \psi_0|e^{i\hat Ht/\hbar}\hat He^{-i\hat Ht/\hbar}|\psi_0\rangle\\
&=\langle \psi_0|\hat H |\psi_0\rangle=E_0
\end{align*}$$where we were able to commute the exponential terms through the operator since they were constructed through the same operators. This is to say that the expectation value is constant, precisely because the evolution operator $\hat U_t$ is unitary and only a function of $\hat H$.

There is however a more general statement that we can make about time dependence for any operator, known as the Ehrenfest theorem:
> The expectation value of an operator $\hat\Lambda$ that is not itself an explicit function of time obeys:$$\Huge \frac{d}{dt}\langle\hat\Lambda\rangle=-\frac{i}{\hbar}\langle[\hat \Lambda,\hat H]\rangle$$
> To prove this, we take time derivatives of the expectation value as follows:$$\Huge\begin{align*}
\frac{d}{dt}\langle\hat\Lambda\rangle&=\frac{d}{dt}\langle \psi(t)|\hat\Lambda |\psi(t)\rangle\\
&=\left(\frac{d}{dt}\langle \psi(t)|\right)\hat\Lambda |\psi(t)\rangle+\langle \psi(t)|\frac{d}{dt}(\hat\Lambda |\psi(t)\rangle)\\
\left(i\hbar \frac{d}{dt}|\psi(t)\rangle\right)^\dagger&=(\hat H(t)|\psi(t)\rangle)^\dagger\\
\implies-i\hbar \frac{d}{dt} \langle \psi(t)|&=\langle \psi(t)|\hat H^\dagger=\langle \psi(t)|\hat H(t)\\
\implies \frac{d}{dt}\langle\hat \Lambda\rangle&=\frac{i}{\hbar}\langle \psi(t)|\hat H(t)\hat \Lambda |\psi(t)\rangle-\frac{i}{\hbar}\langle \psi(t)|\hat\Lambda\hat H(t)|\psi(t)\rangle\\
&=-\frac{i}{\hbar}\langle[\hat\Lambda,\hat H]\rangle
\end{align*}$$

We can think of the preservation of the norm as the conservation of the operator $\hat{\mathbb{I}}$. This is clear writing:$$\Huge\begin{align*}
\langle\hat{\mathbb{I}}\rangle&=\langle \psi(t)|\hat{\mathbb{I}}|\psi(t)\rangle=\langle \psi(t)|\psi(t)\rangle\\
\implies \frac{d}{dt}\langle\hat{\mathbb{I}}\rangle&=-\frac{i}{\hbar}\langle[\hat{\mathbb{I}},\hat H]\rangle=0
\end{align*}$$
Also note that if a general operator $\hat\Lambda$ commutes with $\hat H$ then we get that $\langle\hat\Lambda\rangle$ is automatically independent of time, making $\hat\Lambda$ a conserved quantity. Therefore we can say that operators that commute with the Hamiltonian have conserved expectations.

Note that the equation for time derivatives of operators is equivalent to the classical one, replacing the [[Hamiltonian Formalism#Poisson bracket|Poisson bracket]] with the commutator term. This motivates a general principle about the relation between a quantum system and its classical equivalent:
> The Correspondence principle states that in order to quantise a classical system, the commutators of the quantum operators should reproduce the classical Poisson bracket:$$\Huge \begin{align*}\langle[\hat A,\hat B]\rangle&=i\hbar\{A,B\}\\
\rightarrow[\hat A,\hat B]&=i\hbar\{A,B\}

\end{align*}$$

This nicely bridges classical and quantum systems, with the intuition that classical systems are simply derived from the limit of large quantum systems. That is, in the limit of large quantum numbers we have:$$\Huge \langle[\hat A,\hat B]\rangle=i\hbar\{\langle\hat A\rangle,\langle\hat B\rangle\}$$
# Angular momentum:

We start by understanding angular momentum as it appears in classical mechanics, where we have $\underline{L}=\underline{r}\times\underline{p}$ which defines angular momentum component-wise:$$\Huge\begin{align*}
L_1&=yp_z-zp_y\\
L_2&=zp_x-xp_z\\
L_3&=xp_y-yp_x
\end{align*}$$We can use this definition to compute the Poisson brackets $\{L_i,L_j\}$:$$\Huge\begin{align*}
\{L_1,L_2\}&=\{yp_z-zp_y,zp_x-xp_z\}\\
&=\frac{\partial (yp_z-zp_y)}{\partial x}\frac{\partial(zp_x-xp_z)}{\partial p_x}+\dots\\
&=xp_y-yp_x=L_3
\end{align*}$$Then by symmetry we have:$$\Huge \{L_i,L_j\}=\epsilon_{ijk}L_k$$