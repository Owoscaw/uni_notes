
The shallow water equations model a thin layer of fluid with constant density, bounded by a rigid surface from below and a free surface from above. By "thin", we mean that the horizontal scale of our system is much larger than the vertical scale. 

# Derivation:

We assume the $z$ axis is perpendicular to the layer of water, $\eta(x,y,t)$ is the vertical position of fluid surface measured from $z=0$. Likewise, $\eta_b(x,y)$ is the vertical height of bottom topography. We use the mean fluid surface as $z=0$, leading to$$\Huge\iint_S\eta\,dx\,dy=0$$where $S$ is the entire surface of the fluid. $h(x,y,t)$ is the thickness of water column measured from bottom boundary all the way to free surface, $h=\eta-\eta_b$. We then define the constant $H$ as the average height of the fluid:$$\huge H=\frac{1}{S}\iint_S h\,dx\,dy$$The thinness of the fluid implies that vertical velocity is much smaller than horizontal velocity components, $w<<u,v$.

## Momentum equations:
One of the main consequence of small vertical velocity appears in the momentum equation. Consider the vertical momentum equation in the [[Stratification#Boussinesq equations|Boussinesq system]]:$$\huge \frac{\partial w}{\partial t}+(\underline{\dot v}\cdot\underline{\nabla}_H)w+w\frac{\partial w}{\partial z}=-\frac{1}{\tilde\rho}\frac{\partial p}{\partial z}-\frac{\rho}{\tilde\rho}g$$Assuming $w$ terms to be negligible, this reduces to:$$\Huge \frac{\partial p}{\partial z}=-\rho g$$This is exactly the [[Stratification#Hydrostatic approximation|hydrostatic balance]] condition we found previously. As we are assuming $\rho=\rho_0$, we integrate this equation from $\eta$ to arbitrary $z$:$$\Large\begin{aligned}
\int_\eta^z\frac{\partial p}{\partial z}dz&=-\int_\eta^z\rho g\,dz\\
\implies p(x,y,z,t)-p(x,y,\eta(x,y,t),t)&=\rho_0g(\eta(x,y,t)-z)
\end{aligned}$$We assume pressure at the free surface $p(x,y,z,t)$ is constant, so we can take the horizontal gradient of both sides to find:$$\Huge\underline{\nabla}_Hp=\rho g\underline{\nabla}_H\eta$$Now looking at the horizontal momentum equation, we find:$$\Large\begin{aligned}
\frac{\partial v}{\partial t}+(\underline{v}\cdot\underline{\nabla}_H)v+w\frac{\partial v}{\partial z}&=-\frac{1}{\rho_0}\underline{\nabla}_Hp\\
&=-g\underline{\nabla}_H\eta\\
_{\text{assuming}\,\underline{v}=\underline{v}(x,y,t)}\implies\frac{\partial \underline{v}}{\partial t}+(\underline{v}\cdot\underline{\nabla}_H)\underline{v}&=-g\underline{\nabla}_H\eta
\end{aligned}$$Note we assumed $\underline{v}$ is independent of $z$, this is motivated by the fact that the RHS was independent of $z$ - i.e. if the initial velocity was independent of $z$, it should remain independent $z$. We write the above equation as:$$\Huge \frac{D\underline{v}}{Dt}=-g\underline{\nabla}\eta$$

## Mass continuity equation:
Consider a column of shallow water:
![[Shallow Water Systems 2026-10-20 18.31.25.excalidraw]]The cross-sectional area of this column is $\Delta x\Delta y$. If fluid enters the column from the sides, height has to increase to conserve mass. Consider the two sides perpendicular to the $x$-axis, velocity normal to one of the sides is $u$. Velocity through the other normal surface will then be $u+\Delta x\frac{\partial u}{\partial x}$. Similarly, if the thickness of one side is $h$, the thickness has to expand to $h+\Delta x\frac{\partial h}{\partial x}$. The mass flux through one side is given by normal velocity $\times$ surface area $\times$ density. We can then calculate the mass flux along each axis:$$\Large\begin{aligned}
MF_x&=\rho_0 uh\Delta y-\rho_0\left(u+\Delta x\frac{\partial u}{\partial x}\right)\left(h+\Delta x\frac{\partial h}{\partial x}\right)\Delta y\\
&=-\rho_0\Delta x\frac{\partial u}{\partial x}h\Delta y-\rho_0 u\Delta x\frac{\partial h}{\partial x}\Delta y-\rho_0\Delta x\frac{\partial u}{\partial x}\Delta x\frac{\partial h}{\partial x}\Delta y\\
MF_y&=-\rho_0\Delta y\frac{\partial v}{\partial y}h\Delta x-\rho_0v\Delta y\frac{\partial h}{\partial y}\Delta x-\rho_0\Delta y\frac{\partial v}{\partial y}\Delta y\frac{\partial h}{\partial y}\Delta x
\end{aligned}$$The rate of change in mass in the fluid column is given by:$$\large\begin{aligned}
\rho_0\Delta x\Delta y\frac{\Delta h}{\Delta t}&=MF_x+MF_y\\
\implies\frac{\Delta h}{\Delta t}&=-\left(\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}+u\frac{\partial }{\partial x}+v\frac{\partial }{\partial y}+\Delta x\frac{\partial u}{\partial x}\frac{\partial }{\partial x}+\Delta y\frac{\partial v}{\partial y}\frac{\partial }{\partial y}\right)h\\
_{\Delta x,\Delta y,\Delta t\to0}\implies\frac{\partial h}{\partial t}&=-h\left(\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}\right)-u\frac{\partial h}{\partial x}-v\frac{\partial h}{\partial y}
\end{aligned}$$We write this using our material derivative or vector notation:$$\huge\frac{\partial h}{\partial t}+\underline{\nabla}\cdot(h\underline{v})=0,\,\,\text{or }\frac{Dh}{Dt}+h\underline{\nabla}\cdot\underline{v}=0$$Note that this is not divergence free, as fluid columns can be compressed by decreasing their height.

Putting this all together, we arrive at our inviscid shallow water equations:$$\huge\begin{aligned}
\text{momentum}&:\frac{D\underline{v}}{Dt}=-g\nabla\eta\\
\text{mass continuity}&:\frac{\partial h}{\partial t}+\underline{\nabla}\cdot(h\underline{v})=0\\
\text{height relation}&:h=\eta-\eta_b
\end{aligned}$$

# Dam break example:

## Deep water:
Consider an example of a dam/membrane creating two levels of fluid that we remove at $t=0$ to see how the fluid evolves in time:![[Shallow Water Systems 2026-10-25 15.31.31.excalidraw]]Since this is one dimensional flow, we can write our initial surface as$$\large\eta(x,t=0)=\begin{cases}\eta_0 & x<0 \\
-\eta_0 & x>0\end{cases}=-\eta_0\sgn(x)$$, noting that our fluid is initially at rest $u(x,t=0)=0$. To do our analysis, we assume disturbances to the initial state are relatively small. I.e. we write:$$\Large h(x,t)=H+\eta(x,t),\,\,u=u(x,t)$$Using these expressions in our shallow water equations leads to$$\Large\begin{aligned}
\frac{\partial u}{\partial t}+u\frac{\partial u}{\partial x}&=-g\frac{\partial \eta}{\partial x}\\
\frac{\partial \eta}{\partial t}+\frac{\partial }{\partial x}((H+\eta)u)&=0\\
_{\text{neglect products of }\eta,u}\implies\frac{\partial u}{\partial t}+g\frac{\partial \eta}{\partial x}&=0\\
\implies\frac{\partial \eta}{\partial t}+H\frac{\partial u}{\partial x}&=0
\end{aligned}$$, where we proceed to cross differentiate:$$\Large\begin{aligned}
\frac{\partial }{\partial x}\left(\frac{\partial u}{\partial t}+g\frac{\partial \eta}{\partial x}\right)&=\frac{\partial^2u}{\partial x\partial t}+g\frac{\partial^2\eta}{\partial x^2}=0\\
\frac{\partial }{\partial t}\left(\frac{\partial \eta}{\partial t}+H\frac{\partial u}{\partial x}\right)&=\frac{\partial^2\eta}{\partial t^2}+H\frac{\partial^2u}{\partial t\partial x}=0\\
_{\text{assume }\partial_x,\partial_t\text{ commute}}\implies\frac{\partial^2\eta}{\partial t^2}-c_0^2\frac{\partial^2\eta}{\partial x^2}&=0,\,\,c_0^2=gH
\end{aligned}$$This is just the one-dimensional wave equation, a surprise to no-one. For unbounded domains, we use the d'Alembert solution$$\Large\eta(x,t)=\frac{1}{2}(F(x-c_0t)+F(x+c_0t))$$, where $F$ is the initial condition. This makes our solution:$$\Large\begin{aligned}
\eta(x,t)&=-\frac{\eta_0}{2}(\sgn(x-c_0t)+\sgn(x+c_0t))\\
&=\begin{cases}\eta_0 & x<-c_0t\\
0 & -c_0t<x<c_0t\\
-\eta_0 & x>c_0t\end{cases}
\end{aligned}$$This suggests half of the disturbance moves backwards, and the other half forwards at the speed $c_0=\sqrt{gH}$. Note that this suggests the disturbances moves faster in deeper water:![[Shallow Water Systems 2026-10-25 15.53.38.excalidraw]]

## Nonlinear wet-dry break:
Now let us tackle this problem without neglecting small product terms, i.e. we do not linearise. Consider a reservoir with constant depth $H$ with a dry region next to it separated by a dam that we remove at $t=0$:![[Shallow Water Systems 2026-10-25 15.56.32.excalidraw]]
Over a flat ($\eta_0=0$) bottom, our one-dimensional shallow water equations become:$$\Large\begin{aligned}
\frac{\partial u}{\partial t}+u\frac{\partial u}{\partial x}&=-g\frac{\partial h}{\partial x}\\
\frac{\partial h}{\partial t}+\frac{\partial (hu)}{\partial x}&=0\\
h(x,0)&=\begin{cases}H & x<0\\
0 & x>0\end{cases}\\
u(x,0)&=0
\end{aligned}$$
We retain the nonlinear advection term. There is no specified length-scale here, so we expect the horizontal scale of the solution to grow with time. To determine the speed of this growth, we seek a solution of the form$$\Large h(x,t)=h(\xi),\,\,u(x,t)=u(\xi),\,\,\xi=\frac{x}{t^n}$$, because I say so. $\xi$'s $x$ and $t$ derivatives are calculated nicely:$$\Large\frac{\partial \xi }{\partial t}=-\frac{n}{t}\xi,\,\,\frac{\partial \xi}{\partial t}=\frac{1}{t^n}$$This makes our momentum equation:$$\Large-\frac{n\xi }{t}\frac{du}{d\xi }+\frac{u}{t^n}\frac{du}{d\xi }=-\frac{g}{t^n}\frac{dh}{d\xi }$$This highlights the benefit of seeking a solution in this form, the momentum equation is now an ODE. For this to hold for all time, we expect same $t$ dependence on LHS and RHS, forcing $n=1$. Note we could've done this with the mass equation aswell.

Over time evolution, the disturbed region will simply expand away from the initial dam position. This motivates a solution depending on $x,t$ through the relation:$$\Huge \xi=\frac{x}{t}$$This is known as a self-similar solution. Rewriting our space/time derivatives in terms of $\xi$$$\Large \frac{\partial }{\partial t}=-\frac{\xi}{t}\frac{d}{d\xi },\,\,\frac{\partial }{\partial x}=\frac{1}{t}\frac{d}{d\xi}$$makes the momentum and mass equations take form:$$\Large\begin{aligned}_\text{momentum }(u-\xi)\frac{du}{d\xi}+g\frac{dh}{d\xi }&=0\\
_\text{mass }(u-\xi )\frac{dh}{d\xi }+h\frac{du}{d\xi }&=0\\
\implies\begin{pmatrix}u-\xi  & g\\
h & u-\xi \end{pmatrix}\begin{pmatrix}u_\xi \\
h_\xi \end{pmatrix}&=0
\end{aligned}$$For a non-trivial solution, the determinant of this matrix must vanish:$$\huge\implies(u-\xi )^2=gh$$Writing $c=\sqrt{gh}$, we can write the above as $u-\xi=c$. Writing$$\Large h=\frac{c^2}{g},\,\,\frac{dh}{d\xi }=\frac{2c}{g}\frac{dc}{d\xi }$$we can substitute the above into our momentum equation to get:$$\Large\begin{aligned}
\frac{du}{d\xi}+2\frac{dc}{d\xi}&=0\\
\implies u+2c&=\text{constant}
\end{aligned}$$
To impose boundary conditions, we look at the left-had edge of the disturbance where the solution must match the undisturbed reservoir:$$\Large u=0,\,\,h=H\text{ at left-hand edge}$$Now using our relation between $u,c,\xi$ and $c_0=\sqrt{gH}$ we can write:$$\Large\begin{aligned}
u(\xi)&=\frac{2}{3}(c_0+\xi)\\
c(\xi)&=\frac{1}{3}(2c_0-\xi)\\
_{h=\frac{c^2}{g}}\implies h(\xi)&=\frac{1}{9g}(2c_0-\xi)^2\\
\implies u(x,t)&=\frac{2}{3}\left(c_0+\frac{x}{t}\right)\\
\implies h(x,t)&=\frac{1}{9g}\left(2c_0-\frac{x}{t}\right)^2
\end{aligned}$$We must still determine where we can apply this solution. At the left hand edge, $u=0,h=H\implies x/t=-c_0$. At the right hand edge, $h=0\implies x/t=2c_0$. Therefore our complete solution is:$$\Large (h,u)=\begin{cases}(H,0) & x<-c_0t \\
\left(\frac{1}{9g}\left(2c_0-\frac{x}{t}\right)^2,\frac{2}{3}\left(c_0+\frac{x}{t}\right)\right) & -c_0t<x<2c_0t \\
(0,0) & x>2c_0t\end{cases}$$