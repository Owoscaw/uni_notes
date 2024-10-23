
Say that a [[Graph definitions|node]] $i$ leads to $j$, written as $i\to j$, if $\mathbb{P}[X_n=j]>0$ for some $n\geq0$. Say $i$ communicates with $j$ if $i\to j$ and $j\to i$, written as $i\leftrightarrow j$.

For distinct [[Definitions of Markov Chains#Definition|states]] $i,j$, the following statements are equivalent:
> $i\to j$
> $\exists n,i_0,i_1,\dots,i_n$ with $i_0=i,i_n=j$ and $P_{i_0i_j}P_{i_1i_2}\dots P_{i_{n-1}i_n}>0$
> $P^{(n)}_{ij}>0$ for some $n\geq0$

Where $P$ is the [[Definitions of Markov Chains#Stochastic matrices|stochastic matrix]] representing the Markov Chain, $I$ is the set of possible states, and $P_{ij}^{(n)}$ is the [[Definitions of Markov Chains#Linear algebra|n-step transition probability]] between $i$ and $j$. To prove this, we notice that $\{\omega:X_0(\omega)=i,X_n(\omega)=j\}$ is a subset of $\bigcup_{k\geq0}\{\omega:X_0(\omega)=i,X_k(\omega)=j\}$, so we have that $P_{ij}^{(n)}\leq \mathbb{P}_i[X_n=j]\leq\sum_{n=0}^\infty \mathbb{P}_i[X_n=j]=\sum_{k=0}^\infty P^{(k)}_{ij}$ for some $n\geq0$. Therefore statement one and three are equivalent. Now since $P_{ij}^{(n)}=\sum_{i_1,\dots,i_{n-1}\in I}P_{i_0i_1}P_{i_1i_2}\dots P_{i_{n-1}i_n}$, which must be positive. So we have that the second and third statements are equivalent, proving the equivalence of all three.

## Communicating class definition:
A Markov Chain can be divided up into communicating classes, $C_i$, using the relation $\leftrightarrow$:$$\Huge C_i:=\{j\in I:i\leftrightarrow j\}$$Note that if $j\in C_i$, then $C_i=C_j$ and if $j\notin C_i$, then $C_j\cap C_i=\emptyset$. Therefore we can say that communicating classes partition $I$ disjointly. 

We call a Markov Chain irreducible if it consists of a single communicating class, otherwise it is called reducible.  A class $C$ is closed if $i\in C$, $i\to j$ and $j\in C$, that is there is no way to escape $C$ once you are at a node inside it. A state $i$ is called absorbing if $\{i\}$ is a closed communicating class.

# Periodicity:

Some properties of Markov Chains hold for all states in a communicating class, called class properties. One of these properties is called periodicity. A state $i$ is called aperiodic if:$$\Huge \gcd\{n:P^{(n)}_{ii}>0\}=1$$That is, $i$ is aperiodic if and only if $P^{(n)}_{ii}>0$ for large enough $n$.

If $P$ is the transition matrix of an irreducible Markov Chain, and $i$ is aperiodic, then all $j\in I$ are aperiodic. If $i$ is not aperiodic, then we define the period of state $i$ as $\gcd\{n:P^{(n)}_{ii}>0\}$.

# Hitting times:

The hitting time of a set of states $A\subset I$ is the random variable $H^A:\Omega\mapsto\mathbb{N}_0\cup\{\infty\}$ defined by the following formula:$$\Huge H^A:=\inf\{n\geq0:X_n\in A\}$$