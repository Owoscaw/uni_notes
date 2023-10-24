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
$f(x)$ has a stationary point at $x=a$ if it is differentiable at $x=a$ and that $f^{\prime}(a)=0$. An interior point $x=a$ on the domain of $f$ is critical if either $f^{\prime}(a)=0$ or $f^{}$