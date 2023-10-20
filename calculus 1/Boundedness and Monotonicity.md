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

If $f(x)$ is continuous on a close interval $[a,b]$, then it is bounded on that interval and has upper bounds which are attained, $x_1,x_2\in[a,b]$