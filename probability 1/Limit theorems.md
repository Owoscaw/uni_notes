# Weak law of large numbers:

Consider a coin tossed $n$ times, with probability of heads on each toss being $p$. Let $X$ denoted the number of heads and $B_n:=\frac{X}{n}$ be the proportion of heads tossed. Since $X\sim Bin(n,p)$, then the [[Expectation#Definition and interpretation|expectation]] and [[Expectation#Variance and Co-Variance|variance]] are given by $np,np(1-p)$ respectively. We also get:$$\Huge \mathbb E[B_n]=\frac{\mathbb E[x]}{n}=p,\,\,var(B_n)=\frac{Var(X)}{n^2}=\frac{p(1-p)}{n}$$
So by [[Expectation#Inequalities|Chebychev's]] inequality, for any $\epsilon>0$:$$\Huge \mathbb P(|B_n-p|\geq \epsilon)\leq\frac{p(1-p)}{n\epsilon^2}$$
Note that the LHS tends to zero as $n$ tends to infinity. This is interpreted as the sample proportion having a very high probability within any small interval centred on $p$.

Suppose an infinite sequence of independent random variables, $X_1,X_2,\dots$, with the same mean and variance. Then we write:$$\Huge \mathbb E[X_i]=\mu,\,\,var(X_i)=\sigma^2\,\,\forall i$$
Consider the sample average $\overline X_n:=\frac{1}{n}\sum_{i=1}^nX_i$, then for any $\epsilon>0$:$$\Huge \lim_{n\to\infty}\mathbb P(|\overline X_n-\mu|>\epsilon)=0$$
This is interpreted as being very close to the expected value $\mu$ for large $n$. This type of convergence is known as convergence in probability. The weak law of large numbers states that $\overline X_n$ converges in probability to $\mu$. This is proven by the application of Chebyshev's inequality, then taking the limit.

# The central limit theorem:

Suppose a sequence of identically distributed independent variables, $X_1,X_2,\dots$. Then let $\mathbb E[X]=\mu,var(X)=\sigma^2,\,\sigma>0$. Define the following:$$\Huge S_n=\sum_{i=1}^nX_i,\,\,\overline X_n=\frac{S_n}{n}$$
Then for any $z\in\Re$:$$\Huge Z_n:=\frac{S_n-n\mu}{\sigma\sqrt{n}}=\frac{\overline X_n-\mu}{\sigma/\sqrt{n}}$$$$\Huge \lim_{n\to\infty}F_{Z_n}(z)=\lim_{n\to\infty}\mathbb P(Z_n\leq z)=\Phi(z)$$
Here, $Z_n$ converges in distribution to the [[Random variables#Normal distribution|standard normal distribution]].

# Normal approximations:

Let $X_n\sim Bin(n,p), B_n=\frac{X_n}{n}$ and:$$\Huge Z_n=\frac{X_n-np}{\sqrt{np(1-p)}}=\frac{B_n-p}{\sqrt{p(1-p)/n}}$$
Then:$$\Huge \lim_{n\to\infty}\mathbb P(Z_n\leq z)=\Phi(z)\,\,\forall z\in\Re$$
This is proven by applying the central limit theorem. Let $X_1,X_2,\dots$ be identically distributed independent random variables. Let $S_n=\sum_{i=1}^nX_i$, we know that $\mathbb E[S_n]=np$ and $var(S_n)=\sum_{i=1}^nvar(X_i)=n\,var(X_1)=np(1-p)$. Applying the theorem gives the result above for $Z_n$, which gives the approximation as required. So for large enough $n$ and $0<p<1$:$$\Huge \mathbb P(X\leq x)\approx\Phi\left(\frac{x-np}{\sqrt{np(1-p)}}\right)$$

# Generating functions:

For any real valued random variable $X$, the function $M_X:\Re\mapsto[0,\infty]$ is given by:$$\Huge M_X(t)=\mathbb E[e^{tx}]\,\,\forall t\in\Re$$
Using LOTUS, we can derive the following definitions for $M_X(t)$:$$\Huge M_X(t)=\begin{cases}\displaystyle{\sum_{x\in\mathcal X}e^{tx}p(x)}&\text{if X is discrete}\\\displaystyle{\int_{-\infty}^\infty e^{tx}f(x)}&\text{if X is continuous}\end{cases}$$
Note that $M_X(t)\geq 0$ but can take the value $+\infty$.