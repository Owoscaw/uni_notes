
In interpreting a [[Disease testing using Bayesian Methods|disease test]] result of $T^+$, typically there exists a prior probability of $P(D^+)$ of an individual having the disease. This usually represents the background prevalence of the disease in a population. Given the information of a positive test, the probability that takes this information into account is called the posterior probability, given by $P(D^+|T^+)$:
> $P(D^+)$ is the prior probability of disease
> $P(T^+|D^+)$ and $P(T^+|D^-)$ are the likelihood of positive test given disease status
> $P(D^+|T^+)$ is the posterior probability of disease given positive test

Bayes theorem is used to calculate the posterior probability:$$\Huge P(D^+|T^+)=\frac{P(T^+|D^+)P(D^+)}{P(T^+)}=\frac{P(T^+|D^+)P(D^+)}{P(T^+|D^+)P(D^+)+P(T^+|D^-)P(D^-)}$$Using partition theorem also. Below is an example of calculating posterior probability for the data used in [[Disease testing using Bayesian Methods]]:![[disease testing follow up]]
Note that $P(D^+|T^+)$ is still low because the prior probability $P(D^+)$ was very low. Despite evidence from a positive test, it is still unlikely to have covid. Another way to see this is by looking at the denominator of Bayes theorem, $P(T^+)=P(T^+|D^+)P(D^+)+P(T^+|D^-)P(D^-)$. In the above case, $P(D^+)$ is so low that the probability of getting a false positive result is much greater than that of an accurate positive test. Therefore the majority of people testing positive for covid would be doing so due to a false positive rather than an accurate positive test.

# Advanced Bayesian Calculations:

## Repeated tests:
Consider the august 2020 covid example where $P(D^+|T^+)=0.0156$. Then take a second test which is also positive, denoting this as $T^{++}$. However in this case, the nature of the test has to be explored further. One assumption could be that the test results are conditionally independent given disease status, that is:$$\Huge P(T^{++}|D^+)=P(T^+|D^+)^2,\,\,P(T^{++}|D^-)=P(T^+|D^-)^2$$This is reasonable if the test fails independently each time. So consider this:$$\small P(D^+|T^{++})=\frac{P(T^{++}|D^+)P(D^+)}{P(T^{++}|D^+)P(D^+)+P(T^{++}|D^-)P(D^-)}=\frac{P(T^+|D^+)^2P(D^+)}{P(T^+|D^+)^2P(D^+)+P(T^+|D^-)^2P(D^-)}=0.501$$

## Sequential learning:
Sequential learning occurs when multiple tests are conducted in a row (sequence), for example $T^{++}$. Additional information about a test changed the probability of a belief one after the other. Bayes theorem is consistent in the sense that sequential updates by $T^+$ can be applied at once, for example going straight from $P(D^+)$ to $P(D^+|T^{++})$. The posteriors $P(D^+|T_1^+)$ and $P(D^-|T^+_1)$ can be used as priors for the second test, $P(D^+|T^{++})=P(D^+|T_1^+,T_2^+)$. This becomes:$$\Huge\frac{P(T_2^+|D^+,T_1^+)P(D^+|T_1^+)}{P(T_2^+|D^+,T_1^+)P(D^+|T_1^+) + P(T_2^+|D^-,T_1^+)P(D^-|T_1^+)}$$However since we assume that the test result dependent only on disease status, this can be rewritten as:$$\Huge\frac{P(T_2^+|D^+)P(D^+|T_1^+)}{P(T_2^+|D^+)P(D^+|T_1^+) + P(T_2^+|D^-)P(D^-|T_1^+)}$$
## Sensitivity of the posterior to the prior:
We saw that the posterior $P(D^+|T^+)$ was sensitive to the value of the prior. We can explore this locally for a particular prior by examining the [[Differentiable Functions|derivative]] of the posterior with respect to the prior:$$\Huge \frac{d(P(D^+|T^+))}{d(P(D^+))}$$If there was uncertainty about the prior, however a certain action would be taken if the posterior were over a given threshold, Bayes theorem can be rearranged to solve for $P(D^+)$ in terms of the posterior.

# Information from the Posterior:

Simple summaries of $f(\theta|x)$ such as plots, location summaries, and spread summaries can be made from $f(\theta|x)$. Probabilities using $f(\theta|x)$ can directly calculated, for example $P(\theta>a|x)$. Point estimates summaries the distribution in terms of a single value of $\theta$, the best guess. Predictions about future data given $\theta$ and $x$ can be made. Intervals that capture a proportion of the possible values of $\theta$ can be found.

# Point estimates:

Point estimates are single values of $\theta$ that are a "best guess" value obtained from $f(\theta|x)$. There are two main choices for this:
> Posterior Mode or Maximum a Posteriori estimate. $\hat \theta_{MAP}$ is the value of $\theta$ that maximises the posterior $f(\theta|x)$, analogous to $\hat \theta_{MLE}$
> Posterior Mean, $E[\theta|x]=\int \theta f(\theta|x)d \theta$. This is simply the posterior expectation


# Credible Intervals:

A $1-\alpha$ credible interval is derived from the PDF of $\theta$ such that the interval contains $\theta$ with probability $1-\alpha$. A $1-\alpha$ credible interval $[l,u]$ for a random variable $\theta$ satisfies the following:$$\Huge P(l\leq \theta\leq u)=P(\theta\in[l,u])=1-\alpha$$Similarly, a $1-\alpha$ credible interval for $\theta$ given $X=x$ satisfies:$$\Huge P(l\leq \theta\leq u|X=x)=P(\theta\in [l,u]|X=x)=1-\alpha$$Note that $l,u$ are constants, not random variables. There are two standard ways to construct a credible interval:
> Equal-tailed intervals. Here, the interval is constructed such that $P(\theta<l)=P(\theta>u)=\frac{\alpha}{2}$, so that there is equal probability of falling in each tail of the distribution. If $\theta$ has a standard distribution, the CDF $F_\theta$ can be used to find values of $l,u$. We required$$\Huge F_\theta(l)=\frac{\alpha}{2},\,\,F_\theta(u)=1-\frac{\alpha}{2}$$
> 
> Highest Posterior Density intervals. This interval is the narrowest possible interval (smallest $|l-u|$) that we can construct with the given restriction ($P(\theta\in[l,u])=1-\alpha$). Such intervals contain the regions of highest probability density.

# Normal approximation to Credible Intervals:

If the distribution of $\theta$ is known, and we can find its CDF, it is possible to calculate $[l,u]$ exactly by integration tables or computers. However we can adopt a normal approximation to the credible interval if this is not the case:

Given a random variable $\theta$, an approximate $1-\alpha$ credible interval for $\theta$ is given by:$$\Huge E[\theta]\pm Z_{\frac{\alpha}{2}}^*\sqrt{Var[\theta]}$$Assuming the approximation $\theta\approx\sim N(E[\theta],Var[\theta])$. This is often done using the posterior distribution, $\theta|x$, giving:$$\Huge E[\theta|x]\pm Z_{\frac{\alpha}{2}}^*\sqrt{Var[\theta|x]}$$This is a good approximation for a uni-modal, symmetric, and "well peaked" distribution.

# Conjugate Analysis for Normal Data:

When data is normally distributed, we have $X_i\sim N(\mu, \sigma^2)$. Assume $\sigma$ to be known and fixed, we then take $\theta=\mu$. The conjugate prior family for the mean $\mu$ is itself normal.

We define the precision, $\tau$, of a random variable to be the inverse of variance:$$\Huge \tau=\frac{1}{Var[X]}=\frac{1}{\sigma^2}$$We can then write $X\sim N(\mu,\frac{1}{\tau})$, making the PDF:$$\Huge f(x|\mu,\tau)=\sqrt{\frac{\tau}{2\pi}}e^{-\frac{\tau}{2}(x-\mu )^2}$$
## The normal-normal method:
Let $X_1,\dots,X_n$ be independently identically distributed with $X_i\sim N(\mu,\frac{1}{\tau})$ and precision $\tau>0$ known. Suppose our prior PDF for uncertain $\mu$ is $\mu\sim N(m,\frac{1}{t})$ with $t>0$.