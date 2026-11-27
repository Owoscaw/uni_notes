
Let us look for the simplest solutions in [[Einstein's theory#Equations of Motion for gravity|Einstein's theory]] with the absence of matter fields. In this case, we have to look for "[[Curvature#Ricci tensor|Ricci]] flat" spacetimes:$$\Large R_{\mu\nu}=0$$More specifically, we look for spherically symmetric solutions. One such spacetime is Minkowski spacetime, which we write in polar coordinates as$$\Large\begin{aligned}
ds^2&=-dt^2+dx^2+dy^2+dz^2\\
&=-dt^2+dr^2+r^2(d\theta^2+\sin^2\theta d\varphi)\\
_{\text{introducing }d\Omega_2}&=-dt^2+dr^2+r^2d\Omega_2^2
\end{aligned}$$, noting that $d\Omega_2^2$ is invariant under $\Re^3$ Euclidean rotations. 

# The Schwarzschild solution:

In order to find more general spherically symmetric solutions, we keep the $d\Omega_2^2$ part of the metric and aim to generalise the other terms with the following:$$\Large ds^2=\gamma_{tt}(t,r)dt^2+2\gamma_{tr}(t,r)dt\,dr+\gamma_{rr}(t,r)dr^2+\gamma_{\Omega\Omega}(t,r)d\Omega_2^2$$This is the most general metric we can write which preserves spherical symmetry. We can do better than this by exploiting coordinate transformations of the form:$$\Large t\to t(t',r'),\,\,r\to t(t',r')$$This allows us to set $\gamma_{tr}=0$ and $\gamma_{\Omega\Omega}=r^2$. Therefore we can write the metric as$$\Large ds^2=-e^{2\alpha(t,r)}dt^2+e^{2\beta(t,r)}dr^2+r^2d\Omega_2^2$$, and the task reduces to finding functions $\alpha,\beta$ that solve $R_{\mu\nu}=0$. 

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

