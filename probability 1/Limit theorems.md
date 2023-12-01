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