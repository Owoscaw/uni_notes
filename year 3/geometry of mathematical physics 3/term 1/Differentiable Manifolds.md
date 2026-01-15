
The groups investigated [[U(1),SU(2),SO(3)|previously]] were fundamentally different to vector spaces, as we could not find one-to-one maps to subsets of $\Re^n$. Such behavior is not exclusive to continuous groups, and gives rise to the more general notion of differentiable manifolds. The general idea is that differentiable manifolds can be covered by open sets, each of which has an associated one-to-one map to an open set inside a vector space. That is, we can build a differentiable manifold by "sewing together" things that we know how to do maths on.

First we review the notion of open and closed sets in $\Re^m$. An open ball in $\Re^m$ centered at $\underline{p}$ is defined as:$$\Huge B_r(\underline{p})=\{\underline{x}\in\Re^m:||\underline{x}-\underline{p}||^2<r^2\}$$Using this we define open and closed sets as:
> A subset $U$ of $\Re^n$ is open if for every point $p\in U$ there is $r$ such that $B_r(\underline{p})$ is fully contained in $U$
> A subset $U$ of $\Re^n$ is closed if its complement $\Re^n\setminus U$ is open.

Not every subset of $\Re^n$ has to be open or closed, and the properties are not mutually exclusive. This is the defining topology of $\Re^n$, known as the standard topology.

We propose that arbitrary unions and infinite intersections of open sets in $\Re^n$ are open. Fuck you if you want proof.

We now aim to describe spaces $X$ sitting inside $\Re^n$. First we need to know the open sets of $X$, that is we need to introduce a topology on $X$. To do this, we simply inherit the notions of open/closedness from $\Re^n$:
> For a subset $X\subseteq\Re^n$ we define the induced topology by declaring that $V\subset X$ is open if $V=U\cap X$ with $U$ open in $\Re^n$. Closed sets of $X$ are then defined as complements in $X$ of open sets in $X$. This definition turns $X$ into a topological space.

For example, consider $S^1\subset\Re^2$ defined by $x_1^2+x_2^2=1$. By intersecting $S^1$ with open balls we obtain open segments on $S^1$. Writing $x_1=\cos\phi,x_2=\sin\phi$ the segments are all of form $\phi_1<\phi<\phi_2$ for some $\phi_1,\phi_2$. Arbitrary unions and finite intersections of these are therefore open, as is $\emptyset$ and the whole of $S^1$:![[Differentiable Manifolds 2025-11-06 21.05.39.excalidraw]]
Given the notion of a topological space, we can redefine continuity:
> A map $f:X\rightarrow Y$ between topological spaces $X,Y$ is called continuous if the set $f^{-1}(U)$ if open in $X$ whenever $U$ is open in $Y$.
> Similarly, a map $f:U_X\rightarrow U_Y$ between open sets $U_X\subset X,U_Y\subset Y$ is called continuous if for all $V\subseteq U_Y$, the set $f^{-1}(V)$ is open in $X$ whenever $V$ is open in $Y$.

This agrees with the usual $\epsilon-\delta$ definition for maps $f:\Re^n\rightarrow\Re^m$. A one-to-one map $f:X\rightarrow Y$ between topological spaces $X,Y$ is called a homeomorphism if both $f,f^{-1}$ are continuous. Such maps preserve the structure of topological spaces.

## Definition:
A subset $X\subseteq\Re^n$ with the induced topology is an $n$-dimensional differentiable manifold if the following conditions are met:
> $X$ is covered by open sets $U_i\subseteq X$ and homeomorphism $\phi_i$ that map $U_i$ to an open subset $\phi_i(U_i)\subset\Re^n$. These are called coordinate charts/patches. The collection of patches $(U_i,\phi_i)$ is known as an atlas.
> Countably many $U_i$ cover $X$
> The coordinate changes $\phi_i\circ\phi_j^{-1}$ and their inverses $\phi_j\circ\phi_i^{-1}$ are $C^\infty$ in their respective domains. That is, they are continuous one-to-one maps that have infinitely many continuous derivatives:![[Differentiable Manifolds 2025-11-06 21.14.25.excalidraw]]

The property that we can cover $X$ with open sets imposes certain restrictions on what $X$ can look like. For example, $X=\{xy=0\}\subset\Re^2$ which is the union of $x=0,y=0$ meeting at the origin is not a manifold. Using topology induced from $\Re^2$ we have no issue defining points away from the origin, however any open set $U$ containing the origin will contain a piece from both branches, so open sets will look like a cross, different from any open subset of $\Re$. Therefore there cannot be any homeomorphism to an open subset of $\Re$ for such $U$. More formally:
> Choose a point $p_a$ on $x=0$ and a open interval on $xy=0$ that connects it to $(0,0)$. Choose a second point $p_b$ on $x=0$ beyond the origin. Using these points we need a continuous map to $\Re$, the interval must be mapped to an open interval in $\Re$. Let $(0,0)$ map to $0\in\Re$. The inverse image must also be an open set, as the coordinate maps must be homeomorphisms. The open sets containing $(0,0)$ all contain points on the other branch, and must also be mapped to the open interval in $\Re$. This cannot be as the map must be one-to-one.

Let us try to make a circle into a differentiable manifold with $g=e^{i\psi}$. First we restrict $\psi\in(-\pi,\pi)$ to avoid multivaluedness of the coordinate $\psi$. We now have a one-to-one map from the open interval $(-\pi,\pi)$ to all of [[U(1),SU(2),SO(3)|U(1)]] except the point $g=-1$. Hence we require a second patch. Let us set $g=e^{i\pi+i\theta}$  and let $\theta\in(-\pi,\pi)$ which lets us reach every point except $g=1$:$$\Huge\begin{align*}
g&=e^{i\psi},\,\,\psi\in(-\pi,\pi)\\
g&=e^{i\pi+i\theta},\,\,\theta\in(-\pi,\pi)\\
\psi&=\pi+\theta,\,\,\theta<0\\
\psi&=-\pi+\theta,\,\,\theta>0
\end{align*}$$We can now use the open intervals described by $\psi,\theta$ to construct functions on $U(1)$, if the functions agree on the overlapped region $g\neq\pm1$.

# Manifolds and the implicit function theorem:

We can describe a subspace $X$ of $\Re^3$ given by the vanishing scalar function $f(x,y,z)$:$$\Huge X:\{(x,y,z)\in\Re^n:f(x,y,z)=0\}$$as a manifold as follows. By the implicit function theorem we can find a function $g(x,y)$ such that $f(x,y,g(x,y))=0$ in a neighbourhood $V\subset\Re^3$ of a point $x_0,y_0,z_0$ where $\frac{\partial f}{\partial z}|_{(x_0,y_0,z_0)}\neq0$. Let us call $\hat U=V\cap X$ and use $\hat x,\hat y$ as coordinates in $\Re^2$. For $p=(x,y,z)\in U$ we set:$$\Huge\hat\phi:(x,y,z)\rightarrow(\hat x,\hat y)$$If this $\frac{\partial f}{\partial z}$ at this point is $0$, but not wrt one of the other coordinates we can use the same theorem for the other coordinate. The only points where this fails are at:$$\Huge\begin{align*}
f(x_0,y_0,z_0)&=0\\
\frac{\partial f}{\partial x}(x_0,y_0,z_0)&=\frac{\partial f}{\partial y}(x_0,y_0,z_0)=\frac{\partial f}{\partial z}(x_0,y_0,z_0)=0
\end{align*}$$At these points, $X$ cannot be given the structure of a differentiable manifold. Such points are known as singularities of the surface $f=0$.

# Paths:

A path is a continuous map $S$ from an open interval $(a,b)\subset\Re$ to $X$. Letting $t\in(a,b)\subset\Re$ we write:$$\Huge S:t\rightarrow\underline{q}(t)\in X$$where $\underline{q}(t)$ is a description of the path using the coordinates on $\Re^m\supset X$. Furthermore we demand that $\underline{q}(t)$ is a differentiable function from $S$ to $\Re^m$.

A tangent vector at $\underline{p}$ is the derivative of a path passing through $\underline{p}$ wrt its parameter, evaluated at $\underline{p}$. Assuming that $t_0$ is such that $\underline{q}(t_0)=\underline{p}$ we write:$$\Huge T_\underline{p}(S):=\frac{\partial \underline{q}(t)}{\partial t}\vert_{t_0}$$
These definitions use the fact that $X$ is a submanifold of $\Re^m$ which allows us to write tangent vectors as sitting inside $\Re^m$. We could have defined paths and tangent vectors in terms of the coordinate charts for a manifold to get a more abstract notion.

Note that the tangent vectors $T_\underline{p}(S)$ at a point $\underline{p}$ form a real $n$-dimensional vector space $T_\underline{p}X$, called the tangent space at $\underline{p}$.

For example, we can find the tangent vector of [[U(1),SU(2),SO(3)|SO(3)]] associated to the path:$$\Huge t\rightarrow\begin{pmatrix}\cos t & \sin t & 0 \\ -\sin t & \cos t & 0 \\ 0 & 0 & 1\end{pmatrix}$$at $t=0$. Note that at $t=0$ this reduces to the identity element $\mathbb{1}$:$$\Huge\frac{\partial }{\partial t}\begin{pmatrix}\cos t & \sin t & 0 \\ -\sin t & \cos t & 0 \\ 0 & 0 & 1\end{pmatrix}|_{t=0}=\begin{pmatrix}0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$
 