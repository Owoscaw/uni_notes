
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
# Coherent states:

Coherent states are, in a sense, the most classical-like lump we can build in the SHO because they are lumps that do not "wobble". They maintain their shape as they oscillate in the potential. It turns out that they obey:$$\Huge \hat a |\alpha\rangle=\alpha |\alpha\rangle$$such that they are eigenstates of $\hat a$ with $\alpha$ being its complex and time-dependent eigenvalue. We will explore how such a state evolves in time. According to Schrodinger, the time evolved state is:$$\Huge |\alpha,t\rangle=e^{-i\hat Ht/\hbar}|\alpha\rangle$$But we know that $\hat H=\hbar\omega(\hat a^\dagger\hat a+1/2)$ and that:$$\Huge [\hat a,\hat a^\dagger\hat a]=[\hat a,\hat a^\dagger]\hat a+\hat a^\dagger[\hat a,\hat a]=\hat a$$Using this equation on $\hat H$ we have $\hat a\hat H=(\hat H+\hbar\omega)\hat a$, and iterating gives $\hat a\hat H^n=(\hat H+\hbar\omega)^n\hat a$. Hence we may pass $\hat a$ through the Schrodinger evolution factor as:$$\Huge\begin{align*}
\hat ae^{-i\hat Ht/\hbar}&=e^{-i(\hat H+\hbar\omega)t/\hbar}\hat a\\
&=e^{-i\hat Ht/\hbar}e^{-i\omega t}\hat a
\end{align*}$$Now let us see what the $\hat a$ eigenvalue of the time-evolves state is:$$\Huge\begin{align*}
\hat a |\alpha,t\rangle&=\hat ae^{-i\hat Ht/\hbar}|\alpha\rangle\\
&=e^{-i\hat Ht/\hbar}e^{-i\omega t}\hat a |\alpha\rangle\\
&=e^{-i\hat Ht/\hbar}e^{-i\omega t}\alpha |\alpha\rangle\\
&=e^{-i\omega t}\alpha |\alpha,t\rangle
\end{align*}$$Therefore the state evolves in time simply by acquiring a time dependent phase. This is an interesting observation as it is similar to what we see with energy eigenstates. We can encapsulate this by promoting $\alpha$ itself to a function of time:$$\Huge \alpha(t)=e^{-i\omega t}\alpha_0$$WLOG we assume $\alpha(0)=\alpha_0$ is real and we can absorb the phase on it into a redefinition of where we set $t=0$.

This is the first important observation and makes this kind of state rather unusual. It means that we can derive the time-evolving wave-function by simply solving a single eigenvalue problem:$$\Huge \hat a |\alpha\rangle=\alpha(t)|\alpha\rangle$$with all time-dependence incorporated in its time-dependent eigenvalue $\underline{\alpha}$. This is what makes such states unique.

We can find the form of these by solving its defining equation:$$\Huge \frac{1}{\sqrt{2m\omega\hbar}}(m\omega x+\hbar\partial_x)\psi(x)=\alpha(t)\psi(x)$$The solution is relatively straightforward by setting $z=\sqrt{m\omega/\hbar x}$. We then have:$$\Huge \psi_z+z\psi=\sqrt 2\alpha\psi$$which is rewritten with an integrating factor as:$$\Huge \frac{\partial }{\partial z}(\psi e^{z^2/2})=\sqrt 2\alpha\psi e^{z^2/2}\implies\psi=Ce^{\sqrt 2\alpha z-z^2/2}$$where $C$ is a constant which can also be time dependent. We can find $C$ by imposing unit norm on the wavefunction. Recalling that $\alpha$ is a complex function of time given by $\alpha=\alpha_0e^{i\omega t}$ , the norm requirement becomes:$$\Huge\begin{align*}
1&=\int|\psi|^2dx\\
&=\sqrt{\frac{\hbar}{m\omega}}|C|^2\int e^{2\sqrt 2\Re(\alpha)-z^2}dz\\
&=\sqrt{\frac{\hbar}{m\omega}}|C|^2e^{-2\Re(\alpha)^2}\int e^{(\sqrt 2\Re(\alpha)-z)^2}dz\\
&=\sqrt{\frac{\pi\hbar}{m\omega}}|C|^2e^{-2\Re(\alpha)^2}
\end{align*}$$Hence we see that $C$ is time dependent and:$$\Huge\begin{align*}
\psi&=e^{\Re(\alpha)^2}\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{\sqrt 2\alpha z-z^2/2+i\theta(t)}\\
&=\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-(\sqrt 2\Re(\alpha)-z)^2/2+i\theta(t)+i\sqrt 2\Im(\alpha)z}
\end{align*}$$for some phase $\theta(t)$ which is allowed in $C$. Thus the answer becomes:$$\Huge \psi(x,t)=\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-\frac{m\omega}{2\hbar}(x-x_c(t))^2+i\sqrt\frac{2\hbar}{m\omega}\alpha_0x\sin(\omega t)+i\theta(t)}$$with a density profile:$$\Huge |\psi(x,t)|=\left(\frac{m\omega}{\pi\hbar}\right)^{1/2}e^{-\frac{m\omega}{\hbar}(x-x_c(t))^2}$$This is the density profile of the displaced SHO groundstate, oscillating around the classical solution with:$$\Huge x_c(t)=\sqrt\frac{2\hbar}{m\omega}\alpha_0\cos(\omega t)$$that is with maximum displacement $x_0=\sqrt\frac{2\hbar}{m\omega}\alpha_0$. Note that if $\alpha_0=0$, then the wavefunction actually becomes the SHO groundstate.

We knew that the coherent state had to be an eigenstate of $\hat a$ as we can show that such a state saturates the Heisenberg uncertainty principle. If this is the case, then any perturbation of the profile could only ever increase $\Delta x\Delta p$. It is possible to unpick these properties of $\hat a$ eigenstates without ever solving for the wavefunction profile itself. To see this we return to the starting assumption about the wavefunction, namely that it obeys:$$\Huge\hat a |\alpha\rangle=\alpha(t)|\alpha\rangle$$We can now evaluate the expectation of position for the state $|\alpha(t)\rangle$ using the relation between $\hat x,\hat a$:$$\Huge \hat x=\sqrt{\frac{\hbar}{2m\omega}}(\hat a+\hat a^\dagger),\,\,\hat p=-i\sqrt{\frac{m\omega\hbar}{2}}(\hat a-\hat a^\dagger)$$This gives:$$\Huge\begin{align*}
\langle\hat x\rangle&=\langle \alpha(t)|\hat x |\alpha(t)\rangle\\
&=\sqrt{\frac{\hbar}{2m\omega}}\langle \alpha(t)|\hat a+\hat a^\dagger |\alpha\rangle\\
&=\sqrt{\frac{\hbar}{2m\omega}}\langle \alpha(t)|\alpha(t)+\alpha(t)^*|\alpha\rangle\\
&=\sqrt{\frac{\hbar}{2m\omega}}(\alpha(t)+\alpha(t)^*)\\
&=\sqrt{\frac{2\hbar}{m\omega}}\alpha_0\cos(\omega t)
\end{align*}$$where we must at to the left or right with $\hat a^\dagger$ and $\hat a$ respectively, which is just that of the classical oscillator if we identify $x_0=\sqrt{\frac{2\hbar}{m\omega}}\alpha_0$. So now we calculate $\Delta x^2=\langle x^2\rangle-\langle\hat x\rangle^2$. We proceed:$$\Huge\begin{align*}
\langle\hat x^2\rangle&=\langle \alpha(t)|\hat x |\alpha(t)\rangle\\
&=\frac{\hbar}{2m\omega}\langle \alpha(t)|\hat a^2+\hat a^{\dagger2}+\hat a\hat a^\dagger+\hat a^\dagger\hat a |\alpha(t)\rangle\\
&=\frac{\hbar}{2m\omega}\langle \alpha(t)|\hat a^2+\hat a^{\dagger2}+[\hat a,\hat a^\dagger]+2\hat a^\dagger\hat a |\alpha(t)\rangle\\
&=\frac{\hbar}{2m\omega}\langle \alpha(t)|\hat a^2+\hat a^{\dagger2}+1+2\hat a^\dagger\hat a |\alpha(t)\rangle\\
&=\frac{\hbar}{2m\omega}((\alpha(t)+\alpha(t)^*)^2+1)\\
&=\frac{2\hbar}{m\omega}(\alpha_0^2\cos^2(\omega t)+1/4)\\
\implies\Delta x^2&=\frac{2\hbar}{m\omega}((\alpha_0^2\cos^2(\omega t)+1/4)-\alpha_0^2\cos^2(\omega t))\\
&=\frac{\hbar}{2m\omega}
\end{align*}$$Hence we find that the spread in our Gaussian is constant. We see that it comes from the fact that $\hat a,\hat a^\dagger$ operators in $\hat x$ reduced trivially in the eigenstate. Now we do the same to momentum:$$\Huge\begin{align*}
\langle\hat p\rangle&=-i\sqrt{\frac{m\omega\hbar}{2}}\langle \alpha|\hat a-\hat a^\dagger |\alpha\rangle\\
&=-i\sqrt{\frac{m\omega\hbar}{2}}\langle \alpha|\alpha-\alpha^*|\alpha\rangle\\
&=-2\sqrt{2m\omega\hbar}\alpha_0\sin(\omega t)
\end{align*}$$Note that Ehrenfest dictates this obeys $\langle\hat p\rangle=m\frac{d\langle\hat x\rangle}{dt}$. We proceed:$$\Huge\begin{align*}
\langle\hat p^2\rangle&=-\frac{m\omega\hbar}{2}\langle \alpha|(\hat a-\hat a^\dagger)^2|\alpha\rangle\\
&=-\frac{m\omega\hbar}{2}\langle \alpha|\hat a^2+\hat a^{\dagger2}-\hat a\hat a^\dagger-\hat a^\dagger\hat a |\alpha\rangle\\
&=-\frac{m\omega\hbar}{2}\langle \alpha|\hat a^2+\hat a^{\dagger2}-[\hat a,\hat a^\dagger]-2\hat a^\dagger\hat a |\alpha\rangle\\
&=-\frac{m\omega\hbar}{2}\langle \alpha|\hat a^2+\hat a^{\dagger2}-1-2\hat a^\dagger\hat a |\alpha\rangle\\
&=-\frac{m\omega\hbar}{2}\langle \alpha|(\alpha-\alpha^*)^2-1|\alpha\rangle\\
&=2m\omega\hbar\alpha_0^2\sin^2(\omega t)+\frac{m\omega\hbar}{2}\\
\implies\Delta p^2&=\frac{m\omega\hbar}{2}
\end{align*}$$Hence we saturate the uncertainty principle, the defining property of a coherent state.

It is tempting to think we can make the state infinitely classical by taking $m\to\infty$. However the state is not really made more classical as while $\Delta x\to0$ we have $\Delta p\to\infty$, called squeezing. The fact we can contemplate this limit is disconcerting as one imagines that a large $\Delta p$ must mean that the state will "fly off" somewhere. This is not the correct interpretation, in fact it means that the state contains all momentum eigenstates, the outcome would be very uncertain. Until that moment, the wavefunction continues to evolve in this coherent way.

Another interesting expectation value is the energy. Using our above results we find:$$\Huge\begin{align*}
\langle\hat H\rangle&=\left\langle\frac{\hat p^2}{2m}+\frac{m\omega^2}{2}\hat x^2\right\rangle\\
&=\frac{1}{2m}\langle\hat p^2\rangle+\frac{m\omega^2}{2}\langle\hat x^2\rangle\\
&=\omega\hbar\alpha(0)^2\sin^2(\omega t)+\frac{\omega\hbar}{4}+\hbar\omega\alpha(0)^2+\omega\hbar\alpha(0)^2\cos^2(\omega t)+\frac{\omega\hbar}{4}\\
&=\omega\hbar\alpha(0)^2+\frac{\hbar\omega}{2}\\
&=\frac{m\omega^2}{2}x_0^2+\frac{\hbar\omega}{2}
\end{align*}$$That is to say, the zero-point energy plus classical energy is the expectation of the energy operator.

# The $2D$ Isotropic SHO:
Extending to two dimensions we have:$$\Huge\begin{align*}
\hat H&=\frac{\hat p_x^2+\hat p_y^2}{2m}+\frac{1}{2}m\omega^2(\hat x^2+\hat y^2)\\
&=\frac{\hat p_x^2}{2m}+\frac{1}{2}m\omega^2\hat x^2+\frac{\hat p_y^2}{2m}+\frac{1}{2}m\omega^2\hat y^2\\
&=\hat H_x+\hat H_y\\
[\hat x,\hat y]&=[\hat p_x,\hat p_y]=[\hat p_x,\hat y]=[\hat p_y,\hat x]=0\\
[\hat x,\hat p_x]&=[\hat y,\hat p_y]=i\hbar\\
[\hat H_x,\hat H_y]&=0
\end{align*}$$The last equation suggests that we can diagonalise simultaneously wrt $\hat H_x,\hat H_y$, so we label the eigenbasis of $\hat H$ with two integers $n_x,n_y$ ang define the corresponding creation-annihilation operators:$$\Huge\begin{align*}
\hat a_x&=\frac{1}{\sqrt{2\hbar m\omega}}(m\omega\hat x+ip_x)\\
\hat a_y&=\frac{1}{\sqrt{2\hbar m\omega}}(m\omega\hat y+ip_y)\\
[\hat a_x,\hat a_x^\dagger]&=[\hat a_y,\hat a_y^\dagger]=1\\
[\hat a_x,\hat a_y]&=[\hat a_x^\dagger,\hat a_y]=0
\end{align*}$$Our new ground state $|0,0\rangle$ now satisfies:$$\Huge \hat a_x |0,0\rangle=\hat a_y |0,0\rangle=0$$Our general eigenvector will have following form and corresponding eigenvalue:$$\Huge\begin{align*}
|n_x,n_y\rangle&=\frac{1}{\sqrt{n_x!n_y!}}(\hat a_x^\dagger)^{n_x}(\hat a_y^\dagger)^{n_y}|0,0\rangle\\
\hat H |x_n,n_y\rangle&=\hbar\omega(n_x+n_y+1)|n_x,n_y\rangle
\end{align*}$$Showing that the $2D$ oscillator is degenerate.

## The Fermionic SHO:
The SHO we considered before are "Bosonic", meaning that we can add as many "quanta" as we desire by acting with $\hat a^\dagger$ on the ground state. This is different from the fermionic case, where we must obey Pauli's Exclusion Principle. This principle dictates that no two fermionic quanta can occupy the same state. 

The Hamiltonian for this system is then:$$\Huge \begin{align*}
\hat H&=\hbar\omega\hat b^\dagger\hat b\\
\{\hat b^\dagger,\hat b\}&=\hat b^\dagger\hat b+\hat b\hat b^\dagger=1\\
\{\hat b^\dagger,\hat b^\dagger\}&=\{\hat b,\hat b\}=0
\end{align*}$$Note that this implies:$$\Huge \{\hat b^\dagger,\hat b^\dagger\}=0\iff2\hat b^\dagger\hat b^\dagger=0\iff(\hat b^\dagger)^2=0$$Now we let $\hat H=\hbar\omega\hat N$, that is define $\hat N=\hat b^\dagger\hat b$ and observe $\hat N^2$:$$\Huge\begin{align*}
\hat N^2&=\hat b^\dagger\hat b\hat b^\dagger\hat b\\
&=\hat b^\dagger(\{\hat b,\hat b^\dagger\}-\hat b^\dagger\hat b)\hat b\\
&=\hat b^\dagger(1-\hat b^\dagger\hat b)\hat b\\
&=\hat b^\dagger\hat b-(\hat b^\dagger)^2\hat b^2\\
&=\hat b^\dagger\hat b=\hat N
\end{align*}$$Therefore the eigenvalues of $\hat N$ are $0$ or $1$ since:$$\Huge \begin{align*}
\hat N |n\rangle&=n |n\rangle\\
\hat N^2|n\rangle&=n\hat N |n\rangle\\
&=n^2|n\rangle\\
\implies n^2&=n\\
\implies n&=0\text{ or }1
\end{align*}$$Therefore the eigenvalues of $\hat H$ are either $0$ or $\hbar\omega$. This exactly embodies Pauli's exclusion principle as it forces different states to have different quanta. Note that in principle, we could have degeneracy (more than one state with $\hat N |0,s\rangle=0$ with $s=0,1,\dots$). We assume non-degeneracy to simplify the system:$$\Huge \begin{align*}
\hat N |0\rangle&=0\\
\iff\hat b^\dagger\hat b |0\rangle&=0\\
\implies \langle 0|\hat b^\dagger\hat b |0\rangle&=0\\
\implies \hat b |0\rangle&=0
\end{align*}$$That is, $|0\rangle$ is an eigenvector of $\hat b$ with eigenvalue $0$.$$\Huge\begin{align*}
\hat N\hat b^\dagger |0\rangle&=\hat b^\dagger\hat b\hat b^\dagger |0\rangle\\
&=\hat b^\dagger(\{\hat b,\hat b^\dagger\}-\hat b^\dagger\hat b)|0\rangle\\
&=1\cdot\hat b^\dagger |0\rangle\\
\implies |1\rangle&=c\hat b^\dagger |0\rangle\\
\implies \langle 1|1\rangle&=|c|^2\langle 0|\hat b\hat b^\dagger |0\rangle\\
&=|c|^2\langle 0|\{\hat b,\hat b^\dagger\}-\hat b^\dagger\hat b |0\rangle\\
&=|c|^2 \langle 0|0\rangle\\
&=|c|^2\\
\implies c&=1
\end{align*}$$It only remains to check $\hat b |1\rangle$ and $\hat b^\dagger |1\rangle$ to complete the system:$$\Huge\begin{align*}
\hat b |1\rangle&=\hat b\hat b^\dagger |0\rangle\\
&=(\{\hat b,\hat b^\dagger\}-\hat b^\dagger\hat b)|0\rangle\\
&=|0\rangle\\
\hat b^\dagger |1\rangle&=(\hat b^\dagger)^2|0\rangle\\
&=0
\end{align*}$$