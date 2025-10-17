
Consider a free particle on the real line with initial position and momentum given by $(x_0,p_0)$. According to classical mechanics it will evolve in time according to:$$\Huge\begin{align}
x(t)&=x_0+\frac{p_0}{m}t\\
p(t)&=p_0
\end{align}$$
The equivalent scenario in quantum mechanics is an initial [[Wave function#Expectation values|wave function]] $\psi(x,0)$ with [[Momentum and Planck's constant#Momentum expectation|expectations]] $\langle x\rangle=x_0,\langle p\rangle=p_0$. We then aim to determine the wave function at later times.

# Hamiltonian eigenfunctions:

We must first construct an orthonormal basis of eigenfunctions of the Hamiltonian operator:$$\Huge \hat H=-\frac{\hbar}{2m}\frac{\partial^2}{\partial x^2}$$which have form:$$\Huge \phi_p(x)=\frac{1}{\sqrt{2\pi\hbar}}e^{ipx/\hbar}$$and we see that:$$\Huge \hat H\phi_p(x)=\frac{p^2}{2m}\phi_p(x)$$So the eigenfunction $\phi_p(x)$ as above has corresponding eigenvalue $p^2/2m$. The momentum operator therefore has a continuous spectrum with normalisation chosen such that:$$\Huge\begin{align}
\langle \phi_p(x),\phi_{p'}(x)\rangle&=\int_{-\infty}^\infty\overline{\phi_p(x)}\phi_{p'}(x)dx\\
&=\frac{1}{2\pi\hbar}\int_{-\infty}^\infty e^{-i(p-p')x/\hbar}dx\\
&=\delta(p-p')
\end{align}$$
Note that the spectrum of Hamiltonian eigenfunctions is degenerate since $\phi_p(x),\phi_{-p}(x)$ have the same energy, as $E_p=E_{-p}$ with $E_p=\frac{p^2}{2m}$. This is a consequence of "parity". These can still be taken as an orthonormal basis.

Also, these eigenfunctions are stationary solutions to [[Schrodinger's equation]]:$$\Huge\begin{align}
\psi_p(x,t)&=\phi_p(x)e^{-iE_pt/\hbar}\\
&=\frac{1}{\sqrt{2\pi\hbar}}e^{i(px-E_pt)/\hbar}
\end{align}$$These are called plane waves. Note that $\psi_p,\psi_{-p}$ correspond to plane waves of equal magnitude and opposite direction, so will have equal energy. This explains where the parity of eigenvalues comes from.

# Time evolution:

We expand $\psi(x,0)$ as a linear combination of Hamiltonian eigenfunctions. As the spectrum of $\hat H$ is continuous, we write this as the integral:$$\Huge\begin{align}
\psi(x,0)&=\int_{-\infty}^\infty c(p)\phi_p(x)dp\\
&=\frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^\infty c(p)e^{ipx/\hbar}dp\\
\end{align}$$This is exactly the form of a [[Fourier transform]] in the coefficients $c(p)$. We therefore use the inverse relation:$$\Huge c(p)=\frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^\infty\psi(x,0)e^{-ipx/\hbar}dx$$which corresponds to the Fourier transformation between the initial wave function $\psi(x,0)$ and the initial momentum-space wave function $c(p)=\tilde\psi(x,0)$.

We can use this to state the wave function at later times through the addition of the exponential term in the "linear combination":$$\Huge\begin{align}
\psi(x,t)&=\int_{-\infty}^\infty c(p)\psi_p(x,t)dp\\
&=\frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^\infty c(p)e^{ipx/\hbar}e^{-ip^2t/2m\hbar}dp\\
&=\frac{1}{2\pi\hbar}\int_{-\infty}^\infty\left(\int_{-\infty}^\infty\psi(x',0)e^{-ipx'/\hbar}dx'\right)e^{ipx/\hbar}e^{-ip^2t/2m\hbar}dp\\
&=\frac{1}{2\pi\hbar}\int_{-\infty}^\infty \psi(x',0)\left(\int_{-\infty}^\infty e^{-ip(x'-x)/\hbar-ip^2t/2m\hbar}dp\right)dx'
\end{align}$$where we have substituted in the time evolving coefficient formula and exchanged the integrals over momentum and $x'$. This is now a Gaussian integral, which is computed via the formula:$$\Huge \int_{-\infty}^\infty e^{-\alpha y^2+\beta y}dy=\sqrt{\frac{\pi}{\alpha}}e^{\beta^2/4\alpha}$$where we have:$$\Huge \alpha=\frac{it}{2m\hbar},\,\,\beta=i\frac{x-x'}{\hbar}$$so the inner integral in the time evolving wave function is given by:$$\Huge \int_{-\infty}^\infty e^{-ip(x'-x)/\hbar-ip^2t/2m\hbar}dp=\left(\frac{2\pi\hbar m}{it}\right)^{1/2}e^{im(x-x')^2/2\hbar t}$$
Putting all this together we get the function:$$\Huge \psi(x,t)=\left(\frac{m}{2\pi\hbar it}\right)^{1/2}\int_{-\infty}^\infty\psi(x',0)\exp\left(\frac{im(x-x')^2}{2\hbar t}\right)dx'$$This is the time evolution of the wave function in terms of the initial wave function.

Note that the expression:$$\Huge G(x,x';t)=\left(\frac{m}{2\pi\hbar it}\right)^{1/2}\exp\left(\frac{im(x-x')^2}{2\hbar t}\right)$$is known as the propagator.

# Gaussian example:

Take for example the initial wave function:$$\Huge \psi(x,t)=Ce^{-x^2/4\Delta^2}e^{ip_0x/\hbar}$$with normalisation such that $C=(2\pi\Delta^2)^{-1/4}$. We see that this has the initial probability distribution:$$\Huge P(x,0)=\frac{1}{\sqrt{2\pi\Delta^2}}e^{-x^2/2\Delta^2}$$which is exactly a Gaussian distribution with mean $0$ and standard deviation $\Delta$. We can calculate $\Delta x$ and $\Delta p$ to show that this saturates [[Commutators and Uncertainty Principle#General Uncertainty Principle|Heisenberg's uncertainty principle]], such a wave function is known as the minimal uncertainty wave packet. 

Using the formula derived above we can calculate the time evolving probability distribution:$$\Huge P(x,t)=|\psi(x,t)|^2=\frac{1}{\sqrt{2\pi\Delta(t)^2}}\exp\left(-\frac{x(t)^2}{4\Delta(t)^2}\right)$$with:$$\Huge x(t)=x-\frac{p_0t}{m},\,\,\Delta(t)=\Delta\sqrt{1+\frac{\hbar^2t^2}{4m^2\Delta^4}}$$
Re-calculating $\Delta x,\Delta p$ shows that Heisenberg's uncertainty principle is still saturated and is indeed time independent.

# Two particle system:

Multiple particle systems are still described by a single wave function. Such wave functions can sometimes be factorised into single-particle wave functions. When they are not factorised, we call the particles entangled. This has the effect of measurement of one particle influencing the other. We now have a single wave function $\psi(x_1,x_2)$ with probability density $P(x_1,x_2)$. This has the interpretation where the probability to find particle 1 in the interval $a<x_1<b$ and particle 2 in the interval $c<x_2<d$ is:$$\Huge \int_a^b\int_c^dP(x_1,x_2)dx_1\,dx_2$$It also makes sense to consider the position of a single particle with the integral:$$\Huge \int_a^bP(x_1,x_2)dx_2$$representing the probability of finding particle $1$ in $a<x_1<b$. If both particles are measured at once, the wave function collapses to the product of position eigenstates:$$\Huge \psi_\text{before}(x_1,x_2)\rightarrow\psi_{\text{after}}(x_1,x_2)\propto\delta(x_1-\tilde x_1)\delta(x_2-\tilde x_2)$$where $\tilde x_1,\tilde x_2$ are the measured positions of the particles. If only one of the particles is measured, we get:$$\Huge\begin{align}
\psi_\text{before}(x_1,x_2)\rightarrow\psi_\text{after}(x_1,x_2)&\propto\delta(x_1-\tilde x_1)\psi_\text{before}(x_1,x_2)\\
&=\delta(x_1-\tilde x_1)\psi_\text{before}(\tilde x_1,x_2)
\end{align}$$
Now put two particles in a box of size $L$. That is, $0<x_1,x_2<L$ and assume the potential vanishes inside the box, and is infinite outside. The Hamiltonian for two free, non-interacting particles of equal mass is then:$$\Huge \hat H=\frac{1}{2m}\hat p_1^2+\frac{1}{2m}\hat p_2^2$$The eigenfunctions are then simply the products of the single particle eigenfunctions:$$\Huge \phi(x_1,x_2)=\frac{2}{L}\sin\left(\frac{n\pi x_1}{L}\right)\sin\left(\frac{m\pi x_2}{L}\right)$$We can then easily find the time-dependence using our prior knowledge. We must therefore find the corresponding eigenvalue for this wave function. We see that:$$\Huge \hat H\phi(x_1,x_2)=\frac{\hbar^2}{2m}\frac{\pi^2}{L^2}(n^2+m^2)\phi(x_1,x_2)$$So we have that the eigenvalue is simply the sum of the individual particle eigenvalues. This is an example of separable particles, as the wave function separates into factors containing only $x_1$ and $x_2$ respectively.