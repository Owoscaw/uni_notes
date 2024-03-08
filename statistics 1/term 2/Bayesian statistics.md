
The goal of statistics is to make [[Inference|inference]] using observed data. In order to do this, data is assumed to have originated from a model, $f(x|\theta)$, and inference is usually expressed in terms of an unobserved parameter $\theta$, which reveals information about the real world. We saw that the [[Likelihood#Maximum likelihood estimation|MLE]] can be found from data, however this does not directly tell you much about the underlying patterns of the data since it comes from the randomness of said data. Confidence intervals can be constructed from the MLE since is has a variance and an expected value.

The fundamental principle of Bayesian statistics is that everything is uncertain and can be treated as random. Everything has an associated probability distribution, provided a subjective interpretation of probability. Therefore $\theta$ is treated as a random variable, uncertainty about $\theta$ is described by a subjective PDF $f(\theta)$.

To learn about $\theta$ from data $x$, conditional probability is used with $f(\theta)$ and $f(x|\theta)$ in order to find $f(\theta|x)$. We use $f(\theta|x)$ to answer all questions about $\theta$. The Bayesian approach works for any $n$, whearas the frequentist approach tends to break down for small $n$.

# Bayesian results:

## Conditional probability:
Let $f(x,y)$ be a joint PDF, the marginal PDF of $Y$ is then given by $\int_\chi f(x,y)dx$ and the conditional pdf of $Y$ given $X=x$ is:$$\Huge f(y|x)=\frac{f(x,y)}{f(x)}\implies f(x,y)=f(x|y)f(y)=f(y|x)f(x)$$
## Partition theorem:
For discrete variables, $P(A)=\sum_{b\in B}P(A|B=b)P(B=b)$, then for continuous variables:$$\Huge f(y)=\int_\chi f(y|x)f(x)dx$$
# Bayesian stages:
## Prior:
We have an unknown parameter $\theta$ describing some real world quantity of interest. We assign a prior distribution $f(\theta)$ to represent our uncertainty beliefs about $\theta$.

## Data:
We observe data $X=x$, allowing the likelihood to be formed, $f(x|\theta)$.

## Posterior:
After observing data, the likelihood of each parameter value $\theta$ can be evaluated given the data $x$ using the prior. This is done using Baye's theorem, giving us $f(\theta|x)$.

## Inference:
Using the posterior distribution $f(\theta|x)$, we can make many inference statements, eg a probability interval, or probability of a given hypothesis

$$\Huge f(\theta)\longrightarrow f(x|\theta)\longrightarrow f(\theta|x)$$
# Fundamental equation of Bayesian statistics:

Any Bayesian problem is expressed as:$$\Huge f(\theta|x)=\frac{f(x|\theta)f(\theta)}{f(x)},\,\text{posterior}=\frac{\text{likelihood}\times \text{prior}}{\text{data probability}}$$Note that once data is observed, $x$ becomes constant, making the posterior proportional to the product of likelihood and prior. To find this proportionality constant, either integrate over $f(\theta|x)$ and set this to $1$ or spot that $f(x|\theta)f(\theta)$ looks like a known distribution from a known family with a known constant.

# Probability distributions and Conjugates:

The presence of prior distributions in calculations is the main difference between bayesian and frequentist approaches. In general there are two types of prior distributions:
> Informative priors, $f(\theta)$ expresses specific knowledge about the behaviour of $\theta$
> Non-informative priors, $f(\theta)$ is very vauge, the simplest form is a uniform distribution

Another consideration is to choose a prior that captures knowledge about $\theta$, which are convienient to do bayesian calculations with. Such priors are called conjugate priors.

A conjugate prior distribution is one where the form of the posterior distribution is the same as the form of the prior distribution, that is they are both normal for example. In which case we say that $f(\theta)$ is a conjugate prior for the likelihood, $f(x|\theta)$. Conjugacy implies that the prior and posterior have the same functional form, however will have different parameters for their shared distribution. The use of a conjugate prior makes the subsequent use of Bayes theorem very easy.

For a random variable $X$ with PDF $f(x)$, if we can express its PDF as $f(x)=C\kappa(x)$, where $C>0$ is a constant independent of $X$, we call $\kappa(x)$ the core of the density $f(x)$. We propose that each core of a distribution corresponds to a unique PDF. If you want proof go fuck yourself.

# Conjugate Bayesian Analysis for Binomial data:

To deal with binomial data/scenarios, we aim to choose a good family of priors. The conjugate prior to a binomial likelihood is a known distribution, the Beta distribution: Let $X\sim\beta(a,b)$ for $a,b>0$ known, then $X$ has Beta distribution with PDF:$$\Huge f(x)=\frac{1}{B(a,b)}x^{a-1}(1-x)^{b-1}=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}x^{a-1}(1-x)^{b-1}$$For $0\leq x\leq1$. Here, $B(a,b)$ is the Beta function and $\Gamma$ is the gamma function. This has properties as follows:
> The core of a Beta distribution with parameters $a,b$ is $\kappa(x)=x^{a-1}(1-x)^{b-1}$
> If $X\sim\beta(1,b)$ then $E[X]=\frac{a}{a+b}$ and $Var[X]=\frac{ab}{(a+b)^2(a+b+1)}$ and $Mode[x]=\frac{a-1}{a+b-2}$ 
> $\beta(1,1)$ is the same as $U[0,1]$ where $U$ is the uniform distribution.
> For large $a,b$ then $$