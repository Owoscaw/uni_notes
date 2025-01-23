In quantum mechanics, particles do not have fixed position or generalised momenta. These are assigned according to a complex wave function. The wave function $\psi(x,t)$ is a complex function of position $x$ and time $t$. We define a continuous function:$$\Huge\begin{align}
\psi_t&:\Re\rightarrow\mathbb{C}\\
&:x\mapsto\psi(x,t)
\end{align}$$at each time $t\in\Re$. We also define the probability density as the modulus squared of the wave function:$$\Huge P(x,t):=|\psi(x,t)|^2$$This describes the "probability density" for a measurement at time $t$ to find the particle at position $x$. There are two interpretations of this:
> The probability to find the particle between an infinitesimally small interval $[x, x+dx]$ at time $t$ is $P(x,t)dx$.
> The probability to find the particle in a finite interval $a<x<b$ is:$$\Huge\int_a^bP(x,t)dx$$

Normalisation of the [[Probability definition#Axioms|probability density]] demands that:$$\Huge\int_{-\infty}^\infty P(x,t)dx=1$$For some fixed $t$. The wave function can be normalised with constants to satisfy this condition. Note that the normalisation constant can only be found up to phase, since we are using the complex norm to find it.
![[wave function.png]]

# Expectation values:

For any probability distribution, the [[Expectation#Definition and interpretation|expectation]] value of a polynomial function is given by:$$\Huge\begin{align}
\left<f(x)\right>&:=\int_{-\infty}^\infty f(x)P(x,t)dx\\
&=\int_{-\infty}^\infty f(x)|\psi(x,t)|^2dx
\end{align}$$The expectation value $\langle x\rangle$ is the mean of position measurements over many particles described by the same wave function. We can then define the standard deviation:$$\Huge\Delta x=\sqrt{\langle x^2\rangle-\langle x\rangle^2}$$This is a measure of the spread of the probability distribution around the mean, $\langle x\rangle$. We therefore call this quantity the "uncertainty" in the position.

## Gaussian wave function:
Consider the wave function given by:$$\Huge\psi(x,t)=Ce^{-\frac{x^2}{4\Delta^2}}$$Where $\Delta>0$ has units of length and $C$ is a constant to be determined:$$\Huge\begin{align}
1&=\int_{-\infty}^\infty|\psi(x,t)|^2dx\\
&=|C|^2\int_{-\infty}^\infty e^{-\frac{x^2}{2\Delta^2}}dx\\
&=|C^2|\sqrt{2\Delta^2}\int_{-\infty}^\infty e^{-y^2}dy\\
&=|C^2|\sqrt{2\pi\Delta^2}\implies C=(2\pi\Delta^2)^{-1/4}
\end{align}$$We immediately see that $\langle x^{2n+1}\rangle=0$ for any $n\in\mathbb{Z}_0$, as the integrand is an odd function of $x$. Since $\Delta$ is the only length parameter, we can say that $\langle x^{2n}\rangle\propto\Delta^{2n}$ for $n\in\mathbb{Z}_0$.

## Infinite potential well:
Consider a particle confined to the region $0<x<L$:$$\Huge V(x)=\begin{cases}0&0<x<L\\\infty&\text{otherwise}\end{cases}$$This particle would then require infinite energy to be found in a position $x\leq 0$ or $x\geq L$, so we require that the wave function vanish in these regions. Such a wave function is defined by:$$\Huge\psi(x,t)=\begin{cases}C\sqrt{x(L-x)}&0<x<L\\0&\text{otherwise}\end{cases}$$We can then find the normalisation constant:$$\Huge 1=|C|^2\int_0^Lx(L-x)dx=|C|^2\frac{L^3}{6}$$So therefore $C=\sqrt{\frac{6}{L^3}}e^{i\theta}$. For convenience we set $e^{i\theta}=1$. Again since $L$ is the only parameter in the expression we can say $\langle x^n\rangle\propto L^n$ for any $n\in\mathbb{Z}_0$:$$\Huge\begin{align}
\langle x\rangle&=\frac{6}{L^3}\int_0^Lx^2(L-x)dx=\frac{L}{2}\\
\langle x^2\rangle&=\frac{6}{L^3}\int_0^Lx^3(L-x)dx=\frac{3L^2}{10}
\end{align}$$We can then find the uncertainty:$$\Huge\Delta x=\sqrt{\frac{3L^2}{10}-\left(\frac{L}{2}\right)^2}=\frac{L}{\sqrt{20}}$$
# Phases:

Note that if we multiply the wave function by a position dependent phase, the probability density is unchanged due to the use of the complex norm:$$\Huge \psi(x)\rightarrow e^{i\theta}\psi(x),\,\,P(x)\rightarrow P(x)$$That is to say, measurements of position cannot differentiate between the wave function $\psi(x)$ and $e^{i\theta}\psi(x)$