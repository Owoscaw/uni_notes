
# Parallel transport:

With all our machinery around the [[Covariant derivative|covariant derivative]], it is not clear what the covariant derivative is measuring change with respect to. It turns out that it measures the rate of change of tensors, the covariant derivative quantifies the instantaneous rate of change of a tensor field in comparison to what the tensor field would be if it were "parallel transported":![[Geodesics 2026-11-10 15.04.37.excalidraw]]In flat space, parallel transport is achieved simply by keeping its cartesian components constant. That is, a [[Covariant derivative#Christoffel connection|connection]] defines a specific way to keep a vector constant along some path. Based on this, we can compare nearby tensors.

This concept of moving a vector along a path while keeping it constant is known as parallel transport. For this, we require a connection to be well defined, the intuitive manipulation of vectors in flat space made implicit use of the Christoffel connection on this space. In curved space, the result of parallel transporting a vector between points will depend on the path taken:
> We can see this explicitly on a $2$-sphere. Starting with a vector on the equator pointing along a line of constant longitude, we parallel transport it to the north pole in an obvious way. Taking the original vector and parallel transporting along the equator by an angle $\theta$ and moving it to the north pole as before, we can see this difference:![[Geodesics 2026-11-10 15.22.10.excalidraw]]

There is no solution to this, we must live with the fact that two vectors can only be naturally compared if they are elements of the same tangent space. That is, two particles at different points on a curved manifold do not have a well defined notion of relative velocity. The inference of galaxies "receding" from redshift is nonsense, what actually happens is that the metric of spacetime between Earth and distance galaxies changed along the path of the photon.

Given a curve $x^\mu(\lambda)$, the constancy requirement of a tensor $T^{\mu_1\dots\mu_k}{}_{\nu_1\dots\nu_l}$ along this curve in flat space is simply that the components remain constant:$$\Large \frac{d}{d\lambda} T^{\mu_1\dots\mu_k}{}_{\nu_1\dots\nu_l}=\frac{dx^\mu}{d\lambda}\frac{\partial }{\partial x^\mu} T^{\mu_1\dots\mu_k}{}_{\nu_1\dots\nu_l}=0$$To make this properly tensorial, we replace this partial derivative with a covariant derivative and define the directional covariant derivative:$$\huge \frac{D}{d\lambda}=\frac{dx^\mu}{d\lambda}\nabla_\mu$$This is a map, defined along the path, from $[k,l]$ tensors to $[k,l]$ tensors. We can then define the parallel transport of the tensor $T$ along the path $x^\mu(\lambda)$ to be the requirement that the covariant derivative of $T$ along the path vanishes:$$\Large  \left(\frac{D}{d\lambda}T\right)^{\mu_1\dots\mu_k}{}_{\nu_1\dots\nu_l}=\frac{dx^\sigma}{d\lambda}\nabla_\sigma  T^{\mu_1\dots\mu_k}{}_{\nu_1\dots\nu_l}=0$$This is a well defined tensor equation, known as the equation of parallel transport. For a vector it takes form:$$\Large \frac{d}{d\lambda}V^\mu+\Gamma^\mu_{\sigma\rho}\frac{dx^\sigma}{d\lambda}V^\rho=0$$We can look at this as a first-order differential equation defining an IVP. Given a tensor at some point along the path, there is a unique combination of the tensor to other points along the path such that the continuation solves the parallel transport equation. We say such a tensor is parallel transported.

This is obviously dependent on the connection, for a metric compatible connection the metric is always parallel transported with respect to it:$$\Large \frac{D}{d\lambda}g_{\mu\nu}=\frac{dx^\sigma}{d\lambda}\nabla_\sigma g_{\mu\nu}=0$$It follows that the inner product of two parallel-transported vectors is preserved. That is, if $V^\mu,W^\nu$ are parallel transported along a curve $x^\sigma(\lambda)$, we have:$$\Large\begin{aligned}
\frac{D}{d\lambda}(g_{\mu\nu}V^\mu W^\nu)&=\left(\frac{D}{d\lambda}g_{\mu\nu}\right)V^\mu W^\nu+g_{\mu\nu}\left(\frac{D}{d\lambda}V^\mu\right)W^\nu+g_{\mu\nu}V^\mu\left(\frac{D}{d\lambda}W^\nu\right)\\
&=0
\end{aligned}$$That is, parallel transport wrt a metric compatible connection preserved the norm of vectors. 

## Geodesics:
With parallel transport well defined, the next logical step is to define [[year 3/differential geometry 3/term 2/Geodesics|geodesics]]. These are the curved space generalisation of Euclidean-space straight lines. A straight line is a path that parallel transports its own tangent vector, this will be the shortest path between two points if and only if the connection is the Christoffel connection. The tangent vector to a path $x^\mu(\lambda)$ is $\frac{dx^\mu}{d\lambda}$, so the parallel transport condition is$$\huge \frac{D}{d\lambda}\frac{dx^\mu}{d\lambda}=0$$, or equivalently:$$\Large \frac{d^2x^\mu}{d\lambda^2}+\Gamma^\mu_{\rho\sigma}\frac{dx^\rho}{d\lambda}\frac{dx^\sigma}{d\lambda}=0$$This is the geodesic equation. In Euclidean space, this recovers the equation for a straight line in cartesian coordinates ($\Gamma^\mu_{\rho\sigma}$). Let us turn to the nontrivial case of the shortest-distance definition:
> There are subtleties involved in the notion of distance on Lorentzian spacetime. For null paths the distance is zero, for timelike paths it is convenient to use proper time - and the resulting equation will be valid for any path.
> Therefore we consider the proper time functional$$\Large\tau=\int\left(-g_{\mu\nu}\frac{\partial x^\mu}{\partial \lambda}\frac{dx^\nu}{d\lambda}\right)^{1/2}d\lambda$$where the integral is taken over the path.
> To find shortest-distance paths, we use the [[Calculus of variations#Functionals|calculus of variations]] to find critical points of this functional. These will be curves of maximum proper time, consistent with the twin paradox. We can simplify the algebra by noticing the variation looks like:$$\Large\begin{aligned}
\delta\tau&=\int\delta\sqrt{-f}d\lambda\\
&=-\int\frac{1}{2}(-f)^{-1/2}\delta f\,d\lambda
\end{aligned}$$
> Taking $\tau$ to be our parameter rather than $\lambda$, the tangent vector is simply the four-velocity $U^\mu$. This fixes the value of $f$ and therefore allows us to calculate the variation:$$\Large\begin{aligned}
f&=g_{\mu\nu}\frac{dx^\mu}{d\tau}\frac{dx^\nu}{d\tau}\\
&=g_{\mu\nu}U^\mu U^\nu=-1\\
\implies\delta\tau&=-\frac{1}{2}\int\delta f\,d\tau
\end{aligned}$$
> Therefore stationary points of the functional $\tau$ are therefore equivalent to stationary points of the simpler integral:$$\Large I=\frac{1}{2}\int f\,d\tau=\frac{1}{2}\int g_{\mu\nu}\frac{dx^\mu}{d\tau}\frac{dx^\nu}{d\tau}d\tau$$Taking variations of this expression is a shortcut to finding shortest-distance paths. Now let us consider infinitesimal variations of the path:$$\Large\begin{aligned}
x^\mu&\to x^\mu+\delta x^\mu\\
g_{\mu\nu}&\to g_{\mu\nu}+(\partial_\sigma g_{\mu\nu})\delta x^\sigma
\end{aligned}$$The transformation of the metric here comes from the Taylor expansion in curved spacetime, which notably uses the partial derivative instead of the covariant one. This makes the variation in the integral:$$\Large\delta I=\frac{1}{2}\int d\tau\left(\partial_\sigma g_{\mu\nu}\frac{dx^\mu}{d\tau}\frac{dx^\nu}{d\tau}\delta x^\sigma+g_{\mu\nu}\frac{d(\delta x^\mu)}{d\tau}\frac{dx^\nu}{d\tau}+g_{\mu\nu}\frac{dx^\mu}{d\tau}\frac{d(\delta x^\nu)}{d\tau}\right)$$Taking $\delta x^\mu$ to vanish at the endpoints of the path, we neglect boundary terms and therefore integrate the last two terms by parts:$$\Large\begin{aligned}\frac{1}{2}\int g_{\mu\nu}\frac{dx^\mu}{d\tau}\frac{d(\delta x^\nu)}{d\tau}d\tau&=-\frac{1}{2}\int\delta x^\nu\left(g_{\mu\nu}\frac{d^2x^\mu}{d\tau^2}+\frac{dg_{\mu\nu}}{d\tau}\frac{dx^\mu}{d\tau}\right)d\tau\\
&=-\frac{1}{2}\int\delta x^\nu\left(g_{\mu\nu}\frac{d^2x^\mu}{d\tau^2}+\partial_\sigma g_{\mu\nu}\frac{dx^\sigma}{d\tau}\frac{dx^\mu}{d\tau}\right)d\tau\end{aligned}$$We can do the same for the other term, and rearrange some dummy indices to write:$$\Large\delta I=-\int\delta x^\sigma\left(g_{\mu\sigma}\frac{d^2x^\mu}{d\tau^2}+\frac{1}{2}\left(\partial_\mu g_{\nu\sigma}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu}\right)\frac{dx^\mu}{d\tau}\frac{dx^\nu}{d\tau}\right)d\tau$$
> We want this to vanish for any variation $\delta x^\sigma$, so let us multiply the bracketed term by the inverse metric $g^{\rho\sigma}$ and set it to $0$:$$\Large \frac{d^2x^\rho}{d\tau^2}+\frac{1}{2}g^{\rho\sigma}(\partial_\mu g_{\nu\sigma}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu})\frac{dx^\mu}{d\tau}\frac{dx^\nu}{d\tau}=0$$

We have arrived at exactly the geodesic equation with the specific connection choice of the Christoffel connection. Therefore extremals of the length functional are curves that parallel transport their tangent vector wrt the Christoffel connection associated with the metric on the manifold.

# Geodesic properties:

The primary use of geodesics in general relativity is that they are paths followed by unaccelerated test particles. That is, particles whose body does not influence the geometry around it. This allows us to explore gravitational fields around objects, without worrying about the field of the object whose motion we are following. The geodesic equation can therefore be thought of as the generalisation of Newton's Law. We can easily introduce forces by adding terms to the RHS:$$\Large \frac{d^2x^\mu}{d\tau^2}+\Gamma^\mu_{\rho\sigma}\frac{dx^\rho}{d\tau}\frac{dx^\sigma}{d\tau}=\frac{q}{m}F^\mu_\nu\frac{dx^\nu}{d\tau}$$

Our path is parametrised by $\lambda$, however we used a specific parametrisation of proper time to find our parallel transport formula. It is clear that this equation is invariant under transformations$$\Large\tau\to\lambda=a\tau+b$$for some constants $a,b$. Parameters related to proper time in this way are called affine parameters, and are all valid parametrisations. That is to say, the parallel transport condition implies the definition of the paths parameter upon its creation. 

More generally, equations of the form$$\Large \frac{d^2x^\mu}{d\alpha^2}+\Gamma^\mu_{\rho\sigma}\frac{dx^\rho}{d\alpha}\frac{dx^\sigma}{d\alpha}=f(\alpha)\frac{dx^\mu}{d\alpha}$$for some parameter $\alpha(\lambda)$, where $f(\alpha)$ is related to the affine parameter by:$$\Large f(\alpha)=-\left(\frac{d^2\alpha}{d\lambda^2}\right)\left(\frac{d\alpha}{d\lambda}\right)^{-2}$$The converse is also true, if the first equation is satisfied one can find an affine parameter $\lambda(\alpha)$ for which geodesic equation is satisfied.

> For timelike paths, the geodesic equation can be written in terms of four-velocity $U^\mu=\frac{dx^\mu}{d\tau}$ as$$\huge U^\lambda\nabla_\lambda U^\mu=0$$, and in terms of four-momentum $p^\mu=mU^\mu$:$$\huge p^\lambda\nabla_\lambda p^\mu=0$$
> For null paths, proper time vanishes and $\tau$ is not an appropriate affine parameter. It is still well-defined to ask if a parametrised path $x^\mu(\lambda)$ satisfies the geodesic equation. There is simply no preferred choice amongst affine parameters, however it is often convenient to choose the normalisation such that $p^\mu=\frac{dx^\mu}{d\lambda}$.

Note in timelike paths, $\frac{dx^\mu}{d\tau}$ is momentum per unit mass and so an observer with four-velocity $U^\mu$ measures the energy of particle to be:$$\huge E=-p_\mu U^\mu$$This works for both null and timelike paths for $p^\mu$. We call timelike/null/spacelike the character of the geodesic, which will not change relative to a (Lorentzian) [[Covariant derivative|metric compatable]] connection. This is because parallel transport preserves inner products, i.e. $V^\mu V_\mu$ is preserved. Spacelike paths will in general only have an overall minus sign in relevant equations.

As we can approximate any timelike path with a sequence of null ($0$ path length) paths, timelike curves cannot be minima of proper time (they are infinitesimally approximated by paths with smaller path length). This explains the [[False Paradoxes#Twin paradox|twin paradox]] nicely, as the twin who remains home travels on a geodesic and therefore ages more (maximises proper time). Note there can be more than one geodesic, i.e. great circles on $S^2$ and so we should say geodesics locally maximises proper time.

## Tangent spaces from geodesics:

A convenient way of mapping the tangent space $T_p$ of a point $p$ to a region of the manifold containing $p$ is through the exponential. This map defines a set of coordinates for this region that are automatically [[The metric tensor and Causality#Locally inertial coordinates|locally inertial]].

Noticing that any vector $k\in T_p$ defines a unique geodesic passing through it, for which $k$ is the tangent vector at $p$, and $\lambda(p)=0$:$$\Large \frac{dx^\mu}{d\lambda}(\lambda=0)=k^\mu$$Uniqueness comes from the fact that the geodesic equation is a second order differential equation, and initial data of form $x^\mu(p)$ and $k^\mu=(\frac{dx^\mu}{d\lambda})(p)$ completely determines a solution. On these geodesics, there will be a unique points $M$ for which $\lambda=1$. The exponential map at $p$, $\exp_p:T_p\to M$ is then defined as:$$\Large \exp_p(k)=x^\nu(\lambda=1)$$![[Geodesics 2026-11-12 21.51.06.excalidraw]]

For a set of tangent vectors $k^\mu$ near the $0$ vector, this map will be well-defined and even invertible. Depending on geometry, different geodesics starting at the same point may eventually cross. At such point(s), $\exp_p:T_p\to M$ is no longer one-to-one. The range of the map is not necessarily the whole manifold is not necessarily and the domain is not necessarily the whole tangent space. Manifolds that have any set of points that cannot be bridged with a geodesic are known as geodesically incomplete, singularities are often the cause.

We can use the exponential map to construct locally inertial coordinates first by finding basis vectors $\{\hat e_{(\hat\mu)}\}$ for $T_p$ such that the components of the metric are those of the canonical form:$$\Large g_{\hat\mu\hat\nu}=g(\hat e_{(\hat\mu)},\hat e_{(\hat\nu)})=\eta_{\hat\mu\hat\nu}$$ Here, $g(\cdot,\cdot)$ denotes the metric as a multilinear map from $T_p\times T_p\to\Re$ with $\hat e$ denoting basis vectors and $\hat\mu,\hat\nu$ denoting indices associated with locally inertial coordinates. We can always diagonalise any set of components for $g_{\mu\nu}$ and rescale the basis vectors to satisfy the above. It remains to find a coordinate system $x^{\hat\mu}$ for which the basis vectors $\{\hat e_{(\hat\mu)}\}$ comprise the coordinate basis $\hat e_{(\hat\mu)}=\partial_{\hat\mu}$ and such that the first partial derivatives of $g_{\hat\mu\hat\nu}$ vanish. The exponential map automatically achieves this:
> For any point $q$ sufficiently close to $p$, there is a unique geodesic path connecting $p$ to $q$, and a unique parametrisation $\lambda$ such that $\lambda(p)=0$ and $\lambda(q)=1$.
> At $p$, the tangent vector $k$ to this geodesic can be written as a linear combination of our basis vectors, $k=k^{\hat\mu}\hat e_{(\hat\mu)}$.
> We define the coordinates $x^{\hat\mu}$ simply to be these components:$$\Large x^{\hat\mu}(q)=k^{\hat\mu}$$That is, we have defined the coordinates wrt our normalised basis to be the components of the tangent vector $k$ that gets mapped to $q$ by $\exp_p$. Coordinates constructed this way are known as Riemann normal coordinates at $p$.

We must verify these coordinates satisfy:$$\huge\partial_{\hat\sigma}g_{\hat\mu\hat\nu}(p)=0$$Rays in the tangent space will e mapped to geodesics by the exponential map, so curves $x^{\hat\mu}(\lambda)$ (in Riemann normal coordinates) of the form$$\huge x^{\hat\mu}(\lambda)=\lambda k^{\hat\mu}$$will solve the geodesic equation. Any geodesic through $p$ can be expressed this way, for some appropriate vector $k^{\hat\mu}$. Therefore$$\huge \frac{d^2x^{\hat\mu}}{d\lambda^2}=0$$along any geodesic through $p$ in this coordinate system. By the geodesic equation we also have$$\Large \frac{d^2x^{\hat\mu}}{d\lambda^2}(p)=-\Gamma^{\hat\nu}_{\hat\rho\hat\sigma}(p)k^{\hat\rho}k^{\hat\sigma}$$where $k^{\hat\rho}=(\frac{dx^{\hat\rho}}{d\lambda})(p)$. Since this holds for any $k^{\hat\rho}$, we must have:$$\huge\Gamma^{\hat\mu}_{\hat\rho\hat\sigma}(p)=0$$This makes the metric compatibility condition$$\Large\begin{aligned}
0&=\nabla_{\hat\sigma}g_{\hat\mu\hat\nu}\\
&=\partial_{\hat\sigma}g_{\hat\mu\hat\nu}-\Gamma^{\hat\lambda}_{\hat\sigma\hat\mu}g_{\hat\lambda\hat\nu}-\Gamma^{\hat\lambda}_{\hat\sigma\hat\nu}g_{\hat\mu\hat\lambda}\\
&=\partial_{\hat\sigma}g_{\hat\mu\hat\nu}
\end{aligned}$$, where all quantities are evaluated at $p$. Note these locally inertial coordinates are not unique, there are infinitely many non-Riemann-normal coordinate systems in which $g_{\hat\mu\hat\nu}(p)=\eta_{\hat\mu\hat\nu}$ and $\partial_{\hat\sigma}g_{\hat\mu\hat\nu}(p)=0$, however they only differ from Riemann normal coordinates at third order in $x^{\hat\mu}$ when expanded around $p$.

# Revisiting [[The metric tensor and Causality#Expanding universes|expanding universes]]:

Recall the expanding universe metric:$$\Large\begin{aligned}
ds^2&=-dt^2+a^2(t)(dx^2+dy^2+dz^2)\\
&=-dt^2+a^2(t)\delta_{ij}dx^idx^j
\end{aligned}$$Describing a universe of flat spatial sections expanding as a function of time, with relative distance growing proportionally to a scale factor $a(t)$:
> Let us proceed by computing the Christoffel symbols, using the technique we found earlier. We have:$$\Large I=\frac{1}{2}\int\left(-\left(\frac{dt}{d\tau}\right)^2+a^2(t)\delta_{ij}\frac{dx^i}{d\tau}\frac{dx^j}{d\tau}\right)d\tau$$
> We consider variations $x^\mu\to x^\mu+\delta x^\mu$ and demand $\delta I$ vanish, giving $n$ equations on an $n$-dimensional manifold ($n=4$). In our variation, the coefficient of $(\frac{dx^\rho}{d\tau})(\frac{dx^\sigma}{d\tau})$ will be $\Gamma^\mu_{\rho\sigma}$.
> In the metric we must consider separate variations wrt $x^0=t$ and one $x^i$ (sufficient due to equivalence).
> Starting with $t\to t+\delta t$, the nontrivial time dependence comes from the scale factor,$$\Large a(t+\delta t)=a(t)+\frac{da}{dt}\delta t=a(t)+\dot a\delta t$$and so $\delta I$ takes form:$$\Large\begin{aligned}
\delta I&=\frac{1}{2}\int\left(-2\frac{dt}{d\tau}\frac{d(\delta t)}{d\tau}+2a\dot a\delta_{ij}\frac{dx^i}{d\tau}\frac{dx^j}{d\tau}\right)d\tau\\
&=\int\left(\frac{d^2t}{d\tau^2}+a\dot a\delta_{ij}\frac{dx^i}{d\tau}\frac{dx^j}{d\tau}\right)\delta t\,d\tau
\end{aligned}$$
> Requiring this to vanish implies$$\Large\frac{d^2t}{d\tau^2}+a\dot a\delta_{ij}\frac{dx^i}{d\tau}\frac{dx^j}{d\tau}=0$$which is equivalent to the geodesic equation with $\mu=0$:$$\Large\begin{aligned}
	\frac{d^2x^0}{d\tau^2}+\Gamma^0_{\rho\sigma}\frac{dx^\rho}{d\tau}\frac{dx^\sigma}{d\tau}&=0\\
\implies\Gamma^0_{00}&=0\\
\Gamma^0_{i0}=\Gamma^0_{0i}&=0\\
\Gamma^0_{ij}&=a\dot a\delta_{ij}
\end{aligned}$$
> Repeating this for a spatial coordinate $x^i\to x^i+\delta x^i$, the variation is:$$\Large\begin{aligned}
\delta I&=\frac{1}{2}\int a^2\left(2\delta_{ij}\frac{dx^i}{d\tau}\frac{d\delta x^j}{d\tau}\right)d\tau\\
_\text{IBP}&=-\int\left(a^2\frac{d^2x^i}{d\tau^2}+2a\frac{da}{d\tau}\frac{dx^i}{d\tau}\right)\delta_{ij}\delta x^jd\tau
\end{aligned}$$Expressing $\frac{da}{d\tau}$ in terms of $\dot a$ using the chain rule $\frac{da}{d\tau}=\dot a\frac{dt}{d\tau}$ and setting the coefficient of $\delta x^j$ to $0$ implies the geodesic equation:$$\Large \frac{d^2x^i}{d\tau^2}+2\frac{\dot a}{a}\frac{dt}{d\tau}\frac{dx^i}{d\tau}=0$$
> Comparing to the geodesic equation, the Christoffel symbols must satisfy$$\Large \Gamma^i_{\rho\sigma}\frac{dx^\rho}{d\tau}\frac{dx^\sigma}{d\tau}=2\frac{\dot a}{a}\frac{dt}{d\tau}\frac{dx^i}{d\tau}$$, so we can see:$$\Large\begin{aligned}
\Gamma^i_{00}&=0\\
\Gamma^i_{j0}=\Gamma^i_{0j}&=\frac{\dot a}{a}\delta^i_j\\
\Gamma^i_{jk}&=0
\end{aligned}$$
> These together with the symbols associated with the temporal translation are all the connection coefficient for the metric.

## Cosmological redshift:

These are necessary for studying the geodesics of the spacetime and for taking covariant derivatives. Let us therefore solve for the null geodesics, which massless particles like photons will follow. In this case we use $\lambda$ as a parameter instead of $\tau$. WLOG we consider paths in the $x$-direction:$$\Large x^\mu(\lambda)=(t(\lambda),x(\lambda),0,0)$$Using $ds^2=0$, we have:$$\Large\begin{aligned}
0&=-dt^2+a^2(t)dx^2\\
\implies \frac{dx}{d\lambda}&=\frac{1}{a}\frac{dt}{d\lambda}
\end{aligned}$$

To show these paths are geodesics, we must solve for coordinates $t,x$ in terms of the parameter $\lambda$. We begin by solving $dt/d\lambda$, using $\mu=0$ component of the geodesic equation (replacing $\tau\to\lambda$):$$\Large \frac{d^2t}{d\lambda^2}+\frac{\dot a}{a}\left(\frac{dt}{d\lambda}\right)^2=0$$This is solved by$$\huge \frac{dt}{d\lambda}=\frac{\omega_0}{a}$$, where $\omega_0$ is a constant. For a given form of $a$, this can be integrated to find $t(\lambda)$. I

It is more interesting to look at the energy $E$ of the photon, measured by a comoving observer with four-velocity $U^\mu=(1,0,0,0)$. Using $p^\mu=dx^\mu/d\lambda$, we have$$\Large\begin{aligned}
E&=-p_\mu U^\mu\\
&=-g_{00}\frac{dx^0}{d\lambda}U^0\\
&=\frac{\omega_0}{a}
\end{aligned}$$, showing that the energy is simply the frequency $\omega_0$ of the photon $(\hbar=1)$ when $a=1$. This is a cosmological redshift.

Photons emitted with energy $E_1$ at a scale factor $a_1$ and observed with energy $E_2$ at a scale factor $a_2$ we have:$$\huge\frac{E_2}{E_1}=\frac{a_1}{a_2}$$This provides an easy way to measure change in scale factor between us and distance galaxies, and can serve as a proxy for the distance.

## [[SR, Manifolds, and Field theory summary#Energy-Momentum tensor|Energy-momentum tensor]]:
We model the matter filling the universe as a perfect fluid with energy-momentum tensor coming from the generalisation$$\Large T^{\mu\nu}=(\rho+p)U^\mu U^\nu+pg^{\mu\nu}$$, where $\rho$ is energy density, $p$ is pressure, and $U^\mu$ is the fluid's four-velocity. The energy-momentum conservation equation becomes:$$\huge \nabla_\mu T^{\mu\nu}=0$$
The components of the inverse (expanding universe) metric are:$$\Large g^{\mu\nu}=\begin{pmatrix}-1 & 0 & 0 & 0 \\ 0 & a^{-2} & 0 & 0 \\ 0 & 0 & a^{-2} & 0 \\ 0 & 0 & 0 & a^{-2}\end{pmatrix}$$We take the fluid to be in its rest frame in these coordinates, so that components of four-velocity are $U^\mu=(1,0,0,0)$. Therefore the energy-momentum tensor takes form:$$\Large\begin{aligned}
T^{\mu\nu}&=(\rho+p)\begin{pmatrix}1 & 0 & 0 & 0\end{pmatrix}^\mu\begin{pmatrix}1 \\ 0 \\ 0 \\ 0\end{pmatrix}^\nu+pg^{\mu\nu}\\
&=(\rho+p)\mathbb{I}^{\mu\nu}+pg^{\mu\nu}\\
&=\begin{pmatrix}\rho & 0 & 0 & 0\\
 0 & a^{-2}p & 0 & 0\\
0 & 0 & a^{-2}p & 0\\
0 & 0 & 0 & a^{-2}p\end{pmatrix}
\end{aligned}$$
Let us look at what energy-momentum conservation implies for a perfect fluid in an expanding universe. Taking the covariant derivative implies:$$\Large \nabla_\mu T^{\mu\nu}=\partial_\mu T^{\mu\nu}+\Gamma^\mu_{\mu\rho}T^{\rho\nu}+\Gamma^\nu_{\mu\rho}T^{\mu\rho}=0$$This has $4$ components, however each $\mu=i\in\{1,2,3\}$ are equivalent so we look at $\nu=0$ component. We compute each term:$$\Large\begin{aligned}
\partial_\mu T^{\mu0}&=\partial_0T^{00}=\dot\rho\\
\Gamma^\mu_{\mu\rho}T^{\rho0}&=\Gamma^\mu_{\mu0}T^{00}=3\frac{\dot a}{a}\rho\\
\Gamma^0_{\mu\rho}T^{\mu\rho}&=\Gamma^0_{00}T^{00}+\Gamma^0_{11}T^{11}+\Gamma^0_{22}T^{22}+\Gamma^0_{33}T^{33}\\
&=3\frac{\dot a}{a}p
\end{aligned}$$Where we used the diagonality of $T^{\mu\nu}$, the explicitly form of our energy-momentum tensor, and the connection coefficients we previously calculated. Therefore the equation states:$$\Large\dot\rho=-3\frac{\dot a}{a}(\rho+p)$$
Looking at a spatial component $\nu=1$ we work term by term again:$$\Large\begin{aligned}
\partial_\mu T^{\mu1}&=\partial_1 T^{11}=a^{-2}\partial_xp\\
\Gamma^\mu_{\mu\rho}T^{\rho1}&=\Gamma^\mu_{\mu1}T^{11}=0\\
\Gamma^1_{\mu\rho}T^{\mu\rho}&=\Gamma^1_{00}T^{00}+\Gamma^1_{11}T^{11}+\Gamma^1_{22}T^{22}+\Gamma^1_{33}T_{33}=0\\
\implies\partial_ip&=0
\end{aligned}$$
These tell us how a lot of laws applied to classical physical change in an expanding flat spacetime.

# The Riemann curvature tensor:

We are now prepared to discuss curvature in a meaningful way, quantified by the Riemann curvature tensor which is derived from the connection. The notion of curvature comes from how we differ from the "flat" metric. These "flat" metrics have a number of properties that we take as manifestations of "flatness":
> Parallel transportation around closed loops leaves a vector unchanged.
> Covariant derivatives of tensors commute.
> Initially, parallel geodesics remain parallel.

The Riemann tensor arises when we study these properties in more general contexts. We saw that parallel transport around a closed loop on curved space introduces some transf