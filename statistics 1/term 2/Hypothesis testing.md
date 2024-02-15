
Suppose we are interested in a single unkown parameter $\theta$, we suggest a number $r$ which we either beleive may be the value for $\theta$, or we want to compare $\theta$ to. We then define the null and alternative hypothesis. Construct two hypotheses:
>$H_0$, the null hypothesis, that $\theta=r$
>$H_a$, the alternative hypothesis denies the null hypothesis, the type of denial determines whether the hypothesis test is one sided or two sided

A two sided hypothesis test states:$$\Huge H_0:\theta=r,\,\,H_a:\theta \neq r$$A one sided test states:$$\Huge H_0:\theta=r,\,\,H_a:\begin{cases}\theta<r\\\theta>r\end{cases}$$
The big questions is, given a particular sample of data, should we reject the null hypothesis or not. For example, consider $\mu$ to be the mean of the population of cuckoo eggs. An ornithologist wishes to test the hypothesis $\mu=22.5$, then $H_0:\mu=22.5$ and $H_a:\mu\neq22.5$. This is an example of a two sided test, an example of a single sided test would be a lightbulb manufacturer claiming that the average lifetime of their lightbulbs is at least $1200$ hours. The consumer association wants to test this, so $H_0:\mu=1200$ and $H_a:\mu<1200$.

# Two sided case:

If we have a two sided hypothesis, an [[Random sampling and proportions#Totals and estimators|estimator]] for $\theta$ and a sampling distribution of the estimator, then we can construct a $(1-\alpha)$ [[Inference#Confidence intervals for the population mean|confidence interval]] for $\theta$. We then reject $H_0$ if $r$ lies outside of this confidence interval, at the $\alpha$% level of significance. We fail to accept $H_0$ at the $\alpha$% level of significance otherwise.

# One sided case:

If we have a one sided hypothesis, an estimator for $\theta$, a sampling distribution of the estimator, and a level of significance $\alpha$, we can then construct a $(1-2\alpha)$ confidence interval for $\theta$. Then we reject $H_0$ if $r$ falls to the right (for $H_0:\theta<r$) of the confidence interval. We fail to reject $H_0$ otherwise.

# Hypothesis testing using p-values:

Using confidence intervals is one way to test a hypothesis, an alternative method is to calculate an appropriate test statistic from the data. We can then find the probability of observing a value at least as extreme as the statistic under the assumption that $H_0$ is true, we call said probability the $p$ value.

This probability can be found by comparing the test statistic with critical values of the relevant sampling distribution. The more extreme a statistic is, the less likely it is that $H_0$ is true. The threshold for the $p$ value is the level of significance, $\alpha$.