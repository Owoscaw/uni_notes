
Probability is a function that is applied to $\mathcal{F}$, the complete set of events in a [[Sample spaces and events|sample space]] $\Omega$ defined as:
$$\Huge \mathcal{F}=2^{\Omega}$$
That is, $\mathcal{F}$ is the set of every possible subset in $\Omega$, where each subset represents an event. Probability is a function that maps this set to a real number, let $A\in\mathcal{F}$ represent an event:
$$\Huge \mathbb{P}:\mathcal{F}\mapsto\Re,\,\,\mathbb{P}(A)\in\Re$$
The probability function follows these rules, given that $A,B\in\mathcal{F}$ and $A\cap B=\emptyset$:
>$$\Huge \mathbb{P}\geq0,\,\,\forall A\in\mathcal{F}$$
>$$\Huge \mathbb{P}(\Omega)=1$$
>$$\Huge \mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)$$

This last rule can be generalised given that every event is disjoint from another. That is, any two events $A$, and $B$:
$$\Huge A\cap B=\emptyset$$
Give for all $A_i$, $i\geq 1$, each event is pairwise disjoint:
$$\Huge \mathbb{P}\left(\bigcup_{i=1}^{\infty}A_i\right)=\sum_{i=1}^{\infty}\mathbb{P}(A_i)$$
The following is also true given the above assumption about $A,B$:
$$\Huge |A\cup B|=|A|+|B|$$
If $A\cap B\neq\emptyset$:
$$\Huge |A\cup B|=|A|+|B|-|A\cap B|$$

Given a sample space, $\Omega=\{\omega _1, \omega_2,\dots,\omega_n\}$, $\mathcal{F}$ is defined as $\mathcal{F}=2^{\Omega}$. Given also that $\mathbb{P}(\{\omega _i\})=P(i)$, such that $1\leq i \leq n$, the following are true:
> $$\Huge P(i)\geq0,\,\,\sum_{i=1}^{n}P(i)=1$$
> $$\Huge \forall A\in \mathcal{F}, \,\,\mathbb{P}(A)=\sum_{i=1}^{n}P(i),\,\,i:\omega_i\in A$$

That is, for all outcomes $\omega _i$ in the event $A$, the probability of $i$ being an outcome is greater than or equal to $0$