The derivative $f^{\prime}(a)$ of a function $f(x)$ at the points $a$ is equal to the slope of the tangent to the graph of $f$ at $x=a$, if it exists. This is naturally defined as the [[Limits and Continuity#Limits|limit]] of the slope of a line segment joining two nearby points, $a$ and $a+h$, on the graph:![[graphic derivative as a limit]]
That is, a function is differentiable at a point $a$ if the following limit exists:
$$\Huge f^{\prime}(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$$
The equation of the tangent to $f(x)$ at the point $(a,f(a))$ is given in terms of the derivative, given $f(a)$ and $f^{\prime}(a)$ both exist:$$\Huge y=f^{\prime}(a)(x-a)+f(a)$$

# Differentiability

If this limit exists $\forall a\in Dom\,f$, we say that $f$ is differentiable. If $f$ is differentiable, then $f^{\prime}(x)$ is a function called the derivative of $f(x)$. A necessary condition for $f^{\prime}(a)$ to exist is for $f$ to be continuous at $a$, but this is not sufficient to call $f$ differentiable. 

A function can fail to be differentiable at a point, $x=a$, where it is [[Limits and Continuity#Continuity|continuous]]:
> The tangent line is vertical, that is $f^{\prime}(a)$ tends to $\pm\infty$ at $a$, as $\infty\notin\Re$.
> There is no unique tangent at $a$, for example $|x|$:![[undifferentiable example]]

If $f(x)$ is differentiable, then $f^{\prime}(x)$ may also be differentiable. If $f$ is differentiable twice, then we can say that $f$ has a second derivative:$$\Huge (f^{\prime}(x))^{\prime}=f^{\prime\prime}(x)$$
The $n$th derivative of $f$ is denoted as:
$$\Huge f^{(n)}(x)=\frac{d^nf}{dx^n}=D^nf(x)$$
When differentiating with respect to time, $\cdot$ is used instead of $\prime$.