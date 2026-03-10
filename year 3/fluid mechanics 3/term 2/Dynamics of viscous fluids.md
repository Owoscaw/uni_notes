
So far we have studied inviscid fluids, where there was no friction between neighboring fluid elements or any boundaries in the system. To capture this behaviour, we need to build viscous stress into the forces in our momentum equation.

# Viscous stress:

Recall when we derived the integral equation for [[Dynamics of ideal fluids#Conservation of momentum|conservation of momentum]]:$$\Huge\int_V\rho\frac{D\underline{u}}{Dt}dV=\int_S\underline{\sigma}\cdot dS+\int_V\rho\underline{f}dV$$This is essentially $F=ma$, which separates into body forces and internal surfaces forces, represented by the stress tensor $\underline{\sigma}=(\sigma_{ij})$.

Applying the [[Integral theorems#Divergence theorem|divergence theorem]] to the surface term, we find that$$\Huge\int_V\rho\frac{D\underline{u}}{Dt}dV=\int_V(\underline{\nabla}\cdot\underline{\sigma}^\top+\rho\underline{f})dV$$where $\underline{\nabla}\cdot\underline{\sigma}^\top$ is a vector with components:$$\Huge (\underline{\nabla}\cdot\underline{\sigma}^\top)_i=\underline{\nabla}_j\sigma_{ji}^\top=\frac{\partial \sigma_{ij}}{\partial x_j}$$Without making any assumptions about $\underline{\sigma}$, we know that this equation has to be satisfied for any $V$, implying the Cauchy momentum equation:$$\Huge \rho\frac{D\underline{u}}{Dt}=\underline{\nabla}\cdot\underline{\sigma}^\top+\rho\underline{f}$$This is simply a generalisation of the Euler momentum equation, where the stress term looked like $-\underline{\nabla}p$. This was because we assumed the only internal force comes from pressure $p$, which acts normally inwards. Recall that the elements of $\underline{\sigma}$ correspond to:![[Dynamics of ideal fluids 2025-11-11 20.22.40.excalidraw]]The pressure-only model is equivalent to assuming $\underline{\sigma}$ has no off-diagonal components, $\sigma_{ij}=-p\delta_{ij}$.

Since we want $\underline{\sigma}$ to include friction, the off-diagonal components must encompass this behaviour. One constraint on these components comes from the conservation of angular momentum in the fluid. This is only conserved if the stress tensor is symmetric:$$\Huge\sigma_{ji}=\sigma_{ij}$$
## Stress tensor symmetry:
Conservation of angular momentum for a fluid element means that:$$\Huge \frac{d}{dt}\int_{V(t)}\underline{x}\times\rho\underline{u}\,dV=\int_{S(t)}\underline{x}\times(\underline{\sigma}\cdot dS)+\int_{V(t)}\underline{x}\times\rho\underline{f}\,dV
$$Here, $\underline{x}$ is the position vector from the origin and $V(t),S(t)$ are the volume and surface of the fluid at a given time. Conservation of momentum leads to statements like $F=ma$, and so we expect conservation of angular momentum to look like $\underline{x}\times\underline{F}=\underline{x}\times m\underline{a}$, so this form is not surprising.

Notice that the volume and surface now depend on time, as we are considering a moving fluid element. The challenge this imposes is the question of bringing derivatives inside the integral. For a fixed $V$, $\frac{d}{dt}\to\frac{\partial }{\partial t}$ as it moves inside, but if $V$ is moving we must also account for this.

The result that solves this problem is known as the Reynolds transport theorem. This dictates that for a function $f(\underline{x},t)$:$$\Huge \frac{d}{dt}\int_{V(t)}f\rho\,dV=\int_{V(t)}\frac{Df}{Dt}\rho\,dV$$That is to say, the rate of change of $f\rho\delta V$ following the element is just $Df/Dt$ multiplied by the mass $\rho\delta V$, as each fluid element mass is conserved. Applying the transport theorem, we find that:$$\Huge\begin{align*}
\frac{d}{dt}\int_{V(t)}\underline{x}\times\rho\underline{u}\,dV&=\int_{V(t)}\frac{D}{Dt}(\underline{x}\times\underline{u})\rho\,dV\\
&=\int_{V(t)}\left(\frac{D\underline{x}}{Dt}\times\underline{u}+\underline{x}\times\frac{D\underline{u}}{Dt}\right)\rho\,dV\\
&=\int_{V(t)}\underline{x}\times\rho\frac{D\underline{u}}{Dt}dV
\end{align*}$$
Now consider the stress term in our conservation of angular momentum equation and apply the divergence theorem:$$\Huge\begin{align*}
\int_{S(t)}(\underline{x}\times(\underline{\sigma}\cdot dS))_i&=\int_{S(t)}\epsilon_{ijk}x_j\sigma_{kl}\hat n_t\,dS\\
&=\int_{V(t)}\frac{\partial }{\partial x_l}(\epsilon_{ijk}x_j\sigma_{kl})dV\\
&=\int_{V(t)}\epsilon_{ijk}\left(\frac{\partial x_j}{\partial x_l}\sigma_{kl}+x_J\frac{\partial \sigma_{kl}}{\partial x_l}\right)dV\\
&=\int_{V(t)}\epsilon_{ijk}(\delta_{jl}\sigma_{kl}+x_j(\underline{\nabla}\cdot\underline{\sigma}^\top)_k)dV\\
&=\int_{V(t)}\epsilon_{ijk}\sigma_{kj}+\epsilon_{ijk}x_j(\underline{\nabla}\cdot\underline{\sigma}^\top)_k
\end{align*}$$Using our transport theorem result with this and the original equation we find:$$\Huge \int_{V(t)}x_{ijk}x_j\left(\rho\frac{Du_k}{Dt}-(\underline{\nabla}\cdot\underline{\sigma}^\top)_k-\rho f_k\right)dV=\int_{V(t)}\epsilon_{ijk}\sigma_{kj}dV$$The LHS vanishes by the Cauchy momentum equation, so angular momentum is conserved if and only if:$$\Huge\int_{V(t)}\epsilon_{ijk}\sigma_{kj}dV=0$$This must hold for all $V(t)$, and so:$$\Huge\begin{align*}
\epsilon_{ijk}\sigma_{kj}&=0\\
\iff\epsilon_{imn}\epsilon_{ijk}\sigma_{kj}&=0\\
\iff(\delta_{mj}\delta_{nk}-\delta_{mk}\delta_{nj})\sigma_{kj}&=0\\
\iff\sigma_{nm}-\sigma_{mn}&=0\\
\iff\sigma_{ij}&=\sigma_{ji}
\end{align*}$$

We also want the property that $\sigma_{ij}$ reduces to the inviscid equation in the absence of viscosity, so we write:$$\Huge \sigma_{ij}=-p\delta_{ij}+\tau_{ij}$$where $\underline{\tau}=(\tau_{ij})$ is called the deviatoric stress tensor. Since the diagonal components of $\underline{\sigma}$ no longer need to be equal, we simply define the pressure $p$ as the mean normal stress:$$\Huge p=-\frac{1}{3}\sigma_{ii}=-\frac{1}{3}(\sigma_{11}+\sigma_{22}+\sigma_{33})$$It follows that the deviatoric part is traceless, $\tau_{ii}=0$. We now how our general form for the elements of $\underline{\sigma}$ so that each element depends on the other in an allowed physical way and reduces to the ideal case when shear stresses are near zero.

--- W16 ---
# Newtonian fluids:

A Newtonian fluid is one where the shear stresses depend linearly on velocity gradients. This is the most common model for a viscous fluid and the one we now adopt. 

## Simple shear:
Let us consider a shear flow$$\Huge \underline{u}=U(y)\hat{\underline{e}}_x$$ with $U'(y)>0$:![[Dynamics of viscous fluids 2026-02-17 01.34.07.excalidraw]]Consider the stress on the surface $S$ given by $y=y_0$. In an ideal fluid, the forces would all be normal to $S$ so there would be no momentum transfer across $S$. In reality, kinetic theory dictates that some molecules will diffuse across $S$, transferring momentum. If a molecule moves from $y<y_0$ to $y>y_0$, it must be accelerated, so there must be a force in the $x$ direction. In a Newtonian fluid, we approximate the shear stress with a linear relation$$\Huge\sigma_{12}=\mu \frac{dU}{dy}$$, where the constant of proportionality $\mu$ is the viscosity. Since $\hat{\underline{n}}=\hat{\underline{e}}_y$ for the volume $y<y_0$, the force $\underline{\sigma}\cdot\underline{\hat{n}}$ on the lower fluid is to the right (speeding it up). For the volume $y>y_0$, the force to the left (slowing it down) since $\underline{\hat{n}}=-\hat{\underline{e}}_y$. So viscosity opposes relative motion between different parts of the fluid. Effectively it adds a drag force.

## Shear in all directions:
In general, we need to consider viscous force exerted across all components of $\underline{u}$ on surfaces with arbitrary orientation. Therefore we define a Newtonian fluid with the linear relation$$\Huge \tau_{ij}=A_{ijkl}\frac{\partial u_l}{\partial x_k}$$for some rank $4$ tensor $A_{ijkl}$. This is essentially a matrix of matrices such that for every combination of $ijkl$ there is a specific number. We make the further assumption that $A_{ijkl}$ is isotropic. We are assuming not that $\frac{\partial u_l}{\partial x_k}$ is the same everywhere, but that there is no preferred direction in space for the relation between this $\tau_{ij}$. Such isotropy holds for fluids like air or water, but not for polymer suspensions with long chain molecules. $A_{ijkl}$ therefore takes form:$$\Huge A_{ijlk}=\alpha\delta_{ij}\delta_{kl}+\beta\delta_{ik}\delta_{jl}+\gamma\delta_{il}\delta_{jk}$$This is a general result for rank $4$ tensors and can be proved using rotation matrices or geometrical arguments. For our purposes we use it directly. Therefore:$$\Huge \begin{align*}
\tau_{ij}&=\alpha\delta_{ij}\delta_{kl}\frac{\partial u_l}{\partial x_k}+\beta\delta_{ik}\delta_{jl}\frac{\partial u_l}{\partial x_k}+\gamma\delta_{il}\delta_{jk}\frac{\partial u_l}{\partial x_k}\\
&=\alpha\frac{\partial u_k}{\partial x_k}\delta_{ij}+\beta\frac{\partial u_j}{\partial x_i}+\gamma\frac{\partial u_i}{\partial x_j}
\end{align*}$$Since $\underline{\sigma}$ is symmetric we must also have $\tau_{ji}=\tau_{ij}$, implying $\gamma=\beta$ so$$\Huge\tau_{ij}=\alpha\frac{\partial u_k}{\partial x_k}\delta_{ij}+\beta\left(\frac{\partial u_j}{\partial x_i}+\frac{\partial u_i}{\partial x_j}\right)$$. Finally we apply $\tau_{ii}=0$ to find$$\Huge 0=3\alpha\frac{\partial u_k}{\partial x_k}+2\beta\frac{\partial u_i}{\partial x_i}$$, which implies $3\alpha=-2\beta$ since each derivative is simply a relabel. Writing $\mu=\beta$ gives:$$\Huge \tau_{ij}=\mu\left(\frac{\partial u_j}{\partial x_i}+\frac{\partial u_i}{\partial x_j}-\frac{2}{3}\frac{\partial u_k}{\partial x_k}\delta_{ij}\right)$$Thus we finally have the stress tensor for a Newtonian fluid $$\Huge\sigma_{ij}=-p\delta_{ij}+\mu \left(\frac{\partial u_j}{\partial x_i}+\frac{\partial u_i}{\partial x_j}-\frac{2}{3}(\underline{\nabla}\cdot\underline{u})\delta_{ij}\right)$$where $\mu$ is the viscosity. In non-Newtonian fluids such as toothpaste or magma, the stress cannot be modelled by a simple linear equations. If the condition $\tau_{ii}=0$ is not imposed, there are two independent coefficients of viscosity, written as:$$\Huge \tau_{ij}=\mu\left(\frac{\partial u_j}{\partial x_i}+\frac{\partial u_i}{\partial x_j}-\frac{2}{3}\frac{\partial u_k}{\partial x_k}\delta_{ij}\right)+\mu'\frac{\partial u_k}{\partial x_k}\delta_{ij}$$

# The Navier-Stokes equations:

We can now write down the infamous equations of motion for a viscous fluid. To derive the equation for conservation of momentum, we insert the Newtonian stress tensor $\underline{\sigma}$ into the general Cauchy momentum equations:$$\Huge\begin{align*}
[\underline{\nabla}\cdot\underline{\sigma}^\top]_i&=\frac{\partial \sigma_{ij}}{\partial x_j}\\
&=-\frac{\partial p}{\partial x_i}+\mu\left(\frac{\partial^2u_j}{\partial x_j\partial x_i}+\frac{\partial^2u_i}{\partial x_j\partial x_j}-\frac{2}{3}\frac{\partial }{\partial x_i}(\underline{\nabla}\underline{u})\right)\\
&=-\frac{\partial p}{\partial x_i}+\mu\left(\frac{\partial }{\partial x_i}\frac{\partial u_j}{\partial x_j}+\underline{\nabla}^2u_i-\frac{2}{3}\frac{\partial }{\partial x_j}(\underline{\nabla}\cdot\underline{u})\right)\\
&=-\frac{\partial p}{\partial x_i}+\mu\left(\frac{1}{3}\frac{\partial }{\partial x_i}(\underline{\nabla}\cdot\underline{u})+\underline{\nabla}^2u_i\right)
\end{align*}$$And so the [[Dynamics of viscous fluids#Viscous stress|Cauchy momentum equation ]]dictates:$$\Huge \rho\frac{D\underline{u}}{Dt}=-\underline{\nabla}p+\frac{\mu}{3}\underline{\nabla}(\underline{\nabla}\cdot\underline{u})+\mu \underline{\nabla}^2\underline{u}+\rho\underline{f}$$Thus the compressible Navier-Stokes equations are:$$\Huge\begin{align*}
\frac{\partial \rho}{\partial t}+\underline{\nabla}\cdot(\rho\underline{u})&=0\\
\frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}&=-\frac{1}{\rho}\underline{\nabla}\rho+\frac{\mu}{3\rho}\underline{\nabla}(\underline{\nabla}\cdot\underline{u})+\frac{\mu}{\rho}\underline{\nabla}^2\underline{u}+\underline{f}
\end{align*}$$With an additional unspecified equation describing the state. We discuss the incompressible Navier-Stokes equations:$$\Huge\begin{align*}
\underline{\nabla}\cdot\underline{u}&=0\\
\frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}&=-\frac{1}{\rho_0}\underline{\nabla}p+\frac{\mu}{\rho_0}\underline{\nabla}^2\underline{u}+\underline{f}
\end{align*}$$Usually we write $\nu=\mu/\rho_0$, the kinematic viscosity. The boundary conditions are different to an inviscid fluid. For a viscous fluid we need no-slip condition $\underline{u}$ that matches the speed of any boundary. If the boundary is stationary then $\underline{u}=0$. Example:
> Couette flow: Consider the flow between two moving boundaries with $p=0$ and $\underline{f}=0$. Let the boundary $y=0$ be stationary and the boundary at $y=h$ move rightwards with velocity $U$:![[Dynamics of viscous fluids 2026-02-17 13.11.47.excalidraw]]
> Using this in the incompressible Navier-Stokes equations gives:$$\Huge\begin{align*}
\underline{\nabla}\cdot\underline{u}&=0\\
\frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}&=-\frac{1}{\rho_0}\underline{\nabla}p+\nu\underline{\nabla}^2\underline{u}+\underline{f}\\
0+\left(\underline{u}\frac{\partial }{\partial x}\right)\underline{u}&=0+\nu\underline{\nabla}^2\underline{u}+0\\
\implies\nu\underline{\nabla}^2\underline{u}&=0\\
\implies\nu \frac{d^2\underline{u}}{dy^2}&=0,\,\,u(0)=u(h)=0
\end{align*}$$Which we solve by integrating twice:$$\Huge \implies u=Ay+B\implies_{BCs}\,u=\frac{U}{h}y$$
> The vorticity of this solution is:$$\Huge \underline{\omega}=\underline{\nabla}\times\underline{u}=\begin{vmatrix}\hat{\underline{e}}_x & \hat{\underline{e}}_y & \hat{\underline{e}}_z \\ \partial_x & \partial_y & \partial_z \\ u & 0 & 0\end{vmatrix}=-\frac{U}{h}\hat{\underline{e}}_z$$

Let us look at another example known as Poiseuille flow:
> We consider flow in a pipe of radius $a$ oriented along the $z$ axis:![[Dynamics of viscous fluids 2026-02-17 13.25.30.excalidraw]]We force fluid through the pipe using a pressure gradient. We assume $\underline{f}=0$ with no-slip boundary conditions:$$\Huge \underline{\nabla}p=-G\hat{\underline{e}}_z$$
> We look for steady flow solutions, so write $\underline{u}=u(r)\hat{\underline{e}}_z$. Putting this into the Navier-Stokes equations, we first compute each term in our cylindrical coordinates$$\Huge\begin{align*}
(\underline{u}\cdot\underline{\nabla})\underline{u}&=\left(u_r\frac{\partial }{\partial r}+\frac{u_\theta}{r}\frac{\partial }{\partial \theta}+u_z\frac{\partial }{\partial z}\right)(u_r\hat{\underline{e}}_r+u_\theta\hat{\underline{e}}_\theta+u_z\hat{\underline{e}}_z)\\
&=u_z\frac{\partial }{\partial z}(u_z\hat{\underline{e}}_z)=0\\
\underline{\nabla}^2\underline{u}&=\left(\underline{\nabla}^2u_r-\frac{u_r}{r^2}-\frac{2}{r}^2\frac{\partial u_\theta}{\partial \theta}\right)\hat{\underline{e}}_r\\
&+\left(\underline{\nabla}^2u_\theta+\frac{2}{r^2}\frac{\partial u_r}{\partial \theta}-\frac{u_\theta}{r^2}\right)\hat{\underline{e}}_\theta+\underline{\nabla}^2u_z\hat{\underline{e}}_z\\
&=\underline{\nabla}^2u_z\hat{\underline{e}}_z\\
&=\left(\frac{1}{r}\frac{\partial }{\partial r}\left(r\frac{\partial u_z}{\partial r}\right)+\frac{1}{r^2}\frac{\partial^2u_z}{\partial \theta^2}+\frac{\partial^2u_z}{\partial z^2}\right)\hat{\underline{e}}_z\\
\implies_\text{NS}0&=G+\frac{\mu}{r}\frac{d}{dr}\left(r \frac{du}{dr}\right)\\
\implies \frac{d}{dr}(r \frac{du}{dr})&=-\frac{G_r}{\mu}\\
\implies \frac{du}{dr}&=-\frac{Gr}{\mu}+\frac{A}{r}\\
\implies u&=-\frac{Gr^2}{4\mu}+A\log r+B
\end{align*}$$Note that the presence of the logarithm dictates that $A=0$ as $u$ must be finite there. $u(a)=0$ then implies:$$\Huge u(r)=\frac{G}{4\mu}(a^2-r^2)$$This makes intuitive sense, as the velocity will be greater near $r=0$ and lesser near $r=a$, due to friction with the pipes. We can find the total flow rate (flux) of this profile:$$\Huge \begin{align*}
Q=&=\iint ur\,dr\,d\theta\\
&=2\pi\int_0^a ur\,dr\\
&=\frac{\pi Ga^4}{8\mu}
\end{align*}$$This allows $\mu$ to be found in practice by measuring $Q$.
> Note in real life, this expression only works up to some critical pressure gradient $G$. While this equation holds true, we have steady unidirectional flow. After some critical pressure, we see unsteady flow where flow rate falls behind this linear approximation. After this stage, there is turbulent flow and the relation does not hold.

# Effects of viscosity:

There is a reason that steady state solutions have fairly smooth profiles for vorticity and velocity. This is because viscosity causes vorticity to decay and spread out, so any steady state solution is the long-term limit of this decay.

## Diffusion of vorticity:
Let us take the curl of the momentum equation and use our favourite vector identity to arrive at:$$\Huge \frac{\partial \underline{\omega}}{\partial t}+\underline{\nabla}\times(\underline{\omega}\times\underline{u})=\nu\underline{\nabla}^2\underline{\omega}$$This is the [[Dynamics of ideal fluids#Vorticity dynamics|vorticity equation]] with viscosity taken into account. The Laplacian in the RHS represents diffusion, scaled by the kinematic viscosity $\nu$. To illustrate this interaction, let us consider an example that suddenly generates vorticity:
> Suppose a viscous fluid lies at rest in $y>0$ and at $t=0$ the rigid boundary $y=0$ is jerked off with constant velocity $U\hat{\underline{e}}_x$:![[Dynamics of viscous fluids 2026-02-24 16.55.56.excalidraw]]
> We assume the form of the flow as above with $u(y,0)=0$ and that there is no external pressure gradient so that $p=p_0$. Then the incompressible Navier-Stokes equations reduce to:$$\Huge \frac{\partial u}{\partial t}=\nu\frac{\partial^2u}{\partial y^2},\,\,\begin{cases}u(0,t)=U & t>0 \\
u\to0 & y\to\infty \\
u(y,0)=0\end{cases}$$
> We can solve this diffusion equation by looking for a solution in the form $u(y,t)=f(\eta)$ where $\eta=\frac{y}{\sqrt{\nu t}}$. This form is known as a similarity solution, we are effectively assuming that the solution depends on a combination of $y$ and $t$ rather than the two variables independently.
> The chain rule then dictates:$$\Huge\begin{align*}
\frac{\partial u}{\partial t}&=f'(\eta)\frac{\partial \eta}{\partial t}=-f'(\eta)\frac{y}{2\nu^{1/2}t^{3/2}}=-f'(\eta)\frac{\eta}{2t}\\
\frac{\partial u}{\partial y}&=f'(\eta)\frac{\partial \eta}{\partial y}=f'(\eta)\frac{1}{\nu^{1/2}t^{1/2}}\\
\frac{\partial^2u}{\partial y^2}&=f''(\eta)\left(\frac{\partial \eta}{\partial y}\right)^2=f''(\eta)\frac{1}{\nu t}
\end{align*}$$
> Therefore we arrive at the ODE:$$\Huge -\frac{\eta}{2t}f'(\eta)=\frac{1}{t}f''(\eta)\implies f''(\eta)+\frac{\eta}{2}f'(\eta)=0$$
> We solve this using an integrating factor:$$\Huge\begin{align*}
\frac{d}{d\eta}(e^{\eta^2/4}f'(\eta))&=0\\
\implies f'(\eta)&=Ae^{-\eta^2/4}\\
\implies f(\eta)&=A\int_0^\eta e^{-s^2/4}ds+B
\end{align*}$$Imposing boundary conditions at $y=0$ gives $B=U$. The limiting behaviour $y\to\infty$ and $t\to0$ correspond to $f\to0$ as $\eta\to\infty$ so we impose:$$\Huge 0=A\int_0^\infty e^{-s^2/4}ds+U$$We can set $r=s/2$ to find:$$\Huge 0=2A\int_0^\infty e^{-r^2}dr+U\implies A=-\frac{U}{\sqrt\pi}$$
> Therefore we can write out velocity profile as$$\Huge\begin{align*}
u(y,t)&=U\left(1-\frac{1}{\sqrt\pi}\int_0^{y/\sqrt{\nu t}}e^{-s^2/4}ds\right)\\
&=U\left(1-\text{erf}\left(\frac{y}{2\sqrt{\nu t}}\right)\right)
\end{align*}$$, where $\text{erf}$ is the error function.
> Note that at time $t$, the effects of the boundary motion reach a distance of order $\sqrt{\nu t}$ from the boundary.
> Considering the vorticity of form $\underline{\omega}=\omega(y,t)\hat{\underline{e}}_z$ with:$$\Huge\omega(y,t)=-\frac{\partial u}{\partial y}=\frac{U}{\sqrt{\pi\nu t}}\exp\left(-\frac{y^2}{4\nu t}\right)$$
> Plotting both velocity and vorticity for different $\nu t$:![[Dynamics of viscous fluids 2026-02-24 17.14.06.excalidraw]]
> So we see that the viscosity spreads out the vorticity, which was initially concentrated in a vortex sheet of infinite strength at $y=0$. The vorticity is generated by the initial impulse and diffuses into the fluid. In the long time limit, we have no vorticity as $u\to U$.

## Viscous dissipation:
Another way to analyse the effect of viscosity on a flow is to observe its effect on kinetic energy. Again we expect viscosity to cause the decay and spread out of the kinetic energy. Let us observe our incompressible Navier-Stokes equations with conservative body force:$$\Huge\begin{align*}
\underline{\nabla}\cdot\underline{u}&=0\\
\frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}&=-\frac{1}{\rho_0}\underline{\nabla}p+\nu\underline{\nabla}^2\underline{u}-\underline{\nabla}\Phi
\end{align*}$$We saw that kinetic energy given by$$\Huge E=\frac{1}{2}\int_V\rho_0|\underline{u}|^2dV$$and its corresponding Euler equations conserve kinetic energy in a fixed, closed container. The presence of viscosity $\nu\neq0$ leads to the dissipation of this energy. Let us calculate $\frac{dE}{dt}$ with our new model:$$\Huge\begin{align*}
\frac{dE}{dt}&=\rho_0 \frac{d}{dt}\int_V\frac{1}{2}|\underline{u}|^2dV\\
&=\rho_0\int_V\underline{u}\cdot\frac{\partial \underline{u}}{\partial t}dV\\
&=\rho_0\int_V\underline{u}\cdot\underline{\nabla}\left(-\frac{1}{\rho_0}\underline{\nabla}p-(\underline{u}\cdot\underline{\nabla})\underline{u}+\nu\underline{\nabla}^2\underline{u}-\underline{\nabla}\Phi\right)dV\\
&=-\rho_0\int_V\underline{u}\cdot\underline{\nabla}\left(\frac{p}{\rho_0}+\frac{1}{2}|\underline{u}|^2+\Phi\right)dV+\mu\int_V\underline{u}\cdot\underline{\nabla}^2\underline{u}dV\\
&=-\rho_0\int_S H\underline{u}\cdot d\underline{S}+\mu\int_V\underline{u}\cdot\underline{\nabla}^2\underline{u}dV
\end{align*}$$ Here, we used our favourite vector identity as well as the reverse product rule and divergence theorem as well as defining $H$. Finally, since $\underline{u}\cdot d\underline{S}=\underline{u}\cdot\underline{\hat{n}}dS=0$ on $S$ we write:$$\Huge \frac{dE}{dt}=\mu\int\underline{u}\cdot\underline{\nabla}^2\underline{u}dV$$
In viscous fluids, we have the no-slip condition along boundaries rather than the no-flux condition we used above. We impose this later, however for now we can just use the product rule:$$\Huge\begin{align*}
\int_V\underline{u}\cdot\underline{\nabla}^2\underline{u}dV&=\int_Vu_k\frac{\partial^2u_k}{\partial x_j^2}dV\\
&=\int_V\frac{\partial }{\partial x_j}\left(u_k\frac{\partial u_k}{\partial x_j}\right)-\frac{\partial u_k}{\partial x_j}\frac{\partial u_k}{\partial x_j}dV\\
&=\int_Su_k\frac{\partial u_k}{\partial x_j}\hat n_jdS-\int_V\frac{\partial u_k}{\partial x_j}\frac{\partial u_k}{\partial x_j}dV\\
&=-\int_V\frac{\partial u_k}{\partial x_j}\frac{\partial u_k}{\partial x_j}dV
\end{align*}$$Here, we did use the no-slip boundary condition to remove the surface integral term as $\underline{u}=0$ along that surface. One can show that this integral is equivalent to $\int_V|\underline{\nabla}\times\underline{u}|^2dV$ and so we write:$$\Huge \frac{dE}{dt}=-\mu\int_V|\underline{\omega}|^2dV$$Note that this is a decreasing function until vorticity reaches $0$. In reality, this does not cause energy to disappear and instead gets converted to heat (which we do not account for, though we could).

# The Reynolds number:

We need a method to determine how important the effects of viscosity will be for a given flow situation. This will depend on $\nu$ as well as its size relative to the other terms in the Navier-Stokes. To do this, we look at the scaling properties of the equations, through a process called nondimensionalisation.

Let $U$ denote a characteristic flow speed $|\underline{u}|$ for the problem of interest, and let $L$ denote a characteristic length scale for this flow. We can then move to the dimensionless variables:$$\Huge \underline{u}'=\frac{1}{U}\underline{u},\,\,\underline{x}'=\frac{1}{L}\underline{x},\,\,t'=\frac{U}{L}t$$Our derivatives also become$$\Huge \frac{\partial }{\partial t}=\frac{\partial t'}{\partial t}\frac{\partial }{\partial t'}=\frac{U}{L}\frac{\partial }{\partial t'},\,\,\frac{\partial }{\partial x_j}=\frac{\partial x_j'}{\partial x_j}\frac{\partial }{\partial x_j'}=\frac{1}{L}\frac{\partial }{\partial x_j'}$$, making the continuity equation$$\Huge \frac{U}{L}\underline{\nabla}'\cdot\underline{u}'=0\iff\underline{\nabla}'\cdot\underline{u}'=0$$, and the unforced momentum equation:$$\Huge\begin{align*}
\frac{U^2}{L}\frac{\partial \underline{u}'}{\partial t'}+\frac{U^2}{L}(\underline{u}'\cdot\underline{\nabla}')\underline{u}'&=-\frac{1}{\rho_0L}\underline{\nabla}'p+\frac{U}{L^2}\nu\underline{\nabla}'^2\underline{u}'\\
\iff\frac{\partial \underline{u}'}{\partial t'}+(\underline{u}'\cdot\underline{\nabla}')\underline{u}'&=-\frac{1}{\rho_0U^2}\underline{\nabla}'p+\frac{\nu}{UL}\underline{\nabla}'^2\underline{u}'
\end{align*}$$Now all of our variables are nondimensionalised except for pressure. We can define dimensionless pressure as$$\Huge p'=\frac{1}{\rho_0U^2}p$$, making our fully nondimensionalised Navier-Stokes equation$$\Huge \frac{\partial \underline{u'}}{\partial t'}+(\underline{u}'\cdot\underline{\nabla}')\underline{u}'=-\underline{\nabla}'p'+\frac{1}{\text{Re}}\underline{\nabla}'^2\underline{u}'$$, where the remaining parameter here is the Reynolds number:$$\Huge \text{Re}=\frac{UL}{\nu}$$Two flows with the same $\text{Re}$ can be called dynamically similar, as the solutions will be the same under rescaling. Additional terms lead to additional dimensionless parameters, compressibility leads to the Mach number $\text{Ma}=U/c_0$, while introducing other body forces $\underline{f}$ leads to many other parameters.

## High $\text{Re}$ limit:
As $\text{Re}\to\infty$, the viscous term in the dimensionless Navier-Stokes equation becomes smaller and smaller. This limit however is singular, the solution of the Navier-Stokes equation does not generally tend to the solution of the Euler equation as the viscous term has the highest derivative:
> To illustrate this point, let us observe that happens when the highest derivative term is multiplied by a small parameter $\epsilon$$$\Huge \epsilon u''+u'=1,\,\,\epsilon<<1$$with $u(0)=0,u(1)=2$.
> Setting $\epsilon=0$ we arrive at $u'=1\implies u(x)=x+C$, boundary conditions cannot be satisfied.
> To find the full equation, we divide through by $\epsilon$ and solve with an integrating factor:$$\Huge\begin{align*}
\frac{d}{dx}(e^{x/\epsilon}u')&=\frac{1}{\epsilon}e^{x/\epsilon}\\
\implies u'&=1+Ae^{-x/\epsilon}\\
\implies u(x)&=x+B-A\epsilon e^{-x/\epsilon}
\end{align*}$$
> Imposing boundary conditions gives:$$\Huge\begin{align*}
x=0&\implies B=\epsilon A\\
x=1&\implies A=\frac{1}{\epsilon(1-e^{-1/\epsilon})}\\
\implies u(x)&=x+\frac{1-e^{-x/\epsilon}}{1+e^{-1/\epsilon}}
\end{align*}$$
> The solution to the second-order equation looks like the first-order solution with a thin layer near the boundary where it changes to meet the second boundary condition. In such layer, $u''$ is large enough to compensate for $\epsilon$ and will continue to exist for any $\epsilon>0$.

In the fluid case, we have an analogous layer above a solid boundary, where $\underline{u}$ departs from inviscid flow in order to satisfy the no-slip condition. We call this a boundary layer, which we saw in a previous example where the thickness grew with $\sqrt{\nu t}$. More often we have:![[Dynamics of viscous fluids 2026-03-02 21.08.31.excalidraw]]Here, we have flow past a stationary object that slows down near the surface and stops at the surface itself. In this case, the reduction in speed propagates from the surface within the boundary layer:
> We can estimate how big this layer grows as a high $\text{Re}$ flow moves past an object. If the object has length $L$ and flow speed $U$, the thickness of the boundary will reach $\sqrt{\nu t}=\sqrt{\frac{\nu L}{U}}$ at the rear.
> The sheared flow within the layer is then advected beyond the object as a wake, which continues to widen due to viscous diffusion. The flow takes time $x/U$ to move a distance $x$, so the wake spreads a distance $\sqrt{\nu t}=\sqrt{\nu x/U}$.
> Secondary flows can cause the boundary to separate before it reaches the rear of the object. Aerofoils are shaped to prevent this premature separation, but this only works if the angle of attack is not too high. When the angle of attack is increased too far we get a sudden separation of the flow, reducing lift from the wing. This is known as a stall.

# Stokes flows:

Looking at the other extreme, $\text{Re}<<1$, viscosity dominates. We see this in flows with small length scales and very viscous fluids like honey.

Returning to the nondimensionalisation of the Navier-Stokes equations, we had to scale pressure to balance dominant forces. In the limit $\text{Re}<<1$, the viscous term dominates and so instead of choosing $P=\rho_0 U^2$ we instead choose$$\Huge P=\frac{\mu U}{L}$$, giving us the nondimensionalised Navier-Stokes momentum equation of the form:$$\Huge \frac{\partial \underline{u'}}{\partial t'}+(\underline{u}'\cdot\underline{\nabla}')\underline{u}'=\frac{1}{\text{Re}}(-\underline{\nabla}'p'+\underline{\nabla}'^2\underline{u}')$$Taking the limit $\text{Re}<<1$, we obtain (reintroducing dimension) the Stokes equations:$$\Huge \begin{align*}
\underline{\nabla}\cdot\underline{u}&=0\\
\mu\underline{\nabla}^2\underline{u}&=\underline{\nabla}p
\end{align*}$$
## Unique solutions to Stokes flows:
The Stokes equations are linear, so are easier to deal with. These also admit only one unique solution, $\underline{u}(\underline{x}),p(\underline{x})$ in a domain $V$ matching a given boundary condition $\underline{u}=\underline{u}_S(\underline{x})$ on $S$. Therefore the boundary drives the flow, and pressure $p$ is unique up to an additive constant.

To see this, suppose we have two solution $\underline{u}_1,\underline{u}_2$ and consider $\underline{v}=\underline{u}_1-\underline{u}_2$ with corresponding pressure different $q=p_1-p_2$. By linearity we have the same Stokes equations for $\underline{v}$. Since $\underline{u}_1,\underline{u}_2$ satisfy the same boundary condition, we have $\underline{v}=0$ on $S$ and it follows that:$$\Huge\begin{align*}
\int_V\underline{v}\cdot(\mu\underline{\nabla}^2\underline{v}-\underline{\nabla}q)dV&=0\\
\implies\int_Vv_i\left(\mu\frac{\partial^2v_i}{\partial x_jx_j}-\frac{\partial q}{\partial x_i}\right)dV&=0
\end{align*}$$The product rule then dictates$$\Huge\mu\int_V\frac{\partial }{\partial x_j}\left(v_i\frac{\partial v_i}{\partial x_j}\right)dV-\mu\int_V\frac{\partial v_i}{\partial x_j}\frac{\partial v_i}{\partial x_j}dV-\int_V\frac{\partial }{\partial x_i}(v_iq)dV=0$$, which we apply the divergence theorem to and find$$\Huge\begin{align*}
\mu\int_Sv_i\frac{\partial v_i}{\partial x_j}\hat n_jdS-\mu\int_V\frac{\partial v_i}{\partial x_j}\frac{\partial v_i}{\partial x_j}dV-\int_Sqv_i\hat n_idS&=0\\
\implies\mu\int_V\frac{\partial v_i}{\partial x_j}\frac{\partial v_i}{\partial x_j}dV&=0
\end{align*}$$where we used the boundary condition $\underline{v}=0$. The remaining integrand is:$$\Huge\frac{\partial v_i}{\partial x_j}\frac{\partial v_i}{\partial x_j}=|\underline{\nabla}v_x|^2+|\underline{\nabla}v_y|^2+|\underline{\nabla}v_z|^2$$Therefore the only way for the integral to vanish is for $\underline{v}$ to be constant. Since $\underline{v}=0$ on the boundary we must have $\underline{v}=0$ everywhere, so it follows that $\underline{u}_1=\underline{u}_2$.

## Viscous stream function:
We can find solutions to the stokes equations$$\Huge\begin{align*}
\underline{\nabla}\cdot\underline{u}&=0\\
\mu\underline{\nabla}^2\underline{u}&=\underline{\nabla}p
\end{align*}$$using [[Kinematics of Fluids#The stream function|stream functions]]. In two dimensional flow, the stream function $\psi$ satisfies:$$\Huge u=\frac{\partial \psi}{\partial y},\,\,v=-\frac{\partial \psi}{\partial x}$$This definition automatically satisfies the continuity equation, and we can rewrite the momentum equation using$$\Huge\underline{\nabla}\times(\underline{\nabla}\times\underline{u})=\underline{\nabla}(\underline{\nabla}\cdot\underline{u})-\underline{\nabla}^2\underline{u}$$to give us:$$\Huge \underline{\nabla}p=-\mu\underline{\nabla}\times\underline{\omega}$$Two dimensional flows only have a $z$-component for the vorticity, so we can write this equation component wise as:$$\Huge\begin{align*}
\frac{\partial p}{\partial x}&=-\mu\frac{\partial \omega}{\partial y}\\
\frac{\partial p}{\partial y}&=\mu\frac{\partial \omega}{\partial x}
\end{align*}$$We cross-differentiate this and subtract to find:$$\Huge 0=\frac{\partial^2p}{\partial x\partial y}-\frac{\partial^2p}{\partial y\partial x}=\mu\left(\frac{\partial^2\omega}{\partial x^2}+\frac{\partial^2\omega}{\partial y^2}\right)=\mu\underline{\nabla}^2\omega$$Reintroducing the stream function, we know that$$\Huge\omega=\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}=-\left(\frac{\partial^2\psi}{\partial y^2}+\frac{\partial^2\psi}{\partial x^2}\right)=-\underline{\nabla}^2\psi$$, putting everything together we then arrive at:$$\Huge\underline{\nabla}^2(\underline{\nabla}^2\psi)=0$$That is, $\psi$ satisfies the biharmonic equation. Therefore for two dimensional Stokes flow, the problem reduces to solving the biharmonic equation with appropriate boundary conditions.

The stream function only works in two dimensional flows, however we can use an analogous idea for $3D$ axisymmetric flows. In spherical coordinates we have:$$\Huge\underline{u}=u_r(r,\theta)\hat{\underline{e}}_r+u_\theta(r,\theta)\hat{\underline{e}}_\theta,\,\,u_\phi=0$$Here, the continuity equation becomes:$$\Huge\frac{1}{r^2}\frac{\partial }{\partial r}(r^2u_r)+\frac{1}{r\sin\theta}\frac{\partial }{\partial \theta}(\sin\theta u_\theta)=0$$We can see that this is satisfied automatically if we introduce $\Psi$ such that:$$\Huge u_r=\frac{1}{r^2\sin\theta}\frac{\partial \Psi}{\partial \theta},\,\,u_\theta=-\frac{1}{r\sin\theta}\frac{\partial \Psi}{\partial r}$$We call $\Psi$ the Stokes stream function.

For axisymmetric flow, the vorticity only has a $\phi$-component and so$$\Huge\begin{align*}
\underline{\omega}&=\frac{1}{r^2\sin\theta}\begin{vmatrix}\hat{\underline{e}}_r & r\hat{\underline{e}}_\theta & (r\sin\theta)\hat{\underline{e}}_\phi\\
\frac{\partial }{\partial r} & \frac{\partial }{\partial \theta} & \frac{\partial }{\partial \phi}\\
u_r & ru_\theta & (r\sin\theta)0\end{vmatrix}=\omega_\phi\hat{\underline{e}}_\phi\\
\implies\omega_\phi
&=\frac{1}{r}\left(\frac{\partial }{\partial r}\left(ru_\theta\right)-\frac{\partial u_r}{\partial \theta}\right)\end{align*}$$, substituting in our chosen form of $u$ leads to$$\Huge\begin{align*}
\omega_\phi&=\frac{1}{r}\left(\frac{\partial }{\partial r}\left(-\frac{1}{\sin\theta}\frac{\partial \Psi}{\partial r}\right)-\frac{\partial }{\partial \theta}\left(\frac{1}{r^2\sin\theta}\frac{\partial \Psi}{\partial \theta}\right)\right)\\
&=-\frac{1}{r}\left(\frac{1}{\sin\theta}\frac{\partial }{\partial r}\left(\frac{\partial \Psi}{\partial r}\right)+\frac{1}{r^2}\frac{\partial }{\partial \theta}\left(\frac{1}{\sin\theta}\frac{\partial \Psi}{\partial \theta}\right)\right)\\
&=-\frac{1}{r\sin\theta}D^2\Psi
\end{align*}$$where:$$\Huge D^2=\frac{\partial^2}{\partial r^2}+\frac{\sin\theta}{r^2}\frac{\partial }{\partial \theta}\left(\frac{1}{\sin\theta}\frac{\partial }{\partial \theta}\right)$$Moving on to the momentum equation, we find that$$\Huge\underline{\nabla}p=-\frac{\mu}{r^2\sin\theta}\begin{vmatrix}\hat{\underline{e}}_r & r\hat{\underline{e}}_\theta & (r\sin\theta)\hat{\underline{e}}_\phi \\ \frac{\partial }{\partial r} & \frac{\partial }{\partial \theta} & \frac{\partial }{\partial \phi} \\ 0 & 0 & (r\sin\theta)\omega_\phi\end{vmatrix}$$, which we write component-wise as:$$\Huge\begin{align*}
\frac{\partial p}{\partial r}&=\frac{\mu}{r^2\sin\theta}\frac{\partial }{\partial \theta}D^2\Psi\\
\frac{1}{r}\frac{\partial p}{\partial \theta}&=-\frac{\mu}{r\sin\theta}\frac{\partial }{\partial r}D^2\Psi
\end{align*}$$Again we cross-differentiate and find:$$\Huge D^2(D^2\Psi)=0$$Therefore for axisymmetric Stokes flow, the Stokes stream function satisfies a biharmonic-type equation, written in terms of the operator $D^2$ appropriate to spherical geometry. Note for cylindrical polars $(r,z)$, the equivalent operator is:$$\Huge D^2=\frac{\partial^2}{\partial r^2}-\frac{1}{r}\frac{\partial }{\partial r}+\frac{\partial^2}{\partial z^2}$$
Let us consider a Stokes flow in the half plane $x\geq0$ driven by a flow through a permeable wall at $x=0$:![[Dynamics of viscous fluids 2026-03-03 17.47.21.excalidraw]]
> At $x=0$, the flow $(u,v)$ is given by$$\Huge u(0,y)=U\cos(ay),\,\,v=0$$, we aim to find $\psi$ by solving $\underline{\nabla}^2(\underline{\nabla}^2\psi)=0$.
> The boundary conditions on $\psi$ are the flow at $x=0$:$$\Huge\frac{\partial \psi}{\partial y}=U\cos(ay),\,\,\frac{\partial \psi}{\partial x}=0\implies\psi|_{x=0}=\frac{U}{a}\sin(ay)$$Here, we set the integration constant to $0$ as the stream function is only defined up to an additive constant.
> Given the form of the boundary condition, we look for a separable solution on the whole domain$$\Huge\psi=f(x)\sin(ay)$$, which makes the biharmonic equation take form:$$\Huge\begin{align*}
\underline{\nabla}^2\psi&=(f''-a^2f)\sin(ay)\\
&=F(x)\sin(ay)\\
\implies\underline{\nabla}^2(\underline{\nabla}^2\psi)&=(F''-a^2F)\sin(ay)=0
\end{align*}$$
> Therefore the problem is equivalent to solving $F''-a^2F=0$, which is a nice ODE:$$\Huge\begin{align*}
F&=Ae^{ax}+Be^{-ax}\\
\implies f''-a^2f&=\text{above}
\end{align*}$$We solve this using the repeated root particular integral results:$$\Huge f(x)=C_1e^{ax}+C_2xe^{ax}+C_3e^{-ax}+C_4xe^{-ax}$$
> To determine the constants, note that we require bounded solutions at $x\to\infty$ so we can immediately discard the exponentially growing terms ($C_1=C_2=0$). Using the flow at $x=0$, we observe that$$\Huge\psi|_{x=0}=\frac{U}{a}\sin(ay)\implies f(0)=\frac{U}{a}=C_3$$and also:$$\Huge\begin{align*}
\frac{\partial \psi}{\partial x}|_{x=0}=0&\implies f'(0)=0\\
&\implies -aC_3+C_4=0\\
&\implies C_4=U
\end{align*}$$
> Our stream function is therefore given by:$$\Huge\psi=U\left(\frac{1}{a}+x\right)e^{-ax}\sin(ay)$$We see exponential decay away from the boundary with decay length $1/a$, showing that spatial oscillations along the wall induce localised viscous motion.

Let us consider Stokes flow past a sphere. We consider a sphere of radius $a$ placed in an oncoming uniform stream with speed $U$:![[Dynamics of viscous fluids 2026-03-03 20.34.27.excalidraw]]
> The geometry of the problem suggest an axisymmetric solution in spherical coordinates $(r,\theta,\phi)$$$\Huge \underline{u}=u_r\hat{\underline{e}}_r+u_\theta\hat{\underline{e}}_\theta,\,\,u_\phi=0$$, where we are solving $D^2(D^2\Psi)=0$. We know the form of our solution will be$$\Huge u_r=\frac{1}{r^2\sin\theta}\frac{\partial \Psi}{\partial \theta},\,\,u_\theta=-\frac{1}{r\sin\theta}\frac{\partial \Psi}{\partial r}$$, so we need to implement our boundary conditions.
> As $r\to\infty$ we must recover the uniform stream $\underline{u}\to U\hat{\underline{e}}_x$, which translates to polar coordinates as:$$\Huge\begin{align*}
u_r\to U\cos\theta&\implies\frac{\partial \Psi}{\partial \theta}\to Ur^2\sin\theta\cos\theta\\
u_\theta\to-U\sin\theta&\implies\frac{\partial \Psi}{\partial r}\to Ur\sin^2\theta\\
\implies\Psi&\to\frac{1}{2}Ur^2\sin^2\theta
\end{align*}$$
> On the boundary of the sphere, we impose the no-slip condition:$$\Huge\begin{align*}
u_\theta&=0\implies\frac{\partial \Psi}{\partial r}=0\\
u_r&=0\implies\frac{\partial \Psi}{\partial \theta}=0
\end{align*}$$These combine to impose that $\Psi$ is constant on the surface of the sphere. WLOG we set this constant to $0$. 
> The form of the boundary conditions suggest a separable solution of the form:$$\Huge\Psi=f(r)\sin^2\theta$$We substitute this into the biharmonic equation to get:$$\Huge\begin{align*}
D^2\Psi&=\left(\frac{\partial^2}{\partial r^2}+\frac{\sin\theta}{r^2}\frac{\partial }{\partial \theta}\left(\frac{1}{\sin\theta}\frac{\partial }{\partial \theta}\right)\right)\Psi\\
&=f''\sin^2\theta+\frac{\sin\theta}{r^2}f\frac{\partial }{\partial \theta}\left(2\frac{\sin\theta\cos\theta}{\sin\theta}\right)\\
&=\left(f''-\frac{2}{r^2}f\right)\sin^2\theta=F(r)\sin^2\theta\\
\implies D^2(D^2\Psi)&=D^2(F(r)\sin^2\theta)\\
&=\left(F''-\frac{2}{r^2}F\right)\sin^2\theta=0
\end{align*}$$
> Now we solve $r^2F''-2F=0$, a Cauchy type ODE, by setting $F=r^\lambda$$$\Huge\begin{align*}
\implies\lambda(\lambda-1)-2&=0\\
\implies(\lambda-2)(\lambda+1)&=0\\
\implies\lambda&=2,-1
\end{align*}$$Using this in our ODE gives:$$\Huge\begin{align*}
F&=Ar^2+Br^{-1}\\
\implies f''-\frac{2}{r^2}f&=Ar^2+Br^{-1}\\
\implies r^2f''-2f&=Ar^4+Br
\end{align*}$$This is an inhomogeneous ODE, so the solution is a complementary function and particular integral. We already know the complementary function is $f=C_1r^2+C_2r^{-1}$ and we see by inspection that the particular integral is $f=C_3r^4+C_2r^{-1}$. Therefore our function is of form:$$\Huge f(r)=C_1r^2+C_2r^{-1}+C_3r^4+C_4r$$
> Applying boundary conditions at $r\to\infty$ we have$$\Huge f(r\to\infty)=\frac{1}{2}Ur^2$$, which sets $C_3=0$ and $C_1=U/2$. At $r=a$ we have:$$\Huge \begin{align*}
f(a)&=0,\,\,f'(a)=0\\
\implies C_4&=-\frac{3}{4}aU,\,\,C_2=\frac{1}{4}a^3U
\end{align*}$$
> Therefore, our Stokes stream function is given by:$$\Huge \Psi=\frac{1}{2}Ur^2\sin^2\theta\left(1-\frac{3a}{2r}+\frac{a^3}{2r^3}\right)$$

# Time reversibility:

Another key insight into the effects of viscous flow is to consider what we can infer about earlier times in the system based on the fluid state at later times. To see this, suppose that $\underline{u},p$ solve the incompressible Navier-Stokes equations with conservative body force and let time run backwards so that:$$\Huge \underline{u}\to-\underline{u},\,\,p\to p,\,\,\frac{\partial }{\partial t}\to-\frac{\partial }{\partial t},\,\,\underline{\nabla}\to\underline{\nabla}$$Then $\underline{\nabla}\cdot\underline{u}=0$ is invariant, but the momentum equation becomes:$$\Huge \frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}=-\frac{1}{\rho_0}\underline{\nabla}p-\nu\underline{\nabla}^2\underline{u}-\underline{\nabla}\Phi$$This is not invariant, information is lost during the Navier-Stokes evolution due to the dissipation of viscosity and kinetic energy. This suggests three scenarios:
> All terms present: When the nonlinear and viscous terms are present, the fluid will in general have multi-scale eddies and complex flows that are smoothed by the viscosity. As fine scales are smooth out, different starting states can have the same end state. Therefore the system is irreversible.
> High $\text{Re}$: In the high Reynolds number limit, we recover the Euler equations making the momentum equation invariant. If we know some later state, we can exactly reproduce the earlier state by running the equation in reverse. At this scale, small eddies can form but there is no dissipation so we maintain the one-to-one link between start and end states.
> Low $\text{Re}$: The same is true for the low Reynolds number limit where we have Stokes flow. Since this regime is driven by the motion of the boundary, reversing the equation gives an exact reversal of the flow: 
> > To demonstrate this, let the flow on the boundary be given by $\underline{u}_S(\underline{x})=\underline{g}(\underline{x})$ for some particular function $\underline{g}$ and suppose $\underline{u}_1,p_1$ is the corresponding solution to the Stokes equation.
> > Now we change the boundary conditions to $\underline{u}_S=-\underline{g}(\underline{x})$ on the boundary. The solution$$\Huge \underline{u}_2(\underline{x})=-\underline{u}_1(\underline{x}),\,\,P_2=C-p_1$$matches the new conditions. Since there is only one unique solution in Stokes flow, this is the only solution. 
> > In this regime, the high viscosity damps out the nonlinear complex flows that result in higher Reynolds number flows, leaving something simple enough to reverse.

# Lubrication theory:

So far, we have obtained solutions to the Navier-Stokes equations in one of two ways:
> The geometry was simple enough to eliminate most terms
> The Reynolds number was sufficiently small that inertia is neglected (Stokes flow)

We move on to consider flows in thin layers and narrow gaps. Here, the key features are not only the low Reynolds number but also a small aspect ratio (one dimension of the flow is much smaller than others). This approximation is known as lubrication theory and reduces the Navier Stokes equations to a much simpler form while retaining the physics of viscous flow in confined spaces.

Consider a flow with length scale $L$ and height scale $H$:![[Dynamics of viscous fluids 2026-03-10 14.59.00.excalidraw]]In a thin layer, we can write:$$\Huge \frac{H}{L}=\epsilon<<1$$We also say that $U$ is a typical speed along the channel and that the flow is steady. As we are comparing the sizes of terms in the Navier-Stokes equations, it is useful to nondimensionalise it. Since we have different length scales for $x$ and $y$ directions, we must nondimensionalise as$$\Huge u=Uu',\,\,v=Vv',\,\,x=Lx',\,\,y=Hy'=\epsilon Ly',\,\,p=Pp'$$where we are free to choose $V,P$. The continuity equation transforms to$$\Huge\begin{align*}
\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}&=0\\
\implies\frac{U}{L}\frac{\partial u'}{\partial x'}+\frac{V}{\epsilon L}\frac{\partial v'}{\partial y'}&=0
\end{align*}$$therefore we choose $V=\epsilon U$ to maintain the continuity equation. The momentum equation in $x$ becomes:$$\large\begin{align*}
\rho\left(u\frac{\partial u}{\partial x}+v\frac{\partial u}{\partial y}\right)&=-\frac{\partial p}{\partial x}+\mu\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}\right)\\
\implies\frac{\rho U^2}{L}\left(u'\frac{\partial u'}{\partial x'}+v'\frac{\partial u'}{\partial y'}\right)&=-\frac{P}{L}\frac{\partial p'}{\partial x'}+\frac{\mu U}{L^2}\left(\frac{\partial^2u'}{\partial x'^2}+\frac{1}{\epsilon^2}\frac{\partial^2u'}{\partial y'^2}\right)\\
\implies\frac{\rho UL}{\mu}\epsilon^2\left(u'\frac{\partial u'}{\partial x'}+v'\frac{\partial u'}{\partial y'}\right)&=-\frac{PL\epsilon^2}{\mu U}\frac{\partial p'}{\partial x'}+\epsilon^2\frac{\partial^2u'}{\partial x'^2}+\frac{\partial^2u'}{\partial y'^2}
\end{align*}$$Note that the first term features a leading Reynolds number with length scale $L$. To fix $P$ we must impose that pressure balances the dominant term, and therefore:$$\Huge P=\frac{\mu U}{L\epsilon^2}$$Then for $\epsilon<<1$ and $\epsilon^2\text{Re}_L<<1$ this reduces to:$$\Huge 0=\frac{\partial p'}{\partial x'}+\frac{\partial^2u'}{\partial y'^2}$$
The momentum equation in $y$ is$$\large\begin{align*}
\rho\left(u\frac{\partial v}{\partial x}+v\frac{\partial v}{\partial y}\right)&=-\frac{\partial p}{\partial y}+\mu\left(\frac{\partial^2v}{\partial x^2}+\frac{\partial^2v}{\partial y^2}\right)\\
\implies\frac{\rho U^2\epsilon}{L}\left(u'\frac{\partial v'}{\partial x'}+v'\frac{\partial v'}{\partial y'}\right)&=-\frac{P}{\epsilon L}\frac{\partial p'}{\partial y'}+\frac{\mu\epsilon U}{L^2}\left(\frac{\partial^2v'}{\partial x'^2}+\frac{1}{\epsilon^2}\frac{\partial^2v'}{\partial y'^2}\right)\\
\implies(\text{Re}_L\epsilon^2)\epsilon^2(u'\frac{\partial v'}{\partial x'}+v'\frac{\partial v'}{\partial y'})&=-\frac{\partial p'}{\partial y'}+\epsilon^2\left(\epsilon^2\frac{\partial^2v'}{\partial x'^2}+\frac{\partial^2v'}{\partial y'^2}\right)
\end{align*}$$Then for $\epsilon<<1$ and $\epsilon^2\text{Re}_L<<1$ this reduces to$$\Huge 0=\frac{\partial p'}{\partial y'}$$, that is the channel is too thin to support a pressure gradient in the $y$-direction. 

Combining our equations, we get the $2D$ lubrication equations:$$\Huge\begin{align*}
0&=\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}\\
0&=-\frac{\partial p}{\partial x}+\mu\frac{\partial^2u}{\partial y^2}\\
0&=\frac{\partial p}{\partial y}
\end{align*}$$We see that the "battle" here is between pressure and viscosity in the $y$-direction.

## The Reynolds lubrication equation:
Consider a $2D$ flow between a solid wall at $y=0$ and a surface at $h(x,t)$ that moves with speed $(U,V)$:![[Dynamics of viscous fluids 2026-03-10 15.17.16.excalidraw]]
The lubrication equations have no time derivatives, so we are looking for a quasi-steady solution (where the flow immediately adapts to boundaries). Our boundary conditions here are$$\Huge\begin{align*}
u&=U(x,t),&v&=V(x,t)&\text{at }y&=h\\
u&=0,&v&=0&\text{at }y&=0
\end{align*}$$, so we solve the lubrication equations:$$\Huge \frac{\partial p}{\partial y}=0\implies p=p(x,t)$$Therefore when we integrate$$\Huge \frac{\partial^2u}{\partial y^2}=\frac{1}{\mu}\frac{\partial p}{\partial x}$$twice, we get:$$\Huge u=\frac{1}{2\mu}\frac{\partial p}{\partial x}y^2+A(x,t)y+B(x,t)$$The boundary condition $y=0,u=0$ forces $B(x,t)=0$. The boundary condition $y=h,u=U$ allows us to find $A$:$$\Huge\begin{align*}
u&=\frac{1}{2\mu}\frac{\partial p}{\partial x}y^2+\left(-\frac{1}{2\mu}\frac{\partial p}{\partial x}h+\frac{U}{h}\right)y\\
&=\frac{1}{2\mu}\frac{\partial p}{\partial x}(y^2-hy)+\frac{Uy}{h}
\end{align*}$$Here, the first term represents a [[Dynamics of viscous fluids#The Navier-Stokes equations|Poiseuille]] flow component driven by a pressure gradient. The second term represents a [[Dynamics of viscous fluids#The Navier-Stokes equations|Couette]] flow driven by the motion of the wall. 

We find $v$ by integrating both sides of the continuity equation:$$\Huge-\int_0^h\frac{\partial v}{\partial y}dy=\int_0^h \frac{\partial u}{\partial x}dy$$The LHS is simply $-V$, however since the domain is not fixed in the RHS integral we must use the Leibniz integral rule$$\Huge\frac{\partial }{\partial x}\int_{a(x)}^{b(x)}u(x,y)dy=\int_{a(x)}^{b(x)}\frac{\partial u}{\partial x}dy+u(x,b)\frac{\partial b}{\partial x}-u(x,a)\frac{\partial a}{\partial x}$$to move the derivative through the integral sign. Therefore:$$\Huge\begin{align*}
-V&=\frac{\partial }{\partial x}\int_0^hu\,dy-U\frac{\partial h}{\partial x}\\
&=\frac{\partial }{\partial x}\left[\frac{1}{2\mu}\frac{\partial p}{\partial x}\left(\frac{y^3}{3}-\frac{hy^2}{2}\right)+\frac{Uy^2}{2h}\right]_0^h-U\frac{\partial h}{\partial x}\\
&=\frac{\partial }{\partial x}\left(-\frac{h^3}{12\mu}\frac{\partial p}{\partial x}+\frac{Uh}{2}\right)-U\frac{\partial h}{\partial x}\\
\implies0&=\frac{\partial }{\partial x}\left(-\frac{h^3}{12\mu}\frac{\partial p}{\partial x}+\frac{Uh}{2}\right)-U\frac{\partial h}{\partial x}+V
\end{align*}$$This is the Reynolds lubrication equation. For a given $h,U,V$ we can find $p$ and therefore $u,v$.

Let us consider an example of a rule sitting on a film of fluid:![[Dynamics of viscous fluids 2026-03-10 15.33.15.excalidraw]]
> The ruler of length $2a$ is raised with vertical speed $V$. Imposing the Reynolds lubrication equation directly with $U=0$ and $h=h(t)$ we have$$\Huge-\frac{h^3}{12\mu}\frac{\partial^2p}{\partial x^2}+V=0$$, which we integrate in $x$ twice to get:$$\Huge p=\frac{6\mu V}{h^3}x^2+Ax+B$$
> We have pressure boundary conditions, since the fluid just outside of the ruler at $x=\pm a$ is exposed to atmospheric pressure:$$\Huge p=p_\text{atm} \text{ at }x=\pm a$$
> Implementing these conditions imposes:$$\Huge p=p_\text{atm}+\frac{6\mu V}{h^3}(x^2-a^2)$$Since the bracketed term is always negative, we see that the pressure inside the thin gape is less than atmospheric pressure.
> We can recover flow speed from our equation with Couette/Poiseuille flows:$$\Huge\begin{align*}
u&=\frac{1}{2\mu}\frac{\partial p}{\partial x}(y^2-hy)+\frac{Uy}{h}\\
&=-\frac{6Vx}{h^3}(h-y)
\end{align*}$$This is parabolic inward flow.
 