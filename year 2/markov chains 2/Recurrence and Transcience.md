A state $i\in I$ is called recurrent if:$$\Huge \mathbb{P}_i[X_n=i\text{ for infinitely many }n]=1$$And transient if:$$\Huge \mathbb{P}_i[X_n=i\text{ for infinitely many }n]=0$$The event $X_n=i$ for infinitely many $n$ can be thought of as:$$\Huge \bigcap_{k\geq0}\{X_n=i\text{ at least }k\text{ times}\}$$
The following dichotomy holds:
> $\mathbb{P}_i[T_i<\infty]=1$, then $i$ is recurrent and $\sum_{n=0}^\infty P_{ii}^{(n)}=\infty$. That is, there is always a non-zero probability of returning to state $i$, and therefore the expected number of visits to $i$ is infinite.
> $\mathbb{P}_i[T_i<\infty]<1$, then $i$ is transient and $\sum_{n=0}^\infty P_{ii}^{(n)}<\infty$. That is, there is a non-zero probability that state $i$ is never returned to, and therefore has a finite expected number of visits.

Where $T_i$ is the first [[Class structure, hitting times, and stopping times#Passage times and strong Markov|passage time]] of $i$. Note that this means every state is either recurrent or transient, since $\mathbb{P}_i[T_i<\infty]\in[0,1]$ and the dichotomy defines the state on $[0,1]$. We define:$$\Huge T_i^{(r)}=\inf\{n>T_i^{(r-1)}:X_n=i\}$$As the $r$th passage time to $i$ and $T_i^{(0)}=0$.

Consider $(X_n(\omega))_{n\geq0}$ with $I=\{a,b,c\}$, the sequence of realized states on a $3$ state Markov Chain. Take for example $(X_n(\omega))_{n\geq0}=(a,a,c,b,a,b,b,c,a,b,b,\dots)$, we ask the first passage time to $a$ and the $3$rd passage time to $b$. We see that $T_a^{(1)}=1$ and $T_b^{(3)}=6$.

## Excursion length:
Define:$$\Huge S_i^{(r)}=\begin{cases}T_i^{(r)}-T_i^{(r-1)}&T_i^{(r-1)}<\infty\\0&\text{otherwise}\end{cases}$$As the $r$th excursion length:![[Recurrence and Transcience 2024-11-05 16.38.28.excalidraw]]For $r=2,3,\dots$ conditional on $\{T_i^{r-1}<\infty\}$, the excursion length $S_i^{(r)}$ is independent of $X_0,X_1,\dots,X_{T_i^{r-1}}$ and:$$\Huge \mathbb{P}[S_i^{(r)}=n|T_i^{(r-1)}<\infty]=\mathbb{P}_i[T_i=n]$$To prove this, we aim to use the [[Class structure, hitting times, and stopping times#Passage times and strong Markov|SMP]]. Set $T=T_i^{(r-1)}$, the Strong Markov Property states that conditioned on $\{T<\infty\}$ and $\{X_T=i\}$, $(X_{T+n})_{n\geq0}$ is $\text{Markov}(\delta_{i},P)$ and independent of $X_0,X_1,\dots,X_T$. So if $\{T<\infty\}$ occurs, $S_i^{(r)}$ is non-zero and $S_i^{(r)}=\inf\{n>0:X_{T+n}=i\}$, equivalent to the first passage time from $(X_{T+n})_{n\geq0}$ to $i$. So by SMP we get the claim, as $(X_{T+n})_{n\geq0}$ is $\text{Markov}(\delta_i,P)$.

Define:$$\Huge V_i=\sum_{n=0}^\infty1_{\{X_n=i\}}$$As the number of times $i$ is visited. Using the result for [[Random variables#Indicator random variables|indicator variables]] $\mathbb{E}[1_A]=\mathbb{P}[A]$ we see:$$\Huge \mathbb{E}_iV_i=\mathbb{E}_i\sum_{n=0}^\infty1_{\{X_n=i\}}=\sum_{n=0}^\infty\mathbb{E}_i[1_{\{X_n=i\}}]=\sum_{n=0}^\infty\mathbb{P}_i[X_n=i]=\sum_{n=0}^\infty P_{ii}^{(n)}$$
For $r=0,1,2,\dots$:$$\Huge\mathbb{P}_i[V_i>r]=(\mathbb{P}_i[T_i<\infty])^r$$Proven by induction as follows. Taking the base case $r=0$ the proof is trivial. Assume that the claim is true for some $r\geq0$, then if $X_0=i$:$$\Huge \{V_i>r+1\}=\{T_i^{(r+1)}<\infty\}$$That is, one must return to $i$ $r+1$ times to visit $i$ at least $r+2$ times, so:$$\Huge\begin{align}
\mathbb{P}_i[V_i>r+1]&=\mathbb{P}_i[T_i^{(r+1)}<\infty]\\&=\mathbb{P}_i[T_i^{(r)}<\infty,S_i^{(r+1)}<\infty]\\&=\mathbb{P}_i[S_i^{(r+1)}<\infty|T_i^{(r)}<\infty]\mathbb{P}_i[T_i^{(r)}<\infty]\\&=\mathbb{P}_i[S_i^{(r+1)}<\infty|T_i^{(r)}<\infty](\mathbb{P}_i[T_i<\infty])^r\\&=(\mathbb{P}_i[T_i<\infty])^r\sum_{n=0}^\infty\mathbb{P}_i[S_i^{(r+1)}=n|T_i^{(r)}<\infty]\\&=(\mathbb{P}_i[T_i<\infty])^r\sum_{n=0}^\infty\mathbb{P}_i[T_i=n]\\&=\mathbb{P}_i[T_i<\infty](\mathbb{P}_i[T_i<\infty])^r\\&=(\mathbb{P}_i[T_i<\infty])^{r+1}
\end{align}$$We have advanced the induction by one step, proving the theorem. We can now prove the dichotomy discussed previously:

## Recurrence/Transience proof:
Suppose $\mathbb{P}_i[T_i<\infty]=1$. Then $\mathbb{P}_i[\text{visit }i\text{ infinitely many times}]=\mathbb{P}_i[V_i=\infty]$:$$\Huge\begin{align}
\mathbb{P}_i[V_i=\infty]&=\lim_{r\to\infty}\mathbb{P}_i[V_i>r]\\&=\lim_{r\to\infty}(\mathbb{P}_i[T_i<\infty])^r\\&=\lim_{r\to\infty}1^r\\&=1
\end{align}$$So we have that $i$ is recurrent and $\sum_{n=0}^\infty P^{(n)}_{ii}=\mathbb{E}_i[V_i]=\infty$. Suppose $\mathbb{P}_i[T_i<\infty]<1$:$$\Huge\begin{align}
\sum_{n=0}^\infty P^{(n)}_{ii}&=\mathbb{E}_i[V_i]\\
&=\sum_{n=0}^\infty\mathbb{P}_i[V_i>n]\\
&=\sum_{n=0}^\infty(\mathbb{P}_i[T_i<\infty])^n\\&=\frac{1}{1-\mathbb{P}_i[T_i<\infty]}<\infty
\end{align}$$Since $\mathbb{P}_i[T_i<\infty]$ was assumed to be less than $1$, so the fraction can never reach infinity. Therefore we have $\mathbb{P}_i[V_i=\infty]=0$ and state $i$ is transient.

Let $C$ be a [[Class structure, hitting times, and stopping times#Communicating class definition|communicating]] class of a Markov Chain, then either:
> All states in $C$ are recurrent
> All states in $C$ are transient

Let $i,j\in C$ and suppose that $i$ is transient, that is $\sum_{n=0}^\infty P_{ii}^{(n)}<\infty$. We know that there exists $k,l$ such that $P_{ij}^{(k)}>0$ and $P_{ji}^{(l)}>0$ since $i\leftrightarrow j$. So for $r\geq0$ we have that:$$\Huge \begin{align}P_{ii}^{(k+l+r)}&\geq P_{ij}^{(k)}P_{jj}^{(r)}P_{ji}^{(l)}\\
P_{jj}^{(r)}&\leq\frac{1}{P_{ij}^{(k)}P_{ji}^{(l)}}P_{ii}^{(k+l+r)}\\
\sum_{r=0}^\infty P_{jj}^{(r)}&\leq\frac{1}{P_{ij}^{(k)}P_{ji}^{(l)}}\sum_{r=0}^\infty P_{ii}^{(k+l+r)}\\
&\leq\frac{1}{P_{ij}^{(k)}P_{ji}^{(l)}}\sum_{r=0}^\infty P_{ii}^{(r)}<\infty
\end{align}$$Therefore $j$ is transient. This also motivates the notion that every recurrent class is closed.

We propose that every finite closed class is recurrent. 