
# Contrapositive:

The general technique for a contrapositive proof is summarised as follows. Let $A,B$ be statements. The statement "If $A$ then $B$" is equivalent to "If not $B$ then not $A$". This can be shown through a truth table:

| $A$ | $B$ | $A\implies B$ | not $A$ | not $B$ | not $B\implies$ not $A$ |
| --- | --- | ------------- | ------- | ------- | ----------------------- |
| T   | T   | T             | F       | F       | T                       |
| T   | F   | F             | T       | F       | F                       |
| F   | T   | T             | F       | T       | T                       |
| F   | F   | T             | T       | T       | T                        |
It is obvious that column 3, $A\implies B$, is logically equivalent to column 6, not $B\implies$ not $A$.

# Indirect:

The technique for an indirect proof involves showing that for any statement $A$, not $A$ is false, so $A$ must be true, as $not(not(A))$ is $A$.

# Negations:

"For all $x$ we have $A(x)$" is negated by "There exists $x$ with not $A(x)$", "There exists $x$ with $B(x)$" is negated by "For all $x$ we have not $B(x)$". In general, For all negates There exists.

Let $A,B$ be statements. The negation of $A\implies B$ is $A$ and not $B$.

# Mathematical induction:

Assume we are given a statement $A(n)$ for every $n\in\mathbb{N}$. To show that $A(n)$ is true for all $n\in\mathbb{N}$ the following need to be shown:
> $A(1)$ is true
> For every $n\in\mathbb{N}$, $A(n)\implies A(n+1)$

# Examples:

Let $a_1,\dots,a_n$ be $n$ real numbers. The sum of these numbers is denoted as $\sum_{i=1}^n=a_1+\dots+a_n$. Their product is denoted as $\Pi_{i=1}^n=a_1\dots a_n$. For $n\in\mathbb{N}$, the factorial of $n$ is denoted as $\Pi_{i=1}^ni=n!$. Note that $0!$ is defined to be 1.

## Binomial coefficient and theorem:

For $n,k\in\mathbb{N}_0$, given $k\leq n$, the binomial coefficient is defined as:
$$\Huge \begin{pmatrix}n\\k\end{pmatrix}=\frac{n!}{(n-k)!n!}$$
The binomial theorem states that for $a,b\in\Re$ and $n\in\mathbb{N}$:
$$\Huge (a+b)^n=\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}a^{n-k}b^k=a^n+na^{n-1}b+\dots+nab^{n-1}+b^n$$

The $n=1$ case is obvious:$$\Huge (a+b)^1=a+b=\sum_{k=0}^1\begin{pmatrix}1\\k\end{pmatrix}a^{1-k}b^k=a+b$$
Now for the $n+1$ case:
$$\large (a+b)^{n+1}=(a+b)(a+b)^n,\,\,\text{using the assumed hypothesis},\,\,(a+b)\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}a^{n-k}b^k$$$$\implies \sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}a^{(n+1)-k}b^k+\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}a^{n-k}b^{k+1}=\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}a^{(n+1)-k}b^k+\sum_{k=1}^{n+1}\begin{pmatrix}n\\k-1\end{pmatrix}a^{(n+1)-k}b^{k}$$
$$\implies a^{n+1}+\sum_{k=1}^n\begin{pmatrix}n\\k\end{pmatrix}a^{(n+1)-k}b^k+\sum_{k=1}^N\begin{pmatrix}n\\k-1\end{pmatrix}a^{(n+1)-k}b^k+b^{n+1}$$
$$\small \implies a^{n+1}+\sum_{k=1}^n\left(\begin{pmatrix}n\\k\end{pmatrix}a^{(n+1)-k}b^k+\begin{pmatrix}n\\k-1\end{pmatrix}a^{(n+1)-k}b^k\right)+b^{n+1}=a^{n+1}+\sum_{k=1}^n\left(\begin{pmatrix}n\\k\end{pmatrix}+\begin{pmatrix}n\\k-1\end{pmatrix}\right)a^{(n+1)-k}b^k+b^{n+1}$$
$$\implies a^{n+1}+\sum_{k=1}^n\begin{pmatrix}n+1\\k\end{pmatrix}a^{(n+1)-k}b^k+b^{n+1}=\sum_{k=0}^{n+1}\begin{pmatrix}(n+1)\\k\end{pmatrix}a^{(n+1)-k}b^k$$

## Bernoulli inequality:

The Bernoulli inequality states for $x\geq -1$ and $n\in\mathbb{N}$:$$\Huge (1+x)^n\geq1+nx$$
![[bernoulli inequality proof]]