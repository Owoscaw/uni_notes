A curve $C$ is a one dimensional subset of $\Re^n$ usually described by a parametrisation $\underline{x}(t)$:$$\Huge \underline x(t)=x_1(t)\underline e_1+\dots+x_n(t)\underline e_n$$This maps an interval $[t_0,t_1]$ to $\Re^n$:![[line parameterisation]]Here, $\underline e_1,\dots, \underline e_n$ represent the [[Bases and dimensions in RN|standar unit vectors]]. For example, consider the circle $x^2+y^2=a^2$ in $\Re^2$. We look for a parametrisation $\underline x(t)$:![[circle parametrisation]]A curve is closed if $\underline x(t_0)=\underline x(t_1)$. A curve is simple if it does not intersect itself. 

Consider the helix $\underline x(t)=\cos t \underline e_1+\sin t \underline e_2+t \underline e_3$ for $t\in[0,6\pi]$. We see $\underline x(0)=\underline e_1$ and $\underline x(6\pi)=\underline e_1+6\pi \underline e_3$, so the curve is not closed.

## Tangent vectors:

A parametrisation of a curve, $\underline x(t)$, is differentiable if it has a well defined tangent vector:$$\Huge \frac{d \underline x}{dt}=\lim_{dt\to 0}\frac{\underline x(t+dt)-\underline x(t)}{dt}$$![[curve tangent vector]]Note that the tangent vector is a velocity, making $\left|\frac{d \underline x}{dt}\right|$ the speed at $\underline x(t)$.

## Different parametrisations:

The parametrisation of a curve is not unique, different speeds and different directions can parameterise the same curve. 

For example, take the parametrisation $\underline x(t)=\underline a+t(\underline b-\underline a)$ for $t\in[0,1], \underline a,\underline b\in\Re^n$:$$\Huge \frac{d \underline x}{dt}=\underline b- \underline a$$Another example, where $\underline x(t)=\underline a+\sin(t)(\underline b-\underline a)$ for $t\in[0,\frac{\pi}{2}]$:$$\Huge \frac{d \underline x}{dt}=\cos(t)(\underline b-\underline a)$$Both of these describe the same straight line between $\underline a$ and $\underline b$, however they travel at different velocities, since their derivatives are not the same (one is constant, one has a cosine term).

If $\underline x(t)$ and $\underline x(\tau)$ are two parametrisations of the same curve, then the [[Leibniz and Chain rules|chain rule]] dictates that:$$\Huge \frac{d \underline x}{dt}=\frac{d \underline x}{d\tau}\frac{d\tau}{dt}$$
A parametrisation $\underline x(t)$ is regular if $\frac{d \underline x}{dt}\neq0$ everywhere, otherwise it is singular. The points at which a parametrisation is singular are called cusps.

# Line integrals of Scalar Fields:

A scalar field on $\Re^n$ is a map $f:\Re^n\mapsto\Re$. The line integral of a scalar field $f(\underline x)$ along a curve $C$ with parametrisation $\underline x(t)$ for $t\in[t_0,t_1]$ is defined as:$$\Huge \int_Cf(x)dl=\int_{t_0}^{t_1}f(\underline x(t))\left|\frac{d \underline x}{dt}\right|dt$$Take $f(\underline x)=y+x^2$ integrated around the unit circle as an example:![[line integral example]]The meaning of the line integral can be thought of as summing the values of $f$ along the line $C$.

We propose that the line integral of a scalar field is independent of parametrisation. We prove this by considering two possible parametrisations of the same curve, $\underline x(t)$ and $\underline x(\tau)$ for $t\in[t_0,t_1]$ and $\tau\in[\tau_0,\tau_1]$. The chain rule also dictates:$$\Huge \frac{d \underline x}{dt}=\frac{d\tau}{dt}\frac{d \underline x}{d\tau}\implies \left|\frac{d \underline x}{dt}\right|=\left|\frac{d\tau}{dt}\right|\left|\frac{d \underline x}{d\tau}\right|$$There are now two cases, where both curves are parametrised in the same direction, that is $\underline x(t_0)=\underline x(\tau_0)$, then:$$\large \frac{d\tau}{dt}>0\implies\int_{t_0}^{t_1}f(\underline x(t))\left|\frac{d \underline x}{dt}\right|dt=\int_{t_0}^{t_1}f(\underline x(t))\left|\frac{d \underline x}{d\tau}\right|\frac{d\tau}{dt}dt=\int_{\tau_0}^{\tau_1}f(\underline x(\tau))\left|\frac{d \underline x}{d\tau}\right|d\tau$$The other case is where they are parametrised in opposing directions, that is $\underline x(t_0)= \underline x(\tau_1)$, then:$$\small \frac{d\tau}{dt}<0\implies\int_{t_0}^{t_1}f(\underline x(t))\left|\frac{d \underline x}{dt}\right|dt=\int_{t_0}^{t_1}f(\underline x(t))\left|\frac{d \underline x}{dt}\right|\left(-\frac{d\tau}{dt}\right)dt=-\int_{\tau_1}^{\tau_0}f(\underline x(\tau))\left|\frac{d \underline x}{d\tau}\right|=\int_{\tau_0}^{\tau_1}f(\underline x(\tau))\left|\frac{d \underline x}{d\tau}\right|d\tau$$The last step switches the bounds of integration to get rid of the negative sign and show that the line integral is indeed independent of choice of parametrisation.

## Arclength:

There is a special case where $f(\underline x)=1$, then the line integral is called the arclength of the curve:$$\Huge L=\int_Cdl=\int_{t_0}^{t_1}\left|\frac{d \underline x}{dt}\right|dt$$Which represents the geometric length of the path taken. There is always an arclength parametrisation $\underline x(s)$ where $\left|\frac{d \underline x}{ds}\right|=1$ along the entire curve. Then $s$ is distance, making the length $L=\int_0^Lds$. Using our example from before:![[arclength example]]
# Line integrals of vector fields:

A vector field is a function $\underline f:\Re^n\mapsto\Re^n$ that assigns a vector to each point in $\Re^n$. Here you can see the vector field $\underline f(\underline x)=- \underline x$ in $\Re^2$:
```desmos-graph
left=-2; right=2;
top=2; bottom=-2;
---
F\left(x,y\right)=\left(-x,-y\right)
m\left(x\right)=3\left(\sqrt{s_{x}s_{y}}\log\left(x+1\right)\right)
l\left(x\right)=0.4x
b=1
\left(x_{0}+tm\left(M\left(F\left(x_{0},y_{0}\right)\right)\right)\cos\left(A\left(F\left(x_{0},y_{0}\right)\right)\right),y_{0}+tm\left(M\left(F\left(x_{0},y_{0}\right)\right)\right)\sin\left(A\left(F\left(x_{0},y_{0}\right)\right)\right)\right)
\left(x_{0}+m\left(M\left(F\left(x_{0},y_{0}\right)\right)\right)\cos\left(A\left(F\left(x_{0},y_{0}\right)\right)\right)+tl\left(m\left(M\left(F\left(x_{0},y_{0}\right)\right)\right)\right)\cos\left(A\left(F\left(x_{0},y_{0}\right)\right)-b-\frac{\pi}{2}\right),y_{0}+m\left(M\left(F\left(x_{0},y_{0}\right)\right)\right)\sin\left(A\left(F\left(x_{0},y_{0}\right)\right)\right)+tl\left(m\left(M\left(F\left(x_{0},y_{0}\right)\right)\right)\right)\sin\left(A\left(F\left(x_{0},y_{0}\right)\right)-b-\frac{\pi}{2}\right)\right)
\left(x_{0}+m\left(M\left(F\left(x_{0},y_{0}\right)\right)\right)\cos\left(A\left(F\left(x_{0},y_{0}\right)\right)\right)+tl\left(m\left(M\left(F\left(x_{0},y_{0}\right)\right)\right)\right)\cos\left(A\left(F\left(x_{0},y_{0}\right)\right)+b+\frac{\pi}{2}\right),y_{0}+m\left(M\left(F\left(x_{0},y_{0}\right)\right)\right)\sin\left(A\left(F\left(x_{0},y_{0}\right)\right)\right)+tl\left(m\left(M\left(F\left(x_{0},y_{0}\right)\right)\right)\right)\sin\left(A\left(F\left(x_{0},y_{0}\right)\right)+b+\frac{\pi}{2}\right)\right)
A\left(p\right)=\left\{p.x>0:\left\{p.y\ge0:\tan^{-1}\left(\frac{p.y}{p.x}\right),\tan^{-1}\left(\frac{p.y}{p.x}\right)+2\pi\right\},\left\{p.x<0:\tan^{-1}\left(\frac{p.y}{p.x}\right)+\pi,\left\{p.y>0:\frac{\pi}{2},\left\{p.y<0:\frac{3\pi}{2}\right\}\right\}\right\}\right\}
M\left(p\right)=\sqrt{p.x^{2}+p.y^{2}}
y_{0}=p_{y}-s_{y}\operatorname{floor}\left(\frac{i-1}{n_{x}}\right)
x_{0}=p_{x}+s_{x}\operatorname{mod}\left(i-1,n_{x}\right)
i=\left[1,...,n_{x}n_{y}\right]
n_x=13
n_y=13
s_x=0.2
s_y=0.2
p_x=-1.2
p_y=1.2
```

For a curve with parametrisation $\underline x(t)$ for $t\in[t_0,t_1]$, the unit tangent vector is:$$\Huge \hat{ \underline t}=\frac{d \underline x}{dt}\div\left|\frac{d \underline x}{dt}\right|$$An oriented curve is a curve together with a specified, consistent choice of $\hat{ \underline t}$. The line integral of a vector field $\underline f(\underline x)$ along an oriented curve, $C$, with parametrisation $\underline x(t)$ for $t\in[t_0,t_1]$ is defined as:$$\Huge \int_C\underline f\cdot \hat{}$$
