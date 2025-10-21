
# What is a fluid?

On a human scale, we perceive a fluid as a continuous indivisible object, formally known as the continuum hypothesis. A continuum is a substance such that an infinitesimally small volume of the continuum can be taken, without the overall properties of the fluid changing. A fluid has the properties;
> Density, $\rho(\underline x, t)$, is formally described by the limit of change in mass over change in volume:$$\Huge \rho (\underline x,t)=\lim_{\delta V\to 0}\frac{\delta M}{\delta V}$$Note that this defines density at a point, whereas points have no volume. This makes the above definition reliant on the continuum hypothesis.
> Velocity, $\underline u(\underline x,t)$

Small $\delta V$ are known as fluid elements and exhibit the same properties as the fluid itself. Taking the limit $\delta V\to0$ allows for the definition of point density as well as the notion of a fluid particle.

# Fluid motion:

Consider a funnel:![[Lagrangian vs Eulerian]]Here, we expect $|\underline u_1|<|\underline u_2|$, so the fluid must be accelerating. However, we see that water is pumped in and flows out at a steady rate, so cannot be accelerating. This is a matter of perspective and leads to two descriptions of velocity:
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

# The material derivative:

Suppose that we have a quantity $\alpha(\underline x,t)$. Fixing position we would like to see how it changes in time. In this case, all the information we have is:$$\Huge \frac{d \alpha}{dt}=\frac{\partial \alpha}{\partial t}$$since $\underline x$ is fixed. If we follow a fluid particle instead of fixing $\underline x$ we can use the chain rule alongside the equation that determines [[Kinematics of Fluids#Particle paths|particle paths]]:$$\Huge\begin{align}
\frac{d \alpha}{dt}&=\frac{d }{dt}(\alpha(\underline x(t),t))\\
&=\frac{\partial \alpha}{\partial t}\frac{d t}{dt}+\frac{\partial \alpha}{\partial \underline x}\cdot\frac{d \underline x}{dt}\\
&=\left(\frac{\partial }{\partial t}+\underline u\cdot\underline{\nabla}\right)\alpha
\end{align}$$This type of derivative is called the material derivative. The first term on the operator acting on $\alpha$ represents the time derivative from the fixed $\underline x$ point of view, whereas the second term represents the change due to the fluid particle being carried to a new position along the gradient of $\alpha$. We write this as:$$\Huge \frac{D}{Dt}=\frac{\partial }{\partial t}+\underline u\cdot\underline{\nabla}$$The key ideas for the material derivative are:
> $D/Dt$ is applied in the Eulerian reference frame
> It is the rate of change following the particle on its journey (Lagrangian reference frame)
> This is a bridge between Eulerian and Lagrangian physics

# Conservation of mass:

Consider a mass $m$ of fluid inside a fixed fluid volume $V$ with surface $S$. The mass is the integral of the density:$$\Huge m=\int_V\rho\,dV$$Although volume is fixed, the mass can change as fluid particles enter and leave the volume:![[Kinematics of Fluids 2025-10-14 02.23.11.excalidraw]]The mass that leaves $V$ through $S$ per unit time is the integral of all the mass leaving $V$ outward through each $dS$:$$\Huge\begin{align}
-\frac{d m}{dt}&=-\frac{d }{dt}\int_V\rho\,dV\\
&=\int_S\rho(\underline u\cdot\underline{\hat{n}})dS\\
&=\int\rho\underline u\cdot d\underline S
\end{align}$$As volume is fixed, we can differentiate under the integral (Leibniz' integral rule) at step 1 and use the [[Integral theorems#Divergence theorem|divergence theorem]] on step 3 to get:$$\Huge \int_V\left(\frac{\partial \rho}{\partial t}+\underline{\nabla}\cdot(\rho\underline u)\right)dV=0$$This is true for any volume $V$, so the integrand itself must be zero. Additionally if we use the product rule for the divergence:$$\Huge \underline{\nabla}\cdot(\rho\underline u)=\underline u\cdot\underline{\nabla}\rho+\rho\underline{\nabla}\cdot\underline u$$we can write the integrand using the material derivative to get the continuity equation:$$\Huge \frac{D\rho}{Dt}+\rho\underline{\nabla}\cdot\underline u=0$$
These are essentially two methods to get the same result. We fixed the volume and let mass vary, the Eulerian approach. The Lagrangian approach is to fix mass and vary the surface by making it a fluid element. No fluid will enter or leave the fluid element, however the shape (and therefore the surface) will instead deform with the flow. 

## Incompressibility:
An approximation we can make for a large class of fluids is that the density of a fluid element doesn't change as it moves (incompressible flow). This condition ($D\rho/Dt=0$) reduces the above equation to:$$\Huge \underline{\nabla}\cdot\underline u=0$$That is to say, the velocity is divergence free.

# The stream function:

If $u$ is both incompressible and two-dimensional we can encode velocity and streamlines inside a single scalar function. We define our velocity $\underline u=\begin{pmatrix}u\\v\end{pmatrix}$ where $u(x,y),v(x,y)$, and consider:$$\Huge \underline F=\begin{pmatrix}-v\\u\end{pmatrix}$$We can show that $\underline F$ is a conservative vector field by finding its integral over a closed curve. Let the closed curve $C$ enclose a region $R$:$$\Huge\begin{align}
\oint_C\underline F\cdot d\underline x&=\oint_C(-v\,dx+u\,dy)\\
&=\iint_R\left(\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}\right)dx\,dy\\
&=\iint_R\underline{\nabla}\cdot\underline u\,dx\,dy=0
\end{align}$$where we used [[Integral theorems#Green's theorem|Green's theorem]] and the fact that $\underline u$ is incompressible (divergence free). We know that conservative vector fields can be written as the gradient of a scalar field. Therefore there exists some $\psi=\psi(x,y)$ such that $\nabla\psi=\underline F$. Such scalar $\psi$ can therefore encode the velocity field, known as the stream function. Equivalently, we write:$$\Huge \underline u=\underline{\nabla}\times(\psi\underline{\hat e}_z)$$
Consider $\underline{u}\cdot\underline{\nabla}\psi$:$$\Huge\underline{u}\cdot\underline{\nabla}\psi=\begin{pmatrix}u \\ v\end{pmatrix}\cdot\begin{pmatrix}-v \\ u\end{pmatrix}=-uv+uv=0$$That is, $\underline{u}$ is perpendicular to $\underline{\nabla}\psi$, so $\underline{u}$ is parallel to lines of constant $\psi$, or $\psi=\text{constant}$ are like streamlines.

## Stream functions to measure flux:
Take two points on a streamline and draw a curve, $C$, between them. We then ask what the total [[Surface and volume integrals#Surface integrals of vector fields|flux]] through the curve is:![[Kinematics of Fluids 2025-10-19 03.27.46.excalidraw]]Flux is simply defined as the total amount of fluid passing through the curve:$$\Huge\int_C\underline{u}\cdot\underline{\hat{n}}\,ds$$No flow can pass through the streamline, as the streamline is parallel to the velocity. Therefore there is only one way in and out of the region enclosed by the streamline and $C$. By mass conservation, the total flow in must equal total flow out and:$$\Huge\int_C\underline{u}\cdot\underline{\hat{n}}\,ds=0$$Consider the case where $C$ connects two points on different streamlines:![[Kinematics of Fluids 2025-10-19 03.31.49.excalidraw]]Let $C$ have tangent vector $\underline{t}(s)$. The unit normal to $C$ is then given as:$$\Huge\underline{\hat{n}}=\frac{1}{|\underline{t}|}\begin{pmatrix}t_y \\ -t_x\end{pmatrix}$$The flux through $C$ in this direction is therefore:$$\Huge\begin{align*}
\int_C\underline{u}\cdot\underline{\hat{n}}\,ds&=\int_C\begin{pmatrix}\frac{\partial \psi}{\partial y}\\
-\frac{\partial \psi}{\partial x}\end{pmatrix}\cdot\frac{1}{|\underline{t}|}\begin{pmatrix}t_u\\
-t_x\end{pmatrix}ds\\
&=\int_C\frac{\underline{\nabla}\psi\cdot\underline{t}}{|\underline{t}|}ds\\
&=\int_C\underline{\nabla}\psi\cdot d\underline{x}=\psi(\underline{x_2})-\psi(\underline{x_1})
\end{align*}$$which is path independent. Therefore we conclude that the flux (clockwise about $\underline{x_1}$) across any line between two points $\underline{x_1}$ and $\underline{x_2}$ is given by $\psi(\underline{x_2})-\psi(\underline{x_1})$.

# Local analysis of the flow:

To get a better physical understanding of fluid flow, we ask what an arbitrary flow $\underline{u}(\underline{x},t)$ does to a single fluid element. We compare the velocity at two nearby points $\underline{x}+\delta\underline{x}$ in the same fluid element $D$. A difference in this velocity must cause the fluid element to deform:![[Kinematics of Fluids 2025-10-21 10.14.12.excalidraw]]Expanding about the fixed point $\underline{x}$ using Taylors theorem:$$\Huge \underline{u}(\underline{x}+\delta\underline{x},t)=\underline{u}(\underline{x},t)+\pmb{J}(\underline{x},t)\cdot\delta\underline{x}+\mathcal{O}(|\delta\underline{x}|^2)$$where $\pmb J$ is the [[year 1/calculus 1/term 1/Integration#Changing variable and the Jacobian||Jacobian]] matrix:$$\Huge J_{ij}=\nabla_ju_i=\frac{\partial u_i}{\partial x_j}$$The transpose of $\pmb J$ is called the velocity gradient tensor, $\underline{\nabla}\underline{u}$, where $(\underline{\nabla}\underline{u})_{ij}=\nabla_iu_j$. So the local structure of the velocity field is defined by the Jacobian. The matrix can be decomposed as:$$\Huge \pmb J=\frac{1}{2}(\pmb J+\pmb J^T)+\frac{1}{2}(\pmb J-\pmb J^T)=\pmb E+\pmb\Omega$$where $\pmb E$ is the symmetric tensor (rate of strain tensor), and $\pmb\Omega$ is the antisymmetric tensor. Note that $\pmb J$ is a rank two tensor, and so is written in bold font to indicate this. Using these definitions in the Taylor expansion:$$\Huge \underline{u}(\underline{x}+\delta\underline{x},t)\approx\underline{u}(\underline{x},t)+(\pmb E(\underline{x},t)+\pmb\Omega(\underline{x},t))\cdot\delta\underline{x}$$There are three components in this approximation:
>$\underline{u}(\underline{x},t)$ represents the bodily translation of the whole of $D$ with velocity $\underline{u}(\underline{x},t)$
>$\pmb E(\underline{x},t)\cdot\delta\underline{x}$ represents the stretching/compression of $D$. Since $\pmb E$ is symmetric, it can be [[Eigenvalues, Eigenvectors, and Diagonalisation#Diagonalisation|diagonalised]] as $\pmb E=\pmb P\pmb D\pmb P^{-1}$ where $\pmb D=\text{diag}(\lambda_1,\lambda_2,\lambda_3)$ contains the eigenvalues of $\pmb E$. Additionally, $\pmb P$ is formed of the eigenvectors $\underline{v}_i$ of $\pmb E$, which are orthogonal:$$\Huge \pmb P=\begin{pmatrix}\underline{v_1} & \underline{v_2} & \underline{v_3}\end{pmatrix}$$which makes the effect of $\pmb E$ equivalent to stretching/compressing along its eigenvectors. $\pmb P$ is simply used to change into $\pmb P$ basis, while $\pmb D$ does the actual stretch. The normalised eigenvectors are called the principal axes, and the eigenvalues are the corresponding principal rates of strain.
>$\pmb\Omega(\underline{x},t)\cdot\delta\underline{x}$ represents the rotation of $D$. To see this, we introduce $\underline{\omega}=\underline{\nabla}\times\underline{u}$, making the three dimensional $\pmb\Omega$ take form:$$\Huge \pmb\Omega=\frac{1}{2}\begin{pmatrix}0 & -\omega_3 & \omega_2 \\ \omega_3 & 0 & -\omega_1 \\ -\omega_2 & \omega_1 & 0\end{pmatrix}$$The quantity $\underline{\omega}$ is known as the vorticity. Note that we can write:$$\Huge \pmb\Omega\cdot\delta\underline{x}=\frac{1}{2}\underline{\omega}\times\delta\underline{x}$$which highlights the fact that the fluid element is rotated with angular velocity $\frac{1}{2}\underline{\omega}$.

#### Example:
![[Kinematics of Fluids 2025-10-21 10.40.37.excalidraw]]

The decomposition into the action of the flow, $\pmb E,\pmb\Omega$ is the fluid equivalent of rigid body dynamics, where the motion of a body is described in terms of of translation and rotation. Notice the third term represents stretching/compression, which is needed for fluid dynamics.

# Vorticity:

