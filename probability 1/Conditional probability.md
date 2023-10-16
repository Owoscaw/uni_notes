
Given $A, B$ are [[Sample spaces and events#Events|events]], where $\mathbb{P}(B)>0$, we define:
$$\Huge \mathbb{P}(A|B)=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(B)}$$
For any event $B\subseteq \Omega$, with $\mathbb{P}(B)>0$, $\mathbb{P}(\cdot|B)$ satisfies all [[Probability definition#Axioms|axioms of probability]], and therefore all [[Probability definition#Consequences of probability axioms|consequences of probability]]. Given a [[Probability definition#Sigma algebra|probability space]], $(\Omega,\mathcal{F},\mathbb{P})$ we define:
$$\Huge \mathbb{P}|_{B}:\mathcal{F}\mapsto\Re\,\text{as follows:}$$
$$\Huge \mathbb{P}|_B(A):=\mathbb{P}(A|B)=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(B)}$$
# Multiplication rule:

For any events, $A$ and $B$, with $\mathbb{P}(A),\mathbb{P}(B)>0$:$$\Huge \mathbb{P}(A\cap B)=\mathbb{P}(B)\mathbb{P}(A|B)=\mathbb{P}(A)\mathbb{P}(B|A)$$
More generally for $A,B,C$:$$\Huge \mathbb{P}(A\cap B|C)=\mathbb{P}(B|C)\mathbb{P}(A|B\cap C),\,\,\mathbb{P}(B\cap C)>0$$
This is fully generalised for any events $A_0,A_1,\dots,A_k$, given $\mathbb{P}\left(\right)$