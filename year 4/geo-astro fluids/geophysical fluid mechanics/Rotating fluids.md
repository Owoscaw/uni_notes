
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