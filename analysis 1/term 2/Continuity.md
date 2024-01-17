Let $f:X\mapsto\Re$ be a function and let $x\in X$. Then $f$ is called continuous at $c$ if for all $\epsilon>0$ there exists a $\delta>0$ such that:$$\Huge |f(x)-f(c)|<\epsilon\,\,\forall x\in X:|x-c|<\delta$$The function is called continuous if it is continuous at $c$ for all $c\in X$. If $c\in X$ is an [[Functions and their limits#Open-ness? and interior points|interior point]], then $f$ is continuous at $c$ if and only if:$$\Huge \lim_{x\to c}f(x)=f(c)$$Left continuity can be defined at $c\in X$ if and only if $\lim_{x\to c^-}f(x)=f(c)$. Similarly, right continuity can be defined at $c\in X$ if and only if $\lim_{x\to c^+}f(x)=f(c)$. For interior points $c$, $f$ is only continuous at $c$ if it is both left and right continuous at that point.

Continuity at a point $c\in X$ is a local property, it is only dependent on the behaviour of the function over a small interval around $c$. Examples:
![[continuous function examples]]

## Continuity through sequences:

Let $X\subset\Re$, $c\in X$, and $f:X\mapsto\Re$ be a function. Then $f$ is continuous at $c$ if and only if for all sequences $(x_n)_{n\in\mathbb N}\in X$ with $\lim_{n\to\infty}x_n=c$ we have:$$\Huge \lim_{n\to\infty}f(x_n)=f(c)=f(\lim_{n\to\infty}x_n)$$To prove this, use the above results.

## Continuity through COLT:

Let $X\subset\Re,c\in X$ and $f,g:X\mapsto\Re$ be continuous at $c$, then:
> $h(x)=\alpha f(x)+\beta g(x)$ is continuous at $c$ for all $\alpha,\beta\in\Re$
> $h(x)=f(x)g(x)$ is continuous at $c$
> $h(x)=\frac{f(x)}{g(x)}$ is continuous at $c$, given that $g(c)\neq0$

This is proven by using COLT with continuity through sequences. For example, consider a polynomial $p:\Re\mapsto\Re$ as a function given by:$$\Huge f(x)=a_nx^n+\dots+a_1x+a_0\text{ with }n\in\mathbb N_0, a_0,\dots,a_n\in\Re$$Any polynomial is continuous, since it can be broken down into a linear combination of continuous functions to certain powers, which can be broken down into the repeated product of the same function ($h(x)=x$). 

## Function compositions:

Given two functions $f:X\mapsto\Re$, $g:Y\mapsto\Re$ with $X,Y\subset\Re$ and:$$\Huge f(X)=\{y\in\Re:y=f(x)\text{ for some }x\in X\}\subset Y$$We can then form the composition $g\circ f:X\mapsto\Re$ given by:$$\Huge g\circ f(x)=g(f(x))\,\forall x\in X$$If $f$ is continuous at $c\in X$ and $g$ is continuous at $f(c)\in Y$ then $g\circ f$ is continuous at $c\in X$. Proof:![[continuous composition]]
