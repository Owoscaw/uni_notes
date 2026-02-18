
When a quantum particle is propagating in arbitrary potential $V(\underline{x})$, the only way to solve the corresponding [[Time evolution of QM states#Schrodinger equation motivation|Schrodinger equation]] is numerically. However, we study the qualitative features of the energy spectrum as well as properties of the wave function.

# General properties of wave functions:

For simplicity, we restrict to $1D$ systems although many results generalise to higher dimensions. The following properties hold:
> $\psi(x,t)$ is always single valued and continuous, as $|\psi(x,t)|^2$ has interpretation as the probability to find a particle around $(x,t)$.
> $\psi'(x,t)$ is continuous for any $V(x)<\infty$. Note that this does not hold if $V(x)$ is a delta function.
> If $V=\infty,\psi=0$. Again the only exception is for a delta function potential.
> In the region where the particle cannot propagate classically, the wave function is decreasing (approximately exponentially) as the particle propagates through the potential![[QM systems for general potentials 2026-02-13 01.53.41.excalidraw]]
> In the region where particles can propagate classically, the wave function is oscillatory:![[QM systems for general potentials 2026-02-13 01.55.25.excalidraw]]
> If a potential varies in space, the smaller $V(x)$ is, the larger the kinetic energy:$$\Huge K=E-V(x)=\frac{p^2}{2m}$$Hence $\psi$ oscillates faster in this region, which makes sense as:$$\Huge \lambda=\frac{2\pi\hbar}{p}\sim\frac{2\pi\hbar}{\sqrt{E-V(x)}}$$
> If $V(x)$ varies in space, a particle will spend less time in regions where $V(x)$ is smaller. Therefore we are "less likely" to find the particle in that region. Furthermore, the amplitude of $\psi$ must be smaller in that region:![[QM systems for general potentials 2026-02-13 02.00.30.excalidraw]]

We see two phenomena when the particle moves through the potential:
> Bounded propagation
> Quantum scattering

# Bounded propagation:

In the classical picture, this occurs when $E<E_0$. The particle is moving in some potential $V(x)$, from which it cannot escape (classically), since it lacks the energy:![[QM systems for general potentials 2026-02-13 02.07.34.excalidraw]]The particle with energy $E<V_0$ will classically oscillate between two turning points $x_1,x_2$:
> At $x_1$, we have $E=V(x_1)$, implying that velocity $v(x_1)=0$.
> At $x_2$, we have $E=V(x_2)$, implying that velocity $v(x_2)=0$.

In the quantum picture, we have two situations depending on $E$:
> Case A, where $0<E<V_\infty\leq V_0$. The energy of the particle is no longer arbitrary or real, but it is quantised. Therefore, between $x_1,x_2$ we have oscillatory behaviour for $\psi$.![[QM systems for general potentials 2026-02-13 02.18.06.excalidraw]]Here, we see exponential decay in $\psi$ either side of $x_1,x_2$ and the quantum oscillatory behaviour between $x_1,x_2$. Note that the particle will still have probability to be found past $x_1,x_2$ (blue), however it will decay approximately exponentially as $x\to\pm\infty$.
> Case B, where $V_\infty<E<V_0$. Here, the particle cannot escape from a potential well classically, but can tunnel through a barrier and escape to $\pm\infty$ in the quantum case. Inside the potential well, energy is quantised and so particles created inside the well have discrete energy states. If a particle is created outside the well at $x=\pm\infty$, they experience a continuous spectrum of energy states:![[QM systems for general potentials 2026-02-13 02.27.53.excalidraw]]This is divided into three regions:
> > Region $I$, where the particle oscillates about $0$ and the particle cannot classically escape. 
> > Region $II$, where the particle is between $x_2',x_2''$ and the classical particle is forbidden. Here, the particle can continue "rolling down the wave function hill" until it exits at $x_2'$. This is quantum tunnelling, and also occurs between $x_1'$ and $x_2'$. Note that exponential decay of the wave function is present within this region.
> > Region $III$, where the particle is before $x_1'$ or after $x_2'$. Here, the particle can exist classically and the wave function is oscillatory once again.

# Quantum scattering (unbounded propagation):

We are studying a situation when a particle comes from $\pm\infty$ and scattering off of some potential bump $V(x)$:![[QM systems for general potentials 2026-02-18 01.34.18.excalidraw]]Classically:
> If $E<V_0$ the particle will elastically bounce off the potential and will return to whence it came.
> If $E>V_0$, the particle goes over the potential as if $V(x)=0$.

In our superior way of thinking, both for $E>V_0$ and $E<V_0$, some figment of a particle wave is scattered back and the rest transmits through. In order to see how much of an incoming wave transmits through the potential and how much scatters back, we look at $\psi(x,t)$ at $x\to\pm\infty$:$$\Huge\begin{align*}
x\to-\infty&:\Psi(x,t)\to A_Ie^{ipx}+A_Re^{-ipx}=\Psi_I+\Psi_R\\
x\to+\infty&:\Psi(x,t)\to Be^{iqx}=\Psi_T
\end{align*}$$Here, $A_I$ is the amplitude of the incoming particle with momentum $p$. $A_R$ is the amplitude of reflected particles with momentum $-p$. $B$ is the amplitude of the transmitted particle with momentum $q$:![[QM systems for general potentials 2026-02-18 01.40.40.excalidraw]]In order to quantify which fraction of particles go through the barrier and which reflect, we introduce the following quantities.:
> Probability density $\rho$:$$\Huge\rho(\underline{x},t)=|\psi(\underline{x},t)|^2$$is the probability to find a particles in $dV$ around $(\underline{x},t)$.
> Probability current, $J_i$:$$\Huge J_i=\frac{i}{2m}(\psi^*\partial_i\psi-\psi\partial_i\psi^*)$$is the vector dictating how probability distributes across space. For each wave $k$ for $k\in\{I,R,T\}$:$$\Huge J(\psi_k)=\frac{\hbar}{m}\times\text{associated momemntum of }\psi_k\times|\psi_k|^2$$

We are trying to find a quantity of unit time, so we see that:
> $\rho(\psi_k)=|\psi_k|^2$ is the number of particles in $dV$. Therefore we multiply by the velocity $v=p/m$.
> $|\psi_k|^2\frac{\text{momentum}}{m}$ is the number of particles per unit time through $dV$ at $(\underline{x},t)$

We can now find the coefficients that dictate the probabilities of each particle phenomenon:
> The transmission coefficient will be the amount of transmitted wave as a fraction of the incoming wave:$$\Huge T=\frac{J_T}{J_I}=\frac{p_T}{p_I}\frac{|\psi_T|^2}{|\psi_I|^2}$$
> The reflection coefficient is then the fraction of incoming wave that gets transmitted:$$\Huge R=\frac{J_R}{J_I}=\frac{p_I}{p_I}\frac{|\psi_R|^2}{|\psi_I|^2}$$

Note that we have the important property:$$\Huge R+T=1$$This ensures we do not lose any particles, as it demands $\int|\psi|^2=1$