
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

# Newtonian fluids:
