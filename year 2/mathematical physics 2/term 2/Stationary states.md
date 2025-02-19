
We have the [[Schrodinger's equation|Schrodinger equation]] in explicit time-dependent form:$$\Huge i\hbar\frac{\partial \psi(x,t)}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\psi(x,t)}{\partial x^2}+V(x)\psi(x,t)$$We aim to give a unique solution for [[Wave function|$\psi$]] given an initial condition $\psi(x,0)$ using the method of separation of variables. We therefore assume:$$\Huge \psi(x,t)=\phi(x)T(t)$$which gives the following when substituted into Schrodinger's equation:$$\Huge i\hbar\frac{1}{T(t)}\frac{\partial T(t)}{\partial t}=-\frac{\hbar^2}{2m}\frac{1}{\phi(x)}\frac{\partial^2\phi(x)}{\partial x^2}+V(x)$$Now both sides of the equation only contain either $x$ or $t$, so each must be constant. That is to say:$$\Huge\begin{align}
i\hbar\frac{1}{T(t)}\frac{d T(t)}{dt}&=E\\
-\frac{\hbar^2}{2m}\frac{1}{\phi(x)}\frac{d^2\phi(x)}{dx^2}+V(x)&=E
\end{align}$$Note that we have assumed $V$ is time independent. The first equation has immediate solution:$$\Huge T(t)=e^{-iEt/\hbar}$$up to normalisation. The second equation states that $\phi(x)$ is an eigenfunction of the [[Schrodinger's equation#Hamiltonian operator|Hamiltonian operator]] $\hat H$ with corresponding eigenvalue $E$:$$\Huge \hat H\phi(x)=E\phi(x)$$Using these, we can see that:
> The probability density for position is:$$\Huge P(x,t)=|\psi(x,t)|^2=|\phi(x)e^{-iEt/\hbar}|^2=|\phi(x)|^2$$
> The probability to measure $E$ is:$$\Huge P_E=|\langle \phi,\psi\rangle|^2=|\langle \phi,\phi\rangle e^{-iEt/\hbar}|^2=|\langle \phi,\phi\rangle|^2=1$$

Where $\langle \rangle$ defines the [[Inner product spaces#Complex inner products|Hermitian inner product]]. Such solutions are known as stationary wave functions.

# Solution:

As Schrodinger's equation is linear, we can construct all possible solutions as a linear combination of stationary wave functions. Suppose that the initial wave function $\psi(x,0)$ is given, we now provide a method for determining general $\psi(x,t)$:
> Construct an orthonormal basis of Hamiltonian eigenfunctions $\phi_j(x)$ with corresponding eigenvalues $E_j$. We assume the spectrum is [[Momentum and Planck's constant#Energy|discrete and non-degenerate]], which gives stationary wave functions:$$\Huge \psi_j(x,t)=\phi_j(x)e^{-iE_jt/\hbar}$$These remain orthonormal for all time, as dependence on phase cancels out:$$\Huge \langle \psi_i,\psi_j\rangle=e^{i(E_i-E_j)t/\hbar}\langle \phi_i,\phi_j\rangle=\delta_{ij}$$
> We now expend the initial wave function as a linear combination of such orthonormal basis:$$\Huge \psi(x,0)=\sum_jc_j\phi_j(x)$$
> We promote this to the new wave function:$$\Huge \psi(x,t)=\sum_jc_j\psi_j(x,t)=\sum_jc_j\phi_j(x)e^{-iE_jt/\hbar}$$

## Particle in a box example:
Consider the infinite square well with $0<x<L$ and initial wave function:$$\Huge \psi(x,0)=\frac{1}{\sqrt{2}}(\phi_1(x)+\phi_2(x))$$Then the unique solution of Schrodinger's equation is:$$\Huge \psi(x,t)=\frac{1}{\sqrt{2}}(\phi_1(x)e^{-iE_1t/\hbar}+\phi_2(x)e^{-iE_2t/\hbar})$$The outcomes of energy measurements and associated probabilities are independent of $t$ and given by $E_1=1/2,E_2=1/2$. However this is not the case for probability density. We see that:$$\large\begin{align}
P(x,t)&=|\psi(x,t)|^2\\
&=\frac{1}{2}|\phi_1(x)|^2+\frac{1}{2}|\phi_2(x)|^2+\frac{1}{2}(\phi_1(x)\overline{\phi_2(x)}e^{-i(E_1-E_2)t/\hbar}+C)\\
&=\frac{1}{L}\left(\sin^2\left(\frac{\pi x}{L}\right)+\sin^2\left(\frac{2\pi x}{L}\right)+2\sin\left(\frac{\pi x}{L}\right)\sin\left(\frac{2\pi x}{L}\right)\cos(\omega t)\right)
\end{align}$$which oscillates with frequency:$$\Huge \omega=\frac{E_2-E_1}{\hbar}=\frac{3\hbar\pi^2}{2mL^2}$$