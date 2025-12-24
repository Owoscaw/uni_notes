
We aim to introduce the notion of a smooth map $f:S\rightarrow\Re^n$ from a [[Surfaces in R3|surface]] $S\subset\Re^3$ into $\Re^n$. The problem here is that it is not clear how we define smoothness of functions that are only defined on subsets of $\Re^3$ if they are lower dimensional and curved.

# Smooths maps on surfaces:

Recall that a map $f:U\rightarrow\Re^m$ with an open set $U\subset\Re^n$ is called smooth at a point $\underline{p}\in U$ if all of its component-wise partial derivatives are continuous at $\underline{p}$. It is important that $U$ is open to define this as then the curves $t\rightarrow\underline{p}+t\underline{e}_i$ lie inside $U$ for $|t|$ small enough.

In the case of a surface $S\subset\Re^3$ and a map $f:S\rightarrow\Re^m$, the set $S$ is not necessarily an open subset of $\Re^3$ and it is not clear how we can define smoothness at $\underline{p}\in S$. To remedy this, note that we always have a local parametrisation $\underline{x}:U\rightarrow S$ with $\underline{p}\in\underline{x}(U)$. We can use this local parametrisation to describe a neighbourhood around $\underline{p}$ in the surface by an open set in $\Re^2$, coinciding with $U$. 

Let $S\subset\Re^3$ be a regular surface and $\underline{p}\in S$. We call a map $f:S\rightarrow\Re^m$ smooth at $\underline{p}\in S$ if there exists a local parametrisation $\underline{x}:U\rightarrow S$ with $\underline{p}\in\underline{x}(\underline{q})$ and $\underline{q}\in U$ such that the composition $f\circ\underline{x}:U\rightarrow\Re^m$ is smooth at $\underline{q}$:![[Smooth maps between surfaces 2025-12-22 19.03.50.excalidraw]]
It is natural to ask if this definition is independent of local parametrisation:
> Let $V=\underline{x}(U)$ and $\tilde V=\tilde{\underline{x}}(\tilde U)$. We know that the [[Surfaces in R3#Change of parametrisations|change of parametrisation]] given by:$$\Huge h=\underline{x}^{-1}\circ\tilde{\underline{x}}:\tilde{\underline{x}}^{-1}(V\cap\tilde V)\rightarrow\underline{x}^{-1}(V\cap\tilde V)$$is a diffeomorphism, so we write:$$\Huge f\circ\tilde{\underline{x}}=(f\circ\underline{x})\circ h:\tilde{\underline{x}}^{-1}(V\cap\tilde V)\rightarrow\Re^m$$Note that $h$ is smooth at $\tilde{\underline{q}}$ and $f\circ\underline{x}$ is smooth at $\underline{q}=h(\tilde{\underline{q}})$ by assumption. Then $f\circ\tilde{\underline{x}}$ is also smooth at $\tilde{\underline{q}}$ as it is a composition of smooth maps.

## Gauss map:
We now introduce the Gauss map of a surface as a map that assigns a unit normal to every point on a surface. Let $S\subset\Re^3$ be a regular surface and $W\subset S$. A Gauss map of the surface $S$ is a smooth map $N:W\rightarrow\Re^3$ which assigns every point $\underline{p}\in S$ a unit normal vector $N(\underline{p})$, that is $N(\underline{p})\perp$[[Tangent planes#Definition|$T_{\underline p}S$]]. Therefore we have a map $N:W\rightarrow S^2$, where $S^2\subset\Re^3$ is the unit sphere centered at the origin.

Note that if $N:W\rightarrow S^2$ is a Gauss map of $S$ then $-N:W\rightarrow S^2$ with $\underline{p}\rightarrow -N(\underline{p})$ is also a Gauss map of $S$. Such a Gauss map can always be defined in the following way, given a local parametrisation $\underline{x}:U\rightarrow S$ and $\underline{p}\in\underline{x}(U)$:$$\Huge(N\circ\underline{x})(u,v)=\frac{\underline{x}_u\times\underline{x}_v}{||\underline{x}_u\times\underline{x}_v||}(u,v)$$This is well defined as $\underline{x}_u,\underline{x}_v$ will always be linearly independent, which also makes the map smooth. Moreover, $N(\underline{p})\perp T_{\underline{p}}S$ as $\underline{x}_u,\underline{x}_v$ span the tangent plane and $N(\underline{p})$ is defined in terms of their cross product, producing a perpendicular vector.

While this is well defined on $\underline{x}(U)\subset S$, we may not be able to find a smooth map on all of $S$. This problem has to do with the orientability of a surface, and we will see that a non-orientable surface like the Mobius strip does not admit a globally defined Gauss map. Take for example:
> The graph of a function defined as the surface $S=\{(u,v,g(u,v)):(u,v)\in U\}$ with an open set $U\subset\Re^2$ and a smooth function $g:U\rightarrow\Re$. A global parametrisation of $S$ is given by $\underline{x}(u,v)=(u,v,g(u,v))$ and we have:$$\Huge\begin{align*}
\underline{x}_u(u,v)&=\left(1,0,\frac{\partial g}{\partial u}(u,v)\right),\,\,\underline{x}_v(u,v)=\left(0,1,\frac{\partial g}{\partial v}(u,v)\right)\\
\implies(\underline{x}_u\times\underline{x}_v)(u,v)&=\left(-\frac{\partial g}{\partial u}\left(u,v\right),-\frac{\partial g}{\partial v}(u,v),1\right)\\
\implies N\circ\underline{x}&=\frac{1}{\sqrt{1+(\frac{\partial g}{\partial u})^2+(\frac{\partial g}{\partial v})^2}}\left(-\frac{\partial g}{\partial u},-\frac{\partial g}{\partial v},1\right)
\end{align*}$$

A surface $S\subset\Re^3$ is called non-orientable if there exists no global Gauss map $N:S\rightarrow S^2$, that is we cannot define the map $N$ to be continuous on all of $S$. If $S$ admits a global Gauss map, we call it orientable.

Take for example the Mobius strip. We construct this topologically as follows: take a rectangle, twist it once and stitch the ends together. The resulting object is a Mobius strip, which we can parametrise as a [[Surfaces in R3#Ruled|ruled surface]]. Take the curve:$$\Huge \underline{\alpha}(u)=(2\sin u,2\cos u,0)$$that parametrises a horizontal circle of radius $2$ in the $(x,y)$-plane. We then take a rotating unit vector in the $(x,z)$-plane that performs a half-rotation on $[0,2\pi]$:$$\Huge u\rightarrow(-\sin(u/2),0,\cos(u/2))$$This unit vector rotates with our curve $\underline{\alpha}$ and determines the vector $\underline{w}:[0,2\pi]\rightarrow\Re^3$ with:$$\Huge \underline{w}(u)=\left(-\sin u\sin\left(\frac{u}{2}\right),-\cos u\cos\left(\frac{u}{2}\right),\cos\left(\frac{u}{2}\right)\right)$$The Mobius strip is then given by $\underline{x}:\Re\times(-1,1)\rightarrow\Re^3$ with:$$\Huge\begin{align*}
\underline{x}(u,v)&=\alpha(u)+v\underline{w}(u)\\
&=\left(\left(2-v\sin\left(\frac{u}{2}\right)\right)\sin u,\left(2-v\sin\left(\frac{u}{2}\right)\right)\cos u,v\cos\left(\frac{u}{2}\right)\right)
\end{align*}$$Then there is a clear discontinuity in the Gauss map at $(0,2,0)$.

## Other smooth maps:
Moving on from the Gauss map, we can look at two other smooth maps given a ruled surface $S\subset\Re^3$:
> The height function defined by fixing a vector $\underline{v}\subset S^2$ and defining a function $h:S\rightarrow\Re$ by:$$\Huge h(\underline{p})=\underline{p}\cdot\underline{v}$$Then $h$ is a smooth map that measures the height of $S$ in the $\underline{v}$ direction.
> The distance squared function defined by letting $\underline{a}\in\Re^3$:$$\Huge d^2(\underline{p})=||\underline{p}-\underline{a}||^2=(\underline{p}-\underline{a})\cdot(\underline{p}-\underline{a})$$Then $d^2$ is a smooth map where $d=\sqrt{d^2}$ measures the distance between $\underline{p}\in S$ and a reference point $\underline{a}\in\Re^3$.

# The derivative of smooth maps:

Recall the definition of the derivative of a smooth map $f:U\rightarrow\Re^m$ with an open set $U\subset\Re^n$ at a point $\underline{p}\in U$. The derivative is denoted as $d_\underline{p}f$, a linear map from $\Re^n$ to $\Re^m$. It is represented by the Jacobi matrix $J_\underline{p}f$. We know that a linear map $T:V\rightarrow W$ between vector spaces $V,W$ is fully determined by its action on a basis. That is, if $\underline{v}_1,\dots,\underline{v}_n\in V$ is a basis of $V$ and we have $T(\underline{v}_i)=\underline{w}_i$, then any vector $\underline{v}\in V$ can be uniquely written as a sum:$$\Huge T(\underline{v})=T\left(\sum_{i=1}^nc_i\underline{v}_i\right)=\sum_{i=1}^nc_iT(\underline{v}_i)=\sum_{i=1}^nc_i\underline{w}_i$$We will see that a smooth map $f:S_1\rightarrow S_2$ between regular surfaces $S_1,S_2\subset\Re^3$ allows for every $\underline{p}\in S_1$ a derivative $d_\underline{p}f$. Such derivative will be a linear map between the corresponding tangent planes of $S_1,S_2$. That is, $d_\underline{p}f:T_\underline{p}S_1\rightarrow T_{f(\underline{p})}S_2$. However we must first introduce the derivatives of more general smooth maps $f:S\rightarrow\Re^m$ where $S\subset\Re^3$ is a regular surface.

Let $S\subset\Re^3$ be a regular surface, $\underline{p}\in S$, and $\underline{x}:U\rightarrow S$ be a local parametrisation with $\underline{p}\in\underline{x}(U)$. Then the derivative of a smooth map $f:S\rightarrow\Re^m$ as the point $\underline{p}$ is a linear map:$$\Huge \begin{align*}
d_\underline{p}f&:T_\underline{p}S\rightarrow\Re^m\\
d_\underline{p}f(\underline{x}_u(\underline{q}))&=\frac{\partial }{\partial u}(f\circ\underline{x})(\underline{q})\in\Re^m\\
d_\underline{p}f(\underline{x}_v(\underline{q}))&=\frac{\partial }{\partial v}(f\circ\underline{x})(\underline{q})\in\Re^m
\end{align*}$$Note that this definition fully determines the linear map, as any vector $\underline{v}\in T_\underline{p}S$ can be written as a linear combination of the $u,v$ derivatives of $\underline{x}$. Letting $v\in T_\underline{p}S$ have form $\underline{v}=a\underline{x}_u(\underline{q})+b\underline{x}(\underline{q})$ we have:$$\Huge d_\underline{p}f(\underline{v})=ad_\underline{p}f(\underline{x}_u(\underline{q}))+b d_\underline{p}f(\underline{x}_v(\underline{q}))\in\Re^m$$We now show that this definition does not depend on local parametrisation:
> First we define the tangent plane as:$$\Huge T_\underline{p}S=\{\underline{\alpha}'(0):\underline{\alpha}:(-\epsilon,\epsilon)\rightarrow S\text{ is smooth with }\underline{\alpha}(0)=\underline{p}\}$$we will proceed to show that:$$\Huge d_\underline{p}f(\underline{\alpha}'(0))=(f\circ\underline{\alpha})'(0)$$This will show that $d_\underline{p}f(\underline{\alpha}'(0))$ only depends on $\underline{\alpha}$, not local parametrisation. Using the other definition shows that $d_\underline{p}f(\underline{\alpha}'(0))$ does not depend on the global structure of $\underline{\alpha}$, only on the tangent vector at $0$.
> Let $\underline{\alpha}:(-\epsilon,\epsilon)\rightarrow S$ be a smooth curve with $\underline{\alpha}(0)=\underline{p}$ and $\underline{x}:U\rightarrow S$ be a local parametrisation with $\underline{\alpha}((-\epsilon,\epsilon))\subset\underline{x}(U)$. Let $\underline{\beta}:(-\epsilon,\epsilon)\rightarrow U$ be such that $\underline{\alpha}=\underline{x}\circ\underline{\beta}$ and $\underline{\beta}(t)=(u(t),v(t))$. Let $\underline{q}=\underline{\beta}(0)$, implying that $\underline{x}(\underline{q})=\underline{\alpha}(0)=\underline{p}$. Then we have:$$\Huge \underline{\alpha}'(0)=(\underline{x}\circ\underline{\beta})'(0)=u'(0)\underline{x}_u(\underline{q})+v'(0)\underline{x}_v(\underline{q})\in T_\underline{p}S$$which shows that $\underline{\alpha}'(0)$ is a linear combination of basis vectors of the tangent plane. We proceed:$$\Huge\begin{align*}
(f\circ\underline{\alpha})'(0)&=((f\circ\underline{x})\circ\underline{\beta})'(0)\\
&=u'(0)\frac{\partial (f\circ\underline{x})}{\partial u}(\underline{q})+v'(0)\frac{\partial (f\circ\underline{x})}{\partial v}(\underline{q})\\
&=u'(0)d_\underline{p}f(\underline{x}_u(\underline{q}))+v'(0)d_\underline{p}f(\underline{x}_v(\underline{q}))\\
&=d_\underline{p}f(u'(0)\underline{x}_u(\underline{q})+v'(0)\underline{x}_v(\underline{q}))=d_\underline{p}(\underline{\alpha}'(0))
\end{align*}$$

We can finally move on to consider the derivative of smooth maps between surfaces. First note that if $\underline{\alpha}:(-\epsilon,\epsilon)\rightarrow S_1$ is a curve through $\underline{p}=\underline{\alpha}(0)\in S_1$ in the surface $S_1$, then $f\circ\underline{\alpha}:(-\epsilon,\epsilon)\rightarrow S_2$ is a curve through $f(\underline{p})=(f\circ\underline{\alpha})(0)\in S_2$ in the surface $S_2$. Therefore we have:$$\Huge d_\underline{p}f(\underline{\alpha}'(0))=(f\circ\underline{\alpha})'(0)\in T_{f(\underline{p})}S_2$$This shows that $d_\underline{p}f$ is actually a linear map between the tangent vector space of each surface:$$\Huge d_\underline{p}f:T_\underline{p}S_1\rightarrow T_{f(\underline{p})}S_2,,\,\underline{\alpha}'(0)\rightarrow (f\circ\underline{\alpha})'(0)$$

Note that the Gauss map can be considered a smooth map between surface, and therefore acts in this way:$$\Huge d_\underline{p}N:T_\underline{p}N\rightarrow T_{N(\underline{p})}S^2$$Noting that $N(\underline{p})\perp T_\underline{p}S$ we also have $N(\underline{p})\perp T_{N(\underline{p})}S^2$, implying that $T_\underline{p}S=T_{N(\underline{p})}S^2$:$$\Huge \implies d_\underline{p}N:T_\underline{p}S\rightarrow T_\underline{p}S$$That is, $d_\underline{p}N$ is a linear map of the tangent plane $T_\underline{p}S$ onto itself:![[Smooth maps between surfaces 2025-12-22 20.57.35.excalidraw]]
As the chain rule was fundamental in many of our proofs, it makes sense that the chain rule also holds for the derivative of maps between smooth surfaces. Let $S_1,S_2,S_3\subset\Re^3$ be regular surfaces and $f:S_1\rightarrow S_2,g:S_2\rightarrow S_3$ be smooth maps. Then the composition $g\circ f:S_1\rightarrow S_3$ is also a smooth map and for all $\underline{p}\in S_1$:$$\Huge d_\underline{p}(g\circ f)=d_{f(\underline{p})}g\circ d_{\underline{p}}f:T_\underline{p}S_1\rightarrow T_{g(f(\underline{p}))}S_3$$Proof:
> Let $\underline{v}\in T_\underline{p}S_1$. Then there exists a smooth curve $\underline{\alpha}:(-\epsilon,\epsilon)\rightarrow S_1$ with $\underline{\alpha}(0)=\underline{p}$ and $\underline{\alpha}'(0)=\underline{v}$. Then $f\circ\underline{\alpha}:(-\epsilon,\epsilon)\rightarrow S_2$ is a smooth curve in $S_2$ and we have:$$\Huge\begin{align*}
d_\underline{p}(g\circ f)(\underline{v})&=d_\underline{p}(g\circ f)(\underline{\alpha}'(0))\\
&=((g\circ f)\circ\underline{\alpha})'(0)\\
&=(g\circ(f\circ\underline{\alpha}))'(0)\\
&=d_{f(\underline{p})}g((f\circ\underline{\alpha}))'(0)\\
&=d_{f(\underline{p})}(d_\underline{p}f(\underline{\alpha}'(0)))\\
&=d_{f(\underline{p})}(d_\underline{p}(\underline{v}))=(d_{f(\underline{p})}g\circ d_\underline{p}f)(\underline{v})
\end{align*}$$Completing the proof.

Take for example the sphere and ellipsoid. Let $S^2\subset\Re^3$ denote the unit sphere at the origin. For $a,b,c>0$ let:$$\Huge S=f^{-1}(1)\subset\Re^3,\,\,f(x,y,z)=(x/a)^2+(y/b)^2+(z/c)^2$$be the corresponding ellipsoid. Consider the map $F:S^2\rightarrow S$ given by $F(x,y,z)=(ax,by,cz)$, a linear map which can also be viewed as $F:\Re^3\rightarrow\Re^3$ in the ambient space. The derivative of $F$ as a map in the ambient space is also linear and we have:$$\Huge d_\underline{p}F(\underline{v})=d_\underline{p}F(v_1,v_2,v_3)=(av_1,bv_2,cv_3)$$for $\underline{v}=(v_1,v_2,v_3)\in\Re^3$. We proceed to verify the restriction of $d_\underline{p}F$ to the tangent space $T_\underline{p}S^2$ is a linear map from $T_\underline{p}S^2$ to $T_{F(\underline{p})}S$. Indeed we have for $\underline{p}=(x,y,z)\in S^2$ that $F(\underline{p})=(ax,by,cz)$ and:$$\Huge T_\underline{p}S=\underline{\nabla}f(\underline{q})^\perp=\{\underline{w}\in\Re^3:\underline{w}\cdot\underline{\nabla}f(\underline{q)}=0\}$$Since $\underline{\nabla}f=2(x/a^2,y/b^2,z/c^2)$ we have:$$\Huge \underline{\nabla}f(F(\underline{p}))=\underline{\nabla}f(ax,by,cz)=2(x/a,y/b,z/c)$$And therefore:$$\Huge\begin{align*}
T_{F(\underline{p})}S&=\{\underline{w}\in\Re^3:\underline{w}\cdot\underline{\nabla}f(F(\underline{p}))=0\}\\
&=\left\{(w_1,w_2,w_3)\in\Re^3:\frac{w_1x}{a}+\frac{w_2y}{b}+\frac{w_3z}{c}=0\right\}
\end{align*}$$Now if $\underline{v}=(v_1,v_2,v_3)\in T_\underline{p}S^2$ then $\underline{v}\cdot\underline{p}=0$. Then:$$\Huge (w_1,w_2,w_3)=d_\underline{p}F(v_1,v_2,v_3)=(av_1,bv_2,cv_3)$$and we conclude:$$\Huge \underline{w}\cdot\underline{\nabla}f(F(\underline{p}))=2\left(\frac{w_1x}{a}+\frac{w_2y}{b}+\frac{w_3z}{c}\right)=2(v_1x+v_2y+v_3z)=0$$confirming that $\underline{w}\in T_{F(\underline{p})}S$.

# Isometries and conformal maps:

We now consider a family of maps between regular surfaces:
> Isometries are maps that preserve the length of tangent vectors and angles between them. In this case, an isometry $f:S_1\rightarrow S_2$ preserves the intrinsic geometry of both surfaces, however they may be embedded into $\Re^3$ differently.
> Conformal maps preserve only angles.

Let us consider an example to show that intrinsic geometry is preserved. Let $S_1\subset\Re^3$ be the subset $(0,2\pi)\times\Re\times\{0\}$, clearly a regular surface. Let $S_2\subset\Re^3$ be the cylinder with the vertical line $\{(1,0,v)\in\Re^3:v\in\Re\}$ removed, that is $S_2=\{(\cos u,\sin u,v):u\in(0,2\pi),v\in\Re\}$. Let $f:S_1\rightarrow S_2$ be given by $f(u,v,0)=(\cos u,\sin u,v)$. Then for any smooth curve $\underline{\alpha}:[a,b]\rightarrow S$ with $\underline{\alpha}(t)=(u(t),v(t),0)$ we have:$$\large L(\underline{\alpha})=\int_a^b||\underline{\alpha}'(t)||_{\underline{\alpha}(t)}dt=\int_a^b||(u',v',0)||dt=\int_a^b\sqrt{(u'(t))^2+(v'(t))^2}dt$$and:$$\Huge\begin{align*}
L(f\circ\underline{\alpha})&=\int_a^b||(f\circ\underline{\alpha})'(t)||_{f\circ\underline{\alpha}(t)}dt\\
&=\int_a^b||(-u'\sin u,u'\cos u,v')||dt\\
&=\int_a^b\sqrt{(u'(t))^2+(v'(t))^2}dt
\end{align*}$$So we see that $L(\circ\underline{\alpha})=L(\underline{\alpha})$, length is preserved under $f$. We now introduce the family of maps that preserve intrinsic geometry.

## Isometries:
A smooth map $f:S_1\rightarrow S_2$ between regular surfaces $S_1,S_2\subset\Re^3$ is called a local isometry if we have:$$\Huge \langle d_\underline{p}f(\underline{v}_1),d_\underline{p}f(\underline{v}_2)\rangle_{f(\underline{p})}=\langle \underline{v}_1,\underline{v}_2\rangle_\underline{p}$$for all $\underline{p}\in S_1$ and $\underline{v}_1,\underline{v}_2\in T_\underline{p}S_1$. If $f$ is a local isometry and also a diffeomorphism, then $f$ is called an isometry and $S_1,S_2$ are isometric to each other.

We can verify that our example above is an isometry using this definition. It is clear that $f$ is a diffeomorphism. Moreover for all $\underline{p}=(u,v,0)\in S_1=(0,2\pi)\times\Re\times\{0\}$ we have:$$\Huge T_\underline{p}S_1=\Re^2\times\{0\}$$Let $\underline{v}=(a,b,0)\in T_\underline{p}S_1$, then we have:$$\Huge\begin{align*}
d_\underline{p}f(\underline{v})&=\frac{d}{dt}f(\underline{p}+t\underline{v})|_{t=0}\\
&=\frac{d}{dt}f(u+ta,v+tb,0)|_{t=0}\\
&=\frac{d}{dt}(\cos(u+ta),\sin(u+ta),v+tb)|_{t=0}\\
&=(-a\sin u,a\cos u,b)\in T_{f(\underline{p})}S_2
\end{align*}$$Therefore:$$\large\begin{align*}
\langle d_\underline{p}f(a_1,b_1,0),d_\underline{p}f(a_2,b_2,0)\rangle_{f(\underline{p})}&=\langle (-a\sin u,a\cos u,b),(-a\sin u,a\cos u,b)\rangle_{f(\underline{p})}\\
&=a_1a_2+b_1b_2\\
&=(a_1,b_1,0)\cdot(a_2,b_2,0)\\
&=\langle (a_1,b_1,0),(a_2,b_2,0)\rangle_{\underline{p}}
\end{align*}$$So we indeed have a local isometry. Note that the map $f$ is not a bijection, so the map is not a global isometry and $S_1,S_2$ are not isometric.

Let $f:S_1\rightarrow S_2$ be a smooth map between regular surfaces $S_1,S_2\subset\Re^3$ and $\underline{x}:U\rightarrow S_1$ be a local parametrisation. Then the restriction of $f$ to $\underline{x}(U)\subset S_1$ is a local isometry if and only if:$$\Huge \langle f_u,f_u\rangle_{f\circ\underline{x}}=E,\,\,\langle f_u,f_v\rangle_{f\circ\underline{x}}=F,\,\,\langle f_v,f_v\rangle_{f\circ\underline{x}}=G$$where $E,F,G$ are the coefficients of the [[Tangent planes#First fundamental form|first fundamental form]] of $S_1$ wrt $\underline{x}$. We prove this as follows:
> Firstly we assume that $f$ is a local isometry on $\underline{x}(U)\subset S_1$. Then we have for $\underline{p}=\underline{x}(\underline{q})$:$$\Huge\begin{align*}
d_\underline{p}f(\underline{x}_u(\underline{q}))&=\frac{\partial (f\circ\underline{x})}{\partial u}(\underline{q})=f_u(\underline{q})\\
d_\underline{p}f(\underline{x}_v(\underline{q}))&=\frac{\partial (f\circ\underline{x})}{\partial v}(\underline{q})=f_v(\underline{q})
\end{align*}$$
> Now using the definition of a local isometry we obtain:$$\Huge\begin{align*}
\langle f_u(\underline{q}),f_v(\underline{q})\rangle_{f(\underline{p})}&=\langle d_\underline{p}f(\underline{x}_u(\underline{q})),d_\underline{p}f(\underline{x}_v(\underline{q}))\rangle_{f(\underline{p})}\\
&=\langle \underline{x}_u(\underline{q}),\underline{x}_v(\underline{q})\rangle_\underline{p}=F(\underline{q})
\end{align*}$$with similar derivations for $E,G$. This proves the forward implication.
> Now for the converse, assume that we have the coefficients of the first fundamental form as above. Now we let:$$\Huge \underline{w}_1=a_1\underline{x}_u(\underline{q})+b_1\underline{x}_v(\underline{q}),\,\,\underline{w}_2=a_2\underline{x}_u(\underline{q})+b_2\underline{x}_v(\underline{q})\in T_\underline{p}S_1$$Then we compute:$$\large \begin{align*}
\langle d_\underline{p}f(\underline{w}_1),d_\underline{p}f(\underline{w}_2)\rangle_{f(\underline{p})}&=a_1a_2\langle f_u,f_u\rangle+(a_1b_2+a_2b_1)\langle f_u,f_v\rangle+b_1b_2\langle f_v,f_v\rangle\\
&=a_1a_2 E(\underline{q})+(a_1b_2+a_2b_1)F(\underline{q})+b_1b_2G(\underline{q})\\
&=\langle a_1\underline{x}_u(\underline{q})+b_1\underline{x}_v(\underline{q}),a_2\underline{x}_u(\underline{q})+b_2\underline{x}_v(\underline{q})\rangle_{\underline{p}}\\
&=\langle \underline{w}_1,\underline{w}_2\rangle_\underline{p}
\end{align*}$$

Remarks:
>Note that if $f:S_1\rightarrow S_2$ is a diffeomorphism between $\underline{x}(U)\subset S_1$ and $f(\underline{x}(U))\subset S_2$, then one can verify that $\underline{y}=f\circ\underline{x}:U\rightarrow S_2$ is also a local parametrisation of $S_2$. In this case we have $\underline{y}_u=f_u,\underline{y}_v=f_v$ and the isometry iff statement translates to:$$\Huge E_\underline{x}=E_\underline{y},\,\,F_\underline{x}=F_\underline{y},\,\,G_\underline{x}=G_\underline{y}$$where $E_\underline{x},E_\underline{y},\dots$ are the first fundamental forms wrt to $\underline{x},\underline{y}$ respectively.
> Since the quadratic form $\underline{I}_\underline{p}:T_\underline{p}S\rightarrow\Re$ fully determines the bilinear form $\langle \cdot,\cdot\rangle_\underline{p}:T_\underline{p}S\times T_\underline{p}S\rightarrow\Re$, one can verify that a smooth map $f:S_1\rightarrow S_2$ is an isometry through the condition:$$\Huge \underline{I}_{f(\underline{p})}^{S_2}(d_\underline{p}\underline{v})=\underline{I}_\underline{p}^{S_1}(\underline{v})$$for all $\underline{p}\in S_1,\underline{v}\in T_\underline{p}S$.
> A natural way to define distance between two points $\underline{p}_1,\underline{p}_2\in S$ of a connected regular surface $S$ is as follows:$$\large d_S(\underline{p}_1,\underline{p}_2)=\inf\{L(\underline{\alpha}):\underline{\alpha}:[0,1]\rightarrow S\text{ is smooth},\underline\alpha(0)=\underline{p}_1,\underline{\alpha}(1)=\underline{p}_2\}$$While isometries preserve lengths of individual curves, they may not preserve distance between two points. However if we have a global isometry $f:S_1\rightarrow S_2$ between connected regular surfaces $S_1,S_2\subset\Re^3$, then we have for any pair $\underline{p}_1,\underline{p}_2\in S_1$:$$\Huge d_{S_2}(f(\underline{p}_1),f(\underline{p}_2))=d_{S_1}(\underline{p}_1,\underline{p}_2)$$
> A global isometry preserves all geometric properties.

Let us consider the example of an isometry between a helicoid and a catenoid. The helicoid $S_1$ is given by the equation $x\sin z=y\cos z$ and is globally parametrised by:$$\Huge\underline{x}_1(u,v)=(\sinh v\cos u,\sinh v\sin u,u)$$The catenoid $S_2$ is given by the equation $x^2+y^2=\cosh^2z$ and is parametrised by:$$\Huge \underline{x}_2(u,v)=(\cosh v\cos u,\cosh v\sin u,v)$$We then find the coefficients of the first fundamental forms wrt $\underline{x}_1,\underline{x}_2$ in both cases to be:$$\Huge E_1=E_2=\cosh^2v,\,\,F_1=F_2=0,\,\,G_1=G_2=\cosh^2v$$that is, both local parametrisations are [[Tangent planes#First fundamental form|isothermal]]. Moreover the map $f=\underline{x}_2\circ\underline{x}_1^{-1}:S_1\rightarrow S_2$ is a local isometry. This immediately follows from our first remark above when we restrict $S_1$ to one twist of the helicoid $S_1$ as this makes the map a diffeomorphism.

## Conformal maps:
Let $f:S_1\rightarrow S_2$ be a smooth map between regular surfaces $S_1,S_2\subset\Re^3$. The map $f$ is called conformal if there is some smooth function:$$\Huge \lambda:S_1\rightarrow(0,\infty)$$such that:$$\Huge \langle d_\underline{p}f(\underline{w}_1),d_\underline{p}f(\underline{w}_2)\rangle_{f(\underline{p})}=\lambda(\underline{p})^2\langle \underline{w}_1,\underline{w}_2\rangle_\underline{p}$$for all $\underline{p}\in S_1$ and $\underline{w}_1,\underline{w}_2\in T_\underline{p}S_1$. The function $\lambda$ is known as the conformal factor of the map. We call $f$ a conformal diffeomorphism if $f$ is both a conformal map and a diffeomorphism.

Note that a conformal map $f:S_1\rightarrow S_2$ with conformal factor $\lambda(\underline{p})=1$ for all $\underline{p}\in S_1$ is a local isometry and conformal diffeomorphisms with this property become global isometries. In this sense, conformal maps and diffeomorphisms are generalisations of local and global isometries.

Let $f:S_1\rightarrow S_2$ be a conformal map. Then $f$ preserves angles between tangent vectors. That is to say, for all $\underline{p}\in S_1$ and $\underline{w}_1,\underline{w}_2\in T_\underline{p}S_1$:$$\Huge \cos\angle(\underline{w}_1,\underline{w}_2)=\frac{\langle \underline{w}_1,\underline{w}_2\rangle_{\underline{p}}}{||\underline{w}_1||^2_\underline{p}\cdot||\underline{w}_2||^2_\underline{p}}=\cos\angle(d_\underline{p}f(\underline{w}_1),d_\underline{p}f(\underline{w}_2))$$Which we prove by computing:$$\Huge\begin{align*}
\cos\angle(d_\underline{p}f(\underline{w}_1),d_\underline{p}f(\underline{w}_2))&=\frac{\langle d_\underline{p}f(\underline{w}_1),d_\underline{p}f(\underline{w}_2)\rangle_{f(\underline{p})}}{\underline{I}_{f(\underline{p})}(d_\underline{p}f(\underline{w}_1))\cdot\underline{I}_{f(\underline{p})}(d_\underline{p}f(\underline{w}_2))}\\
&=\frac{\langle \underline{w}_1,\underline{w}_2\rangle}{\underline{I}_\underline{p}(\underline{w}_1)\cdot\underline{I}_\underline{p}(\underline{w}_2)}\\
&=\cos\angle(\underline{w}_1,\underline{w}_2)
\end{align*}$$as required.

Take the Gauss map as an example. We consider the catenoid, $S$, we previously considered with the parametrisation $\underline{x}(u,v)=(\cosh v\cos u,\cosh v\sin u,v)$. That is:$$\Huge S=\{\underline{x}(u,v):u\in[0,2\pi],v\in\Re\}$$Recall we found that the Gauss map of $S$ has form:$$\Huge N(\underline{x}(u,v))=\frac{1}{\cosh v}(\cos u,\sin u,-\sinh v)$$Here we have $N:S\rightarrow S^2$ where $S^2$ is the unit sphere at the origin. We show that $N$ is conformal with an equivalent definition; we look for a function $\lambda$ such that:$$\Huge \langle N_u,N_u\rangle_{N\circ\underline{x}}=\lambda^2E,\,\,\langle N_u,N_v\rangle_{N\circ\underline{x}}=\lambda^2F,\,\,\langle N_v,N_v\rangle_{N\circ\underline{x}}=\lambda^2G$$where $E,F,G$ are the coefficients of the first fundamental form of the catenoid $S$. We then find, using our previous computation of these coefficients:$$\Huge\begin{align*}
\langle N_u,N_u\rangle_\underline{x}&=\frac{1}{\cosh^2v}=\frac{1}{\cosh^4v}E\\
\langle N_u,N_v\rangle_\underline{x}&=0=\frac{1}{\cosh^4v}F\\
\langle N_v,N_v\rangle_\underline{x}&=\frac{1}{\cosh^4v}(\sinh^2v+1)=\frac{1}{\cosh^4v}G
\end{align*}$$So we find that $\lambda(u,v)=\frac{1}{\cosh^2v}$ and $N:S\rightarrow S^2$ is a conformal map.

Global isometries from a surface $S$ onto itself are of particular importance. It is clear that a composition of two such isometries is also an isometry and that the inverse of such isometries are also isometries. The same is true for conformal diffeomorphisms. If $f_1:S\rightarrow S$ and $f_2:S\rightarrow S$ are two conformal diffeomorphisms with conformal factors $\lambda_1,\lambda_2$ respectively, then $f_2\circ f_2:S\rightarrow S$ and $f_1^{-1}:S\rightarrow S$ are again conformal diffeomorphisms with conformal factors $\lambda_1\cdot\lambda_2$ and $\lambda_1^{-1}$ respectively.

Let $S$ be a regular surface. The set of all global isometries $f:S\rightarrow S$ as the structure of a [[Basics of groups|group]], such group is known as the isometry group of a regular surface, denoted as $\text{Iso}(S)$.

Take for example the isometry group of the Hyperbolic plane. Let $\mathbb{H}^2=\{z=u+iv\in\mathbb{C}:>0\}$ be the upper half complex plane model of the Hyperbolic plane with:$$\Huge \langle w_1,w_2\rangle_z=\frac{\Re(w_1\bar w_2)}{\Im^2(z)}$$for $z\in\mathbb{H}^2$ and $w_1,w_2\in T_z\mathbb{H}^2$. One can verify that the maps:$$\Huge f_A(z)=\frac{az+b}{cz+d}$$of [[Mobius transform|Mobius transformations]] corresponding to matrices $A=\begin{pmatrix}a & b \\ c & d\end{pmatrix}\in SL_2(\Re)$ are isometries of $\mathbb{H}^2$. These maps form a group as we have:$$\Huge (f_A)^{-1}=f_{A^{-1}},\,\,f_{AB}=f_A\circ f_B$$

### Conformal diffeomorphisms of $\Re^2$:
Recalling our learning from complex analysis, we saw that orientation preserving conformal maps between open sets in $\Re^2$ are [[Complex differentiation#Holomorphicity|holomorphic maps]] between the same open sets with $\Re^2$ in $\mathbb{C}$. Furthermore, orientation preserving conformal diffeomorphism are equivalent to biholomorphic maps.

The set of all biholomorphic maps in $\mathbb{C}$ are linear polynomials $f(z)=az+b$ with complex numbers $a,b\in\mathbb{C}$ with $a\neq0$. The conformal factor of $f$ is then $\lambda(z)=|a|$

