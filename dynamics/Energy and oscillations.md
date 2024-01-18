Consider a particle on the line in the case [[Particle on a line#Case $F=F(x)$|$F=F(x)$]] and write $V(x)=-\int F(x)dx$ then you can write:$$\Huge \frac{d}{dx}\left(\frac{1}{2}mv^2+V\right)=mv\frac{dv}{dx}-F=0$$So we then define:$$\Huge E=\frac{1}{2}mv^2+V$$This is constant over time, since the chain rule gives:$$\Huge \frac{dE}{dt}=\frac{dE}{dx}\dot x=0,\,\text{since }\frac{dx}{dt}=0$$The quantity $E$ is the energy of the particle, which is always conserved. The equation for energy contains two terms, $\frac{1}{2}mv^2$ and $V(x)$. The latter of these is the particle's kinetic energy, whereas the former is the particles potential energy. This leads to the following conclusions:
> A force in the form $F(x)$ is said to be conservative, as it causes energy to be conserved. Note that the cases where $F=F(t)$ or $F=F(\dot x)$ are not necessarily conservative.
> Potential $V$ and energy $E$ are only defined up to an arbitrary constant.
> When $F(x)$ is constant, $V$ is linear in $x$.
> Using the conservation of energy, an idea of the particles motion can be gained without finding $x(t)$.
> $E$, energy, is constant for a given solution.
> A point where $F(x)=0$ is called an equilibrium point.

# Motion in Potential:

This is best demonstrated in an example:![[motion in potential]]

# Simple Harmonic Oscillator:

A spring extended by a distance $x$ will have a restoring force $F=-kx$. this is a case where [[Particle on a line#Case $F=F(x)$|$F=F(x)$]] and is a conservative force. This allows for conserved energy. So potential energy is given by:$$\Huge V(x)=\int Fdx=\int-kxdx=\frac{1}{2}kx^2$$This has $F=0$ point at $x=0$, the equilibrium position. In this case, the equation of motion can be completely solved:$$\Huge m\ddot x=-kx\implies\ddot x+\frac{k}{m}x=0\implies\lambda=\pm i\sqrt{\frac{k}{m}}$$This implies that the general solution is given by:$$\Huge x(t)=A\cos(\omega t)+B\sin(\omega t)$$Where $\omega=\sqrt{\frac{k}{m}}$ is the angular frequency of oscillation. This is known as Simple Harmonic Motion, periodic in $t$ with $T=\frac{2\pi}{\omega}=2\pi\sqrt{\frac{m}{k}}$. The amplitude of this oscillation is $\sqrt{A^2+B^2}$. Taking gravity into account, the equation of motion becomes $F=m\ddot x=-kx-mg$. This is an [[Second Order Differential Equations#Inhomogeneous case, $ phi(x) neq 0$|inhomogeneous second order differential equation]], with general solution:$$\Huge x(t)=A\cos(\omega t)+B\sin(\omega t)+\left(-\frac{mg}{k}\right)$$This moves the equilibrium position from $x=0$ to $x=-\frac{mg}{k}$.

# Damped oscillators:

