
In studying [[Green's method#Green's function via delta function|Green's function]] we defined the delta "function" which is, at best, a limit of functions. We saw that it was defined by acting with another function to "sift out" the value at zero:$$\Huge\int_\Re\delta(x)f(x)dx=f(0)$$where $f$ is any bounded, smooth function. This can also be defined in terms of an [[Inner product spaces|inner product]]:$$\Huge \langle \delta,\phi\rangle=\phi(0)$$where $\delta$ is the delta distribution and $\phi$ is the test function.

# Test functions:

A test function $\phi$ is a function:$$\Huge \phi:\Re\rightarrow\Re,\,\,\phi\in C_0^\infty(\Re)$$That is, a test function has the properties:
> Infinitely differentiable ($C^\infty$)
> Compact support ($C_0$), that is there is some $X$ such that $f(x)=0$ for all $x\notin[-X,X]$

The first property allows for any order derivative of a distribution to be taken, and the second allows manipulation through integration by parts with no boundary conditions. For example, the "bump" function defined as:$$\Huge \phi_{C;\epsilon}=\begin{cases}\exp\left(-\frac{C}{\epsilon^2-(x-a)^2}\right)&a-\epsilon<x<a+\epsilon\\0&\text{otherwise}\end{cases}$$for $C,\epsilon>0$. One can show that:$$\Huge\begin{align}
\lim_{x\to (a+\epsilon)^+}\frac{d}{dx^n}\phi_{C;\epsilon}(x)&=0\\
\lim_{x\to(x-\epsilon)^-}\frac{d}{dx^n}\phi_{C;\epsilon}(x)&=0
\end{align}$$that is, the function is infinitely differentiable everywhere including where the piecewise definitions join. If this function is multiplied by some other function that does not necessarily have compact support, then the product $\phi_{C;\epsilon}(x)g(x)$ will have compact support.

# Weak derivatives:

Let $u(x)$ be continuously differentiable such that there is some $f(x)$ for which $\frac{du}{dx}=f$. Now we take the integral:$$\Huge \int_\Re u'\phi\,dx=\int_\Re f\phi\,dx$$for some test function $\phi$. Now integrating by parts gives:$$\Huge [u\phi]_{-\infty}^\infty-\int_\Re u\phi'dx=-\int_\Re u\phi'dx=\int_\Re f\phi\,dx$$where we have used the compact support property of $\phi$ to make the first term vanish. We take this as the definition of the weak derivative, that is $f$ is the weak derivative of $u$ if the above condition is met.