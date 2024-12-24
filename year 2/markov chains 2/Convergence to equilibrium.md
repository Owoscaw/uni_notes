Suppose that a [[Definition and Properties|Markov chain]] with [[Definition and Properties#Stochastic matrices|stochastic matrix]] $P$ is [[Class structure#Periodicity|aperiodic]] and irreducible and $\pi$ is an [[Invariance#Invariance|invariant distribution]] for $P$. Then $(X_n)_{n\geq0}$ is $\text{Markov}(\lambda,P)$ and for all $j\in I$:$$\Huge \lim_{n\to\infty}\mathbb{P}[X_n=j]=\pi_j$$Taking $\lambda=\delta_i$ then this theorem states that $P_{ij}^{(n)}\to\pi_j$. Take the following as example:![[conv to eq example]]
# Ergodic theorem:

S
# Convergence proof:

Suppose that $P$ is irreducible and aperiodic such that $P$ has stationary distribution $\pi$. If $(X_n)_{n\geq0}$ is $\text{Markov}(\lambda,P)$ then for all $j\in I$ we have:$$\Huge\lim_{n\to\infty}\mathbb{P}[X_n=j]=\pi_j$$Assume the existence of two independent Markov chains $X_n$ and $Y_n$ such that $X_n$ is $\text{Markov}(\lambda,P)$ and $Y_n$ is $\text{Markov}(\pi,P)$ where $\pi$ is the invariant distribution of $P$. Suppose at some $n\geq0$ we have $X_n=Y_n$, then by the memorylessness of Markov chains we must have that the distribution of $X_n$ and $Y_n$ are the same. Since $Y_n$ has a stationary distribution, $X_n$ must therefore have a stationary distribution, it is therefore sufficient to show that $X_n=Y_n$ for some $n\geq0$.

Formally, let $(X_n)_{n\geq0}$ and $(Y_n)_{n\geq0}$ be $\text{Markov}(\lambda,P),\text{Markov}(\pi,P)$ respectively such that each chain is independent from one another. Let $b\in I$ and set $T=\inf\{n\geq1:X_n=Y_n=b\}$ as a [[Class structure#Stopping times|stopping time]] equivalent to the [[Class structure#Passage times and strong Markov|first passage time]] of the pair $(X_n,Y_n)_{n\geq0}$ to state $b$. 

It is sufficient to show that if $\mathbb{P}[T<\infty]=1$ and $(Z_n)_{n\geq}$ defined as:$$\Huge Z_n=\begin{cases}X_n&n<T\\Y_n&n\geq T\end{cases}$$Is $\text{Markov}(\lambda,P)$, we then get the result. 

Observe:$$\Huge\begin{align}
\mathbb{P}[Z_n=j]&=\mathbb{P}[Z_n=j,T>n]+\mathbb{P}[Z_n=j,T\leq n]\\
&=\mathbb{P}[X_n=j,T>n]+\mathbb{P}[Y_n=j,T\leq n]\\
|\mathbb{P}[Z_n=j]-\pi_j|&=|\mathbb{P}[Z_n=j]-\mathbb{P}[Y_n=j]|\\
&=|\mathbb{P}[X_n=j,T>n]+\mathbb{P}[Y_n=j,T\leq n]-\mathbb{P}[Y_n=j]|\\
&=|\mathbb{P}[X_n=j,T>n]-\mathbb{P}[Y_n=j,T<n]|\\
&\leq \mathbb{P}[X_n=j,T>n]+\mathbb{P}[Y_n=j,T>n]\\
&\leq2\mathbb{P}[T>n]
\end{align}$$Now notice that $\lim_{n\to\infty}\mathbb{P}[T>n]=\lim_{n\to\infty}\mathbb{P}\left[\bigcap_{k=0}^n\{T>k\}\right]=\mathbb{P}[T=\infty]=0$, so taking the limit of the above we get:$$\Huge \lim_{n\to\infty}|\mathbb{P}[Z_n=j]-\pi_j|\leq\lim_{n\to\infty}2\mathbb{P}[T>n]=0$$So we have that:$$\Huge\lim_{n\to\infty}\mathbb{P}[Z_n=j]=\pi_j$$As required. Note that this proof requires the chain to be aperiodic. Consider what would happen to the coupling argument if the Markov chain were periodic, in particular the simple two state Markov chain with unique invariant distribution $\begin{pmatrix}\frac{1}{2}&\frac{1}{2}\end{pmatrix}$. Suppose that the chain $(X_n)_{n\geq0}$ starts at state $0$ and the chain $(Y_n)_{n\geq0}$ starts at state $1$. As the $n\to\infty$ we see that whenever $X_n$ is at a given state, $Y_n$ must be at the other state, and the chains never meet. Therefore these chains can never be "coupled" and the proof fails.

## Alternative proof:
One can restate this theorem as follows. For every finite aperiodic irreducible Markov Chain with unique invariant distribution $\pi$ and transition matrix $P$ we have that:$$\Huge P^n\to\Pi\text{ as }n\to\infty$$Where $\Pi$ is the $|I|\times|I|$ matrix with rows given by $\pi$. 

Under these conditions, we know that $\exists n$ such that for all $i,j\in I$ we have $P_{ij}^{(n)}>0$. Now if $|I|<\infty$ this reduces to: $\exists r>0:P_{ij}^{(r)}>0\forall i,j\in I$, that is $P^{(r)}$ has all positive entries. Formally, for $i,j\in I$ there exists $N(i,j)$ such that for $n\geq N(i,j)\implies P_{ij}^{(n)}>0$ by taking $r=\max\{N(i,j)\}$. A consequence of this is that $\exists\delta>0:P_{ij}^{(r)}\geq\delta\pi_j$ for all $i,j\in I$. Note that taking $\delta=\min\{\frac{P_{ij}^{(r)}}{\pi_j}\}$ works since $P_{ij}^{(r)}=\frac{P_{ij}^{(r)}}{\pi_j}\cdot\pi_j\geq\delta\pi_j$ since $\pi_j>0$ for all $i,j\in I$. Now let $\theta=(1-\delta)$ and define $Q$ such that:$$\Huge P^r=(1-\theta)\Pi+\theta Q$$One can show that $Q$ is stochastic. We then claim:$$\Huge P^{rk}=(1-\theta^k)\Pi +\theta^kQ^k$$We prove this by induction on $k$. The base case is trivial, as it reduces to the definition of $Q$. Now suppose that this holds for $k=n$:$$\Huge\begin{align}
P^{(n+1)r}&=P^{nr}P^r=((1-\theta^n)\Pi+\theta^nQ^n)P^r\\
&=(1-\theta^n)\Pi P^r+\theta^nQ^nP^r\\
&=(1-\theta^n)\Pi+\theta^nQ^n((1-\theta)\Pi+\theta Q)\\
&=(1-\theta^n)\Pi+(1-\theta)\Pi \theta^nQ^n+\theta^{n+1}Q^{n+1}\\
&=(1-\theta^n)\Pi+(1-\theta)\theta^n\Pi+\theta^{n+1}Q^{n+1}\\
&=(1-\theta^n+\theta^n-\theta^{n+1})\Pi+\theta^{n+1}Q^{n+1}\\
&=(1-\theta^{n+1})\Pi+\theta^{n+1}Q^{n+1}
\end{align}$$Where we have used the fact that $\Pi P^r=\Pi$ as the rows of $\Pi$ are invariant under $P^r$ and the fact that $Q\Pi=\Pi$ since $Q$ is stochastic. We have advanced the induction as required, so the formula holds. A consequence of this is that:$$\Huge P^{rk+j}-\Pi=\theta^k(Q^kP^j-\Pi)$$Now since $\theta\in[0,1]$ we have that:$$\Huge \lim_{k\to\infty}P^{rk+j}-\Pi=\lim_{k\to\infty}\theta^k(Q^kP^j-\Pi)=0$$Implying that:$$\Huge \lim_{k\to\infty}P^{rk+j}-\Pi=0\implies\lim_{k\to\infty}P^k=\Pi$$As required. 

# Total variation distance

One can make the above proof clearer, let $\mu,\nu$ be two distributions on $I$. Define the total variation distance between $\mu,\nu$ to be:$$\Huge ||\mu-\nu||_{\text{TV}}=\max_{A\subset I}\left\{\left(\sum_{i\in A}\mu_i\right)-\left(\sum_{i\in A}\nu_i\right)\right\}$$That is, the maximum difference in probabilities assigned to any event. Suppose that $P$ is irreducible, aperiodic, and $|I|<\infty$. Then there exists $c>0$ and $0<\alpha<1$ such that for all $\lambda$:$$\Huge ||\lambda P^n-\pi||_\text{TV}\leq c\alpha^n$$One can see that as $n\to\infty$, we get convergence to equilibrium as required. To prove this, observe that $\lambda P^n-\pi=\lambda P^n-\lambda\Pi$. The proof follows from the definition of total variation distance. Taking $n=n(\epsilon,\alpha,c)=\log\frac{\epsilon}{c}\cdot\frac{1}{\log\alpha}$, we can see that the distribution of $X_n$ has total variation distance from $\pi$ given by $\epsilon$ with probability $1-\epsilon$. Taking the limit as $\epsilon\to0$ gives convergence to equilibrium as required.