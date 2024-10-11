
A metric space is a set $X$ together with a function $d:X\times X\mapsto\Re_{\geq0}$ such that for all $x,y,z\in X$:
>Positivity: $d(x,y)=0\iff x=y$
>Symmetry: $d(x,y)=d(y,x)$
>Triangle inequality: $d(x,y)\leq d(x,z)+d(z,y)$

$X$ is the set with elements that we want to find the distance of, and $d(x,y)$ is the distance between points $x$ and $y$. The function $d$ is called a metric, a metric space is often denoted as $(X,d)$. Examples of metrics:
> On $\Re$ or $\mathbb{C}$, $d(x,y)=|x-y|$, where $|x|$ is the modulus, or absolute value of $x$
> On $\Re^n$ or $\mathbb{C}^n$, $d_{EUC}((x_1,\dots,x_n),(y_1,\dots,y_n))=\sqrt{\sum_{i=1}^n|x_i-y_i|^2}$
> A metric on $\mathbb{C}$ can be defined by using the [[The complex plane and Riemann Sphere#The Riemann Sphere|stereographic projection]]. This is known as the Riemannian metric:$$\Huge d_{\text{Chordal}}(z,\omega)=d_{EUC}(P^{-1}(z),P^{-1}(\omega))$$This metric also works on $\hat{\mathbb{C}}$.