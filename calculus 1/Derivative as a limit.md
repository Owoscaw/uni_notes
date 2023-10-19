The derivative $f^{\prime}(a)$ of a function $f(x)$ at the points $a$ is equal to the slope of the tangent to the graph of $f$ at $x=a$, if it exists. This is naturally defined as the limit of the slope of a line segment joining two nearby points, $a$ and $a+h$, on the graph:![[graphic derivative as a limit]]
That is, a function is differentiable at a point $a$ if the following limit exists:
$$\Huge f^{\prime}(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$$
If this limit exists $\forall a\in Dom\,f$, we say that $f$ is differentiable. If $f$ is differentiable, then $f^{\prime}(x)$ is a function called the derivative of $f(x)$. A necessary condition for $f^{\prime}(a)$ to exist is for $f$ to be continuous at $a$, but this is not sufficient to call $f$ differentiable. 

The equation of the tangent to $f(x)$ at the point $(a,f(a))$ is given in terms of the derivative, given $f(a)$ and $f^{\prime}(a)$ both exist:$$\Huge y=f^{\prime}(a)(x-a)+f(a)$$

A function can fail to be differentiable at a point, $x=a$, where it is continuous:
> The tangent line is vertical, that is $f^{\prime}(a)$ tends to $\pm\infty$ at $a$, as $\infty\notin\Re$.
> There is no unique tangent at $a$, for example $|x|$:![[Derivative as a limit .excalidraw]]