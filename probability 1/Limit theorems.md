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

# Moment Generating functions:

For any real valued random variable $X$, the function $M_X:\Re\mapsto[0,\infty]$ is given by:$$\Huge M_X(t)=\mathbb E[e^{tx}]\,\,\forall t\in\Re$$
Using LOTUS, we can derive the following definitions for $M_X(t)$:$$\Huge M_X(t)=\begin{cases}\displaystyle{\sum_{x\in\mathcal X}e^{tx}p(x)}&\text{if X is discrete}\\\displaystyle{\int_{-\infty}^\infty e^{tx}f(x)}&\text{if X is continuous}\end{cases}$$
Note that $M_X(t)\geq 0$ but can take the value $+\infty$. Consider the [[Taylor series#Taylor polynomials|taylor expansion]] for $e^{tx}$:$$\Huge e^{tx}=1+tx+\frac{t^2x^2}{2!}+\dots\implies\mathbb E(e^{tx})=1+t\mathbb E(X)+\frac{t^2}{2!}\mathbb E(X^2)+\dots$$
Here, each $\mathbb E(X)$ is known as the moment. Increasing powers of $X$ inside the expectation products the next moment. For example $\mathbb E(X)$ is the first moment, $\mathbb E(X^2)$ is the second moment, et cetera. $\mathbb E(X^k)$ are the moments of $X$. The moment generating function has the following properties:
> It follows that differentiating this Taylor polynomial $k$ times will product the $k$th moment of $X$:$$\Huge M_X^{(k)}(0)=\frac{d^k}{dt^k}M_X(T)|_{t=0}=\mathbb E(X^k)$$
> If $X,Y$ are two random variables with moment generating functions $M_X,M_Y$ respectively, then there is some $h>0$ such that:$$\Huge M_X(t)=M_Y(t)<\infty,\,\,\text{for all}\,\,|t|<h$$Then $X$ and $Y$ have the same distribution, that is $F_X(x)=F_Y(x)$ for all $x\in\Re$
> For $a,b\in\Re$:$$\Huge M_{aX+b}(t)=e^{bt}M_X(at)$$
> If $X_1,\dots,X_n$ are independent random variables and $S_n=\sum_{i=1}^nX_i$ then:$$\Huge M_{S_n}(t)=\prod_{i=1}^nM_{X_i}(t)$$
> Suppose that $X,X_1,X_2,\dots$ are random variables. If there exists $h>0$ such that:$$\Huge \lim_{n\to\infty}M_{X_n}(t)=M_X(t)<\infty\,\,\text{for all }\,\,|t|<h$$Then $X_n$ converges in distribution to $X$.

One can show that the CDF of any any random variable has at most a countable number of points where the CDF is not continuous. To see this consider:$$\Huge D_n=\left\{x\in\Re:F(x)-F(x-)>\frac{1}{n}\right\}$$
This is the set of points, $x$, where $F(x)$ has a jump of at least size $1/n$. The discontinuous points of $F$ can then be expressed as:$$\Huge D=\bigcup_{n\in\mathbb N}D_n$$Consider that $D_n$ is a finite set as $F$ is non-decreasing (since its a CDF). Note $D_n$ is of size at most $n$, otherwise the jumps would sum to a size of more than $1$, which is impossible for a CDF. This makes $D$ a countable union of finite sets, which must be countable.

# Proof of CLT:

We need to show that for:$$\Huge Z_n=\sum_{i=1}^n\frac{X_i-\mu}{\sigma\sqrt{n}},\,\,\text{we have}\,\,M_{Z_n}(t)\to e^{\frac{t^2}{2}}$$For all $t$ on an open interval containing $0$. This converges to and characterises the CLT. Let $Y_i=(X_i-\mu)/\sigma$ and denote the MGF of $Y_i$ by $m(t)$. Then we have that $Y_i/\sqrt{n}$ will have $m(t/\sqrt{n})$, and that $\sum_{i=1}^nY_i/\sqrt{n}$ is given by:$$\Huge M_{Z_n}(t)=(m(t/\sqrt{n}))^n$$Using the moment generating property of $m(t/\sqrt{n})$ we have:$$\Huge m(0)=\mathbb E(Y_i^0)=1,\,m'(0)=\mathbb E(Y_i)=0,\,m''(0)=\mathbb E(Y_i^2)=1$$So by [[Taylor series#Taylor's theorem|Taylor's theorem]] we have that there exists a function $h$ around $0$ with $$