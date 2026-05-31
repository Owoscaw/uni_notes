
# Integrals and regions in surfaces:

In order to formulate the local Gauss-Bonnet theorem, we need to introduce some concepts and notions in a given surface $S$. 

Let us recall the integral of a continuous function $f:R\rightarrow\Re$ defined on a region $R\subset S$. Let us assume for simplicity that this region is totally contained in the image of a local parametrisation $\underline{x}:U\rightarrow S$, $R=\underline{x}(R_0)$ with $R_0\subset U$. In such case we define:$$\Huge \int_R f\,dA=\int_{R_0}(f\circ\underline{x})(u,v)\sqrt{E(u,v)G(u,v)-F^2(u,v)}du\,dv$$It can be shown that this is independent of parametrisation and that this works even if the parametrisation does not totally cover $R\subset S$.

Now consider a region $R\subset S$ bounded by a piecewise regular simple closed curve $\underline{\alpha}:[a,b]\rightarrow S$. We write $\partial R\subset S$ for the trace of such a boundary curve $\underline{\alpha}:[a,b]\rightarrow S$ of a region $R\subset S$ and call such object the boundary of $R$. Furthermore we refer to the regular segments of $\underline{\alpha}$, that is $\underline{\alpha}_i:[t_i,t_{i+1}]\rightarrow S$, as the edges of $\partial R$ and the points $\underline{\alpha}(t_i)\in S$ as the vertices of $\partial R$.

Next we introduce the notion of interior/exterior angles at vertices. Let $\underline{p}_i=\underline{\alpha}(t_i)\in S$ be a vertex. Then the two adjacent edges define two tangent lines given by $\Re\cdot\underline{\alpha}'_{i-1}(t_i)\subset T_{\underline{p}_i}S$ and $\Re\cdot\underline{\alpha}_i'(t_i)\subset T_{\underline{p}_i}S$. The angle $\gamma_i\in(0,2\pi)$ subtended by all tangent vectors pointing into $R$ is called the interior angle of $R$ at the vertex $\underline{p}_i$. The exterior angle is then defined as:$$\Huge \theta_i=\pi-\gamma_i\in(-\pi,\pi)$$

For any function $g:[a,b]\rightarrow\Re$ along a regular curve $\underline{\alpha}:[a,b]\rightarrow S$ let us introduce its line integral as:$$\Huge \int_{\underline{\alpha}}g\,ds=\int_a^bg(\underline{\alpha}(t))||\underline{\alpha}'(t)||_{\underline{\alpha}(t)}dt$$This is well defined and independent of parametrisations with the same orientation. We can extend this to piecewise regular curves with edges $\underline{\alpha}_i$ by:$$\Huge\int_{\underline{\alpha}}g\,ds=\sum_{i=0}^{n-1}\int_{\underline{\alpha}_i}g\,ds$$

Let us assume we have a region $R\subset S$ of an oriented surface $S$ with boundary $\partial R$. We say that the boundary of $R$ is traversed in a mathematically positive direction if, along the edges of $\partial R$, the positive rotations of the tangent vectors by $\pi/2$ are pointing into $R$.

Let $S$ be an oriented surface, $R\subset S$ be a region and $\underline{\alpha}:[a,b]\rightarrow S$ be a mathematically positively traversed parametrisation of $\partial R$. Let $\underline{p}_i$ be a vertex. Then the exterior angle $\theta_i$ at this vertex agrees with the angle of orientation from $\underline{\alpha}'_{i-1}(t_i)$ to $\underline{\alpha}_i'(t_i)$, measured in the positive direction.

# Local theorem of Gauss-Bonnet:

Let $S$ be an oriented surface and $T\subset S$ be a triangle. Let $\alpha,\beta,\gamma\in(0,2\pi)$ be its interior 