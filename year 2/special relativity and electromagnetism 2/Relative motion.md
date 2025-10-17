
# Relativistic velocity addition:

The [[Lorentz transformations#Lorentz boosts|SLT]] is written in matrix form as:$$\Huge \begin{pmatrix}ct'\\x'\end{pmatrix}=\begin{pmatrix}\gamma&-\frac{\gamma v}{c}\\-\frac{\gamma v}{c}&\gamma\end{pmatrix}\begin{pmatrix}ct\\x\end{pmatrix}=L(v)\begin{pmatrix}ct\\x\end{pmatrix}$$Where:$$\Huge L(v)=\frac{\gamma}{c}\begin{pmatrix}c&-v\\-v&c\end{pmatrix}$$This satisfies:
> $\det(L(v))=1$
> $(L(v))^T=L(v)$
> $(L(v))^{-1}=L(-v)$

We can then compute the result of applying two successive SLTs with velocities $v_1,v_2$ respectively:$$\Huge\begin{align}
L(v_2)L(v_1)&=\frac{\gamma_1\gamma_2}{c^2}\begin{pmatrix}c&-v_2\\-v_2&c\end{pmatrix}\begin{pmatrix}c&-v_1\\-v_1&c\end{pmatrix}\\
&=\frac{\gamma_1\gamma_2}{c^2}\begin{pmatrix}c^2+v_1v_2&-c(v_1+v_2)\\-c(v_1+v_2)&c^2+v_1v_2\end{pmatrix}=L(v)
\end{align}$$Where:$$\Huge v=\frac{v_1+v_2}{1+\frac{v_1v_2}{c^2}}$$The [[Lorentz transformations#Galilean boost|Galilean velocity addition]] formula is a good approximation when $v_1,v_2<<c$ as the denominator in this expression is close to $1$.

# Rapidity:

As speeds are limited by $c$, we use the parametrisation:$$\Huge v=c\tanh\theta$$Where $\theta$ is known as the rapidity. We can write $\gamma$ in terms of rapidity:$$\Huge \gamma=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}}=\frac{1}{\sqrt{1-\tanh^2\theta}}=\frac{1}{\sqrt{\text{sech}^2\theta}}=\cosh\theta$$And therefore:$$\Huge v\gamma=c\tanh\theta\cosh\theta=c\sinh\theta$$Using this in the matrix form of the SLT gives:$$\Huge L(v)=\begin{pmatrix}\cosh\theta&-\sinh\theta\\-\sinh\theta&\cosh\theta\end{pmatrix}$$Which is similar to a rotation matrix, only hyperbolic. Writing the relativistic velocity addition formula in terms of rapidity:$$\Huge c\tanh\theta=\frac{c(\tanh\theta_1+\tanh\theta_2)}{1+\tanh\theta_1\tanh\theta_2}=c\tanh(\theta_1+\theta_2)$$So we see that rapidities add, similar to the addition of angles in successive rotations.

# Relativistic Doppler effect:

The Doppler effect involves the observed change in frequency of a wave for an observer moving relative to a source. The relativistic Doppler effect is similar but different:![[relative doppler]]
Consider a light source that moves with velocity $v$ towards an observer. In the rest frame of the source, waves are emitted with frequency $f_0$, we aim to calculate $f$, the frequency of waves at the observer. Let $T$ be the time interval between the emission of successive wave crests, measured at the observer. The first wave is emitted at $t=0$ and the second at $t=T$. At the latter time, the first wave has moved a distance $cT$ closer to the observer and the source has moved a distance $vT$ closer to the observer. The distance between the two waves is the wavelength $\lambda$ that is measured at the observer, that is:$$\Huge \lambda=(c-v)T$$Which corresponds to the frequency:$$\Huge f=\frac{c}{\lambda}=\frac{c}{(c-v)T}$$
In the rest frame of the source, $T_0=1/f_0$ is the period. By time dilation we find:$$\Huge T=\gamma T_0=\frac{\gamma}{f_0}$$Using this expression to find the frequency gives:$$\Huge\begin{align}
f&=f_0\frac{c}{\gamma(c-v)}\\
&=f_0\frac{c\sqrt{1-v^2/c^2}}{c-v}\\
&=f_0\frac{\sqrt{c^2-v^2}}{c-v}\\
&=f_0\sqrt{\frac{(c+v)(c-v)}{(c-v)^2}}=f_0\sqrt{\frac{c+v}{c-v}}
\end{align}$$So when the source is moving towards the observer we see that the observed frequency$$\Huge f=f_0\sqrt{\frac{c+v}{c-v}}>f_0$$is greater than the emitted frequency. This can also be written as:$$\Huge \lambda=\lambda_0\sqrt{\frac{c-v}{c+v}}<\lambda_0$$An increase in wavelength relative to the observer is called redshift, whereas a decrease in wavelength relative to the observer is called blueshift.