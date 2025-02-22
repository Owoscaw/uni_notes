
# Limit points, interiors, and closures:

Let $X$ be a [[Topological spaces#Topologies|topological space]] and $x\in X,A\subseteq X$:
> A neighbourhood of $x$ is a set $N\subseteq X$ with open subset $U$ such that $x\in U\subseteq N$
> A point $x\in X$ is called a limit point of $A$ if every neighbourhood $N$ of $x$ satisfies:$$\Huge (N\setminus\{x\})\cap A\neq\emptyset$$

Note that a point in $A$ may or may not be a limit point of $A$, and a limit point of $A$ may or may not be in $A$. If $x$ is a limit point of $A$, then however small a neighbourhood around $x$, it must include some other point of $A$.

The point $x$ is not a limit point of $A$ if and only if there is some neighbourhood $N$ of $x$ with:$$\Huge A\cap N=\begin{cases}\{x\}&x\in A \\
\emptyset&x\notin A\end{cases}$$
Take for example $X=\Re$. Then $0\in X,(-1,1),(-2,3],$ and $[-4,5]$ are all neighbourhoods of $0$, in each case we take the open set $U=(-1,1)$.

If $U\subseteq X$ is open, then $U$ is a neighbourhood of every $x\in U$.

Let $A=\{1/n\in\Re:n\in\mathbb{Z}\setminus\{0\}\}$. Then $A$ has exactly one limit point $0$ and $0\notin A$. To check that no other point note that for given $x\neq0$, if $x\notin A$ we can find a small enough interval $(x-\epsilon,x+\epsilon)$ so that no other point of $A$ is in the interval. Each case shows that $x$ is not a limit point.

We can now define the interior and the closure of a set. First note that if for $A,B$ we have $A\subseteq B$ we can say that $A$ is smaller than $B$ or $B$ is larger than $A$. Let $X$ be a topological space with $A\subseteq X$. The interior of $A$, $A^\circ$ is the largest open set contained in $A$.  The closure of $A$, $\bar A$ is the smallest closed set containing $A$. Formally:$$\Huge A^\circ=\bigcup_{\text{open }U\subseteq A}U,\,\,\bar A=\bigcap_{\text{closed }A\subseteq C}C$$A subset $A\subseteq X$ is called dense if $\bar A=X$.

We then have the following results:
> $\overline{(X\setminus A)}=X\setminus A^\circ$
> $\bar A=X\setminus(A\setminus A^\circ)$ or $X\setminus\bar A=(X\setminus A)^\circ$, the complement of the closure of a set if the interior of its complement

To prove the first result, we know $\overline{(X\setminus A)}$ is closed and contains $X\setminus A$. Therefore its complement is an open set and lies within $X\setminus(X\setminus A)=A$. Also, $\overline{(X\setminus A)}$ is the smallest possible such closed set, so its complement must be the largest possible such open set, that is $A^\circ$. Replacing $A$ by $X\setminus A$ then gives the second result.

For example, let $\mathbb{Q}\subseteq\Re$ with the standard topology. Then $\mathbb{Q}^\circ=\emptyset$ and $\overline{\mathbb{Q}}=\Re$. To prove this, note that any non-empty subset of $\Re$ contains the open interval $(a-\epsilon,a+\epsilon)$ around each point $a\in\Re$. That is, any non-empty subset of $\Re$ contains both rational and irrational numbers. The interior of $\mathbb{Q}$ must then be an open set within $\mathbb{Q}$, which is only satisfied by $\emptyset$. The interior of $\Re\setminus\mathbb{Q}$ must then be an open set within $\Re\setminus\mathbb{Q}$ and must therefore be empty. Then by the above $\overline{\mathbb{Q}}=\Re\setminus(\Re\setminus\mathbb{Q})^\circ=\Re\setminus\emptyset=\Re$, therefore $\mathbb{Q}$ is dense in $\Re$.

Let $A\subseteq X$. Then $\bar A=A\cup\{\text{limit points of }A\}$. We prove this by showing two inclusions:
> We show that the RHS subsets the LHS by showing that $x\notin\text{RHS}\implies x\notin\text{LHS}$. Let $x\notin\bar A$, then $U=X\setminus\bar A$ is a neighbourhood of $x$. Note that $U\cap A\subseteq U\cap\bar A=\emptyset$, so $x$ is not a limit point of $A$. Clearly $x\notin A\subseteq\bar A$ so $x\notin\text{RHS}$, we have $A\cup\{\text{limit points of }A\}\subseteq\bar A$.
> We show the other subset in the same manner. Let $x\notin A\cup\{\text{limit points of }A\}$. Then $x$ has a neighbourhood $N$ with $N\cap A=\emptyset$. By definition this contains an open subset $U$ such that $x\in U\subseteq N$. Therefore $U\cap A\subseteq N\cap A=\emptyset$ and $X\setminus U$ is a closed set containing $A$. Recall that $\bar A$ is the intersection of all such closed sets, so $\bar A\subseteq X\setminus U$. Since $x\notin X\setminus U$ it follows that $x\notin\bar A$.

We extend this notion to functions. Let $f:X\rightarrow Y$ be a function between topological spaces. Then the following are equivalent:
> $f$ is continuous
> $f(\bar A)\subseteq\overline{f(A)}$ for every subset $A\subseteq X$
> $\overline{f^{-1}(V)}\subseteq f^{-1}(\bar V)$ for every subset $V\subseteq Y$

The latter two statements say that a larger set may be found by taking the closure in $Y$ rather than in $X$. Proofs:
>Continuity implies the second statement since $\overline{f(A)}$ is a closed set in $Y$ then $f^{-1}(\overline{f(A)})$ but also:$$\Huge A\subseteq f^{-1}(f(A))\subseteq f^{-1}(\overline{f(A)})$$As it is a closed set containing $A$, we have $\bar A\subseteq f^{-1}(\overline{f(A)})$. Then applying $f$ to both sides gives:$$\Huge f(\bar A)\subseteq f(f^{-1}(\overline{f(A)}))\subseteq\overline{f(A)}$$So we have that $f$ is continuous implies the second statement.
>For any $V\subseteq Y$ we have $f^{-1}(V)\subseteq X$. The second statement implies:$$\Huge f(\overline{f^{-1}(V)})\subseteq\overline{f(f^{-1}(V))}\subseteq\bar V$$Now we apply $f^{-1}$ to both sides to give:$$\Huge \overline{f^{-1}(V)}\subseteq f^{-1}(f(\overline{f^{-1}(V)}))\subseteq f^{-1}(\bar V)$$as required.
>Let $C\subseteq Y$ be closed, then $\bar C=C$ and we have:$$\Huge f^{-1}(C)\subseteq\overline{f^{-1}(C)}\subseteq f^{-1}(\bar C)=f^{-1}(C)$$which shows that $f^{-1}(C)$ is closed as required.

## The Dirichlet prime number theorem:
