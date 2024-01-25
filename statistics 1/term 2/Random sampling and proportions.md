# Bernoulli distribution:

When an experiment has binary outcome, that is a success or failure. We denote the two outcomes at $0$ or $1$. We then define the Bernoulli distribution with parameter $p\in[0,1]$ that has outcome either $0$ or $1$:$$\Huge P(X=1)=p,\,\,P(X=0)=1-p$$$$\Huge f(x|p)=\begin{cases}p^xq^{1-x}&\text{for }x=0,1\\0&\text{otherwise}\end{cases}$$Where $q=1-p$. Note that $f(1|p)=p,\,f(0|p)=q$. From this we calculate the expectation and variance:$$\Huge E[X]=\sum_{x=0}^1xf(x|p)=0\times q+1\times p=p$$$$\Huge E[X^2]=\sum_{x=0}^1x^2f(x|p)=0^2\times q+1^2\times p=p$$$$\Huge Var[X]=E[X^2]-E^2[X]=p-p^2=p(1-p)=pq$$We can also calculate the [[Limit theorems#Moment Generating functions|MGF]] also:$$\Huge \psi(t)=E[e^{tX}]=\sum_{x=0}^1e^{tx}f(x|p)=e^0\times q+e^t\times p=q+pe^t$$
## Bernoulli trials:
Given a sequence of $n$ random variables $X_1,\dots,X_n$ which are independent and identically distributed. If each $X_i$ has a Bernoulli distribution with parameter $p$ then we say $X_1,\dots,X_n$ form $n$ Bernoulli trials. This is a great model for the US presidential election.

# Statistical inference:

Often in statistics, the results of a real world experiment are taken and the statistician is asked to infer something meaningful about an underlying probability $p$. This probability can be thought of in one of two ways:
>$p$ is real with a fixed value that is unknown (frequentist)
>$p$ is an unknown quantity which should represent our subjective uncertainty (bayesian)

For the first interpresentation, an estimation of $p$ can be constructed from $X_1,\dots,X_n$. The attributes of this estimator can then be examined to determine its reliability.

# Totals and estimators:

Define $X$ as the total sum of all successes over $n$ trials:$$\Huge X=\sum_{i=1}^nX_n$$With each $X_i$ taking value $0$ or $1$, i.e. a Bernoulli distribution. Then we need to take the [[Frequentist methods#Continuous random variables|PMF]] of all $n$ trials:$$\Huge f(x_1,\dots,x_n|p)=\prod_{i=1}^nf(x_i|p)=\prod_{i=1}^np^{x_i}q^{1-x_i}=p^{\sum_{i=1}^nx_i}q^{\sum_{i=1}^n1-x_i}=p^xq^{n-x}$$