
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
The IVT is useful for finding the roots of a function. If $f$ is continuous on $[a,b]$ with $f(a)<0<f(b)$ or $f(b)<0<f(a)$, then the IVT states that there is at least one root such that $f(x)=0,\,a<x<b$ or $b<x<a$. 

# Limits with logarithms, powers, and exponentials:

## Lemma 1:
$$\Huge\forall x\geq0,\,e^x\geq1+x$$
Consider $f(x)=e^x-(1+x)$. We have $f(0)=0$, and $f^\prime(x)=e^x-1\geq 0$. Since the derivative of $f$ is always positive, it must be [[EVT, MVT, boundedness and monotonicity#Monotonicity|monotic increasing]] on $[0,\infty)$, so $f(x)\geq 0,\,\forall x\geq0$.

## Lemma 2:
$$\Huge \forall x\geq0,\,n\in\mathbb{N},\,e^x\geq\sum_{j=0}^n\frac{x^j}{j!}$$
When $n=1$, $e^x\geq\sum_{j=0}^1\frac{x^j}{j!}=\frac{x^0}{0!}+\frac{x^1}{1!}$, which is proven true by [[Limits and Continuity#Lemma 1|lemma 1]]. Now let:$$\Huge f_n(x)=e^x-\sum_{j=0}^n\frac{x^j}{j!}=e^x-\left(1+x+\frac{x^2}{2!}+\dots+\frac{x^n}{n!}\right)$$
Note that $f_n(0)=0,\,\forall n\in\mathbb{N}$. Differentiating, we have:$$\large f^\prime_n(x)=e^x-\left(1+x+\frac{x^2}{2!}+\dots+\frac{x^{n-1}}{(n-1)!}\right)=e^x-\sum_{j=1}^{n-1}\frac{x^j}{j!}=f_{n-1}(x)$$
Since $f_1(x)\geq0$ by lemma 1, we then have $f^\prime_2(x)\geq0$. Now since $f_2(x)\geq 0,\,\forall x\geq 0$. This continues for $f_n(x)\geq0$ and $f^\prime_n(x)\geq0$. Therefore, for all $n\in\mathbb{N}$, the statement is true by mathematical induction.

## Powers beat logs:
$$\Huge \forall a>0,\,\lim_{x\to\infty}\frac{log\,x}{x^a}=0$$
Let $x=e^y$, then we have:
$$\Huge \lim_{x\to\infty}\frac{log\,x}{x^a}=\lim_{y\to\infty}\frac{y}{e^{ay}}$$
Then for $y>0$, using lemma 2 in the $n=2$ case:$$\Huge 0\leq \frac{y}{e^{ay}}\leq\frac{y}{1+ay+\frac{1}{2}a^2y^2}\leq\frac{y}{\frac{1}{2}a^2y^2}=\frac{2}{a^2y}$$
Now the expression is bounded from above and below, with two expression that will have a limit of $0$ when $y\to\infty$:$$\Huge 0\leq\lim_{y\to\infty}\frac{y}{e^{ay}}\leq0$$
So the expression has only one value, $0$ as $y\to\infty$. This proves the original result by our change of variables.

## Exponentials beat powers:

For any $a>0$:$$\Huge \lim_{x\to\infty}\frac{x^a}{e^x}=0$$
Let $n$ be the smallest possible integer such that $n>a$. By lemma 2 for $x>0$ we have:
$$\Huge 0\leq \frac{x^a}{e^x}\leq\frac{x^a}{1+x+\dots+\frac{x^n}{n!}}=\frac{x^{a-n}}{x^{-n}+x^{1-n}+\dots+\frac{1}{n!}}$$
This is bounded above by expressions that will both take value $0$ when $x\to\infty$, so the squeezing theorem applies ($n-a<0$):$$\Huge 0\leq\lim_{x\to\infty}\frac{x^a}{e^x}\leq0$$
Which gives the result as required.

# Exponential as a limit:

For any $a\in\Re$:$$\Huge \lim_{x\to\infty}$$

