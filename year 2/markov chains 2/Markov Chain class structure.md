
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

The hitting time of a set of states $A\subset I$ is the random variable $H^A:\Omega\mapsto\mathbb{N}_0\cup\{\infty\}$ defined by the following formula:$$\Huge H^A:=\inf\{n\geq0:X_n\in A\}$$We also define:$$\Huge h_i^A:=\mathbb{P}_i[H^A<\infty],\,\,k_i^A:=\mathbb{E}_i[H^A]$$That is, when starting at state $i$, $h_i^A$ represents the probability that the hitting time is finite and $k_i^A$ is the expected hitting time. We can find this expectation:$$\Huge k_i^A=\sum_{n=0}^\infty n \mathbb{P}_i[H^A=n]+\begin{cases}0&\mathbb{P}_i[H^A=\infty]=0\\\infty&\text{otherwise}\end{cases}$$Sometimes $h_i^A$ is called absorption probability if $A$ is a closed communicating class. The vector of hitting probabilities $(h_i^A)_{i\in I}$ is the minimal non negative solution to the system of equations:$$\Huge \begin{cases}h_i^A=1&i\in A\\h_i^A=\sum_{j\in I}P_{ij}h_j^A&i\notin A\end{cases}$$The vector of hitting expectations $(k_i^A)_{i\in I}$ is the minimal non negative solution to the system of equations:$$\Huge \begin{cases}k_i^A=0&i\in A\\k_i^A=1+\sum_{j\in I}P_{ij}k_j^A&i\notin A\end{cases}$$To prove this theorem, we need to show that $(h_i^A)_{i\in I}$ solves the system of equations and that any other solution must not be minimal. To show that this solves the system of equations, we notice for $i\in A$, $h_i^A=1$ and if $i\notin A$ we have:$$\Huge \mathbb{P}_i[H^A<\infty]=\sum_{j\in I}\mathbb{P}_i[H^A<\infty,X_1=j]=\sum_{j\in I}\mathbb{P}_i[H^A<]$$