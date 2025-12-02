
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
## Linearisation:
The full system is nonlinear and therefore difficult to solve, but we can find approximate solutions by assuming that changes in $\eta,\phi$ are small and approximating the first and last equations using linearisation.

In a linearisation, we choose some fixed value for each variable and consider a small perturbation around that value:$$\Huge\begin{align*}
\eta(x,t,y)&\rightarrow\eta_0+\epsilon\eta_1(x,y,t)\\
\phi(x,y,z,t)&\rightarrow\phi_0+\epsilon\phi_1(x,y,z,t)
\end{align*}$$where $\epsilon<<1$. We make these substitutions and ignore anything of order $\epsilon^2$ or greater. This produces equations involving $\eta_0,\eta_1,\phi_0,\phi_1$ without any quadratic (or higher) terms, hence the name "linearisation".

We are looking for small-amplitude waves, so we perturb around the solution when the fluid is at rest (equilibrium). This imposes $\eta_0=0$ and $\phi_0$ constant so that $\underline{u}=\underline{\nabla}\phi=\underline{0}$:$$\Huge\begin{align*}
\eta&\rightarrow0+\epsilon\eta_1\\
\phi&\rightarrow\phi_0+\epsilon\phi_1
\end{align*}$$Our system therefore becomes:$$\Huge\begin{align*}
\underline{\nabla}^2\phi_1&=0,\,\,-h<z<\epsilon\eta_1\\
\frac{\partial \phi_1}{\partial z}&=0,\,\,z=-h\\
\frac{\partial \eta_1}{\partial t}+\epsilon\underline{\nabla}\phi_1\cdot\underline{\nabla}\eta_1&=\frac{\partial \phi_1}{\partial z},\,\,z=\epsilon\eta_1\\
\frac{\partial \phi_1}{\partial t}+\frac{1}{2}\epsilon|\underline{\nabla}\phi_1|^2+g\eta_1&=0,\,\,z=\epsilon\eta_1
\end{align*}$$We now neglect the terms with a leading $\epsilon$.

Now we use a Taylor series expansion to expand derivatives of $\phi_1$ at the free surface about the fixed plane $z=\eta_0=0$, giving:$$\Huge\begin{align*}
\frac{\partial \phi_1}{\partial z}|_{z=\epsilon\eta_1}&=\frac{\partial \phi_1}{\partial z}|_{z=0}+\epsilon\eta_1\frac{\partial^2\phi_1}{\partial z^2}|_{z=0}+\dots\\
\frac{\partial \phi_1}{\partial t}|_{z=\epsilon\eta_1}&=\frac{\partial \phi_1}{\partial t}|_{z=0}+\epsilon\eta_1\frac{\partial^2\phi_1}{\partial z\partial t}|_{z=0}+\dots
\end{align*}$$To maintain consistency, we neglect terms with leading $\epsilon$, giving us a fully linearised system. We proceed cheekily, dropping the subscript:$$\Huge\begin{align*}
\underline{\nabla}^2\phi&=0,\,\,-h<z<0\\
\frac{\partial \phi}{\partial z}&=0,\,\,z=-h\\
\frac{\partial \eta}{\partial t}&=\frac{\partial \phi}{\partial z},\,\,z=0\\
\frac{\partial \phi}{\partial t}+g\eta&=0,\,\,z=0
\end{align*}$$
# Travelling waves in an infinite domain:

## Solution for specific wavenumber:
We have our simplified, linearised system. Now we look for a separable travelling plane wave solution of the form:$$\Huge \phi(x,z,t)=X(x-ct)Z(z)$$That is, we look for solutions that move at a constant phase speed $c$ along the $x$-direction. Substituting this into our first equation gives:$$\Huge\begin{align*}
0=\underline{\nabla}^2\phi&=\frac{\partial^2\phi}{\partial x^2}+\frac{\partial^2\phi}{\partial z^2}\\
&=X''Z+XZ''\\
\implies-\frac{X''}{X}&=\frac{Z''}{Z}=\lambda
\end{align*}$$for some constant $\lambda$. We know that one of $X,Z$ must be periodic, and the other will be non-periodic. A solution periodic in $x-ct$ would be nice, so we look at the kinematic and floor boundary conditions:$$\Huge\begin{align*}
XZ'&=0,\,\,z=-h\\
XZ'&=\frac{\partial \eta}{\partial t},\,\,z=0
\end{align*}$$We do not want periodicity in $Z$ so we set $\lambda=k^2$ and start by solving:$$\Huge \frac{Z''}{Z}=k^2,\,\,Z'(-h)=0$$which has general solution:$$\Huge Z(z)=A\cosh(kz)+B\sinh(kz)$$but could also be:$$\Huge Z(z)=A\cosh(k(z+h))+B\sinh(k(z+h))$$we choose this form by convention, as it makes implementing the $Z'(-h)=0$ condition easy:$$\Huge \implies B=0,\,\,Z(z)=A\cosh(k(z+h))$$
Now the $X$ equation gives:$$\Huge X(x-ct)=\tilde C\cos(k(x-ct))+\tilde D\sin(k(x-ct))$$or equivalently:$$\Huge X(x-ct)=C\cos(k(x-ct)+\alpha)$$Since we can set $t=0$ to be any reference point we want, we can choose it to be such that $\alpha=0$ and hence:$$\Huge X(x-ct)=C\cos(k(x-ct))=C\Re(e^{ik(x-ct)})$$
Our solution for a given $k$ is therefore:$$\Huge \phi(x,z,t)=\Re(A(k)\cosh(k(z+h))e^{ik(x-ct)})$$for a combined, real constant $A(k)$.