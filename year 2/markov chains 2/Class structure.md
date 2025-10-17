
Say that a [[Graph definitions|node]] $i$ leads to $j$, written as $i\to j$, if $\mathbb{P}[X_n=j]>0$ for some $n\geq0$. Say $i$ communicates with $j$ if $i\to j$ and $j\to i$, written as $i\leftrightarrow j$.

For distinct [[Definition and Properties#Definition|states]] $i,j$, the following statements are equivalent:
> $i\to j$
> $\exists n,i_0,i_1,\dots,i_n$ with $i_0=i,i_n=j$ and $P_{i_0i_j}P_{i_1i_2}\dots P_{i_{n-1}i_n}>0$
> $P^{(n)}_{ij}>0$ for some $n\geq0$

Where $P$ is the [[Definition and Properties#Stochastic matrices|stochastic matrix]] representing the Markov Chain, $I$ is the set of possible states, and $P_{ij}^{(n)}$ is the [[Definition and Properties#Linear algebra|n-step transition probability]] between $i$ and $j$. To prove this, we notice that $\{\omega:X_0(\omega)=i,X_n(\omega)=j\}$ is a subset of $\bigcup_{k\geq0}\{\omega:X_0(\omega)=i,X_k(\omega)=j\}$, so we have that $P_{ij}^{(n)}\leq \mathbb{P}_i[X_n=j]\leq\sum_{n=0}^\infty \mathbb{P}_i[X_n=j]=\sum_{k=0}^\infty P^{(k)}_{ij}$ for some $n\geq0$. Therefore statement one and three are equivalent. Now since $P_{ij}^{(n)}=\sum_{i_1,\dots,i_{n-1}\in I}P_{i_0i_1}P_{i_1i_2}\dots P_{i_{n-1}i_n}$, which must be positive. So we have that the second and third statements are equivalent, proving the equivalence of all three.

## Communicating class definition:
A Markov Chain can be divided up into communicating classes, $C_i$, using the relation $\leftrightarrow$:$$\Huge C_i:=\{j\in I:i\leftrightarrow j\}$$Note that if $j\in C_i$, then $C_i=C_j$ and if $j\notin C_i$, then $C_j\cap C_i=\emptyset$. Therefore we can say that communicating classes partition $I$ disjointly. 

We call a Markov Chain irreducible if it consists of a single communicating class, otherwise it is called reducible.  A class $C$ is closed if $i\in C$, $i\to j$ and $j\in C$, that is there is no way to escape $C$ once you are at a node inside it. A state $i$ is called absorbing if $\{i\}$ is a closed communicating class.

# Periodicity:

Some properties of Markov Chains hold for all states in a communicating class, called class properties. One of these properties is called periodicity. A state $i$ is called aperiodic if:$$\Huge \gcd\{n:P^{(n)}_{ii}>0\}=1$$That is, $i$ is aperiodic if and only if $P^{(n)}_{ii}>0$ for large enough $n$.

If $P$ is the transition matrix of an irreducible Markov Chain, and $i$ is aperiodic, then all $j\in I$ are aperiodic. If $i$ is not aperiodic, then we define the period of state $i$ as $\gcd\{n:P^{(n)}_{ii}>0\}$.

# Hitting times:

The hitting time of a set of states $A\subset I$ is the random variable $H^A:\Omega\mapsto\mathbb{N}_0\cup\{\infty\}$ defined by the following formula:$$\Huge H^A:=\inf\{n\geq0:X_n\in A\}$$We also define:$$\Huge h_i^A:=\mathbb{P}_i[H^A<\infty],\,\,k_i^A:=\mathbb{E}_i[H^A]$$That is, when starting at state $i$, $h_i^A$ represents the probability that the hitting time is finite and $k_i^A$ is the expected hitting time. We can find this expectation:$$\Huge k_i^A=\sum_{n=0}^\infty n \mathbb{P}_i[H^A=n]+\begin{cases}0&\mathbb{P}_i[H^A=\infty]=0\\\infty&\text{otherwise}\end{cases}$$Sometimes $h_i^A$ is called absorption probability if $A$ is a closed communicating class. The vector of hitting probabilities $(h_i^A)_{i\in I}$ is the minimal non negative solution to the system of equations:$$\Huge \begin{cases}h_i^A=1&i\in A\\h_i^A=\sum_{j\in I}P_{ij}h_j^A&i\notin A\end{cases}$$The vector of hitting expectations $(k_i^A)_{i\in I}$ is the minimal non negative solution to the system of equations:$$\Huge \begin{cases}k_i^A=0&i\in A\\k_i^A=1+\sum_{j\in I}P_{ij}k_j^A&i\notin A\end{cases}$$To prove this theorem, we need to show that $(h_i^A)_{i\in I}$ solves the system of equations and that any other solution must not be minimal. To show that this solves the system of equations, we notice for $i\in A$, $h_i^A=1$ and if $i\notin A$ we have:$$ \mathbb{P}_i[H^A<\infty]=\sum_{j\in I}\mathbb{P}_i[H^A<\infty,X_1=j]=\sum_{j\in I}\mathbb{P}_i[H^A<\infty|X_1=j]\mathbb{P}[X_1=j]=\sum_{j\in I}P_{ij}h^A_j$$

# Gambler's ruin:

![[gamblers ruin|100%]]
This chain has transitions given by:
> $P_{00}=1$
> $P_{i\,i+1}=p$
> $P_{i\,i-1}=1-p=q$

We aim to find the probability of ending up broke starting from state $1$. Let $h_i=\mathbb{P}_i[H^{\{0\}}<\infty]$, the probability of hitting state $0$ after a finite amount of transitions. By the above theorems, we see that $(h_i)$ is the minimal non negative solution to:$$\Huge h_0=1,\,\,h_i=ph_{i+1}+qh_{i-1}$$For $i\geq1$. We know the solution to this [[Recurrence relations#General method for homogeneous linear recurrence relations|recurrence relation]] takes form:$$\Huge h_i=A+B\left(\frac{q}{p}\right)^i\text{ if }q\neq p,\,\,h_i=A+Bi\text{ if }q=p=\frac{1}{2}$$Now $h_0=1\implies A+B=1$. There are now three possibilities:
> $p<q$, $h_i=(1-B)+B\left(\frac{q}{p}\right)^i$ and since $h_i\in[0,1]$ we have that $B=0$ and $h_i=1$, you go broke
> $p>q$, $h_i=1-B\left(1-\left(\frac{q}{p}\right)^i\right)$. The minimal non negative solution to this takes $B=1$. This gives $h_i=\left(\frac{q}{p}\right)^i$. This may tend to zero if $i>>1$.
> $p=q$, $h_i=1+Bi\implies B=0$ so $h_i=1$ and you go broke.

# Birth-death chains:

Consider a similar, but different, example:![[life death|100%]]
Here we have $r_i+q_i=1$ for $i\geq1$. We then get the transition probabilities $P_{00}=1,P_{i\,i+1}=r_i,P_{i\,i-1}=q_i$. This chain can be interpreted as a population of $i$ individuals. Then $h_i$ is the probability that a population goes extinct if it starts with $i$ individuals, we then have:$$\Huge h_0=1,\,\,h_i=r_ih_{i+1}+q_ih_{i-1}$$Now we have a recurrence relation with non-constant coefficients. To solve this, we change variables:$$\Huge (r_i+q_i)h_i=r_ih_{i+1}+q_ih_{i-1}\implies r_i(h_i-h_{i+1})=q_i(h_{i+1}-h_i)$$So let $u_i=h_{i-1}-h_i,r_iu_{i+1}=q_iu_i$. We then see that $u_{i+1}=\frac{q_i}{r_i}u_i$, which becomes:$$\Huge u_{i+1}=\gamma_iu_1,\,\,\gamma_i=\prod_{j=1}^i\frac{q_j}{r_j}$$Also, $u_1+u_2+\dots+u_i=h_0-h_i=1-h_i$. Therefore:$$\Huge h_i=1-(u_1+u_2+\dots+u_i)=1-u_1(\gamma_0+\gamma_1+\dots+\gamma_i)$$With $\gamma_0=1$ and any $u_1$. Determining $u_1$ uses the minimal non negative solution:
> $\sum_{i=0}^\infty\gamma_i\to\infty\implies u_1=0$ since we require $h_i\in[0,1]$
> The other case, where the sum converges. Note that $h_i\geq0$ requires that $u_1\leq\left(\sum_{i=0}^{\infty}\gamma_i\right)^{-1}$, then minimality requires that these are equal. So we have:$$\Huge h_i=\frac{\sum_{k=i}^{\infty}\gamma_k}{\sum_{k=0}^\infty\gamma_k}$$

# Stopping times:

A random variable $T:\Omega\mapsto\{0,1,2\dots\}\cup\{\infty\}$ is a stopping time for $(X_n)_{n\in\mathbb{N}}$ if $\{T=k\}$ depends only on $X_0,X_1,\dots,X_k$ for all $k=0,1,\dots$. That is, $\{T=k\}$ can be written as an event only involving these random variables $X_1,\dots,X_k$. For example, $H^A$ is a stopping time, as it can be written as $\{H^A=k\}=\{X_0,X_1,\dots,X_{k-1}\notin A,X_k\in A\}$.

# Passage times and strong Markov:

The first passage time to $j,T_j$ is:$$\Huge T_j:=\inf\{n\geq1:X_n=j\}$$This is a stopping time since $\{T_j=k\}=\{X_1,\dots,X_{k-1}\neq j,X_k=j\}$.

The Markov Property dictates that, depending on $\{X_n=i\}$, the future $(X_{n+m})_{m\geq0}$ is $\text{Markov}(\delta_i,P)$ and is independent of the past. The strong Markov Property dictates the same is true for stopping times. 

Let $(X_n)_{n\geq0}$ be $\text{Markov}(\lambda,P)$ and let $T$ be a stopping time for $(X_n)_{n\geq0}$. Conditionally on $\{T,\infty\}$ and $\{X_T=i\}$ we have that $(X_{T+n})_{n\geq0}$ is $\text{Markov}(\delta_i,P)$ and independent of $X_0,X_1,\dots,X_T$.

 To prove this, we aim to decompose and event according to the value of a stopping time. We aim to show for any event $B$ determined by $X_0,X_1,\dots,X_T$ and any $n\geq0$ we have:$$\small \mathbb{P}[\{X_T=j_0,X_{T+1}=j_1,\dots,X_{T+n}=j_n\}\cap B|T<\infty,X_T=i]=\mathbb{P}_i[X_0=j_0,\dots, X_n=j_n]\mathbb{P}[B|T<\infty,X_t=i]$$Note that if $B=\Omega$, the above states that $(X_{T+n})_{n\geq0}$ is $\text{Markov}(\delta_i,P)$ as $\mathbb{P}[\Omega|T<\infty,X_T=i]=1$. $B\cap\{T=m\}$ is determined by $X_0,X_1,\dots,X_m$. We then have $$\mathbb{P}[\{X_T=j_0,\dots,X_{T+n}=j_n\}\cap B\cap\{T=m\}\cap\{X_T=i\}]=\mathbb{P}[\{X_m=j_0,\dots,X_{m+n}\}\cap\dots]$$Then by the Markov Property:$$\Huge =\mathbb{P}_i[X_0=j_0,\dots,X_n=j_n]\mathbb{P}[B\cap\{T=m\}\cap\{X_T=i\}]$$Note that $\{T<\infty\}=\bigcup_{m=0}^\infty\{T=m\}$, a disjoint union of events. So by countable additivity we have:$$\small \mathbb{P}[\{X_T=j_0,\dots,X_{T+n}=j_n\}\cap B\cap\{T<\infty\}\cap\{X_T=i\}]=\mathbb{P}_i[X_0=j_0,\dots,X_n=j_n]\mathbb{P}[B\cap\{T<\infty\}\cap\{X_T=i\}]$$As required.

Let $A$ be an event and write $1_A$ for the random variable:$$\Huge 1_A(\omega)=\begin{cases}1&\omega\in A\\0&\omega\notin A\end{cases}$$This is the indicator of $A$. Then write:$$\Huge T_j^{(n)}=\inf\{m>T_j^{(n-1)}:X_m=j\},\,\,T_j^{(0)}=0$$For the $n$th passage time to $j$. Now consider $i\neq j$ and:$$\Huge \sum_{m=0}^{T_j^{(n)}}1_{\{X_m=i\}}$$For $(X_n)_{n\geq0}$ with $\text{Markov}(\delta_j,P)$. 