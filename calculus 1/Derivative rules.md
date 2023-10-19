
# Leibniz rule:

If $f,g$ are both [[Derivative as a limit#Differentiability|differentiable]] $n$ times, then $fg(x)$ is also differentiable $n$ times. We have:$$\Huge D(fg)=(Df)g+f(DG)$$
$$\Huge D^2(fg)=(D^2f)g+2(Df)(Dg)+f(D^2g)$$
This is following the [[Combinations#Pascals triangle and Binomial theorem|binomial]] coefficients. This leads to the definition of the general Leibniz rule:
$$\Huge D^n(fg)=\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}(D^kf)(D^{n-k}g)$$
Example:![[Leibniz and Chain rules .excalidraw]]
# Chain rule:

For differentiating the composition $f\circ g$, the chain rule can be used. Given $g(x)$ is differentiable at $x$, and $f(x)$ is differentiable at $g(x)$, then:$$\Huge (f\circ g)^{\prime}(x)=f^{\prime}(g(x))g^{\prime}(x),\,\text{or},\,\frac{d}{dx}f(g(x))=\frac{df}{dg}\frac{dg}{dx}=\frac{df(g)}{dg}\frac{dg(x)}{dx}$$

# L'Hopital's rule:

By the [[Limits and Continuity#Consequences of continuity|calculus of limits theorem]] (COLT):$$\Huge \lim$$
