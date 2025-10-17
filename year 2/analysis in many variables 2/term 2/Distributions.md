
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

Take for example the Heaviside step function:$$\Huge \langle H,\phi\rangle=\int_\Re H(x)\phi(x)dx=\int_0^\infty\phi(x)dx=\int_0^X\phi(x)dx$$for a test function $\phi(x)$ with compact support on $[-X,X]$. We now see:$$\Huge |\langle H,\phi\rangle|=\left|\int_0^X\phi(x)dx\right|\leq\int_0^X|\phi(x)|dx\leq X\max_{0\leq x\leq X}|\phi(x)|$$so we have continuity with $N=0$ and $C=X$.

All distributions that are induced by integrable $f$ are called regular distributions, otherwise they are called singular. Singular distributions $\langle u,\phi\rangle$ are induced by functions $u$ that are not well defined outside the integral definition, like the delta distribution.

# Operations on distributions:

## Linear combinations:
Let $u_1,u_2,u$ be distributions, $f_1,f_2,f$ be locally integrable functions, and $\alpha_1,\alpha_2\in\Re$. Then we have:$$\Huge\begin{align}
\langle \alpha_1f_1+\alpha_2f_2,\phi\rangle&=\int_\Re(\alpha_1f_1+\alpha_2f_2)\phi\,dx\\
&=\alpha_1\int_\Re f_1\phi\,dx+\alpha_2\int_\Re f_2\phi\,dx\\
&=\alpha_1\langle f_1,\phi\rangle+\alpha_2\langle f_2,\phi\rangle
\end{align}$$This is well defined as $f_1,f_2$ are integrable and induce regular distributions. We ask if the linear combination of $\alpha_1u_1+\alpha_2u_2$ is also well defined. Obviously, the distribution induced by this linear combination has the same form as above, however we must check continuity, that is:$$\Huge |\langle \alpha_1u_1+\alpha_2u_2,\phi\rangle|\leq C\sum_{m\leq N}\max_{-X\leq x\leq X}\left|\frac{d^m\phi}{dx^m}\right|$$for some $C>0,N\geq0$ where $\phi$ is a test function supported on $[-X,X]$. As $\alpha_1\langle u_1,\phi\rangle,\alpha_2\langle u_2,\phi\rangle$ are singular distributions themselves, we know that:$$\Huge\begin{align}
|\alpha_1\langle u_1,\phi\rangle|&\leq C_1\sum_{m\leq N_1}\max_{-X\leq x\leq X}\left|\frac{d^m\phi}{dx^m}\right|\\
|\alpha_2\langle u_2,\phi\rangle|&\leq C_2\sum_{m\leq N_2}\max_{-X\leq x\leq X}\left|\frac{d^m\phi}{dx^m}\right|
\end{align}$$for some $C_1,C_2>0$ and $N_1,N_2\geq0$. Now let $\alpha_\text{max}=\max(\alpha_1,\alpha_2),C_\text{max}=\max(C_1,C_2),N_\text{max}=\max(N_1,N_2)$:$$\Huge\begin{align}
|\langle \alpha_1u_2+\alpha_2u_2,\phi\rangle|&=|\alpha_1\langle u_1,\phi\rangle+\alpha_2\langle u_2,\phi\rangle|\\
&\leq|\alpha_1||\langle u_1,\phi\rangle|+|\alpha_2||\langle u_2,\phi\rangle|\\
&\leq2|\alpha_\text{max}|C_\text{max}\sum_{m\leq N_\text{max}}\max_{-X\leq x\leq X}\left|\frac{d^m\phi}{dx^m}\right|
\end{align}$$which satisfies the definition of continuity with $C=2|\alpha_\text{max}|C_\text{max}$ and $N=N_\text{max}$.

## Distributional derivatives:
For a general distribution $u$ we defined the notion of the weak derivative:$$\Huge \langle u',\phi\rangle=-\langle u,\phi'\rangle\,\,\forall\phi\in C_0^\infty(\Re)$$We see that $u':\phi\rightarrow-\langle u,\phi'\rangle$ is also a distribution as $u$ itself is a distribution and $\phi'\in C_0^\infty(\Re)$ by definition. Using this we can check that the derivative of the Heaviside function is indeed the delta function:$$\Huge\begin{align}
\langle H',\phi\rangle&=-\langle H,\phi'\rangle\\
&=-\int_\Re H(x)\phi'(x)dx\\
&=-\int_0^\infty\phi'(x)dx\\
&=\phi(0)-\phi(\infty)\\
&=\phi(0)
\end{align}$$where we have used the fact that $\phi$ is a test function and therefore must vanish at infinity by compact support. So we have that $\langle H',\phi\rangle=\phi(0)$, which is the definition of the delta function. So we have that the Heaviside function is indeed the weak derivative (at least) of the delta function.

## Translations:
For a distribution $u$ and $a\in\Re$ we have:$$\Huge \langle u(x-a),\phi(x)\rangle=\langle u(x),\phi(x+a)\rangle$$which is proven by taking $y=x-a$ and noticing that $\langle ,\rangle$ is translation invariant.

## Multiplication:
Let $a(x)$ be infinitely differentiable, then:$$\Huge \langle au,\phi\rangle=\langle u,a\phi\rangle$$Trivial.

## Convergence:
Let $u_1,u_2,\dots$ be a sequence of distributions. Convergence of $u_j\to u$ as $j\to\infty$ means that:$$\Huge \lim_{j\to\infty}\langle u_j,\phi\rangle=\langle u,\phi\rangle$$Similarly if $u(\alpha)$ is a family of distributions dependent on $\alpha$ and $u(\alpha)\to u(\alpha_0)$ as $\alpha\to\alpha_0$ then we have:$$\Huge \lim_{\alpha\to\alpha_0}\langle u(\alpha),\phi\rangle=\langle u(\alpha_0),\phi\rangle$$

# Distributed solutions:

Consider an equation:$$\Huge Lu=a_2(x)u''+a_1(x)u'+a_0(x)u=f$$A distributed solution to this equation is defined as:$$\Huge\begin{align}
\langle Lu,\phi\rangle&=\langle a_2u'',\phi\rangle+\langle a_1u',\phi\rangle+\langle a_0u,\phi\rangle\\
&=\langle u,(a_2\phi)''\rangle-\langle u,(a_1\phi)'\rangle+\langle u,a_0\phi\rangle\\
&=\langle u,L^*\phi\rangle
\end{align}$$where $L^*$ is the formal [[Eigenfunction methods#Adjoint operators|adjoint operator]]. In this case we call $u$ a distributed solution to $Lu=f$ if $\langle u,L^*\phi\rangle=\langle f,\phi\rangle$ for all $\phi\in C_0^\infty(\Re)$.

Take for example the differential equation:$$\Huge Lu=u''+u=0$$We show that $u=\cos x$ is a distributed solution in the following manner:$$\Huge\begin{align}
\langle u,L^*\phi\rangle&=\langle \cos x,\phi''+\phi\rangle\\
&=\int_\Re\frac{d^2\cos x}{dx^2}\phi+\cos x\,\phi\,dx\\
&=\int_\Re\phi(-\cos x+\cos x)dx=0
\end{align}$$where we used integration by parts twice on the $\cos x\,\phi''$ term. So $u=\cos x$ indeed fits the description of a distributed solution.

This definition is not trivial when considering [[Green's method]]. In this case we solve:$$\Huge \langle Lg,\phi\rangle=\langle \delta(x-\xi),\phi\rangle$$which has distributed solution:$$\Huge \langle g(x,\xi),L^*\phi\rangle=\phi(\xi)$$