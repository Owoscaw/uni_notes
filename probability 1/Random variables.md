
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
This is known as the probability mass function