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

Consider a simple harmonic oscillator when a shock absorber is added. This will add a new restoring force proportional to velocity. Take this force to be $-2mb\dot x$ with $b>0$. The equation of motion becomes:$$\Huge m\ddot x=-kx-2mb\dot x\implies \ddot x+2b\dot x+\omega^2x=0$$Where again $\omega=\sqrt{\frac{k}{m}}$. This has auxiliary equation $\lambda^2+2b\lambda+\omega^2=0$. This has roots $\lambda=-b\pm\sqrt{b^2-\omega^2}$. Three cases naturally arise from this:
> $b>\omega$, overdamping. Here $\lambda_\pm$ are real and negative since $b-\pm\sqrt{b^2-\omega^2}$. Here the general solution is:$$\Huge x(t)=Ae^{\lambda_+t}+Be^{\lambda_-t}$$
> $0\leq b<\omega$, underdamping. Here $b^2-\omega^2<0$, so the roots $\lambda_\pm$ are complex, $\lambda_{\pm}=-b\pm i\sqrt{\omega^2-b^2}$. The general solution then becomes:$$\Huge x(t)=e^{-bt}(A\cos(t\sqrt{\omega^2-b^2})+{B\sin(t\sqrt{\omega^2-b^2})})$$
> $b=\omega$, critical damping. Now $\lambda_\pm=-b$, so the general solution is:$$\Huge x(t)=e^{bt}(A+Bt)$$

![[damped oscillations]]