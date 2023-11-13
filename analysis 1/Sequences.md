A sequence of real numbers is a function, $\mathbb{N}\mapsto\Re$. Each $n\in\mathbb{N}$ has an assigned value $x_n\in\Re$, denoted as $(x_n)_{n\in\mathbb{N}}$. The following are different types of sequences:
> Let $x_n=\lambda$ for all $n\in\mathbb{N},\,\lambda\in\Re$. This is called a constant sequence.
> Let $x_n=\frac{1}{n}$ for all $n\in\mathbb{N}$.
> Let $x_n=(-1)^n$ for all $n\in\mathbb{N}$, this oscillates between $+1$ and $-1$.
> Let $x_n=x_{n-1}+x_{n-2}$, with $x_1=1,\,x_2=1$, for all $n\in\mathbb{N}>2$. This is defined recursively, in terms of other elements of the sequence.

# Limit of a sequence:

A real sequence $(x_n)_{n\in\mathbb{N}}$ is said to be convergent to limit $x\in\Re$ if for every $\epsilon>0$, there exists an index $n_0\in\mathbb{N}$ such that $|x_n-x|<\epsilon$ for all $n\geq n_0$. In this case, we write:
$$\Huge \forall \epsilon>0,\,\exists\,n_0\in\mathbb{N}:|x_n-x|<\epsilon\,\,\,\forall n\geq n_0,\,\,\lim_{n\to\infty}x_n=x$$
If the sequence is not convergent, it is divergent:
![[conv div example]]
Examples:
> Take $x_n=\lambda$ for all $n\in\mathbb{N}$. Take $\lambda$ to be a candidate for the limit. Start with $\epsilon>0$, there needs to be an $n_0$ with $|x_n-\lambda|<\epsilon$ for all $n\geq n_0$. This simplifies to $|\lambda-\lambda|<\epsilon$, then to $\epsilon>0$. So $\lim_{n\to\infty}x_n=\lambda$.
> Take $x_n=\frac{1}{n}$ for all $n\in\mathbb{N}$. Take $0$ to be a candidate for the limit. Start with $\epsilon>0$, there needs to be an $n_0$ with $|x_n-0|<\epsilon$ for all $n\geq n_0$. This simplifies to $\frac{1}{n}<\epsilon\iff\frac{1}{\epsilon}<n$ for all $n\geq n_0$. By Archimedes theorem, there exists $n_0\in\mathbb{N}$ with $n_0>\frac{1}{\epsilon}$, then use $\frac{1}{\epsilon}<n_0\leq n$. By transitivity, $n>\frac{1}{\epsilon}$ and the definition of a limit is satisfied with $\lim_{n\to\infty}x_n=0$.
> Take $x_n=(-1)^n$ for $n\in\mathbb{N}$. This is a divergent sequence, so we will show it is not convergent. Take $x\in\Re$ to be a candidate for the limit. $|x_n-x|=|x_n-x_{n+1}+x_{n+1}-x|\leq |x_n-x_{n+1}|+|x_{n+1}-x|=2+|x_{n+1}-x|$. So we have $2\leq |x_n-x|+|x-x_{n+1}|$. If $x_n\to x$ as $n\to\infty$, assume $|x_n-x|<\epsilon$. As soon as $\epsilon\leq1$, this will not work and the limit cannot exist.

# Properties of Limits:

## Uniqueness:

A convergent sequence $(x_n)_{n\in\mathbb{N}}$ has precisely one limit. Let $x,x^\circ$ be limits of $x_n$, and assume that $x\neq x^\circ$. Now let $\epsilon=\frac{|x-x^{\circ}|}{2}$:![[uniqueness of the limit example]]
By convergence to $x$, there must be $n_0$ such that $|x_n-x|<\epsilon$ ,for all $n\geq n_0$. By convergence to $x^\circ$, there must be $n_1$ such that $|x_n-x^\circ|<\epsilon$, for all $n\geq n_1$. For $n\geq max(n_0,n_1)$:$$\Huge 2\epsilon=|x-x^\circ|\leq|x-x_n|+|x_n-x^\circ|<\epsilon+\epsilon=2\epsilon$$So we have $2\epsilon<2\epsilon$, $\epsilon<\epsilon$, a contradiction. Therefore our assumption must be false, so $x\neq x^\circ$ must not be true.

## [[The completeness axiom#Bounds, suprema, and infima|Boundedness]]:

Let $(x_n)_{n\in\mathbb{N}}$ be a real sequence, and denote the set $X=\{x_n\in\Re:n\in\mathbb{N}\}$. The sequence $x_n$ is bounded above if the set $X$ is bounded above. Similarly, $x_n$ is bounded below if the set $X$ is bounded below. Finally $x_n$ is bounded if the set $X$ is bounded. Every convergent sequence is bounded.

# Convergence criteria:

## Squeezing theorem:

Let $(x_n)_{n\in\mathbb{N}}$, $(y_n)_{n\in\mathbb{N}}$ be real sequences. If $|x_n|\leq y_n$ for all $n\in\mathbb{N}$, and $y_n\to0$ as $n\to\infty$, then also $x_n\to0$ as $n\to\infty$. Let $\epsilon>0$, since $y_n\to0$ as $n\to\infty$, $\exists\,n_0\in\mathbb{N}$ with $y_n=|y_n-0|<\epsilon$ for all $n\geq n_0$. This implies:$$\Huge |x_n-0|=|x_n|\leq y_n<\epsilon,\,\forall n\geq n_0$$
This shows that $x_n\to0$ as $n\to\infty$. Example:
![[convergent example]]

## Calculus of limits theorem ([[Limits and Continuity#Consequences of continuity|COLT]]):

Let $(x_n)_{n\in\mathbb{N}}$, $(y_n)_{n\in\mathbb{N}}$ be convergent to $x=\lim_{n\to\infty}x_n$ and $y=\lim_{n\to\infty}y_n$, let $a,b\in\Re$, then:
> $ax_n+by_n\to ax+by$ as $n\to\infty$
> $x_ny_n\to xy$ as $n\to\infty$
> $\frac{x_n}{y_n}\to \frac{x}{y}$ as $n\to\infty$ given $y\neq 0$ and $y_n\neq 0,\,\forall n\in\mathbb{N}$
> 

Proof for second consequence is as follows. Consider $|x_ny_n-xy|=|x_ny_n-x_ny+x_ny-xy|$. Using the triangle inequality:$$\Huge |x_ny_n-xy|\leq |x_n(y_n-y)|+|(x_n-x)y|=|x_n||y_n-y|+|y||x_n-x|$$
As convergent sequences are bounded, $x_n$ must be bounded. Then $x_n\leq C$ for some $C\in\Re$, also assume $|y|\leq C$. Then we have:$$\Huge |x_ny_n-xy|\leq C\left(|y_n-y|-|x_n-x|\right)$$
Now choose some $\epsilon>0$. Since $x_n$ converges, there is $n_0$ with $|x_n-x|<\frac{\epsilon}{2C}$ and since $y_n$ converges there is $n_1$ with $|y_n-y|<\frac{\epsilon}{2C}$. Then for $n\geq max\{n_0,n_1\}$:$$\Huge |x_ny_n-xy|\leq C\left(|y_n-y|+|x_n-x|\right)<C\left(\frac{\epsilon}{2C}+\frac{\epsilon}{2C}\right)=\epsilon$$
Then this means $\lim_{n\to\infty}x_ny_n=xy$, as the criteria for convergence have been met ($|(x_ny_n)-(xy)|<\epsilon$) for all $\epsilon>0$. Now consider this example:
![[COLT example]]

Let $(x_n)_{n\in\mathbb{N}}$ be a real sequence such that $x_n\in[a,b]$ for all $n\in\mathbb{N}$, where $a,b\in\Re$. If the sequence is convergent to $x\in\Re$, then $x\in[a,b]$. The proof is by contradiction, assume that $x<a$. Now choose $\epsilon=\frac{a-x}{2}>0$. By convergence:$$\Huge \exists\,n_o\in\mathbb{N}:|x_n-x|<\epsilon,\,\forall n\geq n_0$$$$\Huge -\epsilon<x_n-x<\epsilon$$$$\Huge -\epsilon<x-x_n$$
Now consider:$$\Huge a-x_n=a-x+x-x_n>2\epsilon-\epsilon=\epsilon>0$$
So then $a>x_n$, a contradiction. Therefore our assumption is false, so the theorem must be true, as a similar proof exists for $x>b$. This has a corollary with $(x_n)_{n\in\mathbb{N}}$ and $(y_n)_{n\in\mathbb{N}}$, two convergent sequences with $x_n\leq y_n,\,\forall n\in\mathbb{N}$, then:$$\Huge \lim_{n\to\infty}x_n=\lim_{n\to\infty}y_n$$
This is proven by considering $a_n=y_n-x_n\in[0,C]$.

## Continuity of [[The completeness axiom#Roots|Root]]:

Let $(x_n)_{n\in\mathbb{N}}$  be a convergent sequence with $x_n\geq 0$ for all $n\in\mathbb{N}$. Then $(\sqrt{x_n})_{n\in\mathbb{N}}$ is a convergent sequence with:$$\Huge \lim_{n\to\infty}\sqrt{x_n}=\sqrt{\lim_{n\to\infty}x_n}$$
Denote $x=\lim_{n\to\infty}x_n$. Since $x_n\geq 0, x\geq 0$ by the above corollary. Distinguish the cases $x=0$ and $x>0$. So assume $x>0$, then also $\sqrt{x}>0$. $$\large \left|\sqrt{x_n}-\sqrt{x}\right|=\left|\frac{(\sqrt{x_n}-\sqrt{x})(\sqrt{x_n}+\sqrt{x})}{\sqrt{x_n}+\sqrt{x}}\right|=\left|\frac{x_n-x}{\sqrt{x_n}+\sqrt{x}}\right|\leq\frac{|x_n-x|}{\sqrt{x}}$$
By squeezing theorem, $\sqrt{x_n}-\sqrt{x}\to0$ as $n\to\infty$, then the proof is completed using COLT. Example:![[root sequence example]]
## Monotonic sequences:

Let $(x_n)_{n\in\mathbb{N}}$ be a [[EVT, MVT, boundedness and monotonicity#Monotonicity|monotonically increasing]] sequence, that is $x_m\leq x_n$ for all $m\leq n$. If $(x_n)_{n\in\mathbb{N}}$ is bounded, then it is convergent. A similar statement exists for a monotonically decreasing sequence. Consider the set of all values in the sequence:$$\Huge M=\left\{x_n\in\Re:n\in\mathbb{N}\right\}$$
$M$ must be bounded, as the sequence is bounded. Therefore we can take the [[The completeness axiom#Bounds, suprema, and infima|supremum]] of the set, which exists by the [[The completeness axiom#The axiom|completeness axiom]]. Let $\epsilon>0$, and $x=sup\,M$. Now we need $n_0\in M$:$$\Huge |x_n-x|<\epsilon,\,\forall n\geq n_0$$
Since $x>x-\epsilon$, it is less than $sup\,M$ and therefore cannot be an upper bound of $M$, so there must exists $x_{n_0}\in M$ with $x_{n_0}>x-\epsilon$. As $x_n$ is monotonically increasing:$$\Huge x-\epsilon<x_{n_0}\leq x_n\leq x+\epsilon\implies x-\epsilon< x_n\leq x+\epsilon$$
$$\Huge \implies -\epsilon<x_n-x<\epsilon$$
Which is what is required for convergence, so our candidate for the limit is the limit, that is $x=sup\,M$.

## Exponential sequences:

For every $x\in\Re$, the sequence $\left(1+\frac{x}{n}\right)^n$ is convergent, with a limit of $e^x$ as $n\to\infty$. This satisfies $e^x>0$ and $e^{-x}=\frac{1}{e^x}$. To prove this, show that the sequence is monotonically increasing for $x\geq0$ and that it is bounded above by $e^k$ for $k\in\mathbb{N}$ with $x\leq k$. This gives convergence as every bounded sequence has a limit. 

Let $x\in(-\infty,1)$, then:$$\Huge 1+x\leq e^x\leq\frac{1}{1-x}$$
Take $n\in\mathbb{N}$ with $\frac{x}{n}>-1$. By the Bernoulli inequality:$$\Huge \left(1+\frac{x}{n}\right)^n\geq 1+x$$
Now tending $n\to\infty$:$$\Huge \lim_{n\to\infty}\left(1+\frac{x}{n}\right)\geq\lim_{n\to\infty}1+x\implies e^x\geq1+x$$
Now consider:$$\Huge \frac{1}{\left(1-\frac{x}{n}\right)^n}\leq\frac{1}{1-x}$$
Again tending $n\to\infty$:$$\Huge \lim_{n\to\infty}\frac{1}{\left(1-\frac{x}{n}\right)^n}\leq\lim_{n\to\infty}\frac{1}{1-x}\implies e^x=\frac{1}{e^{-x}}\leq\frac{1}{1-x}$$
So we have the inequality as required. This lemma can be used to show that $e^{x+y}=e^x+e^y$ for any $x,y\in\Re$. This also allows the exponential function to be defined:$$\Huge\text{exp}:\Re\mapsto(0,\infty)$$
If $x<y$, then $\frac{\text{exp}(y)}{\text{exp}(x)}=\text{exp}(y-x)>1\iff\text{exp}(x)<\text{exp}(y)$, as the exponential function is strictly monotonic increasing. Let $a>0$, then there exists $x\in\Re$ with $\text{exp}(x)=a$. Consider the set:$$\Huge X=\left\{y\in\Re:\text{exp}(y)<a\right\}$$
$e^n$ is an unbounded sequence, so there is $n\in\mathbb{N}$ with $\text{exp}(n)>a$. As the exponential function is increasing, $n$ is an upper bound for $X$. Note that $e^{-n}=\left(\frac{1}{e}\right)^n\to0$ as $n\to\infty$. So this means that there exists $n\in\mathbb{N}$ with $\text{exp}(-n)<a$, so $-n\in X$. This means that $X$ is bounded above, and is non-empty, so the [[The completeness axiom|completeness axiom]] can be used. 

Now we can use the completeness and set $x=sup\,X$. Still to show that $\text{exp}(x)=a$, we need to show $e^x<a$ is not true and $e^x>a$ is not true. So first assume $\text{exp}(x)<a$, then $\frac{a}{\text{exp}(x)}>1$. Now consider $\text{exp}\left(x+\frac{1}{n}\right)=\text{exp}(x)\,\text{exp}\left(\frac{1}{n}\right)$. By the above lemma, $\text{exp}\left(\frac{1}{n}\right)\leq1+\frac{1}{n-1}$, now by Archimedes there exists $n$ with $1+\frac{1}{n-1}<\frac{a}{\text{exp}(x)}$. Now $\text{exp}\left(x+\frac{1}{n}\right)=\text{exp}(x)\,\text{exp}\left(\frac{1}{n}\right)<\text{exp}(x)\,\frac{a}{\text{exp}(x)}=a$. So we have $\text{exp}\left(x+\frac{1}{n}\right)<a$, so $x+\frac{1}{n}\in X$, contradicting $x=sup\,X$. So assuming $\text{exp}(x)<a$ leads to a contradiction, so it must not be true. A similar method can be used for $\text{exp}(x)>a$, leading to the conclusion that for $a>0$, there exists $x\in\Re$ with $\text{exp}(x)=a$, making the exponential function bijective, so the folllowing inverse is defined: 

## Logarithmic sequences:

Consider the inverse to the exponential function, the logarithm:$$\Huge log:(0,\infty)\mapsto\Re,\,\,log(\text{exp}(x))=x$$
Let $a>0$ and $x\in\Re$, define the following:$$\Huge a^x=\text{exp}(x\,log(a))$$
If $a\neq 1$, then:
$$\Huge log_a(x)=\frac{log(x)}{log(a)}$$
Now let $a,b>0$ with $b\neq 1$ and $x,y\in\Re$, then the logarithm has the following properties:
>$a^{x+y}=a^x\,a^y$
>$(a^x)^y=a^{xy}$
>$log_b(xy)=log_b(x)+log_b(y)$, for $x,y>0$
>$log_b(x^y)-y\,log(x)$, for $x>0$

Using a similar lemma from the exponential function, we have:$$\Huge \frac{x-1}{x}\leq log(x)\leq x-1$$
Now we arrive at our final comparison between functions, powers beat logarithms. That is to say, for $k\in\mathbb{N}$:$$\Huge \lim_{n\to\infty}\frac{n^k}{e^n}=0$$
$$\Huge e^n\geq\left(1+\frac{n}{k+1}\right)^{k+1}\geq\frac{n^{k+1}}{(k+1)^{k+1}}$$
Here, the rightmost term is the final term in the binomial expansion of the middle term. Now reverse the inequality and multiply by $n^k$:$$\Huge \frac{n^k}{e^n}\leq\frac{n^k(k+1)^{k+1}}{n^{k+1}}=\frac{(k+1)^{k+1}}{n}$$
Since $(k+1)^{k+1}$ is constant, the limit as $n\to\infty$ of the rightmost term is $0$. We also have $\frac{n^k}{e^n}>0$ as both numerator and denominator are $>0$, so by the squeezing theorem we get the required result. 

We also have $log(n)=k\,log(n^{\frac{1}{k}})\leq\epsilon\,n^{\frac{1}{n}}$. Given large enough $n$ and since $\epsilon>0$ is arbitrary, we also get:$$\Huge \lim_{n\to\infty}\frac{log(n)}{\sqrt[k]{n}}=0$$

# The Bolzano-Weierstrass Theorem:

Let $(x_n)_{n\in\mathbb{N}}$ be a sequence. A subsequence of $(x_n)_{n\in\mathbb{N}}$ is a sequence $(x_{n_j})_{j\in\mathbb{N}}$ with $n_1<n_2<\dots$, for example $(x_{2j})_{j\in\mathbb{N}}$ would be a subsequence of $(x_n)_{n\in\mathbb{N}}$, with only the even indexes.

Given a convergent sequence $(x_n)_{n\in\mathbb{N}}$ with a limit $x_n\to x$ as $n\to\infty$. Then every subsequence $(x_{n_j})_{j\in\mathbb{N}}$ is also convergent with:$$\Huge \lim_{j\to\infty}x_{n_j}=x$$
The Bolzano-Weierstrass theorem dictates that for a bounded sequence $(x_n)_{n\in\mathbb{N}}$, there exists a convergent subsequence. This is proven using the following lemma:

Every real sequence $(x_n)_{n\in\mathbb{N}}$ contains a subsequence that is either increasing or decreasing. Let $(x_n)_{n\in\mathbb{N}}$ be a sequence. $x_{n_0}$ is a peak element if $x_{n_0}\geq x_n$ for all $n>n_0$, then $n_0$ is called the peak index.
> If there are infinitely many peak indices, $n_0<n_1<n_2<\dots$, which forms a subsequence with $x_{n_0}\geq x_{n_1}\geq x_{n_2}\geq\dots$, which is a monotonically decreasing subsequence.
> 	If there are finitely many peak indices, there must exists an $n_0$ such that $n_0$ is greater than all other peak indices. Then there must also exist $n_1=n_0+1>n_0$ that is not a peak index. Since $n_1$ is not a peak index, there exists $n_2$ with $x_{n_1}<x_{n_2}$ and $n_2>n_1$. $n_2$ is also not a peak index, so there exists $n_3>n_2$ such that $x_{n_2}<x_{n_3}$ and so on. Using these indices, a monotonically increasing subsequence can be formed.

Now let $(x_n)_{n\in\mathbb{N}}$ be a bounded sequence. By the above lemma, there exists a subsequence $(x_{n_j})_{j\in\mathbb{N}}$ that is either monotonically increasing or decreasing. Since the sequence is bounded, we have $|x_n|\leq C$ for all $n\in\mathbb{N}$. The subsequence must also be bounded by $C$. Since the subsequence is bounded and either monotonically increasing or decreasing, it must be convergent as it is a [[Sequences#Monotonic sequences|monotonic sequence]].

# Lim inf and Lim sup:

Given a bounded sequence $(x_n)_{n\in\mathbb{N}}$, two sequences are defined, $(\overline x_n)_{n\in\mathbb{N}}$ and $(\underline x_n)_{n\in\mathbb{N}}$:$$\Huge \overline x_n=sup\{x_m:m\geq n\}$$$$\Huge \underline x_n=inf\{x_m:m\geq n\}$$
Let $(x_n)_{n\in\mathbb{N}}$ be a bounded sequence, then $(\overline x_n)_{n\in\mathbb{N}}$ is monotonically decreasing and bounded, and $(\underline x_n)_{n\in\mathbb{N}}$ is monotonically increasing and bounded. So they both have limits, given by:$$\Huge \lim_{n\to\infty}\underline x_n\leq\lim_{n\to\infty}\overline x_n$$
This is proven as follows:
> Since $(x_n)_{n\in\mathbb{N}}$ is bounded, there exists $c<C$ with $c\leq x_n\leq X$