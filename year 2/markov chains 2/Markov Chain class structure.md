
Say that a [[Graph definitions|node]] $i$ leads to $j$, written as $i\to j$, if $\mathbb{P}[X_n=j]>0$ for some $n\geq0$. Say $i$ communicates with $j$ if $i\to j$ and $j\to i$, written as $i\leftrightarrow j$.

For distinct [[Definitions of Markov Chains#Definition|states]] $i,j$, the following statements are equivalent:
> $i\to j$
> $\exists n,i_0,i_1,\dots,i_n$ with $i_0=i,i_n=j$ and $P_{i_0i_j}P_{i_1i_2}\dots P_{i_{n-1}i_n}>0$
> $P^{(n)}_{ij}>0$ for some $n\geq0$

Where $P$ is the [[Definitions of Markov Chains#Stochastic matrices|stochastic matrix]] representing the Markov Chain, and $P_{ij}^{(n)}$ is the [[Definitions of Markov Chains#Linear algebra|n-step transition probability]] between $i$ and $j$. To prove this, we notice that $\{\omega:X_0(\omega)=i,X_n(\omega)=j\}$ is a subset of $\bigcup_{k\geq0}\{\omega:X_0(\omega)=i,X_k(\omega)=j\}$, so we have that $P_{ij}^{(n)}\leq \mathbb{P}_i[X_n=j]\leq\sum_{n=0}^\infty \mathbb{P}_i[X_n=j]=\sum_{k=0}^\infty P^{(k)}_{ij}$ for some $n\geq0$. Therefore statement one and three are equivalent. Now since $P_{ij}^{(n)}=\sum_{i_1,\dots,i_{n-1}\in I}P_{i_0i_1}P_{i_1i_2}\dots P_{i_{n-1}i_n}$, 