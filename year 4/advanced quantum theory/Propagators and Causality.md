
We wish to understand how [[QFT in canonical formalism#Multi-particle states|particles]] propagate through space, making our quantisation procedure manifestly [[SR and Noether's theorem#Lorentz group on scalar fields|Lorentz invariant]]. Recall our field definition:$$\Large\Phi(t,\underline{x})=\int\frac{d^3k}{(2\pi)^3}\frac{1}{\sqrt{2\omega_\underline{k}}}(\hat a_\underline{k}e^{ik_\mu x^\mu}+\hat b_\underline{k}^\dagger e^{-ik_\mu x^\mu})$$The bracketed term is nicely Lorentz invariant. 

Therefore let us start from the measure$$\Large\int d^4k\,\delta(-k^2-m^2)\theta(k^0)$$where $-k^2-m^2=-k^\mu k_\mu-m^2$ and $\theta(k)$ is the Heaviside function. We aim to recover our field definition (or something similar) from this, but first let us check a few things. This measure is manifestly Lorentz invariant:$$\Large\begin{aligned}
k^\mu&\to\Lambda^\mu_\nu k^\nu=k'^\nu\\
d^4k&\to d^4k'|\det\Lambda|^{-1}=d^4k'\\
-k^\mu k_\mu-m^2&\to-k'^\mu k'_\mu-m^2\\
_\text{orthochronous}\implies\theta(k^0)&\to\theta(k'^0)
\end{aligned}$$Note the equation$$\huge (k^0)^2-\underline{k}\cdot\underline{k}=m^2$$describes a hyperboloid in $k$, known as the mass-shell condition. We can solve for two solutions$$\Large k^0=\pm\sqrt{|\underline{k}|^2+m^2}=\pm\omega_\underline{k}$$, however we discard the negative solution due to the presence of the Heaviside function in our measure. Splitting our measure integral over components like this, we write:$$\Large\begin{aligned}
\int d^4k\,\delta(-k^2-m^2)\theta(k^0)&=\int d^3k\int dk^0\delta((k^0)^2-\omega_\underline{k}^2)\theta(k^0)\\
&=\int d^3k\int dk^0\delta(k^0-\omega_\underline{k})\left|\frac{d(k^0)^2}{dk^0}\right|^{-1}\\
&=\int\frac{d^3k}{2\omega_\underline{k}}
\end{aligned}$$This is a Lorentz invariant measure that we can use to integrate over the $3$-dimensional hyperboloid mentioned above. The fact that this is Lorentz invariant allows us to construct a Lorentz invariant delta function. Let us denote this function by $\tilde\delta^{(3)}(\underline{k}-\underline{k}')$, we want this to satisfy$$\Large\int\frac{d^3k}{2\omega_\underline{k}}\tilde\delta^{(3)}(\underline{k}-\underline{k}')f(\underline{k})=f(\underline{k}')$$so that we maintain Lorentz invariance on the measure and the delta function. This implies the Lorentz invariant delta function on the mass shell is:$$\Large\tilde\delta^{(3)}(\underline{k}-\underline{k}')=2\omega_\underline{k}\delta^{(3)}(\underline{k}-\underline{k}')$$We can then adapt our commutation relations$$\Large\begin{aligned}
[a_\underline{k},a_\underline{k'}^\dagger]&=(2\pi)^3\delta^{(3)}(\underline{k}-\underline{k}')=\frac{(2\pi)^3}{2\omega_\underline{k}}\tilde\delta^{(3)}(\underline{k}-\underline{k}')\\
[b_\underline{k},b_\underline{k'}^\dagger]&=(2\pi)^3\delta^{(3)}(\underline{k}-\underline{k}')=\frac{(2\pi)^3}{2\omega_\underline{k}}\tilde\delta^{(3)}(\underline{k}-\underline{k}')
\end{aligned}$$, which then imply the form of relativistically normalised creation/annihilation operators:$$\Large\begin{aligned}
&\tilde a_\underline{k}=\sqrt{2\omega_\underline{k}}a_\underline{k}&\tilde a_\underline{k}^\dagger=\sqrt{2\omega_\underline{k}}a_\underline{k}^\dagger\\
&\tilde b_\underline{k}=\sqrt{2\omega_\underline{k}}b_\underline{k}&\tilde b_\underline{k}^\dagger=\sqrt{2\omega_\underline{k}}b_\underline{k}^\dagger
\end{aligned}$$These manifestly satisfy the above commutation relations without the prefactor of $1/(2\omega_\underline{k})$.

# Commutators and the light-cone:

In our process of quantisation, we made a choice in time (and therefore rest frame). Our starting point was the canonical [[QFT in canonical formalism#Equal-time commutation relations|equal-time commutation relation]]:$$\Large[\Phi(t,\underline{x}),\Pi(t,\underline{y})]=i\delta^{(3)}(\underline{x}-\underline{y})$$Therefore the resulting quantum theory may not be Lorentz covariant, our procedure may have broken this symmetry.

To find out, let us test with operators that are timelike or spacelike separated. If an event happens at some point $x$ in spacetime, then an event at another spacetime point $y$ can affect the event at $x$ if they are timelike separated $(x-y)^2<0$ and cannot affect it if they are spacelike separated $(x-y)^2>0$. The surface separating these regions is a cone in $\Re^{1,3}$ known as the light-cone.

Lorentz invariance demands no information propagates faster than the speed of light, so it follows that any two measurements in the quantum theory that are spacelike separated should not affect each other, i.e. they commute:$$\Large[\mathcal{O}_1(x),\mathcal{O}_2(y)]=0,\,\,(x-y)^2>0$$Notably, these operators need not be evaluated at the same time. This is satisfied by the canonical equal-time commutation relations since the RHS is only ever non-zero if $x=y$, on the light-cone. 

Let us consider a non-trivial example:
> We know the form of the commutator:$$\Large[\Phi(x),\Phi^\dagger(y)]=\int\frac{d^3k}{(2\pi)^32\omega_\underline{k}}(e^{i\underline{k}\cdot(\underline{x}-\underline{y})}-e^{-i\underline{k}\cdot(\underline{x}-\underline{y})})$$The first term comes from $[a_\underline{k},a_\underline{k}^\dagger]$, the second comes from $[b_\underline{k},b_\underline{k}^\dagger]$.
> The RHS of this is not immediately zero, to compute the integral note that it is Lorentz covariant since it was built from the Lorentz invariant measure we made as well as the scalar product:$$\Large \underline{k}\cdot(\underline{x}-\underline{y})=k_\mu(x-y)^\mu$$Therefore we use a Lorentz transformation to force $x-y$ to lie in a particular direction and use Lorentz covariance to reconstruct the full result.
> For timelike separated $x$ and $y$, we choose $x-y$ to point in the time direction. That is, there exists a Lorentz transformation such that:$$\Large\Lambda^\mu_\nu(x-y)^\nu=(x'^0-y'^0,0,0,0)^\mu$$The integral then becomes$$\Large\int\frac{d^3k}{(2\pi)^32\omega_\underline{k}}(e^{-i\omega_\underline{k}(x'^0-y'^0)}-e^{i\omega_\underline{k}(x'^0-y'^0)})$$, a non-vanishing oscillatory function in $(x'^0-y'^0)$.
> For spacelike separated $x$ and $y$, we can choose $x-y$ to be zero in the time direction. That is, we take a Lorentz transformation such that:$$\Large\Lambda^\mu_\nu(x-y)^\nu=(0,\underline{x}'-\underline{y}')^\mu$$The integral then becomes$$\Large\begin{aligned}
&\int\frac{d^3k}{(2\pi)^32\omega_\underline{k}}(e^{i\underline{k}\cdot(\underline{x}'-\underline{y}')}-e^{-i\underline{k}\cdot(\underline{x}'-\underline{y}')})\\
_{\text{changing }\underline{k}\to-\underline{k}\text{ in second term}}&\int\frac{d^3k}{(2\pi)^32\omega_\underline{k}}(e^{i\underline{k}\cdot(\underline{x}'-\underline{y}')}-e^{i\underline{k}\cdot(\underline{x}'-\underline{y}')})=0
\end{aligned}$$, which we are allowed to do since $\omega_{-\underline{k}}=\omega_\underline{k}$. By Lorentz covariance, we find:$$\Large[\Phi(x),\Phi^\dagger(y)]=0,\,\,(x-y)^2>0$$

The same turns out to be true for any commutator of spacelike separated local operators. Furthermore, it holds for both free and interacting theories. In QFT, information cannot propagate outside the light-cone and we call the theory causal.

# Particle propagation:

Consider a particle at a spacetime point $x$, we probe the causal structure of QFT by considering the amplitude for finding it at a different spacetime point $y$. One way to answer this is to consider the overlap:$$\Large\begin{aligned}
D(y-x)&=\langle 0|\phi(y)\phi^\dagger(x)|0\rangle\\
&=\langle \psi_f|\psi_i\rangle
\end{aligned}$$We can write this as$$\Large D(y-x)=\int\frac{d^3k}{(2\pi)^2}\frac{1}{2\omega_\underline{k}}e^{i\underline{k}\cdot(\underline{y}-\underline{x})}$$, known as the propagator and is Lorentz covariant. We could compute this integral by considering $(y-x)^2=|\underline{y}-\underline{x}|^2$ for spacelike separations. For large $|\underline{y}-\underline{x}|\to\infty$, this behaves like:$$\Large D(y-x)\sim\exp(-m|\underline{y}-\underline{x}|)$$The fact this does not vanish shows us that there is some degree of entanglement in the vacuum of a QFT. That is, there is quantum entanglement between two points in space. This does not violate causality, as the amplitudes will cancel between these two events.

## Feynman propagator:
We define the notion of time ordering, which orders operators evaluated at earlier times to the right and operators evaluated at later times to the left$$\Large\begin{aligned}
\underline{T}(\mathcal{O}_1(y),\mathcal{O}_2(x))&=\begin{cases}\mathcal{O}_1(y)\mathcal{O}_2(x) & y^0>x^0\\
\mathcal{O}_2(x)\mathcal{O}_1(y) & x^0>y^0\end{cases}\\
&=\theta(y^0-x^0)\mathcal{O}_1(y)\mathcal{O}_2(x)+\theta(x^0-y^0)\mathcal{O}_2(x)\mathcal{O}_1(y)
\end{aligned}$$, where $\theta$ is the Heaviside function. The Feynman operator is then defined as:$$\Large\begin{aligned}
G(y-x)&=\langle 0|\underline{T}(\phi(y),\phi^\dagger(x))|0\rangle=G(x-y)\\
&=\theta(y^0-x^0)D(y-x)+\theta(x^0-y^0)D(x-y)\\
&=\theta(y^0-x^0)\int\frac{d^3k}{(2\pi)^3}\frac{1}{2\omega_\underline{k}}e^{i\underline{k}\cdot(\underline{y}-\underline{x})}\\
&+\theta(x^0-y^0)\int\frac{d^3k}{(2\pi)^3}\frac{1}{2\omega_\underline{k}}e^{i\underline{k}\cdot(\underline{x}-\underline{y})}
\end{aligned}$$This will be the same for both particles and anti-particles:
> We claim this is equal to:$$\Large -i\int\frac{d^4k}{(2\pi)^4}\frac{1}{k^2+m^2}e^{i\underline{k}\cdotp(\underline{y}-\underline{x})}$$
> Let us start by separating our the time direction in the above$$\Large\begin{aligned}
G(\underline{y}-\underline{x})?&=-i\int\frac{d^3k}{(2\pi)^3}\int\frac{dk^0}{2\pi}\frac{e^{i\underline{k}\cdot(\underline{y}-\underline{x})}}{-(k^0)^2+\underline{k}\cdot\underline{k}+m^2}\\
&=\int\frac{d^3k}{(2\pi)^3}I(\underline{k})\\
I(\underline{k})&=i\int_\Re\frac{dk^0}{2\pi}\frac{e^{i\underline{k}\cdot(\underline{y}-\underline{x})}}{(k^0+\omega_\underline{k})(k^0-\omega_\underline{k})}
\end{aligned}$$
>  This integrand is singular for $k^0=\pm\omega_\underline{k}$, with two [[Cauchy's Residue theorem#Meromorphicity|simple poles]] and therefore meromorphic. We use [[Cauchy's Residue theorem#Part 1|Cauchy's Residue theorem]] and the Feynman prescription ($i\epsilon$ prescription) to construct our complex integral. First we notice if $y^0>x^0$ our term $\exp(-ik^0(y^0-x^0))\to0$ exponentially as $k^-\to-i\infty$ (justifying making this contour closed):![[Propagators and Causality 2026-11-13 15.29.20.excalidraw]]This is a clockwise contour, and so we calculate:$$\Large\begin{aligned}
I(\underline{k})&=\int_{\gamma_1}+\int_{\gamma_\infty}\\
&=-2\pi i\,\text{res}_{k^0=\omega_\underline{k}}\frac{i\exp(-ik^0(y^0-x^0)+i\underline{k}\cdot(\underline{y}-\underline{x}))}{2\pi(k^0+\omega_\underline{k})(k^0-\omega_\underline{k})}\\
&=-2\pi i\lim_{k^0\to\omega_\underline{k}}(k^0-\omega_\underline{k})\cdot(")\\
&=\frac{\exp(-i\omega_\underline{k}(y^0-x^0)+i\underline{k}\cdot(\underline{x}-\underline{y}))}{2\omega_\underline{k}}
\end{aligned}$$
> If we take $x^0>y^0$ we will have to close the contour with $k^0\to+i\infty$ to exponentially suppress the integrand:$$\Large\begin{aligned}
I(\underline{k})&=\int_{\gamma_1}+\int_{\gamma_\infty'}\\
&=2\pi i\,\text{res}_{k^0=-\omega_\underline{k}}(\dots)\\
&=\frac{\exp(-i\omega_\underline{k}(x^0-y^0)-i\underline{k}\cdot(\underline{x}-\underline{y}))}{2\omega_\underline{k}}
\end{aligned}$$Where $\gamma_\infty'$ is the infinite leg of the path from above this time (note this is now a ccw contour). 
> Therefore we have found:$$\Large\begin{aligned}
-i\int\frac{d^4k}{(2\pi)^4}\frac{e^{-i\underline{k}\cdot(\underline{y}-\underline{x})}}{k^2+m^2}&=\int\frac{d^3k}{(2\pi)^3}I(\underline{k})\\
&=\theta(y^0-x^0)\int\frac{d^3k}{(2\pi)^3}\frac{e^{-i\omega_\underline{k}(y^0-x^0)+i\underline{k}\cdot(\underline{y}-\underline{x})}}{2\omega_\underline{k}}\\
&+\theta(x^0-y^0)\int\frac{d^3k}{(2\pi)^3}\frac{e^{-i\omega_\underline{k}(x^0-y^0)+i\underline{k}\cdot(\underline{x}-\underline{y})}}{2\omega_\underline{k}}
\end{aligned}$$Note in our integral prescription, we took an infinitesimal radius $i\epsilon$ around each pole and took $\epsilon\to0$:![[Propagators and Causality 2026-11-13 15.55.00.excalidraw]]