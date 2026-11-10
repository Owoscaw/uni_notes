
# Rotating reference frames:

Consider a fluid in two different frames:$$\Large\begin{aligned}
I&:&\{\underline{e}_1,\underline{e}_2,\underline{e}_3\}\\
R&:&\{\hat{\underline{e}}_1,\hat{\underline{e}}_2,\hat{\underline{e}}_3\}
\end{aligned}$$Here, $R$ is rotating with angular velocity $\underline{\Omega}$ relative to $I$. Defining $\left(\frac{d}{dt}\right)_I$ as the time derivative in the inertial frame $I$, we see that:$$\Large\begin{aligned}
\left(\frac{d\underline{e}_i}{dt}\right)_I&=0\\
\left(\frac{d\hat{\underline{e}}_i}{dt}\right)_I&\neq0 
\end{aligned}$$
Now consider a vector of constant length $\underline{C}$ rotating relative to the inertial frame with angular velocity $\underline{\Omega}$. Over a small interval of time $\delta t$, $\underline{C}$ rotates through an angle of $\delta\lambda$:![[Rotating fluids 2026-10-30 16.37.41.excalidraw]]It is clear that the change in $\underline{C}$, $\delta\underline{C}$ is then given by:$$\Large\begin{aligned}
\delta\underline{C}&=|\underline{C}|\sin(\gamma)\delta\lambda\underline{e}_n\\
&=|\underline{C}||\underline{\Omega}|\sin\gamma\,\delta t\underline{e}_n\\
&=\underline{\Omega}\times\underline{C}\,\delta t\\
\implies\left(\frac{d\underline{C}}{dt}\right)_I&=\underline{\Omega}\times\underline{C}
\end{aligned}$$This holds for any constant magnitude vector in the inertial frame. 

Let us consider a general vector with changing magnitude:$$\Large\underline{B}=B_1(t)\hat{\underline{e}}_1+B_2(t)\hat{\underline{e}}_2+B_3(t)\hat{\underline{e}}_3$$Since we define the vector in our rotating frame, it follows that:$$\Large \left(\frac{d\underline{B}}{dt}\right)_R=\frac{dB_i}{dt}\hat{\underline{e}}_i$$In the inertial frame, we have:$$\Large\begin{aligned}
\left(\frac{d\underline{B}}{dt}\right)_I&=\frac{d}{dt}(B_i(t)\hat{\underline{e}}_i)\\
&=\frac{dB_i}{dt}\hat{\underline{e}}_i+B_i\left(\frac{d\hat{\underline{e}}_i}{dt}\right)_I\\
&=\left(\frac{d\underline{B}}{dt}\right)_R+B_j\underline{\Omega}\times\hat{\underline{e}}_j\\
&=\left(\frac{d\underline{B}}{dt}\right)_R+\underline{\Omega}\times(B_j\hat{\underline{e}}_j)\\
&=\left(\frac{d\underline{B}}{dt}\right)_R+\underline{\Omega}\times\underline{B}
\end{aligned}$$
# Rotating frame dynamics:

Taking $\underline{B}=\underline{X}$ to be the position of a fluid parcel, we have$$\Large\left(\frac{d\underline{X}}{dt}\right)_I=\left(\frac{d\underline{X}}{dt}\right)_R+\underline{\Omega}\times\underline{X}\implies\underline{u}_I=\underline{u}_R+\underline{\Omega}\times\underline{X}$$where $\underline{u}_I$ is velocity in the inertial frame, and $\underline{u}_R$ is velocity in the rotating frame. We can then find the dynamics of acceleration by writing $\underline{B}=\underline{u}_I$:$$\Large\begin{aligned}
\left(\frac{d\underline{u}_I}{dt}\right)_I&=\left(\frac{d\underline{u}_I}{dt}\right)_R+\underline{\Omega}\times\underline{u}_I\\
&=\left(\frac{d}{dt}(\underline{u}_R+\underline{\Omega}\times\underline{X})\right)_R+\underline{\Omega}\times(\underline{u}_R+\underline{\Omega}\times\underline{X})\\
&=\left(\frac{d\underline{u}_R}{dt}\right)_R+\underline{\Omega}\times\left(\frac{d\underline{X}}{dt}\right)_R+\underline{\Omega}\times\underline{u}_R+\underline{\Omega}\times(\underline{\Omega}\times\underline{X})\\
&=\left(\frac{d\underline{u}_R}{dt}\right)_R+2\underline{\Omega}\times\underline{u}_R+\underline{\Omega}\times(\underline{\Omega}\times\underline{X})
\end{aligned}$$In an inertial frame, Newton's law gives$$\Huge\left(\frac{d\underline{u}_I}{dt}\right)_I=\frac{1}{m}\underline{F}$$, therefore in a rotating frame the parcel will obey:$$\Large \left(\frac{d\underline{u}_R}{dt}\right)_I=\frac{1}{m}\underline{F}-2\underline{\Omega}\times\underline{u}_R-\underline{\Omega}\times(\underline{\Omega}\times\underline{X})$$These extra forces on the RHS result from working in the non-inertial reference frame. Since these are a mathematical artefact and not physical forces, these are regarded as fictitious forces:
> The second RHS term is known as the Coriolis force, and if $\underline{\Omega}$ points up/down, the fluid parcel is deflected horizontally right/left observed in a rotating frame.
> The third RHS term is known as Centrifugal force, appearing to push objects away from the axis of rotation.

We can now write the [[Dynamics of ideal fluids#Revisiting the momentum equation|momentum equation]] in our rotating frame, by replacing $\frac{D\underline{u}_I}{Dt}$ with our expression we derived for the rotating time derivative above. In the case of the [[Stratification#Boussinesq equations|Boussinesq equation]], the momentum equation becomes:$$\Large \frac{D\underline{u}_r}{Dt}+2\underline{\Omega}\times\underline{u}_R+\underline{\Omega}\times(\underline{\Omega}\times\underline{X})=-\frac{1}{\rho_0}\underline{\nabla}p+b\underline{e}_z$$As density is a scalar, we can summarise the Boussinesq equations in a rotating frame as:$$\Large\begin{aligned}
\frac{D\underline{u}}{Dt}+2\underline{\Omega}\times\underline{u}+\underline{\Omega}\times(\underline{\Omega}\times\underline{X})&=-\frac{1}{\rho_0}\underline{\nabla}p+b\underline{e}_z\\
\underline{\nabla}\cdot\underline{u}&=0\\
\frac{Db}{Dt}+N^2(z)w&=0
\end{aligned}$$
## Centrifugal force as a potential:
We can simplify these equations if we are able to write the centrifugal force as the gradient of a scalar potential that can then be combined with pressure terms. Let us define a set of cylindrical polar coordinates $(s,\theta,z)$ in which the $z$-axis points along $\underline{\Omega}$, $s$ is then the perpendicular distance from the $z$-axis:$$\Large\begin{aligned}
_\text{cylindrical coordinates}\implies\underline{X}&=s\underline{e}_s+z\underline{e}_z\\
\implies\underline{\Omega}\times(\underline{\Omega}\times\underline{X})&=\Omega\underline{e}_z+\Omega s\underline{e}_\theta\\
&=-\Omega^2s\underline{e}_s
\end{aligned}$$This demonstrates that the centrifugal force pushes objects away from $\underline{\Omega}$. We aim to find a potential $\phi_c$ such that $\underline{\nabla}\phi_c=\underline{\Omega}\times(\underline{\Omega}\times\underline{X})$:$$\Large\frac{\partial \phi_c}{\partial s}=-\Omega^2s,\,\,\frac{\partial \phi_c}{\partial \theta}=\frac{\partial \phi_c}{\partial z}=0$$Therefore we can write:$$\Large \phi_c=-\frac{\Omega^2s^2}{2}=-\frac{1}{2}|\underline{\Omega}\times\underline{X}|^2$$We can therefore simplify the centrifugal force term in the rotating Boussinesq equations$$\Large \frac{D\underline{u}}{Dt}+2\underline{\Omega}\times\underline{u}=-\frac{1}{\rho_0}\underline{\nabla}p_r+b\underline{e}_z$$where $p_r=p+\rho_0\phi_c$.

## Tangent-plane approximation:
It is often convenient to work in reference frames rotating with a planet during the study of oceans and atmospheres. However, rotation forces often dominate and so we make two approximations. In spherical polars $(r,\theta,\phi)$ we have that$$\Large\underline{\Omega}=\Omega\sin\theta\,\underline{e}_r+\Omega\cos\theta\,\underline{e}_\theta$$, where $\theta$ is latitude and $\phi$ is longitude. That is to say, the most general form of $\underline{\Omega}$ has latitude dependent radial and meridional components. If we limit dynamics to a small region in $\theta$, we can make a set of simplifications by defining a tangent plane to the surface at some latitude $\theta_0$.

Taking the $z$-axis to point along $-\underline{\nabla}\Phi$ and writing $-\underline{\nabla}\Phi=g\underline{e}_z$, we take $x$ to point east and $y$ north with $y=0$ at $\theta=\theta_0$:![[Rotating fluids 2026-11-08 17.01.54.excalidraw]]In this approximation, gravity points (nearly) radially inwards so we take $\underline{e}_r\approx\underline{e}_z$ and $\underline{\theta}\approx\underline{e}_y$ at $\theta=\theta_0$:$$\Large\implies\underline{\Omega}\approx\Omega\sin\theta\,\underline{e}_z+\Omega\cos\theta\,\underline{e}_y$$For small $\theta-\theta_0$, $y\approx r_e(\theta-\theta_0)$ so:$$\Large\begin{aligned}
\sin(\theta)&=\sin(\theta_0-(\theta-\theta_0))=\sin\theta_0+(\theta-\theta_0)\cos\theta_0+\mathcal{O}((\theta-\theta_0)^2)\\
&\approx\sin\theta_0+\frac{\cos\theta_0}{r_e}y\\
\cos\theta&\approx\cos\theta_0-\frac{\sin\theta_0}{r_e}y\text{ similarly}
\end{aligned}$$Therefore if we write $\underline{\Omega}=\Omega_z\underline{e}_z+\Omega_y\underline{e}_y$ with$$\Large\begin{aligned}
\Omega_z&=\Omega\sin\theta_0+\frac{\Omega\cos\theta_0}{r_e}y\\
\Omega_y&=\Omega\cos\theta_0-\frac{\Omega\sin\theta_0}{r_e}y
\end{aligned}$$, we can write the Coriolis force $2\underline{\Omega}\times\underline{u}$ as:$$\Large2\underline{\Omega}\times\underline{u}=(2\Omega_yw-2\Omega_zv,2\Omega_zu,-2\Omega_yu)$$Therefore the cartesian components of the momentum equations under our approximation become:$$\Large\begin{aligned}
\frac{Du}{Dt}+2(\Omega_yw-\Omega_zv)&=-\frac{1}{\rho_0}\frac{\partial p}{\partial x}\\
\frac{Dv}{Dt}+2\Omega_zu&=-\frac{1}{\rho_0}\frac{\partial p}{\partial y}\\
\frac{Dw}{Dt}-2\Omega_yu&=-\frac{1}{\rho_0}\frac{\partial p}{\partial z}+b
\end{aligned}$$Further assuming that the layer is thin, we have $|w|<<|u|,|v|$ and so we drop the $\omega_yw$ term for the $x$-direction equation. To conserve energy we also drop the $-\Omega_yw$ term, leading to the equations:$$\Large\begin{aligned}
\frac{Du}{Dt}-fv&=-\frac{1}{\rho}\frac{\partial p}{\partial x}\\
\frac{Dv}{Dt}+fv&=-\frac{1}{\rho}\frac{\partial p}{\partial y}\\
\frac{Dw}{Dt}&=-\frac{1}{\rho}\frac{\partial p}{\partial z}+b\\
f&=2\Omega_z\\
\implies \frac{D\underline{u}}{Dt}+\underline{f}\times\underline{u}&=-\frac{1}{\rho}\underline{\nabla}p+b\underline{e}_z
\end{aligned}$$Where $\underline{f}=f(y)\underline{e}_z$. This is known as the traditional approximation, and $f$ is known as the Coriolis parameter. We often write$$\Large f=f_0+\beta y,\,\,f_0=2\Omega\sin\theta_0,\,\,\beta=\frac{2\Omega\cos\theta_0}{r_e}$$, called the $\beta$-plane approximation. Here, $\beta$ contains the latitudinal variations in $f$. For extremely localised flows, we do not need to take latitudinal variations into account $(\beta=0)$. This is known as the $f$-plane approximation.

Considering the tangent plane approximation, we can write our usual set of equations in the rotating frame:
> The rotating shallow water equations become:$$\Large\begin{aligned}
\frac{\partial \underline{v}}{\partial t}+(\underline{v}\cdot\underline{\nabla}_H)\underline{v}+\underline{f}\times\underline{v}&=-g\underline{\nabla}_H\eta\\
\frac{\partial h}{\partial t}+\underline{\nabla}_H\cdot(h\underline{v})&=0\\
h&=\eta-\eta_b
\end{aligned}$$
> The rotating hydrostatic Boussinesq equations become:$$\Large\begin{aligned}
\frac{\partial \underline{v}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{v}+\underline{f}\times\underline{v}&=-\frac{1}{\rho_0}\underline{\nabla}_Hp\\
\frac{1}{\rho_0}\frac{\partial p}{\partial z}&=b\\
\underline{\nabla}\cdot\underline{u}&=0\\
\frac{\partial b}{\partial t}+(\underline{u}\cdot\underline{\nabla})b+N^2w&=0
\end{aligned}$$
> The rotating non-hydrostatic Boussinesq equations become:$$\Large\begin{aligned}
\frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}+\underline{f}\times\underline{u}&=-\frac{1}{\rho_0}\underline{\nabla}p+b\underline{e}_z\\
\underline{\nabla}\cdot\underline{u}&=0\\
\frac{\partial b}{\partial t}+(\underline{u}\cdot\underline{\nabla})b+N^2(z)w&=0
\end{aligned}$$

# Rotationally dominated flow:

In fluid flows where the Coriolis force dominates other forces and acceleration terms, the horizontal components of the rotating Boussinesq equations reduce to:$$\huge \underline{f}\times\underline{u}=-\frac{1}{\rho_0}\underline{\nabla}_Hp$$This is known as Geostrophic Balance. Recalling our $2$-dimensional velocity $\underline{v}=(u,v,0)$, it follows that:$$\Large\underline{v}\cdot(\underline{f}\times\underline{u})=0\implies\underline{v}\cdot\underline{\nabla}_Hp=0$$Therefore horizontal wind will flow along lines of constant pressure.

## Taylor-Proudman theorem:
If we assume hydrostatic balance in the vertical direction, the $z$-direction equation dictates$$\huge\frac{\partial p}{\partial z}=-\rho g$$, and if we consider $\rho=\rho(z)$ then geostrophic balance in horizontal directions give:$$\Large\begin{aligned} &-fv=-\frac{1}{\rho_0}\frac{\partial p}{\partial x}&fu=-\frac{1}{\rho_0}\frac{\partial p}{\partial y}\\
\implies &v=\frac{\partial }{\partial x}\frac{p}{f\rho_0}&u=-\frac{\partial }{\partial y}\frac{p}{f\rho_0}\\
\implies&0=\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}
\end{aligned}$$So we must have $\frac{\partial w}{\partial z}=0$. That is, vertical velocity is independent of height. Since we assumed $\rho$ to be a function only in $z$ our equation for $p$ gives $\frac{\partial^2p}{\partial x\partial z}=\frac{\partial^2p}{\partial y\partial z}=0$. Then by the above we deduce $\frac{\partial u}{\partial z}=\frac{\partial v}{\partial z}=0$, horizontal flow independent of height.

This is known as the Taylor-Proudman theorem, which states that the fluid velocity is uniform along any line parallel to the axis of rotation for a fluid steadily rotated at high angular velocity.