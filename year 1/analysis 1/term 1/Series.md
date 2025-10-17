# Fundamental notions and properties:

Let $(a_k)_{k\in\mathbb N}$ be a [[Sequences#Limit of a sequence|sequence]]. Then the sequence of partial sums $(s_n)_{n\in\mathbb N}$ is defined as:$$\Huge S_n=\sum_{k=1}^na_k=a_1+\dots+a_n$$
This sequence is called the series of $(a_k)_{k\in\mathbb N}$ . If the sequence $(S_n)_{n\in\mathbb N}$ is convergent, then the series is convergent. In this case we write:$$\Huge \sum_{k=1}^\infty a_k=\lim_{n\to\infty}S_n$$
Otherwise it is called divergent. Sometimes series start at $k=0$, this will affect the limit, however convergence is not. That is to say:$$\Huge \sum_{k=1}^\infty a_k\,\,\text{converges}\iff\sum_{k=N}^\infty a_k\,\,\text{converges}$$
## Geometric series:

Take $q\in\Re$, then define:$$\Huge S_n=\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q},\,\,q\neq 1$$$$\Huge \lim_{n\to\infty}S_n=\lim_{n\to\infty}\frac{1-q^{n+1}}{q-1}=\begin{cases}\displaystyle{\frac{1}{1-q}}&\text{for}\,\,|q|<1\\\text{unbounded}&\text{for}\,\,|q|>1\end{cases}$$ 
The special cases where $q=\pm1$ are defined as follows:$$\Huge S_n=\sum_{k=0}^n1^k=1+1+\dots+1=n,\,\lim_{n\to\infty}S_n=\text{unbounded}$$
$$\large S_n=\sum_{k=0}^n(-1)^k=1-1+\dots+(-1)^n=\begin{cases}1&\text{if $n$ is even}\\0&\text{if $n$ is odd}\end{cases},\,\lim_{n\to\infty}S_n\,\text{is not convergent}$$
So we have:$$\Huge \sum_{k=0}^\infty q^k=\frac{1}{1-q}\iff|q|<1$$
If $\sum_{k=0}^\infty a_k$ is convergent, then $\lim_{k\to\infty}a_k=0$. This is proven as follows:![[series divergence criteria]]
Just because the sequence converges to zero, the series does not necessarily converge. This is shown in the following example:![[harmonic divergence]]
Assume that $\sum_{k=0}^\infty a_k$ and $\sum_{k=0}^\infty b_k$ both converge to $a$ and $b$ respectively. Then we can define a sort of [[Sequences#Calculus of limits theorem ( Limits and Continuity Consequences of continuity COLT )|COLT]] for series:
> $\displaystyle{\sum_{k=0}^\infty}a_k+b_k$ converges to $a+b$
> $\displaystyle{\sum_{k=0}^\infty \lambda a_k}$ converges to $\lambda a$ with $\lambda\in\Re$

# Convergence criteria:

Let $N\in\mathbb N$, and $(a_k)_{k\geq N},(b_k)_{k\geq N}$ be sequences with $0\leq a_k\leq b_k$ for all $k\geq N$ (comparison test):
> If $\displaystyle{\sum_{k=N}^\infty b_k}$ is convergent with limit $b$, then $\displaystyle{\sum_{k=N}^\infty a_k}$ is also convergent with limit $a\leq b$
> If $\displaystyle{\sum_{k=N}^\infty a_k}$ is divergent, then so is $\displaystyle{\sum_{k=N}^\infty b_k}$

This is proven as follows. Let $s_n=\sum_{k=N}^na_k$ and $t_n=\sum_{k=N}^n$. We have $0\leq s_n\leq t_n\leq b$, since $(t_n)$ is monotonically increasing with a limit $b$. $(s_n)$ is also monotonically increasing and bounded above by $b$, so must be convergent to a limit $a$. $s_n\leq t_n$ implies:$$\Huge a=\lim_{n\to\infty}s_n\leq\lim_{n\to\infty}t_n=b
$$
Notice that $a_k\geq0$ is bounded by the limit of $t_n$. So if $s_n$ is not convergent, it is not bounded by the limit of $t_n$, so this limit cannot exist. Therefore $t_n$ must also be divergent.

Let $\alpha\in\Re$, then:$$\Huge \sum_{k=1}^\infty\frac{1}{k^\alpha}\,\,\text{converges}\iff\alpha>1$$
If $\alpha=1$, we get the harmonic series, which has been shown to diverge. If we take $\alpha\leq1$, we get that the series is still divergent by the comparison test. So now assume $\alpha>1$:
![[inverse alpha convergence]]

# Alternating series:

A series $\displaystyle{\sum_{k=1}^\infty a_k}$ is alternating if:
> $a_{2k}\geq0$ and $a_{2k-1}\leq 0$ for all $k\in\mathbb N$
> or $a_{2k}\leq0$ and $a_{2k-1}\geq0$ for all $k\in\mathbb N$

## Alternating sign test:

Let $(a_k)_{k\in\mathbb N}$ be a monotonically decreasing sequence of positive numbers with $\lim_{n\to\infty} a_k=0$, then the alternating series $\displaystyle{\sum_{k=1}^\infty(-1)^{k+1}a_k}$ is also convergent. Considering the sequence of partial sums, we have:$$\Huge s_2\leq s_4\leq\dots\leq s_{2n}\leq\dots\leq\sum_{k=1}^\infty(-1)^{k+1}a_k\leq\dots\leq s_{2n+1}\leq\dots\leq s_3\leq s_1$$
$$\Huge \left|s_n-\sum_{k=1}^\infty(-1)^{k+1}a_k\right|\leq a_{n+1}$$
Since $a_k$ is monotonically increasing, we get $a_k-a_{k-1}\geq0$, which implies $a_{2n+1}-a_{2n+2}\geq0$. Adding the partial sum $s_{2n}$, we get $s_{2n+2}=s_{2n}+a_{2n+1}-a_{2n+2}\geq s_{2n}$, so the subsequence $(s_{2n})_{n\in\mathbb N}$ is monotonically increasing. Similarly, we can show $(s_{2n-1})_{n\in\mathbb N}$ is monotonically decreasing. We then get $s_{2n}=s_{2n-1}-a_{2n}<s_{2n-1}<s_1$, so the subsequence is bounded. Similarly, $(s_{2n-1})_{n\in\mathbb N}$ is also bounded. These are both bounded subsequences that are either monotonically increasing or decreasing, so must be convergent. We denote these as: $$\Huge s^e=\lim_{n\to\infty}s_{2n},\,s^o=\lim_{n\to\infty}s_{2n-1}$$
Now since $a_{2n}=s_{2n-1}-s_{2n}\to0$ as $n\to\infty$, we get that by COLT, $s^e=s^o$, denoted by $s$. Then claim that the original sequence $(s_n)_{n\in\mathbb N}$ converges to $s$. Let $\epsilon>0$, from the convergence of subsequences we also get $n_e,n_0\in\mathbb N$ with:$$\Huge |s_{2n}-s|<\epsilon\,\,\forall2n\geq n_e\,\,\text{and}\,\,|s_{2n-1}-s|<\epsilon\,\,\forall2n-1\geq n_o$$
So take $n_0=max\{n_e,n_o\}$, then for all $n\geq n_0$ we get that $|s_n-s|<\epsilon$, meaning that the alternating series converges to $s$.

# Absolute convergence:

Let $\sum_{k=1}^\infty a_k$ be a series. This series is absolute convergent if $\sum_{k=1}^\infty|a_k|$ is convergent. Every absolute convergent series is also convergent with:$$\Huge \left|\sum_{k=1}^\infty a_k\right|\leq \sum_{k=1}^\infty|a_k|$$
Let $\sum_{k=1}^\infty a_k$ be absolute convergent. Then $\sum_{k=1}^\infty 2|a_k|$ is also convergent by COLT. Since $0\leq |a_k|+a_k\leq 2|a_k|$. By the comparison theorem, $\sum_{k=1}^\infty|a_k|+a_k$ is convergent. Using COLT again, we get:$$\Huge \sum_{k=1}^\infty a_k=\sum_{k=1}^\infty|a_k|+a_k-|a_k|\,\,\text{is convergent}$$
We have the result by the triangle inequality when considering:$$\Huge \left|\sum_{k=1}^n a_k\right|\leq\sum_{k=1}^n|a_k|\leq\sum_{k=1}^\infty|a_k|$$And taking the limit as $n\to\infty$. Since we know it is convergent.

# Ratio test:

Let $(a_k)_{k\in\mathbb N}$ be a sequence with $a_k\neq0$ for all but possibly finitely many $k$:
> If $\displaystyle{\lim_{k\to\infty}\left|\frac{a_{k+1}}{a_k}\right|<1}$ then the series $\displaystyle{\sum_{k=1}^\infty a_k}$ converges absolutely
> If $\displaystyle{\lim_{k\to\infty}\left|\frac{a_{k+1}}{a_k}\right|>1}$ then the series $\displaystyle{\sum_{k=1}^\infty a_k}$ is divergent
> If this limit equals $1$, try a different test

This limit does not necessarily have to exist. In fact if $\displaystyle{\limsup_{k\to\infty}}\left|\frac{a_{k+1}}{a_k}\right|<1$, then we can conclude the same as above. The other case where if $\left|\frac{a_{k+1}}{a_k}\right|\geq1$ for all but finitely many $k$, then the series diverges.

We can show that if $\left|\frac{a_{k+1}}{a_k}\right|\leq q<1$ for all but finitely many $k$, then the series converges absolutely. We assume that this inequality is true for all $k\geq n_0\in\mathbb N$. This implies that for all $j\in\mathbb N$, $|a_{n_0+j}|\leq q|a_{n_0+j-1}|\leq\dots\leq q^j|a_{n_0}|$. Now we look at the series:$$\Huge \sum_{j=1}^\infty|a_{n_0+j}|\leq\sum_{j=1}^\infty q^j|a_{n_0}|=\frac{|a_{n_0}|}{1-q}\,\,\text{is convergent}$$
By the comparison theorem, our LHS series must also converge. So we have that:$$\Huge \sum_{j=1}^\infty|a_{n_0+j}|=\sum_{j=n_0+1}^\infty a_j\,\,\text{converges absolutely}$$
On the other hand, we assume that $\left|\frac{a_{k+1}}{a_k}\right|\geq 1$ for all $k\geq n_0$. Then $|a_{k+1}|\geq|a_k|\geq|a_{n_0}|>0$. We have that every term is greater than the previous, so the series is bounded from below by $0$ and is not bounded above, as there will always be a term $|a_{k+1}|$ that makes the series greater. Since this series is unbounded, it does not converge.

# Root test:

For a sequence $(a_k)_{k\in\mathbb N}$, we set $a=\limsup_{k\to\infty} \sqrt[k]{|a_k|}$. Then we get:
> If $a<1$ then $\displaystyle{\sum_{k=1}^\infty a_k}$ is absolutely convergent
> If $a>1$ then $\displaystyle{\sum_{k=1}^\infty a_k}$ diverges

To prove this, assume $a<1$. Then for all buy finitely many $k\geq n_0$ we have:$$\Huge \sqrt[k]{|a_k|}\leq q<1\implies|a_k|\leq q^k$$
Comparing this with a converging geometric series $\sum_{k=1}^\infty q^k$, we get that the aforementioned series is convergent. To prove the other part, assume $a>1$. Then there exists $q>1$ with:$$\Huge \sqrt[k]{|a_k|}\geq q>1\implies|a_k|\geq q^k$$
Comparing this with the diverging geometric series $\sum_{k=1}^\infty q^k$, we get that the aforementioned series is divergent. Both parts of this proof use the comparison test.

# Rearrangement of series:

$$\Huge \sum_{k=1}^\infty\frac{(-1)^{k+1}}{k}$$
Is a convergent series by the alternating sign test, with limit $c\in(\frac{1}{2},1)$. Rearranging the summands such that every positive term is followed by the next two negative summands leads to the result that $c=\frac{1}{2}c$, which implies that $c=0$, a contradiction. This shows that the commutativity used in finite sums cannot be used for infinite sums.

Let $\sum_{k=1}^\infty a_k$ be a series that is convergent but not absolutely convergent, we call this conditionally convergent. Riemann's Rearrangement Theorem states that for $L\in\Re$, there exists a rearrangement:$$\Huge \sigma:\mathbb N\mapsto\mathbb N$$Such that the rearranged sum will converge to $L$. Moreover, the sum can also be rearranged so that it diverges. The idea of the proof is as follows: Take all the positive terms in $a_k$ and order them decreasingly, that is $b_1\geq b_2\geq\dots\geq b_n\geq\dots\geq 0$. We then show $\lim_{k\to\infty}b_k=0$. Doing the same with the negative terms, $c_1\leq c_2\leq\dots\leq c_n\leq\dots\leq0$, with $\lim_{k\to\infty}c_k=0$. One can show that both $\sum_{k=1}^\infty b_k$ and $\sum_{k=1}^\infty c_k$ diverge to $\infty,-\infty$ respectively. Assume $L>0$, then add up sufficient $b_i$ until the sum is greater than $L$. Now add sufficient $c_i$ until the sum is less than $L$. Since $b_i,c_i$ are sorted by size, iterating this process will oscillate the limit around $L$ with increasing precision on each step.

Note that for an absolutely convergent series, every rearrangement still converges to the same limit. That is:$$\Huge \sum_{k=1}^\infty a_k=\sum_{k=1}^\infty a_{\sigma(k)}$$Since for any $\epsilon<0$ we have:$$\Huge -\epsilon<\sum_{k=1}^na_k-a_{\sigma(k)}<\epsilon$$For sufficiently large $N$. Consider the partial sum of the absolute summands:$$\Huge S_n=\sum_{k=1}^n|a_k|$$This will converge to $s$. Then there exists $n_0$ with:$$\Huge |S_n-s|=\sum_{k=n+1}^\infty|a_k|<\frac{\epsilon}{2}$$Now take $n\geq n_0$ such that $n>\sigma^{-1}(1),\dots,\sigma^{-1}(n_0)$, then:$$\large \left|\sum_{k=1}^na_k-a_{\sigma(k)}\right|=\left|\sum_{k=n_0+1}^na_k-\sum_{k=1,\,\sigma(k)\geq n_0+1}^na_{\sigma(k)}\right|\leq\sum_{k=n_0+1}^n|a_k|+\sum_{k=n_0+1}^\infty|a_k|<\frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon$$So you get convergence with the same limit.

## Cauchy product theorem:

Let $\sum_{k=0}^\infty a_k,\sum_{k=0}^\infty b_k$ be absolutely convergent series with limits $a,b$ respectively. Then for $n\geq0$ let:$$\Huge c_n=\sum_{k=0}^na_kb_{n-k}$$
Then the series $\sum_{k=0}^n c_k$ is called the Cauchy product of the two series. This is absolutely convergent with $\lim_{k=0}^\infty c_k=a\cdot b$