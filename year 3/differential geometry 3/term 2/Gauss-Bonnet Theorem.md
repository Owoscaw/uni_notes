
# Integrals and regions in surfaces:

In order to formulate the local Gauss-Bonnet theorem, we need to introduce some concepts and notions in a given surface $S$. 

Let us recall the integral of a continuous function $f:R\rightarrow\Re$ defined on a region $R\subset S$. Let us assume for simplicity that this region is totally contained in the image of a local parametrisation $\underline{x}:U\rightarrow S$, $R=\underline{x}(R_0)$ with $R_0\subset U$. In such case we define:$$\Huge \int_R f\,dA=\int_{R_0}(f\circ\underline{x})(u,v)\sqrt{E(u,v)G(u,v)-F^2(u,v)}du\,dv$$It can be shown that this is independent of parametrisation and that this works even if the parametrisation does not totally cover $R\subset S$.

Now consider a region $R\subset S$ bounded by a piecewise regular simple closed curve $\underline{\alpha}:[a,b]\rightarrow S$. We write $\partial R\subset S$ for the trace of such a boundary curve $\underline{\alpha}:[a,b]\rightarrow S$ of a region $R\subset S$ and call such object the boundary of $R$. Furthermore we refer to the regular segments of $\underline{\alpha}$, that is $\underline{\alpha}_i:[t_i,t_{i+1}]\rightarrow S$, as the edges of $\partial R$ and the points $\underline{\alpha}(t_i)\in S$ as the vertices of $\partial R$.

Next we introduce the notion of interior/exterior angles at vertices. Let $\underline{p}_i=\underline{\alpha}(t_i)\in S$ be a vertex. Then the two adjacent edges define two tangent lines given by $\Re\cdot\underline{\alpha}'_{i-1}(t_i)\subset T_{\underline{p}_i}S$ and $\Re\cdot\underline{\alpha}_i'(t_i)\subset T_{\underline{p}_i}S$. The angle $\gamma_i\in(0,2\pi)$ subtended by all tangent vectors pointing into $R$ is called the interior angle of $R$ at the vertex $\underline{p}_i$. The exterior angle is then defined as:$$\Huge \theta_i=\pi-\gamma_i\in(-\pi,\pi)$$

For any function $g:[a,b]\rightarrow\Re$ along a regular curve $\underline{\alpha}:[a,b]\rightarrow S$ let us introduce its line integral as:$$\Huge \int_{\underline{\alpha}}g\,ds=\int_a^bg(\underline{\alpha}(t))||\underline{\alpha}'(t)||_{\underline{\alpha}(t)}dt$$This is well defined and independent of parametrisations with the same orientation. We can extend this to piecewise regular curves with edges $\underline{\alpha}_i$ by:$$\Huge\int_{\underline{\alpha}}g\,ds=\sum_{i=0}^{n-1}\int_{\underline{\alpha}_i}g\,ds$$

Let us assume we have a region $R\subset S$ of an oriented surface $S$ with boundary $\partial R$. We say that the boundary of $R$ is traversed in a mathematically positive direction if, along the edges of $\partial R$, the positive rotations of the tangent vectors by $\pi/2$ are pointing into $R$.

Let $S$ be an oriented surface, $R\subset S$ be a region and $\underline{\alpha}:[a,b]\rightarrow S$ be a mathematically positively traversed parametrisation of $\partial R$. Let $\underline{p}_i$ be a vertex. Then the exterior angle $\theta_i$ at this vertex agrees with the angle of orientation from $\underline{\alpha}'_{i-1}(t_i)$ to $\underline{\alpha}_i'(t_i)$, measured in the positive direction.

# Local theorem of Gauss-Bonnet:

Let $S$ be an oriented surface and $T\subset S$ be a triangle. Let $\alpha,\beta,\gamma\in(0,2\pi)$ be its interior angles. Then we have$$\Huge\int_TK\,dA+\int_{\partial T}\kappa_g\,ds=\alpha+\beta+\gamma-\pi$$where $K:S\rightarrow\Re$ is the Gauss curvature of $S$ and $\kappa_g:[a,b]\rightarrow S$ is the geodesic curvature of a mathematically positively traversed piecewise regular parametrisation $\underline{\alpha}:[a,b]\rightarrow S$ of $\partial T$.

The angle of the tangent along a mathematically positively traversed piecewise regular simple closed curve $\underline{\alpha}:[0,1]\rightarrow \Re^2$ in the Euclidean plane turns by $2\pi$. That is, if $\theta:[0,1]\rightarrow\Re$ is the continuously varying angle between $\underline{\alpha}'(0)$ and $\underline{\alpha}'(t)$, then we have:$$\Huge\int_0^1\theta'(s)ds=2\pi$$This has an immediate corollary for geodesic triangles in surfaces of constant Gauss curvature. Let $T\subset \mathbb{H}^2$ be a triangle in an oriented surface $S\subset\Re^3$ of constant Gauss curvature $K$. Assume that $T$ has three geodesic sides and denote its interior angles by $\alpha,\beta,\gamma$. Then we have:$$\Huge K\cdot\text{area}(T)=\alpha+\beta+\gamma-\pi$$

Let $S$ be an oriented surface and $R\subset S$ be a polygon with interior angles $\gamma_1,\dots,\gamma_n$. Then we have$$\Huge \int_RK\,dA+\int_{\partial R}\kappa_g\,ds=\sum_{i=1}^n\gamma_i-(n-2)\pi$$where $K:S\rightarrow \Re$ is the Gauss curvature of $S$ and $\kappa_g:[a,b]\rightarrow\Re$ is the geodesic curvature of a mathematically positively traversed piecewise regular parametrisation $\underline{\alpha}:[a,b]\rightarrow S$ of $\partial R$.

# Euler characteristic and global Gauss-Bonnet:

Let $R\subset S$ be a region of a surface $S$. A triangulation $\mathcal{T}$ of $R$ is a subdivision of $R$ into finitely many triangles meeting only in common edges or common vertices. The Euler characteristic of $R$ is defined by:$$\Huge\begin{align*}
\chi(R)&=F(\mathcal{T})-E(\mathcal{T})+V(\mathcal{T})\\
&=\text{no. triangles }-\text{no. edges }-\text{no. vertices}
\end{align*}$$
Let $S$ be an oriented surface and $R\subset S$ be a region with piecewise smooth boundary $\partial R$ oriented in such a way that positive rotations by $\pi/2$ of the tangent vectors of a parametrisation of a piecewise regular curve lead to tangent vectors pointing into the region $R$. Let $\theta_1,\dots,\theta_n$ be the exterior angles at the vertices of $\partial R$. Then we have$$\Huge\int_R K\,dA+\int_{\partial R}\kappa_g\,ds+\sum_{i=1}^n\theta_i=2\pi\chi(R)$$, in particular if $S\subset\Re^3$ is a closed connected surface then:$$\Huge\int_RK\,dA=2\pi\chi(R)$$