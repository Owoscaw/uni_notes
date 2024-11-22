
# Measures:

A measure is a row vector with non-negative values. Distributions are a special case of measures with entries that sum to $1$. If $P$ is a [[Definitions of Markov Chains#Stochastic matrices|stochastic matrix]], a measure $\lambda$ is called invariant if $\lambda P=\lambda$. An invariant measure is also called stationary or equilibrium.

If $\lambda$ is a measure and $\sum_{i\in I}\lambda_i<\infty$ then:$$\Huge \Pi_i=\frac{\lambda_i}{\sum_{j\in I}\lambda_j}$$Defines a distribution. Note that if $\lambda$ is invariant, $\Pi$ is invariant. If $|I|<\infty$ it is always possible to define a distribution. We ask for the following example, if there exist any stationary distribution(s):![[stationary dist]]
# Invariance:

If $(X_n)_{n\geq0}$ is $\text{Markov}(\lambda,P)$ and $\lambda$ is invariant for $P$, then for any $m\geq0$:$$\Huge (X_{m+n})_{n\geq0}\text{ is Markov}(\lambda,P)$$To prove this, consider the fact that $(X_{m+n})_{n\geq0}$ is $\text{Markov}(\mu,P)$ with $\mu_i=\mathbb{P}_\lambda[X_m=i]$ by the Markov property. We need to show that $\mu=\lambda_i$, that is that $\mu$ is the distribution of $X_m$. By the definition of a Markov chain, $\mu_i=\mathbb{P}_\lambda[X_m=i]=(\lambda P^m)_i=\lambda_i$. However notice that $\lambda P^m=(\lambda P)P^{m-1}=\lambda P^{m-1}=\dots=\lambda$ using the fact that $\lambda P=\lambda$. So we have:$$\Huge\begin{align}
\mathbb{P}_\lambda[(X_{m+n})_{n\geq0}\in A]&=\sum_{i\in I}\mathbb{P}_\lambda[(X_{m+n})_{n\geq0}\in A|X_m=i]\mathbb{P}_\lambda[X_m=i]\\
&=\sum_{i\in I}\mathbb{P}_i[(X_n)_{n\geq0}\in A]\mu_i\\
&=\mathbb{P}_\mu[(X_n)_{n\geq0}\in A]
\end{align}$$Therefore, $(X_{m+n})_{n\geq0}$ is indeed $\text{Markov}(\lambda,P)$.

Suppose that $|I|<\infty$ and that there exists an $i\in I$ such that for all $j\in I$:$$\Huge \lim_{n\to\infty}P_{ij}^{(n)}=\Pi_j$$Then $(\Pi_j)_{j\in I}$ is an invariant distribution for $P$. To prove this, consider the following. $\sum_{j\in I}\Pi_j=\sum_{j\in I}\lim_{n\to\infty}P_{ij}^{(n)}=\lim_{n\to\infty}\sum_{j\in I}P_{ij}^{(n)}=\lim_{n\to\infty}1=1$, so $\Pi$ is indeed a distribution. We now check that it is the distribution of $P$:$$\Huge\begin{align}
\Pi_j&=\lim_{n\to\infty}P_{ij}^{(n)}=\lim_{n\to\infty}\sum_{k\in I}P_{ik}^{(n-1)}P_{ki}\\
&=\sum_{k\in I}\left(\lim_{n\to\infty} P_{ik}^{(n-1)}\right)P_{kj}\\
&=\sum_{k\in I}\Pi_kP_{kj}=(\Pi P)_j
\end{align}$$So we have that $\Pi_j$ is indeed the distribution of $P$ and $\Pi$ is invariant. Note that putting the limit inside of the sum is conditional on $|I|<\infty$.

# Invariant 

We define a new measure $\gamma^k$ for $k\in I$ with:$$\Huge \gamma^k_i=\mathbb{E}_k\left[\sum_{n=0}^{T_k-1}1_{\{X_n=i\}}\right]$$That is, the expected number of visits to state $i$ before returning to $k$. Here, $T_k$ is the first [[Class structure, hitting times, and stopping times#Passage times and strong Markov|passage time]] to state $k$. Let $P$ be a stochastic matrix representing an irreducible Markov chain:
> $\gamma_k^k=1$
> $\gamma^kP=\gamma^k$
> $0<\gamma^k_i<\infty$ for all $i\in I$

The proof of the first statement is trivial. For the third, irreducibility implies that for any $i,k\in I$ there exists $m,n$ such that $P_{ik}^{(m)},P_{ki}^{(n)}>0$. Then by using statement two, we have that $\gamma_i^k=(\gamma^kP)_i=(\gamma^kP^m)_i\geq\gamma_k^kP_{ki}^{(m)}>0$. By the same reasoning one can show that $\gamma_i^k<\infty$ so we have the third statement, dependent on the second being true, proven as such:$$\Huge\begin{align}
\gamma_i^k&=\mathbb{E}_k\left[\sum_{n=0}^{T_k}1_{\{X_n=i\}}\right]\\
&=\mathbb{E}_k\left[\sum_{n=1}^\infty1_{\{X_n=i,T_k\geq n\}}\right]\\
&=\sum_{n=1}^\infty \mathbb{P}_k[X_n=i,T_k\geq n]\\
\end{align}$$Now we notice that $\mathbb{P}_k[X_n=i,T_k\geq n]=\sum_{j\in I}\mathbb{P}_k[X_n=i,X_{n-1}=j,T_k\geq n]$, then we can apply the Markov property at time $n-1$ to write $\mathbb{P}_k[X_n=i,T_k\geq n]=\sum_{j\in I}\mathbb{P}_k[X_{n-1}=j,T_k\geq n]P_{ji}$. Now we can write the sum as:$$\Huge\begin{align}
\gamma_i^k&=\sum_{n=1}^\infty\sum_{j\in I}P_{ji}\mathbb{P}_k[X_{n-1}=j,T_k\geq n]\\
&=\sum_{j\in I}P_{ji}\sum_{n=1}^\infty\mathbb{P}_k[X_{n-1}=j,T_k\geq n]\\
&=\sum_{j\in I}P_{ji}\mathbb{E}_k\left[\sum_{n=0}^{T_k-1}1_{\{X_n=j\}}\right]\\
&=\sum_{j\in I}P_{ji}\gamma_j^k=(\gamma^kP)_i
\end{align}$$As required. Here we have interchanged the sums, as every term is positive. So this measure is indeed invariant and satisfies the above properties. 

If $P$ is irreducible, $\lambda$ is an invariant measure on $P$, and $\lambda_k=1$ then we have:
> $\lambda_i\geq \gamma_i^k$ for all $i\in I$
> If $P$ is recurrent then $\lambda=\gamma^k$