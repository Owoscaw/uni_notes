
TODO:
> Research the dipole magnet used, and how it affects particle paths
> Brush up on C++ and Python


# Integral/differential calculus:

We can embed $2$ dimensional surfaces in $\Re^3$ dimensional space parametrically using a map $\underline{x}(u,v)$ for $u\in[u_0,u_1],v\in[v_0,v_1]$. The partial derivatives$$\Huge\frac{\partial \underline{x}}{\partial u},\,\,\frac{\partial \underline{x}}{\partial v}$$represent the tangent vectors of the curve with fixed $v,u$ along $\underline{x}(u,v)$ respectively. We can similarly define volumes in $\Re^3$ as a subregion $V\subset\Re^3$.

## Surface integrals:
We can integrate over a scalar field $f$ over a surface $S$ with parametrisation $\underline{x}(u,v)$ using the definition$$\Huge\int_Sf\,dS=\int_Uf(\underline{x}(u,v))\left|\frac{\partial \underline{x}}{\partial u}\times\frac{\partial \underline{x}}{\partial v}\right|du\,dv$$where $U$ is the pre-image of $S$ in the $(u,v)$ plane. Note that the cross-product term represents the (un-normalised) normal vector of the surface $S$, the norm of which is the Jacobian.

We can integrate over a vector field $\underline{f}$ over a surface $S$ with unit normal $\underline{\hat{n}}$ using the definition$$\Huge\int_S\underline{f}\cdot\underline{\hat{n}}\,dS=\int_U\underline{f}(\underline{x}(u,v))\cdot\left(\frac{\partial \underline{x}}{\partial u}\times\frac{\partial \underline{x}}{\partial v}\right)du\,dv$$where $U$ is defined similarly. We write $\underline{\hat{n}}\,dS$ as $\underline{dS}$, the vector area element, so it is intuitive that the "flux" depends on the sign of $\underline{\hat{n}}$.

# Volume integrals:
Stepping up a dimension, we can define the volume integral of a scalar field $f$ over a volume $V$ as$$\Huge\int_V f\,dV=\int_Uf(\underline{x}(u,v,w))\left|\frac{\partial \underline{x}}{\partial u}\cdot\left(\frac{\partial \underline{x}}{\partial v}\times\frac{\partial \underline{x}}{\partial w}\right)\right|du\,dv\,dw$$where $U$ is the pre-image of $V$ in $(u,v,w)$ space. Similar to the definition of surface integrals, the spat product term represents the "volume element".

# Integral theorems:
The fundamental theorem of calculus can be generalised to vector calculus in a number of ways.

## Fundamental theorem of line integrals:
For a $C^1$ scalar field $f$ and an oriented curve $C$ with parametrisation $\underline{x}(t)$ with $t\in[t_0,t_1]$ we have:$$\Huge\int_C\underline{\nabla}f\cdot\hat{\underline{t}}\,dl=f(\underline{x}(t_1))-f(\underline{x}(t_0))$$Here $\underline{\nabla}$ is the gradient operator, representing the vector along which $f$ increases most rapidly for a fixed point. This is useful for conservative vector fields, which are vector fields $\underline{f}$ that can be written as the gradient of a scalar field $g$, $\underline{f}=\underline{\nabla}g$. Conservative vector fields have the property that the path integral between any pair of points is independent of the curve between them.

## Divergence theorem:
For a $C^1$ vector field and a closed surface $S$ with outwards normal $\underline{\hat{n}}$ that bounds a region $V$ we have:$$\Huge\oint_S\underline{f}\cdot\underline{\hat{n}}\,dS=\int_V(\underline{\nabla}\cdot\underline{f})dV$$This is essentially the generalisation of a derivative, the total flux out of the boundary of a region is equal to the total "expansion/compression" of the vector field in the region.

## Stokes' theorem:
For a $C^1$ vector field and closed oriented curve $C$ bounding a surface $S$, we have:$$\Huge\oint_C\underline{f}\cdot\hat{\underline{t}}\,dl=\int_S\underline{\nabla}\times\underline{f}\,dS$$This essentially states that the flux through ANY surface bounded by a curve $C$ is the same, we can generalise this further to:$$\Huge\int_\Omega d\omega=\int_{\partial\Omega}\omega$$Here $\Omega$ is a manifold with differential form $\omega$. This acts like a higher dimensional form of the fundamental theorem of calculus.