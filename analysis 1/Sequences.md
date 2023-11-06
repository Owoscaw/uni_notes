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
By squeezing theorem, $\sqrt{x_n}-\sqrt{x}\to0$ as $n\to\infty$, then the proof is completed using COLT. Example:![[Sequences .excalidraw]]