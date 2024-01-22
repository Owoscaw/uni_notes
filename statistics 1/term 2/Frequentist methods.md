# Discrete random variables:

A discrete random variable $X$ can take a countably infinite set of values $x_1,x_2,\dots\in X$ according to some experiment or random phenomenon. We denote the probability mass function ([[Random variables#Discrete random variables|PMF]]) as follows:$$\Huge f(x)=P(X=x),\,\,\forall x\in X$$Often a discrete random variable has a distribution dependent on an external parameter. For example, consider a [[Random variables#Poisson distribution|Poisson distribution]] dependent on the parameter $\lambda$. We denote this PMF as:$$\Huge f(x|\lambda)=P(X=x|\lambda)=\begin{cases}\frac{e^{-\lambda}\lambda^x}{x!}&\text{if }x=0,1,2,\dots\\0&\text{otherwise}\end{cases}$$
## Expectation:
The [[Expectation#Definition and interpretation|expectation]] of a discrete random variable $X$ is given by:$$\Huge E[X]=\sum_{x\in X}xP(X=x)=\sum_{x\in X}xf(x)$$If a function $h(x)$ is applied to the set $X$:$$\Huge E[h(X)]=\sum_{x\in X}h(x)P(X=x)=\sum_{x\in X}h(x)f(x)$$
## Variance:
The [[Expectation#Variance and Co-Variance|variance]] of a discrete random variable $X$ is given by:$$\Huge Var[X]=E[(X-E[X])^2]=E[X^2]-E^2[X]$$We also define the standard deviation:$$\Huge SD[X]=\sqrt{Var[X]}$$
# Continuous random variables:

The probability density function ([[Random variables#Continuous random variables|PDF]]) of a continuous random variable $X$ describes the probability density of each value:$$\Huge P(x\leq X\leq x+dx)=f(x)dx,\,\,P(a\leq X\leq B)=\int_a^bf(x)dx$$Take the [[Random variables#Normal distribution|normal distribution]], $X\sim N(\mu,\sigma^2)$ and its PDF:$$\Huge f(x|\mu,\sigma)=\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$
## Expectation and Variance:
$$\Huge E[X]=\int xf(x)dx,\,\,Var[X]=E[X^2]-E^2[X]$$That is:$$\Huge Var[X]=\int x^2f(x)dx-\left(\int xf(x)dx\right)^2$$

# Properties of expectation and variance:

## Change in scale and location:
Consider and random variable $X$ with any $a,b\in\Re$. Then we have:$$\Huge E[aX+b]=aE[X]+b$$By the linearity of the sum and of the integral. Similarly:$$\Huge Var[aX+b]=a^2Var[X]$$