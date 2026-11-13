
# Rossby number and [[Rotating fluids#Taylor-Proudman theorem|geostrophic balance]]:

We want to find a scale where we can see the effects of [[Stratification|stratification]] and [[Rotating fluids#Rotating reference frames|rotation]]. The characteristic length scale that marks the relative importance of these phenomena is known as the deformation radius$$\huge \mathcal{L}_d=\frac{N\mathcal{H}}{f_0}$$, where $\mathcal{H}$ is the vertical scale and $f_0,N$ are the [[Rotating fluids#Rotating frame dynamics|coriolis]] and [[Stratification#Buoyancy frequency|bouyancy frequency]]. For the atmosphere $\mathcal{L}_d\approx1000\text{km}$ and for the ocean $\mathcal{L}_d\approx100\text{km}$.

Let us scale our variables with the following characteristic values$$\Large\begin{aligned}
(x,y)=\mathcal{L}(x^*,y^*),\,\,z&=\mathcal{H}z^*,\,\,t=\mathcal{T}t^*\\
(u,v)=\mathcal{U}(u^*,v^*),\,\,w=\mathcal{W}w^*,\,\,p&=\mathcal{P}p^*,\,\,b=\mathcal{B}b^*,\,\,\underline{f}=f_0\underline{f}^*
\end{aligned}$$, where ${}^*$ represents a dimensionless quantity. Our $\beta$-plane approximation becomes $f^*=1+\frac{\beta}{f_0}y$. Proceeding to non-dimensionalise the hydrostatic rotating Boussinesq equations, first by writing $w$ terms out and using our horizontal nabla:$$\Large\begin{aligned}
\frac{\partial \underline{v}}{\partial t}+(\underline{v}\cdot\underline{\nabla}_H)\underline{v}+w\frac{\partial \underline{v}}{\partial z}+\underline{f}\times\underline{v}&=-\frac{1}{\rho_0}\underline{\nabla}_Hp\\
\frac{\mathcal{U}}{\mathcal{T}}\frac{\partial \underline{v}^*}{\partial t^*}+\frac{\mathcal{U}^2}{\mathcal{L}}(\underline{v}^*\cdot\underline{\nabla}_H^*)\underline{v}^*+\frac{\mathcal{WU}}{\mathcal{H}}w^*\frac{\partial \underline{v}^*}{\partial z^*}+f_0\mathcal{U}\underline{f}^*\times\underline{v}^*&=-\frac{1}{\rho_0}\frac{\mathcal{P}}{\mathcal{L}}\underline{\nabla}_H^*p^*\\
_{\text{dropping }*}\frac{1}{f_0\mathcal{T}}\frac{\partial \underline{v}}{\partial t}+\frac{\mathcal{U}}{f_0\mathcal{L}}(\underline{v}\cdot\underline{\nabla}_H)\underline{v}+\frac{\mathcal{W}}{f_0\mathcal{H}}w\frac{\partial \underline{v}}{\partial z}+\underline{f}\times\underline{v}&=-\frac{\mathcal{P}}{\rho_0f_0\mathcal{UL}}\underline{\nabla}_Hp\\
_{\text{eqn in }z}\implies\frac{\rho_0\mathcal{BH}}{\mathcal{P}}b&=\frac{\partial p}{\partial z}\\
_\text{mass continuity}\implies\underline{\nabla}_H\cdot\underline{v}+\frac{\mathcal{WL}}{\mathcal{UH}}\frac{\partial w}{\partial z}&=0\\
\implies\frac{1}{f_0\text{T}}\frac{\partial b}{\partial t}+\frac{\mathcal{U}}{f_0\mathcal{L}}(\underline{v}\cdot\underline{\nabla}_H)b+\frac{\mathcal{W}}{f_0\mathcal{H}}w\frac{\partial b}{\partial z}+\frac{N^2\mathcal{W}}{f_0\mathcal{B}}w&=0
\end{aligned}$$We see the prefactor $\frac{\mathcal{U}}{f_0\mathcal{L}}$ shows up a lot, and is an important dimensionless parameter known as the Rossby number:$$\huge\text{Ro}=\frac{\mathcal{U}}{f_0\mathcal{L}}$$This is essentially the time scale of rotational inertial effects $1/f_0$ over the time scale of Coriolis effects. Therefore for dominant Coriolis force, we expect small $\text{Ro}$. We also make the following assumptions:
> Horizontal scale is not significantly larger than deformation radius$$\Large \frac{\mathcal{L_d}}{\mathcal{L}}\approx 1=\mathcal{O}(1)$$, a direct translation of considering our length/height scales.
> Time scale is$$\Large \mathcal{T}=\frac{\mathcal{L}}{\mathcal{U}}$$, known as the eddy turnover time. A vortex with velocity $\mathcal{U}$ and diameter $\mathcal{L}$ will take time $\mathcal{T}$ to complete a full turn.
> We assume vertical velocity to scale as$$\large\mathcal{W}=\frac{\mathcal{UH}}{\mathcal{L}}$$, in order for $\frac{\partial w}{\partial z}$ to stay relevant in the continuity equation.
> The $\beta$ effect is an order $\epsilon$ smaller than $f_0$$$\Large \underline{f}^*=\left(\frac{f_0+\beta y^*}{f_0}\right)\underline{e}_z=\left(1+\frac{\beta\mathcal{L}}{f_0}y^*\right)\underline{e}_z=(1+\epsilon\beta^*y^*)\underline{e}_z$$, where $\beta^*$ is $\mathcal{O}(1)$ due to the assumption.

Using these assumptions, we write our non-dimensionalised equations in terms of $\epsilon$:$$\Large\begin{aligned}
\implies\epsilon\left(\frac{\partial \underline{v}^*}{\partial t^*}+(\underline{v}^*\cdot\underline{\nabla}_H^*)\underline{v}^*+w^*\frac{\partial \underline{v}^*}{\partial z^*}\right)+\underline{f}^*\times\underline{v}^*&=-\frac{\mathcal{P}}{\rho_0f_0\mathcal{LU}}\underline{\nabla}^*_Hp^*\\
\implies\frac{\rho_0\mathcal{BH}}{\mathcal{P}}b^*&=\frac{\partial p^*}{\partial z^*}\\
\implies\underline{\nabla}^*_H\cdot\underline{v}^*+\frac{\partial w^*}{\partial z^*}&=0\\
\epsilon\left(\frac{\partial b^*}{\partial t^*}+(\underline{v}^*\cdot\underline{\nabla}^*_H)b^*+w^*\frac{\partial b^*}{\partial z^*}\right)+\frac{N^2\mathcal{UH}}{f_0\mathcal{LB}}w^*&=0
\end{aligned}$$In order to have the same scaling for the pressure gradient and the Coriolis force, and to have the same scaling on the vertical momentum equation, we find fixed scales for $\mathcal{P,B}$:$$\huge\begin{aligned}
\mathcal{P}&=\rho_0f_0\mathcal{LU}\\
\mathcal{B}&=\frac{f_0\mathcal{LU}}{\mathcal{H}}
\end{aligned}$$Finally, for the vertical momentum equation we notice the scale on $w^*$ to be$$\Large \frac{N^2\mathcal{UH}}{f_0\mathcal{LB}}=\left(\frac{\mathcal{L_d}}{\mathcal{L}}\right)^2$$, making the set of equations:$$\Large\begin{aligned}
\epsilon\left(\frac{\partial \underline{v}}{\partial t}+(\underline{v}\cdot\underline{\nabla}_H)\underline{v}+w\frac{\partial \underline{v}}{\partial z}\right)+\underline{e}_z\times\underline{v}+\epsilon
\end{aligned}$$