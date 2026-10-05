
Recall the compressible Navier-Stokes:
> Conservation of mass:$$\Huge\frac{\partial \rho}{\partial t}+\underline{\nabla}\cdot(\rho\underline{ u})=\frac{D\rho}{Dt}+\rho\underline{\nabla}\cdot\underline{u}$$
> Conservation of momentum:$$\Huge \frac{D\underline{u}}{Dt}=\underline{f}_b-\frac{1}{\rho}\underline{\nabla}p+\frac{\nu}{3}\underline{\nabla}(\underline{\nabla}\cdot\underline{u})+\nu\nabla^2\underline{u}$$

Where $D/Dt$ is the [[Kinematics of Fluids#The material derivative|material derivative]], $\underline{f}_b$ are body forces, and $\nu$ is the kinetic viscosity. An incompressible fluid is that which has constant fluid parcel density over time, that is:$$\Huge\begin{align*}
\frac{D\rho}{Dt}&=0\\
\implies \underline{\nabla}\cdot\underline{u}&=0\\
\implies\frac{D\underline{u}}{Dt}&=\underline{f}_b-\frac{1}{\rho}\underline{\nabla}p+\nu\nabla^2\underline{u}
\end{align*}$$We impose two kinds of boundary condition:
> No-slip, $\underline{u}=0$ on the boundary
> Free-slip, normal velocity is zero

For a fluid in hydrostatic balance, $\underline{f}_b=-g\underline{e}_z$, which implies:$$\Huge \frac{Dw}{Dt}=-\frac{1}{\rho}\frac{\partial p}{\partial z}-g\approx 0\implies\frac{\partial p}{\partial z}=-\rho g$$At a fixed point $(x_0,y_0)$ we integrate from $z_0$ to $z$:$$\Huge P(x_0,y_0,z)-P(x_0,y_0,z_0)=-\int_{z_0}^z\rho(x_0,y_0,s)g\,ds$$
Consider an ideal atmosphere with no motion and constant temperature. This is an ideal gas equation so we have $p=\rho RT$ and we have:$$\Huge \frac{dp}{dz}=-\rho g\implies \frac{dp}{dz}=-\frac{g}{RT}p=-\frac{p}{H}$$Which has solution $p=p_0e^{-z/H}$.