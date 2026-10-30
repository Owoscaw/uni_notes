
# Metrics:

The [[SR, Manifolds, and Field theory summary#Tensors on manifolds|metric tensor]] is an integral object in curved space, we write it as $g_{\mu\nu}$ and will now discuss restrictions on its components. We take this metric to be symmetric, rank $(2,0)$, and nondegenerate - allowing for the definition of its inverse:$$\huge g^{\mu\nu}g_{\nu\sigma}=g_{\lambda\sigma}g^{\lambda\mu}=\delta^\mu_\sigma$$Note this is different to the [[Metrics|topological]] notion of a metric, and we cannot use this definition to create a topology. We will put this lil guy through the ringer:
> The metric implies a past and a future
> The metric allows path lengths and proper time to be computed
> The metric is [[Geodesics#Fundamental properties of geodesics|geodesic]]
> The metric replaces the [[Gravitational potential|Newtonian gravitational field]] $\phi$
> The metric provides a notion of locally inertial reference frames
> The metric defines causality
> The metric replaces the "dot product"

We often write our infinitesimal line element $ds$ in terms of the metric:
$$\Huge ds^2=g_{\mu\nu}dx^\mu dx^\nu$$From this we can easily write the following expressions for the inner product of vectors $V^\mu,W^\nu$:$$\huge g_{\mu\nu}V^\mu W^\nu=g(V,W)=ds^2(V,W)$$We will see that the metric tensor contains all information needed to describe the curvature of a manifold. In Minkowski space we choose coordinates in which the components of the metric are constant, however let me emphasise that curvature is independent of coordinate embedding. Note that the constancy of metric components is sufficient for a space to be called flat, however there are many ways to deviate from a flat surface - some of which may be hard to find a coordinate system to embed the manifold. In canonical form we write:$$\Large g_{\mu\nu}=\text{diag}(-1,\dots,-1,+1,\dots,+1,0,\dots,0)$$This is clearly non-degenerate, we will always deal with non-degenerate continuous metrics:
> If all signs are positive, the metric is Riemannian
> If there is a single minus, the metric is Lorentzian
> Other metrics are called indefinite

We are interested in Lorentzian metrics.

## Locally inertial coordinates:
It is always possible to write the metric in canonical form at a point $p\in\mathbf{M}$, however this is only possible at the point. That is, we cannot write a canonical form for the metric in a neighbourhood of $p$. At any point $p$ we have a coordinate system $x^{\hat\mu}$ in which $g_{\hat\mu\hat\nu}$ takes its canonical form and all first derivatives $\partial_{\hat\sigma}g_{\hat\mu\hat\nu}$ all vanish (not applicable to second derivatives):$$\huge g_{\hat\mu\hat\nu}(p)=\eta_{\hat\mu\hat\nu},\,\,\partial_{\hat\sigma}g_{\hat\mu\hat\nu}(p)=0$$Such coordinates are called locally inertial, and the associated basis vectors form the local Lorentz frame. Due to the vanishing of first derivatives, the metric at $p$ in locally inertial coordinates looks like flat space (this is the formal notion of "flat enough"). One can construct such basis vectors by looking at the metric's transformation law and Taylor expanding.

These coordinates are very useful, and best of all we do not have to construct them. We will take physically interesting questions, answer them in locally inertial coordinates, and write an answer in coordinate-independent form. Take for example:
> Consider an observer with four-velocity $U^{\hat\mu}$ passed by a rocket with four-velocity $V^{\hat\mu}$.
> Working such that the observer is our rest frame and the rocket moves along the $x$ axis, we can write the four-velocities as$$\Large U^{\hat\mu}=(1,0,0,0),\,\,V^{\hat\mu}=(\gamma,v\gamma,0,0)$$, where $v$ is three-velocity and $\gamma$ is the Lorentz factor.
> In flat spacetime,$$\Large\gamma=-\eta_{\hat\mu\hat\nu}U^{\hat\mu}V^{\hat\nu}=-U_{\hat\mu}V^{\hat\mu}$$, so we can solve for three-velocity:$$\huge v=\sqrt{1-(U_{\hat\mu}V^{\hat\mu})^{-2}}$$
> Returning to curved spacetime, we are free to use locally inertial coordinates. In this case $g_{\hat\mu\hat\nu}$ matches $\eta_{\hat\mu\hat\nu}$ and so this answer is still valid in curved spacetime (for this coordinate system). Note that this equation is completely tensorial and is therefore coordinate independent.

## Expanding universes:
A simple example of a nontrivial Lorentzian geometry is given by a four-dimensional spacetime with metric$$\Large ds^2=-dt^2+a^2(t)(dx^2+dy^2+dz^2)$$, describing a universe for which space at a fixed moment in time is a flat three dimensional Euclidean space expanding as a function of time. We call worldlines (and therefore volumes) that remain at constant spatial coordinates $x^i$ (or spaces whose boundaries expand with volume) co-moving. The form of this metric suggests the distance between points grows with $a(t)$, which we call the scale factor.

Typically, solutions for the scale factor are power laws, $a(t)=t^q$ for $0<q<1$. In our case, $t=0$ represents a true singularity of the geometry (the Big Bang) which we exclude from the manifold. We can draw a spacetime diagram by considering null paths ($ds^2=0$) for which we hold $y,z$ constant:$$\Large\begin{aligned}
0&=-dt^2+t^{2q}dx^2\\
\implies \frac{dx}{dt}&=\pm t^{-q}
\end{aligned}$$Note that we don't just "divide by $dt^2$" here, instead we act on the $(0,2)$ tensor in the first line with two copies of $V=\left(\frac{dx^\mu}{d\lambda}\right)\partial_\mu$. Consider acting on $V$ with $dt^2$ only:$$\Large\begin{aligned}
dt^2(V,V)&=(dt\otimes dt)(V,V)=dt(V)\cdot dt(V)\\
dt(V)&=dt\left(\frac{dx^\mu}{d\lambda}\partial_\mu\right)\\
&=\frac{dx^\mu}{d\lambda}dt(\partial_\mu)\\
&=\frac{dx^\mu}{d\lambda}\frac{\partial t}{\partial x^\mu}=\frac{dt}{d\lambda}\\
_{\text{same with }dx^2}\implies dx(V)&=\frac{dx}{d\lambda}\\
\implies0&=-\left(\frac{dt}{d\lambda}\right)^2+t^{2q}\left(\frac{dx}{d\lambda}\right)^2
\end{aligned}$$Our equation for $\frac{dx}{dt}$ is then a direct implication of the chain rule. What we take from this is that we can manipulate basis one-forms as if they were differentials. Solving our equation in terms of $t$ gives$$\Large t=(1-q)^{\frac{1}{1-q}}(\pm x-x_0)^{\frac{1}{1-q}}$$, where $x_0$ is a constant of integration. These curves define light cones in this universe:![[The metric tensor and Causality 2026-10-30 01.26.39.excalidraw]]Note the assumption that $0<q<1$ implies the light cones are tangent to the singularity at $t=0$. A feature of this geometry is that the light cones of two point need not intersect in the past, unlike Minkowski space. We say every event defines some horizon outside of which worldlines have no influence on the event. That is, events can only be influenced by events either on or inside of it's past light cone.

# Causality:

The fact that we can solve initial value problems is due to causality, the idea that future events can be understood as consequences of initial conditions in addition to the laws of physics. We look at the problem of evolving matter fields on a fixed background spacetime, rather than the evolution of the metric. Our guiding principle is that information can only flow along null or timelike curves (which are not necessarily geodesic):
> We define a causal curve to be one that is null or timelike everywhere
> Given a subset $S\subset M$ of a manifold $M$, we define the causal future of $S$ (denoted $J^+(S)$) to be the set of points that can be reached from $S$ by following a future-directed causal curve.
> The chronological future $I^+(S)$ is then the set of points that can be reached from $S$ by following a future-directed timelike curve. 

Note that a curve of length $0$ is causal but not chronal, i.e. a point $p$ will always be in its own $J^+(p)$ but not necessarily $I^+(p)$. Causal/Chronological past are defined similarly.

A subset $S\subset M$ is called achronal if no two points in $S$ are connected by timelike curve. Given a closed achronal set $S$, we define the future dependence of $S$, $D^+(S)$, as the set of points such that every past-moving inextendible causal curve through the point must intersect $S$. Note that elements of $S$ are themselves elements in $D^+(S)$. The past domain of dependence $D^-(S)$ is defined similarly. We define the boundary of the future dependence domain as the future Cauchy horizon:$$\huge\partial D^\pm(S)=H^\pm(S)$$These are both null surfaces. Taking $S$ to be a subset of an achronal surface $\Sigma$:![[The metric tensor and Causality 2026-10-30 13.52.55.excalidraw]]
If every curve that remains inside this light cone must intersect $S$, then information specified on $S$ can be used to solve for the value of the fields at $p$. The set of all points for which our solution holds is simply the domain of dependence:$$\huge D(S)=D^+(S)\cup D^-(S)$$
A closed achronal surface $\Sigma$ is called a Cauchy surface if $D(\Sigma)$ is the entire manifold. I.e. we can predict what happens across spacetime from the information given on a Cauchy surface. If a spacetime has a Cauchy surface (not generally), we call it globally hyperbolic. Any closed, achronal set $\Sigma$ that has no boundary is called a partial Cauchy surface.

As global spacetime curvature can "tilt" light cones from one point to another, a sufficiently curved surface should make it possible for an everywhere timelike curve to intersect itself in its "past". This is a closed timelike curve. To highlight this point, consider the following:
> Consider a two-dimensional geometry with coordinates $(t,x)$ such that $(t,x+1)$ is identified with $(t,x)$. The topology is therefore $\Re\times S^1$ and we take