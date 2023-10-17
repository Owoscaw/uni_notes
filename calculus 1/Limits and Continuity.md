
# Limits:
A [[Functions, Domain and Range|function]], $f$, has a limit, $L$, at a point $x=a$ if $f(x)$ is always close to $L$ whenever $x$ is close to $a$. More precisely, if there is an acceptable error  $\epsilon \in\Re$, $\epsilon > 0$, between $f(x)$ and $L$, then the following is required:
$$\Huge |f(x)-L|<\epsilon$$
This is true for all $x$ on some interval around $x=a$ such that $x$ is "close" to $a$. More precisely, if there is a distance $\delta\in\Re$, $\delta >0$ between $x$ and $a$, then the following is required:
$$\Huge |x-a|<\delta$$
Combining the above requirements, a limit can be precisely defined:
$$\Huge \forall\,\epsilon>0\,\exists\,\delta>0:|f(x)-L|<\epsilon\,\,when\,\,0<|x-a|<\delta$$
That is:
$$\Huge \lim_{x\to a}f(x)=a$$
![[definition of limit]]

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
$$\Huge \lim_{x\to 0}\frac{sin\,x}{x}=1,\,\lim_{x\to 0}\frac{1-cos\,x}{x}=0$$

 This is proven through the sandwich theorem:
 ![[limit of sinx]]
 This result can be used to prove the second result:
 $$\Huge \lim_{x\to 0}\frac{1-cos\,x}{x}=\lim_{x\to 0}\frac{(1-cos\,x)(1+cos\,x)}{x(1+cos\,x)}=\lim_{x\to 0}\frac{sin^2x}{x(1+cos\,x)}$$
 $$\Huge =\lim_{x\to 0}\frac{sin\, x}{x}\times\frac{sin\,x}{1+cos\,x}=^{COLT}1\times0=0$$
# Classification of discontinuities:

$f(x)$ has a right sided limit, $L^+=\lim_{x\to a^+}f(x)$, as $x$ tends to $a$ from above if:$$\Huge \forall\epsilon>0\,\exists\,\delta>0:|f(x)-L^+|<\epsilon\,\forall x:0<x-a<\delta$$
Note the difference between the restriction on $x-a$. This is different as $x>a$ for a right sided limit. Similarly, $f(x)$ has a left sided limit, $L^-=\lim_{x\to a^-}f(x)$ as $x$ tends to $a$ from below if:
$$\Huge \forall \epsilon>0\,\exists\,\delta>0:|f(x)-L^-|<\epsilon\,\forall x:0<a-x<\delta$$
These relate to the general limit, $L$, in the way that $L$ exists if and only if $L^+$ and $L^-$ exists, and are equal, that is:
$$\Huge \lim_{x\to a}f(x)=L\iff L=L^+=L^-$$
Using these definition, there exists three types of discontinuities:
> A removable discontinuity is where $L$ exists, but $L\neq f(a)$. This can be removed to make a continuous function:$$\Huge g(x)=\begin{cases}f(x)&\text{if}&x\neq a\\L&\text{if}&x=a\end{cases}$$
> A jump discontinuity is where $L^+$ and $L^-$ both exists, but $L^+\neq L^-$.
> An infinite/essential discontinuity is where at least one $L^+$ or $L^-$ do not exist.

![[types of discontinuity]]

# Infinite limits:

A function has a limit as $x\to\infty$ if $f(x)$ can be kept arbitrarily close to some value, $L$, by making $x$ sufficiently large. That is to say:$$\Huge f(x)\,\text{has a limit}\,L\,\text{as}\,x\,\text{tends to}\,\infty\,\text{if:}$$$$\Huge \forall \epsilon>0\,\exists\,S>0:|f(x)-L|<\epsilon\,\,\forall x>S$$
Similarly for $x\to -\infty$, the above holds $\forall x<S<0$:
$$\Huge \forall \epsilon>0\,\exists S<0:|f(x)-L|<\epsilon\,\forall x<S$$
Substituting for "problem values" can be helpful, for example:
![[infinite limit example]]
The graph of a function $f$ will have a horizontal asymptote to the right or left at $y=L$ if $\lim_{x\to\infty}f(x)=L$ for the right or $\lim_{x\to -infty}f(x)=L$ for the left.

# Intermediate Value Theorem:

This theorem states that if $f$ is continuous on a closed interval $[a,b]$, and $u$ is any value between $f(a)$ and $f(b)$, then $\exists c\in(a,b):f(c)=u$:![[IVT]]
