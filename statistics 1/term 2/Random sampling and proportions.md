# Bernoulli distribution:

When an experiment has binary outcome, that is a success or failure. We denote the two outcomes at $0$ or $1$. We then define the Bernoulli distribution with parameter $p\in[0,1]$ that has outcome either $0$ or $1$:$$\Huge P(X=1)=p,\,\,P(X=0)=1-p$$$$\Huge f(x|p)=\begin{cases}p^xq^{1-x}&\text{for }x=0,1\\0&\text{otherwise}\end{cases}$$Where $q=1-p$. Note that $f(1|p)=p,\,f(0|p)=q$. From this we calculate the expectation and variance:$$\Huge E[X]=\sum_{x=0}^1xf(x|p)=0\times q+1\times p=p$$$$\Huge E[X^2]=\sum_{x=0}^1x^2f(x|p)=0^2\times q+1^2\times p=p$$$$\Huge Var[X]=E[X^2]-E^2[X]=p-p^2=p(1-p)=pq$$We can also calculate the [[Limit theorems#Moment Generating functions|MGF]] also:$$\Huge \psi(t)=E[e^{tX}]=\sum_{x=0}^1e^{tx}f(x|p)=e^0\times q+e^t\times p=q+pe^t$$
## Bernoulli trials:
Given a sequence of $n$ random variables $X_1,\dots,X_n$ which are independent and identically distributed. If each $X_i$ has a Bernoulli distribution with parameter $p$ then we say $X_1,\dots,X_n$ form $n$ Bernoulli trials. This is a great model for the US presidential election.

# Statistical inference:

Often in statistics, the results of a real world experiment are taken and the statistician is asked to infer something meaningful about an underlying probability $p$. This probability can be thought of in one of two ways:
>$p$ is real with a fixed value that is unknown (frequentist)
>$p$ is an unknown quantity which should represent our subjective uncertainty (Bayesian)

For the first interpretation, an estimation of $p$ can be constructed from $X_1,\dots,X_n$. The attributes of this estimator can then be examined to determine its reliability.

# Totals and estimators:

Define $X$ as the total sum of all successes over $n$ trials:$$\Huge X=\sum_{i=1}^nX_n$$With each $X_i$ taking value $0$ or $1$, i.e. a Bernoulli distribution. Then we need to take the [[Frequentist methods#Continuous random variables|PMF]] of all $n$ trials:$$\Huge f(x_1,\dots,x_n|p)=\prod_{i=1}^nf(x_i|p)=\prod_{i=1}^np^{x_i}q^{1-x_i}=p^{\sum_{i=1}^nx_i}q^{\sum_{i=1}^n1-x_i}=p^xq^{n-x}$$Where $x=\sum_{i=1}^nx_i$. Note that the PMF only depends on $p,n$ and $x$. It is useful to estimate $p$ using only $n$ and $x$. Another way to frame this is to ask which estimate, $\hat p$, will maximise this PMF. $\log{f(x_1\,\dots,x_n|p)}$ is used because its easier to differentiate, and the maximum will occur at the same value since $\log x$ is monotonically increasing:$$\Huge \log{f(x_1,\dots,x_n|p)}=\log(p^xq^{n-x})=x\log p+(n-x)\log(1-p)$$$$\Huge\frac{\partial}{\partial p}\log{f(x_1,\dots,x_n|p)}=\frac{x}{p}-\frac{n-x}{1-p}$$Therefore an estimate, $\hat p$, for $p$ that maximises this expression is given by $\frac{\partial f}{\partial p}=0$:$$\Huge \frac{x}{\hat p}-\frac{n-x}{1-\hat p}=0\implies x(1-\hat p)=(n-x)\hat p\implies\hat p=\frac{x}{n}$$This is a very intuitive result. This estimate is also called the sample proportion, $Y$:$$\Huge \hat p=Y=\frac{X}{n}=\frac{1}{n}\sum_{i=1}^nX_i$$It follows that $Y\to\hat p$ as $n\to\infty$ by the[[Limit theorems#Weak law of large numbers|weak law of large numbers]] 

# The Binomial Distribution:

$X$ has a binomial distribution with parameters $n,p$ if $X$ is discrete with PMF:$$\Huge f(x|n,p)=\begin{cases}{n\choose x}p^xq^{n-x}&\text{for }x=0,1,\dots,n\\0&\text{otherwise}\end{cases}$$Where:
>$n$ is a positive integer
>$0\leq p\leq 1$
>$X\sim Bin(n,p)$

If the collection of random variables, $X_1,\dots,X_n$ form $n$ Bernoulli trials with parameter $p$ and if $X=X_1+\dots+X_n$ represents the sum of successes then $X\sim Bin(n,p)$. We can therefore calculate expectation, variance:$$\Huge E[X]=\sum_{i=1}^nE[X_i]=n\times p=np$$$$\Huge Var[X]=\sum_{i=1}^nVar[X_i]=n\times pq=np(1-p)$$