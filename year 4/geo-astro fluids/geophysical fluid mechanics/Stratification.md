
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
\end{aligned}$$Note that this can be done for a compressible fluid as well. This approximation is valid almost everywhere in the ocean, since density variations are small. This also applies for bands of the atmosphere confined to $1\text{km}$ or less.

# Buoyancy as a variable:

Consider splitting our variables into a reference state and perturbations to said state. Consider a static, time-independent reference state with a vertical density stratification $\rho=\tilde\rho(z)$. The second and third Boussinesq equations are satisfied, and the first demands:$$\Large p=\tilde p(z)\text{ with }\frac{d\tilde p}{dz}=-\tilde\rho g$$This makes our variable decomposition:$$\Large\underline{u}=\underline{u}'(\underline{x},t),\,\,\rho=\tilde\rho(z)+\rho'(\underline{x},t),\,\,p=\tilde p(z)+p'(\underline{x},t)$$Here, the prime quantities represent perturbations to reference states. Substituting the above into the first Boussinesq equation gives:$$\Large\begin{aligned}
\frac{\partial \underline{u}'}{\partial t}+(\underline{u}'\cdot\underline{\nabla})\underline{u}'&=-\frac{1}{\rho_0}\nabla(\tilde p+p')-\frac{\tilde\rho +\rho'}{\rho_0}g\underline{e}_z\\
&=-\frac{1}{\rho_0}\left(\frac{d\tilde p}{dz}\underline{e}_z\right)-\frac{1}{\rho_0}\tilde\rho g\underline{e}_z-\frac{1}{\rho_0}\nabla p'-\frac{\rho'}{\rho_0}g\underline{e}_z\\
&=-\frac{1}{\rho_0}\nabla p'+b\underline{e}_z
\end{aligned}$$Here, we used the condition on $\frac{d\tilde p}{dz}$ and introduce the buoyancy variable:$$\Huge b=-\frac{\rho'}{\rho_0}g$$The second Boussinesq equation trivially gives $\underline{\nabla}\cdot\underline{u}'=0$, while the third reads:$$\Large\begin{aligned}
\frac{\partial }{\partial t}(\tilde\rho +\rho')+(\underline{u'}\cdot\underline{\nabla})(\tilde\rho+\rho')&=0\\
\frac{\partial \rho'}{\partial t}+(\underline{u}'\cdot\underline{\nabla})\rho'+\underline{u}'\cdot\left(\frac{d\tilde\rho}{dz}\underline{e}_z\right)&=\\
\frac{\partial \rho'}{\partial t}+(\underline{u}'\cdot\underline{\nabla})\rho'+w \frac{d\tilde\rho}{dz}&=
\end{aligned}$$Introducing the buoyancy variable by multiplying through with $-\frac{g}{\rho_0}$ we find$$\begin{aligned}\Large\frac{Db}{Dt}+(-\frac{g}{\rho_0}\frac{d\tilde\rho}{dz})w'&=0\\
\implies\frac{Db}{Dt}+N^2(z)w'&=\\
\text{where }N^2(z)&=-\frac{g}{\rho_0}\frac{d\tilde\rho}{dz}
\end{aligned}$$Note that the buoyancy frequency $N(z)$ here is slightly different to the previous definition. These form our Non-hydrostatic Boussinesq equations:$$\Large\begin{aligned}
\frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}&=-\frac{1}{\rho_0}\nabla p+b\underline{e}_z\\
\underline{\nabla}\cdot\underline{u}&=0\\
\frac{\partial b}{\partial t}+(\underline{u}\cdot\underline{\nabla})b+N^2(z)w&=0
\end{aligned}$$Note that here, $p$ is the perturbation to background pressure and $\rho$ is the perturbation to the background density. Buoyancy frequency is often measured and can be used to identify different regions of the atmosphere:
![[Capture.png]]


# Lee waves caused by stratification:

An interesting phenomenon that arises from stratification is the generation of lee waves. Consider a gentle mountain (i.e. slowly varying height) that is periodic and described by$$\Huge h=h_0\sin(kx)$$where $h_0$ is the height of the mountain. A windspeed of $U$, which we assume constant, blows over the mountain and displaces air parcels vertically. We expect buoyancy to act as a restoring force on the displaced parcels:![[Stratification 2026-10-13 03.31.59.excalidraw]]

Consider a steady, two-dimensional version of this problem, assuming variations in $y$ are negligible. Writing the flow variables as background plus perturbation gives:$$\Large u=U+u',\,\,v=0,\,\,w=w',\,\,p=p',\,\,b=b'$$Substituting these into the non-hydrostatic Boussinesq equations (neglecting $\partial_y,\partial_t$ for obvious reasons) gives:$$\Large\begin{aligned}
\left((U+u')\frac{\partial }{\partial x}+w'\frac{\partial }{\partial z}\right)(U+u',0,w')&=-\frac{1}{\rho_0}\nabla p'+b'\underline{e}_z\\
\underline{e}_x\implies (U+u')\frac{\partial }{\partial x}(U+u')+w'\frac{\partial }{\partial z}(U+u')&=-\frac{\partial p'}{\partial x}\\
\implies(U+u')\frac{\partial u'}{\partial x}+w'\frac{\partial u'}{\partial z}&=-\frac{\partial p'}{\partial x}\\
\underline{e}_z\implies(U+u')\frac{\partial w'}{\partial x}+w'\frac{\partial w'}{\partial z}&=-\frac{\partial p'}{\partial z}+b'\\
\underline{\nabla}\cdot(U+u',0,w')&=0\\
\implies\frac{\partial u'}{\partial x}+\frac{\partial w'}{\partial z}&=0\\
\left((U+u')\frac{\partial }{\partial x}+w'\frac{\partial }{\partial z}\right)b'+N^2w'&=0\\
 U\frac{\partial b'}{\partial x}+b'\left(\frac{\partial u'}{\partial x}+\frac{\partial w'}{\partial z}\right)+N^2w'&=\\
\implies U\frac{\partial b'}{\partial x}+N^2w'
&=0\end{aligned}$$
We can neglect products of disturbance quantities, as these will be small (akin to discarding $\epsilon^2$ terms). This gives us the linearised version of the above:$$\Large\begin{aligned}
U\frac{\partial u}{\partial x}&=-\frac{\partial p}{\partial x}\\
U\frac{\partial w}{\partial x}&=-\frac{\partial p}{\partial z}+b\\
\frac{\partial u}{\partial x}+\frac{\partial w}{\partial z}&=0\\
U\frac{\partial b}{\partial x}+N^2w&=0
\end{aligned}$$We can eliminate $u,p,$ and $b$ to write this purely in terms of $w$:$$\Huge \frac{\partial^2w}{\partial x^2}+\frac{\partial^2w}{\partial z^2}=-\frac{N^2}{U^2}w$$This is known as the Helmholtz equation. 

At the ground, a fluid parcel follows the terrain. The surface of the mountain is described by $z=h(x)$, so the vertical velocity of a parcel on the surface is:$$\Huge w=\frac{Dh}{Dt}$$In our steady, two-dimensional flow this reduces to:$$\Large w(x,z=h)=(U+u')\frac{\partial h}{\partial x}$$For small mountains, we linearise this condition by evaluating at $z=0$ and neglecting the higher order disturbance term $u'\frac{\partial h}{\partial x}$:$$\Large w(x,z=0)\approx U\frac{\partial h}{\partial x}$$Using our model for the mountain, the lower boundary condition becomes:$$\Large w(x,z=0)=h_0Uk\cos(kx)$$And so we seek a solution of the form$$\Large w(x,z)=h_0 Uk\cos(kx+mz)$$, which we substitute into our equation for $w$:$$\Large\begin{aligned}
h_0Uk\frac{\partial^2}{\partial x^2}\cos(kx+mz)+h_0Uk\frac{\partial^2}{\partial z^2}\cos(kx+mz)&=-\frac{N^2k}{U}\cos(kx+mz)\\
-h_0Uk(k^2+m^2)\cos(kx+mz)&=\\
\implies\left(-k^2-m^2+\frac{N^2}{U^2}\right)h_0Uk\cos(kx+mz)&=0
\end{aligned}$$For this to hold $\forall x,z$, we require:$$\Huge -k^2-m^2+\frac{N^2}{U^2}=0$$Hence we write, assuming $\frac{N}{U}>k$:$$\Large m^2=\frac{N^2}{U^2}-k^2,\,\,m=\pm\sqrt{\frac{N^2}{U^2}-k^2}$$This condition is favoured by strong stratification, weak winds, or sufficiently long wavelengths. We must determine which sign of $m$ corresponds to a physical solution. We expect energy to propagate upwards. Vertical wave energy flux is given by $pw$, pressure work:$$\Large\begin{aligned}
w&=h_0Uk\cos(kx+mz)\\
\implies\frac{\partial u}{\partial x}&=h_0Ukm\sin(kx+mz)\\
\implies\frac{\partial p}{\partial x}&=-h_0U^2km\sin(kx+mz)\\
\implies p&=h_0U^2m\cos(kx+mz)\\
\implies pw&=h_0^2 U^3km\cos^2(kx+mz)
\end{aligned}$$Since $x$ is taken to be the direction of the background wind we have $U>0$, and we take $k>0$ as $\cos^2\geq0$. The sign of vertical energy flux is therefore determined by the sign of $m$, and so we naturally take the positive branch as we expect energy to propagate away from the mountains:$$\Huge m=+\sqrt{\frac{N^2}{U^2}-k^2}$$Hence our final solution is:$$\Large\begin{aligned}
w&=h_0Uk\cos\left(kx+\sqrt{\frac{N^2}{U^2}-k^2}z\right)\\
u&=-h_0U\sqrt{\frac{N^2}{U^2}-k^2}\cos\left(kx+\sqrt{\frac{N^2}{U^2}-k^2}z\right)\\
p&=h_0U^2\sqrt{\frac{N^2}{U^2}-k^2}\cos\left(kx+\sqrt{\frac{N^2}{U^2}-k^2}\right)
\end{aligned}$$In sufficiently moist air, the upward displacement can cause condensation and therefore cloud bands along oscillatory paths:
![[Capture (2).png]]

In reality, mountains are not purely sinusoidal but can actually be decomposed using a Fourier transform. Since all of our equations are linear, the wave response to each Fourier component can be calculated and the solutions superposed.

If we have no stratification, $N=0$, our equation for $w$ reduces to $\frac{\partial^2w}{\partial x^2}+\frac{\partial^2w}{\partial z^2}=0$, leading to a decaying solution with the same sinusoidal ground forcing:$$\Large N=0\implies w=h_0Uke^{-kx}\cos(kx)$$
## Hydrostatic approximation:
A common approximation is to assume horizontal scale is much larger than the vertical scale. In such case, vertical components in the momentum equation are replaced by the hydrostatic balance equation. This gives the hydrostatic Boussinesq equations:$$\Large\begin{aligned}
\frac{\partial v}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}&=-\frac{1}{\rho_0}\nabla_H
p\\
\frac{\partial p}{\partial z}&=\rho_0b=-\rho g\\
\underline{\nabla}\cdot\underline{u}&=0\\
\frac{\partial b}{\partial t}+(\underline{u}\cdot\underline{\nabla})b+N^2w&=0\end{aligned}$$Where $\underline{u}=(u,v)$ is horizontal velocity and $\nabla_H=\left(\frac{\partial }{\partial x},\frac{\partial }{\partial y}\right)$.