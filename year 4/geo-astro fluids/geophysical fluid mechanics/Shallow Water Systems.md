
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
-\eta_0 & x>0\end{cases}=-\eta_0\text{sgn}(x)$$, noting that our fluid is initially at rest $u(x,t=0)=0$. To do our analysis, we assume disturbances to the initial state are relatively small. I.e. we write:$$\Large h(x,t)=H+\eta(x,t),\,\,u=u(x,t)$$Using these expressions in our shallow water equations leads to$$\Large\begin{aligned}
\frac{\partial u}{\partial t}+u\frac{\partial u}{\partial x}&=-g\frac{\partial \eta}{\partial x}\\
\frac{\partial \eta}{\partial t}+\frac{\partial }{\partial x}((H+\eta)u)&=0\\
_{\text{neglect products of }\eta,u}\implies\frac{\partial u}{\partial t}+g\frac{\partial \eta}{\partial x}&=0\\
\implies\frac{\partial \eta}{\partial t}+H\frac{\partial u}{\partial x}&=0
\end{aligned}$$, where we proceed to cross differentiate:$$\Large\begin{aligned}
\frac{\partial }{\partial x}\left(\frac{\partial u}{\partial t}+g\frac{\partial \eta}{\partial x}\right)&=\frac{\partial^2u}{\partial x\partial t}+g\frac{\partial^2\eta}{\partial x^2}=0\\
\frac{\partial }{\partial t}\left(\frac{\partial \eta}{\partial t}+H\frac{\partial u}{\partial x}\right)&=\frac{\partial^2\eta}{\partial t^2}+H\frac{\partial^2u}{\partial t\partial x}=0\\
_{\text{assume }\partial_x,\partial_t\text{ commute}}\implies\frac{\partial^2\eta}{\partial t^2}-c_0^2\frac{\partial^2\eta}{\partial x^2}&=0,\,\,c_0^2=gH
\end{aligned}$$This is just the one-dimensional wave equation, a surprise to no-one. For unbounded domains, we use the d'Alembert solution$$\Large\eta(x,t)=\frac{1}{2}(F(x-c_0t)+F(x+c_0t))$$, where $F$ is the initial condition. This makes our solution:$$\Large\begin{aligned}
\eta(x,t)&=-\frac{\eta_0}{2}(\text{sgn}(x-c_0t)+\sgn)
\end{aligned}$$