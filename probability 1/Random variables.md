
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

# Binomial and Geometric distributions:

A random experiment is repeated $n$ times. Each trial is independent of one another. A trial has a binary outcome. Each trial has a fixed probability of success, $p$. $X$ is defined to be the number of successful trials in $n$ total trials. $\Omega=\{\omega_n=(\omega_1,\omega_2,\dots,\omega_n):\omega_i\in\{0,1\}\}$, so we define:$$\Huge X(\omega)=\sum_{i=1}^n\omega_i=x\iff\mathbb{P}(X=x)={n\choose x}p^x(1-p)^{n-x}$$
