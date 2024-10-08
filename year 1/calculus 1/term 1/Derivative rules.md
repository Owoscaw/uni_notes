
# Leibniz rule:

If $f,g$ are both [[Derivative as a limit#Differentiability|differentiable]] $n$ times, then $fg(x)$ is also differentiable $n$ times. We have:$$\Huge D(fg)=(Df)g+f(DG)$$
$$\Huge D^2(fg)=(D^2f)g+2(Df)(Dg)+f(D^2g)$$
This is following the [[Combinations#Pascals triangle and Binomial theorem|binomial]] coefficients. This leads to the definition of the general Leibniz rule:
$$\Huge D^n(fg)=\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}(D^kf)(D^{n-k}g)$$
Example:![[Leibniz and Chain rules]]
# Chain rule:

For differentiating the composition $f\circ g$, the chain rule can be used. Given $g(x)$ is differentiable at $x$, and $f(x)$ is differentiable at $g(x)$, then:$$\Huge (f\circ g)^{\prime}(x)=f^{\prime}(g(x))g^{\prime}(x),\,\text{or},\,\frac{d}{dx}f(g(x))=\frac{df}{dg}\frac{dg}{dx}=\frac{df(g)}{dg}\frac{dg(x)}{dx}$$

# L'Hopital's rule:

By the [[Limits and Continuity#Consequences of continuity|calculus of limits theorem]] (COLT), for $\lim_{x\to a}f(x)=L$, $\lim_{x\to a}g(x)=M$:
$$\Huge \lim_{x\to a}\frac{f(x)}{g(x)}=\frac{L}{M}$$
If $M=0$, $L\neq 0$, then this limit does not exist. However if $L=M=0$, then the limit is in indeterminant form. A limit is in indeterminant form if it takes the "value":
> $\frac{0}{0}$
> $\frac{\infty}{\infty}$
> $0\times\infty$
> $\infty-\infty$
> $0^0$
> $1^{\infty}$
> $\infty^0$

L'Hopital's rule applies to the first two indeterminant forms and states that for two differentiable functions $f,g$ on the interval $I=(a-h,a)\cup (a,a+h)$ for some $h>0$, with $\lim_{x\to a}f(x)=\lim_{x\to a}g(x)=0$ and $\lim_{x\to a}\frac{f^{\prime}(x)}{g^{\prime}(x)}$ exists and $g^{\prime}(x)\neq 0\,\,\forall x\in I$:$$\Huge \lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f^{\prime}(x)}{g^{\prime}(x)}$$
This can be shown, adding the restrictions that $f$ and $g$ are continuous and differentiable at $a$ and that $g^{\prime}(a)\neq 0$:
$$ \lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f(x)-f(a)}{g(x)-g(a)}=\lim_{x\to a}\frac{\frac{f(x)-f(a)}{x-a}}{\frac{g(x)-g(a)}{x-a}}=^{COLT}\frac{\lim_{x\to a}\frac{f(x)-f(a)}{x-a}}{\lim_{x\to a}\frac{g(x)-g(a)}{x-a}}=\frac{f^{\prime}(a)}{g^{\prime}(a)}=\lim_{x\to a}\frac{f^{\prime}(x)}{g^{\prime}(x)}$$
L'Hopital's rule can be repeatedly applied if conditions remain to be met.



