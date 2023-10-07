
Probability is a function that is applied to $\mathcal{F}$, the complete set of events in a [[Sample spaces and events|sample space]] $\Omega$ defined as:
$$\Huge \mathcal{F}=2^{\Omega}$$
That is, $\mathcal{F}$ is the set of every possible subset in $\Omega$, where each subset represents an event. Probability is a function that maps this set to a real number, let $A\in\mathcal{F}$ represent an event:
$$\Huge \mathbb{P}:\mathcal{F}\mapsto\Re,\,\,\mathbb{P}(A)\in\Re$$
The probability function follows these axioms, given that $A,B\in\mathcal{F}$ and $A\cap B=\emptyset$:
>$$\Huge \mathbb{P}\geq0,\,\,\forall A\in\mathcal{F}$$
>$$\Huge \mathbb{P}(\Omega)=1,\,\, \mathbb{P}(\emptyset)=0$$
>$$\Huge \mathbb{P}(A^{'})=1-\mathbb{P}(A)$$
>$$\Huge \mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)$$

The following is also true given the above assumption about $A,B$:
$$\Huge |A\cup B|=|A|+|B|$$
If $A\cap B\neq\emptyset$:
$$\Huge |A\cup B|=|A|+|B|-|A\cap B|$$

Given a sample space, $\Omega=\{\omega _1, \omega_2,\dots,\omega_n\}$, $\mathcal{F}$ is defined as $\mathcal{F}=2^{\Omega}$. Given also that $\mathbb{P}(\{\omega _i\})=P(i)$, such that $1\leq i \leq n$, the following are true:
> $$\Huge P(i)\geq0,\,\,\sum_{i=1}^{n}P(i)=1$$
> $$\Huge \forall A\in \mathcal{F}, \,\,\mathbb{P}(A)=\sum_{i=1}^{n}P(i),\,\,i:\omega_i\in A$$

That is, for all outcomes $\omega _i$ in the event $A$, the probability of $i$ being an outcome is greater than or equal to $0$, and the sum of the probabilities of all outcomes is $1$. The second statement says that for ever event $A$ in $\mathcal{F}$, the probability of $A$ is equal to the sum of the probabilities of all outcomes that define $A$.

Let all events, $A_i$ for $1\leq i\leq\infty$, be pairwise disjoint, that is:
$$\Huge \bigcap_{i=1}^{\infty}A_i=\emptyset$$
# Consequences of probability axioms:

For two events, $A, B\in\Omega$.

>C1$$\Huge \mathbb{P}(B\setminus A)=\mathbb{P}(B)-\mathbb{P}(A\cap B)$$
>C2$$\Huge \mathbb{P}(A^{'})=1-\mathbb{P}(A)$$
>C3$$\Huge \mathbb{P}(\emptyset)=0$$
>C4$$\Huge \mathbb{P}(A)\leq1$$
>Given $A\subseteq B$, C5$$\Huge\mathbb{P}(A)\leq\mathbb{P}(B)$$
>C6$$\Huge \mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A\cap B)$$
>Given $A_1,A_2,\dots,A_n$ are pairwise disjoint, C7
> $$\Huge \mathbb{P}\left(\bigcup_{i=1}^nA_i\right)=\sum_{i=1}^n\mathbb{P}(A_i)$$
>For any sequence of events, $A_1,A_2,\dots$, C8$$\Huge \mathbb{P}\left(\bigcup_{i=1}^{\infty}A_i\right)\leq\sum_{i=1}^{\infty}\mathbb{P}(A_i)$$
>If $A_1$