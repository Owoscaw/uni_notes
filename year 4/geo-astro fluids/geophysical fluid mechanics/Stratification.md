
# Buoyancy frequency:

Fluids in the atmosphere and ocean are typically stratified, i.e. their density varies with height. In a stable medium, a fluid parcel that is vertically displaced will return to its original position due to the effects of buoyancy. Therefore let us consider a fluid parcel![[Stratification 2026-10-10 21.04.45.excalidraw]]
At rest, we have hydrostatic balance and therefore:$$\Huge \frac{d\tilde p}{dz}=-g\tilde\rho$$Now consider what happens when we raise this parcel from $z=0$ to $z=Z$. To make the distinction between background density and parcel density, we write $\rho_p$ for the density of the parcel:$$\Large\begin{aligned}
\frac{d\tilde p}{dz}\vert_{z=0}&=-g\tilde\rho(0)=-g\rho_p(0)\\
\frac{d\tilde p}{dz}\vert_{z=Z}&=-g\tilde\rho(Z)
\end{aligned}$$Once displaced, hydrostatic equilibrium is broken. Since our parcel has fixed mass and is incompressible, its density does not change after being raised:$$\Huge \rho_p(Z)=\rho_p(0)=\tilde\rho(0)$$
The force due to the upward pressure gradient per unit volume is then$$\Large-\frac{d\tilde p}{dz}\vert_{z=Z}=g\tilde\rho(Z)$$, while its weight is $g\rho_p(Z)$. We can therefore find the net vertical force on the parcel once raised:$$\Large F_\text{net}=-\frac{d\tilde p}{dz}\vert_{z=Z}-g\rho_p(Z)=g(\tilde\rho(Z)-\rho_p(Z))$$Applying Newton's second law then goes like$$\Large\begin{aligned}
\rho_p(Z)\frac{d^2 Z}{dt^2}&=F_\text{net}\\
\implies \frac{d^2Z}{dt^2}&=\frac{g}{\rho_p(Z)}(\tilde\rho(Z)-\rho_p(Z))\\
&=\frac{g}{\tilde\rho(0)}(\tilde\rho(Z)-\tilde\rho(0))\\
&\approx\frac{g}{\tilde\rho(0)}\frac{d\tilde\rho}{dz}\vert_{z=0}Z
\end{aligned}$$where we Taylor expanded $\tilde\rho(Z)$ about $z=0$. We define a new constant:$$\Large N_0^2=-\frac{g}{\tilde\rho(0)}\frac{d\tilde\rho}{dz}\vert_{z=0}\implies \frac{d^2Z}{dt^2}=-N_0^2Z$$Once we release the parcel at, say, $t=0$ after raising it to, say, $Z=Z_0$. We must therefore solve$$\Large \frac{d^2Z}{dt^2}=-N_0^2Z,\,\,Z(0)=Z_0,\,\,\frac{dZ}{dt}(0)=0$$which has solution:$$\Huge Z(t)=Z_0\cos(N_0t)$$This is oscillatory motion with frequency $N_0$, hence the name "Buoyancy frequency". If we release our parcel from a general height instead of $z=0$, we define a more general buoyancy frequency:$$\Huge N^2(z)=-\frac{g}{\tilde\rho}\frac{d\tilde\rho}{dz}$$This gives the frequency of small oscillations of a fluid parcel in a stably stratified medium. Note that if the above derivative is positive, then $N^2<0$ and stratification is unstable as the parcel rises.

# Boussinesq equations:

For fluids where density/temperature varies slowly with horizontal displacement or in time(i.e. lower atmosphere, oceans), it makes sense to approximate density as a base value plus a small perturbation:$$\Large\rho(\underline{x},t)=\rho_0+\delta\rho(\underline{x},t),\,\,\rho_0>>\delta\rho$$Using this in the [[Dynamics of ideal fluids#Revisiting the momentum equation|momentum equation]] gives:$$\Large\begin{aligned}
(\rho_0+\delta\rho)\frac{D\underline{u}}{Dt}&=-\nabla p-(\rho_0+\delta\rho)g\underline{e}_z\\
\implies(\rho_0+\delta\rho)\frac{Dw}{Dt}&=-\frac{\partial p}{\partial z}-(\rho_0+\delta\rho)g\\
\implies\rho_0\frac{Dw}{dt}&=-\frac{\partial p}{\partial z}-\rho g+\mathcal{O}(\delta\rho^2)\\
\implies\frac{D\underline{u}}{Dt}&=-\frac{1}{\rho_0}\nabla p-\frac{\rho}{\rho_0}g\underline{e}_z
\end{aligned}$$Where we set $\delta\rho=0$ after collecting terms of order $\delta p^2$ and higher. These form the Boussinesq equations:$$\Large\begin{aligned}
\frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}&=-\frac{1}{\rho_0}\nabla p-\frac{\rho}{\rho_0}g\underline{e}_z\\
\underline{\nabla}\cdot\underline{u}&=0\\
\frac{D\rho}{Dt}&=\frac{\partial \rho}{\partial t}+(\underline{u}\cdot\underline{\nabla})\rho=0
\end{aligned}$$