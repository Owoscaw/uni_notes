
Recall that both [[Geometry of the Gauss map#Curvatures|Gauss and mean]] curvature of a [[Surfaces in R3#Regular points/values|regular surface]] $S\subset\Re^3$ are introduced via the Weingarten map, which is essentially the derivative of the Gauss map. The principal curvatures are invariants of the surface $S$, which depends on the embedding. This means that all inner geometric properties remain unchanged. These intrinsic geometries can be derived from the [[Tangent planes#First fundamental form|first fundamental form]], while many extrinsic properties are related to the second fundamental form.

The Gauss curvature, while defined extrinsically, is an intrinsic quantity. This is one of Gauss' fundamental discoveries, naming it "Theorema Egregium" which translates to "Outstanding Theorem". More formally, this result states tat Gauss curvature of a surface $S$ with parametrisation $x:U\rightarrow S$ can be computed solely from the coefficients $E,F,G:U\rightarrow\Re$ of the first fundamental form and their derivatives.

The Gauss curvature at a point $\underline{p}\in S\subset\Re^3$ depends only on the coefficients $E,F,G$ and their derivatives of a local parametrisation $x:U\rightarrow S$ with $\underline{p}\in x(U)$.

# Christoffel symbols:

Christoffel symbols are useful objects in their description of second derivatives of a local parametrisation. Let $x:U\rightarrow S$ be a local parametrisation of a regular surface $S\subset\Re^3$ and $N:S\rightarrow S^2$ be a Gauss map of $S$. Note that for all $\underline{q}\in U$, the vectors $x_u(\underline{q}),x_v(\underline{q}),N(x(\underline{q}))$ form a basis of $\Re^3$. The Christoffel symbols $\Gamma^k_{ij}$ for $i,j,k\in\{1,2\}$ are functions $\Gamma^k_{ij}:U\rightarrow\Re$ defined as follows:$$\Huge\begin{align*}
x_{uu}(\underline{q})&=\Gamma^1_{11}(\underline{q})x_u(\underline{q})+\Gamma^2_{11}(\underline{q})x_v(\underline{q})+L(\underline{q})N(x(\underline{q}))\\
x_{uv}(\underline{q})&=\Gamma^1_{12}(\underline{q})x_u(\underline{q})+\Gamma^2_{12}(\underline{q})x_v(\underline{q})+M(\underline{q})N(x(\underline{q}))\\
x_{uu}(\underline{q})&=\Gamma^1_{21}(\underline{q})x_u(\underline{q})+\Gamma^2_{21}(\underline{q})x_v(\underline{q})+M(\underline{q})N(x(\underline{q}))\\
x_{uu}(\underline{q})&=\Gamma^1_{22}(\underline{q})x_u(\underline{q})+\Gamma^2_{22}(\underline{q})x_v(\underline{q})+N(\underline{q})N(x(\underline{q}))
\end{align*}$$Here, $L,M,N:U\rightarrow\Re$ are the coefficients of the second fundamental form wrt $x$. Note that the coefficients in front of $N(x(\underline{q}))$ are determined by the Gauss map definition of the second fundamental form. Also, since $x_{uv}=x_{vu}$, the Christoffel symbols are symmetric in the lower indices:$$\Huge \Gamma^k_{ij}=\Gamma^k_{ji}$$
We now aim to describe the Christoffel symbols in terms of $E,F,G$. We compute:$$\Huge\begin{align*}
x_{uu}\cdot x_u&=\frac{1}{2}\frac{\partial }{\partial u}x_u\cdot x_u=\frac{1}{2}E_u\\
x_{uv}\cdot x_u&=x_{vu}\cdot x_u=\frac{1}{2}\frac{\partial }{\partial v}x_u\cdot x_u=\frac{1}{2}E_v\\
x_{vv}\cdot x_v&=\frac{1}{2}\frac{\partial }{\partial v}x_v\cdot x_v=\frac{1}{2}G_v\\
x_{vu}\cdot x_v&=x_{uv}\cdot x_v=\frac{1}{2}\frac{\partial }{\partial u}x_v\cdot x_v=\frac{1}{2}G_u\\
x_{uu}\cdot x_v&=\frac{\partial }{\partial u}x_u\cdot x_v-x_u\cdot x_{uv}=F_u-\frac{1}{2}E_v\\
x_{vv}\cdot x_u&=\frac{\partial }{\partial v}x_v\cdot x_v-x_v\cdot x_{vu}=F_v-\frac{1}{2}G_u
\end{align*}$$Using these identities and the definition of the Christoffel symbols, we find that:$$\Huge\begin{align*}
E\Gamma^1_{11}+F\Gamma^2_{11}&=x_{uv}\cdot x_u=\frac{1}{2}E_u\\
F\Gamma^1_{11}+G\Gamma^2_{11}&=x_{uv}\cdot x_v=\frac{1}{2}G_u
\end{align*}$$Which we can write in matrix form as:$$\Huge \begin{pmatrix}E & F \\ F & G\end{pmatrix}\begin{pmatrix}\Gamma^1_{11} \\ \Gamma^2_{11}\end{pmatrix}=\begin{pmatrix}\frac{1}{2}E_u \\ F_u-\frac{1}{2}E_v\end{pmatrix}$$Similarly, we obtain both:$$\Huge \begin{pmatrix}E & F \\ F & G\end{pmatrix}\begin{pmatrix}\Gamma^1_{12} \\ \Gamma^2_{12}\end{pmatrix}=\begin{pmatrix}\frac{1}{2}E_v \\ \frac{1}{2}G_u\end{pmatrix},\,\,\begin{pmatrix}E & F \\ F & G\end{pmatrix}\begin{pmatrix}\Gamma^1_{22} \\ \Gamma^2_{22}\end{pmatrix}=\begin{pmatrix}F_v-\frac{1}{2}G_u \\ \frac{1}{2}G_v\end{pmatrix}$$Combining our results, we find that:$$\Huge \begin{pmatrix}E & F \\ F & G\end{pmatrix}\begin{pmatrix}\Gamma^1_{11} & \Gamma^1_{12} & \Gamma^1_{22} \\ \Gamma^2_{11} & \Gamma^2_{12} & \Gamma^2_{22}\end{pmatrix}=\begin{pmatrix}\frac{1}{2}E_u & \frac{1}{2}E_v & F_v-\frac{1}{2}G_u \\ F_u-\frac{1}{2}E_v & \frac{1}{2}G_u & \frac{1}{2}G_v\end{pmatrix}$$From this we conclude that for a local parametrisation $x:U\rightarrow S$ with associated coefficients $E,F,G$ of the first fundamental form, we can write the Christoffel symbols as:$$\large \begin{pmatrix}\Gamma^1_{11} & \Gamma^1_{12} & \Gamma^1_{22} \\ \Gamma^2_{11} & \Gamma^2_{12} & \Gamma^2_{22}\end{pmatrix}=\frac{1}{EG-F^2}\begin{pmatrix}G & -F \\ -F & E\end{pmatrix}\begin{pmatrix}\frac{1}{2}E_u & \frac{1}{2}E_v & F_v-\frac{1}{2}G_u \\ F_u-\frac{1}{2}E_v & \frac{1}{2}G_u & \frac{1}{2}G_v\end{pmatrix}$$This is significant, as this defines the Christoffel symbols as an intrinsic quantity. Note that in the case of an orthogonal parametrisation ($F=0$), this simplifies considerably:$$\Huge\begin{align*}
\begin{pmatrix}\Gamma^1_{11} & \Gamma^1_{12} & \Gamma^1_{22}\\
\Gamma^2_{11} & \Gamma^2_{12} & \Gamma^2_{22}\end{pmatrix}&=\frac{1}{EG}\begin{pmatrix}G & 0\\
0 & E\end{pmatrix}\begin{pmatrix}\frac{1}{2}E_u & \frac{1}{2}E_v & -\frac{1}{2}G_u\\
-\frac{1}{2}E_v & \frac{1}{2}G_u & \frac{1}{2}G_v\end{pmatrix}\\
&=\frac{1}{2}\begin{pmatrix}1/E & 0\\
0 & 1/G\end{pmatrix}\begin{pmatrix}E_u & E_v & -G_u\\
-E_v & G_u & G_v\end{pmatrix}\\
&=\frac{1}{2}\begin{pmatrix}E_u/E & E_v/E & -G_u/E\\
-E_v/G & G_u/G & G_v/G\end{pmatrix}
\end{align*}$$