
Suppose that $\hat x_i |x_1,\dots,x_n\rangle=x_i |x_1,\dots, x_n\rangle$ are [[Generalisation to infinite dimensional Hilbert spaces#Position operator|position eigenstates]] and:$$\Huge [\hat x_i,\hat x_j]=0,\,\,[\hat p_i,\hat p_j]=0,\,\,[\hat x_i,\hat p_j]=i\hbar\delta_{ij}\hat{\mathbb{I}},\,\,\forall i,j$$These are called commutating relations. Take for example the classical non-relativistic Hamiltonian:$$\Huge H=\frac{\underline{p^2}}{2m}+V(\underline{x})\rightarrow\frac{1}{2m}(\hat P_x^2+\hat P_y^2+\hat P_z^2)+V(\hat{\underline{x}})$$where $\hat P_i$ is the [[Generalisation to infinite dimensional Hilbert spaces#Momentum operator|momentum operator]] in the $i$-direction and $\hat{\underline{x}}$ is the position operator. Here we have quantised the system by replacing variables with their corresponding quantum operators. This is not always the case:$$\Huge H=xp\rightarrow H=\hat x\hat p\implies H^\dagger\neq H$$In such case, we can add operators symmetrically to preserve hermiticity:$$\Huge H=xp\rightarrow H=\frac{1}{2}(\hat x\hat p+\hat p\hat x)\implies H^\dagger=H$$However this does not always work, consider $H=p^2x$.

# Schrodinger's wave equation:

Take the classical Hamiltonian described above and consider [[Time evolution of QM states#Schrodinger equation motivation|Schrodinger's equation]]:$$\Huge i\hbar \frac{d}{dt}|\psi\rangle=\hat H |\psi\rangle$$We write this in the $x_i$-basis by multiplying with $\langle \underline{x}|=\langle x,y,z|$:$$\Huge\begin{align*} 
i\hbar \frac{d}{dt} \langle \underline{x}|\psi\rangle&=\langle \underline{x}|\hat H |\psi\rangle\\
&=\langle \underline{x}|\frac{1}{2m}(\hat p_x^2+\hat p_y^2+\hat p_z^2)+V(\hat{\underline{x}})|\psi\rangle\\
&=-\frac{\hbar^2}{2m}\underline{\nabla}^2 \langle \underline{x}|\psi\rangle+V(\underline{x})\langle \underline{x}|\psi\rangle
\end{align*}$$Now we define $\langle \underline{x}|\psi\rangle=\psi(\underline{x})$, which gives us the following in terms of the wave equation:$$\Huge i\hbar \frac{d}{dt}\psi=-\frac{\hbar^2}{2m}\underline{\nabla}^2\psi+V(\underline{x})\psi$$
# [[Time evolution of QM states#Time evolution of expectation values|Ehrenfest's theorem]] revisited:

Recall the statement of Ehrenfest's theorem:$$\Huge \frac{d}{dt}\langle\hat A\rangle=-\frac{i}{\hbar}\langle[\hat A,\hat H]\rangle$$We then ask what this states for $A=\hat x$, the position operator:$$\Huge\begin{align*}
\frac{d}{dt}\langle\hat x\rangle=-\frac{i}{\hbar}\langle[\hat x,\hat H]\rangle
\end{align*}$$We find this by considering the following commutator:$$\Huge\begin{align*}
[\hat x,\hat x^m\hat p^n]&=\hat x^m([\hat x,\hat p]\hat p^{n-1}+\hat p[\hat x,\hat p]\hat p^{n-2}+\dots+\hat p^{n-1}[\hat x,\hat p])\\
&=i\hbar n\hat x^m\hat p^{n-1}\\
&=i\hbar \frac{\partial }{\partial \hat p}(\hat x^m\hat p^n)\\
\implies[\hat x,\hat H]&=i\hbar\frac{\partial H(\hat x,\hat p)}{\partial \hat p}\\
\implies \frac{d}{dt}\langle x\rangle&=-\frac{i}{\hbar}i\hbar\left\langle\frac{\partial H}{\partial \hat p}\right\rangle=\left\langle\frac{\partial H}{\partial \hat p}\right\rangle
\end{align*}$$One can also find a similar formula for the expectation of momentum, together we have:$$\Huge \frac{d\langle\hat x\rangle}{dt}=\left\langle\frac{\partial H}{\partial \hat p}\right\rangle,\,\,\frac{d\langle\hat p\rangle}{dt}=-\left\langle\frac{\partial H}{\partial \hat x}\right\rangle$$