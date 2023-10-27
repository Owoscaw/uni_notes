# Bounds:

Let $f(x)$ be defined on an interval $I$. $f(x)$ is bounded from above in $I$ by an upper bound $k_1$ if $\exists k_1:f(x)\leq k_1\forall x\in I$. $f(x)$ need not take the value of $k_1$ over the interval $I$. If $\exists x_1\in I$ such that $f(x_1)=k_1$, then the upper bound has been attained, $k_1$ becomes the global maximum value of $f(x)$ in $I$.

Similarly, $f(x)$ is bounded from below in $I$ by a lower bound $k_2$ if $\exists k_2:f(x)\geq k_2\forall x\in I$. If $\exists x_2$ such that $f(x_2)=k_2$, then the lower bound has been attained, $k_2$ becomes the global minimum value of $f(x)$ in $I$.

Combining both definitions, $f(x)$ is bounded if it is bounded both above and below in $I$. That is if $\exists k$ such that $|f(x)|\leq k$. If no interval $I$ is specified, it should be taken that $I=Dom\,f$. For a function to have global maximum or minimum, the bounds by which $f(x)$ is bound must be attained, otherwise $f(x)$ is still bounded on $I$, however has no global maximum or minimum on $I$. Example with cos:
```desmos-graph
left=-2pi; right=2pi;
bottom=-1.5; top=1.5;
---
y=1|dashed
y=-1|dashed
y=\cos(x)
```
It is true that $|cos\,x|\leq 1,\,\forall x\in I$ where $I=Dom\, cos\,x$. Both $cos\,x=1$ and $cos\,x=-1$ can be attained, so these are the global maximum and minimum, shown by dashed lines.

## Extreme value theorem:

If $f(x)$ is continuous on a close interval $[a,b]$, then it is bounded on that interval and has upper bounds which are attained, $x_1,x_2\in[a,b]:f(x_2)\leq f(x)\leq f(x_1),\,\forall x\in[a,b]$. This is to say if $f(x)$ always has a global maximum and minimum if it is defined on a closed interval.


# Monotonicity:

$f(x)$ is monotonic increasing on an interval $[a,b]$ if $f(x_1)\leq f(x_2)\,\forall\,x_1,x_2:a\leq x_1<x_2\leq b$. This is to say for any $x_1,x_2$ on the interval $[a,b]$ with $x_1<x_2$ if any two $x_1,x_2$ satisfy $f(x_1)\leq f(x_2)$. Similarly, $f(x)$ is strictly monotonic increasing on an interval $[a,b]$ if $f(x_1)<f(x_2)$, with the same conditions as above. Monotonic and strictly monotonic decreasing are defined similarly.

# Critical Points:

A function $f(x)$ has a local maximum or minimum at $x=a$ if $\exists\, h>0$ such that $f(x)\leq f(a)$ ($\geq$ for a minimum) $\forall\,x\in(a-h,a+h)$. A local extremum is either a local max or a local min. If $f(x)$ has a local max or min at $x=a$ and is differentiable at this point, then $f^{\prime}(a)=0$. Since $f(x)$ is differentiable at $x=a$:
$$\Huge \lim_{x\to a^-}\frac{f(x)-f(a)}{x-a}=\lim_{x\to a^+}\frac{f(x)-f(a)}{x-a}=f^{\prime}(a)$$
If $f(x)$ has a local maximum at $x=a$:
$$\Huge \frac{f(x)-f(a)}{x-a}\leq0\,\,\,\forall x\in(a,a+h),\,\text{so:}$$
$$\Huge f^{\prime}(a)=\lim_{x\to a^+}\frac{f(x)-f(a)}{x-a}\leq 0$$
Similarly:$$\Huge \frac{f(x)-f(a)}{x-a}\geq0\,\,\forall x\in (a-h, a),\,\text{so}:$$$$\Huge f^{\prime}(a)=\lim_{x\to a^-}\frac{f(x)-f(a)}{x-a}\geq 0$$
There is only one value for $f^{\prime}(a)$ that satisfies both inequalities, that is:
$$\Huge 0\leq f^{\prime}(a)\leq0\iff f^{\prime}(a)=0$$
### Stationary points:

$f(x)$ has a stationary point at $x=a$ if it is differentiable at $x=a$ and that $f^{\prime}(a)=0$. An interior point $x=a$ on the domain of $f$ is critical if either $f^{\prime}(a)=0$ or $f^{\prime}(a)$ does not exist. Every local maxima or minima is a stationary point, however not every stationary point is a local maxima or minima.

### Points of inflection:

If $f(x)$ is twice differentiable on an open interval around $x=a$, with $f^{\prime\prime}(a)=0$, and if $f^{\prime\prime}(a)$ changes sign at $x=a$, then $x=a$ is a point of inflection.

## First derivative test:

Suppose $f(x)$ is continuous at a critical point $x=a$:
> If $\exists\,h>0$ such that $f^{\prime}(x)<0\,\forall x\in(a-h,a)$ and $f^{\prime}(x)>0\,\forall x\in(a,a+h)$, then $x=a$ is a local minimum
> If $\exists\,h>0$ such that $f^{\prime}(x)>0\,\forall x\in(a-h,a)$ and $f^{\prime}(x)<0\,\forall x\in(a,a+h)$, then $x=a$ is a local maximum
> If $\exists\,h>0$ such that $f^{\prime}(x)$ has constant sign $\forall x\neq a\in(a-h,a+h)$, then $x=a$ is not an extremum

## Second derivative test:

Suppose $f(x)$ is twice differentiable at $x=a$ with $f^{\prime}(a)=0$:
> If $f^{\prime\prime}(a)>0$ then $x=a$ is a local minimum
> If $f^{\prime\prime}(a)<0$ then $x=a$ is a local maximum

### Endpoints:

If $C\in Dom\,f$ and if $\exists\,h>0$ such that $f(x)$ is defined on $[C,C+h)$ but not on $(C-h,C)$, or vice versa, then $x=C$ is an endpoint of $f(x)$. If $Dom\,f=[a,b]$, then $x=a$ and $x=b$ are endpoints.

If $x=C$ is an endpoint of $f(x)$, then $f(x)$ has an endpoint maximum or minimum at $x=C$ if $f(x)\leq f(C)$ ($\geq$ for minimum) for $x$ sufficiently close to $C$. If $f(x)$ is continuous and differentiable sufficiently close to an endpoint, then the sign of the derivative determines the nature of the endpoint.

If $f(x)$ is continuous on a closed interval $[a,b]$, then all global extrema on this interval are attained at either critical points or endpoints.

# Rolle's Theorem:

Rolle's Theorem states that if $f$ is differentiable on the open interval $(a,b)$ and continuous on the closed interval $[a,b]$ with $f(a)=f(b)$, then there is at least one $c\in(a,b)$ for which $f^{\prime}(c)=0$, that is $c$ is a stationary point.:
![[Rolle's Theorem example]]

By the extreme value theorem, $\exists\,x_1,x_2\in[a,b]$ such that $f(x_1)\leq f(x)\leq f(x_2)\,\,\forall x\in [a,b]$. If $x_1\in(a,b)$, then $x_1$ is a local minimum and $f^{\prime}(x_1)=0$. If $x_2\in(a,b)$, then $x_2$ is a local maximum and $f^{\prime}(x_2)=0$. Otherwise, both $x_1$ and $x_2$ are endpoints $a,b$. Since $f(a)=f(b)$, then $f(x_1)=f(x_2)=f(a)=f(b)$, and so $f(a)\leq f(x)\leq f(b),\,\,\forall x\in[a,b]$ so $f(x)$ is constant on $[a,b]$ and $f^{\prime}(x)=0,\,\,\forall x\in (a,b)$.

A corollary of this is that if $f(x)$ is differentiable on an open interval $I$, then each pair of zeros of $f(x)$ is separated by at least one zero of $f^{\prime}(x)$. This can be used to find a bound on the number of distinct real zeros of a function.


# Mean Value Theorem:

The mean value theorem (MVT) states that if $f$ is differentiable on $(a,b)$, and continuous on $[a,b]$, then there is at least one $c\in(a,b)$ for which:$$\Huge f^{\prime}(c)=\frac{f(b)-f(a)}{b-a}$$
![[MVT example]]
Geometrically, this means that there is at least one point at which the gradient is parallel to the line joining $f(a)$ and $f(b)$. Note that Rolle's Theorem is a special case of the MVT (kind of like pulling the line connecting $f(a)$ to $f(b)$ down to the $x$ axis):

Let $g(x)=(b-a)(f(x)-f(a))-(x-a)(f(b)-f(a))$. This is a transformation on the original function $f$, described above. Then:
$$\Huge g(a)=(b-a)(f(a)-f(a))-(a-a)(f(b)-f(a))=0$$
$$\Huge g(b)=(b-a)(f(b)-f(a))-(b-a)(f(b)-f(a))=0$$
$$\Huge g(a)=0=g(b),\,\text{so we can use Rolles Theorem}$$
So $\exists\,c\in(a,b):g^{\prime}(c)=0$, $g^{\prime}(x)=(b-a)f^{\prime}(x)-(f(b)-f(a))$, so:$$\Huge 0=(b-a)f^{\prime}(c)-(f(b)-f(a))\implies f^{\prime}(c)=\frac{f(b)-f(a)}{b-a}$$
As required. The MVT can be used to show some results between monotonicity and the derivative:

Suppose $f(x)$ is continuous on $[a,b]$ and differentiable on $(a,b)$ with $f^{\prime}(x)\geq 0,\,\,\forall x\in(a,b)$. Then $f(x)$ is monotonic increasing in $(a,b)$. If $a\leq x_1<x_2\leq b$ then by MVT $\exists\,c\in(a,b):f^{\prime}(c)=\frac{f(x_2)-f(x_1)}{x_2-x_1}$. Since $f^{\prime}(x)\geq 0$ in $(a,b)$ then $f^{\prime}(c)\geq 0\implies f(x_2)\geq f(x_1)$, that is $f$ is monotonic increasing. 


# Inverse function rule:

The inverse function rule states that if $f(x)$ is continuous on $[a,b]$ and differentiable on $(a,b)$ with $f^{\prime}(x)>0\,\forall x\in(a,b)$ then it's [[Functions, Domain and Range#Inverse functions|inverse function]] $g(y):g(f(x))=x$ is differentiable for all $f(a)<y<f(b)$ with:
$$\Huge g^{\prime}(y)=\frac{1}{f^{\prime}(g(y))}$$

This is because a continuous function $f(x)$ that is monotonic increasing on $(a,b)$ will always be injective, so will always have an inverse function. The domain of this inverse then becomes the range of $f(x)$, producing the restriction that $g^{\prime}(y)$ is only defined on $f(a)<y<f(b)$. This follows using the chain rule:$$\Huge \frac{d}{dx}\left(g(f(x))\right)=g^{\prime}(f(x))f^{\prime}(x)=\frac{d}{dx}(1)$$
$$\Huge g^\prime(f(x))=\frac{1}{f^\prime(x)},\,\,\text{with}\,\,y=f(x):$$$$\Huge g^\prime(y)=\frac{1}{f^\prime(g(y))}$$

# Partial derivatives:

Functions can have two or more variables, where $f(x,y)$ can be thought of as the height of a function over the $xy$ plane:
![[mv function example]]

The partial derivative is needed to describe the rate of change of $f(x,y)$ as each $x$ or $y$ are varied, while keeping the other constant. The partial derivative of $f$ with respect to $x$ is denoted as $\frac{\partial f}{\partial x}$ or $f_x(x,y)$ and is found by differentiating $f$ with respect to $x$, treating $y$ as a constant. The process is similar when finding the partial derivative of $f$ with respect to $y$, denoted as $\frac{\partial f}{\partial y}$ or $f_y(x,y)$. The following limits are assumed to exist:$$\large \frac{\partial f}{\partial x}(x,y)=\lim_{h\to 0}\frac{f(x+h,y)-f(x,y)}{h},\,\,\frac{\partial f}{\partial y}(x,y)=\lim_{h\to 0}\frac{f(x,y+h)-f(x,y)}{h}$$
The following second order partial derivatives also exist:$$\large \frac{\partial^2f}{\partial x^2}=\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right),\,\frac{\partial^2 f}{}$$
