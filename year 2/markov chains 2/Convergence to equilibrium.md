Suppose that a [[Definitions of Markov Chains|Markov chain]] with [[Definitions of Markov Chains#Stochastic matrices|stochastic matrix]] $P$ is [[Class structure, hitting times, and stopping times#Periodicity|aperiodic]] and irreducible and $\pi$ is an [[Statistical properties of Markov Chains#Invariance|invariant distribution]] for $P$. Then $(X_n)_{n\geq0}$ is $\text{Markov}(\lambda,P)$ and for all $j\in I$:$$\Huge \lim_{n\to\infty}\mathbb{P}[X_n=j]=\pi_j$$Taking $\lambda=\delta_i$ then this theorem states that $P_{ij}^{(n)}\to\pi_j$. Take the following as example:![[conv to eq example]]
# Ergodic theorem:

Suppose that $(X_n)_{n\geq0}$ is $\text{Markov}(\lambda,P)$ and is irreducible, where $V_i(n)=\sum_{m=0}^{n-1}1_{\{X_m=i\}}$:
> $\mathbb{P}\left[\frac{1}{N}V_i(N)\to_{N\to\infty}\frac{1}{\mathbb{E}_i[T_i]}\right]=1$
> If the chain is [[Statistical properties of Markov Chains#Recurrence with invariant distributions|positive recurrent]] and $f:I\mapsto\Re$ is bounded then:$$\Huge \mathbb{P}\left[\frac{1}{N}\sum_{m=0}^{N-1}f(X_m)\to_{N\to\infty}\mathbb{E}_\pi[f]\right]=1$$Where $\pi$ is the unique stationary distribution of $P$ and $\mathbb{E}_\pi[f]=\sum_{j\in I}f(j)\pi_j$.

We call the left hand side of these limits sample averages and the right hand side of these limits equilibrium averages. Then the ergodic theorem states that sample averages tend to equilibrium averages with probability $1$.

For example, suppose that each $(X_n)_{n\geq0}$ are identically distributed with $\mathbb{P}[X_n=H]=\mathbb{P}[X_n=T]=\frac{1}{2}$. This is a positive recurrent Markov chain on $\{H,T\}$. The ergodic theorem dictates that the fraction of $H$ tosses tends to $\frac{1}{2}$ with probability $1$. Suppose that £2 were awarded for $H$ and £1 was lost for $T$. Then $\frac{1}{N}\sum_{m=0}^{N-1}f(X_m)$ is the average earning in $N$ tosses with $f(H)=2,f(T)=-1$. Then the ergodic theorem dictates that this tends to $\mathbb{E}_\pi[f]$:$$\Huge \mathbb{E}_\pi[f]=\pi_Hf(H)+\pi_Tf(T)=\frac{1}{2}(2)-\frac{1}{2}=\frac{1}{2}$$So over $N$ tosses, the expected profit is £$\frac{N}{2}$.

# Metropolis chain:

Often it is easier to understand $(X_n)_{n\geq0}$, so we can compute $\frac{1}{N}\sum_{m=0}^{N-1}f(X_m)$ to find an approximation for $\mathbb{E}_\pi[f]$. This is done by constructing a Markov chain with invariant distribution $\pi$. Suppose $\tilde P_{ij}=\tilde P_{ji}$ for all $i,j\in I$, that $\tilde P$ is irreducible, and $\pi_i>0$. Set:$$\Huge P_{ij}=\begin{cases}\tilde P_{ij}\min\{1,\frac{\pi_j}{\pi_i}\}&i\neq j\\1-\sum_{i,j\in I}\tilde P_{ij}\min\{1,\frac{\pi_j}{\pi_i}\}&i=j\end{cases}$$So we take $(X_n)_{n\geq0}$ to be $\text{Markov}(\lambda,P)$. Then $P$ is stochastic, irreducible, and has invariant distribution $\pi$. Now the ergodic theorem applies and we have that:$$\Huge \frac{1}{N}\sum_{i=0}^{N-1}f(X_i)\to\mathbb{E}_\pi[f]$$
By definition, the sum of each row in $P$ will be $1$, so we have that $P$ is stochastic. Since $\tilde P$ was stochastic, each non-diagonal entry of  $P$ will be positive by definition. We then need to check the invariance of $\pi$. Using detailed balance for $i\neq j$ we see that:$$\Huge\begin{align} 
\pi_iP_{ij}&=\pi_i\tilde P_{ij}\min\left\{1,\frac{\pi_j}{\pi_i}\right\}\\
&=\tilde P_{ij}\min\{\pi_i,\pi_j\}\\
&=\tilde P_{ji}\min\{\pi_j,\pi_i\}=\pi_jP_{ji}
\end{align}$$So we have that $\pi$ is indeed the invariant distribution of $P$. Irreducibility of $\tilde P$ implies irreducibility of $P$. This concludes the proof.

A substitution code is a function from one alphabet to another. Markov chains can be used to break such substitutions. To do this, take $I=\{\text{substitution codes}\}$ and, given a message, design $\pi$ such that the correct decoding $f$ is the most likely by far.

# Convergence proof:

Suppose that $P$ is irreducible and aperiodic such that $P$ has stationary distribution $\pi$. If $(X_n)_{n\geq0}$ is $\text{Markov}(\lambda,P)$ then for all $j\in I$ we have:$$\Huge\lim_{n\to\infty}\mathbb{P}[X_n=j]=\pi_j$$Assume the existence of two independent Markov chains $X_n$ and $Y_n$ such that $X_n$ is $\text{Markov}(\lambda,P)$ and $Y_n$ is $\text{Markov}(\pi,P)$ where $\pi$ is the invariant distribution of $P$. Suppose at some $n\geq0$ we have $X_n=Y_n$, then by the memorylessness of Markov chains we must have that the distribution of $X_n$ and $Y_n$ are the same. Since $Y_n$ has a stationary distribution, $X_n$ must therefore have a stationary distribution, it is therefore sufficient to show that $X_n=Y_n$ for some $n\geq0$.

Formally, let $(X_n)_{n\geq0}$ and $(Y_n)_{n\geq0}$ be $\text{Markov}(\lambda,P),\text{Markov}(\pi,P)$ respectively such that each chain is independent from one another. Let $b\in I$ and set $T=\inf\{n\geq1:X_n=Y_n=b\}$ as a [[Class structure, hitting times, and stopping times#Stopping times|stopping time]] equivalent to the [[Class structure, hitting times, and stopping times#Passage times and strong Markov|first passage time]] of the pair $(X_n,Y_n)_{n\geq0}$ to state $b$. 

It is sufficient to show that if $\mathbb{P}[T<\infty]=1$ and $(Z_n)_{n\geq}$ defined as:$$\Huge Z_n=\begin{cases}X_n&n<T\\Y_n&n\geq T\end{cases}$$Is $\text{Markov}(\lambda,P)$, we then get the result. 

Observe:$$\Huge\begin{align}
\mathbb{P}[Z_n=j]&=\mathbb{P}[Z_n=j,T>n]+\mathbb{P}[Z_n=j,T\leq n]\\
&=\mathbb{P}[X_n=j,T>n]+\mathbb{P}[Y_n=j,T\leq n]\\
|\mathbb{P}[Z_n=j]-\pi_j|&=|\mathbb{P}[Z_n=j]-\mathbb{P}[Y_n=j]|\\
&=|\mathbb{P}[X_n=j,T>n]+\mathbb{P}[Y_n=j,T\leq n]-\mathbb{P}[Y_n=j]|\\
&=|\mathbb{P}[X_n=j,T>n]-\mathbb{P}[Y_n=j,T<n]|\\
&\leq \mathbb{P}[X_n=j,T>n]+\mathbb{P}[Y_n=j,T>n]\\
&\leq2\mathbb{P}[T>n]
\end{align}$$Now notice that $\lim_{n\to\infty}\mathbb{P}[T>n]=\lim_{n\to\infty}\mathbb{P}\left[\bigcap_{k=0}^n\{T>k\}\right]=\mathbb{P}[T=\infty]=0$, so taking the limit of the above we get:$$\Huge \lim_{n\to\infty}|\mathbb{P}[Z_n=j]-\pi_j|\leq\lim_{n\to\infty}2\mathbb{P}[T>n]=0$$So we have that:$$\Huge\lim_{n\to\infty}\mathbb{P}[Z_n=j]=\pi_j$$As required.