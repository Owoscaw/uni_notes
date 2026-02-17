
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
\end{align*}$$And so the [[Dynamics of viscous fluids#Viscous stress|Cauchy momentum equation ]]dictates:$$\Huge \rho\frac{D\underline{u}}{Dt}=-\underline{\nabla}p+\frac{\mu}{3}\underline{\nabla}(\underline{\nabla}\cdot\underline{u})+\mu \underline{\nabla}^2\underline{u}+\rho\underline{f}$$