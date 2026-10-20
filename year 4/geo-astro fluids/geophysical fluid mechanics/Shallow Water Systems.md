
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