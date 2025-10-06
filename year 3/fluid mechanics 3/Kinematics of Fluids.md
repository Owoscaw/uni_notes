
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