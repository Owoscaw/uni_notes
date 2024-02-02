
Let $X\subset\Re$ be open, and $f:X\mapsto\Re$  a function. $f$ is called differentiable at a point $c\in X$ if the following exists:$$\Huge \lim_{x\to c}\frac{f(x)-f(c)}{x-c}$$This is denoted as $f^\prime(c)$, where $f^\prime(c)$ is the derivative of $f$ at $c$. A function is called differentiable if for all $c\in X$, it is differentiable at $x=c$. This expression has a geometric interpretation, it is the slope of the line between points $(c,f(c))$ and $(x,f(x))$.

Let $f:X\mapsto\Re$ be a function. Then $f$ is differentiable at $c\in X$ if and only if the following holds: There exists $m\in\Re$ and a function $r(x)$ such that:$$\Huge f(x)=f(c)+m(x-c)+r(x)(x-c)$$With $r$ continuous at $c$ and $\lim_{x\to c}r(x)=r(c)=0$. Let $f:X\mapsto\Re$ be a function where $X\subset\Re$. Then $f$ is differentiable at $c\in X$ if and only if the following holds:$$\Huge \exists m\in\Re,r(x):f(x)=f(c)+m(x-c)+r(x)(x-c)$$With $r$ [[Continuity|continuous]] at $c$ and $\lim_{x\to c}r(x)=r(c)=0$. Here, $m=f'(c)$. We prove this as follows:![[differentiability at a point proof]]
Let $f:X\mapsto\Re$ be a function where $X\subset\Re$. If $f$ is differentiable at $c\in X$ then $f$ is also continuous at $c$, proven as follows.:$$\Huge f(x)-f(c)=\frac{(x-c)(f(x)-f(c))}{x-c},\,\text{for }x\neq c$$$$\Huge\lim_{x\to c}f(x)-f(c)=\lim_{x-c}(x-c)\lim_{x\to c}\frac{f(x)-f(c)}{x-c}=0\times f'(c)=0$$Using the definition of the derivative and COLT. This implies that $\lim_{x\to c}f(x)=f(c)$, so $f$ is continuous at $c$. This does not go the other way around, not all continuous functions are differentiable but all differentiable functions are continuous. There exist functions $f:\Re\mapsto\Re$ that are continuous everywhere but differentiable nowhere.

# Differentiable results:

Let $f,g$ be two differentiable functions at the point $c$ and $\alpha\in\Re$, then $f+c$ and $\alpha f$ are also differentiable at $c$:$$\Huge (f+g)'(c)=f'(c)+g'(c),\,\,(\alpha f)'(c)=\alpha f'(c)$$Furthermore, their product $fg$ is also differentiable at $c$:$$\Huge (fg)'(c)=f(c)g'(c)+f'(c)g(c)$$
Let $f,g$ be two functions such that $g$ is differentiable at $c$ and $f$ is differentiable at $g(c)$. Then $f\circ g$ is differentiable at $c$ with:$$\Huge  (f\circ g)'(c)=f'(g(c))g'(c)$$![[function compositions differentiability]]
# Mean value theorems:

If $f$ is differentiable at $c$ and has a local extrema at $c$ then $f'(c)=0$. For a local maxima this means that $\exists\delta>0:f(c)\geq f(x)\,\,\forall x\in(c-\delta,c+\delta)$, and for a local minima $\exists\delta>0:f(c)\leq f(c)\,\,\forall x\in(c-\delta,c+\delta)$. We prove this for the maxima case, as the minima case is very similar: 

At a local maximum, $f(x)-f(c)\leq0$ so consider the left and right limits of the definition of the derivative. If $x>c$ then $\frac{f(x)-f(c)}{x-c}\leq0$ and if $x<c$ then $\frac{f(x)-f(c)}{x-c}\geq0$ and we get:$$\Huge \lim_{x\to c^+}\frac{f(x)-f(c)}{x-c}\leq0,\,\,\lim_{x\to c^-}\frac{f(x)-f(c)}{x-c}\geq0$$This can only take one value, $0$, so we get the proof as required. $c$  is a local maxima $\implies f'(c)=0$.

# Rolle's theorem:

Let $f:[a,b]\mapsto\Re$ be continuous and differentiable on $(a,b)$ and suppose that $f(a)=f(b)$ then there exists $c\in(a,b)$ such that $f'(c)=0$. Since $f$ is continuous on $[a,b]$ then $f$ attains its maximum and minimum, so there exists $d,e\in[a,b]$ with $f(d)\geq f(x)\geq f(e)\,\,\forall x\in[a,b]$.

Using the same function as before, there exists $c\in(a,b)$ such that:f′(c)=f(b)−f(a)b−aTo prove this we set $g(x)=f(x)-\frac{f(b)-f(a)}{b-a}(x-a)$. Since this contains $f(x)$, this function is continuous on $[a,b]$ and differentiable on $(a,b)$. Then:g′(x)=f′(x)−f(b)−f(a)b−aNote that $g(a)=f(a)$ and $g(b)=f(a)=g(a)$. Then we can apply Rolle's theorem to $g$. So there exists $c\in(a,b)$ such that $g'(c)=0$:g′(c)=0⟹f′(c)=f(b)−f(a)b−aSo we get the mean value theorem proven by Rolle's theorem.

# Monotonicity:

Let $f:I\mapsto\Re$ be continuous on an interval $I$ and differentiable over its interior points, then:
> If $f'(x)=0$ for all $x$, then $f$ is a constant function
> If $f'(x)\geq0$ for all $x$, then $f$ is monotonically increasing
> If $f'(x)\leq0$ for all $x$, then $f$ is monotonically decreasing

For the above inequalities, if the inequality is strict then the function can be said to be strictly monotonically increasing/decreasing. These are proven using the [[EVT, MVT, boundedness and monotonicity#Mean Value Theorem|MVT]]. Let $c,d\in I$ with $c<d$. By the MVT we have that there exists $\alpha\in(c,d)$ such that $f(d)-f(c)=f'(\alpha)(d-c)$:$$\Huge f(d)-f(d)=f'(\alpha)(d-c)=\begin{cases}0&\text{if }f'(x)=0\\\geq0&\text{if }f'(x)\geq0\\\leq0&\text{if }f'(x)\leq0\end{cases}$$Hence we get:$$\Huge f(d)=\begin{cases}f(c)&\text{if }f'(x)=0\\\geq f(c)&\text{if }f'(x)\geq0\\\leq f(c)&\text{if }f'(x)\leq0\end{cases}$$Which proves our cases for constant, increasing, and decreasing functions.

## Cauchy's generalised MVT:
Let $f,g:[a,b]\mapsto\Re$ be continuous and differentiable on interior points. Assume that $g'(x)\neq0\forall x\in(a,b)$. Then there exists $c\in(a,b)$ such that:$$\Huge \frac{f'(c)}{g'(c)}=\frac{f(b)-f(a)}{g(b)-g(a)}$$Note that the MVT is a special case where $g(x)=x$. To prove this, consider $h(x)=(g(b)-g(a))f(x)-(f(b)-f(a))g(x)$, which is continuous on $[a,b]$ and differentiable on $(a,b)$ since $f,g$ are both continuous and differentiable.$$\Huge h(a)=(g(b)-g(a))f(a)-(f(b)-f(a))g(a)=g(b)f(a)-f(b)g(a)=h(b)$$Now we can use Rolle's theorem on $h$. So we get that $\exists c\in(a,b)$ with $h'(c)=0$:$$\Huge h'(c)=0=(g(b)-g(a))f'(c)-(f(b)-f(a))g'(c)$$$$\Huge \implies f'(c)(g(b)-g(a))=g'(c)(f(b)-f(a))\implies\frac{f'(c)}{g'(c)}=\frac{f(b)-f(a)}{g(b)-g(a)}$$Note that neither $g'(c)=0$ (by assumption) or $g(b)-g(a)=0$ by MVT.

# L'Hopital's rule:

Let $f,g$ be differentiable functions in some interval $(a,b)$. Assume that both $\lim_{x\to a^+}f(x)=0$ and $\lim_{x\to a^+}g(x)=0$ and $g(x),g'(x)\neq0$ for all $x$, then if $\lim_{x\to a^+}\frac{f'(x)}{g'(x)}$ exists, then $\lim_{x\to a^+}\frac{f(x)}{g(x)}$ also exists with:$$\Huge \lim_{x\to a^+}\frac{f(x)}{g(x)}=\lim_{x\to a^+}\frac{f'(x)}{g'(x)}$$This also holds for the other endpoint, and any interior points, as well as a two sided limit. Limits to infinity also work. To prove this, extend $f$ and $g$ to $x=a$ by setting $f(a)=g(a)=0$, preserving continuity. It is enough to show that $\lim_{n\to\infty}\frac{f(x_n)}{g(x_n)}=L=\lim_{x\to a^+}\frac{f'(x)}{g'(x)}$ for all sequences $(x_n)_{n\in\mathbb N}\in(a,b)$ with $\lim_{n\to\infty}x_n=a$. By the generalised MVT, we can find $y_N\in(a,x_n)$ with:$$\Huge \frac{f'(y_n)}{g'(y_n)}=\frac{f(x_n)-f(a)}{g(x_n)-g(a)}$$We know $a<y_n<x_n$, so by squeezing theorem we know $y_n\to a$ as $n\to\infty$, then:$$\Huge L=\lim_{n\to\infty}\frac{f'(y_n)}{g'(y_n)}=\lim_{n\to\infty}\frac{f(x_n)-f(a)}{g'(x_n)-g(a)}=\lim_{n\to\infty}\frac{f(x_n)}{g(x_n)}$$As required. There is a simple proof in the case that $f,g$ are differentiable at $a$ such that $f(a)=g(a)=0$ and $g'(a)\neq0$:$$\large \lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f(x)-f(a)}{g(x)-g(a)}=\lim_{x\to a}\left(\frac{f(x)-f(a)}{x-a}\times\frac{x-a}{g(x)-g(a)}\right)=\lim_{x\to a}\frac{f'(x)}{g'(x)}$$
# Taylor's theorem:

Let $f:I\mapsto\Re$ be a function differentiable $n$ times on $I$, and let $c\in I$. Then there exists a function $r_n(x)$ such that:$$\large f(x)=f(c)+f'(c)(x-c)+\frac{f''(c)}{2}(x-c)^2+\dots+\frac{f^{(n)}(c)}{n!}(x-c)^n+r_n(x)(x-c)^{n+1}$$With $\lim_{x\to c}r_n(x)=0$. This is called the Peano form of the remainder. If additionally, $f$ is $n+1$ times differentiable on $I$, then:$$\large f(x)=f(c)+f'(c)(x-c)+\frac{f''(c)}{2}(x-c)^2+\dots+\frac{f^{(n)}(c)}{n!}(x-c)^n+\frac{f^{(n+1)}(\zeta)}{(n+1)!}(x-\zeta)^{n+1}$$Is called the Lagrange form of the remainder.
Proof:![[Differentiable Functions .excalidraw]]