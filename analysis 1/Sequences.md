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
> Take $x_n=(-1)^n$

