
# Definitions/Axioms:

A random variable $X$ takes values in $\mathcal{S}$, the set of possible outcomes. This set can be either discrete or continuous. Consider a single random variable, with $X\in\Re=\mathcal{S}$. We then define the probability density by$$\huge\text{Prob}(X\in[x,x+dx])=p(x)dx$$, where $p(x)$ full characterises the distribution. $p$ should always be positive and integral normalised $\int_\Re p(x)=1$:
> We can then define probability an expectation values:$$\Large\begin{aligned}
\text{prob}(X\in[a,b])&=\int_a^bp(x)dx\\
\langle F(X)\rangle&=\int p(x)F(x)dx
\end{aligned}$$$F(X)$ is therefore also a random variable, with its own measure:$$\Large\text{prob}(F(X)\in[f,f+df])=p_F(f)df$$We can calculate this measure from the underlying PDF for $x$. Consider the solutions $x_i$ to $F(x_i)=f$:$$\Large p_F(f)df=\sum_Ip(x_i)dx\implies p_F(f)=\sum_i p(x_i)\left|\frac{dx}{dF}\right|_{x=x_i}$$Note the derivative terms in the sum are just the Jacobians associated with a change of variable $x\to f$. 
> We can also define the $n$-th moment of a random variable $x$ as the expectation of $x^n$:$$\Large m_n=\langle x^n\rangle=\int p(x)x^ndx$$
> The characteristic function $\tilde p(k)$ is also defined through the expectation value$$\Large \tilde p(k)=\langle e^{-ikx}\rangle=\int p(x)e^{-ikx}dx$$and can be thought of as the Fourier transform of $p(x)$. Notably, we can easily invert the Fourier transform to recover the original distribution from the characteristic function:$$\Large p(x)=\frac{1}{2\pi}\int\tilde p(k)e^{ikx}dk$$Writing the exponential in summation form, we see that the characteristic function can be expanded to provide moments:$$\Large\tilde p(k)=\int p(x)\sum_{n=0}^\infty\frac{(-ik)^n}{n!}x^ndx=\sum_{n=0}^\infty\frac{(-ik)^n}{n!}\langle x^n\rangle$$
> Cumulant generating functions are defined as the logarithm of characteristic functions. These functions generate cumulants $\langle x^n\rangle_c$ when expanded in powers of $k$. We define cumulants through the following:$$\Large\log\tilde p(k)=\sum_{n=1}^\infty\frac{(-ik)^n}{n!}\langle x^n\rangle_c$$These contain a lot of useful information about the distribution. The information from moments is actually the same as those in cumulants. Explicitly taking the logarithm$$\Large
\log\tilde p(k)=\log\left(\sum_{n=0}^\infty\frac{(-ik)^n}{n!}\langle x^n\rangle\right)$$, one can use the expansion for $\log(1+\epsilon)$ and equation terms to find:$$\Large\begin{aligned}
\langle x\rangle_c&=\langle x\rangle&\text{mean}\\
\langle x^2\rangle_c&=\langle x^2\rangle-\langle x\rangle^2&\text{variance }\sigma^2\\
\langle x^3\rangle_c&=\langle x^3\rangle-3\langle x^2\rangle\langle x\rangle+2\langle x\rangle^3&\text{skewness}
\end{aligned}$$

# Notable distributions:

## Gaussian:
The normal, or Gaussian, distribution for a single continuous variable $x$ is defined as:$$\Large p(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\lambda)^2}{2\sigma^2}\right)$$This is the bell curve, with mean $\lambda$ and width $\sigma$. More precisely, let us calculate the characteristic function:$$\Large\begin{aligned}
\tilde p(k)&=\int\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-ikx-\frac{(x-\lambda)^2}{2\sigma^2}\right)dx\\
_\text{completing the square}&=\int\frac{1}{\sigma\sqrt{2\pi}}\exp\left(\frac{(x-\lambda-ik\sigma^2)^2}{2\sigma^2}-\frac{\sigma^2k^2}{2}-ik\lambda\right)dx\\
_{\text{shift in }x\text{, normalise}}&=\exp\left(-\frac{k^2\sigma^2}{2}-ik\lambda\right)
\end{aligned}$$