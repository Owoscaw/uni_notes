
Many potentials in real life are not simple, so it is important to have approximate methods for finding the [[QM systems for general potentials|energy spectrum/wave function]]. 

# Constant potential:

We use the trivial constant potential and "build" on it to gain insight into less trivial potentials:![[The WKB approximation 2026-02-20 23.17.39.excalidraw]]The wave function for this is:$$\Huge\Psi_{\pm}=A_{\pm}e^{\pm ikx},\,\,k=\sqrt{2m(E-V)}$$So the wave function is oscillatory with wavelength $\lambda=2\pi/k$. 

Taking $E<V$ we will get exponential decay in either direction the particle can go. The associated wavefunction is then:$$\Huge\Psi_\pm(x)=B_\pm e^{\pm\kappa x},\,\,\kappa=\sqrt{2m(V-E)}$$The particle essentially becomes localised in $[-1/\kappa,1/\kappa]$.

# "Slow" potentials:

We assume $E>V(x)$ for all $x$ and that $V(x)$ varies in space slowly in comparison with $\lambda$. That is, $V(x)$ varies in such a way that it remains almost constant over a region containing multiple wavelengths. Here we expect that $\Psi$ is similar to the first case, however with amplitude $A$ and wavelength $\lambda$ functions of $x$ that are slowly varying.

Assuming $E<V(x)$ with slowly varying $V$ compared to $1/\kappa$, we see that $\Psi$ will have the same form as the constant case however with $A,\kappa$ slowly varying functions of $x$.

Let us make this intuition more quantitative:
> $E>V(x)$, the Schrodinger equation becomes:$$\Huge\begin{align*}
-\frac{1}{2m}\frac{d^2\Psi}{dx^2}+(V(x)-E)\Psi(x)=0\\
\iff \frac{d\Psi}{dx^2}&=-2m(E-V(x))\Psi\\
&=p^2(x)\Psi
\end{align*}$$
>We assume the form of $\Psi$ to be:$$\Huge\begin{align*}
\Psi(x)&=A(x)e^{ip(x)}\\
\implies A''(x)+2iA'(x)p'(x)+iA(x)p''(x)&=A(x)(p'(x))^2\\
&=-p^2(x)A(x)
\end{align*}$$Looking at the real part of this equation we find$$\Huge A''-(p')^2A=-p^2A\implies A''(x)=A(x)((p')^2-p^2)$$and for the imaginary part:$$\Huge\begin{align*}
2A'p'+Ap''&=0\\
\implies(A^2p)'&=\\
\implies A^2p'&=\eta^2=\text{constant}\\
\implies A(x)&=\frac{\eta}{\sqrt{|p'(x)|}}
\end{align*}$$
>The real equation cannot be solved in general, but if we assume $A''/A<<((p')^2-p^2)$ we can approximate$$\Huge\begin{align*}
(p'(x))^2&=p^2(x)\\
\implies p'&=\frac{dp}{dx}=\pm p(x)\\
\implies p(x)&=\pm\int_\alpha^xp(y)dy
\end{align*}$$for some constant $\alpha$. This constant is arbitrary, so we choose $\alpha=0$ for simplicity.
> The wave function then becomes$$\Huge\Psi_{I,\pm}(x)\approx\frac{\eta_\pm}{\sqrt{p(x)}}e^{\pm i\int_0^xp(y)dy},\,\,p(x)=\sqrt{2m(E-V(x))}$$, and general solutions are given by linear combinations of $\Psi_{I,+},\Psi_{I,-}$.

Note that:
> If $V=\text{constant}$ we recover the plane wave solution $e^{\pm ip(x-\alpha)}$
> $|\psi_{I,\pm}|^2=\frac{\eta^2}{p(x)}$, the probability to find a particle in $x\pm dx$ is inverse proportional to its velocity.

Let us look at the "bump" square well potential:
>![[The WKB approximation 2026-02-20 23.43.24.excalidraw]]In regions $I,III$ we simply have $\Psi_I=\Psi_{III}=0$ as there is infinite potential.
>In region $II$ we assume $E>V(x)$ and that $f(x)$ is slowly varying. Therefore our wave function is simply a linear combination of the wave function we derived above:$$\Huge\begin{align*}
\Psi(x)&=\frac{1}{\sqrt{p(x)}}(\eta_+e^{ip(x)}+\eta_-e^{-ip(x)})\\
&=\frac{1}{\sqrt{p(x)}}(\eta_1\cos(p(x))+\eta_2\sin(p(x)))
\end{align*}$$
> We now impose the boundary conditions:$$\Huge\begin{align*}
\Psi_{II}(0)=\Psi_{I}(0)&=0\implies\eta_1=0\\
\Psi_{II}(a)=\Psi_{III}(0)&=0\implies\sin(p(a))=0\\
\implies p(a)\int_0^ap(y)dy&=n\pi
\end{align*}$$Hence we see that energy is quantised, as$$\Huge\begin{align*}
\int_0^ap(x)dx&=\int_0^a\sqrt{2m(E-V(x))}dx\\
&=F_n(E)=n\pi\\
\implies E&=E(n)
\end{align*}$$, so we recover the generality of [[QM systems for general potentials#Bounded propagation|bounded propagation]] giving quantised energy.
> Looking at the case where $E<V(x)$ in region $II$, we follow a similar analysis to find:$$\Huge\Psi_{II,\pm}(x)\approx\frac{\xi_\pm}{\sqrt{q(x)}}e^{\pm\int_0^xq(y)dy},\,\,q(y)=\sqrt{2m(V(x)-E)}$$

Let us look at a particle scattering off of a "bumpy step" potential:
> ![[The WKB approximation 2026-02-20 23.53.57.excalidraw]]