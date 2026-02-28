
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
Let $S\subset\Re^3$, $\underline{p}\in S$, $\underline{w}\in T_\underline{p}S$ where [[Tangent planes#The tangent plane|$T_\underline{p}S$]] is the tangent plane to $S$ at $\underline{p}$. Then for all $\underline{\alpha}(s)\in S$ with $\underline{p}=\underline{\alpha}(s)$ (and so $\underline{w}=\underline{\alpha}'(s)$), the normal curvature is the same at that point for all curves:$$\Huge\kappa_n(s)=\underline{II}_\underline{p}(|\underline{w}|^{-1}\underline{w})=\frac{1}{||\underline{w}||^2}\langle -d_\underline{p}\underline{N}(\underline{w}),\underline{w}\rangle_\underline{p}$$Here, $\underline{II}_\underline{p}$ is the [[Geometry of the Gauss map#Weingarten map and second fundamental form|second fundamental form]]. It makes sense that $\underline{\alpha}$ does not appear in this result, as $\kappa_n(s)$ is independent of the curve. Proof:
> Let us assume $\underline{\alpha}$ is a unit speed curve and let $\underline{p}=\underline{\alpha}(s)$ for some $s\in I$. We differentiate $\underline{\alpha}'\cdot(N\circ\underline{\alpha})=0$ at $s$ and obtain:$$\Huge\begin{align*}
0&=\underline{\alpha}''(s)\cdot\underline{N}(\underline{\alpha}(s))+\underline{\alpha}'(s)\cdot d_\underline{p}\underline{N}(\underline{\alpha}'(s))\\
&=\kappa_n(s)-\langle -d_\underline{p}\underline{N}(\underline{\alpha}'(s)),\underline{\alpha}'(s)\rangle_\underline{p}\\
\implies\kappa_n(s)&=\langle -d_\underline{p}\underline{N}(\underline{\alpha}'(s)),\underline{\alpha}'(s)\rangle_\underline{p}
\end{align*}$$with $||\underline{\alpha}'(s)||=1$. This proves the theorem for a unit speed curve and by our previous observations, for general curves passing through $\underline{p}$.

Note that the reason why the [[Geometry of the Gauss map#Weingarten map and second fundamental form|Weingarten map]] was defined as the negative derivative is because that otherwise, the relationship between normal curvature and the second fundamental form would require another minus sign. Our choice for the Weingarten map therefore gives the simplest possible relation between curvature and second fundamental form.

We can also use Meusnier's theorem to give a relation between normal curvature and principal curvature. Let $S\subset\Re^3$ be a regular surface with Gauss map $\underline{N}:S\rightarrow S^2$ and $\underline{p}\in S$. Then the principal curvatures $\kappa_1(\underline{p}),\kappa_2(\underline{p})$ are the minimum and maximal value of the possible normal curvatures obtained via regular curves $\underline{\alpha}:I\rightarrow S$ through $\underline{p}$. Proof:
> Let $\underline{X}_1,\underline{X}_1\in T_\underline{p}S$ be an orthonormal basis of eigenvalues of the Weingarten map $-d_\underline{p}\underline{N}$ to the eigenvalues $\kappa_1,\kappa_2$ respectively.
> It is known that if $X_\theta=\cos\theta X_1+\sin\theta X_2\in T_\underline{p}S$ then we can write$$\Huge\underline{II}_\underline{p}(X_\theta)=\kappa_1\cos^2\theta+\kappa_2\sin^2\theta$$, assuming that $\kappa_1\leq\kappa_2$ we see that:$$\Huge \kappa_1=\min_\theta\underline{II}_\underline{p}(X_\theta),\,\,\kappa_2\max_\theta\underline{II}_\underline{p}(X_\theta)$$
> Then by Meusnier's theorem, the normal curvature of any regular curve $\underline{\alpha}:I\rightarrow S$ with $\underline{\alpha}(t)=\underline{p}$ is given by$$\Huge\kappa_n(t)=\underline{II}_\underline{p}(\underline{\alpha}'(t)/||\underline{\alpha}'(t)||)$$and there exists $\theta\in\Re$ with $\underline{\alpha}'(t)/||\underline{\alpha}'(t)||=X_\theta$. Conversely, it is easy to see that for every $\theta\in\Re$ we can find a regular curve $\underline{\alpha}:I\rightarrow S$ with $\underline{\alpha}(t)=X_\theta$. This shows that $\kappa_1$ agrees with the minimum normal curvature of curves through $\underline{p}$ and $\kappa_2$ agrees with the maximal, as required.

Another direct consequence of Meusnier's theorem is a formula to calculate normal curvature with the coefficients of the first and second fundamental forms. Let $S\subset\Re^3$ be a regular surface with Gauss map $\underline{N}:S\rightarrow S^2$. Let $\underline{x}:U\rightarrow S$ be a local parametrisation and $E,F,G,L,M,N:U\rightarrow\Re$ be the corresponding coefficients of the fundamental forms. Then we have for any $\underline{a; }:I\rightarrow\underline{x}(U)\subset S$ with $\underline{\alpha}(t)=\underline{x}(u(t),v(t))$:$$\Huge\kappa_n=\frac{\underline{II}_\underline{\alpha}(\underline{\alpha}')}{\underline{I}_\underline{\alpha}(\underline{\alpha}')}=\frac{(u')^2L+2u'v'M+(v')^2N}{(u')^2E+2u'v'F+(v')^2G}$$Proof:
> The first identity follows from Meusnier's theorem directly:$$\Huge \kappa_n(t)=\underline{II}_{\underline{\alpha(t)}}\left(\frac{\underline{\alpha}'(t)}{||\underline{\alpha}'(t)||}\right)=\frac{\underline{II}_{\underline{\alpha}(t)}(\underline{\alpha}'(t))}{||\underline{\alpha}'(t)||^2}=\frac{\underline{II}_{\underline{\alpha}(t)}(\underline{\alpha}'(t))}{\underline{I}_{\underline{\alpha}(t)}(\underline{\alpha}'(t))}$$
> The second is a consequence of the way we write the first and second fundamental form calculated with a local parametrisation. By the chain rule,$$\Huge\underline{\alpha}'(t)=u'(t)\underline{x}_u(\underline{q})+v'(t)\underline{x}_v(t)$$with $\underline{q}=(u(t),v(t))$ and therefore $\underline{p}=\underline{x}(\underline{q})$. 
> Using linearity in the inner form and the symmetry of the Weingarten map:$$\large\begin{align*}
\underline{II}_{\underline{\alpha}(t)}(\underline{\alpha}'(t))&=(-d_\underline{p}\underline{N}(\underline{\alpha}'(t)))\cdot\underline{\alpha}'(t)\\
&=(u'(t))^2(-d_\underline{p}\underline{N}(\underline{x}_u(\underline{q}))\cdot\underline{x}_u(\underline{q}))+u'(t)v'(t)(-d_\underline{p}\underline{N}(\underline{x}_u(\underline{q}))\cdot\underline{x}_v(\underline{q}))\\
&+v'(t)u'(t)(-d_\underline{p}\underline{N}(\underline{x}_v(\underline{q}))\cdot\underline{x}_u(\underline{q}))+(v'(t))^2(-d_\underline{p}\underline{N}(\underline{x}_v(\underline{q}))\cdot\underline{x}_v(\underline{q}))\\
&=(u'(t))^2L+2u'(t)v'(t)M+(v'(t))^2N
\end{align*}$$
> Similarly, we obtain$$\Huge \underline{I}_{\underline{\alpha}(t)}(\underline{\alpha}'(t))=(u'(t))^2E+2u'(t)v'(t)F+(v'(t))^2G$$, finishing the proof.

Let $S\subset\Re^3$ be a regular surface with Gauss map $\underline{N}:S\rightarrow S^2$ and $\underline{\beta}:I\rightarrow S)$ be a regular curve not necessarily unit speed. Then the geodesic curvature of $\underline{\beta}$ is given by:$$\Huge\kappa_g=\frac{1}{||\underline{\beta}'||^2}(\underline{\beta}'\times\underline{\beta}'')\cdot(\underline{N}\circ\underline{\beta})$$
# Asymptotic curves and lines of curvature:

Let $S\subset\Re^3$ be a regular surface. A regular curve $\underline{\alpha}:I\rightarrow S$ is called a line of curvature if $\underline{\alpha}'(t)$ is an eigenvector of the Weingarten map for all $t\in I$. That is, there exists a function $\lambda:I\rightarrow\Re$ such that$$\Huge -d_{\underline{\alpha}(t)}\underline{N}(\underline{\alpha}'(t))=-(\underline{N}\circ\underline{\alpha})'(t)=\lambda(t)\underline{\alpha}'(t)$$and $\lambda(t)$ is a principle curvature of $S$ at $\underline{\alpha}'(t)\in S$.

Let us discuss the situation near any $\underline{p}\in S$ that is not umbilic. We can then choose a small neighbourhood $V\subset S$ of $\underline{p}$ which still contains no umbilic points and two distinct eigenvalues $\kappa_1,\kappa_2:V\rightarrow\Re$ of the Weingarten map. Since the map is symmetric, the corresponding eigenvectors are perpendicular. This gives rise to two local families of curves, all of which are lines of curvatures, such that any curve of the first family meets any curve of the second perpendicularly at any intersection. 

Lines of curvature satisfy a particular ODE in coordinates of a local parametrisation. Let $E,\dots, N:U\rightarrow\Re$ be the coefficients of the first and second fundamental form of a local parametrisation $\underline{x}:U\rightarrow S$ of a regular surface $S\subset\Re^3$. A smooth curve $\underline{\alpha}:I\rightarrow S$ with $\underline{\alpha}(t)=\underline{x}(u(t),v(t))$ is a line of curvature if and only if$$\Huge\begin{vmatrix}(v')^2 & -u'v' & (u')^2 \\ E & F & G \\ L & M & N\end{vmatrix}=0$$with $E,\dots,N$ viewed along the curve $(u(t),v(t))$. Proof:
> We conclude from the definition of $\underline{\alpha}$ that$$\Huge\underline{\alpha}'=u'\underline{x}_u+v'\underline{x}_v$$, $\underline{\alpha}$ is a line of curvature if and only if$$\Huge -d_\underline{\alpha}\underline{N}(u'\underline{x}_u+v'\underline{x}_v)=\lambda(u'\underline{x}_u+v'\underline{x}_v)$$for some $\lambda$.
> We now use the matrix representation of the Weingarten map in terms of our basis, so our IFF translates to:$$\Huge\frac{1}{EG-F^2}\begin{pmatrix}GL-FM & GM-FN \\ -FL+EM & -FM+EN\end{pmatrix}\begin{pmatrix}u' \\ v'\end{pmatrix}=\lambda\begin{pmatrix}u' \\ v'\end{pmatrix}$$
> Since $\lambda$ is arbitrary and $EG-F^2\neq0$, this is equivalent to the condition that $(a,b)$ (LHS vector) is a multiple of $(u',v')$. That is $av'=bu'$, which we write as$$\large\begin{align*}
((GL-FM)u'+(GM-FN)v')v'&=((-FL+EM)u'+(-FM+EN)v')u'\\
\iff(EM-FL)(u')^2+(-FM+EN&-GL+FM)u'v'+(FN-GM)(v')^2=0\\
\iff(EM-GL)(u')^2+(EN-GL)&u'v'+(FN-GM)(v')^2=0
\end{align*}$$
> This can be written as$$\large (v')^2\begin{vmatrix}F & G \\ M & N\end{vmatrix}-(-u'v')\begin{vmatrix}E & G \\ L & N\end{vmatrix}+(u')^2\begin{vmatrix}E & F \\ L & M\end{vmatrix}=\begin{vmatrix}(v')^2 & -u'v' & (u')^2 \\ E & F & G \\ L & M & N\end{vmatrix}$$as required.

Let $\underline{x}:U\rightarrow S$ be a principal parametrisation of a surface $S\subset\Re^3$ with Gauss map $\underline{N}:S\rightarrow S^2$. That is we take $F=M=0$, then the coordinate curves are lines of curvature. Proof:
> For curves $u(t)=(t,v_0),v(t)=(u_0,t)$, $u'v'=0$ is satisfied and since $F=M=0$ we have$$\Huge\begin{vmatrix}(v')^2 & -u'v' & (u')^2 \\ E & F & G \\ L & M & N\end{vmatrix}=\begin{vmatrix}(v')^2 & 0 & (u')^2 \\ E & 0 & G \\ L & 0 & M\end{vmatrix}=0$$, implying that both coordinate curves $\underline{x}(t,v_0)$ and $\underline{x}(u_0,t)$ are lines of curvature.

Note that the converse is true in the sense that if $\underline{x}$ is a principal parametrisation and if umbilic points on $S$ are isolated, then the only lines of curvature are coordinate curves.

A curve $\underline{\alpha}:I\rightarrow S$ on a regular surface $S\subset\Re^3$ is called an asymptotic curve if its normal curvature vanishes identically, $\kappa_n=0$. These curves have the following properties:
> A unit speed curve is asymptotic if and only if:$$\Huge \underline{\alpha}''(s)\cdot\underline{N}(\underline{\alpha}(s))=0$$
> It follows from Meusnier's Theorem that $\underline{\alpha}$ is an asymptotic curve if and only if $\underline{II}_{\underline{\alpha}(s)}(\underline{\alpha}'(s))=0$.
> It follows from the previous fact that a curve $\underline{\alpha}(s)=\underline{x}(u(s),v(s))$ is an asymptotic curve if and only if $$\Huge (u')^2L+2u'v'M+(v')^2N=0$$, indeed we have $\underline{\alpha}'=u'\underline{x}_u(u,v)+v'\underline{x}_v(u,v)$ and:$$\Huge \underline{II}_{\underline{\alpha}(\cdot)}(\underline{\alpha}')=u'^2L(u,v)+2u'v'M(u,v)+v'^2N(u,v)$$

We know that we can write$$\Huge\underline{II}_\underline{p}(\cos\theta X_1+\sin\theta X_2)=\kappa_1(\underline{p})\cos^2\theta+\kappa_2(\underline{p})\sin^2\theta$$where $X_1,X_2\in T_\underline{p}S$ is an orthonormal basis of eigenvectors of the Weingarten map. In order to have $\underline{II}_{\underline{\alpha}(s)}(\underline{\alpha}'(s))=0$ (making the curve asymptotic), the principle curvatures $\kappa_1,\kappa_2$ cannot have the same sign. That is we must have $K(\underline{p})=\kappa_1(\underline{p})\kappa_2(\underline{p})\leq0$. Therefore asymptotic curves only exist in hyperbolic or flat regions of a regular surface $S\subset\Re^3$.

Moreover if $S\subset\Re^3$ contains a straight Euclidean line, then its normal curvature vanishes along the line. Such a line is therefore an asymptotic curve of the surface. This holds in particular for lines in a ruled surface.

Let us consider a few examples:
> Consider the surface of revolution obtained from a catenoid. Let $S\subset\Re^3$ be the regular surface obtained by rotating a regular curve, $\underline{\alpha}(v)=(f(v),0,g(v)),v\in I$ with $f(v)>0$ and $I$ an open interval, around the $z$-axis with local parametrisation given by $\underline{x}:(0,2\pi)\times I\rightarrow S$:$$\Huge \underline{x}(u,v)=(f(v)\cos u,f(v)\sin u,g(v))$$
> We saw that $E=f^2,F=0,G=||\underline{\alpha}'||^2$ and:$$\Huge L=-\frac{fg'}{||\underline{\alpha}'||},\,\,M=0,\,\,N=\frac{f''g'-f'g''}{||\underline{\alpha}'||}$$In particular, this local parametrisation is principal and therefore the coordinate curves$$\Huge\begin{align*}
u&\rightarrow (f(v_0)\cos u,f(v_0)\sin u,g(v_0))\\
v&\rightarrow (f(v)\cos u_0,f(v)\sin u_0,g(v))
\end{align*}$$are lines of curvature. Note that these correspond to the parallels ($u$) and meridians ($v$) of the surface $S$. The asymptotic curves of $S$ are curves $\underline{\alpha}$ satisfying $$\large -f(v(t))g'(v(t))(u'(t))^2=(f'(v(t))g''(v(t))-f''(v(t))g'(v(t)))(v'(t))^2$$
> In the case of a catenoid, we have $f(v)=\cosh(v),g(v)=v$ and therefore we find $u'(t)=\pm v'(t)$. Choosing $v(t)=t$ we obtain $u(t)=\pm t+c$.

We see that lines of curvature bisect the angle between asymptotic curves. Moreover, asymptotic curves intersect each other perpendicularly if and only if the surface is minimal. This is the case for our catenoid. 

Recall that we required non-positive Gauss curvature for the existence of asymptotic curves. An interesting surface to study will then be the hyperbolic paraboloid, as this has negative Gauss curvature and is not minimal:
> The hyperbolic paraboloid is given by $S=\{\underline{x}\in\Re^3:z=xy\}$ and is parametrised by $\underline{x}(u,v)=(u,v,uv)$. We define $D=\sqrt{1+u^2+v^2}$ and write$$\Huge \underline{x}_u=(0,1,v),\,\,\underline{x}_v=(1,0,u),\,\,\underline{N}(\underline{x})=\frac{1}{D}(-v,-u,1)$$and further:$$\Huge \underline{x}_{uu}=(0,0,0),\,\,\underline{x}_{uv}=(0,0,1),\,\,\underline{x}_{vv}=(0,0,0)$$We can then calculate the coefficients of the first and second fundamental forms:$$\Huge\begin{align*}
E=1+v^2&,\,\,F=uv,\,\,G=1+u^2\\
L&=\underline{x}_{uu}\cdot\underline{N}(\underline{x})=0\\
M&=\underline{x}_{uv}\cdot\underline{N}(\underline{x})=\frac{1}{D}\\
N&=\underline{x}_{vv}\cdot\underline{N}(\underline{x})=0
\end{align*}$$
> Plugging these into our determinant formula for determining lines of curvature gives:$$\Huge\begin{align*}
0&=\begin{vmatrix}(v')^2 & -u'v' & (u')^2\\
E & F & G\\
L & M & N\end{vmatrix}\\
&=\begin{vmatrix}(v')^2 & -u'v' & (u')^2\\
1+v^2 & uv & 1+u^2\\
0 & \frac{1}{D} & 0\end{vmatrix}\\
&=-\frac{1}{D}((1+u^2)(v')^2-(1+v^2)(u')^2)
\end{align*}$$
> We can solve this using separation of variables$$\Huge \frac{u'}{\sqrt{1+v^2}}=\pm\frac{v'}{\sqrt{1+u^2}}$$, which we integrate to get:$$\Huge \text{arcsinh}(v(t))=c\pm\text{arcsinh}(u(t))$$
> Lines of curvature are then given by$$\Huge x(u(t),v(t))=\begin{cases}(\sinh(t),\sinh(c+t),\sinh(t)\sinh(c+t)) \\
(\sinh(t),\sinh(c-t),\sinh(t)\sinh(c-t))\end{cases}$$for any $c\in\Re$. The equation for asymptotic curves then yields$$\Huge 0=(u')^2L+2u'v'M+(v')^2N=\frac{2}{D}u'v'$$, so we see that coordinate curves $u\rightarrow\underline{x}(u,v_0),v\rightarrow\underline{x}(u_0,v)$ are asymptotic curves.