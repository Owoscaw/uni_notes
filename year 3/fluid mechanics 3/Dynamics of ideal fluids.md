
We have previously described how fluids move with quantities like [[Kinematics of Fluids#Vorticity|vorticity]], however we still have not described why fluids move like this. What we have not considered yet is force. In general, fluids experience two types of force:
> "body forces" that act throughout the fluid 
> "surface forces" that act internally between fluid elements

One special type of surface force is the friction-like force between layers of fluid, creating the fluid's viscosity. Firstly we look at fluids with no viscosity, called inviscid. Furthermore if the fluid is incompressible we call it ideal.

# Conservation of momentum:

## The momentum equation:
Consider a fixed volume $V$ of fluid with surface $S$. The momentum is then:$$\Huge\int_V\rho\underline{u}\,dV$$where $\underline{u}$ is the velocity field and $\rho$ is the density. To show conservation of momentum, consider:
![[Dynamics of ideal fluids 2025-11-11 20.01.07.excalidraw]]Volume is fixed, but fluid particles can enter and leave the volume. We now show that the $i$-th component of the momentum is conserved:$$\Huge\begin{align*}
\frac{d}{dt}\int_V\rho u_i\,dV&=-\int_S\rho u_i(\underline{u}\cdot\underline{\hat{n}})\,dS+\int_VF_i\,dV\\
&=-\int_S\rho u_i\,\underline{u}\cdot d\underline{S}+\int_V F_i\,dV
\end{align*}$$Here, the dot product term represents the speed of the flow in the $\underline{\hat{n}}$ direction, and the whole first integrand represents the momentum flux through $dS$. For now, $\underline{F}$ represents the total force on $V$ per unit volume. As $V$ is fixed, we differentiate under the integral on the LHS and used [[Integral theorems#Divergence theorem|divergence theorem]] to show:$$\Huge\int_V\frac{\partial }{\partial t}(\rho u_i)dV=-\int_V\underline{\nabla}\cdot(\rho u_i\underline{u})dV+\int_VF_idV$$Now using the product rules for divergence we see that:$$\Huge\begin{align*}
\underline{\nabla}\cdot(\rho u_i\underline{u})&=\underline{\nabla}\cdot(u_i(\rho\underline{u}))=\rho\underline{u}\cdot\underline{\nabla}u_i+u_i\underline{\nabla}\cdot(\rho\underline{u})\\
\implies\int_V\frac{\partial \rho}{\partial t}u_i+\rho\frac{\partial u_i}{\partial t}dV&=\int_V(-\rho\underline{u}\cdot\underline{\nabla}u_i-u_i\underline{\nabla}\cdot(\rho\underline{u})+F_i)dV
\end{align*}$$Here, the $\frac{\partial \rho}{\partial t}u_i$ term cancels with the $u_i\underline{\nabla}\cdot(\rho\underline{u})$ term to leave us with:$$\Huge\int_V\rho\frac{\partial u_i}{\partial t}dV=\int_V-(\rho\underline{u}\cdot\underline{\nabla})u_i+F_i\,dV$$which we rewrite using the [[Kinematics of Fluids#The material derivative|material derivative]]:$$\Huge\int_V\rho\frac{Du_i}{Dt}dV=\int_VF_idV$$Which is simply another way to write $\underline{F}=m\underline{a}$. In vector form:$$\Huge\int_V\rho\frac{D\underline{u}}{Dt}dV=\int_V\underline{F}dV$$
## Body forces:
It is convenient to write body forces as accelerations:$$\Huge\int_V\underline{F}_\text{body}dV=\int_V\rho\underline{f}dV$$where $\underline{f}$ contains these accelerations. A common body force is gravity, written as $\underline{f}=-g\hat{\underline{e}}_z$. 

## Pressure:
If we consider two touching fluid elements, we ask why they do not merge into one another. At the microscale, fluid molecules are bouncing off each other all the way along the fluid element's surface. This is called pressure, and from a fluid element's perspective it pushes inwards all over the surface:$$\Huge\int_V\underline{F}_\text{pressure}dV=\int_S-p\underline{\hat{n}}\,dS=\int_S-p\,d\underline{S}$$
## The stress tensor:
We saw that pressure acts inwards on the fluid element, however this is not a general result. A fluid can have forces acting in any direction to its surface. We can encode forces acting on any surface by introducing the stress tensor, $\underline{\sigma}$, which is a $3\times3$ rank two tensor. 

Physically, the index $i$ of $\sigma_{ij}$ gives the coordinate direction in which the force acts, and the index  $j$ gives the orientation of the surface it is acting on. To find the stress on a surface with normal $\underline{\hat{n}}$ we take $\underline{\sigma}\cdot\underline{\hat{n}}$, which gives a vector with components $\sigma_{ij}n_j$:$$\Huge \int_V\underline{F}_\text{stress}dV=\int_S\underline{\sigma}\cdot\underline{\hat{n}}dV=\int_S\underline{\sigma}\cdot d\underline{S}$$![[Dynamics of ideal fluids 2025-11-11 20.22.40.excalidraw]]
Suppose we wish to calculate the stress on the surface in the $x$ direction. Then our normal is $\underline{\hat{n}}=\hat{\underline{e}}_x$:$$\Huge\underline{\sigma}\cdot\underline{\hat{n}}=\begin{pmatrix}\sigma_{11} & \sigma_{12} & \sigma_{13} \\ \sigma_{21} & \sigma_{22} & \sigma_{23} \\ \sigma_{31} & \sigma_{32} & \sigma_{33}\end{pmatrix}\begin{pmatrix}1 \\ 0 \\ 0\end{pmatrix}=\begin{pmatrix}\sigma_{11} \\ \sigma_{21} \\ \sigma_{31}\end{pmatrix}$$
In order to specify $\underline{\sigma}$, we need a model for how the particular fluid behaves. If the only internal force we want is pressure, acting normal to surfaces, then we can see that we just want $\sigma_{11},\sigma_{22},\sigma_{33}$ to be non-zero. Specifically, we want them to be $-p(\underline{x},t)$, so for an inviscid fluid the stress becomes:$$\Huge\underline{\sigma}=-p\mathbb{I}\iff \sigma_{ij}=-p\delta_{ij}$$
## Revisiting the momentum equation:
Using our understanding of stress, we can write:$$\Huge\begin{align*}
\int_V\rho\frac{D\underline{u}}{Dt}dV&=\int_V\underline{F}\,dV\\
&=\int_S\underline{\sigma}\cdot d\underline{S}+\int_V\rho\underline{f}\,dV\\
&=\int_V(\underline{\nabla}\cdot\underline{\sigma}^T+p\underline{f})dV\text{  (divergence thm)}\\
&=\int_V(-\underline{\nabla}p+p\underline{f})dV
\end{align*}$$for an inviscid fluid. Now assuming the smoothness of the integrant, the only way this result holds for an arbitrary domain $V$ is for the PDE to hold:$$\Huge\rho\frac{D\underline{u}}{Dt}=-\underline{\nabla}p+p\underline{f}\iff\frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}=-\frac{1}{\rho}\underline{\nabla}p+\underline{f}$$The form with a general stress is known as the Cauchy momentum equation. The specific form we have written with pressure alone is known as the Euler equation.

# Incompressible Euler equations:

Since the body force $\underline{f}$ is imposed, we have a set of four equations (including the [[Kinematics of Fluids#The material derivative|continuity equation]]) in $\Re^3$ but have five unknowns ($\rho,u,v,w,p$), we require another equation to complete the system.

The simplest choice would be to assume that the fluid has constant uniform density $\rho=\rho_0$, making the fluid incompressible. This simplifies the continuity equation and defines the system:$$\Huge\begin{align*}
\underline{\nabla}\cdot\underline{u}&=0\\
\frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}&=-\frac{1}{\rho_0}\underline{\nabla}p+\underline{f}
\end{align*}$$known as the incompressible Euler equations. We now have four equations and four unknowns, but no boundary conditions.

Since inviscid fluids have no friction at the boundaries, fluid is free to flow tangential to the boundary. Therefore we can impose $\underline{u}\cdot\underline{\hat{n}}=0$ (no normal flow).

## Mug example:
Take for example a mug containing a volume of tea:$$\Huge V=\{\underline{x}\in\Re^3:x^2+y^2\leq R^2,-h\leq z\leq0\}$$under gravity $\underline{f}=-g\hat{\underline{e}}_z$. Realistic boundary conditions would be:$$\Huge\begin{align*}
z=-h&:\underline{\hat{n}}=-\hat{\underline{e}}_z,\,\,\underline{u}\cdot\underline{\hat{n}}=0\\
r=R&:\underline{\hat{n}}=\hat{\underline{e}}_r,\,\,\underline{u}\cdot\underline{\hat{n}}=0
\end{align*}$$We could allow for motion at the top surface, but for simplicity we assume $\underline{u}\cdot\underline{\hat{n}}=0$ at $z=0$ also. A trivial example of a solution would be $\underline{u}=\underline{0}$. We ask what the pressure has to be in order for this to be a correct solution. To do this, we look at the momentum equation, which becomes:$$\Huge\begin{align*}
\hat{\underline{e}}_x&:0=-\frac{1}{\rho_0}\frac{\partial p}{\partial x}\implies p\neq p(x)\\
\hat{\underline{e}}_y&:0=-\frac{1}{\rho_0}\frac{\partial p}{\partial y}\implies p\neq p(y)\\
\hat{\underline{e}}_z&:0=-\frac{1}{\rho_0}\frac{\partial p}{\partial z}-g\implies p(z)=-\rho_0gz+C
\end{align*}$$Where the constant $C$ is determined by setting the pressure at the surface $z=0$ equal to atmospheric pressure $p_\text{atm}$, giving us:$$\Huge p(z)=p_\text{atm}-\rho_0gz$$This solution is known as hydrostatic equilibrium. We can also calculate the net force exerted on an object submerged in the fluid:$$\Huge\begin{align*}
\int_{V_\text{object}}\underline{F}_\text{pressure}dV&=\int_{S_\text{object}}-p\,d\underline{S}\\
&=\int_{V_\text{object}}-\underline{\nabla}p\,dV\\
&=\int_{V_\text{object}}\rho_0g\hat{\underline{e}}_z\,dV=\rho_0gV\hat{\underline{e}}_z
\end{align*}$$where $V$ is the volume of the object. The result is simply the negative of the weight of the displaced fluid, known as buoyancy. 

Another possible velocity that satisfies the boundary conditions is an axisymmetric flow:$$\Huge \underline{u}=G(r)\hat{\underline{e}_\theta}$$in cylindrical coordinates. Writing down the divergence, we see that the continuity equation is satisfied:$$\Huge\underline{\nabla}\cdot\underline{u}=\frac{1}{r}\frac{\partial }{\partial r}(ru_r)+\frac{1}{r}\frac{\partial u_\theta}{\partial \theta}+\frac{\partial u_z}{\partial z}=\frac{\partial G(r)}{\partial \theta}=0$$Next we look at the momentum equation. To do this, we need $(\underline{u}\cdot\underline{\nabla})\underline{u}$ in cylindrical coordinates:$$\Huge\begin{align*}
(\underline{u}\cdot\underline{\nabla})\underline{u}&=\left(u_r\frac{\partial }{\partial r}+\frac{u_\theta}{r}\frac{\partial }{\partial \theta}+u_z\frac{\partial }{\partial z}\right)(u_r\hat{\underline{e}}_r+u_\theta\hat{\underline{e}}_\theta+u_z\hat{\underline{e}}_z)\\
&=\frac{G}{r}\frac{\partial }{\partial \theta}(G\hat{\underline{e}}_\theta)\\
&=\frac{G^2}{r}\frac{\partial \hat{\underline{e}_\theta}}{\partial \theta}=-\frac{G^2}{r}\hat{\underline{e}}_r
\end{align*}$$Making the momentum equation (since $\partial_t\underline{u}=0$):$$\Huge-\frac{G^2}{r}\hat{\underline{e}}_r=-\frac{1}{\rho_0}\underline{\nabla}p-g\hat{\underline{e}}_z$$To solve for the pressure, we first write:$$\Huge p(\underline{x})=p_h(z)+p_d(\underline{x})$$where $p_h=p_\text{atm}-\rho_0gz$ is the hydrostatic pressure from before, and $p_d$ is called the dynamic pressure. Then the pressure gradient becomes:$$\Huge\begin{align*}
\underline{\nabla}p&=\underline{\nabla}p_h+\underline{\nabla}p_d\\
&=-\rho_0g\hat{\underline{e}}_z+\underline{\nabla}p_d\\
\implies-\frac{G^2}{r}\hat{\underline{e}}_r&=-\frac{1}{\rho_0}\underline{\nabla}p_d
\end{align*}$$which we solve component wise:$$\Huge\begin{align*}
\hat{\underline{e}}_\theta&:0=\frac{1}{\rho_0r}\frac{\partial p_d}{\partial \theta}\implies p_d\neq p_d(\theta)\\
\hat{\underline{e}}_z&:0=\frac{1}{\rho_0}\frac{\partial p_d}{\partial z}\implies p_d=p_d(z)\\
\hat{\underline{e}}_r&:\frac{G^2}{r}=\frac{1}{\rho_0}\frac{\partial p_d}{\partial r}\implies p_d(r)=\int\rho_0\frac{G(r)^2}{r}dr
\end{align*}$$Making the full pressure:$$\Huge p(\underline{x})=p_\text{atm}-\rho gz+\int\rho_0\frac{G(r)^2}{r}dr$$
# Conservation of energy:

We ask what are the [[year 3/solitons 3/Conservation laws#Standard methodology|conserved quantities]] for the incompressible Euler equations. Firstly, we consider kinetic energy.

## Kinetic energy:
For a fluid region $V$, we define the kinetic energy as:$$\Huge E=\frac{1}{2}\int_V\rho_0|\underline{u}|^2dV$$Verifying that it is indeed conserved:$$\Huge\begin{align*}
\frac{dE}{dt}&=\frac{d}{dt}\int_V\frac{1}{2}\rho_0|\underline{u}|^2dV\\
&=\frac{1}{2}\int_V\rho_0\frac{\partial }{\partial t}(\underline{u}\cdot\underline{u})dV\\
&=\frac{1}{2}\int_V\rho_0(2\underline{u}\cdot\underline{u}_t)dV\\
\text{using Euler eqns}&=\int_V\rho_0\underline{u}\cdot(-(\underline{u}\cdot\underline{\nabla})\underline{u}-\frac{1}{\rho_0}\underline{\nabla}p+\underline{f})dV\\
&=\int_V
\rho_0\underline{u}\cdot(-(\underline{\nabla}\times\underline{u})\times\underline{u}+\frac{1}{2}\underline{\nabla}(|\underline{u}|^2-")dV\\
&=\int_V\rho_0\underline{u}\cdot\left(-\frac{1}{2}\underline{\nabla}\left(|\underline{u}^2|\right)-\frac{1}{\rho_0}\underline{\nabla}p+\underline{f}\right)dV\\
\text{assuming }f\text{ conservative}&=-\int_V\rho_0\underline{u}\cdot\underline{\nabla}\left(\frac{1}{2}|\underline{u}|^2+\frac{p}{\rho_0}+\Phi\right)dV\\
\text{defining }H(x,t)&=-\int_V\rho\underline{u}\cdot\underline{\nabla}H(\underline{x},t)dV\\
&=-\int_V\rho_0(\underline{\nabla}\cdot(H\underline{u})-H\underline{\nabla}\cdot\underline{u})dV\\
&=-\rho_0\int_V\underline{\nabla}\cdot(H\underline{u})dV\\
&=-\rho_0\int_SH\underline{u}\cdot d\underline{S}=0
\end{align*}$$which holds when $\underline{u}\cdot\underline{n}_S=0$ on the surface ,$S$, of the fluid region $V$. Therefore kinetic energy is a conserved quantity. 

# Bernoulli's principle:

When $\underline{f}$ is a conservative field, the momentum equation becomes:$$\Huge\begin{align*}
\frac{\partial u}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}&=-\frac{1}{\rho_0}\underline{\nabla}p-\underline{\nabla}\Phi\\
\frac{\partial u}{\partial t}+(\underline{\nabla}\times\underline{u})\times\underline{u}&=-\underline{\nabla}\left(\frac{p}{\rho_0}+\frac{1}{2}|\underline{u}|^2+\Phi\right)\\
&=-\underline{\nabla}H(\underline{x},t)
\end{align*}$$If the flow is steady ($u_t=0$), and we take the dot product with $\underline{u}$ we get:$$\Huge \underline{u}\cdot\underline{\nabla}H(\underline{x},t)=0$$where $H$ is called the "energy head". This equation says that $\underline{\nabla}H$ is constant along [[Kinematics of Fluids#Streamlines|streamlines]]. This is known as Bernoulli's principle, and has two conditions:
> Incompressible, steady, ideal flow
> Conservative body force $\underline{f}=-\underline{\nabla}\Phi$

In such case:$$\Huge H(\underline{x},t)=\frac{1}{2}|\underline{u}|^2+\frac{p}{\rho_0}+\Phi$$is constant along streamlines. The first term is interpreted as kinetic energy, the second is interpreted as an internal "heat-like" energy, and the last is interpreted as potential.

## Pitot tube example:
A Pitot tube is used to measure airspeed on an aircraft, usually attached near the cockpit:![[Dynamics of ideal fluids 2025-11-18 13.21.58.excalidraw]]
Then by Bernoulli's principle:$$\Huge \frac{1}{2}u_1^2+\frac{p_1}{\rho_0}=0+\frac{p_2}{\rho_0}\implies u_1=\sqrt{\frac{2(p_2-p_1)}{\rho_0}}$$so we can find airspeed by knowing the pressure inside and outside the aircraft.

## Mug with a hole example:
Recalling the mug we previously discussed, consider a hole drilled with area $a$ on the side at the base:![[Dynamics of ideal fluids 2025-11-18 13.29.12.excalidraw]]In which case we have $\underline{f}=-g\hat{\underline{e}}_z=-\underline{\nabla}\Phi\implies\Phi=gz$. Assuming that the hole is small ($a/A<<1$), then the flow will be approximately steady and we can use Bernoulli's principle. We then ask how $u$ depends on $h$. Here, the mass flux at the exit must be equal to the mass flux at the surface:$$\Huge\int_{S_a}\rho_0\underline{u}\cdot d\underline{S}=\rho_0ua=\rho_0UA=\int_{S_A}\rho_0\underline{U}\cdot d\underline{S}\implies U=\frac{a}{A}u$$Bernoulli's principle then dictates that the energy head at the surface is the same as the energy head at the exit:$$\Huge\frac{1}{2}u^2+\frac{p_\text{atm}}{\rho_0}+0=\frac{1}{2}U^2+\frac{p_\text{atm}}{\rho_0}+gh$$Combining these two conditions gives:$$\Huge\begin{align*}
u^2-U^2&=2gh\\
\implies u^2\left(1-\frac{a^2}{A^2}\right)&=2gh\\
\implies u&=\sqrt\frac{2gh}{1-\frac{a^2}{A^2}}\\
\implies u&\approx\sqrt{2gh}\,\,,\frac{a}{A}<<1
\end{align*}$$which is analogous to the classical mechanics scenario with a ball being dropped at height $h$.

## Bernoulli's principle for steady potential flows:
If $\underline{\nabla}\times\underline{u}=0$ then we have $\underline{u}=\underline{\nabla}\phi$ and $\frac{\partial u}{\partial t}=0$, the momentum equation reduces to:$$\Huge \underline{\nabla}H=0\implies H=\text{constant}$$so we get a stronger condition, that the energy head is constant throughout space, not just along streamlines.
### Line vortex example:
Consider the flow defined by a [[Kinematics of Fluids#Vorticity|line vortex]]:$$\Huge \underline{u}=\frac{k}{r}\hat{\underline{e}}_\theta,\,\,r>0$$![[Dynamics of ideal fluids 2025-11-18 13.49.18.excalidraw]]Then we have:$$\Huge \frac{P(r)}{\rho_0}+\frac{1}{2}\left(\frac{k}{r}\right)^2+gh=\frac{p_\text{atm}}{\rho_0}+0+gh$$where we have used the $r\to\infty$ case for the RHS. We can then solve for $P(r)$ (pressure close to the vortex):$$\Huge P(r)=p_\text{atm}-\frac{\rho_0}{2}\left(\frac{k}{r}\right)^2$$
# Vorticity dynamics:

We have seen that it is sometimes convenient to describe flows in terms of [[Kinematics of Fluids#Vorticity|vorticity]] rather than velocity, so we aim to find a momentum equation in terms of vorticity. First we take a conservative body force $\underline{f}=-\underline{\nabla}\Phi$ and use the same vector identity we used in deriving Bernoulli's principle:$$\Huge \frac{\partial \underline{u}}{\partial t}+(\underline{\nabla}\times\underline{u})\underline{u}=-\underline{\nabla}\left(\frac{p}{\rho_0}+\frac{1}{2}|\underline{u}|^2+\Phi\right)$$As we are aiming for vorticity, it seems natural to take the curl of this, which completely eliminates the RHS and we are left with:$$\Huge \frac{\partial \underline{\omega}}{\partial t}+\underline{\nabla}\times(\underline{\omega}\times \underline{u})=0$$known as the vorticity equation, describing conservation of angular momentum. We can also write this using the vector identity:$$\Huge\begin{align*}
\underline{\nabla}\times(\underline{\omega}\times\underline{u})&=\underline{\omega}\underline{\nabla}\cdot\underline{u}-\underline{u}\underline{\nabla}\cdot\underline{\omega}+(\underline{u}\cdot\underline{\nabla})\underline{\omega}-(\underline{\omega}\cdot\underline{\nabla})\underline{u}\\
&=(\underline{u}\cdot\underline{\nabla})\underline{\omega}-(\underline{\omega}\cdot\underline{\nabla})\underline{u}
\end{align*}$$as we are considering incompressible fluids. Therefore we can write:$$\Huge \frac{\partial \underline{\omega}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{\omega}=(\underline{\omega}\cdot\underline{\nabla})\underline{u}\iff\frac{D\underline{\omega}}{Dt}=(\underline{\omega}\cdot\underline{\nabla})\underline{u}$$An interesting observation here is that fluid elements with no vorticity do not gain any when they move with the fluid. Given that this holds for any conservative body force, we ask where vorticity comes from?

Consider a two-dimensional time-dependent flow:$$\Huge \underline{\omega}=\omega\hat{\underline{e}}_z\implies(\underline{\omega}\cdot\underline{\nabla})=\omega\frac{\partial }{\partial z}\implies(\underline{\omega}\cdot\underline{\nabla})\underline{u}=0$$As $\underline{u}$ has no $z$-component. In the vorticity equation we are left with:$$\Huge \frac{D\omega}{Dt}=0$$That is, vorticity is conserved for each fluid particle in a two-dimensional flow and is simply advected along the particle path.

## Line vortices example:
This is exactly why we saw that line vortices in potential flow were advected by the overall flow. We can calculate the direction of motion of a given line vortex at a given position and time by considering the flow from all other vortices at this position. 

This interaction leads to the self propulsion of vortex pairs, or vortices travelling along walls due to their image. As $\underline{u}$ is two-dimensional and incompressible, we have a stream function $\underline{u}=\underline{\nabla}\times\psi\hat{\underline{e}}_z$ and can write:$$\Huge\begin{align*}
\omega&=\hat{\underline{e}}_z\cdot\underline{\omega}\\
&=\hat{\underline{e}}_z\cdot(\underline{\nabla}\times \underline{u})\\
&=\hat{\underline{e}}_z\cdot\underline{\nabla}\times(\underline{\nabla}\times\psi\hat{\underline{e}}_z)=-\underline{\nabla}^2\psi
\end{align*}$$
# Circulation dynamics:

Consider a curve $C(t)$ that evolves with the flow of the fluid, we then ask how the circulation evolves in time. As $C$ evolves with the flow, it makes sense to use the time derivative that follows the flow (material derivative):$$\Huge\begin{align*}
\frac{D\Gamma}{Dt}&=\oint_{C(t)}\frac{D}{Dt}(\underline{u}\cdot d\underline{x})\\
&=\oint_{C(t)}\left(\frac{D\underline{u}}{Dt}\cdot d\underline{x}+\underline{u}\cdot\frac{D(d\underline{x})}{Dt}\right)
\end{align*}$$We now use the Euler equation for a conservative body force $\underline{f}=-\underline{\nabla}\Phi$, which allows us to rewrite the first term and find:$$\Huge\begin{align*}
\oint_{C(t)}\frac{D\underline{u}}{Dt}\cdot d\underline{x}&=\oint_{C(t)}-\underline{\nabla}\left(\frac{p}{\rho_0}+\Phi\right)\cdot d\underline{x}\\
&=0
\end{align*}$$as this is an integral of a continuous gradient field around a closed loop.

We now observe the second term, noticing that $D(d\underline{x})/Dt$ is the rate of change of the length of a line segment:$$\Huge\begin{align*}
\oint_{C(t)}\underline{u}\cdot\frac{D(d\underline{x})}{Dt}&=\oint_{C(t)}\underline{u}\cdot d\underline{u}\\
&=\frac{1}{2}\oint_{C(t)}d(|\underline{u}|^2)=0
\end{align*}$$as this is integrating an exact derivative around a curve. 

Putting both terms together we arrive at Kelvin's circulation theorem. This states that in an ideal, incompressible fluid with conservative body force, the circulation around a closed material curve $C(t)$ is constant in time:$$\Huge\frac{D\Gamma}{Dt}=0$$
## Aeroplanes:
Aeroplane wings are designed so that air travels faster over above than below. By Bernoulli's theorem, this produces lower pressure above the wing than below, creating lift. 

Since an aeroplane wing needs faster flow above than below, there must be negative circulation around its wing. Kelvin's theorem therefore implies that for an aeroplane starting from rest ($\Gamma=0$ around the wing) in ideal air, it must shed a starting vortex of opposite sign in order to conserve circulation:![[Dynamics of ideal fluids 2025-11-25 14.59.39.excalidraw]]This indeed happens in real life, although the creation of starting vortices requires the presence of viscosity.

Thinking about the circulation around the wing, we get a vortex tube along the wing and another tube rotating in the opposite direction just behind it. We know that these cant just end mid air, so it makes sense that these tubes connect at the ends, forming a closed loop (like smoke rings). The connecting tube at the end of the wing is said to contain "wing tip vortices". These are visible when an aircraft passes through clouds at landing and takeoff. If air were ideal, these would extend globally.