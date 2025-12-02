
In classical mechanics, the simple harmonic oscillator (SHO) has associated Hamiltonian:$$\Huge H=\frac{p^2}{2m}+\frac{m\omega^2 x^2}{2}\rightarrow\frac{\hat p^2}{2m}+\frac{m\omega^2\hat x^2}{2}$$where we have [[Canonical quantisation of classical systems|quantised]] the system by replacing variables $x,p$ with operators $\hat x,\hat p$.


# Positive definite:

We propose that an operator $\hat B$ that is defined as the sum of squares of [[Operators and Measurement|observable operators]] will have positive definite ($\geq0$) expectation value:
> Consider $\hat B=\hat A^2$ where $\hat A=\hat A^\dagger$:$$\Huge\langle\hat B\rangle= \langle \psi|\hat A^2 |\psi\rangle=\langle \psi|\hat A^\dagger\hat A |\psi\rangle=|\hat A |\psi\rangle|^2\geq0$$
> This is clearly also true if $\hat B$ is the sum of the square of many Hermitian operators.

What this means for our SHO is that $\langle\hat H\rangle\geq0$ and therefore all energy eigenvalues are greater than or equal to $0$.

# Ladder operators:

We define the Ladder operator:$$\Huge \hat a=\frac{1}{\sqrt{2m\hbar\omega}}(m\omega\hat x+i\hat p)$$and proceed by rewriting our operators in terms of it:$$\Huge\hat x=\sqrt{\frac{\hbar}{2m\omega}}(\hat a+\hat a^\dagger),\,\,\hat p=-i\sqrt{\frac{\hbar m\omega}{2}}(\hat a-\hat a^\dagger)$$This makes our commutation relation:$$\Huge\begin{align*}
i\hbar=[\hat x,\hat p]&=-\frac{i\hbar}{2}[\hat a+\hat a^\dagger,\hat a-\hat a^\dagger]\\
&=-\frac{i\hbar}{2}(-[\hat a,\hat a^\dagger]+[\hat a^\dagger,\hat a])\\
&=\frac{i\hbar}{2}([\hat a,\hat a^\dagger]+[\hat a,\hat a^\dagger])=i\hbar[\hat a,\hat a^\dagger]\\
\implies[\hat a,\hat a^\dagger]&=1
\end{align*}$$Now we write the Hamiltonian in terms of $\hat a,\hat a^\dagger$:$$\Huge\begin{align*}
H&=\frac{\hat p^2}{2m}+\frac{m\omega^2}{2}\hat x^2\\
&=\frac{\hbar \omega}{4}(-(\hat a-\hat a^\dagger)^2)+\frac{\hbar\omega}{4}(\hat a+\hat a^\dagger)^2\\
&=\frac{\hbar\omega}{4}(-\hat a^2-(\hat a^\dagger)^2+\hat a^2+(\hat a^\dagger)^2+\hat a\hat a^\dagger+\hat a^\dagger\hat a+\hat a\hat a^\dagger+\hat a^\dagger\hat a)\\
&=\frac{\hbar\omega}{2}(\hat a\hat a^\dagger+\hat a^\dagger\hat a)\\
&=\frac{\hbar\omega}{2}(2\hat a^\dagger\hat a+1)=\hbar\omega\left(\hat a^\dagger\hat a+\frac{1}{2}\right)=\hbar\omega\left(\hat N+\frac{1}{2}\right)
\end{align*}$$where $\hat N=\hat a^\dagger\hat a$ is known as the number operator. Therefore we need to solve $\hat N |n\rangle=n |n\rangle$ since then $\hat H |n\rangle=\hbar\omega(\hat N+1/2)|n\rangle$, which means that:$$\Huge E=\hbar\omega(n+1/2)$$
# Number operator and ground state:

This setup allows for us to find $\hat N$ eigenvalues without actually solving for the wavefunction. In order to do so, we note that the commutator between $\hat a,\hat a^\dagger$ and $\hat N$ can be derived as:$$\Huge\begin{align*}
[\hat a,\hat N]&=[\hat a,\hat a^\dagger\hat a]\\
&=\hat a^\dagger[\hat a,\hat a]+[\hat a,\hat a^\dagger]\hat a\\
&=\hat a\\
\implies[\hat a,\hat N]^\dagger&=\hat a^\dagger\\
\implies[\hat N^\dagger,\hat a^\dagger]&=\hat a^\dagger\\
\implies[\hat a^\dagger,\hat N]&=-\hat a^\dagger
\end{align*}$$Using these identities we observe:$$\Huge\begin{align*}
\hat N\hat a |n\rangle&=(\hat N\hat a-\hat a\hat N+\hat a\hat N)|n\rangle\\
&=[\hat N,\hat a]|n\rangle+\hat an |n\rangle\\
&=(n-1)\hat a |N\rangle
\end{align*}$$This shows that $\hat a |n\rangle$ is an eigenvector of $\hat N$ with eigenvalue $n-1$. This implies that $\hat a |n\rangle=c_{n-1}|n-1\rangle$ as there is no degeneracy in one dimension. Thus more generally we can write a whole tower of eigenstates if we know only one of them:$$\Huge \hat a^m |n\rangle=\left(\prod_{i=1}^mc_{n-i}\right)|n-m\rangle$$
We fill find coefficients after we decide where this process needs to stop. As we can always apply $\hat a$ to the lower eigenvalue, it seems to imply that we can keep applying $\hat a$ until eigenvalues of $\hat N$ become negative. However this will contradict out previous finding that eigenvalues of $\hat H$ are non-negative. Therefore there must be some lowest eigenvalue state, known as the ground state $|0\rangle$ which obeys:$$\Huge \hat a |0\rangle=0$$This has associated energy:$$\Huge \hat H |0\rangle=\frac{\hbar\omega}{2}|0\rangle$$
Starting from this ground state, we can find the entire spectrum without ever solving anything. To do this, we note that $\hat a^\dagger$ must raise the energy eigenvalues. All eigenstates of $\hat N$ are therefore found using:$$\Huge |n\rangle=c_n(\hat a^\dagger)^n |0\rangle$$
These $|n\rangle$ form the complete eigenbasis of $\hat H$. We proceed by fixing the constants $c_n$ by demanding unit norm:$$\Huge\begin{align*}
\langle n|n\rangle&=|c_n|^2 \langle 0|\hat a^n(\hat a^\dagger)^n |0\rangle\\
&=|c_n|^2 \langle 0|\hat a^{n-1}\hat a(\hat a^\dagger)^n |0\rangle\\
&=|c_n|^2\langle 0|\hat a^{n-1}((\hat a^\dagger)^n\hat a+[\hat a,(\hat a^\dagger)^n])|0\rangle\\
&=|c_n|^2(\langle 0|\hat a^{n-1}[\hat a,(\hat a^\dagger)^n]|0\rangle)\\
&=|c_n|^2(\langle 0|\hat a^{n-1}\{[\hat a,\hat a^\dagger](\hat a^\dagger)^{n-1}+\hat a^\dagger[\hat a,\hat a^\dagger](\hat a^\dagger)^{n-2}+\dots\} |0\rangle)\\
&=|c_n|^2(n \langle 0|\hat a^{n-1}(\hat a^\dagger)^{n-1}|0\rangle)\\
&=n|c_n|^2\langle 0|\hat a^{n-1}(\hat a^\dagger)^{n-1}|0\rangle\\
&=\vdots\\
&=n!|c_n|^2\\
\implies c_n&=\frac{1}{\sqrt{n!}}\\
\implies |n\rangle&=\frac{1}{\sqrt{n!}}(\hat a^\dagger)^n |0\rangle
\end{align*}$$
Finally, we can confirm that energy eigenvalues are are given by what we saw previously:$$\Huge\begin{align*}
\hat N |n\rangle&=\hat a^\dagger\hat ac_n(\hat a^\dagger)^n |0\rangle\\
&=c_n\hat a^\dagger((\hat a^\dagger)^n\hat a+[\hat a,(\hat a^\dagger)^n])|0\rangle\\
&=c_n\hat a^\dagger\{[\hat a,\hat a^\dagger](\hat a^\dagger)^{n-1}+\hat a^\dagger[\hat a,\hat a^\dagger](\hat a^\dagger)^{n-2}+\dots\} |0\rangle\\
&=c_n\hat a^\dagger n(\hat a^\dagger)^{n-1}|0\rangle\\
&=n |n\rangle\\
\implies\hat H |n\rangle&=\hbar\omega\left(n+\frac{1}{2}\right)|n\rangle
\end{align*}$$This is why $\hat N$ is called the number operator, as it counts how many raising operations have been performed on the ground state.

# The Fock eigenbasis:

We now aim to find what these wavefunctions actually look like as functions of $x$. We derive them by first determining the ground state wavefunction:

## Ground state:
The ground state $|0\rangle$ is defined as the state that is annihilated by the lowering operator $\hat a$. Expressing this operator in terms of position and momentum gives:$$\Huge \hat a=\frac{1}{\sqrt{2\hbar m\omega}}(m\omega\hat x+i\hat p)$$so the position-space representation ($\phi_0(x)=\langle x|0\rangle$) is:$$\Huge \left(\frac{1}{\sqrt{2\hbar m\omega}}\right)(m\omega x+\hbar\partial_x)\phi_0(x)=0$$This is a solvable differential equation, which has solution:$$\Huge \phi_0(x)=Ae^{-\frac{m\omega x^2}{2\hbar}}$$We must normalise this:$$\Huge 1=\int_{-\infty}^\infty|\phi_0(x)|^2dx=|A|^2\int_{-\infty}^\infty e^{-\frac{m\omega}{\hbar}x^2}dx$$Evaluating the Gaussian integral gives:$$\Huge |A|^2\sqrt{\frac{\pi\hbar}{m\omega}}=1\implies|A|=\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}$$Therefore we define the SHO groundstate as:$$\Huge \phi_0(x)=\left(\frac{m\omega}{\pi\hbar }\right)^{1/4}e^{-\frac{m\omega x^2}{2\hbar}}$$
## Excited states:
Next we find the excited states $|n\rangle$, which are generated by applying the raising operator to the ground state. The position representation of $|n\rangle$ denoted as $\phi_n(x)=\langle x|n\rangle$ can be derived by considering the effect of $\hat a^\dagger$ as a derivative operator:$$\Huge \phi_n(x)=\frac{1}{\sqrt{n!}}\left(\frac{1}{\sqrt{2\hbar m\omega}}(-\hbar\partial_x+m\omega x)\right)^n\phi_0(x)$$The resulting functions are given in terms of the Hermite polynomials $H_n(x)$:$$\Huge \phi_n(x)=\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\frac{1}{\sqrt{2^nn!}}H_n\left(\sqrt{\frac{m\omega}{\hbar}}x\right)e^{-\frac{m\omega x^2}{2\hbar}}$$where $H_n(x)$ is the $n$-th Hermite polynomial.

It is straightforward to find Hermite polynomials from the recurrence relations that arises by inspecting the action of the derivative operator on polynomials:$$\Huge H_n(x)=2xH_{n-1}(x)-2(n-1)H_{n-2}(x)$$with the initial condition $H_0(x)=1$.

# General solutions using the Fock basis:

Our method for finding the time evolved wavefunction will be as follows:![[Quantum S.H.O. 2025-12-02 20.16.54.excalidraw]]
As we can see, there are many similarities to solving PDEs using the [[Fourier transform]]. Suppose that the state begins at time $t=0$ with a wavefunction expressed as some function of $x$:$$\Huge \langle x|\psi(0)\rangle=\psi_0(x)$$
As we have seen, the energy eigenstates of the SHO form a complete basis thanks to the property of completeness of eigenvalues for Hermitian Operators. Therefore the Fock states form a complete orthonormal eigenbasis in which we can express our wavefunction:$$\Huge \langle x|\psi(0)\rangle=\sum_n \langle x|n\rangle \langle n|\psi(0)\rangle$$Here, $\langle n|\psi(0)\rangle$ are simply the coefficients of the energy eigenstates in the wavefunction, while the energy eigenstates evolve with time as we know:$$\Huge\begin{align*}
\langle x|n\rangle&\rightarrow e^{-iE_nt/\hbar}\langle x|n\rangle\\
&=e^{-i\omega(n+1/2)t}\langle x|n\rangle\\
\implies \langle x|\psi(t)\rangle&=\sum_ne^{-i\omega(n+1/2)t}\langle x|n\rangle \langle n|\psi(0)\rangle
\end{align*}$$
All that remains to do is to find the coefficients. However for this, we simply insert an identity:$$\Huge \langle n|\psi(0)\rangle=\int \langle n|x'\rangle \langle x'|\psi(0)\rangle dx'$$We therefore have:$$\Huge \langle x|\psi(t)\rangle=\sum_ne^{-i\omega(n+1/2)t}\phi_n(x)\int \langle n|x'\rangle \langle x'|\psi(0)\rangle dx'$$This is exactly our final result. We can write this in terms of regular functions as:$$\Huge \psi(x,t)=\sum_ne^{-i\omega(n+1/2)t}\phi_n(x)\int\phi_n^*(x')\psi_0(x')dx'$$
We can think of this as simply an expansion in the Fock basis with time dependent coefficients:$$\Huge \psi(x,t)=\sum_nc_n(t)\phi_n(x)$$with:$$\Huge\begin{align*}
c_n(t)&=\sum_ne^{-i\omega(n+1/2)t}c_n(0)\\
c_n(0)&=\int \phi_n^*(x')\psi_0(x')dx'
\end{align*}$$Note that all of this is entirely general, we are yet to perform the integral depending on the initial form of the wave function. As we are working in one dimension, it is quite easy to do numerically. Before we look at an example, note that when $t=0$ we indeed have:$$\Huge\begin{align*}
\psi(x,0)&=\sum_n\int\phi_n(x)\phi_n^*(x')\psi_-(x')dx'\\
&=\int\delta(x-x')\psi_0(x')dx'=\psi_0(x)
\end{align*}$$
## Gaussian wave-function example:
