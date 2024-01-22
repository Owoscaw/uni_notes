# Forcing:

An external forcing term can be added to a [[Energy and oscillations#Simple Harmonic Oscillator|harmonic oscillator]], for example the vibration experience when driving over a corrugated surface:$$\Huge m\ddot x=-kx+m\sin(pt)$$For some positive constant $p$. Solving this gives:$$\Huge \ddot x+\omega^2x=\sin(pt)\implies x(t)=A\cos(\omega t)+B\sin(\omega t)+P(x)$$Where $P(x)$ is the particular integral. This takes form $C\sin(pt)$. Solving for $C$ gives:$$\Huge x(t)=A\cos(\omega t)+B\sin(\omega t)+\frac{1}{\omega^2-p^2}\sin(pt)$$This produces a mixture of oscillations of frequency $\omega$ and $p$. 

# Resonance:

If $\omega=p$, then the complimentary function remains the same however a different particular integral is needed. In this case:$$\Huge x(t)=A\cos(\omega t)+\left(B-\frac{t}{2\omega}\right)\sin(\omega t)$$The amplitude of oscillation then becomes:$$\Huge \sqrt{A^2+\left(B-\frac{t}{2\omega}\right)^2}$$This grows unbounded with $t$, which is very useful for tuning into a particular radio frequency however detrimental when building a bridge.

# Forcing + [[Energy and oscillations#Damped oscillators|Damping]]:

Adding a damping force can often give $x_{CF}$ that will tend to $0$ as $t\to\infty$, for example exponentials with negative powers. In this case, $x_{CF}$ is said to by the transient response. If the non-homogenous side of the second order [[Second Order Differential Equations#Inhomogeneous case, $ phi(x) neq 0$|ODE]] is periodic, then it will not tend to $0$ and is said to be the steady-state response. If this $x_{PI}$ is a linear combination of $\cos$ and $\sin$ terms, then it can be written as a single term using a phase shift. By defining $\tan\phi=\frac{2bp}{\omega^2-p^2}$ then $x_{PI}$ is written as:$$\Huge x_{PI}(t)=C\sin(pt-\phi)$$Note that resonance will now be out of phase with applied force, so cannot happen.

# Small oscillations:

Suppose that [[Energy and oscillations#Motion in Potential|$V(x)$]] has a local minimum at $x_0$.