
# Limits:
A [[Functions, Domain and Range|function]], $f$, has a limit, $L$, at a point $x=a$ if $f(x)$ is always close to $L$ whenever $x$ is close to $a$. More precisely, if there is an acceptable error  $\epsilon \in\Re$, $\epsilon > 0$, between $f(x)$ and $L$, then the following is required:
$$\Huge |f(x)-L|<\epsilon$$
This is true for all $x$ on some interval around $x=a$ such that $x$ is "close" to $a$. More precisely, if there is a distance $\delta\in\Re$, $\delta >0$ between $x$ and $a$, then the following is required:
$$\Huge |x-a|<\delta$$
Combining the above requirements, a limit can be precisely defined:
$$\Huge \forall\,\epsilon>0\,\exists\,\delta>0:|f(x)-L|<\epsilon\,\,when\,\,0<|x-a|<\delta$$
That is:
$$\Huge \lim_{x\to a}f(x)=a$$
![[Limits and Continuity 2023-10-12 22.42.38.excalidraw]]

It is not required that $f(a)$ is equal to $L$ or that $f(a)$ is defined, as we are looking at the tendency of the function as $x$ gets arbitrarily close to $a$. $f(x)$ is no more than $\pm\epsilon$ away from $L$ when $x$ is no more than $\pm\delta$ away from $a$. If there is no such $L$, then the limit does not exist.

# Continuity:

A function, $f$, is continuous at a point $a$ if the following are satisfied:
> $f(a)$ exists
> $\lim_{x\to a}f(x)$ exists
> $\lim_{x\to a}f(x)=f(a)$

A function, $f$, is continuous over a subset, $S\subset Dom\,f$, if it is continuous at all points in $S$. If this subset $S$ is the full domain of $f$, then the function can be called continuous. That is, a function is continuous if at every point, $a\in Dom\,f$, $f$ is continuous at $x=a$

## Consequences of continuity:
> The limit is unique at a point, there does not exist any more than one limit for one point.
> If $f(x)=g(x)\forall x\in\Re\setminus\{a\}$ over some open interval containing $a$, then:$$\Huge\lim_{x\to a}f(x)=\lim_{x\to a}g(x)$$
> If $f(x)\geq k$ is bounded by $(a,b)$ or $(c,a)$ and if $\lim_{x\to a}f(x)=L$, then $L\geq k$
> Calculus of limits theorem (COLT). If $\lim_{x\to a}f(x)=L$ and $\lim_{x\to a}g(x)=M$ then:$$\large \lim_{x\to a}(f(x)+g(x))=L+M,\,\lim_{x\to a}(f(x)g(x))=LM,\,\lim_{x\to a}\left(\frac{f(x)}{g(x)}\right)=\frac{L}{M},\,M\neq0$$
> If $f$ and $g$ are continuous, then $(f+g),(fg),(f/g),$ and $|f|$ are continuous.
> All polynomials, rational functions, trig functions, and hyperbolic functions are continuous.
> If $\lim_{x\to a}g(x)=L$, and $f(x)$ is continuous at $x=L$, then $\lim_{x\to a}(f\circ g)(x)=f(L)$.

# Sandwich theorem:

If $g(x)\leq f(x)\leq h(x)\,\forall x\in\Re\setminus\{a\}$ over some open interval containing $a$, and $\lim_{x\to a}g(x)=\lim_{x\to a}h(x)=L$, then $g,h$ squeeze $f(x)$ such that:
$$\Huge \lim_{x\to a}f(x)=L$$

# Important trig limits:

Two important trigonometric limits are:
$$\Huge \lim_{x\to 0}\frac{sin\,x}{x}=1,$$

```desmos-graph
left=-5; right=5;
top=1.5; bottom=-1.5;
---
(0,1)|open
(0, 0)|open
\sin(x)/x
(1-\cos(x))/x
```
