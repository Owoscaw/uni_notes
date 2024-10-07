A complex number takes the form:$$\Huge z=x+iy$$Where $x,y\in\Re$ and $i=\sqrt{-1}$, the imaginary unit. We can also write:$$\Huge z=\Re(z)+i\Im(z)$$Addition and subtraction work in the following way:$$\Huge z_1\pm z_2:=(x_1\pm x_2)+i(y_1\pm y_2)$$For $z_1,z_2\in \mathbb{C}$. Also:$$z_1z_2=x_1x_2+ix_1y_2+ix_2y_1+i^2y_1y_2=x_1x_2+ix_1y_2+ix_2y_1-y_1y_2=(x_1x_2-y_1y_2)+i(x_1y_2+x_2y_1)$$Since $i^2=-1$.

## Conjugates:

Note that since:$$\Huge (x+iy)(x-iy)=x^2+y^2\in\Re_+$$Motivating the definition of the conjugate:$$\Huge \bar z=x-iy=\Re(z)-i\Im(z)$$We can then define the modulus, $|z|$:$$\Huge |z|=\sqrt{z\bar z}=\sqrt{\Re(z)^2+\Im(z)^2}$$Note that there is no order on $\mathbb{C}$, it does not make sense to compare complex numbers, only their moduli. We can represent conjugacy by reflection in the real axis:![[argand diagram conjugates]]To "realize" the denominator when dividing complex numbers, one must multiply by the conjugate:$$\Huge \frac{z_1}{z_2}=\frac{z_1\bar z_2}{z_2\bar z_2}=\frac{x_1x_2+y_1y_2}{x_2^2+y_2^2}+i\frac{x_2y_1-x_1y_2}{x_2^2+y_2^2}$$A similar process exists for finding $z^{-1}$ by taking $z_1=1,z_2=z$.

# Important properties of complex numbers:

> $z_1z_2=0\iff z_1=0$ or $z_2=0$
> $|z|=\sqrt{z\bar z}$
> $\Re(z)=\frac{z+\bar z}{2}$ and $\Im(z)=\frac{z-\bar z}{2i}$
> $z_{-1}=\frac{\bar z}{|z|^2}$

# Polar form of complex numbers:

We define for any $z\in \mathbb{C}$:$$\Huge |z|:=r,\,\,\arg(z):=\theta=\begin{cases}\arctan\left(\frac{y}{x}\right)&y,x>0\\\frac{\pi}{2}&x=0,y>0\\-\frac{\pi}{2}&x=0,y<0\\\arctan\left(\frac{y}{x}\right)+\pi& x<0,y<0\\\pi-\arctan\left(\frac{y}{x}\right)&x<0,y>0\end{cases}$$Where $r$ is the length of the vector connecting $z$ to the origin, and $\theta$ is the angle it makes with the positive real axis. Note that for any angle, a multiple of $2\pi$ can always be added to give the same complex number. Therefore we assume that $\theta\in(-\pi,\pi]$.