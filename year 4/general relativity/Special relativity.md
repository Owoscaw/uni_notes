
Because the speed of light falls out of [[Abelian gauge theories#Maxwell equation and actions|Maxwell's equations]], it is universal across all reference frames. Universality of the laws of physics seems to require the universality of the speed of light.

# Lorentz transformations:

We consider an observer in a coordinate system $(x,t)$ and label events on this plane by their coordinates as well:![[Special relativity 2026-10-07 12.11.23.excalidraw]]We are interested in the coordinate transformation relating $(t',\underline{x}')$ to $(t,\underline{x})$ for a given event. This is called a Galilean transformation:$$\Huge\begin{aligned}
\underline{x}'&=\underline{x}-vt\\
t'&=t
\end{aligned}$$This is not compatible with the universality of the speed of light, as this leads to the velocity addition rule:$$\Huge \frac{d\underline{x}'}{dt}=\frac{d\underline{x}}{dt}-\underline{v}$$Let us therefore consider a new transformation, under the following assumptions:
> Transformation is linear
> Other coordinates unaffected
> $x=vt$ should map to $x'=0$, which implies $x'=\gamma(v)(x-vt)$
> $x'=-vt'$ should map to $x=0$, which implies $x=\gamma(v)(x+vt)$

Now let us impose the universality of lightspeed by requiring $x=ct$ maps to $x'=ct'$:$$\Huge\begin{aligned}
ct'=x'&=\gamma(x-vt)\\
&=\gamma(c-v)t\\
ct=x&=\gamma(x'+vt')\\
&=\gamma(c+v)t'\\
\implies c^2t&=\gamma(c+v)ct'\\
&=\gamma(c+v)\gamma(c-v)t\\
&=\gamma^2(c^2-v^2)t\\
\implies\gamma(v)&=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}}
\end{aligned}$$Solving $x=\gamma(x'+vt')$ for $t'$ we find:$$\Huge\begin{aligned}
t'&=-\frac{x'}{v}+\frac{x}{v\gamma}\\
&=-\frac{\gamma(x-vt)}{v}+\frac{x}{v\gamma}\\
&=\gamma\left(t-\frac{v}{c^2}x\right)
\end{aligned}$$This lets us define the Lorentz transformation:$$\Huge x'=\gamma(x-vt),\,\,t'=\gamma\left(t-\frac{v}{c^2}x\right),\,\,\gamma=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}}$$

The expression for $t'$ is distinctly profound and leads to the Relativity of Simultaneity:  Events at the same time in one coordinate system do not necessarily occur at the same time in other coordinate systems. Note that the separation between events is invariant under coordinate transforms, implying the invariance of the spacetime interval.$$\Huge \Delta s^2=-c^2\Delta t^2+\Delta x^2$$is invariant. Let us check that this is indeed true:$$\large\begin{aligned}
\implies\Delta t'&=\gamma\left(\Delta t-\frac{v}{c^2}\Delta x\right)\\
\implies\Delta x'&=\gamma(\Delta x-v\Delta t)\\
\implies -c^2(\Delta t')^2+(\Delta x')^2&=\gamma^2\left(-\left(-c\Delta t-\frac{v}{c^2}\right)+(\Delta x-v\Delta t)^2\right)\\
&=\gamma^2\left(-c^2\Delta t^2\left(1-\frac{v^2}{c^2}\right)+\Delta x^2\left(1-\frac{v^2}{c^2}\right)\right)\\
&=-c^2\Delta t^2+\Delta x^2
\end{aligned}$$

This spacetime interval is a coordinate-independent property of the events involved. We take this to be fundamental and define Lorentz transformations to be the linear transformations leaving $\Delta s^2$ invariant. Note that this need not be positive:![[Special relativity 2026-10-07 12.54.49.excalidraw]]


# Relativistic notation:

We set $c=1$ and continue to introduce some useful notation. We write our coordinates as $x^\mu,\mu=0,1,2,3=(t,x,y,z)$, making the spacetime interval:$$\Large\Delta s^2=\eta_{\mu\nu}\Delta x^\mu\Delta x^\nu=\sum_{\mu,\nu=0}^3\eta_{\mu\nu}\Delta x^\mu\Delta x^\nu$$Here, $\eta_{\mu\nu}$ is the Minkowski metric, $\eta_\mu\nu=\text{diag}(-1,1,1,1)$ and we use [[Index notation|Einstein summation convention]]. The infinitesimal version of this acts as the line element:$$\Large ds^2=-dt^2+d\underline{x}^2=\eta_{\mu\nu}dx^\mu dx^\nu$$In this notation, our [[The Lorentz Group#The Lorentz group and its Lie Groups and Algebras Lie algebras Lie algebra|Lorentz transformations]] look like matrix multiplication$$\Huge\tilde x^\mu=\Lambda^\mu_\nu x^\nu$$, where $\Lambda$ is the matrix representation of the Lorentz transformation. The statement of spacetime invariance then becomes:$$\Large\Delta s^2=\eta_{\mu\nu}\Delta x^\mu\Delta x^\nu=\eta_{\rho\sigma}\Delta\tilde x^\rho\Delta\tilde x^\sigma=\eta_{\rho\sigma}\Lambda^\rho_\mu\Lambda^\sigma_\nu\Delta x^\mu\Delta x^\nu$$In order for this to be true $\forall\Delta x^\mu$, a condition is imposed on $\Lambda$:$$\Huge \Lambda^\rho_\mu\Lambda^\sigma_\nu\eta_{\rho\sigma}=\eta_{\mu\nu}$$Lorentz transformations are therefore described by the $4\times 4$ matrices $\Lambda^\sigma_\nu$ satisfying the above. These form the group [[Spacetime and Tensors#Lorentz group|$SO(3,1)$]], extending the spatial rotations $SO(3)$ by including Lorentz boosts. 

For example, the boost in the $x$ direction is given by$$\Large\Lambda=\begin{pmatrix}\gamma & -\gamma v & 0 & 0 \\ -\gamma v & \gamma & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}=\begin{pmatrix}\cosh\beta & -\sinh\beta & 0 & 0 \\ -\sinh\beta & \cosh\beta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}$$, where $\gamma$ is the Lorentz factor and $\beta$ is the rapidity ($\tanh\beta=v$).

The indices $\mu,\nu$ refer to a coordinate system $x^\mu$, except in the Lorentz transformation matrix where one index refers to the $\tilde x^\mu$ coordinates and the other refers to the $x^\mu$ coordinates. To hammer this point in, we write the matrix as the derivative of the coordinate transform:$$\Huge\frac{\partial \tilde x^\mu}{\partial x^\nu}=\Lambda^\mu_\nu$$Here, the inverse transformation from $\tilde x^\mu$ to $x^\nu$ is:$$\Huge\frac{\partial x^\nu}{\partial \tilde x^\rho}=(\Lambda^{-1})^\nu_\rho$$
# Curves and $4$-vectors:

Instead of thinking about particle velocities, we think about the path that the particle takes in space, parametrised by some parameter $\lambda$. We therefore define the [[Curves and Surfaces#Curves and curvature|curve]] our particle takes through space, the points of which are given by a function of the parameter $x^\mu(\lambda)$. The tangent vector is then defined:$$\Huge V^\mu=\frac{dx^\mu}{d\lambda}$$We call this the velocity $4$-vector, which encodes the same information as velocity. In this form, the vector transforms linearly under coordinate transformations, which is very useful as our traditional notion of velocity $\left(\frac{d\underline{x}}{dt}\right)$ would transform in a non-linear fashion under Lorentz transformations.

We can write the transformed tangent vector in terms of the original tangent vector by:$$\Large \tilde V^\mu=\frac{d\tilde x^\mu}{d\lambda}=\frac{\partial \tilde x^\mu}{\partial x^\nu}\frac{dx^\nu}{d\lambda}=\frac{\partial \tilde x^\mu}{\partial x^\nu}V^\nu$$Notice how this transforms in the same way coordinates do under Lorentz transformations, we will tend to focus on quantities that behave this way.

The coordinate transform can be thought of as a change in basis of the tangent space at a point in spacetime. That is, $\tilde V^\mu,V^\nu$ can be thought of as components of an abstract vector wrt different bases in this tangent space. Since Lorentz transformations leave the Minkowski metric invariant, we define the inner product (not really) on this space by:$$\Huge (V,W)=\eta_{\mu\nu}V^\mu W^\nu$$This is invariant under coordinate transformations:$$\Large\begin{aligned}
\eta_{\mu\nu}\tilde V^\mu\tilde W^\nu&=\eta_{\mu\nu}\left(\frac{\partial \tilde x_\mu}{\partial x^\rho}V^\rho\right)\left(\frac{\partial \tilde x^\nu}{\partial x^\sigma}W^\sigma\right)\\
&=\eta_{\mu\nu}\left(\frac{\partial \tilde x^\mu}{\partial x^\rho}\frac{\partial \tilde x^\nu}{\partial x^\sigma}\right)V^\rho W^\sigma\\
&=\Lambda^\mu_\rho\Lambda^\nu_\sigma\eta_{\mu\nu}V^\rho W^\sigma\\
&=\eta_{\rho\sigma}V^\rho W^\sigma
\end{aligned}$$
This is not actually an inner product, as it is not positive definite. This leads to a decomposition of the tangent space. Tangent vectors can be:
> Timelike if $(V,V)<0$ (inside lightcone)
> Null if $(V,V)=0$ (along lightcone)
> Spacelike if$(V,V)>0$ (outside lightcone)

Physical particles can only travel along timelike or null paths. 

For a spacelike curve, we can define an invariant length by integrating the root of its line element along the curve:$$\Huge l=\int\sqrt{ds^2}$$The infinitesimal distance along the curve in an interval $d\lambda$ for a curve $x^\mu(\lambda)$ is written as$$\Large ds^2=\eta_{\mu\nu}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda}(d\lambda)^2=(V,V)d\lambda^2$$where $V^\mu$ is the tangent vector, making the proper length:$$\Large l=\int\sqrt{V,V}d\lambda=\int\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}d\lambda$$This definition of length is independent of both parameter and coordinates on the spacetime, it is intrinsic to the path itself. We often parameterise by $\lambda=l$, that is we use [[Regular curves in Rn#Reparametrisations and unit speed i|arc length parametrised]] curves. 

For a timelike curve, we can define a similar invariant proper time elapsed along the curve:$$\Large \tau=\int\sqrt{-ds^2}=\int\sqrt{-(V,V)}d\lambda=\int\sqrt{-\eta_{\mu\nu}\dot x^\mu\dot x^\nu}d\lambda$$As $ds^2<0$ for timelike curves, this is well defined. The natural choice of parameter here is $\lambda=\tau$, corresponding to $\eta_{\mu\nu}V^\mu V^\nu=-1$. In this case, we call $V^\mu$ a timelike unit vector.

# Free motion:
Free particles in special relativity follow straight lines, we want to understand this in a way that will generalise to whatever spacetime we want. These analogous curves are called [[Geodesics|geodesics]], and are the most general formulation of a "straight line". We could propose that there exists a choice of parameter $\lambda$ such that $x^\mu(\lambda)$ are linear functions, implying $V^\mu=\frac{dx^\mu}{d\lambda}$ is constant. This is an equation of motion for the coordinates as a function of the parameter: $a^\mu=\frac{d^2x^\mu}{d\lambda^2}=0$. Note that we can write this as:$$\Large a^\mu=\frac{dx^\nu}{d\lambda}\partial_\nu(\frac{dx^\mu}{d\lambda})=V^\nu\partial_\nu V^\mu=0$$