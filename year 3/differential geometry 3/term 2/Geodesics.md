
Geodesics are the generalisation of straight lines in Euclidean space. The fundamental properties of straight lines are:
> Straight lines represent the shortest path between two points
> Travelling along straight lines at a constant speed results in no force (no acceleration)

Instead of using a geometric description of straight lines, we use the physical description to generalise straight lines to geodesics on surfaces.
# Geodesics as ODE solutions:

Let $S\subset\Re^3$ be a [[Surfaces in R3#Regular points/values|regular surface]]. A regular curve $\underline{\alpha}:I\rightarrow S$ is called a geodesic if $\underline{\alpha}''$ is normal to $S$. That is:$$\Huge \underline{\alpha}''\perp T_{\underline{\alpha}(t)}S\,\,\forall t\in I$$
An immediate consequence of this definition is that for a geodesic $\underline{\alpha}$ of $S$, we must have $||\underline{\alpha}'||$ is constant. That is, $\underline{\alpha}$ is proportional to a unit speed curve. Proof:
> Let $f(t)=||\underline{\alpha}'(t)||^2=\underline{\alpha}'(t)\cdot\underline{\alpha}'(t)$, the proof is then immediate:$$\Huge\begin{align*}
f'(t)&=\underline{\alpha}''(t)\cdot\underline{\alpha}'(t)+\underline{\alpha}'(t)\cdot\underline{\alpha}''(t)\\
&=2\underline{\alpha}''(t)\cdot\underline{\alpha}'(t)=0
\end{align*}$$This is because $\underline{\alpha}''(t)$ is normal to $S$, while $\underline{\alpha}'(t)\in T_{\underline{\alpha}(t)}S$, so they are orthogonal to one another. Since $f'(t)=0$, $f(t)$ is constant, as required.

Let us consider great circles on a sphere:
> Let $$\Huge S^2(r)=\{\underline{x}\in\Re^3:||\underline{x}||^2=r^2\}$$be the round sphere of radius $r$. A great circle is the intersection of $S^2(r)$ with a plane through the origin. That is, they are circles on $S^2(r)$ with the same center and radius.
> Let $P$ be a plane through the origin, $X_1,X_2$ an orthonormal basis of $P$. Then $P\cap S^2(r)$ is defined by the curve$$\Huge\underline{\alpha}(t)=r\cos tX_1+r\sin tX_2$$, which has derivatives:$$\Huge\begin{align*}
\underline{\alpha}'(t)&=-r\sin tX_1+r\cos tX_2\\
\underline{\alpha}''(t)&=-r\cos tX_1-r\sin tX_2\\
&=-\underline{\alpha}(t)
\end{align*}$$
> This is orthogonal to the tangent plane of $S^2(r)$ and so must be a geodesic.

Let us consider geodesics on a cylinder:
> We define the cylinder as $$\Huge S=\{\underline{x}:x^2+y^2=1\}$$and consider the curve$$\Huge\underline{\alpha}(t)=(\cos(at+b),\sin(at+b),ct+d)$$with $a,b,c,d\in\Re$ and $a,c\neq0$. The trace of this curve is generally a subset that spirals up or down along the cylinder.
> We verify that $\underline{\alpha}$ is a geodesic, we have:$$\Huge\begin{align*}
\underline{\alpha}'(t)&=(-a\sin(at+b),a\cos(at+b),c)\\
\underline{\alpha}''(t)&=(-a^2\cos(at+b),-a^2\sin(at+b),0)
\end{align*}$$
> Noting that the inward unit normal of $S$ is given by $(-x,-y,0)$ and it is clear that $\underline{\alpha}''$ is parallel to the unit normal of $S$ at $\underline{\alpha}(t)$. It can be shown that all geodesics on $S$ have this form.
> In the case of $c=0$ we obtain a parallel of $S$ and in the case of $a=0$ we obtain a meridian of $S$.

We now provide an alternative definition of geodesics that implies geodesics are intrinsic objects of surfaces. Let $S$ be a surface and $\underline{\alpha}:I\rightarrow S$ be a regular curve. Then the following are equivalent:
> $\underline{\alpha}$ is a geodesic
> $\underline{\alpha}$ is constant speed and its geodesic curvature $\kappa_g$ vanishes identically

Since $||\underline{\alpha}'||$ and $\kappa_g$ are intrinsic quantities, geodesics are also intrinsic to the surface:
> Let us assume $\underline{\alpha}$ is a geodesic, then $\underline{\alpha}$ is constant speed trivially and:$$\Huge \begin{align*}
\kappa_g&=\frac{1}{||\underline{\alpha}'||^3}(\underline{\alpha}'\times\underline{\alpha}'')\cdot(\underline{N}\circ\underline{\alpha})\\
&=\frac{1}{||\underline{\alpha}||^3}(\underline{\alpha}\times0)\cdot(\underline{N}\circ\underline{\alpha})=0
\end{align*}$$This prove the first equivalence direction.
> We now assume $\underline{\alpha}$ is constant speed and has vanishing geodesic curvature. Since $\underline{\alpha}$ is regular, $\underline{\alpha}'$ and $\underline{\alpha}'\times\underline{N}(\underline{\alpha})$ span the [[Tangent planes#The tangent plane|tangent plane]] $T_\underline{\alpha}S$. Therefore it is only required to show $\underline{\alpha}''$ is perpendicular to both $\underline{\alpha}'$ and $\underline{\alpha}'\times(\underline{N}\circ\underline{\alpha})$ as this would force $\underline{\alpha}''$ to be normal to $S$.
> Constant $\underline{\alpha}'$ implies $\underline{\alpha}'\cdot\underline{\alpha}'$ is constant and so $\underline{\alpha}''\perp\underline{\alpha}'$. Since $\kappa_g=0$ we have:$$\Huge \kappa_g=\underline{\alpha}'\times\underline{\alpha}''\cdot(\underline{N}\circ\underline{\alpha})=0$$
> A basic property of the spat product is$$\Huge (\underline{x}\times\underline{y})\cdot\underline{z}=\begin{vmatrix}\underline{x} \\ \underline{y} \\ \underline{z}\end{vmatrix}$$and so we can write the vanishing curvature condition as$$\Huge\begin{vmatrix}\underline{\alpha}' \\ \underline{\alpha}'' \\ \underline{N}\circ\underline{\alpha}\end{vmatrix}=0$$where we consider $\underline{\alpha}',\underline{\alpha}'',\underline{N}\circ\underline{\alpha}$ as row vectors. Interchanging rows, we can write this as$$\Huge 0=\begin{vmatrix}\underline{\alpha}' \\ \underline{N}\circ\underline{\alpha} \\ \underline{\alpha}''\end{vmatrix}=(\underline{\alpha}'\times(\underline{N}\circ\underline{\alpha}))\cdot\underline{\alpha}''$$, showing that $\underline{\alpha}''$ is normal to $S$ and therefore a geodesic.

