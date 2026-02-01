
We now introduce the Weingarten map, the derivative of the negative [[Smooth maps between surfaces#Gauss map|Gauss map]] of a regular surface $S$. At every point on $S$, this is a symmetric linear map of the tangent space, and allows us to introduce two fundamental curvature notions; Gaussian curvature and mean curvature.

# Weingarten map and second fundamental form:

Let $S\subset\Re^3$ be a regular surface. Recall that the Gauss map $N:S\rightarrow\Re^3$ is a smooth map associating to every point $\underline{p}\in S$ a unit normal vector $N(\underline{p})\perp T_\underline{p}S$. Often we only need a Gauss map locally and it suffices to define $N$ only on the image of a local parametrisation $\underline{x}:U\rightarrow\underline{x}(U)\subset S$. Since normal vectors lie in the unit sphere $S^2$, the Gauss map can be understood as a smooth map between surfaces. That is $N:S\rightarrow S^2$. We also introduced the derivative of a smooth map between surfaces, in the case of the Gauss map we have for $\underline{p}\in S$$$\Huge d_\underline{p}N:T_\underline{p}S\rightarrow T_{N(\underline{p})}S^2$$Noticing that $N(\underline{p})\perp T_\underline{p}S$ and $T_\underline{q}S^2\perp\underline{q}$ for all $\underline{q}\in S^2$, we conclude that $T_{N(\underline{p})}S^2\perp N(\underline{p})$ and therefore$$\Huge T_\underline{p}S=T_{N(\underline{p})}S^2$$This is a crucial observation, as it allows us to view $d_\underline{p}N$ as a linear map from $T_\underline{p}S$ onto itself.

We now introduce the Weingarten map, $-d_\underline{p}N$. Let $S\subset\Re^3$ be a regular surface and $N:U\rightarrow S^2$ be a Gauss map defined on a region $U\subset S$. For any point $\underline{p}\in U\subset S$, the linear map$$\Huge -d_\underline{p}N:T_\underline{p}S\rightarrow T_{-N(\underline{p})}S^2=T_\underline{p}S$$is called the Weingarten map of $S$ at $\underline{p}\in S$.

It is important to know that the Weingarten map is symmetric wrt the bilinear form $\langle \cdot,\cdot\rangle_\underline{p}$. This implies that $-d_\underline{p}N$ can be represented by a symmetric matrix with respect to an orthonormal basis of $T_\underline{p}S$ and we know that the eigenvalues and eigenvectors of symmetric matrices are all real and the eigenvectors are all perpendicular.

Let us now verify the symmetry of the Weingarten map. That is$$\Huge \langle d_\underline{p}N(\underline{w}_1),\underline{w}_2\rangle_\underline{p}=\langle \underline{w}_1,-d_\underline{p}N(\underline{w}_2)\rangle_\underline{p}$$To prove this, let $\underline{x}:U\rightarrow S$ be a local parametrisation with $\underline{x}(u,v)=\underline{p}$. It suffices to prove symmetry for the vectors of a basis. A basis of $T_\underline{p}S$ is given by $\underline{x}_u(u,v),\underline{x}_v(u,v)\in T_\underline{p}S$, so the proof of symmetry reduces to check$$\Huge \langle -d_\underline{p}N(\underline{x}_u(u,v)),\underline{x}_v(u,v)\rangle_\underline{p}=\langle \underline{x}_u(u,v),-d_\underline{p}N(\underline{x}_v(u,v))\rangle_\underline{p}$$Recall from our definition of the derivative that$$\Huge d_\underline{p}N(\underline{x}_u(u,v))=\frac{\partial N\circ\underline{x}}{\partial u}(u,v)=N_u(u,v)$$Therefore we only need to show that$$\Huge N_u(u,v)\cdot\underline{x}_v(u,v)=\underline{x}_u(u,v)\cdot N_v(u,v)$$Since $N(\underline{x}(u,v))\perp T_\underline{p}S$, we have $(N\circ\underline{x})\cdot\underline{x}_u=0$, and differentiation in the $v$-direction gives$$\Huge\begin{align*}
0&=\frac{\partial }{\partial v}((N\circ\underline{x})\underline{x}_u)(u,v)\\
&=\frac{\partial }{\partial v}\left((N\circ\underline{x})\cdot\frac{\partial \underline{x}}{\partial u}\right)(u,v)\\
&=\frac{\partial N\circ\underline{x}}{\partial v}(u,v)\cdot\frac{\partial \underline{x}}{\partial u}(u,v)+N\left(\underline{x}(u,v)\cdot\frac{\partial^2\underline{x}}{\partial v\partial u}(u,v)\right)\\
&=N_v(u,v)\cdot\underline{x}_u(u,v)+N(\underline{x}(u,v))\cdot\underline{x}_{vu}(u,v)
\end{align*}$$Similarly, differentiation in the $u$-direction gives$$\Huge0=N_u(u,v)\cdot\underline{x}_v(u,v)+N(\underline{x}(u,v))\cdot\underline{x}_{uv}(u,v)$$Taking their difference gives$$\Huge 0=N_u(u,v)\cdot\underline{x}_v(u,v)-N_v(u,v)\cdot\underline{x}_u(u,v)$$, completing the proof.

The Weingarten map $-d_\underline{p}N:T_\underline{p}S\rightarrow T_\underline{p}S$ is a linear map and can be represented by a matrix once we have a chosen basis of the tangent space $T_\underline{p}S$. More precisely, if $\underline{w}_1,\underline{w}_2$ are a basis of $T_\underline{p}S$ and if$$\Huge\begin{align*}
-d_\underline{p}N(\underline{w}_1)&=a\underline{w}_1+b\underline{w}_2\\
-d_\underline{p}N(\underline{w}_2)&=c\underline{w}_1+d\underline{w}_2
\end{align*}$$then we can identify $-d_\underline{p}N$ with the matrix $\begin{pmatrix}a & c \\ b & d\end{pmatrix}$, and $-d_\underline{p}N(\underline{w}_3)$ for $\underline{w}_3=e\underline{w}_1+f\underline{w}_2$ translates to the multiplication $\begin{pmatrix}a & c \\ b & d\end{pmatrix}\begin{pmatrix}e  \\ f\end{pmatrix}$.

We saw that the Weingarten map is symmetric wrt the inner product. If we choose an orthonormal basis $\underline{w}_1,\underline{w}_2\in T_\underline{p}S$ wrt this inner product, the corresponding matrix representation $A$ of $-d_\underline{p}N$ is symmetric. Indeed the entry $A_{ij}$ is just $\langle -d_\underline{p}N(\underline{w}_j),\underline{w}_i\rangle_\underline{p}$ and we have, since $-d_\underline{p}N$ is symmetric,$$\Huge A_{ij}=\langle -d_\underline{p}N(\underline{w}_j),\underline{w}_i\rangle_\underline{p}=\langle \underline{w}_j,-d_\underline{p}N(\underline{w}_i)\rangle_\underline{p}=\langle -d_\underline{p}N(\underline{w}_i),\underline{w}_j\rangle_\underline{p}=A_{ji}$$
Since $-d_\underline{p}N$ is a linear map of $T_\underline{p}S$ onto itself, it has a characteristic polynomial, eigenvalues, trace, and a determinant. They are computed by first choosing an arbitrary basis, finding the corresponding matrix representation, then computing the characteristic polynomial, eigenvalues, trace, and determinant. Two matrices $A,A'$ representing $-d_\underline{p}N$ with respect to different bases are linked by an equation $A'=B^{-1}AB$ , where $B$ is a transition matrix describing one basis in terms of the other. Then we have for the characteristic polynomials$$\Huge\begin{align*}
\det(A'-tI_2)&=\det(B^{-1}AB-tB^{-1}I_2B)\\
&=\det(B^{-1})\det(A-tI_2)\det(B)\\
&=\det(A-tI_2)
\end{align*}$$showing the independence of the characteristic polynomials. One can further show that the trace and determinant are independent of matrix representation.

Recall that we introduced the first fundamental form $\underline{I}_\underline{p}:T_\underline{p}S\rightarrow\Re$ as the quadratic form corresponding to the bilinear form $\langle \cdot,\cdot\rangle_\underline{p}$ as$$\Huge\underline{I}_\underline{p}(\underline{w})=\langle \underline{w},\underline{w}\rangle_\underline{p}=||\underline{w}||^2_\underline{p}$$A similar construction involving the Weingarten map leads to the second fundamental form that we will now define. Let $S\subset\Re^3$ be a regular surface, $\underline{p}\in S$, and $N:U\rightarrow S^2$ be a local Gauss map with $\underline{p}\in U$. Then the second fundamental form $S$ at $\underline{p}$ is the quadratic form $\underline{II}_\underline{p}:T_\underline{p}S\rightarrow\Re$, define by$$\Huge \underline{II}_\underline{p}(\underline{w})=\langle -d_\underline{p}N(\underline{w}),\underline{w}\rangle_\underline{p}$$
# Curvatures:

The determinant and the trace of the Weingarten map are our fundamental curvature notions associated to a regular surface.

Let $S\subset\Re^3$ be a regular surface with Gauss map $\underline{N}:U\rightarrow S^2,U\subset S$ a subset of $S$ containing a point $\underline{p}\in S$. Let $-d_\underline{p}\underline{N}:T_\underline{p}S\rightarrow T_\underline{p}S$ be the corresponding Weingarten map:
> $K(\underline{p})=\det(-d_\underline{p}\underline{N})$ is called the Gauss curvature of $S$ at $\underline{p}$
> $H(\underline{p})=\frac{1}{2}\text{tr}(-d_\underline{p}\underline{N})$ is called the mean curvature of $S$ at $\underline{p}$
> The eigenvalues $\kappa_1(\underline{p}),\kappa_2(\underline{p})\in\Re$ of $-d_\underline{p}\underline{N}$ are called the principal curvatures of $S$ at $\underline{p}$
> The eigenvectors $\underline{X}_1(\underline{p}),\underline{X}_2(\underline{p})\in\Re^3$ of $-d_\underline{p}\underline{N}$ are called the principal directions of $S$ at $\underline{p}$

Note that we have$$\Huge -d_\underline{p}\underline{N}(\underline{X}_1(\underline{p}))=\kappa_1(\underline{p})\underline{X}_1(\underline{p}),\,\,-d_\underline{p}\underline{N}(\underline{X}_2(\underline{p}))=\kappa_2(\underline{p})\underline{X}_2(\underline{p})$$and so we conclude$$\Huge K(\underline{p})=\kappa_1(\underline{p})\kappa_2(\underline{p}),\,\,H(\underline{p})=\frac{1}{2}(\kappa_1(\underline{p})+\kappa_2(\underline{p}))$$
The principal curvatures have a geometric meaning. Let $\underline{p}\in S$, then $\underline{N}=\underline{N}(\underline{p})\in\Re^3$ is a unit vector perpendicular to $T_\underline{p}S$. Intersecting the surface $S$ with a plane $E$ containing the vector $\underline{N}$ through $\underline{p}$, we obtain a curve in the plane $E$ near $\underline{p}$ with a certain curvature. This changes by rotating the plane $E$ around $\underline{N}$ and the principal curvatures $\kappa_1(\underline{p}),\kappa_2(\underline{p})$ are the two extremal curvatures of the resulting curves. It turns out that the two corresponding planes $E_1,E_2$ are perpendicular and are spanned by $\underline{N}$ together with $\underline{X}_1(\underline{p}),\underline{X}_2(\underline{p})$ respectively. Note that the curvature of the curves in $E\cap S$ have a sign, and so we have positive Gauss curvature $K(\underline{p})$ if both principal curvatures have the same sign, and negative Gauss curvature if they have opposite signs.![[Geometry of the Gauss map 2026-02-01 04.56.43.excalidraw]]
Let us consider a sphere $S=S^2(r)=\{\underline{p}\in\Re^3:||\underline{p}||=r\}$. A Gauss map is given by $$\Huge \underline{N}(\underline{p})=\frac{1}{r}\underline{p}$$, which is simply the identity up to a fixed multiplicative constant $(1/r)$. This means that the derivative of $\underline{N}$ will also be the identity, giving us the Weingarten map:$$\Huge -d_\underline{p}\underline{N}(\underline{w})=-\frac{1}{r}\underline{w}$$We therefore have a matrix representation $\begin{pmatrix}-1/r & 0 \\ 0 & -1/r\end{pmatrix}$ wrt any basis, hence $\kappa_1(\underline{p})=\kappa_2(\underline{p})=-1/r$. This implies our curvatures are$$\Huge K(\underline{p})=\frac{1}{r^2},\,\,H(\underline{p})=-\frac{1}{r}$$and our second fundamental form is$$\Huge\underline{II}_\underline{p}(\underline{w})= \langle -d_\underline{p}\underline{N}(\underline{w}),\underline{w}\rangle_\underline{p}=-\frac{1}{r^2}||\underline{w}||^2$$
Let $S\subset\Re^3$ be a regular surface, $\underline{x}:U\rightarrow S$ be a local parametrisation and $\underline{N}:\underline{x}(U)\rightarrow S^2$ be a local Gauss map. The functions $L,M,N:U\rightarrow\Re$ given by$$\Huge\begin{align*}
L(\underline{q})&=\langle \underline{x}_{uu}(\underline{q}),\underline{N}(\underline{x}(\underline{q}))\rangle_{\underline{x}(\underline{q})}=\underline{x}_{uu}(\underline{q})\cdot\underline{N}(\underline{x}(\underline{q}))\\
M(\underline{q})&=\langle \underline{x}_{uv}(\underline{q}),\underline{N}(\underline{x}(\underline{q}))\rangle_{\underline{x}(\underline{q})}=\underline{x}_{uv}(\underline{q})\cdot\underline{N}(\underline{x}(\underline{q}))\\
N(\underline{q})&=\langle \underline{x}_{vv}(\underline{q}),\underline{N}(\underline{x}(\underline{q}))\rangle_{\underline{x}(\underline{q})}=\underline{x}_{vv}(\underline{q})\cdot\underline{N}(\underline{x}(\underline{q}))
\end{align*}$$are called the coefficients of the second fundamental form wrt $\underline{x}$. Then we have at $\underline{p}=\underline{x}(\underline{q})$:$$\Huge \underline{II}_\underline{p}(a\underline{x}_u(\underline{q})+b\underline{x}_v(\underline{q}))=a^2L(\underline{q})+2ab M(\underline{q})+b^2N(\underline{q})$$Proof:
> One can show that$$\Huge\begin{align*}
\underline{N}_u(\underline{q})\cdot\underline{x}_u(\underline{q})&=-\underline{x}_{uu}(\underline{q})\cdot\underline{N}(\underline{p})\\
\underline{N}_v(\underline{q})\cdot\underline{x}_v(\underline{q})&=-\underline{x}_{vv}(\underline{q})\cdot\underline{N}(\underline{p})
\end{align*}$$
> Using these, and the symmetry of the Weingarten map, we find that$$\large\begin{align*}
\underline{II}_\underline{p}(a\underline{x}_u+b\underline{x}_v)&=\langle -d_\underline{p}\underline{N}(a\underline{x}_u+b\underline{x}_v,a\underline{x}_u+b\underline{x}_v\rangle_\underline{p}\\
&=a^2 \langle -d_\underline{p}\underline{N}(\underline{x}_u),\underline{x}_u\rangle_\underline{p}+2ab\langle -d_\underline{p}\underline{N}(\underline{x}_u),\underline{x}_v\rangle_\underline{p}+b^2 \langle -d_\underline{p}\underline{N}(\underline{x}_v),\underline{x}_v\rangle_\underline{p}\\
&=-a^2\underline{N}_u\cdot\underline{x}_u-2ab\underline{N}_u\cdot\underline{x}_v-b^2\underline{N}_v\cdot\underline{x}_v\\
&=a^2\underline{x}_{uu}\cdot\underline{N}+2ab\underline{x}_{uv}\cdot\underline{N}+b^2\underline{x}_{vv}\cdot\underline{N}\\
&=a^2L+2abM+b^2N
\end{align*}$$

Let us assume $\underline{p}=\underline{x}(\underline{q})$, we now derive the matrix representation of the Weingarten map wrt the basis $\underline{x}_u(\underline{q}),\underline{x}_v(\underline{q})\in T_\underline{p}S$. If we have $$\Huge\begin{align*}
-d_\underline{p}\underline{N}(\underline{x}_u(\underline{q}))&=a\underline{x}_u(\underline{q})+b\underline{x}_v(\underline{q})\\
-d_\underline{p}\underline{N}(\underline{x}_v(\underline{q}))&=c\underline{x}_u(\underline{q})+d\underline{x}_v(\underline{q})
\end{align*}$$then the matrix representation is given by $\begin{pmatrix}a & c \\ b & d\end{pmatrix}$. Assuming the above, we find$$\Huge\begin{align*}
L&=\langle -d_\underline{p}\underline{N}(\underline{x}_u),\underline{x}_u\rangle_\underline{p}=aE+bF\\
M&=\langle -d_\underline{p}\underline{N}(\underline{x}_u),\underline{x}_v\rangle_\underline{p}=aF+bG\\
M&=\langle -d_\underline{p}\underline{N}(\underline{x}_v),\underline{x}_u\rangle_\underline{p}=cE+dF\\
N&=\langle -d_\underline{p}\underline{N}(\underline{x}_v),\underline{x}_v\rangle_\underline{p}=cF+dG
\end{align*}$$leading to$$\Huge\begin{pmatrix}L & M \\ M & N\end{pmatrix}=\begin{pmatrix}aE+bF & cE+dF \\ aF+bG & cF+dG\end{pmatrix}=\begin{pmatrix}E & F \\ F & G\end{pmatrix}\begin{pmatrix}a & c \\ b & d\end{pmatrix}$$and we obtain our matrix representation of $-d\underline{N}_\underline{p}$ via left multiplication by $\begin{pmatrix}E & F \\ F & G\end{pmatrix}^{-1}$:$$\Huge\begin{align*}
\begin{pmatrix}a & c\\
b & d\end{pmatrix}&=\frac{1}{EG-F^2}\begin{pmatrix}G & -F\\
-F & E\end{pmatrix}\begin{pmatrix}L & M\\
M & N\end{pmatrix}\\
&=\frac{1}{EG-F^2}\begin{pmatrix}GL-FM & GM-FN\\
-FL+EM & -FM+EN\end{pmatrix}
\end{align*}$$
This representation implies the following, useful for explicit computation. Let $E,F,G$ and $L,M,N$ be the coefficients of the first and second fundamental forms wrt a local parametrisation $\underline{x}:U\rightarrow S$ of a regular surface $S\subset\Re^2$. Then the Gauss and mean curvature at $\underline{p}=\underline{x}(\underline{q})$ are given by$$\Huge\begin{align*}
K(\underline{p})&=\frac{L(\underline{q})N(\underline{q})-M(\underline{q})^2}{E(\underline{q})G(\underline{q})-F(\underline{q})^2}=\frac{\begin{vmatrix}L(\underline{q}) & M(\underline{q})\\
M(\underline{q}) & N(\underline{q})\end{vmatrix}}{\begin{vmatrix}E(\underline{q}) & F(\underline{q})\\
F(\underline{q}) & G(\underline{q})\end{vmatrix}}\\
H(\underline{p})&=\frac{E(\underline{q})N(\underline{q})-2F(\underline{q})M(\underline{q})+G(\underline{q})L(\underline{q})}{2(E(\underline{q})G(\underline{q})-F(\underline{q})^2)}
\end{align*}$$Proof:
> Using our matrix representation, we obtain:$$\Huge\begin{align*}
K(\underline{p})&=\frac{1}{(EG-F^2)^2}\begin{vmatrix}GL-FM & GM-FN\\
-FL+EM & -FM+EN\end{vmatrix}\\
&=\frac{(GL-FM)(-FM+EN)-(GM-FN)(-FL+EM)}{(EG-F^2)^2}\\
&=\frac{(EG-F^2)(LN-M^2)}{(EG-F^2)^2}=\frac{LN-M^2}{EG-F^2}
\end{align*}$$
> Similarly, we find:$$\Huge\begin{align*}
H(\underline{p})&=\frac{1}{2(EG-F^2)}\text{tr}\begin{pmatrix}GL-FM & GM-FN\\
-FL+EM & -FM+EN\end{pmatrix}\\
&=\frac{EN-2FM+GL}{2(EG-F)^2}
\end{align*}$$

# Curvatures of specific surfaces:

Take for example the hyperbolic paraboloid defined by$$\Huge S=\{(x,y,z)\in\Re^3:z=x^2-y^2\}$$, which is parametrised as the graph of the function $f(x,y)=x^2-y^2$. That is, $\underline{x}(u,v)=(u,v,u^2-v^2)$ for $(u,v)\in\Re^2$. Then we have$$\Huge \underline{x}_u(u,v)=(1,0,2u),\,\,\underline{x}_v(u,v)=(0,1,-2v)$$and further$$\Huge \underline{x}_{uu}(u,v)=(0,0,2),\,\,\underline{x}_{uv}=(0,0,0),\,\,\underline{x}_{vv}=(0,0,-2)$$To get our Gauss map, we find$$\Huge \underline{x}_u\times\underline{x}_v=(-2u,2v,1)\implies\underline{N}(\underline{x})=\frac{1}{D}(-2u,2v,1)$$where $D=\sqrt{1+4u^2+4v^2}$ is the norm of the above cross product. Therefore we find our first fundamental form coefficients:$$\Huge E(u,v)=1+4u^2,\,\,F(u,v)=-4uv,\,\,G(u,v)=1+4v^2$$and therefore$$\Huge EG-F^2=(1+4u^2)(1+4v^2)-16u^2v^2=1+4u^2+4v^2=D^2$$Using our Gauss map, we find the coefficients of the second fundamental form$$\Huge L=\frac{2}{D},\,\,M=0,\,\,N=-\frac{2}{D}$$Which implies that the Gauss curvature is given by$$\Huge K(\underline{x})=\frac{LN-M^2}{EG-F^2}=-\frac{4}{(1+4u^2+4v^2)^2}<0$$and the mean curvature$$\Huge \begin{align*}
H(\underline{x})&=\frac{EN+GL}{2(EG-F^2)}\\
&=\frac{-2(1+4u^2)+2(1+4v^2)}{2D^3}\\
&=\frac{4(v^2-u^2)}{(1+4u^2+4v^2)^{3/2}}
\end{align*}$$Finally, let us compute the principal curvatures at $\underline{x}(0,0)=(0,0,0)=\underline{p}\in S$. Here we have $K=-4,H=0$. Note that $\kappa_1,\kappa_2$ are the roots of the characteristic polynomial of any matrix $A$ representing $-d_\underline{p}\underline{N}$, that is$$\Huge\begin{align*}
\det(A-tI_2)&=(t-\kappa_1)(t-\kappa_2)\\
&=t^2-(\kappa_1+\kappa_2)t+\kappa_1\kappa_2\\
&=t^2-2Ht+K=t^2-4=(t-2)(t+2)
\end{align*}$$showing that $\kappa_{1/2}(\underline{p})=\pm2$.

We now introduce the special case where the tangent vectors $\underline{x}_u(\underline{q}),\underline{x}_v(\underline{q})$ are orthonormal wrt the bilinear forms $\langle \cdot,\cdot\rangle_\underline{p}$ and $\langle -d_\underline{p}\underline{N}(\cdot),\cdot\rangle_\underline{p}$ with $\underline{p}=\underline{x}(\underline{q})$. A local parametrisation $\underline{x}:U\rightarrow S$ with $F=0$ is called orthogonal, and a local parametrisation with both $F=M=0$ is called principal. In the case of principal parametrisation, we have that $\underline{x}_u,\underline{x}_v$ are principal directions with corresponding principal curvatures$$\Huge \kappa_1\circ\underline{x}=\frac{L}{E},\,\,\kappa_2\circ\underline{x}=\frac{N}{G}$$with Gauss and mean curvature given by$$\Huge K\circ\underline{x}=(\kappa_1\kappa_2)\circ\underline{x}=\frac{LN}{EG},\,\,H\circ\underline{x}=\frac{1}{2}(\kappa_1+\kappa_2)\circ\underline{x}=\frac{GL+EN}{2EG}$$Proof:
> Recall the matrix representing $-d_\underline{p}\underline{N}$ wrt the basis $\underline{x}_u,\underline{x}_v$ $$\Huge\frac{1}{EG-F^2}\begin{pmatrix}GL-FM & GM-FN \\ -FL+EM & -FM+EN\end{pmatrix}$$
> In the case of principal parametrisation we have $F=M=0$ and so this reduces to$$\Huge \frac{1}{EG}\begin{pmatrix}GL & 0 \\ 0 & EN\end{pmatrix}=\begin{pmatrix}\frac{L}{E} & 0 \\ 0 & \frac{N}{G}\end{pmatrix}$$and so the matrix eigenvalues are simple, corresponding to the result directly.

Take for example a surface of revolution. Let $S\subset\Re^3$ be the regular surface obtained by rotating a regular curve given by $\underline{\alpha}(v)=(f(v),0,g(v))$, $v\in I$ with $f(v)>0$ and $I\subset\Re$ an open interval around the vertical $z$-axis. Local parametrisations of $S$ are given by$$\Huge \underline{x}(u,v)=(f(v)\cos u,f(v)\sin u,g(v))$$for $(u,v)\in(0,2\pi)\times I$. We then have$$\Huge\begin{align*}
\underline{x}_u(u,v)&=(-f(v)\sin u,f(v)\cos u,0)\\
\underline{x}_v(u,v)&=(f'(v)\cos u,f'(v)\sin u,g'(v))
\end{align*}$$and so we have$$\Huge E=f^2(v),\,\,F=0,\,\,G=||\underline{\alpha}'(v)||^2$$, showing that the parametrisation is orthogonal. We also have$$\Huge (\underline{x}_u\times\underline{x}_v)(u,v)=(f(v)g'(v)\cos u,f(v)g'(v)\sin u,-f(v)f'(v))$$and so a Gauss map of the surface is given by$$\Huge \underline{N}(\underline{x}(u,v))=\frac{(\underline{x}_u\times\underline{x}_v)(u,v)}{||(\underline{x}_u\times\underline{x}_v)(u,v)||}=\frac{(g'(v)\cos u,g'(v)\sin u,-f'(v))}{||\underline{\alpha}'(v)||}$$To calculate the coefficients of the second fundamental form wrt $\underline{x}$, we need$$\Huge\begin{align*}
\underline{x}_{uu}(u,v)&=(-f(v)\cos u,-f(v)\sin u,0)\\
\underline{x}_{uv}(u,v)&=(-f'(v)\sin u,f'(v)\cos u,0)\\
\underline{x}_{vv}(u,v)&=(f''(v)\cos u,f''(v)\sin u,g''(v))
\end{align*}$$which implies$$\Huge\begin{align*}
L(u,v)&=\underline{x}_{uu}(u,v)\cdot\underline{N}(\underline{x}(u,v))=-\frac{f(v)g'(v)}{||\underline{\alpha}'(v)||}\\
M(u,v)&=\underline{x}_{uv}(u,v)\cdot\underline{N}(\underline{x}(u,v))=0\\
N(u,v)&=\underline{x}_{vv}(u,v)\cdot\underline{N}(\underline{x}(u,v))=\frac{f''(v)g'(v)-f'(v)g''(v)}{||\underline{\alpha}'(v)||}
\end{align*}$$, showing the parametrisation is principal. Therefore by our above proposition, we have$$\Huge\begin{align*}
\kappa_1\circ\underline{x}(u,v)&=\frac{L(u,v)}{E(u,v)}=-\frac{g'(v)}{f(v)||\underline{\alpha}'(v)||}\\
\kappa_2\circ\underline{x}(u,v)&=\frac{N(u,v)}{G(u,v)}=\frac{f''(v)g'(v)-f'(v)g''(v)}{||\underline{\alpha}'(v)||^3}\\
K\circ\underline{x}(u,v)&=\frac{-g'(v)(f''(v)g'(v)-f'(v)g''(v))}{f(v)||\underline{\alpha}'(v)||^4}\\
H\circ\underline{x}(u,v)&=-\frac{g'(v)}{2f(v)||\underline{\alpha}'(v)||}+\frac{f''(v)g'(v)-f'(v)g''(v)}{2||\underline{\alpha}'(v)||^3}
\end{align*}$$

Let $S\subset\Re^3$ be a regular surface with a Gauss map $\underline{N}:S\rightarrow S^2$ and $\kappa_1,\kappa_2:S\rightarrow\Re$ be the associated principal curvatures and $K:S\rightarrow\Re$ be the corresponding Gauss curvature:
> We call a point $\underline{p}\in S$$$\Huge\begin{cases}\text{elliptic} & K(\underline{p})>0 \\
\text{hyperbolic} & K(\underline{p})<0 \\
\text{flat} & K(\underline{p})=0\end{cases}$$, the subsets of points belonging to each classification are known as the elliptic/hyperbolic/flat regions of $S$.
> A point $\underline{p}\in S$ is called a planar point of the surface $S$ if $\kappa_1(\underline{p})=\kappa_2(\underline{p})=0$. Note that every planar point is also flat.
> A point $\underline{p}\in S$ is called umbilic if we have $\kappa_1(\underline{p})=\kappa_2(\underline{p})$. Note that every planar point is also umbilic.

A particular area in Differential Geometry is the study of minimal surfaces. These are surfaces that minimises area under certain constraints. A regular surface $S\subset\Re^2$ with everywhere vanishing mean curvature ($H=0$), is called minimal. 