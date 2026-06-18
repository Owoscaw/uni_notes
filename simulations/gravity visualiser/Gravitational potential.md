
If we imagine the force due to gravity on a mass $m$ as a conservative vector valued field over space $\underline{f}:\Re^2\rightarrow\Re^2$, we can then define the gravitational potential $g:\Re^2\rightarrow\Re$ as:$$\Huge\underline{f}=-\underline{\nabla}g$$
Let us consider a few examples:
> Let $M$ be a body of mass $M$ centered at the origin. The force due to gravity on a mass $m$ is then$$\Huge \underline{f}(r)=-\frac{GMm}{r^2}\underline{e}_r$$, where $r$ is a scalar representing the distance between the centers of mass $M,m$:$$\Huge r=||\underline{x}_M-\underline{x}_m||_{\Re^2}$$To find $g$, we assume it depends only on $r$ in the polar representation of $\Re^2$ with $(x,y)=(r\cos\theta,r\sin\theta)$ and write:$$\Huge\begin{align*}
-\frac{\partial g}{\partial r}&=\underline{f}_r=-\frac{GMm}{r^2}\\
-\frac{\partial g}{\partial \theta}&=\underline{f}_\theta=0\\
\implies g(r)&=GMm\int r^{-2}dr\\
&=-\frac{GMm}{r}+C\\
\implies V(r)&=\frac{g(r)}{m}=-\frac{GM}{r}
\end{align*}$$Because of the nature of scalar potentials, we set $C=0$ and proceed. 
> We aim to graph the equipotential lines due to a potential involving two bodies of mass $M_1,M_2$ respectively. We assume that mass $M_1$ is centered at $\underline{x}_{M_1}$ and that $M_2$ is centered at $\underline{x}_{M_2}$. Defining$$\Huge\begin{align*}
r_1(x,y)&=||\underline{x}_{M_1}-\underline{x}_m||_{\Re^2}\\
r_2(x,y)&=||\underline{x}_{M_2}-\underline{x}_m||_{\Re^2}
\end{align*}$$we can write the combined potential as:$$\Huge V_T(x,y)=-G\left(\frac{M_1}{r_1\left(x,y\right)}+\frac{M_2}{r_2(x,y)}\right)$$Equipotential curves are then found by setting $V_T(x,y)=C$ constant.

# Finding Lagrange points:

To find the Lagrange points of the Sun-Earth system, we must analyse the Circular Restricted Three Body Problem (CR3BP). First we define a coordinate system centered on the center of mass of the system with the $x$-axis pointing towards $m_E$, $y$-axis within the orbital plane, and $z$-axis perpendicular to the orbital plane. In this rotating reference frame, $m_E$ and $m_S$ will appear stationary.

In this frame, $m_E$ and $m_S$ will lie along the $x$-axis and so have $y,z$ coordinates of $0$. We find these $x$ positions using the fact we defined the center of mass to be at $x=0$:$$\Huge m_Ex_E+m_Sx_S=0$$We know the distance between the masses is $r^*=x_E-x_S\implies x_E=x_S+r^*$, so we solve these equations using the dimensionless ratios:$$\Huge \pi_E=\frac{m_E}{m_E+m_S},\,\,\pi_S=\frac{m_S}{m_E+m_S}$$Noting that $\pi_E+\pi_S=1$, we can solve for $x_E,x_S$:$$\Huge x_S=-\pi_Er^*,\,\,x_E=\pi_Sr^*$$

## Equations of motion:
We must now find the equations of motion for this system with an added mass $m$. Taking the position of this mass to be$$\Huge \underline{r}=x\underline{e}_x+y\underline{e}_y+z\underline{e}_z$$we find that the position of the mass relative to each body is:$$\Huge\begin{align*}
\underline{r}_S&=(x+\pi_Er^*)\underline{e}_x+y\underline{e}_y+z\underline{e}_z\\
\underline{r}_E&=(x-\pi_Sr^*)\underline{e}_x+y\underline{e}_y+z\underline{e}_z
\end{align*}$$The inertial angular velocity of our moving frame is given by$$\Huge \underline{\Omega}=\Omega\underline{e}_z,\,\,\Omega=\sqrt{\frac{G(m_E+m_S)}{{r^*}^3}}$$, since we are finding the inertial velocity of the mass we must add the rotation of the coordinate system:$$\Huge \underline{\dot r}=\underline{\Omega}\times\underline{r}+(\underline{v}_\text{COG}+\underline{v}_\text{rel})$$Here, $\underline{v}_\text{COG}$ is the absolute velocity of the center of mass, and $\underline{v}_\text{rel}$ is the velocity of the mass relative to the moving frame:$$\Huge \underline{v}_\text{rel}=\dot x\underline{e}_x+\dot y\underline{e}_y+\dot z\underline{e}_z$$
We must consider what the time derivative of this vector is in our moving frame:$$\Huge \underline{\dot v}_\text{rel}=\underline{a}_\text{rel}+\underline{\Omega}\times\underline{v}_\text{rel}$$Now we calculate:$$\Huge\begin{align*}
\underline{\ddot r}&=\underline{a}_\text{COG}+(\underline{a}_\text{rel}+\underline{\Omega}\times\underline{v}_\text{rel})+\underline{\dot\Omega}\times\underline{r}+\underline{\Omega}\times(\underline{v}_\text{rel}+\underline{\Omega}\times\underline{r})\\
&=\underline{a}_\text{COG}+\underline{a}_\text{rel}+\underline{\dot\Omega}\times\underline{r}+\underline{\Omega}\times(\underline{\Omega}\times\underline{r})+2\underline{\Omega}\times\underline{v}_\text{rel}
\end{align*}$$It can be shown that $\underline{a}_\text{COG}=\underline{0}$ (assuming our mass is incomparable to the other two), and since the angular velocity is constant for circular orbits, our equation reduces to:$$\Huge \underline{\ddot r}=\underline{\Omega}\times(\underline{\Omega}\times\underline{r})+2\underline{\Omega}\times\underline{v}_\text{rel}+\underline{a}_\text{rel}$$We can substitute our expressions for $\underline{r},\underline{v}_\text{rel}$, and $\underline{a}_\text{rel}$ to find:$$\Huge \underline{\ddot r}=(\ddot x-2\Omega \dot y-\Omega^2x)\underline{e}_x+(\ddot y+2\Omega\dot x-\Omega^2y)\underline{e}_y+\ddot z\underline{e}_z$$
Now we invoke Newton's second law,$$\Huge m\underline{\ddot r}=\underline{F}_E+\underline{F}_S$$where $\underline{F}_E,\underline{F}_S$ are the forces on the mass $m$ due to the Earth and the Sun respectively. Let us write these forces as:$$\Huge\begin{align*}
\underline{F}_E&=-G\frac{m_Em}{r_E^2}\underline{e}_r=-\frac{\mu_Em}{r_E^3}\underline{r}_E\\
\underline{F}_S&=-G\frac{m_Sm}{r_E^2}\underline{e}_r=-\frac{\mu_Sm}{r_S^3}\underline{r}_S
\end{align*}$$We therefore find the the equations of motion to be:$$\Huge\begin{align*}
\underline{\ddot r}&=-\frac{\mu_E}{r_E^3}\underline{r}_E-\frac{\mu_S}{r_S^3}\underline{r}_S\\
\implies\ddot x-2\Omega\dot y-\Omega^2x&=-\frac{\mu_E}{r_E^3}(x-\pi_Sr^*)-\frac{\mu_S}{r_S^3}(x+\pi_Er^*)\\
\implies\ddot y+2\Omega\dot x-\Omega^2y&=-\frac{\mu_E}{r_E^3}y-\frac{\mu_S}{r_S^3}\\
\implies\ddot z&=-\frac{\mu_E}{r_E^3}z-\frac{\mu_S}{r_S^3}z
\end{align*}$$
## Non-dimensionalisation:

Now let us non-dimensionalise these equations. We have units of mass, time, and length and so we use the definitions of $\pi_E,\pi_S$ and find:$$\Huge\begin{align*}
\underline{\rho}&=\frac{\underline{r}}{r^*}=x^*\underline{e}_x+y^*\underline{e}_y+z^*\underline{e}_z\\
\underline{\sigma}&=\frac{\underline{r}_S}{r^*}=(x^*+\pi_E)\underline{e}_x+y^*\underline{e}_y+z^*\underline{e}_z\\
\underline{\psi}&=\frac{\underline{r}_E}{r^*}=(x^*-1+\pi_E)\underline{e}_x+y^*\underline{e}_y+z^*\underline{e}_z
\end{align*}$$Where $x_i^*=x_i/r^*$. Now for time it is natural to use the period of the circular orbit, ignoring the factor of $2\pi$:$$\Huge t^*=\sqrt{\frac{r^*}{G(m_E+m_S)}}=\sqrt{\frac{r^*}{\mu}}$$
 