
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

Let $u(x)$ be continuously differentiable such that there is some $f(x)$ for which $\frac{du}{dx}=f$. Now we take the integral:$$\Huge \int_\Re u'\phi\,dx=\int_\Re f\phi\,dx$$for some test function $\phi$. Now integrating by parts gives:$$\Huge [u\phi]_{-\infty}^\infty-\int_\Re u\phi'dx=-\int_\Re u\phi'dx=\int_\Re f\phi\,dx$$where we have used the compact support property of $\phi$ to make the first term vanish. We take this as the definition of the weak derivative, that is $f$ is the weak derivative of $u$ if the above condition is met for all test functions $\phi\in C_0^\infty(\Re)$. If $u$ is normally differentiable, then this definition gives the same result, however this definition applies even when $u$ is not differentiable in the normal way. Compact support allows smaller intervals than $\Re$ to be used.

# Distributions defined:

A distribution $u$ is a functional mapping test functions to real numbers:$$\Huge u:\phi\in C_0^\infty(\Re)\rightarrow \langle u,\phi\rangle\in\Re$$where the mapping is linear and continuous. We therefore get the properties:
> Linearity, $\langle u,\alpha\phi+\beta\psi\rangle=\alpha \langle u,\phi\rangle+\beta \langle u,\psi\rangle$ for all $\alpha,\beta\in\Re$ and $\phi,\psi\in C_0^\infty(\Re)$
> Continuity, if $\phi_n$ is a sequence of test functions that converges to $0$, then $\phi_n(x)\to0$ as $n\to\infty$ and $\langle u,\phi_n\rangle\to0$. Continuity is defined this way so that distributions converge when the test functions converge, the convergence is inherited from the test functions. That is, we require:$$\Huge \lim_{n\to\infty}\langle u,\phi_n\rangle=\langle u,\lim_{n\to\infty}\phi_n\rangle$$One can show that this holds if for all $X>0$ there exists some $C>0$ and $N\geq0$ such that:$$\Huge |\langle u,\phi\rangle|\leq C\sum_{m\leq N}\max_{-\infty\leq x\leq\infty}\left|\frac{d^m\phi}{dx^m}\right|$$for all $\phi$ with compact support in $[-X,X]$.

Take the delta distribution for example. Linearity is obvious, for continuity we have:$$\Huge |\langle \delta,\phi\rangle|=|\phi(0)|\leq\max_{-X\leq x\leq X}|\phi(x)|$$which is true for all $\phi$ with support $[-X,X]$ so we satisfy continuity with $C=1,N=0$.

Assume $f(x)$ is locally integrable, then there is a natural definition of its distribution:$$\Huge \langle f,\phi\rangle=\int_\Re f(x)\phi(x)dx$$We first check that this satisfies continuity. Let $X>0$ be the compact support of $\phi$, then define:$$\Huge C(X)=\int_{-X}^X|f(x)|dx$$This is assumed to be finite as $f$ is locally integrable. Now let $N=0$ and we have:$$\large |\langle f,\phi\rangle|=\left|\int_{-X}^Xf(x)\phi(x)dx\right|\leq\int_{-X}^X|f(x)||\phi(x)|dx\leq\max_{-X<x<X}|\phi(x)|\int_{-X}^X|f(x)|dx$$where we have used the compact support of $\phi$ and the [[Complex integration#Estimation lemma and contour length|estimation lemma]] to show that $|\langle f,\phi\rangle|\leq C\max_{-X<x<X}|\phi(x)|$, satisfying continuity with $C$ defined above and $N=0$. One can also show that this distribution is well defined and linear, making all locally integrable functions distributions.

Take for example the Heaviside step function:$$\Huge \langle H,\phi\rangle=\int_\Re H(x)\phi(x)dx=\int_0^\infty\phi(x)dx=\int_0^X\phi(x)dx$$for a test function $\phi(x)$ with compact support on $[-X,X]$. We now see:$$\Huge |\langle H,\phi\rangle|=\left|\int_0^X\phi(x)dx\right|\leq\int_0^X|\phi(x)|dx\leq X\max_{0\leq x\leq X}|\phi(x)|$$