
# Review:

Let us recall some of our technology around wave solutions and how we manipulate them. First, let us consider a sinusoidal plane wave:$$\Large\psi(\underline{x},t)=\mathcal{M}\cos(\underline{k}\cdot\underline{x}-\omega t)+\mathcal{N}\sin(\underline{k}\cdot\underline{x}-\omega t)$$Here, $\underline{k}$ is a three-vector called the wave vector, $|\underline{k}|$ is the wave number, and we think of the argument of $\cos,\sin$ as an angle $\theta=\underline{k}\cdot\underline{x}-\omega t$. Writing $A^2=\mathcal{M}^2+\mathcal{N}^2$, we can write the plane wave solution as a single cosine term:$$\Large\psi(\underline{x},t)=A\cos(\underline{k}\cdot\underline{x}-\omega t+\phi_0)$$Here, we define $\phi_0$ as the initial phase shit related to $\mathcal{M},\mathcal{N},A$ by:$$\Large \cos\phi_0=\frac{\mathcal{M}}{A},\,\,\sin(\phi_0)=\frac{\mathcal{N}}{A}$$Note we also write this as the real part of a complex exponential:$$\Large\psi(\underline{x},t)=\Re(Ce^{i(\underline{k}\cdot\underline{x}-\omega t)})$$We also define the wavelength $\lambda=2\pi/|\underline{k}|$ and the wave period $T=2\pi/\omega$. Plane wave solutions tend to be the solution for [[Partial differential equations#Hyperbolic PDEs|hyperbolic]] PDEs. We often use a PDE to find a dispersion relation between $\omega$ and $\underline{k}$. In generality, these relations may involve $\underline{x},t$ as well:$$\Large\text{PDE}\implies\omega=\Omega(\underline{k};\underline{x},t)$$Recall our notions of phase $c_p$ and group $c_g$ velocities. If $c_p$ is independent of $\underline{k}$, the wave will be non-dispersive and the wave will hold its shape throughout time. To arrive at group velocity, consider the sum of two plane waves with different wavenumbers (and therefore $\omega$):$$\Large \psi=A(e^{i(k_1x-\omega_1t)}+e^{i(k_2x-\omega_2t)})$$Consider the case where $\omega_1,\omega_2$ are close together, $(\omega_1,\omega_2)\to(\omega+\Delta\omega,\omega-\Delta\omega)$:$$\Large\begin{aligned}
\psi&=A(e^{i((k+\Delta k)x-(\omega+\Delta\omega)t)}+e^{i((k-\Delta k)x-(\omega-\Delta \omega)t)})\\
&=Ae^{i(kx-\omega t)}(e^{i(\Delta k\,x-\Delta \omega\,t)}+e^{i(-\Delta kx+\Delta\omega\,t)})\\
&=2\cos(x\Delta k-t\Delta\omega)Ae^{i(kx-\omega t)}
\end{aligned}$$We see that the amplitude of the superposition is modulated by the $\cos$ factor in the front. This envelope will propagate with group velocity $c_g$. In the limit $\Delta k,\Delta\omega\to0$, this defines our group velocity:$$\huge c_g=\underline{\nabla}_k\omega$$Group velocity is important, as it is the velocity at which mass/energy will propagate.

# Poincare waves:

Recall the timescale for [[Geostrophic theory#Quasigeostrophy|QG]] $T=\mathcal{L}/U$. With a different timescale with small [[Geostrophic theory#Rossby number and Rotating fluids Taylor-Proudman theorem geostrophic balance|Rossby number]], we can still find wave dynamics (in the shallow water equations). Placing $z$ at the mean free-surface level, we start with the shallow water equations:$$\Large\begin{aligned}
\frac{\partial \underline{v}}{\partial t}+(\underline{v}\cdot\underline{\nabla})\underline{v}+\underline{f}\times\underline{v}&=-g\underline{\nabla}_H\eta\\
\frac{\partial \eta}{\partial t}+H\underline{\nabla}_H\cdot\underline{v}+\underline{\nabla}_H\cdot(\eta\underline{v})&=0
\end{aligned}$$Let us nondimensionalise this with the following:$$\Large (x,y)=\mathcal{L}(x^*,y^*),\,\,(u,v)=U(u^*,v^*),\,\,t=\frac{1}{f_0}t^*,\,\,\eta=\frac{f_0\mathcal{L}U}{g}\eta^*,\,\,f=\frac{1}{f_0}f^*$$This is similar to the scaling for geostrophic theory, however with a characteristic timescale $1/f_0$ as opposed to the advective timescale $\mathcal{L}/U$. Proceeding to nondimensionalise,$$\Large\begin{aligned}
\frac{\partial \underline{v}^*}{\partial t^*}+\text{Ro}(\underline{v}^*\cdot\underline{\nabla}_H^*)\underline{v}^*+\underline{f}_0^*\times\underline{v}^*&=-\underline{\nabla}^*_H\eta^*\\
\frac{\partial \eta^*}{\partial t^*}+\left(\frac{\mathcal{L}_d}{\mathcal{L}}\right)^2\underline{\nabla}_H^*\cdot\underline{v}^*+\text{Ro}\underline{\nabla}_H^*\cdot(\eta^*\underline{v}^*)&=0
\end{aligned}$$which, in the small Rossby number limit, becomes:$$\Large\begin{aligned}
\frac{\partial \underline{v}^*}{\partial t^*}+\underline{f}_0^*\times\underline{v}^*&=-\underline{\nabla}^*_H\eta^*\\
\frac{\partial \eta^*}{\partial t^*}+\left(\frac{\mathcal{L}_d}{\mathcal{L}}\right)^2\underline{\nabla}_H^*\cdot\underline{v}^*&=0
\end{aligned}$$These are the linearised shallow water equations, which we redimensionalise:$$\Large\begin{aligned}
\frac{\partial \underline{v}}{\partial t}+\underline{f}\times\underline{v}&=-g\underline{\nabla}_H\eta\\
\frac{\partial \eta}{\partial t}+H\underline{\nabla}_H\cdot\underline{v}&=0
\end{aligned}$$We have essentially recovered linear equations with the timescale $1/f_0$, small Rossby limit, and $\mathcal{L}_d\approx\mathcal{L}$. Therefore, wave solutions will be admitted and we can analyse the wave dynamics.

Now let us use our wave ansatz $u=\tilde u e^{i\theta},v=\tilde ve^{i\theta},\eta=\tilde\eta e^{i\theta}$. Substituting this in to each component of the linearised shallow water equations:$$\Large\begin{aligned}
-i\omega\tilde v e^{i\theta}-f\tilde v e^{i\theta}&=-g(ik_x)\tilde\eta e^{i\theta}\\
-i\omega\tilde v e^{i\theta}+f\tilde u e^{i\theta}&=-g(ik_y)\tilde\eta e^{i\theta}\\
-i\omega\tilde\eta e^{i\theta}+H(ik_x)\tilde ue^{i\theta}+H(ik_y)\tilde v e^{i\theta}&=0\\
\implies\begin{pmatrix}-i\omega & -f & ik_xg\\
f & -i\omega & ik_yg\\
ik_xH & ik_yH & -i\omega\end{pmatrix}\begin{pmatrix}\tilde u\\
\tilde v\\
\tilde \eta\end{pmatrix}&=0
\end{aligned}$$The only nontrivial solution for this is given by setting the determinant of the matrix to $0$:$$\Large\begin{aligned}
\implies (-i\omega)(-\omega^2+k_y^2gH)+f(-i\omega f+k_xk_ygH)+ik_xg(ifk_yH-k_xH\omega)&=0\\
-i\omega(-\omega^2+k_y^2gH)-i\omega f^2-i\omega k_x^2gH&=0\\
\omega(\omega^2-ghk_y^2-ghk_x^2-f^2)&=0
\end{aligned}$$This has roots given by:$$\Large \omega(\underline{k})=\begin{cases}0  \\
\pm\sqrt{f^2+gH(k_x^2+k_y^2)}\end{cases}$$We have found our dispersion relation, so let us proceed by finding phase and group velocity:$$\Large\begin{aligned}
\underline{c}_p&=\frac{\omega(\underline{k})}{|\underline{k}|}\frac{\underline{k}}{|\underline{k}|}=\frac{\pm\sqrt{f^2+gH(k_x^2+k_y^2)}}{k_x^2+k_y^2}\underline{k}\\
\underline{c}_g&=\left(\frac{\partial \omega}{\partial k_x},\frac{\partial \omega}{\partial k_y}\right)=\left(\frac{\pm gHk_x}{\sqrt{f^2+gH\left(k_x^2+k_y^2\right)}},\frac{\pm gHk_y}{\sqrt{f^2+gH(k_x^2+k_y^2)}}\right)\\
&=\left(\frac{gHk_x}{\omega},\frac{gHk_y}{\omega}\right)=\frac{gH}{\pm\sqrt{f^2+gH(k_x^2+k_y^2)}}\underline{k}\\
\frac{|\underline{c}_g|}{|\underline{c}_p|}&=\frac{gH/\omega}{\omega/|\underline{k}|^2}=\frac{gH|\underline{k}|^2}{\omega^2}=\frac{gH(k_x^2+k_y^2)}{f^2+gH(k_x^2+k_y^2)}=\frac{\mathcal{L}_d^2(k_x^2+k_y^2)}{1+\mathcal{L}_d^2(k_x^2+k_y^2)}
\end{aligned}$$