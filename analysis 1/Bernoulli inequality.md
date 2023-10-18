
Let $a_1,\dots,a_n$ be $n$ real numbers. The sum of these numbers is denoted as $\sum_{i=1}^n=a_1+\dots+a_n$. Their product is denoted as $\Pi_{i=1}^n=a_1\dots a_n$. For $n\in\mathbb{N}$, the factorial of $n$ is denoted as $\Pi_{i=1}^ni=n!$. Note that $0!$ is defined to be 1.

# Binomial coefficient and theorem:

For $n,k\in\mathbb{N}_0$, given $k\leq n$, the binomial coefficient is defined as:
$$\Huge \begin{pmatrix}n\\k\end{pmatrix}=\frac{n!}{(n-k)!n!}$$
The binomial theorem states that for $a,b\in\Re$ and $n\in\mathbb{N}$:
$$\Huge (a+b)^n=\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}a^{n-k}b^k=a^n+na^{n-1}b+\dots+nab^{n-1}+b^n$$
## Proof by [[Proof techniques#Mathematical induction|induction]]:

The $n=1$ case is obvious:$$\Huge (a+b)^1=a+b=\sum_{k=0}^1\begin{pmatrix}1\\k\end{pmatrix}a^{1-k}b^k=a+b$$
Now for the $n+1$ case:
$$\large (a+b)^{n+1}=(a+b)(a+b)^n,\,\,\text{using the assumed hypothesis},\,\,(a+b)\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}a^{n-k}b^k$$$$\implies \sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}a^{(n+1)-k}b^k+\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}a^{n-k}b^{k+1}=\sum_{k=0}^n\begin{pmatrix}n\\k\end{pmatrix}a^{(n+1)-k}b^k+\sum_{k=1}^{n+1}\begin{pmatrix}n\\k-1\end{pmatrix}a^{(n+1)-k}b^{k}$$
$$\implies a^{n+1}+\sum_{k=1}^n\begin{pmatrix}n\\k\end{pmatrix}a^{(n+1)-k}b^k+\sum_{k=1}^N\begin{pmatrix}n\\k-1\end{pmatrix}a^{(n+1)-k}b^k+b^{n+1}$$
$$\small \implies a^{n+1}+\sum_{k=1}^n\left(\begin{pmatrix}n\\k\end{pmatrix}a^{(n+1)-k}b^k+\begin{pmatrix}n\\k-1\end{pmatrix}a^{(n+1)-k}b^k\right)+b^{n+1}=a^{n+1}+\sum_{k=1}^n\left(\begin{pmatrix}n\\k\end{pmatrix}+\begin{pmatrix}n\\k-1\end{pmatrix}\right)a^{(n+1)-k}b^k+b^{n+1}$$
$$\implies a^{n+1}+\sum_{k=1}^n\begin{pmatrix}n+1\\k\end{pmatrix}a^{(n+1)-k}b^k+b^{n+1}=\sum_{k=0}^{n+1}\begin{pmatrix}(n+1)\\k\end{pmatrix}a^{(n+1)-k}b^k$$

# Bernoulli inequality:

The Bernoulli inequality states for $x\geq -1$ and $n\in\mathbb{N}$:$$\Huge (1+x)^n\geq1+nx$$
## Proof by induction:
![[Bernoulli inequality .excalidraw]]