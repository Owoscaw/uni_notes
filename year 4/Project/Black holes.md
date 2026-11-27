
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
\end{aligned}$$, that is $\beta$ must be a function of only $r$ and $\alpha$ must be a sum of functions dependent on each coordinate. Looking back at our ansatz for the metric form, we see that we can absorb $g(t)$ in a time redefinition:$$\Large d\tilde t=e^{g(t)}dt=d\left(\int dt\,e^{g(t)}\right)$$ 