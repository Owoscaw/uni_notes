
We have previously seen [[Curves and Surfaces#Curves and curvature|plane curves]] and [[Space curves|space curves]] and their associated curvature properties:
> For a plane curve $\underline{\alpha}:I\rightarrow\Re^2$ we found the invariants representing the tangent vector and normal vector at a point $s\in I$:$$\Huge t(s)=\alpha'(s),\,\,n(s)=t(s)\begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}$$This let us define the "signed curvature" of the curve $\underline{\alpha}$ as:$$\Huge t'(s)=\kappa(s)n(s)$$
> For a space curve $\underline{\beta}:I\rightarrow\Re^3$ we found three invariants. Firstly we defined the tangent vector $t'(s)=\beta'(s)$ and directly set $\kappa(s)=||t''(s)||$ as the "unsigned curvature" of $\underline{\beta}$ at $s\in I$. Assuming $\kappa(s)\neq0$, we continue to define $n(s)=||t'(s)||^{-1}t'(s)$ and $b(s)=\underline{t}\times \underline{n}$. This allowed us to define the torsion by:$$\Huge b'(s)=\tau(s)n(s)$$

We now look at curves bounded to a [[Surfaces in R3|surface]] in $\Re^3$. Let $S\subset\Re^3$, then $\underline{\alpha}:I\rightarrow S$ is a curve on the surface $S$. For the [[Geometry of the Gauss map|Gauss map]] $N:S\rightarrow S^2$, the following vectors are perpendicular to $\underline{\alpha}'(s)$:
> $\underline{N}(\alpha(s))=\underline{N}(s)$, the normal to $S$
> $\underline{N}(s)\times\underline{\alpha}'(s)$ 
> ![[Curves on surfaces 2026-02-19 15.17.21.excalidraw]]

Since $1=\underline{\alpha}'(s)\cdot\underline{\alpha}'(s)$, we have that:$$\Huge\begin{align*}
\implies0&=\frac{d}{ds}(1)=\frac{d}{ds}(\underline{\alpha}'(s)\cdot\underline{\alpha}'(s))\\
&=2\underline{\alpha}''(s)\cdot\underline{\alpha}'(s)\\
\implies\underline{\alpha}''(s)&\perp\underline{\alpha}'(s)
\end{align*}$$So we have an orthonormal basis for the plane drawn above given by $\{\underline{N},\underline{N}\times\underline{\alpha}'\}$ and $\underline{\alpha}''(s)$ is by definition in this plane.

# Geodesic and normal curvature:

The functions $\kappa_g(s)$ and $\kappa_n(s)$ are known as the geodesic and normal curvatures, defined by:$$\Huge\underline{\alpha}''(s)=\kappa_g(s)\underline{N}\circ\underline{\alpha}(s)\times\underline{\alpha}'(s)+\kappa_n(s)\underline{N}\cdot\underline{\alpha}(s)$$That is, the acceleration vector that we showed was in this specific plane is given by a linear combination of the two vectors we showed to span the plane. The geodesic and normal curvatures are the coefficients in this linear combination. Note that we had $\underline{\alpha}$ is unit speed.

For general curves $\underline{\beta}:I\rightarrow S$ we let $\underline{\alpha}(s)=\underline{\beta}(t(s))$, making the curvatures:$$\Huge \kappa_{\beta,g}(t)=\kappa_{\alpha,g}(t(s)),\,\,\kappa_{\beta,n}(t)=\kappa_{\alpha,n}(t(s))$$This makes sense, as we want these curvatures to be independent of parametrisation. We write the curvatures explicitly as:$$\Huge \kappa_g(s)=\underline{\alpha}''\cdot(\underline{N}\times\underline{\alpha}'),\,\,\kappa_n(s)=\underline{\alpha}''(s)\cdot\underline{N}$$Since $\underline{\alpha}$ is also a space curve, we can relate $\kappa$ for space curves to geodesic and normal curvature:$$\Huge\kappa(s)=||\underline{\alpha}''(s)||=\sqrt{\underline{\alpha}''(s)\cdot\underline{\alpha}''(s)}=\sqrt{\kappa_g^2+\kappa_n^2}$$

We can consider a curve along a plane, which will be both a plane curve and a surface curve:
> Let $S=\{(u,v,0)\in\Re:(u,v)\in\Re^2\}$ and define $\underline{\alpha}:I\rightarrow S$ with $\underline{\alpha}(s)=(u(s),v(s),0)$.
> Here, the Gauss map will be a constant vector $\underline{N}=(0,0,1)$ so we compute:$$\Huge\begin{align*}
\underline{N}\times\underline{\alpha}'&=(0,0,1)\times(u',v',0)\\
&=(-v',u',0)\\
\implies\kappa_g(s)&=(u'',v'',0)\cdot(-v',u',0)\\
&=u'v''-v'u''\\
\implies\kappa_n(s)&=(u'',v'',0)\cdot(0,0,1)=0\\
\implies\kappa_\text{plane}&=(u'',v'')\cdot\underline{n}\\
&=(u'',v'')\cdot(-v',u')=\kappa_g\\
\implies\kappa_\text{space}&=|\kappa_g||(-v',u',0)|=|\kappa_g|=|\kappa_\text{plane}|
\end{align*}$$
> This agrees with our result linking plane curvature to geodesic and normal.

Consider a regular surface $S\subset\Re^3$ containing a straight-line curve $\underline{\alpha}(s)=\underline{p}+s\underline{v}$ for some $\underline{p}\in S$ and $\underline{v}\in\Re^3$ with $||\underline{v}||=1$:
> Then $\underline{\alpha}'(s)=\underline{v}$, $\underline{\alpha}''(s)=0$, and so $\kappa_g=\kappa_n=0$.

## Meusnier's theorem:
Let $S\subset\Re^3$, $\underline{p}\in S$, $\underline{w}\in T_\underline{p}S$ where [[Tangent planes#The tangent plane|$T_\underline{p}S$]] is the tangent plane to $S$ at $\underline{p}$. Then for all $\underline{\alpha}(s)\in S$ with $\underline{p}=\underline{\alpha}(s)$ (and so $\underline{w}=\underline{\alpha}'(s)$), the normal curvature is the same at that point for all curves:$$\Huge\kappa_n(s)=\underline{II}_\underline{p}(|\underline{w}|^{-1}\underline{w})=\frac{1}{||\underline{w}||^2}\langle -d_\underline{p}\underline{N}(\underline{w}),\underline{w}\rangle_\underline{p}$$Here, $\underline{II}_\underline{p}$ is the [[Geometry of the Gauss map#Weingarten map and second fundamental form|second fundamental form]]. It makes sense that $\underline{\alpha}$ does not appear in this result, as $\kappa_n(s)$ is independent of the curve.