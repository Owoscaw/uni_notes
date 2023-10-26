
A random variable on a [[Sample spaces and events|sample space]], $\Omega$ is a mapping from $\Omega$ to some set of possible values:$$\Huge X(\Omega):=\{X(\omega):\omega\in\Omega\},\,\,X:\Omega\mapsto X(\Omega)\,\,\text{given by}\,\,\omega\mapsto X(\omega)$$
> If $X(\Omega)\subseteq\Re$, then $X$ is said to be a real-valued random variable.
> If $X(\Omega)\subseteq\,$[[Vector space definitions|$\Re^n$]], then $X$ is said to be a vector-valued random variable. Here, each element of the vector $X$ is a real valued random variable with $X_i(\omega):=[X(\omega)]_i$, that is $X_i$ is the $i$th component of the vector $X(\omega)$.

Example:
![[random variable dice]]

For any set $B\subseteq X(\Omega)$, we say $X\in B$ is the event $\{\omega:X(\omega)\in B\}=X^{-1}(B)$. So for any $x\in X(\Omega)$ we write $X=x$ is the event $\{\omega:X(\omega)=x\}$, that is $\mathbb{P}(X=x)=\mathbb{P}(\{\omega:X(\omega)=x\})$, with our [[Probability definition#Probability space|probability space definition]] $(\Omega, \mathcal{F}, \mathbb{P})$.
## Indicator random variable:

