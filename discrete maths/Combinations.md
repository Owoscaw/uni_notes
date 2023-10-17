
A combination from a set of objects is an unordered selection of elements in that set. For example, $\left\{\omega_1,\omega_2,\dots,\omega_n\right\}$ and $\left\{\omega_n,\omega_{n-1},\dots,\omega_1\right\}$ are different arrangements but the same combination, order does not matter.

A combination on a set $S$ is identified by the multiplicities $m_i,\forall i\in S$, where $m_i$ determines the number of times $i$ appears in $S$. The easier case to consider is $m_i\in\{0,1\}$, each element used either no times or one time.

The size of a combination is the total number of selections, that is the sum of all multiplicities $\sum_{i\in S}m_i$. A combination of size $k$ is called a $k$-combination.

# Standard problem 3:

How many combinations without repetition of a given size $k$ exist from a given set of size $n$. The arrangements with repetition is given by [[Arrangements and Permutations#Permutations|$P(n,k)$]]. These are ordered lists, so each arrangement using the same elements is counted $k!$ times, so we divide $P(n,k)$ by $k!$ to give the number of combinations without repetition in this scenario:$$\Huge \frac{P(n,k)}{k!}=\frac{n!}{(n-k)!k!}=\begin{pmatrix}n\\k\end{pmatrix}$$
This is also known as the binomial coefficient. A combination of size $k$
