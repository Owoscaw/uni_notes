
Let us look for the simplest solutions in [[Einstein's theory#Equations of Motion for gravity|Einstein's theory]] with the absence of matter fields. In this case, we have to look for "[[Curvature#Ricci tensor|Ricci]] flat" spacetimes:$$\Large R_{\mu\nu}=0$$More specifically, we look for spherically symmetric solutions. One such spacetime is Minkowski spacetime, which we write in polar coordinates as$$\Large\begin{aligned}
ds^2&=-dt^2+dx^2+dy^2+dz^2\\
&=-dt^2+dr^2+r^2(d\theta^2+\sin^2\theta d\varphi)\\
_{\text{introducing }d\Omega_2}&=-dt^2+dr^2+r^2d\Omega_2^2
\end{aligned}$$, noting that $d\Omega_2^2$ is invariant under $\Re^3$ Euclidean rotations. 

# The Schwarzschild solution:

In order to find more general spherically symmetric solutions, we keep the $d\Omega_2^2$ part of the metric and aim to generalise the other terms with the following:$$\Large ds^2=\gamma_{tt}(t,r)dt^2+2\gamma_{tr}(t,r)dt\,dr+\gamma_{rr}(t,r)dr^2+\gamma_{\Omega\Omega}(t,r)d\Omega_2^2$$This is the most general metric we can write which preserves spherical symmetry. We can do better than this by exploiting coordinate transformations of the form:$$\Large t\to t(t',r'),\,\,r\to r(t',r')$$This allows us to set $\gamma_{tr}=0$ and $\gamma_{\Omega\Omega}=r^2$. Therefore we can write the metric as$$\Large ds^2=-e^{2\alpha(t,r)}dt^2+e^{2\beta(t,r)}dr^2+r^2d\Omega_2^2$$, and the task reduces to finding functions $\alpha,\beta$ that solve $R_{\mu\nu}=0$. 

The nontrivial components of the Ricci tensor are:$$\Large\begin{aligned}
R_{00}&=\ddot\beta+\dot\beta^2-\dot\alpha\dot\beta +e^{2(\alpha-\beta)}\left(\alpha''+\alpha'^2-\alpha'\beta'+\frac{2}{r}\alpha'\right)\\
R_{11}&=-\alpha''+\alpha'^2-\alpha'\beta'-\frac{2}{r}\alpha'+e^{2(\beta-\alpha)}(\ddot\beta+\dot\beta^2-\dot\alpha\dot\beta)\\
R_{01}&=\frac{2}{r}\dot\beta\\
R_{22}&=e^{-2\beta}(r(\beta'-\alpha')-1)+1\\
R_{33}&=\sin^2\theta R_{22}
\end{aligned}$$Where we use $\dot f$ to represent time derivatives and $f'$ to represent $r$ derivatives. Now let us examine what Einstein's equations imply for our functions$$\Large\begin{aligned} R_{01}&=0\implies\dot\beta(t,r)=0\implies\beta=\beta(r)\\
\partial_t R_{22}&=0\implies\partial_t\partial_r\alpha(t,r)=0\implies\alpha(t,r)=f(r)+g(t)
\end{aligned}$$, that is $\beta$ must be a function of only $r$ and $\alpha$ must be a sum of functions dependent on each coordinate. Looking back at our ansatz for the metric form, we see that we can absorb $g(t)$ in a time redefinition:$$\Large d\tilde t=e^{g(t)}dt=d\left(\int dt\,e^{g(t)}\right)$$We can therefore set $g(t)=0$ WLOG. Now let us examine the linear combination$$\Large e^{2(\beta-\alpha)}R_{00}+R_{11}=\frac{2}{r}(\alpha'+\beta')=0\implies\alpha(r)=-\beta(r)+c$$, with $c$ a constant that we set to $0$ via a transformation in time. It remains to solve the $R_{22}$ component, so let us proceed:$$\Large R_{22}=0\implies e^{2\alpha}(2r\alpha'+1)=1\implies e^{2\alpha}=1+\frac{\mu}{r}$$Here, $\mu$ is a constant of integration for this ODE. We can therefore write the final form of the metric:$$\Large ds^2=-\left(1+\frac{\mu}{r}\right)dt^2+\left(1+\frac{\mu}{r}\right)^{-1}dr^2+r^2 d\Omega_2^2$$
This is rather profound, we only assumed spherical symmetry and Einstein's equations ended up constraining $\alpha,\beta$ to be time-independent. This is also known as Birkhoff's theorem, any time dependence is artificial and comes from time dependent coordinate transformations. 

Taking the $r\to\infty$ limit, we see that the metric approaches that of Minkowski spacetime in spherical coordinates. The effect of the curved spacetime becomes weak at infinity, so it makes sense to look at the deviation of $g_{00}$ from Minkowski spacetime and treat it as a gravitational potential, consistent with the [[Einstein's theory#year 4/Project/Geodesics Newtonian limit Newtonian limit revisited|Newtonian limit]]:$$\Large g_{00}\approx -1-2\Phi\implies\Phi=\frac{\mu}{2r}$$It is then natural to interpret our metric solution as the spacetime created by a point-like object of mass $M$ sitting at the spacetime origin. This suggests the identification $$\Large \mu=-2 G_NM$$, and so we find the Schwarzschild black hole solution:$$\Large ds^2=-\left(1-\frac{2G_NM}{r}\right)dt^2+\left(1-\frac{2G_NM}{r}\right)^{-1}dr^2+r^2d\Omega_2^2$$
# Motion around a black hole:

Let us now examine the motion of a free particle moving inside the Schwarzschild black hole background metric. We do this via the [[year 4/Project/Geodesics#Geodesics|geodesic equation]] in its affine parametrisation with $\alpha=0$. Equivalently, we can study the action for the free particle that yields the geodesic equation upon variation:$$\Large L'[x^\mu]=\int d\tau\,g_{\mu\nu}(x^\lambda(\tau))V^\mu(\tau)V^\nu(\tau)$$With our background metric above, this becomes$$\Large L'=\int d\tau(-(f(r(\tau))\dot t^2(\tau)+f^{-1}(r(\tau))\dot r^2\theta(\tau)+r^2(\tau)(\dot\theta^2(\tau)+\sin^2\theta(\tau)\dot\phi^2(\tau))))$$where we write $f(r)=1-\frac{2M}{r}$. This yields the equations of motion:$$\Large\begin{aligned}
\frac{d}{d\tau}\left(\left(1-\frac{2M}{r}\right)\dot t\right)&=0\\
\frac{d}{d\tau}(r^2\sin^2\theta\,\phi)&=0\\
-\frac{d}{d\tau}(r^2\dot\theta)+r^2\sin\theta\cos\theta\,\dot\phi^2&=0\\
2\frac{d}{d\tau}\left(-\left(1-\frac{2M}{r}\right)^{-1}\dot r\right)-\frac{2M}{r^2}\dot t^2-\left(1-\frac{2M}{r}\right)\frac{2M}{r^2}\dot r^2+2r(\dot\theta^2+\sin^2\theta\,\dot\phi^2)&=0
\end{aligned}$$Our Schwarzschild spacetime had time symmetry as well as spatial rotation symmetry and so we have the following [[Curvature#Killing vectors|Killing vectors]]:$$\Large\begin{aligned}
T_{(t)}&=\partial_t\\
L_{(1)}&=\partial_\phi\\
L_{(2)}&=-\cos\phi\partial_\theta+\sin\phi\cot\theta\partial_\phi\\
L_{(3)}&=\sin\phi\partial_\theta+\cos\phi\cot\theta\partial_\phi
\end{aligned}$$Each of these admits a conserved quantity, which we calculate:$$\Large\begin{aligned}
E&=-(T_{(t)})_\mu\dot x^\mu=\left(1-\frac{2M}{r}\right)\dot t\\
L&=(L_{(1)})_\mu\dot x^\mu=r^2\sin^2\theta\dot\phi\\
L_x&=(L_{(2)})_\mu\dot x^\mu=-\cos\phi\dot\theta r^2+\cos\phi\cot\theta L\\
L_y&=(L_{(3)})_\mu\dot x^\mu=\sin\phi\dot\theta r^2+\sin\phi\cot\theta L
\end{aligned}$$The first quantity here is the energy of the particle, which is conserved due to time translation symmetry. The last three conserved quantities form the angular momentum vector, which is conserved in both magnitude and direction.

Depending on initial conditions, we can choose the angular momentum vector to lie along the $z$-axis WLOG. To do this, we must work in a frame where $\dot\theta=0,\theta=\phi/2$, which gives $L_x=L_y=0$ initially. Conservation of these quantities then implies these are $0$ for all time, and therefore $\dot\theta,\theta$ will not change their values.

These conservation laws are essentially solving the first three equations of motion. It remains to solve the equation associated with varying the action wrt the radial coordinate. This will not be necessary, as we can find another "conservation law" related to the choice of affine parameter. In the affine parametrisation, the norm of the tangent vector along geodesics remains constant:$$\Large\begin{aligned}
-\left(1-\frac{2M}{r}\right)\dot t^2+\left(1-\frac{2M}{r}\right)^{-1}\dot r^2+r^2(\dot\theta^2+\sin^2\theta\,\dot\phi^2)&=-\epsilon\\
_{\text{substituting conserved quantities}}\implies\left(1-\frac{2M}{r}\right)^{-1}(-E^2+\dot r^2)+\frac{L^2}{r^2}&=-\epsilon
\end{aligned}$$Defining an effective potential, we can write:$$\Large\begin{aligned}
\frac{1}{2}E^2&=\frac{1}{2}\dot r^2+V_\text{eff}(r)\\
_\text{where }V_\text{eff}(r)&=\frac{1}{2}\epsilon-\epsilon\frac{M}{r}+\frac{L^2}{2r^2}-\frac{ML^2}{r^3}
\end{aligned}$$Note the leading terms in the $r\to\infty$ limit are identical to that of a particle moving around an object of mass $M$:$$\Large V_\text{eff}(r)\approx\frac{1}{2}\epsilon-\epsilon\frac{M}{r}+\frac{L^2}{2r^2}$$The contribution from general relativity essentially boils down to the extra term that goes like $1/r^3$ and will become dominant at small distances. We have some remarks to make about this potential:
> $V_\text{eff}$ is bounded from above.
> Massless, light-like particles with $\epsilon=0$ admit a circular orbit at $r=r_0$:$$\Large\begin{aligned}
V_\text{eff}'(r_0)&=0\implies-\frac{L^2}{r_0^3}+\frac{3ML^2}{r_0^4}=0\implies r_0=3M\\
V_\text{eff}''(r_0)&=-\frac{L^2}{M^43^4}<0
\end{aligned}$$So we see that this is an unstable orbit.
> Massive particles with $\epsilon=1$ admit two circular orbits at $r=r_\pm$ with:$$\Large\begin{aligned}
V_\text{eff}'(r_\pm)&=0\implies\frac{M}{r_\pm^2}-\frac{L^3}{r_\pm^3}+\frac{3ML^2}{r_\pm^4}=0\\
\implies r_\pm&=\frac{1}{2M}(L^2\pm\sqrt{L^4-12M^2L^2})
\end{aligned}$$This is different to the non-relativistic motion of particles, however upon checking the second derivative we see only $r=r_+$ is stable.


## Ray of light:
Now let us examine the spherical region at $r=2M$, where the coordinate system we chose to construct the Schwarzschild solution is singular:$$\Large\begin{aligned}
\frac{1}{2}E^2&=\frac{1}{2}\left(\frac{dr}{d\tau}\right)^2+\frac{L^2}{2(2M)^2}-\frac{ML^2}{(2M)^3}\\
\implies \frac{dr}{d\tau}&=-E_{\text{ admits a solution past }r=2M}\\
\implies \frac{dr}{dt}\frac{dt}{d\tau}&=-E\\
_\text{using conservation laws }\frac{dr}{dt}\dot t&=-\left(1-\frac{2M}{r}\right)\dot t \\
\implies \frac{dr}{dt}&=-\left(1-\frac{2M}{r}\right)
\end{aligned}$$We will see this is precisely the point where the event horizon of our black hole is. We will find this point by considering a ray of light ($\epsilon=0$ in effective potential equation) falling radially towards the center of the black hole. For this motion, there is no angular momentum ($\dot\phi=0$).

We saw by considering the affine parametrisation, we could consider a solution dictated by the above ($r=r_0-R\tau$). This equation dictates that after enough proper time $\tau$ has passed, the light ray will pass through $r=2M$ without any blow-up. However in the $t$ parametrisation, the equations dictate that the light ray slows down as it approaches the horizon infinitely and we never see it cross. Observers sitting on the outside will never be able to send information inside the event horizon.