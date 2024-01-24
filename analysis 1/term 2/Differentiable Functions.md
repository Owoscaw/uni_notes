
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

Let $f:[a,b]\mapsto\Re$ be continuous and differentiable on $(a,b)$ and suppose that $f(a)=f(b)$ then there exists $c\in(a,b)$ such that $f'(c)=0$. Since $f$ is continuous 