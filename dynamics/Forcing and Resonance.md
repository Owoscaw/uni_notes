# Forcing:

An external forcing term can be added to a [[Energy and oscillations#Simple Harmonic Oscillator|harmonic oscillator]], for example the vibration experience when driving over a corrugated surface:$$\Huge m\ddot x=-kx+m\sin(pt)$$For some positive constant $p$. Solving this gives:$$\Huge \ddot x+\omega^2x=\sin(pt)\implies x(t)=A\cos(\omega t)+B\sin(\omega t)+P(x)$$Where $P(x)$ is the particular integral. This takes form $C\sin(pt)$. Solving for $C$ gives:$$\Huge x(t)=A\cos(\omega t)+B\sin(\omega t)+\frac{1}{\omega^2-p^2}\sin(pt)$$This produces a mixture of oscillations of frequency $\omega$ and $p$. 

# Resonance:

If $\omega=p$, then the complimentary function remains the same however a different particular integral is needed. In this case:$$\Huge x(t)=A\cos(\omega t)+\left(B-\frac{t}{2\omega}\right)\sin(\omega t)$$The amplitude of oscillation then becomes:$$\Huge \sqrt{A^2+\left(B-\frac{t}{2\omega}\right)^2}$$This grows unbounded with $t$, which is very useful for tuning into a particular radio frequency however detrimental when building a bridge.

# Forcing + [[Energy and oscillations#Damped oscillators|Damping]]:

