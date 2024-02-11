Inference is drawing conclusions from facts, data, and premises.

# Sample mean as an estimator:

Assume there is a population of interest with mean value $\mu$ and standard deviation $\sigma$. A simple random sample of size $n$ is taken such that $n$ is sufficiently large to call successive samples independent. Label each such sample $X_1,\dots,X_n$. Before their values are seen, each $X_i$ is a random variable with expectation $\mu$ and standard deviation $\sigma$. We then define the sample mean:$$\Huge \bar X=\frac{1}{n}\sum_{i=1}^nX_i$$This has the following properties:$$\Huge E[\bar X]=E\left[\frac{1}{n}\sum_{i=1}^nX_i\right]=\frac{1}{n}\sum_{i=1}^nE[X_i]=\frac{1}{n}\times n\mu=\mu$$$$\Huge Var[\bar X]=Var\left[\frac{1}{n}\sum_{i=1}^nX_i\right]=\frac{1}{n^2}\sum_{i=1}^nVar[X_i]=\frac{1}{n}\times n\sigma^2=\frac{\sigma^2}{n}$$This implies $\bar X$ is an [[Random sampling and proportions#Sample proportion as an estimator|unbiased estimator]] and that the variance of $\bar X$ is dependent on $n$. If the population of $X_i$ is normally distributed: $$\Huge X_i\sim N(\mu,\sigma^2)\implies\bar X\sim N\left(\mu,\frac{\sigma^2}{n}\right)$$$\bar X$ is still random before all $X_i$ are measured. Once measured, $X_i$ becomes $x_i$ and $\bar X$ becomes $\bar x$. The Frequentist view is that the population nis true but unknown and the only randomness comes from the random sampling. 

# The central limit theorem:

The above works well, however the population distribution is not always normal, so we suppose the following. Let $X_1,\dots,X_n$ be $n$ identically distributed independent variables, each with mean $\mu$ and standard deviation $\sigma$. Then we can say that the distribution of the sample mean satisfies:$$\Huge \bar X\to N\left(\mu,\frac{\sigma^2}{n}\right)\,\,\text{as}\,\,n\to\infty$$This is true regardless of the population distribution. 

# Standard errors:

Often $\sigma$ is not known, so we need to estimate it sometimes. Before the data is measured, this is the random variable $S$:$$\Huge S=\sqrt{\frac{1}{n-1}\sum_{i=1}^n(X_i-\bar X)^2}=\sqrt{\frac{1}{n-1}\left(\sum_{i=1}^nX_i^2-n\bar X^2\right)}$$Under certain conditions, $E[S^2]=\sigma^2$ and is hence an unbiased estimator, dependent on the $\frac{1}{n-1}$ term rather than the $\frac{1}{n}$ term. Therefore we estimate the standard deviation of the sample mean $\frac{\sigma}{\sqrt{n}}$ by the standard error of the sample mean, $\frac{s}{\sqrt{n}}$. Then we get the result:$$\Huge \frac{\bar X-\mu}{S/\sqrt{n}}\sim N(0,1)$$Given that $n$ is sufficiently large. However if $n$ is not sufficiently large, then $s$ is a poor estimator for $\sigma$ and the above fraction is no longer normally distributed

# $t$ distribution:

What if $\sigma$ is unknown and $n$ is small. If the distribution of $X_i$ is Normal, then we proceed as follows:$$\Huge \frac{\bar X-\mu}{S/\sqrt{n}}\sim t_{n-1}$$Where $t$ represents the $t$ distribution and $s$ is the estimator for $\sigma$. A random variable $T$ has a $t$ distribution with degrees of freedom parameter $\nu$ if it has PDF:$$\Huge f(t|\nu)=\frac{\Gamma(\frac{\nu+1}{2})}{\sqrt{\nu\pi}\,\Gamma(\frac{\nu}{2})}\left(1+\frac{t^2}{\nu}\right)^{-\frac{\nu+1}{2}}$$Where $\Gamma$ is the analytic continuation of the factorial, defined by $\Gamma(n)=(n-1)!$ for positive integers $n$. We write $T\sim t_\nu$ and note $E[T]=0$ and $Var[T]=\frac{\nu}{\nu-2}$ for $\nu>2$. Calculating $f$ is very difficult, so computers and tables are used. The full definition of $\Gamma$ is:$$\Huge \Gamma(z)=\int_{0}^\infty x^{z-1}e^{-x}dx$$

# Confidence Intervals:

## Inference about $\mu$:
Suppose random samples $X_1,\dots,X_n$ are taken from a population of mean $\mu$ and variance $\sigma^2$ . Then by CLT we know $\bar X\sim N(\mu,\sigma^2/\sqrt{n})$, statements of probability can then be made about $\bar X$. Since we know this, we can make statements that infer knowledge about $\mu$:$$\large P\left(-1.96\leq\frac{\bar X-\mu}{\sigma/\sqrt{n}}\leq1.96\right)=0.95\implies P\left(\bar X-1.96\frac{\sigma}{\sqrt n}\leq\mu\leq\bar X+1.96\frac{\sigma}{\sqrt n}\right)$$
Suppose we observe $X_1=x_1,\dots, X_n=x_n$, then we can construct the confidence interval by $\bar X\mapsto\bar x$:$$\Huge \left[\bar x-1.96\frac{\sigma}{\sqrt n},\bar x+1.96\frac{\sigma}{\sqrt n}\right]$$This is called a $95$% confidence interval, $\mu$ lies within this interval with probability of $0.95$. This is not a probability statement since each $X_i$ has been observed, it is a realisation of the random interval so is no longer random.

## General case:
Given a random sample $\underline X=(X_1,\dots,X_n)$ and two statistics $[u(\underline X),v(\underline X)]$, a realisation $[u(\underline x),v(\underline x)]$ of the random interval $[u(\underline X),v(\underline X)]$ is called a confidence interval at a confidence level for a population parameter $\theta$ when:$$\Huge P(u(\underline X)\leq\theta\leq v(\underline X))=1-\alpha$$In general, a $1-\alpha$% confidence interval for an unknown parameter $\theta$ is a range between two numbers such that the method of producing the interval gives an interval which contains the true value of $\theta$ $1-\alpha$% of the time.

## Confidence intervals for the population mean:

### $\sigma$  known:
When $\sigma$ is known, suppose that we have an SRS $X_1,\dots,X_n$ where the standard devation is known and the population is either normal or large enough to use the central limit theorem. Also suppose the calculated sample mean is $\bar x$, then an $(1-\alpha)$% confidence interval for $\mu$ is given by:$$\Huge \bar x\pm z^*\frac{\sigma}{\sqrt{n}}$$Where $z^*$ is a critical value of a standard normal random variable such that:$$\Huge P(-z^*\leq Z\leq z^*)=1-\alpha$$

### $\sigma$ unknown, $n$ small, normal:
When $\sigma$ is unknown, $n$ is small, the population is normal, a simple random sample $X_1,\dots,X_n$ is taken, the calculated observed sample mean is $\bar x$, and the calculated observed standard deviation is  $s$, then a $(1-\alpha)$% confidence interval for $\mu$ is:$$\Huge \bar x\pm t_{n-1}^*\frac{s}{\sqrt{n}}$$Where $t_{n-1}^*$ is the critical value of a $t$ distributed random variable with $n-1$ degrees of freedom such that:$$\Huge P(-t_{n-1}^*\leq T\leq t_{n-1}^*)=1-\alpha$$
### $\sigma$ unknown, $n$ large:
Suppose that a simple random sample $X_1,\dots,X_n$ is taken such that $n\geq30$, the population standard devisation is unkown, the observed sample mean is given by $\bar x$, and the observed standard deviation is given by $s$. Then a $(1-\alpha)$% confidence interval for $\mu$ is:$$\Huge \bar x\pm z^*\frac{s}{\sqrt n}$$Where $z^*$ is a critical value of the standard normal such that:$$\Huge P(-z^*\leq Z\leq z^*)=1-\alpha$$