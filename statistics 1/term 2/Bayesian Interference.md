
In interpreting a [[Disease testing using Bayesian Methods|disease test]] result of $T^+$, typically there exists a prior probability of $P(D^+)$ of an individual having the disease. This usually represents the background prevalence of the disease in a population. Given the information of a positive test, the probability that takes this information into account is called the posterior probability, given by $P(D^+|T^+)$:
> $P(D^+)$ is the prior probability of disease
> $P(T^+|D^+)$ and $P(T^+|D^-)$ are the likelihood of positive test given disease status
> $P(D^+|T^+)$ is the posterior probability of disease given positive test

Bayes theorem is used to calculate the posterior probability:$$\Huge P(D^+|T^+)=\frac{P(T^+|D^+)P(D^+)}{P(T^+)}=\frac{P(T^+|D^+)P(D^+)}{P(T^+|D^+)P(D^+)+P(T^+|D^-)P(D^-)}$$Using partition theorem also. Below is an example of calcul![[disease testing follow up]]