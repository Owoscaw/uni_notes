
Given $A, B$ are [[Sample spaces and events#Events|events]], where $\mathbb{P}(B)>0$, we define:
$$\Huge \mathbb{P}(A|B)=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(B)}$$
For any event $B\subseteq \Omega$, with $\mathbb{P}(B)>0$, $\mathbb{P}(\cdot|B)$ satisfies all [[Probability definition#Axioms|axioms of probability]], and therefore all [[Probability definition#Consequences of probability axioms|consequences of probability]]. Given a [[Probability definition#Sigma algebra|probability space]], $(\Omega,\mathcal{F},\mathbb{P})$ we define:
$$\Huge \mathbb{P}|_{B}:\mathcal{F}\mapsto\Re\,\,\text{as follows:}$$
$$\Huge \mathbb{P}|_B(A):=\mathbb{P}(A|B)=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(B)}$$
This defines the probability of event $A$ happening, given that event $B$ has already happened. Since $\mathbb{P}(A|B)$ is in itself a probability, all axioms and consequences apply to it. Note that $A|B$ is not an event in itself. The $|B$ is a property of the probability only.
# Multiplication rule:

For any events, $A$ and $B$, with $\mathbb{P}(A),\mathbb{P}(B)>0$:$$\Huge \mathbb{P}(A\cap B)=\mathbb{P}(B)\mathbb{P}(A|B)=\mathbb{P}(A)\mathbb{P}(B|A)$$
More generally for $A,B,C$:$$\Huge \mathbb{P}(A\cap B|C)=\mathbb{P}(B|C)\mathbb{P}(A|B\cap C),\,\,\mathbb{P}(B\cap C)>0$$
This is fully generalised for any events $A_0,A_1,\dots,A_k$, given $\mathbb{P}\left(\bigcap_{i=0}^{k-1}A_i\right)>0$:$$\mathbb{P}\left(\bigcap_{i=1}^kA_i|A_0\right)=\mathbb{P}(A_1|A_0)\times\mathbb{P}(A_2|A_1\cap A_0)\times\dots\times\mathbb{P}\left(A_{k-1}|\bigcap_{i=1}^{k-1}A_i\right)\times\mathbb{P}\left(A_k|\bigcap_{i=1}^{k-1}A_i\right)$$
This is derived from repeatedly applying the rule defined above it. Given that $k=3$ and $A_0=\Omega$:$$\Huge \mathbb{P}(A\cap B\cap C)=\mathbb{P}(A)\mathbb{P}(B|A)\mathbb{P}(C|A\cap B)$$
# Law of total probability:

Let $E_1,\dots,E_k$ be a partition of $\Omega$, each $E_i\cap E_j=\emptyset$ and $\bigcup_{i=1}^kE_i=\Omega$. Then for any $A\subseteq\Omega$, $A\in\mathcal{F}$:$$\Huge \mathbb{P}(A)=\sum_{i=1}^k\mathbb{P}(E_i)\mathbb{P}(A|E_i)$$
This is proven as follows:
$$\Huge A=A\cap\Omega=A\cap\left(\bigcup_{i=1}^kE_i\right)=\bigcup_{i=1}^k\left(A\cap E_i\right)$$
Knowing that $A\cap E_i=\emptyset$ for any $E_i$ in our partition:$$\mathbb{P}(A)=\mathbb{P}\left(\bigcup_{i=1}^k\left(A\cap E_i\right)\right)=\sum_{i=1}^k\mathbb{P}(A\cap E_i),\,\text{using the multiplication rule},\,\mathbb{P}(A)=\sum_{i=1}^k\mathbb{P}(E_i)\mathbb{P}(A|E_i)$$
Given that $\mathbb{P}(A|B)$ is itself a probability, another result can be shown:$$\Huge\mathbb{P}(A|B)=\sum_{i=1}^k\mathbb{P}(E_i|B)\mathbb{P}((A|B)|E_i)=\sum_{i=1}^k\mathbb{P}(E_i|B)\mathbb{P}(A|B\cap E_i)$$
# Bayes' theorem:

## V1:

Let $A,B$ be events, with $\mathbb{P}(A),\mathbb{P}(B)>0$, then:$$\Huge \mathbb{P}(A|B)=\frac{\mathbb{P}(A)\mathbb{P}(B|A)}{\mathbb{P}(B)}$$
More generally if $\mathbb{P}(A|C),\mathbb{P}(B|C)>0$:$$\Huge \mathbb{P}(A|B\cap C)=\frac{\mathbb{P}(A|C)\mathbb{P}(B|A\cap C)}{\mathbb{P}(B|C)}$$
This is shown through the following:$$\Huge \mathbb{P}(A|B)=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(B)}=\frac{\mathbb{P}(A)\mathbb{P}(B|A)}{\mathbb{P}(B)},\,\text{using the multiplication rule}$$
## V2:

Let $E_1,\dots,E_k$ form a partition over $\Omega$ and $A\subseteq\Omega$ be an event such that $\mathbb{P}(A)>0$, then:$$\Huge \mathbb{P}(E_i|A)=\frac{\mathbb{P}(A|E_i)\mathbb{P}(E_i)}{\sum_{i=1}^k\mathbb{P}(E_i)\mathbb{P}(A|E_i)}$$
This result is proven through the following:$$\large\mathbb{P}(E_i|A)=\frac{\mathbb{P}(A|E_i)\mathbb{P}(E_i)}{\mathbb{P}(A)}=\frac{\mathbb{P}(A|E_i)\mathbb{P}(E_i)}{\sum_{i=1}^k\mathbb{P}(E_i)\mathbb{P}(A|E_i)},\,\text{using law of total probability}$$
This naturally shows the restriction $\mathbb{P}(A)>0$.

Example:
![[conditional probability for cats]]

# Independence:

Let $A,B$ be events, then $A$ and $B$ are independent if $\mathbb{P}(A\cap B)=\mathbb{P}(A)\mathbb{P}(B)$. $A$ and $B$ are conditionally independent if, given a third event $C$, $\mathbb{P}(C)$:$$\Huge \mathbb{P}(A\cap B|C)=\mathbb{P}(A|C)\mathbb{P}(B|C)$$
This is to say, the occurrence of event $A$ has no effect on event $B$. Given $\mathbb{P}(A)>0$ and $\mathbb{P}(B)>0$, the following statements are equivalent:
>$\mathbb{P}(A\cap B)=\mathbb{P}(A)\mathbb{P}(B)$
>$\mathbb{P}(A|B)=\mathbb{P}(A)$
>$\mathbb{P}(B|A)=\mathbb{P}(B)$

This is shown through the following steps:$$\Huge \mathbb{P}(A|B)=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(B)}=\frac{\mathbb{P}(A)\mathbb{P}(B)}{\mathbb{P}(B)}=\mathbb{P}(A),\,\text{using bayes' theorem}$$
There is a similar statement involving a third event $C$. Given $\mathbb{P}(A\cap B\cap C)>0$, then the following statements are equivalent:
>$\mathbb{P}(A\cap B|C)=\mathbb{P}(A|C)\mathbb{P}(B|C)$
>$\mathbb{P}(A|B\cap C)=\mathbb{P}(A|C)$
>$\mathbb{P}(B|A\cap C)=\mathbb{P}(B|C)$

Example:![[conditional probability for die]]

# Independence of multiple events:

A possibly infinite collection of events $A_i$, for $i\in\mathcal{F}$ are mutually independent if for every finite, non-empty $\zeta\in\mathcal{F}$:$$\Huge \mathbb{P}\left(\bigcap_{i\in\zeta}A_i\right)=\prod_{i\in\zeta}\mathbb{P}(A_i)$$
Similarly, a collection of events $A_i$. for $i\in\mathcal{F}$ are mutually conditionally independent given another event $C$ if for every finite, non-empty $\zeta\in\mathcal{F}$:$$\Huge \mathbb{P}\left(\bigcap_{i\in\zeta}A_i|C\right)=\prod_{i\in\zeta}\mathbb{P}(A_i|C)$$
For example, $3$ events $A,B,C$ are mutually independent if the following are satisfied:
>$\mathbb{P}(A\cap B)=\mathbb{P}(A)\mathbb{P}(B)$
>$\mathbb{P}(B\cap C)=\mathbb{P}(B)\mathbb{P}(C)$
>$\mathbb{P}(A\cap C)=\mathbb{P}(A)\mathbb{P}(C)$
>$\mathbb{P}(A\cap B\cap C)=\mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C)$

Note that it is possible for pairwise independence and not mutual independence. This means that for a collection of events $A_i$ for $i\in\{1,2,\dots,n\}$, events $A_k$ and $A_{k+1}$ may be independent, but $A_k$ and every other event in the collection (mutual independence) may not be independent.

