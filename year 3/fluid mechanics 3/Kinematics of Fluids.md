
# What is a fluid?

On a human scale, we perceive a fluid as a continuous indivisible object, formally known as the continuum hypothesis. A continuum is a substance such that an infinitesimally small volume of the continuum can be taken, without the overall properties of the fluid changing. A fluid has the properties;
> Density, $\rho(\underline x, t)$, is formally described by the limit of change in mass over change in volume:$$\Huge \rho (\underline x,t)=\lim_{\delta V\to 0}\frac{\delta M}{\delta V}$$Note that this defines density at a point, whereas points have no volume. This makes the above definition reliant on the continuum hypothesis.
> Velocity, $\underline u(\underline x,t)$

Small $\delta V$ are known as fluid elements and exhibit the same properties as the fluid itself. Taking the limit $\delta V\to0$ allows for the definition of point density as well as the notion of a fluid particle.

# Fluid motion:

Consider a funnel:![[Kinematics of Fluids 2025-10-06 10.29.15.excalidraw]]Here, we expect $|\underline u_1|<|\underline u_2|$, so the fluid must be accelerating. However, we see that water is pumped in and flows out at a steady rate, so cannot be accelerating. This is a matter of perspective and leads to two descriptions of velocity:
> Eulerian: A fixed point $\underline x$ is chosen and we ask the velocity of the fluid at particle $\underline x$ at a given time $t$. (Bear)
> Lagrangian: A particle at fixed point $\underline a$ is chosen and is tracked. We ask what is the velocity of the fluid particle that started at $\underline a$ at a given time $t$. (Fish)

# Visualising Fluid motion:

## Particle paths:
A particle path is the path $\underline x(t)$ of a fluid particle over time. To find $\underline x(t)$ we must solve:$$\Huge \frac{d \underline x(t)}{dt}=\underline u(\underline x(t),t)$$subject to initial conditions, where $\underline u$ is the Eulerian velocity. As an example, we aim to find the path of a particle in the 2-D flow described by:$$\Huge \underline u(\underline x,t)=x\underline e_x-y\underline e_y$$given $\underline x(0)=\underline a$. We then have to solve:$$\Huge\begin{align}
\frac{d x}{dt}=x,\,\,x(0)=a,\,\,\frac{d y}{dt}=-y,\,\,y(0)=b
\end{align}$$Which has solution:$$\Huge \underline x(\underline a,t)=\begin{pmatrix}ae^t\\be^{-t}\end{pmatrix}$$Note that at $\underline x=\underline 0$ we have that $\underline u=\underline 0$, this is known as a stagnation point.

The material curve is a line that moves with the flow. It can be thought of as the line that threads many fluid particles together. This motivates the definition of a material surface as a surface that moves with the flow.

# Streaklines:

A streakline is a curve comprised of all fluid elements that have passed through a given point in the past. To determine a streakline at a given time, we must find the particles that have previously passed through some given point $\underline a$. Naming the release time $\tau$ we must solve:$$\Huge \frac{d \underline x}{dt}=\underline u(\underline x,t),\,\,\underline x(\tau)=\underline a$$
As an example, consider the flow defined by $\underline e=\underline e_x+t\underline e_y$ and aim to find the streakline at a fixed time $t_0$ of particles that are released from $\underline a$ since time $t=0$. The [[Linear Differential Equations|ODEs]] to solve are therefore:$$\Huge\begin{align}
\frac{d x}{dt}&=1,\,\,x(\tau)=a\\
\frac{d y}{dt}&=1,\,\,y(\tau)=b
\end{align}$$Integrating and fixing $t=t_0$ gives:$$\Huge \underline x(\underline a,t,\tau)|_{t=t_0}=(t_0-\tau=a)\underline e_x+\left(\frac{t_0^2}{2}-\frac{\tau^2}{2}+b\right)\underline e_y$$Note that since $t_0$ is fixed, the streakline is parametrised by $\tau$. Sometimes, $\tau$ can be eliminated entirely to get the explicit equation of the streakline at time $t_0$. We have that $x=t_0-\tau+a$, so we can write the equation as:$$\Huge y=\frac{t_0^2}{2}+b-\frac{1}{2}(t_0+a-x)^2$$Note that this equation describes the streakline of all particles that pass through $\underline a$, so restricting $\tau\in[0,t_0]$ we get $x\in[a,t_0+a]$. This gives the required streakline.

The key difference between particle paths and streaklines is that particle paths describe a single particle over time, whereas a streakline describes the position of many particles at a single given time.

# Streamlines

A streamline is a line parallel to the velocity vector $\underline u(\underline x,t)$ at a fixed time $t=t_0$. It is often used to visualise the velocity field at a given time, as a streamline can be draw through any fixed point $\underline x_0$. A streamline is a curve $\underline x(s)$ that satisfies:
$$\Huge \frac{d\underline x}{ds}=\underline u(\underline x(s),t_0)$$
where $t_0$ is fixed and $s$ is a parameter that varies through the streamline. To obtain the streamline passing through $\underline x_0$ we must also specify the condition $\underline x(0)=\underline x_0$. As an example, consider the flow described previously ($\underline u=\underline e_x+t\underline e_y$). Then the ODEs become:$$\Huge\begin{align}
\frac{d x}{ds}&=1,\,\,x(0)=x_0\\
\frac{d y}{ds}&=t_0,\,\,y(0)=y_0
\end{align}$$Integrating the first expression gives $x=s+x_0$, and the second gives $y=t_0s+t_0$. Once again we can eliminate the parametrising variable $s$ to give the explicit equation for the streamlines:$$\Huge y=t_0(x-x_0)+y_0$$Note that the pattern of streamlines changes over time, as $\underline u$ depends on $t$ (unsteady flow). Note that for steady flows, streamlines, particle paths, and streaklines all coincide.

## Streamlines as boundaries:
As streamlines are defined to be parallel to the velocity, there must be no flow normal to a streamline. This condition is known as the no normal flow condition and is formally written as:$$\Huge \underline u\cdot\underline{\hat{n}}=0$$
Boundaries are impermeable to fluid flow, so the no normal flow condition must apply along the boundary, making the boundary itself a streamline.