
Suppose we are interested in a single unkown parameter $\theta$, we suggest a number $r$ which we either beleive may be the value for $\theta$, or we want to compare $\theta$ to. We then define the null and alternative hypothesis. Construct two hypotheses:
>$H_0$, the null hypothesis, that $\theta=r$
>$H_a$, the alternative hypothesis denies the null hypothesis, the type of denial determines whether the hypothesis test is one sided or two sided

A two sided hypothesis test states:$$\Huge H_0:\theta=r,\,\,H_a:\theta \neq r$$A one sided test states:$$\Huge H_0:\theta=r,\,\,H_a:\begin{cases}\theta<r\\\theta>r\end{cases}$$
The big questions is, given a particular sample of data, should we reject the null hypothesis or not. For example, consider $\mu$ to be the mean of the population of cuckoo eggs. An ornithologist wishes to test the hypothesis $\mu=22.5$, then $H_0:\mu=22.5$ and $H_a:\mu\neq22.5$. This is an example of a two sided test, an example of a single sided test would be a lightbulb manufacturer claiming that the average lifetime of their lightbulbs is at least $1200$ hours. The consumer association wants to test this, so $H_0:\mu=1200$ and $H_a:\mu<1200$.

# Two sided case:

If we have a two sided hypothesis, an [[Random sampling and proportions#Totals and estimators|estimator]] for $\theta$ and a sampling distribution of the estimator, then we can construct a $(1-\alpha)$ [[Inference#Confidence intervals for the population mean|confidence interval]] for $\theta$. We then reject $H_0$ if $r$ lies outside of this confidence interval, at the $\alpha$% level of significance. We fail to accept $H_0$ at the $\alpha$% level of significance otherwise.

# One sided case:

If we have a one sided hypothesis, an estimator for $\theta$, a sampling distribution of the estimator, and a level of significance $\alpha$, we can then construct a $(1-2\alpha)$ confidence interval for $\theta$. Then we reject $H_0$ if $r$ falls to the right of 