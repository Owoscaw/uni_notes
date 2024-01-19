
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
Sequential learning occurs when multiple tests are conducted in a row (sequence), for 