
There are three descriptions of straight lines in $\Re^3$:
> The shortest distance between two points
> The path where no forces act to deflect
> Critical points for a variational problem

We focus on the second description, with the intrinsic geometry of the embedding in mind.

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