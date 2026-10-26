![[Manifolds and tensors 2026-10-25 01.18.02.excalidraw]]
# Introducing tensors:
In our quest to formulate straight lines, we could consider another [[Special relativity#Curves and $4$-vectors|vector]]-like object: the gradient of a function. This can be thought of as the normal to the surface $f=\text{constant}$. For a function $f(x^\mu)$, it's gradient $\partial_\mu f$ is a vector:$$\Huge\tilde\partial_\mu f=\frac{\partial x^\nu}{\partial \tilde x^\mu}\partial_\nu f$$Compared to a $4$-vector $(\tilde V^\mu=\frac{\partial \tilde x^\mu}{\partial x^\nu}V^\nu)$, we see that the gradient transforms in the opposite way. The set of all such vectors forms a vector space, called the cotangent space as it is the dual space to the tangent space. General elements in this space are called covectors. 

Given an element of the tangent space $\omega_\mu$ and an element of the cotangent space $V^\mu$, the product $\omega_\mu V^\mu$ is simply a scalar, independent of coordinates. We can therefore think of cotangent vectors as linear maps from vectors to numbers or visa versa. In order to form an invariant object from two tangent vectors, one must introduce the metric $\eta_{\mu\nu}$. We can also think of an inner product as defining a map from the vector space to its dual, for each tangent vector $W^\nu$ we can define its covector $\omega_\rho=\eta_{\rho\nu}W^\nu$.

If $\omega_\mu=\partial_\mu f$ and $V^\mu=\frac{dx^\mu}{d\lambda}$, the product$$\Huge V^\mu\omega_\mu=\frac{dx^\mu}{d\lambda}\partial_\mu f=\frac{df}{d\lambda}$$can be interpreted as the gradient of $f$ along the curve $x^\mu(\lambda)$. Both vectors and covectors transform linearly under coordinate transformations. Tensors are simply more general objects described in terms of a set of components that transform linearly under coordinate transformations.

Consider linear maps from the tangent space to itself in the most general sense, $W=T(V)$. Given a basis on the vector space, such maps can be represented by a matrix:$$\Huge W^\mu=T^\mu_\nu V^\nu$$This should be independent of basis, and therefore coordinates, so we require $\tilde W_\mu=\tilde T^\mu_\nu\tilde V^\nu$ for some matrix $\tilde T^\mu_\nu$. This implies:$$\Huge \tilde T^\mu_\nu=\frac{\partial \tilde x^\mu}{\partial x^\rho}T^\rho_\sigma\frac{\partial x^\sigma}{\partial \tilde x^\nu}$$As a consequence of this:$$\Large\begin{aligned}
\implies\tilde W^\mu&=\left(\frac{\partial \tilde x^\mu}{\partial x^\rho}T^\rho_\sigma\frac{\partial x^\sigma}{\partial \tilde x^\nu}\right)\left(\frac{\partial \tilde x^\nu}{\partial x^\beta}V^\beta\right)\\
&=\frac{\partial \tilde x^\mu}{\partial x^\rho}T^\rho_\sigma\delta^\sigma_\beta V^\beta\\
&=\frac{\partial \tilde x^\mu}{\partial x^\rho}(T^\rho_\sigma V^\sigma)=\frac{\partial \tilde x^\mu}{\partial x^\rho}W^\rho
\end{aligned}$$As required. In matrix notation, this is equivalent to $\tilde T=\Lambda T\Lambda^{-1}$. The index position is used to keep track of how an object transforms under coordinate transformations. For example, $T^\mu_\nu$ behaves like a vector in the upper index and like a covector in the lower index.
> Such objects are $[1,1]$ tensors ($1$ up index, $1$ down index)
> Vectors are $[1,0]$ tensors
> Covectors are $[0,1]$ tensors
> Scalars are $[0,0]$ tensors

These objects are so useful since they allow us to make coordinate-independent statements. Tensor equations are linear relations between components of tensors of same type. As these equations are independent of coordinate system, they are true in all coordinate systems if they are true in one. 

### Tensor equation rules:
> All quantities must be components of tensors
> The number and positions of free indices in each term must match so that tensorts of the same type are related (i.e. $V^\mu=\omega_\mu$ is not valid)
> Terms may have an arbitrary number of contracted indices, however must appear in pairs of up and down. That is, the sum implied by $V^\mu=T^\mu_\nu\lambda_\nu$ is invalid as $\lambda$ should have an upper $\nu$ index
> Indices may be renamed
> Order of tensors does not matter

# Manifolds:

We want to generalise flat spacetime geometry to consider smoothly curved geometries, characterised by the spacetime looking locally flat on small enough scales. We express this by saying that around every point, there is some coordinate system mapping some local neighbourhood of the point onto $\Re^n$. Therefore we must consider general coordinates, not necessarily ones adapted to inertial observers. By thinking of coordinates as a map from parts of spacetime to open regions of $\Re^n$, $x^\mu(p)$ can be thought of as collections of functions.

Special relativity had come coordinate system associated with inertial observers, in general relativity we move away from these coordinate systems - we do not assume the existence of coordinate systems integral to the theory. 

## Definition:
Let $n$ be a fixed positive integer. Given a set $M$, an $n$-dimensional chart on $M$ is a bijection $\varphi$ from a subset $U\subset M$ to an open subset $\varphi(U)\subset\Re^n$, defining coordinates $x^\mu(p)$ for each $p\in U$. An atlas for $M$ is a collection of charts $\{(U_a,\varphi_a)\}$ such that:
> $\bigcup_aU_a=M$, the charts cover the whole set
> If $U_a\cap U_b\neq\emptyset$, then the map $F=\varphi_a\circ\varphi_b^{-1}:\Re^n\rightarrow\Re^n(\tilde x^\mu(x^\nu))$ is differentiable where it is defined:![[Manifolds and tensors 2026-10-21 12.13.32.excalidraw]]


A maximal atlas is one containing all charts satisfying these conditions. An $n$-dimensional manifold ([[Differentiable Manifolds#Definition|differentiable manifold]]) is the set $M$ together with a maximal atlas. The coordinate map is always invertible where it is defined, so we can think of points $p$ as being determined by their coordinates $p(x^\mu)$. This is the formalisation of the notion that manifolds are spaces that "look like $\Re^n$". 

We can define a coordinate transformation where coordinate systems $x^\mu,\tilde x^\mu$ overlap, a map $\tilde x^\mu(x^\nu)$ from an open region in $\Re^n$ to another open region in $\Re^n$. For example:
> Take $M=\Re^2,U=M,\phi=\text{id}$ to define cartesian coordinates, which cover the whole set. A maximal atlas includes other coordinates, for example polar, related to cartesian coordinates $(x,y)$ by:$$\huge x=r\cos(\phi),\,\,y=r\sin(\phi)$$
> In our notation, the above is the inverse map $\varphi^{-1}$. The following is the map $\varphi$$$\huge r=\sqrt{x^2+y^2},\,\,\phi=\tan^{-1}(y/x)$$except at $x=y=0$. Note that polar coordinates are local coordinates, with a coordinate singularity at $r=0$. Therefore the map $(x,y)\to(r,\theta)$ is not differentiable at $r=0$, and these coordinates map $\Re^2\setminus\{x\geq0,y=0\}$ to the semi-infinite strip $\{r>0,0<\phi<2\pi\}$.
> Take $U=M=S^1$ as another example, we want to map this to the real line. Consider two different charts, one taking $S^1$ to $(0,2\pi)$ and the other taking $S^1$ to $(-\pi,\pi)$:![[Manifolds and tensors 2026-10-21 12.42.00.excalidraw]]
> Another example, taking $U=M=S^2$, is spherical polar coordinates in $\Re^3$. Taking $r=1$, we can define a coordinate system on $S^2$ at every point but the north pole - this is [[The complex plane and Riemann Sphere#The Riemann Sphere|stereographic projection]] of $S^2$ onto $\Re^2$.

The utility of this notation is that it defines a differentiable structure on the underlying set, that is, a notion of smoothness. Given a set $M$, we can define a function $f$ on $M$ as a map $f:M\rightarrow\Re,f:p\rightarrow f(p)$. If $M$ is a manifold, the charts define functions $f\circ\phi^{-1}:\Re^n\to\Re$, which send $x^\mu\to f(p(x^\mu))$. We say $f$ is differentiable function on $M$ if these functions $f\circ\phi^{-1}$ are differentiable where defined. By differentiability of $\tilde x^\mu(x^\nu)$, the notions of differentiability obtained from $f\circ\phi^{-1},f\circ\tilde\phi^{-1}$ agree on overlaps.

# Vectors, covectors, and tensors:

## Vectors:
In curved space, we define the [[Special relativity#Curves and $4$-vectors|tangent vector]] in terms of the directional derivative - giving a coordinate independent definition. We can then determine components wrt some coordinates from this definition:
> Given a curve $\gamma:\Re\to M,\gamma:\lambda\to p(\lambda)$, the tangent vector $V$ to $\gamma$ at $p$ is the derivative along the curve, $V=\frac{d}{d\lambda}$. This acts on functions on $M$, for a function $f:M\to\Re$ we have $f\circ\gamma:\Re\to\Re$, whose derivative is $V(f)=\frac{df}{d\lambda}$.
> Thus, at a point $p$, $V$ is a map from functions on $M$ to the reals. These are linear maps, allowing us to define addition of vectors by $(V+W)(f+g)=V(f)+V(g)+W(f)+W(g)$. This definition allows the vectors to form a vector space, which we nap the tangent space to $M$ at $p$, $T_p$.

The vectors are elements in the tangent space, not $M$ itself. If we embed the manifold in $\Re^n$, we can picture the tangent space as the tangent plane at the point $p$:![[Manifolds and tensors 2026-10-19 14.45.49.excalidraw]]

We can also define a vector field, a choice of vector $V\in T_p$ at each point $p\in M$, a vector-valued function on $M$. Note that while every vector $V\in T_p$ can be realised as the tangent vector to some curve through $p$, given a vector field $V(x^\mu)$, we will not in general be able to find a family of curves such that $V$ is tangent to the curves at every point. 

If we introduce coordinates, we can write $\gamma$ in terms of coordinates as $x^\mu(\lambda)$ (i.e. the composition $\phi\circ\gamma$) and find$$\huge V(f)=\frac{df}{d\lambda}=\frac{dx^\mu}{d\lambda}\frac{\partial f}{\partial x^\mu}$$by the chain rule. This is just the component expansion of an abstract vector:
> To illustrate this point, let us pick a coordinate system on $\Re^n$ and vary a single coordinate. The point $p(x^\mu)$ will trace out a curve in $M$, the image of our chosen coordinate axis. The tangents to these axes $\frac{\partial }{\partial x^\mu}$ are tangent vectors, defining a basis of $T_p$. 
> We can write $V=V^\mu\partial_\mu$, defining the components $V^\mu$ of $V$ wrt this basis, the above formula then dictates$$\huge V^\mu=\frac{dx^\mu}{d\lambda}=\dot x^\mu$$, as we would expect from our $\Re^n$ embedding.
> When we change coordinates to $\tilde x^\mu(x^\nu)$, we also change bases on $T_p$, so we have$$\huge V=V^\mu\frac{\partial }{\partial x^\mu}=\tilde V^\nu\frac{\partial }{\partial \tilde x^\nu}=\tilde V^\nu\frac{\partial x^\mu}{\partial \tilde x^\nu}\frac{\partial }{\partial x^\mu}$$, so the components of $V$ will transform by a change of basis under coordinate transformations:$$\huge\begin{aligned}
V^\mu&=\tilde V^\nu\frac{\partial x^\mu}{\partial \tilde x^\nu},\\
\tilde V^\mu&=\frac{d\tilde x^\mu}{d\lambda}\\
&=\frac{\partial \tilde x^\mu}{\partial x^\nu}\frac{d x^\nu}{d\lambda}=\frac{\partial \tilde x^\mu}{\partial x^\nu}V^\nu
\end{aligned}$$

Note that in our more general context, the coordinate transformation $\tilde x^\mu(x^\nu)$ is not in general linear, but the transformation of the tangent vector still is. A general vector can be given by specifying components $V^\mu(x^\nu)$ wrt the coordinate basis at each point. The relations between components of a vector in different coordinate systems will change as the point moves around a manifold, so it is not possible to equate vectors in different tangent spaces.

## Cotangent vectors:
Given a tangent space $T_p$, we define the cotangent space $T_p^*$ as the dual space. That is, $T_p^*$ is the space of linear maps $\omega:T_p\to\Re$. Linearity implies the map is characterised by its action on basis vectors:$$\Large \partial_\mu:\omega_\mu=\omega(\partial_\mu),\,\,\omega(V)=V^\mu\omega(\partial_\mu)=V^\mu\omega_\mu$$
Each $\omega$ is a cotangent vector (or covector);
> The prototypical example of a covector is the differential $df$ of a function $f$. $f$ naturally maps $V\in T_p$ to a real number $V(f)$, so we can think of defining $df\in T_p^*$ by $df(V)=V(f)$. 
> Component-wise we have $$\Large (df)_\mu=df(\partial_\mu)=\partial_\mu(f)=\partial_\mu f$$, i.e. the differential is a normal vector to the surface $f=\text{constant}$.

We can think of the coordinates as function $x^\mu$ on a manifold $M$, then the associated differentials $dx^\mu$ form a basis of $T_p^*$. We say such a basis is dual to the basis $\partial_\mu\in T_p$, i.e.:$$\huge dx^\nu(\partial_\mu)=\partial_\mu(x^\nu)=\delta^\nu_\mu$$
Our linear maps $\omega_\mu$ can then be thought of as the components of $\omega$ wrt this basis, i.e. if $\omega=\omega_\mu dx^\mu$ we can write$$\Large \omega(\partial_\mu)=\omega_\nu dx^\nu(\partial_\mu)=\omega_\nu\delta^\nu_\mu=\omega_\mu$$, reproducing our definition of $\omega_\mu$. 

Analogous to the tangent space, any element in $T_p^*$ can be written as the differential of some function. We can also define covector fields, however there will not generally exist a function such that a covector field is its differential. 

Under coordinate transformations:$$\Large\begin{aligned}
\omega=\omega_\nu dx^\nu&=\tilde \omega_\mu d\tilde x^\mu\\
&=\tilde\omega_\mu\frac{\partial \tilde x^\mu}{\partial x^\nu}dx^\nu\\
\implies\omega_\nu&=\tilde\omega_\mu\frac{\partial \tilde x^\mu}{\partial x^\nu}
\end{aligned}$$Note that this is linear, but opposite to vector transformation. Our action of a covector on a vector was defined with no reference to coordinates, so we expect $\omega_\mu V^\mu$ to be coordinate-independent:$$\Large\begin{aligned}
\tilde\omega_\nu\tilde V^\mu&=\frac{\partial x^\nu}{\partial \tilde x^\mu}\omega_\nu\frac{\partial \tilde x^\mu}{\partial x^\rho}V^\rho\\
&=\frac{\partial x^\nu}{\partial x^\rho}\omega_\nu V^\rho\\
&=\delta^\nu_\rho\omega_\nu V^\rho=\omega_\nu V^\nu
\end{aligned}$$
## Tensors:
Thinking of covectors as linear maps $T_p\to\Re$ and vectors $T^*_p\to\Re$, we define $V(\omega)=\omega(V)$. Let us generalise this notion to define a tensor of type $[r,s]$ at a point $p$ as a linear map:$$\huge T_{[r,s]}:(T_p^*)^r\times T_p^s\to\Re$$That is, a tensor takes $r$ covectors and $s$ vectors to a single real number. A type $[r,s]$ tensor field defines an $[r,s]$ tensor at each point. Note:
> Scalars are $[0,0]$ tensors
> Vectors are $[1,0]$ tensors
> Covectors are $[0,1]$ tensors
> Everything is a fucking tensor i guess

Since we defined tensors as linear maps, they are completely specified by their action on basis vectors. That is, tensors are characterised by their components:$$\Large T^{\mu_1\dots\mu_r}\,_{\nu_1\dots\nu_s}=T(dx^{\mu_1},\dots,dx^\mu_r,\partial_{\nu_1},\dots,\partial_{\nu_s})$$The action on a general set of vectors and covectors is given by contracting components of the tensor with the components of vectors/covectors:
> Take for example a $[1,1]$ tensor. This takes a vector and a covector as inputs:$$\Large\begin{aligned}
T(\omega,V)&=T(\omega_\mu dx^\mu,V^\nu\partial_\nu)\\
&=\omega_\mu V^\nu T(dx^\mu,\partial_\nu)\\
&=\omega_\mu V^\nu T^\mu_\nu
\end{aligned}$$
> Under coordinate transformations, this moves like$$\Large\tilde T^\rho_\sigma=\frac{\partial \tilde x^\rho}{\partial x^\mu}\frac{\partial x^\nu}{\partial \tilde x^\sigma}T^\mu_\nu$$a scalar...

