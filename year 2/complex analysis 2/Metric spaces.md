
A metric space is a set $X$ together with a function $d:X\times X\mapsto\Re_{\geq0}$ such that for all $x,y,z\in X$:
>Positivity: $d(x,y)=0\iff x=y$
>Symmetry: $d(x,y)=d(y,x)$
>Triangle inequality: $d(x,y)\leq d(x,z)+d(z,y)$

$X$ is the set with elements that we want to find the distance of, and $d(x,y)$ is the distance between points $x$ and $y$. The function $d$ is called a metric, a metric space is often denoted as $(X,d)$. Examples of metrics:
> On $\Re$ or $\mathbb{C}$, $d(x,y)=|x-y|$, where $|x|$ is the modulus, or absolute value of $x$
> On $\Re^n$ or $\mathbb{C}^n$, $d_{EUC}((x_1,\dots,x_n),(y_1,\dots,y_n))=\sqrt{\sum_{i=1}^n|x_i-y_i|^2}$
> A metric on $\mathbb{C}$ can be defined by using the [[The complex plane and Riemann Sphere#The Riemann Sphere|stereographic projection]]. This is known as the Riemannian metric:$$\Huge d_{\text{Chordal}}(z,\omega)=d_{EUC}(P^{-1}(z),P^{-1}(\omega))$$This metric also works on $\hat{\mathbb{C}}$.
> The discrete metric on a set $X$ is defined as $d(x,y)=\begin{cases}0&x=y\\1&x\neq y\end{cases}$

Most of these examples were on vector spaces and said metric is derived from a notion of length. We call this notion of length a norm. Given any real or complex vector space, $V$, a function $||\cdot||:V\mapsto\Re_{\geq0}$ is a norm if it satisfies for all $v,w\in V$:
>$||v||\geq0$ and $||v||=0\iff v=0$
>$||\lambda v||=|\lambda|\cdot||v||$ for $\lambda\in\mathbb{C}$
>$||v+w||\leq||v||+||w||$

A vector space combined with a norm is called a normed vector space. Any norm induces a metric given by:$$\Huge d(v,w):=||v-w||$$

# Taxicab norm:

The $l_p$ norm, with $1\leq p<\infty$ on $\Re^n$ or $\mathbb{C}^n$ is given by:$$\Huge || \underline x||_p=\left(\sum_{i=0}^n|x_i|^p\right)^{\frac{1}{p}}$$Note that $d_{EUC}=l_2$. This norm comes from the dot product on $\Re^n$. In general if $X$ has an inner product, then $||v||=\sqrt{\left<v,v\right>}$ is a norm. Note that when $p\neq 2$, the norm does not come from an inner product.

When $p=1$ on $\Re^2$, we have that $||(x,y)||_l=|x|+|y|$. Consider the limiting case, the $l_{\infty}$ or "sup norm", on $\Re^n$:$$\Huge ||\underline x||_{\infty}=\max$$