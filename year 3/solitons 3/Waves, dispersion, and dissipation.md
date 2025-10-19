
# Dispersion:

Usually, localised waves spread out (disperse) as they travel, preventing them from being [[Basic properties of Solitons|solitons]]. Consider the Klein-Gordon equation:$$\Huge \frac{1}{v^{2}}u_{tt}-u_{xx}+m^2u=0$$where we take $v>0$. We try a complex "plane wave" solution:$$\Huge u(x,t)=e^{i(kx-\omega t)}$$Substituting this into the Klein-Gordon equation gives:$$\Huge\begin{align*}
\frac{1}{v^{2}}u_{tt}-u_{xx}+m^2u&=\frac{1}{v^{2}}(-\omega^2e^{i(kx-\omega t)})+k^2e^{i(kx-\omega t)}+m^2e^{i(kx-\omega t)}\\
&=e^{i(kx-\omega t)}\left(-\frac{\omega^2}{v^2}+k^2+m^2\right)=0
\end{align*}$$So we must have that the second term is zero. Therefore the plane wave is a solution when:$$\Huge\omega=\omega(k)=\pm v\sqrt{k^2+m^2}$$We call;
> $k$, the wave number
> $\omega$, the angular frequency
> $\lambda=\frac{2\pi}{k}$, the wavelength
> $\tau=\frac{2\pi}{\omega}$, the period
> $\omega(k)$, the dispersion relation

Rewriting the plane wave solution as $e^{ik(x-c(k)t)}$ we see that its wave crests move with velocity:$$\Huge c(k)=\frac{\omega(k)}{k}=v\sqrt{1+\frac{m^2}{k^2}}\text{sign}(k)$$We see that waves with different wavenumbers move with different velocities, so we can create a dispersive solution by piling up real Klein-Gordon solving plane waves:$$\Huge u(x,t)=\Re\int_{-\infty}^{\infty}f(k)e^{i(kx-\omega(k)t)}dk$$We can define the velocity of a wave in two different ways:
> The velocity of wave crests, phase velocity:$$\Huge c(k)=\frac{\omega(k)}{k}$$
> The velocity of the lump of field while it disperses, group velocity:$$\Huge c_g(k)=\frac{d\omega(k)}{dk}$$

Note that the energy (and therefore information) travels at the group velocity, not phase velocity. For a relativistic wave equation, we must bind $|c_g(k)|\leq c$, where $c$ is the speed of light. Using the principles of relativity we can calculate:$$\Huge |c_g(k)|=\left|\frac{d\omega(k)}{dk}\right|=\frac{v}{\sqrt{1+\frac{m^2}{k^2}}}\leq v$$$$\Huge|c(k)|=\left|\frac{\omega(k)}{k}\right|=v\sqrt{1+\frac{m^2}{k^2}}\geq v$$Note that the last equation is not an issue for relativistic waves, as the information does not travel at phase velocity.

# The Gaussian wave packet:

The simplest example of a localised field configuration obtained by superposition of plane waves is the Gaussian wave packet, obtained by choosing a Gaussian in the general superposition:$$\Huge f(k)=e^{-a^2(k-\bar k)^2}$$This represents a lump of field with average wavenumber $\bar k$ and spread of wavenumber $\sim1/a$:![[Waves, dispersion, and dissipation 2025-10-18 16.50.11.excalidraw]]Then $u(x,t)=\Re(z(x,t))$ is a real solution of the Klein-Gordon equation, where:$$\Huge z(x,t)=\int_{-\infty}^\infty e^{a^2(k-\bar k)^2}e^{i(kx-\omega(k)t)}dk$$given that $\omega(k)=v\sqrt{k^2+m^2}$. Note that most of this integral comes from the region $k\approx\bar k$, so a good approximation can be found by taking the [[Taylor series|Taylor expansion]] about $k=\bar k$:$$\Huge\begin{align*}
\omega(k)&=\omega(\bar k)+\omega'(\bar k)(k-\bar k)+\mathcal{O}((k-\bar k)^2)\\
&=\omega(\bar k)+c_g(\bar k)(k-\bar k)+\mathcal{O}((k-\bar k)^2)\\
&\approx\omega(\bar k)+c_g(\bar k)(k-\bar k)
\end{align*}$$Substituting this into our solution gives:$$\Huge\begin{align*}
z(x,t)&\approx\int_{-\infty}^\infty e^{-a^2(k-\bar k)^2}e^{i(kx-(\omega(\bar k)+c_g(\bar k)(k-\bar k))t)}dx\\
&=e^{i(\bar kx-\omega(\bar k)t)}\int_{-\infty}^\infty e^{-a^2(k-\bar k)^2}e^{i(k-\bar k)(x-c_g(\bar k)t)}dk\\
&=_{k\rightarrow k+\bar k}e^{i(\bar kx-\omega(\bar k)t)}\int_{-\infty}^\infty e^{-a^2k^2+ik(x-c_g(\bar k)t)}dk\\
&=e^{i(\bar kx-\omega(\bar k)t)}e^{-\frac{1}{4a^2}(x-c_g(\bar k)t)^2}\int_{-\infty}^\infty e^{-a^2(k-\frac{i}{2a^2}(x-c_g(\bar k)t))^2}dx\\
&=e^{i(\bar kx-\omega(\bar k)t)}\cdot\frac{\sqrt{\pi}}{a}e^{-\frac{1}{4a^2}(x-c_g(\bar k)t)^2}
\end{align*}$$where we factored out a plane wave with $k=\bar k$ in the second line, and used the Gaussian integral formula on the fourth line. Here, the first term in the solution is called the carrier wave, and the second is called the envelope:
> The carrier wave is a plane wave moving with phase velocity:![[Waves, dispersion, and dissipation 2025-10-18 17.24.22.excalidraw]]
> The envelope is a localised "wave packet" moving with group velocity:![[Waves, dispersion, and dissipation 2025-10-18 17.26.15.excalidraw]]

This shows the wave packet in blue, and the envelope in red:![[Pasted image 20251018174309.png]]This shows a wave packet with phase velocity greater than group velocity:
![[Wave_packet_propagation_(phase_faster_than_group,_nondispersive).gif]]To this order of approximation, the spatial width of the lump has the same parametric dependence on $a$.

Refining the approximation by Taylor expanding to second order shows that:$$\Huge\text{width}\sim a^2+\frac{\omega''(\bar k)}{4a^2}t^2$$This leads to dispersion, as we can see that width will decrease as $a$ increases:
![[Wave_packet_(dispersion).gif]]

# Dissipation:

So far we have considered wave equations with real dispersion relations ($\omega(k)\in\Re$). If we instead consider $\omega(k)\in\mathbb{C}$, then we see a phenomenon called dissipation. Here, the amplitude of the wave decays exponentially in time. For a plane wave:$$\Huge u(x,t)=e^{i(kx-\omega(k)t)}=e^{i(kx-\Re(\omega(k))t)}e^{\Im(\omega(k))t}$$we have two cases:
> $\Im(\omega(k))<0$ leads to physical dispersion, where the amplitude decays exponentially in time
> $\Im(\omega(k))>0$ leads to unphysical dispersion, where the amplitude grows exponentially in time

Take for example the PDE:$$\Huge \frac{1}{v}u_t+u_x+\alpha u=0$$for $\alpha,v>0$. Substituting in a plane wave gives:$$\Huge\begin{align*}
\frac{1}{v}(-i\omega e^{i(kx-\omega t)})+ike^{i(kx-\omega t)}+\alpha e^{i(kx-\omega t)}=0
\end{align*}$$which implies $-i\frac{\omega}{v}+ik+\alpha=0$, which again implies $\omega(k)=v(k-i \alpha)$. This leads to a complex dispersion relation, making the plane wave solution:$$\Huge u(x,t)=e^{ik(x-vt)}e^{-\alpha vt}$$so the wave decays exponentially (dissipates) to zero as $t\to\infty$. This is an example of physical dissipation.

Take for example the heat equation:$$\Huge u_t-\alpha u_{xx}=0$$with $\alpha>0$. Again substituting in the plane wave gives the dispersion relation $\omega(k)=-i\alpha k^2$, another complex dispersion relation. This makes the solution:$$\Huge u(x,t)=e^{ikx}e^{-\alpha k^2t}$$and the wave dissipates with time.