
# Parametrisations of regular surfaces:

A subset $S$ of $\Re^3$ is called a surface if it can be covered completely by a set of local parametrisations. It is called a regular surface if for every point $\underline{p}\in S$ there exists an open set $V\subset\Re^3$ with $\underline{p}\in V$ and a map $\underline{x}:U\rightarrow V\cap S$, where $U$ is an open set of $\Re^2$, such that:
> The map $\underline{x}:U\rightarrow V\cap S$ is smooth
> The map $\underline{x}:U\rightarrow V\cap S$ is a homeomorphism
> The partial derivatives $\frac{\partial \underline{x}}{\partial u}(u,v),\frac{\partial \underline{x}}{\partial v}(u,v)\in\Re^3$ are linearly independent for all $(u,v)\in U$. As a consequence, the image $d_{(u,v)}\underline{x}(\Re^2)$ (where $d_{(u,v)}$ represents the differential operator) is a two-dimensional Euclidean plane.

The map $\underline{x}:U\rightarrow V\cap S$ is called a local parametrisation of $S$ at the point $\underline{p}$, whereas its inverse is called a local coordinate chart of $S$ at $\underline{p}$.

Let $U\subset\Re^2$ be open and $g:U\rightarrow\Re$ be a smooth function. Then the graph of $g$ given by $\{(u,v,g(u,v)\in\Re^3:(u,v)\in\Re^2\}$ is a regular surface in $\Re^3$:
> Let $S$ be equal to this set, then we choose the map $\underline{x}:U\rightarrow\Re^3$ given by:$$\Huge \underline{x}(u,v)=(u,v,g(u,v))$$as a global parametrisation of $S$ with $V=\Re^3$. It is obvious that the image of $\underline{x}$ covers every $\underline{p}\in S$, and that the map it smooth. It remains to show the final properties.
> The map $\underline{x}:U\rightarrow S$ is bijective and therefore $\underline{x}^{-1}:S\rightarrow U$ exists. Surjectivity of this inverse is obvious, so we show injectivity:$$\Huge\begin{align*}
\underline{x}(u,v)=\underline{x}(u',v')&\implies (u,v,g(u,v))=(u',v',g(u',v'))\\
&\implies(u,v)=(u',v')
\end{align*}$$Moreover, $\underline{x}^{-1}$ is the restriction of $\pi:\Re^3\rightarrow\Re^2$ with $\pi(u,v,w)=(u,v)$, which is continuous. Therefore the restriction $\underline{x}^{-1}$ is also continuous, making $\underline{x}$ a homeomorphism.
> Since $\underline{x}(u,v)=(u,v,g(u,v))$ we have:$$\Huge \frac{\partial \underline{x}}{\partial u}(u,v)=\left(1,0,\frac{\partial g}{\partial u}(u,v)\right),\,\,\frac{\partial \underline{x}}{\partial v}(u,v)=\left(0,1,\frac{\partial g}{\partial v}(u,v)\right)$$These partial derivatives are obviously linearly independent, completing the proof.

Consider the following examples:
> Let $U=\Re^2$ and $g(u,v)=\frac{u^2}{a^2}+\frac{v^2}{b^2}$ with $a,b>0$. The graph $S$ defined by $(u,v,g(u,v))$ is called an elliptic paraboloid. The intersection of $S$ with horizontal planes $E_c=\{(u,v,c)\in\Re^3:u,v\in\Re\}$ with $c>0$ leads to ellipses defined by $\frac{u^2}{a^2}+\frac{v^2}{b^2}=c$.
> Let $U=\Re^2$ and $g(u,v)=\frac{u^2}{a^2}-\frac{v^2}{b^2}$ with $a,b>0$. The graph defined by $(u,v,g(u,v))$ is called a hyperbolic paraboloid. The intersection of the graph with horizontal planes $E_c$ is then described by:$$\Huge X\cdot Y=\left(\frac{u}{a}+\frac{v}{b}\right)\left(\frac{u}{a}-\frac{v}{b}\right)=c$$Note that these definitions of $X,Y$ can be viewed as coordinate changes and the level sets of the surface are hyperbolae 