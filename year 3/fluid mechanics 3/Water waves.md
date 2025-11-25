
We now combine our notions of [[Dynamics of ideal fluids#Incompressible Euler equations|the incompressible Euler equations]] and [[Kinematics of Fluids#Potential flows|potential flows]] to explore a class of solutions known as free surface water waves.

# Governing equations:

We assume that water is inviscid, incompressible, and irrotational. We impose the body force of gravity $\underline{f}=-g\hat{\underline{e}}_z$. The irrotational assumption is justified because there is no vorticity at rest, and we saw that vorticity cannot just appear.

As our domain is simply connected, the irrotational assumption means that we can write $\underline{\nabla}\phi$ for some potential. Using our assumptions we simply get potential flow, governed by Laplace's equation:$$\Huge\underline{\nabla}^2\phi=0,\,\,-h<z<\eta$$
We then have the boundary conditions:
> No flow through the floor. That is, $\underline{n}\cdot\underline{\hat{n}}=0$ on $z=-h$, which gives:$$\Huge\frac{\partial \phi}{\partial z}=0,\,\,z=-h$$
> No flow through the surface at $z=\eta(x,y,t)$. Here we want $\underline{u}\cdot\underline{\hat{n}}=0$ again, but $\underline{\hat{n}}$ here is more complicated as it changes with time. Our condition is equivalent to demanding that a particle on the surface stays on the surface. This is to say if $\underline{u}=(u,v,w)$:$$\Huge\begin{align*}
\frac{D\eta}{Dt}=\frac{Dz}{Dt}&\iff\frac{\partial \eta}{\partial t}+\underline{u}\cdot\underline{\nabla}\eta=w\\
&\iff\frac{\partial \eta}{\partial t}+\underline{\nabla}\phi\cdot\underline{\nabla}\eta=\frac{\partial \phi}{\partial z}\,\,\text{on }z=\eta
\end{align*}$$This is known as the kinematic boundary condition.
> Constant surface pressure. We can set the surface pressure to be whatever we want, so we choose $p=0$ on $z=\eta$. Constant pressure means that we neglect both surface tension and "wind". Using the momentum equation written in "energy head" form, we use the fact that our fluid is irrotational to write $\frac{\partial \underline{u}}{\partial t}=\underline{\nabla}\left(\frac{\partial \phi}{\partial t}\right)$:$$\Huge\begin{align*}
\underline{\nabla}\left(\frac{\partial \phi}{\partial t}+\frac{p}{\rho_0}+\frac{1}{2}|\underline{\nabla}\phi|^2+gz\right)&=0\\
\implies\frac{\partial \phi}{\partial t}+\frac{p}{\rho_0}+\frac{1}{2}|\underline{\nabla}\phi|^2+gz&=C(t)
\end{align*}$$where we set $C(t)=0$ by incorporating it into $\phi$, since adding a uniform function of time to $\phi$ will not change $\underline{u}=\underline{\nabla}\phi$. This gives Bernoulli's principle for unsteady potential flow:$$\Huge\frac{\partial \phi}{\partial t}+\frac{p}{\rho_0}+\frac{1}{2}|\underline{\nabla}\phi|^2+gz=0$$which we evaluate at the surface to get the dynamic boundary condition:$$\Huge\frac{\partial \phi}{\partial t}+\frac{1}{2}|\underline{\nabla}\phi|^2+g\eta=C(t)$$

Our combined system then becomes:$$\Huge\begin{align*}
\underline{\nabla}^2\phi&=0\,\,\text{on }-h<z<\eta\\
\frac{\partial \phi}{\partial z}&=0\,\,\text{on }z=-h\\
\frac{\partial \eta}{\partial t}+\underline{\nabla}\phi\cdot\underline{\nabla}\eta
&=\frac{\partial \phi}{\partial z}\,\,\text{on }z=\eta\\
\frac{\partial \phi}{\partial t}+\frac{1}{2}|\underline{\nabla}\phi|^2+g\eta&=0\,\,\text{on }z=\eta\end{align*}$$