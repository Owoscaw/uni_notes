
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

Any Bayesian problem is expressed as:$$\Huge f(\theta|x)=\frac{f(x|\theta)f(\theta)}{f(x)},\,\text{posterior}=\frac{\text{likelihood}\times \text{prior}}{\text{data probability}}$$Note that once data is observed, $x$ becomes constant, making the posterior proportional to the product of likelihood and prior. To find this proportionality constant, 