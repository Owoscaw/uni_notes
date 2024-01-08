
A combination from a set of objects is an unordered selection of elements in that set. For example, $\left\{\omega_1,\omega_2,\dots,\omega_n\right\}$ and $\left\{\omega_n,\omega_{n-1},\dots,\omega_1\right\}$ are different arrangements but the same combination, order does not matter.

A combination on a set $S$ is identified by the multiplicities $m_i,\forall i\in S$, where $m_i$ determines the number of times $i$ appears in $S$. The easier case to consider is $m_i\in\{0,1\}$, each element used either no times or one time.

The size of a combination is the total number of selections, that is the sum of all multiplicities $\sum_{i\in S}m_i$. A combination of size $k$ is called a $k$-combination.

# Standard problem 3:

How many combinations without repetition of a given size $k$ exist from a given set of size $n$. The arrangements with repetition is given by [[Arrangements and Permutations#Permutations|$P(n,k)$]]. These are ordered lists, so each arrangement using the same elements is counted $k!$ times, so we divide $P(n,k)$ by $k!$ to give the number of combinations without repetition in this scenario:$$\Huge \frac{P(n,k)}{k!}=\frac{n!}{(n-k)!k!}=\begin{pmatrix}n\\k\end{pmatrix}$$
This is also known as the binomial coefficient. A combination of size $k$ without repetition corresponds to a subset of $S$, the set originally chosen from. This is sometimes written as $^nC_k$. Note that:$$\Huge \begin{pmatrix}n\\k\end{pmatrix}=\begin{pmatrix}n\\n-k\end{pmatrix}$$
# Pascals triangle and Binomial theorem:

These coefficients are the same as pascals triangle:
![[pascals triangle]]
So the $k$th element in the $n$th row in pascals triangle is given by the sum of the two elements "above" it. That is to say:$$\Huge \begin{pmatrix}n\\k\end{pmatrix}=\begin{pmatrix}n-1\\k-1\end{pmatrix}+\begin{pmatrix}n-1\\k\end{pmatrix}$$
This also corresponds to the coefficients in the expansion of two numbers raised to a power, hence the name "binomial":
$$\Huge (a+b)^n=\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}a^kb^{n-k}$$
This is because there are $\begin{pmatrix}n\\k\end{pmatrix}$ ways of expanding the brackets to produce a term with powers of $a$ and $b$ equivalent to $a^kb^{n-k}$. The following are identities that can be shown using the binomial theorem:
>$\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}=2^n$
>$\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}(-1)^k=0$
>$\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}2^k=3^n$
>$\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}k=n2^{n-1}$

All of these are based on the identity $(1+x)^n=\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}x^k$.

