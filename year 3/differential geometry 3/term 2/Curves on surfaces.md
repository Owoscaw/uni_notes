
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
# Asymptotic curves and lines of curvature