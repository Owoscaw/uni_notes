
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

Lorentz invariance demands no information propagates faster than the speed of light, so it follows that any two measurements in the quantum theory that are spacelike separated should not affect each other, i.e. they commute:$$\Large[\mathcal{O}_1(x),\mathcal{O}_2(y)]=0,\,\,(x-y)^2>0$$