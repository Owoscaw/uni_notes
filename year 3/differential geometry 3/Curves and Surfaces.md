
# Curves and curvature:

Curves are subsets of Euclidean space, they can be parametrised and described through maps from an interval to the Euclidean plane (in which case they have a direction). Their tangent vectors provide information about the speed and direction in which the curve is traced:![[example curves]]
This motivates a quantitative measure of the shape of a curve at every point. We call such a measure the curvature $\kappa$. We wish for it to have the following properties:
> $\kappa=0$ for all points on a straight line
> $\kappa$ should be independent of parametrisation
> $\kappa\to0$ for points on increasing circles
> $\kappa=\pm1/r$ for points on circles of radius $r>0$

Consider an ellipse with two focal points $A,B$. Unlike a circle, $\kappa$ should not be constant and must have two minima and maxima. Such extrema are called vertices:![[ellipse curvature example]]
We now ask how many vertices are there on a closed plane curve. The Four Vertex Theorem dictates that there are always at least $4$ vertices. We see this precisely on the ellipse, whereas all points are vertices on a circle.

# Surfaces:

Some simple examples of surfaces in $\Re^3$ are:
> Planes
> Paraboloids
> Spheres
> Tori

Give a point $P$ of a surface $S$. Intersecting the surface with a plane $E$ that contains the vector $N$ at $P$ orthogonal to the surface $S$ (normal vector) we see that $E\cap S$ is a planar curve with its own independent curvature (at least locally around $P$). Rotating $E$ around $N$ changes the resulting planar curve, we are interested in the extrema of these curvatures. These are known as the principal curvatures of $S$ at $P$, denoted by $\kappa_1(P),\kappa_2(P)$. This gives rise to the two notions:
> The product $\kappa_1(P)\kappa_2(P)$ is the Gaussian curvature $K(P)$ of the surface $S$ at $P$
> The arithmetic mean $\frac{\kappa_1(P)+\kappa_2(P)}{2}$ is the Mean curvature $H(P)$ of the surface $S$ at $P$

Note that for $S=\text{Euclidean plane}$ we have $K(P)=H(P)=0$ for all $P\in S$ and for $S=\text{Sphere of radius }r$ we have $K(P)=1/r^2,H(P)=1/r$