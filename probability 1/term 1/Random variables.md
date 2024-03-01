
A random variable on a [[Sample spaces and events|sample space]], $\Omega$ is a mapping from $\Omega$ to some set of possible values:$$\Huge X(\Omega):=\{X(\omega):\omega\in\Omega\},\,\,X:\Omega\mapsto X(\Omega)\,\,\text{given by}\,\,\omega\mapsto X(\omega)$$
> If $X(\Omega)\subseteq\Re$, then $X$ is said to be a real-valued random variable.
> If $X(\Omega)\subseteq\,$[[Vector space definitions|$\Re^n$]], then $X$ is said to be a vector-valued random variable. Here, each element of the vector $X$ is a real valued random variable with $X_i(\omega):=[X(\omega)]_i$, that is $X_i$ is the $i$th component of the vector $X(\omega)$.

Example:
![[random variable dice]]

For any set $B\subseteq X(\Omega)$, we say $X\in B$ is the event $\{\omega:X(\omega)\in B\}=X^{-1}(B)$. So for any $x\in X(\Omega)$ we write $\{X=x\}$ as the event $\{\omega:X(\omega)=x\}\subseteq\Omega$, that is $\mathbb{P}(X=x)=\mathbb{P}(\{\omega:X(\omega)=x\})$, with our [[Probability definition#Probability space|probability space definition]] $(\Omega, \mathcal{F}, \mathbb{P})$.

The function $\mathbb{P}_X:\mathcal{F}\mapsto\Re$ is defined by the following:$$\Huge \forall B\subseteq X(\Omega),\,\,\mathbb{P}_X(B)=\mathbb{P}(\{\omega:X(\omega)\in B\})$$
$\mathbb{P}_X$ is a probability in and of itself as it satisfies all axioms, and therefore satisfies all the relating consequences. There are two special cases for this function:
> Discrete random variables
> Continuous random variables

## Indicator random variables:

An event $A\in\mathcal{F}$ denoted as $1_A$, given by the mapping:
$$\Huge 1_A(\omega)=\begin{cases}1&\text{if}\,\,\omega\in A\\0&\text{otherwise}\end{cases}$$
Note that $\mathbb{P}(1_A=1)=\mathbb{P}(\{\omega\in\Omega:\omega\in A\})=\mathbb{P}(A)$, that is the probability of $\omega$ belonging to $A$ is equal to the probability of event $A$ occurring. Also $\mathbb{P}(1_A=0)=1-\mathbb{P}(A)$.


# Discrete random variables:

A random variables $X:\Omega\mapsto X(\Omega)$ is said to be discrete if there exists a finite countable set $\chi\subseteq X(\Omega)$ such that $\mathbb{P}(X\in\chi)=1$. The function $p:\chi\mapsto[0,1]$ defined by:$$\Huge p(x)=\mathbb{P}(X=x),\,\forall x\in\chi$$
This is known as the probability mass function. Let $X$ be a discrete random variable and $p$ to be the PMF of $X$. Then:
$$\Huge \mathbb{P}(X\in B)=\sum_{x\in B}p(x),\,\text{for any}\,B\subseteq\chi$$
Note that $\sum_{x\in\chi}p(x)=1$. $\chi$ is either finite, or countable, or both, so in any case it can be enumerated. A set $B\subseteq\chi$ will also be finite or countable, so it can be written as:$$\Huge \mathbb{P}_X(B)=\mathbb{P}(X\in B)=\mathbb{P}\left(\bigcup_{x\in B}\{X=x\}\right)=\sum_{x\in B}\mathbb{P}(X=x)=\sum_{x\in B}p(x)$$
So we have $$\Huge B=\bigcup_{i=1}^\infty\{X_i=x_i\}$$
If $B=\chi$, we get $sum_{x\in\chi}p(x)=\mathbb{P}(X\in\chi)=1$.

## Binomial distribution:

A random experiment is repeated $n$ times. Each trial is independent of one another. A trial has a binary outcome. Each trial has a fixed probability of success, $p$. $X$ is defined to be the number of successful trials in $n$ total trials. $\Omega=\{\omega_n=(\omega_1,\omega_2,\dots,\omega_n):\omega_i\in\{0,1\}\}$, so we define:$$\Huge X(\omega)=\sum_{i=1}^n\omega_i=x\iff\mathbb{P}(X=x)={n\choose x}p^x(1-p)^{n-x}$$
Here, $X(\omega)$ counts the number of successes that appear in the sequence of trials. This is represented in $\Omega$, where $(0,0,\dots,1)$ represents success on the $n$th trial, $(0,1,0,\dots,0)$ represents a success on the second trial and no other trials, there are [[Combinations#Pascals triangle and Binomial theorem|${n\choose 1}$]] ways of choosing sequences that sum to exactly 1. $\mathbb{P}(X=x)$ determines the probability of a sequence of trials and successes, where the sum over all trials, $X(\omega)$ is equal to $x$.

A random variable $X$ has a binomial distribution with parameters $p\in[0,1]$ and $n\in\mathbb{N}$. Then we write $X\sim Bin(n,p)$. When $\chi=\{0,1,dots,n\}$ and:$$\Huge p(x)={n\choose x}p^x(1-p)^{n-x},\,\forall x\in\{0,1,\dots,n\}$$
A special case occurs when the parameter $n=1$. Then this is called a Bernoulli trial, $X\sim Bin(1,p)$. Then $X$ is referred to as a Bernoulli random variable.

## Geometric distribution:

Suppose that infinite trials are allowed, until the first successful trial is seen. Let $Z:=$ the number of trials until the first success. There must occur $x-1$ failures until there is a successful trial on the $x$th trial, that is:$$\Huge \mathbb{P}(Z=x)=p(1-p)^{x-1}$$
Here, $Z$ is a geometrically distributed random variable. The PMF is given by:$$\Huge p(x)=\mathbb{P}(Z=x)=p(1-p)^{x-1},\,\forall x\in\mathbb{N}$$
Note that:
$$\Huge \sum_{x=1}^\infty p(x)=\sum_{x=1}^\infty p(1-p)^{x-1}=p\sum_{x=1}^\infty(1-p)^{x-1}=\frac{p}{1-(1-p)}=\frac{p}{p}=1$$
A random variable $X$ is said to be geometrically distributed with parameter $p\in(0,1)$, $X\sim Geo(p)$ if the PMF is given as above. Then $\chi=\mathbb{N}$.

## Poisson distribution:

A discrete random variable is Poisson distributed with parameter $\lambda>0$, denoted by $X\sim Poi(\lambda)$, if $\chi=\{0,1,2,dots\}=\mathbb{N}_0$ and:
$$\Huge p(x)=\mathbb{P}(X=x)=\frac{e^{-\lambda}\lambda^x}{x!},\,\forall x\in\mathbb{N}_0$$
This distribution is used to model counts of events that occur randomly at an average rate $\lambda$ per unit time. $$\Huge \mathbb{P}(\text{an event occurs in }[r,r+h])\approx rh,\,\text{for small h}$$
Consider $\lambda>0,\,X_n\sim Bin(n,p_n)$, where $\lim_{n\to\infty}np_n=\lambda$, then let $Y\sim Poi(\lambda)$, then for all $x\in\mathbb{Z}_+$:$$\Huge \lim_{n\to\infty}p_{X_n}(x)=p_Y(x)$$
So $X$ converges in distribution to $Y$. $$\large p_{X_n}(x)=\mathbb{P}(X_n=x)={n\choose x}p_n^x(1-p_n)^{n-x}=n^{-x}\frac{n!}{(n-x)!x!}(np_n)^x(1-p_n)^{n-x}$$
Then we have:
> $\lim_{n\to\infty}(np_n)^x=\lambda^x$
> $\lim_{n\to\infty}(1-p_n)^n=\lim_{n\to\infty}(1-\frac{np_n}{n})^n=e^{-\lambda}$
> $\lim_{n\to\infty}(1-p_n)^{-x}=1$
> $\lim_{n\to\infty}n^{-x}\frac{n!}{(n-x)!}=lim_{n\to\infty}(1-1/n)(1-2/n)\dots(1-\frac{x-1}{n})=1\times 1\times\dots\times 1=1$

Combining these statements:
$$\Huge\lim_{n\to\infty}\mathbb{P}(X_n=x)=\frac{e^{-\lambda}\lambda^x}{x!}$$
So if $X\sim B(n,p)$ with large $n$ and small $p$, then $X\approx\sim Po(np)$. This approximation allows us to avoid the calculation of ${n\choose x}$ for large $x$ and $n$.

# Continuous random variables:

Let $X:\Omega\mapsto\Re$ be a continuous random variable. $\exists\,f:\Re\mapsto[0,\infty)$ such that:$$\Huge \mathbb{P}(X\in[a,b])=\mathbb{P}(a\leq x\leq b)=\int_a^bf(t)dt,\,a\leq b$$
Here, $f$ is called the probability density function (PDF). Then we have:
$$\Huge \mathbb{P}(X=x)=\int_x^xf(t)dt=0,\,\forall x$$
Single points do not have any associated probability, there only exists a probability for a certain interval, that is:$$\Huge \mathbb{P}(X\in[x,x+dx])=\mathbb{P}(X\in(x,x+dx))=f(x)dx$$
For a given $B\subseteq\Re$ a finite union of intervals, and a continuously distributed $X$ with a PDF of $f$:$$\Huge \mathbb{P}(X\in B)=\int_Bf(x)dx$$
This interpretation has the following properties:
>$$\Huge \int_{-\infty}^\infty f(x)dx=\mathbb{P}(X\in\Re)=1$$
>$$\Huge \mathbb{P}(-\infty<x\leq b)=\int_{-\infty}^bf(t)dt$$
>$$\Huge \mathbb{P}(a\leq x<\infty)=\int_a^\infty f(t)dt$$

Note that PDFs can be defined piecewise also. Example:
![[PDF example]]

## Uniform distribution:

$X$ is said to be uniformly distributed on $[a,b]$ for real numbers $a,b\in\Re$, then $X\sim U(a,b)$ where:$$\Huge f(x)=\begin{cases}\frac{1}{b-a}&\forall x\in[a,b]\\0&\text{elsewhere}\end{cases}$$
When $X$ is distributed normally then $X$ can take any value in the continuous range of values from $a$ to $b$ and the probability of finding $X$ in any interval $[x,x+h]\subseteq[a,b]$ is independent of $x$.

## Exponential distribution:

Given an event happens randomly in time at a rate $\beta>0$, and $T>0$ denotes the time at which the first event occurs, the number of events that occur in the interval $[0,\tau]$ is given by $Po(\beta\tau)$, so:$$\Huge \mathbb{P}(T>\tau)=e^{-\beta\tau},\,\mathbb{P}(T\leq\tau)=1-e^{-\beta\tau}$$ For all $\tau\geq0$. This expression is equivalent to $\int_0^\tau\beta e^{-\beta t}dt$, so $T$ is a random variably with PDF of $f(t)=\beta e^{-\beta t}$. Now we define the exponential distribution:

Let $\beta>0$. A continuous random variable $X$ is exponentially distributed with parameter $\beta$, $X\sim Exp(\beta)$ when:$$\Huge f(x)=\begin{cases}\beta e^{-\beta x}&\forall x\geq0\\0&\text{elsewhere}\end{cases}$$

## Normal distribution:

Let $\mu,\sigma\in\Re$ with $\sigma>0$. A continuous random variable $X$ is normally distributed, $X\sim\mathcal{N}(\mu,\sigma^2)$, when:$$\Huge f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2},\,\forall x\in\Re$$
There is no closed analytical form for $\int_a^bf(x)dx,\,\forall a,b\in\Re$ with $a,b$, so numerical integration is often used. As is, the normal distribution's CDF has four parameters ($\mu,\sigma^2,a,b$). By defining a standard normal distribution, $Z$, then the amount of parameters can be reduced, $Z\sim\mathcal{N}(0,1)$. To transform $X$ into $Z$, a change of variable is used:$$\Huge Z=\frac{X-\mu}{\sigma}$$
Now denoting the PDF of $Z$ as $\phi$:$$\Huge \phi(x)=\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}x^2}$$
And the CDF as $\Phi$:
$$\Huge \Phi(x)=\int_{-\infty}^x\phi(t)dt$$
Since $\phi(x)$ is symmetric, the following statement holds:
$$\large \Phi(-z)=\int_{-\infty}^{-z}\phi(t)dt=-\int_{\infty}^z\phi(-x)dx=\int_z^\infty\phi(x)dx=\mathbb{P}(Z>z)=1-\Phi(z)$$
As $\Phi$ has no closed analytical form, it is often tabulated. Using the above statement, only positive values of $z$ need to be tabulated as negative values follow from positive.

# Cumulative distribution function:

For any real valued random variable $X$, the cumulative distribution function (CDF) $F:\Re\mapsto[0,1]$ is defined as:
$$\Huge F(x)=\mathbb{P}(X\leq x)=\mathbb{P}(-\infty<X\leq x)$$
This function completely characterises a distribution. It immediately follows that:$$\small \mathbb{P}(X\in(-\infty,b])=\mathbb{P}(X^{-1}((-\infty,b]))=\mathbb{P}(\omega:X(\omega)\in(-\infty,b])=\mathbb{P}(\omega:X(\omega)\in(-\infty,a]\cup(a,b])$$
Since $(-\infty,a]$ and $(a,b]$ are disjoint unions, then the following is true:$$\Huge \mathbb{P}(X\in(-\infty,b])=\mathbb{P}(\omega:X(\omega)\in(-\infty,a])+\mathbb{P}(\omega:X(\omega)\in(a,b])$$$$\Huge \mathbb{P}(X\in(-\infty,b))=\mathbb{P}(X\leq a)+\mathbb{P}(X\in(a,b])$$
Rearranging, we have:$$\Huge \mathbb{P}(X\in(a,b])=\mathbb{P}(X\leq b)-\mathbb{P}(X\leq a)=F(b)-F(a)$$
Suppose that $X$ is a continuously distributed random variable on $\Re$ with a PDF of $f$, then $F$ is also a continuous function, and $\forall x\in\Re$:$$\Huge F(x)=\int_{-\infty}^xf(t)dt,\,f(x)=\frac{dF}{dx}(x)$$
This can be proving using the [[calculus 1/term 1/Integration#Fundamental theorem of calculus|fundamental theorem of calculus]]. $F$ also satisfies the following:
> $\lim_{x\to\infty}F(x)=1$
> $\lim_{x\to-\infty}F(x)=0$
> $F$ is right continuous, that is for any $t\in\Re$, $F(t)=F(t+)$, where $t+$ is the limit from the right
> $F$ is monotonically increasing

## Discrete case:

If $X$ is a discrete real valued random variable with a probability mass function $p$, then $F$ is piecewise constant and right-continuous (all discontinuities are to the right of a point for an interval), so can be written as a sum:$$\Huge F(x)=\mathbb{P}(X\leq x)=\sum_{t:t\leq x}p(t)$$
Here, $p(x)=F(x)-F(x-)$, where $F(x-)=\lim_{y\to x}F(y)$. 

The CDF, $F$, of a real valued random variable therefore completely determines a distribution

# Functions of random variables:

Let $X:\Omega\mapsto X(\Omega)$ and $g:X(\Omega)\mapsto S$ be a random variable and some function respectively. Then $g(X)$ is also a random variable, defined as $g(X)=g\circ X:\Omega\mapsto S$:
$$\Huge g(X)(\omega):=g(X(\omega)),\,\forall\omega\in\Omega$$
$$\Huge \mathbb{P}(g(X)\in B)=\mathbb{P}(\{\omega\in\Omega:g(X(\omega))\in B\}),\,\forall B\subseteq S$$
