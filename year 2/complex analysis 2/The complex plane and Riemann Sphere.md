A complex number takes the form:$$\Huge z=x+iy$$Where $x,y\in\Re$ and $i=\sqrt{-1}$, the imaginary unit. We can also write:$$\Huge z=\Re(z)+i\Im(z)$$Addition and subtraction work in the following way:$$\Huge z_1\pm z_2:=(x_1\pm x_2)+i(y_1\pm y_2)$$For $z_1,z_2\in \mathbb{C}$. Also:$$z_1z_2=x_1x_2+ix_1y_2+ix_2y_1+i^2y_1y_2=x_1x_2+ix_1y_2+ix_2y_1-y_1y_2=(x_1x_2-y_1y_2)+i(x_1y_2+x_2y_1)$$Since $i^2=-1$.

## Conjugates:

Note that since:$$\Huge (x+iy)(x-iy)=x^2+y^2\in\Re_+$$Motivating the definition of the conjugate:$$\Huge \bar z=x-iy=\Re(z)-i\Im(z)$$We can then define the modulus, $|z|$:$$\Huge |z|=\sqrt{z\bar z}=\sqrt{\Re(z)^2+\Im(z)^2}$$Note that there is no order on $\mathbb{C}$, it does not make sense to compare complex numbers, only their moduli. We can represent conjugacy by reflection in the real axis:![[argand diagram conjugates]]To "realize" the denominator when dividing complex numbers, one must multiply by the conjugate:$$\Huge \frac{z_1}{z_2}=\frac{z_1\bar z_2}{z_2\bar z_2}=\frac{x_1x_2+y_1y_2}{x_2^2+y_2^2}+i\frac{x_2y_1-x_1y_2}{x_2^2+y_2^2}$$A similar process exists for finding $z^{-1}$ by taking $z_1=1,z_2=z$.

# Important properties of complex numbers:

> $z_1z_2=0\iff z_1=0$ or $z_2=0$
> $|z|=\sqrt{z\bar z}$
> $\Re(z)=\frac{z+\bar z}{2}$ and $\Im(z)=\frac{z-\bar z}{2i}$
> $z_{-1}=\frac{\bar z}{|z|^2}$

# Polar form of complex numbers:

We define for any $z\in \mathbb{C}$:$$\Huge |z|:=r,\,\,\arg(z):=\theta=\begin{cases}\arctan\left(\frac{y}{x}\right)&y,x>0\\\frac{\pi}{2}&x=0,y>0\\-\frac{\pi}{2}&x=0,y<0\\\arctan\left(\frac{y}{x}\right)+\pi& x<0,y>0\\\arctan\left(\frac{y}{x}\right)-\pi&x<0,y<0\end{cases}$$Where $r$ is the length of the vector connecting $z$ to the origin, and $\theta$ is the angle it makes with the positive real axis. Note that for any angle, a multiple of $2\pi$ can always be added to give the same complex number. Therefore we assume that $\theta\in(-\pi,\pi]$. Now we have the polar coordinates for $z$:$$\Huge z=r(\cos\theta+i\sin\theta)$$In this form, we get the following properties:
> $\arg(z_1z_2)=(\arg(z_1)+\arg(z_2))\mod 2\pi$
> $\arg\left(\frac{1}{z}\right)=-\arg(z)\mod2\pi$
> $\arg(\bar z)=-\arg(z)\mod2\pi$

To prove the first property, simply multiply:$$\small z_1z_1=r_1r_2(\cos\theta_1+i\sin\theta_1)(\cos\theta_2+i\sin\theta_2)=r_1r_2(\cos\theta_1\cos\theta_2+i\cos\theta_1\sin\theta_2+i\sin\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2)$$$$ z_1z_2=r_1r_2((\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2)+i(\cos\theta_1\sin\theta_2+\sin\theta_1\cos\theta_2))=r_1r_2(\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2))$$This corresponds to scaling the point $z_1$ by $r_2$ and rotating an additional $\theta_2$. Lovely geometry. Using the definition $e^{i\theta}=\cos\theta+i\sin\theta$, we can also see this result. This definition also motivates the result:$$\Huge (\cos\theta+i\sin\theta)^n=\cos(n\theta)+i\sin(n\theta)$$This can be proven by induction. The modulus also has the following properties:
> $|z_1+z_2|\leq|z_1|+|z_2|$
> $|z|\geq0$ with $|z|=0\iff z=0$
> $\max(|\Re(z)|,|\Im(z)|)\leq|z|\leq|\Re(Z)|+|\Im(z)|$

We then define the following functional expressions and domains:

| Functional expression                        | Domain in $\mathbb{C}$      |
| -------------------------------------------- | --------------------------- |
| $\mathbb{D}:=\{z\in \mathbb{C}:\|z\|<1\}$    | Unit disc                   |
| $\mathbb{H}:=\{z\in \mathbb{C}:\Im(z)>0\}$   | Upper half plane            |
| $\mathbb{H}_R:=\{z\in \mathbb{C}:\Re(z)>0\}$ | Right half plane            |
| $\mathbb{H}_L:\{z\in \mathbb{C}:\Re(z)<0\}$  | Left half plane             |
| $\arg(z)=\pi/4$                              | Ray with angle $\pi/4$      |
| $\{z\in \mathbb{C}:\|z-i\|=4\}$              | Circle at $i$ at radius $4$ |
This is how to define shapes in the complex plane.

# The Riemann Sphere:

One can think of $\mathbb{C}$ as a part of a sphere. Let $S^2=\{(\xi,\nu,\zeta)\in\Re^3:\xi^2+\eta^2+\zeta^2=1\}$. Now think of the complex plane as the $xy$ plane in $\Re^3$. Any point in $S^2\setminus\{N\}$ can be assigned a unique point in $\mathbb{C}$ which we denote as $p(\xi,\eta,\zeta)$, the stereographic projection of $(\xi,\eta,\zeta)$. To find the stereographic projection, we connect the point $(\xi,\eta,\zeta)$ to the north pole $N$ with a straight line. Said line intersects the complex plane at a unique point, $P(\xi,\eta,\zeta)$:![[Riemann projection.png]]
For a given $(\xi,\eta,\zeta)\in S^2\setminus\{N\}$, the connecting line is given by:$$\Huge \gamma(t)=N+\left(\begin{pmatrix}\xi\\\eta\\\zeta\end{pmatrix}-N\right)t=\begin{pmatrix}0\\0\\1\end{pmatrix}+\begin{pmatrix}\xi\\\eta\\\zeta-1\end{pmatrix}t=\begin{pmatrix}\xi t\\\eta\,t\\1+(\zeta-1)t\end{pmatrix}$$The intersection with $\mathbb{C}$ happens at $\gamma(t_0)$, where $t_0$ is such that:$$\Huge 1+(\zeta-1)t_0=0$$Note that $\zeta\neq1$ since we require $(\xi,\eta,\zeta)\in S^2\setminus\{N\}$. Plugging this into $\gamma(t)$ we get that:$$\Huge t_0=\frac{1}{1-\zeta}$$