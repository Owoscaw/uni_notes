# Early principles:

There are four initially guiding principles:
> Quantum states in Hilbert space:
> > The first principle states that the quantum state of a system is represented by a vector in a [[QM linear algebra#Hilbert space|complex Hilbert space]]:
> > >A quantum state $|\psi\rangle$ is a vector in a complex Hilbert space $\mathcal{H}$.
> > >The Hilbert space is equipped with an [[Inner product spaces|inner product]] $\langle \phi|\psi\rangle$ which allows us to calculate probability and expectation values.
> > >The state vector $|\psi\rangle$ contains all information about the quantum system.
> > >Any linear combination of allowed states is also an allowed state.
> Observables as Hermitian operators:
> > Physical observables are represented by Hermitian operators acting on the Hilbert space:
> > > An observable $A$ is represented by a Hermitian operator $\hat A$.
> > > Hermitian operators have real eigenvalues, corresponding to possible measurement outcomes.
> > > The eigenvectors of $\hat A$ form a complete orthonormal basis for the Hilbert space.
> > > The expectation value of an observable in a state $|\psi\rangle$ is given by $\langle A\rangle=\langle \psi|\hat A |\psi\rangle$.
> Measurement and probability:
> > Measurement of an observable yields one of its eigenvalues, with a probability determined by the projection of the state onto the corresponding eigenspace:
> > > For an observable $\hat A$ with eigenvalues $a_i$ and corresponding eigenvectors $|a_i\rangle$, the probability of measuring $a_i$ is:$$\Huge P(a_i)=|\langle a_i|\psi\rangle|^2=\langle \psi|\hat P_{a_i}|\psi\rangle$$where $\hat P_{a_i}=|a_i\rangle \langle a_i|$ is the projection operator onto the eigenspace of $a_i$. This is often referred to as the Born rule.
> > > The measurement process causes the wavefunction to collapse into the measured eigenstate.
> State normalisation after measurement:
> > After measurement, the state of the system collapses to the eigenstate corresponding to the measured eigenvalue, and this new state must be normalised:
> > > If outcome $a_i$ is measured, the state immediately after measurement is:$$\Huge |\psi'\rangle=\frac{\hat P_{a_i}|\psi\rangle}{\sqrt{\langle \psi|\hat P_{a_i}|\psi\rangle}}$$
> > > This ensures that the new state $|\psi'\rangle$ is normalised.
> > > Subsequent measurements of the same observable will yield the same result with certainty.

# Expectation values:

We can also derive the formula for the expectation value of an operator:$$\Huge\langle\hat O\rangle=\sum_{i=1}^mw_iP(w_i)=\sum_{i=1}^mw_i\langle \psi|\hat P_{w_i}|\psi\rangle=\langle \psi|\sum_{i=1}^mw_i\hat P_{w_i}|\psi\rangle=\langle \psi|\hat O\|\psi\rangle$$This has the exact same interpretation as the classical expectation formula as classical probability. More generally:$$\Huge \langle\hat f(\hat O)\rangle=\langle \psi|\hat f\hat O |\psi\rangle$$It is important to note that measurements cannot completely fix a quantum mechanical state.


## Quantum coin:
Take for example the quantum coin, $|\psi\rangle=a |H\rangle+b |T\rangle$. Suppose we make a lot of measurements and find the probabilities of heads and tails are $h,t$ respectively. Then:$$\Huge\begin{align*}
P(H)&=|a|^2=h\\
P(T)&=|b|^2=t\\
\implies a&=h^{1/2}e^{i\phi_1t}\\
b&=t^{1/2}e^{i\phi_2t},\,\,\phi_1,\phi_2\in\Re\\
\implies |\psi\rangle&=e^{i\phi_1}(h^\frac{1}{2}|H\rangle+t^{1/2}e^{i(\phi_2-\phi_1)}|T\rangle)
\end{align*}$$Note that the overall phase is not important but relative phase ($\phi_2-\phi_1$) always remains unfixed. Similarly to classical probability, we can ask of the expectation value for the "Head-ness". Define the operator $\hat\Omega_{\text{head}}$ for which $|H\rangle$ and $|T\rangle$ have eigenvalues $\pm1$. Using the definition immediately gives:$$\Huge\langle\hat\Omega_\text{head}\rangle=h-t$$Note that we can alternatively use the matrix form:$$\Huge\Omega_\text{head}=\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$$Which gives the calculation:$$\Huge\langle\hat\Omega_\text{head}\rangle=(a^*,b^*)\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}\begin{pmatrix}a \\ b\end{pmatrix}=|a|^2-|b|^2=h-t$$as required. Now consider two operators "Toss" $\hat A$ and "Swap" $\hat\tau_1$ with the following matrices:$$\Huge A=\frac{1}{\sqrt 2}\begin{pmatrix}1 & i \\ -i & 1\end{pmatrix},\,\,\tau_1=\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$$The toss operator $\hat A$ mixes $|H\rangle$ and $|T\rangle$ to create a state of equal probability from a pure $|H\rangle$ or $|T\rangle$ state, while the swap operator $\hat\tau_1$ swaps $|H\rangle$ and $|T\rangle$:
> For the toss operator $\hat A$ we are solving:$$\Huge\frac{1}{\sqrt 2}\begin{pmatrix}1 & i \\ -i & 1\end{pmatrix}\begin{pmatrix}a \\ b\end{pmatrix}=\lambda\begin{pmatrix}a \\ b\end{pmatrix}$$which yields the eigenvalues $\lambda_1=2,\lambda_2=0$. This leads to the following normalised eigenvectors:$$\Huge |\psi_1\rangle=\frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -i\end{pmatrix},\,\,|\psi_2\rangle=\frac{1}{\sqrt 2}\begin{pmatrix}1 \\ i\end{pmatrix}$$
> Then for the swap operator $\hat\tau_1$:$$\Huge\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}\begin{pmatrix}a \\ b\end{pmatrix}=\lambda\begin{pmatrix}a \\ b\end{pmatrix}$$which yields the eigenvalues $\lambda_1=1,\lambda_2=-1$. This leads to the normalised eigenvectors:$$\Huge |\phi_1\rangle=\frac{1}{\sqrt 2}\begin{pmatrix}1 \\ 1\end{pmatrix},\,\,|\phi_2\rangle=\frac{1}{\sqrt 2}\begin{pmatrix}1 \\ -1\end{pmatrix}$$

Now consider the commutator $[\hat A,\hat\tau_1]$:$$\Huge\begin{align*}
\hat A\hat\tau_1&=\frac{1}{\sqrt 2}\begin{pmatrix}1 & i\\
-i & 1\end{pmatrix}\cdot\frac{1}{\sqrt 2}\begin{pmatrix}0 & 1\\
1 & 0\end{pmatrix}=\frac{1}{2}\begin{pmatrix}i & 1\\
1 & -i\end{pmatrix}\\
\hat \tau_1\hat A&=\frac{1}{\sqrt 2}\begin{pmatrix}0 & 1\\
1 & 0\end{pmatrix}\cdot\frac{1}{\sqrt 2}\begin{pmatrix}1 & i\\
-i & 1\end{pmatrix}=\frac{1}{2}\begin{pmatrix}-i & 1\\
1 & i\end{pmatrix}\\
\implies[\hat A,\hat\tau_1]&=\hat A\hat\tau_1-\hat\tau_1\hat A\\
&=\frac{1}{2}\begin{pmatrix}i & 1\\
1 & -i\end{pmatrix}-\frac{1}{2}\begin{pmatrix}-i & 1\\
1 & i\end{pmatrix}\\
&=\frac{1}{2}\begin{pmatrix}2i & 0\\
0 & 2i\end{pmatrix}=i\begin{pmatrix}1 & 0\\
0 & -1\end{pmatrix}=i\hat\Omega_\text{head}
\end{align*}$$
It is interesting to compute the expectation of the "Head-ness" operator $\hat\Omega_\text{head}$ for the eigenstates of $\hat A,\hat\tau_1$:
> Considering the eigenstates associated with $\hat A$, we proceed with the eigenstate $|\psi_1\rangle=\frac{1}{\sqrt 2}\begin{pmatrix}1 & -i\end{pmatrix}$:$$\Huge\langle\hat\Omega_\text{head}\rangle_{\psi_1}=\langle \psi_1|\hat\Omega_\text{head}|\psi_1\rangle=\frac{1}{\sqrt 2}(1,i)\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}\frac{1}{\sqrt 2}\begin{pmatrix}1 \\ -i\end{pmatrix}=0$$Similarly the eigenstate $|\psi_2\rangle=\frac{1}{\sqrt 2}\begin{pmatrix}1 \\ i\end{pmatrix}$ gives $\langle\hat\Omega_\text{head}\rangle_{\psi_2}=0$.
> Considering the eigenstates associated with $\hat\tau_1$, we get the same results as $\hat A$.

Although the overall phase $\phi_1$ in our quantum coin was not measurable, relative phase $\phi_2-\phi_1$ can actually make a difference. Consider the expectation value of the "imaginary swap" observable $\hat\tau_2$ with defining matrix:$$\Huge\tau_2=\begin{pmatrix}0 & i \\ -i & 0\end{pmatrix}=i |H\rangle \langle T|-i |T\rangle \langle H|$$Which we can do as follows:$$\Huge\begin{align*}
\langle\hat\tau_2\rangle&=(\langle H|a^*+\langle T|b^*)(i |H\rangle \langle T|-i |T\rangle \langle H|)(a |H\rangle+b |T\rangle)\\
&=(ia^* \langle T|-ib^* \langle H|)(a |H\rangle+b |T\rangle)\\
&=i(a^*b \langle T|T\rangle-b^*a \langle H|H\rangle)\\
&=2\sqrt{ht}\sin(\phi_1-\phi_2)
\end{align*}$$If we specialise to "toss" and "swap" eigenstates, they can be written as:$$\Huge\begin{align*}
|\text{toss}_{2,0}\rangle&=\frac{1}{\sqrt 2}(|H\rangle+e^{\mp i\pi/2}|T\rangle)\\
|\text{swap}_1\rangle&=\frac{1}{\sqrt 2}(|H\rangle+e^{i0}|T\rangle)\\
|\text{swap}_{-1}\rangle&=\frac{1}{\sqrt 2}(|H\rangle+e^{i\pi}|T\rangle)
\end{align*}$$Hence we have $\phi_1-\phi_2=\mp\frac{\pi}{2}$ for the toss eigenstates and $0,\pi$ for the swap eigenstates, so we have:$$\Huge\langle\hat\tau_2\rangle=2\sqrt{ht}\sin(\phi_1-\phi_2)=\mp1$$for the toss eigenstates and $0$ for the swap eigenstates. That is to say, after making a swap measurement we have an expectation $\langle\hat\tau_2\rangle=0$. Therefore we can prepare a given state with fixed relative phase by measuring an observable that will fix it in that state. Then we can compute expectation values of any other observables we may wish to measure.

This effect is the same as the interference phenomenon we discussed in the introduction and is the source of time evolution behaviors.