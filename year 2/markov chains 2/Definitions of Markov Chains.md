Recall that a [[Probability definition#Axioms|probability space]] is a triple $(\Omega,\mathcal{F},\mathbb{P})$, with the sample space $\Omega$, the sigma algebra $\mathcal{F}$, and the probability measure $\mathbb{P}$. [[Sample spaces and events#Events|Events]] are subsets of $\Omega$, and we get the [[Probability definition#Axioms|probability axioms]].

## Stochastic matrices:
Let $I$ be a countable set of states, and $X:\Omega\mapsto I$ be an $I$-valued random variable. We define the distribution of $X$ as $\lambda:I\mapsto[0,1]$ given by $\lambda(i)=\lambda_i=\mathbb{P}[X=i]$. A [[Matrix definition|matrix]] $P=(p_{ij})_{i,j\in I}$ induced by $I$ is stochastic if every row of $P$ is a distribution. That is row $i$ is $(p_{ij})_{j\in I}$ is a row vector of probabilities.

This matrix is be used to encode a [[Graph definitions|graph]], where each entry represents the associated probability to go from one state to another.

Choose $I,\lambda,P$ where $\lambda$ is a distribution on $I$, and $P$ is a stochastic matrix. A Markov chain on $I$ with initial distribution $\lambda$ and transition matrix $P=(p_{ij})_{i,j\in I}$ is a sequence $(X_n)_{n\geq0}$ of $I$-valued random variables such that for every $n\geq0$ and any $i_0,i_1,\dots,i_{n+1}\in I$, and $\mathbb{P}[X_0=i_0,\dots,X_n=o_n]>0$:
> $\mathbb{P}[X_0=i_0]=\lambda_{i_0}$
> $\mathbb{P}[X_{n+1}=i_{n+1}|X_0=i_0,\dots,X_n=i_n]=P_{i_ni_{n+1}}$

We say that $(X_n)_{n\geq0}$ is $\text{Markov}(\lambda,P)$. The same can be said if $(X_n)_{0\leq n\leq N}$ is a finite sequence satisfying the above two requirements.


We propose that $(X_n)_{0\leq n\leq N}$ is $\text{Markov}(\lambda,P)$ if and only if for all $i_0,i_1,\dots,i_N\in I$ we have:$$\Huge \mathbb{P}[X_0=i_0,\dots,X_N=i_N]=\lambda_{i_0}P_{i_0i_1}P_{i_1i_2}\dots P_{i_{N-1}i_N}$$To prove this we have to show that the two requirements for a Markov chain imply the above proposition. Assume that $(X_n)_{0\leq n\leq N}$ is $\text{Markov}(\lambda,P)$, then for all $i_0,\dots,i_N\in I$ we have that: $$\tiny\mathbb{P}[X_0=i_0,\dots,X_N=i_N]=\mathbb{P}[X_0=i_0]\mathbb{P}[X_1=i_1,\dots,X_N=i_N]=\mathbb{P}[X_0=i_0]\mathbb{P}[X_1=i_1|X_0=i_0]\mathbb{P}[X_2=i_2,\dots,X_n=i_n|X_0=i_0,X_1=i_1]$$This process continues to give:$$\Huge \mathbb{P}[X_0=i_0]\mathbb{P}[X_1=i_1|X_0=i_0]\dots \mathbb{P}[X_n=i_n|X_0=i_0,\dots,X_{N-1}=i_{N-1}]$$Now we notice that by the two requirements from the assumption, this is equivalent to:$$\Huge \lambda_{i_0}P_{i_0i_1}\dots P_{i_{N-1}i_N}$$This proves the theorem. So we have that Markov chains are described by the probabilities of sequences of states, these probabilities have a simple form.

For example, suppose $X_i$ is uniform on the set $\{a,b,c\}$, with all $X_i$ independent. We ask if $(X_i)_{0\leq i\leq N}$ is a Markov chain on $I=\{a,b,c\}$. For any $i_0,i_1,\dots,i_N$, we have $\mathbb{P}[X_0=i_0,\dots,X_N=i_N]=(1/3)^{N+1}$. So if $\lambda=(\frac{1}{3},\frac{1}{3},\frac{1}{3})$ and $P=\frac{1}{3}\begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix}$, we then see $\lambda_{i_0}P_{i_0i_1}\dots P_{i_{N-1}i_N}=(1/3)^{N+1}$, so we indeed have a Markov chain.

# Memorylessness:

Let $\delta_i:I\mapsto[0,1]$ defined by:$$\Huge \delta_{ij}=\begin{cases}0&j\neq i\\1&j=i\end{cases}$$This is called the unit mass at $i$. If $(X_n)_{n\geq0}$ is $\text{Markov}(\lambda,P)$, then conditional on $X_m=i$, the sequence $(X_{m+n})_{n\geq0}$ is $\text{Markov}(\delta_i,P)$ and is independent of $X_0,X_1,\dots,X_{m-1}$.

To prove this, we will use the idea of an event $A$ being determined by $X_0,\dots,X_m$, meaning that $A$ is a union of events $A_k$, with each:$$\Huge A_k=\{X_0=i_0,\dots,X_m=i_m\}$$Here, each $A_k$ is called an elementary event. We show that for any $A$ determined by $X_0,\dots,X_{m-1}$ and any $i_m,i_{m+1},\dots,i_{m+n}\in I$ we have:$$\large \mathbb{P}[A\cap\{X_m=i_m,\dots,X_{m+n}=i_{m+n}\}|X_m=i]=\delta_{ii_m}P_{i_mi_{m+1}}\dots P_{i_{m+n-1}i_{m+n}}\mathbb{P}[A|X_m=i_m]$$This holds for all elementary $A$, by countable additivity. For such $A$, if $i_m\neq i$ then both sides are zero, otherwise $i_m=i$ and we have:$$\small LHS=\frac{\mathbb{P}[X_0=i_0,\dots,X_{m+n}=i_{m+n}]}{\mathbb{P}[X_m=i_m]}\delta_{ii_m}=\frac{\lambda_{i_0}P_{i_0i_1}\dots P_{i_{m+n-1}i_{m+n}}}{\mathbb{P}[X_m=i_m]}\delta_{ii_m}=\frac{\lambda_{i_0}P_{i_0i_1}\dots P_{i_{m-1}i_m}}{\mathbb{P}[X_m=i_m]}\delta_{ii_m}P_{i_mi_{m+1}}\dots P_{i_{m+n-1}i_{m+n}}$$Now notice the fraction is equivalent to $\mathbb{P}[A|X_m=i]$:$$\Huge LHS=\mathbb{P}[A|X_m=i]\delta_{ii_m}P_{i_mi_{m+1}}\dots P_{i_{m+n-1}i_{m+n}}$$And we have the proof as required.

Sometimes, linear algebra can be used to speed this process up, so let $(X_n)_{n\geq0}$ be $\text{Markov}(\lambda,P)$. For $n,m\geq0$:
>$\mathbb{P}[X_n=j]=(\lambda P^n)_j$
>$\mathbb{P}_i[X_n=j]:=\mathbb{P}[X_n=j|X_0=i]=(P^n)_{ij}$

Note that if $|I|<\infty$, the above is linear algebra as usual, however if $|I|=\infty$ we get the following:$$\Huge (\lambda P)_j:=\sum_{i\in I}\lambda_iP_{ij}\,,\,\,(P^2)=\sum_{k\in I}P_{ik}P_{kj}$$