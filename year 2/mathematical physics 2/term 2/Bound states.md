

In classical mechanics, a particle has a defined position and momentum given by $x(t),p(t)$ for any given time $t$. This is viewed geometrically as some curve in [[Hamiltonian Formalism#Phase space|phase space]] which is parametrised by time $t$. Given initial conditions, the shape of the curve is determined by [[Hamiltonian Formalism#Hamilton's equations|Hamilton's equations]]:$$\Huge \dot x=\frac{\partial H}{\partial p},\,\,\dot p=-\frac{\partial H}{\partial x}$$Where $H$ is the [[Hamiltonian Formalism|Hamiltonian]]. Note that these equations actually specify the tangent space to the curve at time $t$:![[phase space]]
A bound state is a solution of Hamilton's equations that is confined to a finite region of phase space. Such states are derived from oscillations around a local minimum of the potential $V(x)$.

Take for example the simply harmonic oscillator, which has potential described by:$$\Huge V(x)=\frac{1}{2}m\omega^2x^2$$Where $\omega$ is angular frequency. The general solution of Hamilton's equations is then given by:$$\Huge\begin{align}
x(t)&=\sqrt{\frac{2E}{m\omega^2}}\sin(\omega t+\phi)\\
p(t)&=\sqrt{2mE}\cos(\omega t+\phi)
\end{align}$$Where the energy $E\geq0$ and phase $\phi$ are determined by initial conditions. For such a scenario, potential energy and phase space look like this:![[harmonic potential]]Here, the particle is confined to the region where $V(x)\leq E$ and cannot escape the potential well. The curve $(x(t),p(t))$ forms an ellipse in phase space, confined to a finite region. There is therefore a continuous spectrum of bound states parametrised by the energy $E\geq0$. 

# Quantisation:

Classically, we have a solution for any value of $E$, however real world experimentation suggests a solution for discrete values of $E$, given by:$$\Huge E=\frac{\omega}{2\pi}n\hbar$$For $n\in\mathbb{N}$. A way out of this dilemma is to impose the quantisation condition:$$\Huge\int_\text{orbit}p\,dx=\frac{2\pi E}{\omega}=n\hbar$$For some $n\in\mathbb{Z}$. This required that the integration of momentum over the full orbit of a phase space is equal to an integer times a constant.

# The double slit experiment:

The double slit experiment consists of a source emitting electrons towards a screen, $S$, with two slits. A detector $D$ is placed at some distance $L$ from the screen. The electron intensity pattern is then measured.

When the electrons behave as particles, they obey Hamilton's equations:$$\Huge \dot x=\frac{\partial H}{\partial p},\,\,\dot p=-\frac{\partial H}{\partial x},\,\,H=\frac{p^2}{2m}+V(x)$$
![[double slit]]Here, $I_1(x)$ and $I_2(x)$ are the interference patterns resultant from $S_1$ and $S_2$ respectively. When the electrons are treated as waves, we get the following equations:$$\Huge \frac{\partial^2 \psi}{\partial t^2}-v^2\frac{\partial^2 \psi}{\partial x^2}=0,\,\,\psi(x,t)=e^{ikx-i\omega t},\,\,k=\omega/v$$Where $\psi$ describes the amplitude of the wave at a specific point and time and $v$ is the velocity of the wave. Suppose that $\psi_1(x)$ corresponds to the amplitude at the detector with only $S_1$ open, and $\psi_2(x)$ corresponds to the amplitude at the detector with only $S_2$ open. Assuming that the wave amplitude obeys a linear PDE, then the [[Linear Differential Equations#Principle of Superposition|principle of superposition]] states:$$\Huge \psi(x)=\psi_1(x)+\psi_2(x)$$A characteristic interference pattern is produced when these two waves interfere at $D$. By averaging the energy deposited per unit area over a long time, we define the intensity at a point along the detector $x$. The energy carried by a wave is proportional to the modulus squared of the amplitude, ignoring the constant of proportionality we get:$$\Huge I_1(x)=|\psi_1(x)|^2,\,\,I_2(x)=|\psi_2(x)|^2,\,\,I(x)=|\psi(x)|^2$$We can then directly calculate $I(x)$:$$\Huge\begin{align}
I(x)&=|\psi(x)|^2\\
&=|\psi_1(x)+\psi_2(x)|^2\\
&=|\psi_1(x)|^2+|\psi_2(x)|^2+2\Re(\psi_1(x)\overline{\psi_2(x)})\\
&=I_1(x)+I_2(x)+2\sqrt{I_1(x)I_2(x)}\cos(\delta(x))
\end{align}$$Where $\delta(x)$ is the relative phase of $\psi_1(x)$ and $\psi_2(x)$. The additional term on line 3 described the interference of the waves, known as the interference term. It is the general form of the interference pattern.

To find the exact form of this pattern, we make the following observation:![[double slit 2]]
With this, the total amplitude becomes:$$\Huge \psi(x,t)=C(e^{ikr_1}+e^{ikr_2})e^{-i\omega t}$$And the intensity at the point $x$ becomes:$$\Huge\begin{align}
I(x)&=C^2|e^{ikr_1}+e^{ikr_2}|^2\\
&=2C^2(1+\cos(k(r_1-r_2)))\\
&=4C^2\cos^2\left(\frac{k}{2}(r_1-r_2)\right)
\end{align}$$We see constructive interference at $k(r_1-r_2)=2n\pi$ and destructive interference at $k(r_1-r_2)=(2n+1)\pi$ for some $n\in\mathbb{Z}$. The two right triangles seen above give $r_1$ and $r_2$ as functions of $x$:$$\Huge r_1^2=L^2+\left(x-\frac{a}{2}\right)^2,\,\,r_2^2=L^2+\left(x+\frac{a}{2}\right)^2$$We can use a [[Taylor series]] on $a$ since in reality, this slit will be miniscule. We then get:$$\Huge r_1=\sqrt{L^2+x^2}-\frac{ax}{2\sqrt{L^2+x^2}}+\mathcal{O}(a^2)$$And a similar expression for $r_2$. Subtracting the two and assuming $x<<L$ we get the simple expression $r_2-r_1=\frac{ax}{L}$. Using this in the intensity equation gives:$$\Huge I(x)\approx4C^2\cos^2\left(\frac{ka}{2L}x\right)$$This can be shown as follows:
```desmos-graph
left=-5; right=5;
top=5; bottom=-5;
---
y=4(\cos(\frac{x}{2}))^2
```

