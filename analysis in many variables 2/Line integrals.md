A curve $C$ is a one dimensional subset of $\Re^n$ usually described by a parametrisation $\underline{x}(t)$:$$\Huge \underline x(t)=x_1(t)\underline e_1+\dots+x_n(t)\underline e_n$$This maps an interval $[t_0,t_1]$ to $\Re^n$:![[line parameterisation]]Here, $\underline e_1,\dots, \underline e_n$ represent the [[Bases and dimensions in RN|standar unit vectors]]. For example, consider the circle $x^2+y^2=a^2$ in $\Re^2$. We look for a parametrisation $\underline x(t)$:![[circle parametrisation]]A curve is closed if $\underline x(t_0)=\underline x(t_1)$. A curve is simple if it does not intersect itself. 

Consider the helix $\underline x(t)=\cos t \underline e_1+\sin t \underline e_2+t \underline e_3$ for $t\in[0,6\pi]$. We see $\underline x(0)=\underline e_1$ and $\underline x(6\pi)=\underline e_1+6\pi \underline e_3$, so the curve is not closed.

## Tangent vectors:

A parametrisation of a curve, $\underline x(t)$, is differentiable if it has a well defined tangent vector:$$\Huge \frac{d \underline x}{dt}=\lim_{dt\to 0}\frac{\underline x(t+dt)-\underline x(t)}{dt}$$![[curve tangent vector]]Note that the tangent vector is a velocity, making $\left|\frac{d \underline x}{dt}\right|$ the speed at $\underline x(t)$.

## Different parametrisations:

The parametrisation of a curve is not unique, different speeds and different directions can parameterise the same curve. 

For example, take the parametrisation $\underline x(t)=\underline a+t(\underline b-\underline a)$ for $t\in[0,1], \underline a,\underline b\in\Re^n$:$$\Huge \frac{d \underline x}{dt}=\underline b- \underline a$$Another example, where $\underline x(t)=\underline a+\sin(t)(\underline b-\underline a)$ for $t\in[0,\frac{\pi}{2}]$:$$\Huge \frac{d \underline x}{dt}=\cos(t)(\underline b-\underline a)$$Both of these describe the same straight line between $\underline a$ and $\underline b$, however they travel at different velocities, since their derivatives are not the same (one is constant, one has a cosine term).

If $\underline x(t)$ and $\underline x(\tau)$ are two parametrisations of the same curve, then the [[Leibniz and Chain rules|chain rule]] dictates that:$$\Huge \frac{d \underline x}{dt}=\frac{d \underline x}{d\tau}\frac{d\tau}{dt}$$
## Regular parametrisations:

A parametrisation $\underline x(t)$ is regular if $\frac{d \underline x}{dt}\neq0$ everywhere, otherwise it is singular. The points at which a parametrisation is singular are called cusps.