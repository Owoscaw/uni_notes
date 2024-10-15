Recall that a [[Probability definition#Axioms|probability space]] is a triple $(\Omega,\mathcal{F},\mathbb{P})$, with the sample space $\Omega$, the sigma algebra $\mathcal{F}$, and the probability measure $\mathbb{P}$. [[Sample spaces and events#Events|Events]] are subsets of $\Omega$, and we get the [[Probability definition#Axioms|probability axioms]].

Let $I$ be a countable set of states, and $X:\Omega\mapsto I$ be an $I$-valued random variable. We define the distribution of $X$ as $\lambda:I\mapsto[0,1]$ given by $\lambda(i)=\lambda_i=\mathbb{P}[X=i]$. A [[Matrix definition|matrix]] $P=(p_{ij})_{i,j\in I}$ induced by $I$ is stochastic if every row of $P$ is a distribution. That is row $i$ is $(p_{ij})_{j\in I}$ is a row vector of probabilities.

This matrix is be used to encode a [[Graph definitions|graph]], where each entry represents the associated probability to go from one state to another.

Choose $I,\lambda,P$ where $\lambda$ is a distribution on $I$, and $P$ is a stochastic matrix. A Markov chain on $I$ with initial distribution $\lambda$ and transition matrix $P=(p_{ij})_{i,j\in I}$ is a sequence $(X_n)_{n\geq0}$ of $I$-valued random variables such that for every $n\geq0$ and any $i_0,i_1,\dots,i_{n+1}\in I$, and $\mathbb{P}[X_0=i_0,\dots,X_n=o_n]>0$:
> $\mathbb{P}[X_0=i_0]=\lambda_{i_0}$
> $\mathbb{P}[X_{n+1}=i_{n+1}|X_0=i_0,\dots,X_n=i_n]=P_{i_ni_{n+1}}$

We say that $(X_n)_{n\geq0}$ is $\text{Markov}(\lambda,P)$. The same can be said if $(X_n)_{0\leq n\leq N}$ is a finite sequence satisfying the above two requirements.


We propose that $(X_n)_{0\leq n\leq N}$ is $\text{Markov}(\lambda,P)$ if and only if for all $i_0,i_1,\dots,i_N\in I$ we have:$$\Huge \mathbb{P}[X_0=i_0,\dots,X_N=i_N]=\lambda_{i_0}P_{i_0i_1}P_{i_1i_2}\dots P_{i_{N-1}i_N}$$To prove this we have to show that the two requirements for a Markov chain imply the above proposition. Assume that $(X_n)_{0\leq n\leq N}$ is $\text{Markov}(\lambda,P)$, then for all $i_0,\dots,i_N\in I$ we have that: $$\tiny\mathbb{P}[X_0=i_0,\dots,X_N=i_N]=\mathbb{P}[X_0=i_0]\mathbb{P}[X_1=i_1,\dots,X_N=i_N]=\mathbb{P}[X_0=i_0]\mathbb{P}[X_1=i_1|X_0=i_0]\mathbb{P}[X_2=i_2,\dots,X_n=i_n|X_0=i_0,X_1=i_1]$$This process continues to give:$$\Huge \mathbb{P}[X_0=i_0]\mathbb{P}[X_1=i_1|X_0=i_0]\dots \mathbb{P}[X_n=i_n|X_0=i_0,\dots,X_{N-1}=i_{N-1}]$$Now we notice that by the two requirements from the assumption, this is equivalent to:$$\Huge \lambda_{i_0}P_{i_0i_1}\dots P_{i_{N-1}i_N}$$This proves the theorem.