
Let $A$ and $B$ be subsets of $X$. We call $A$ and $B$ complementary subsets of $X$ if $A\cup B=X$ and $A\cup B=\emptyset$. A separation of a [[Topological spaces#Topologies|topological space]] $X$ is a pair of complementary subsets of $X$ which are both open and non-empty. Take for example the following, which are complementary subsets of $\Re$:
> $A=(-\infty,3), B=[3,\infty)$
> $A=\bigcap_{k\in\mathbb{Z}}[2k,2k+1],B=\bigcap_{k\in\mathbb{Z}}(2k+1,2k)$
> $A=\Re,B=\emptyset$

However none of these are separations, as the first two have a non-open set and the last has an empty set.

A topological space $X$ is called connected if there is no separation in $X$:
> $\mathbb{Q}$ is not connected as $L=\mathbb{Q}\cap(-\infty,\sqrt{2}),M=\mathbb{Q}\cap(\sqrt{2},\infty)$ are both open in $\mathbb{Q}$ and non-empty. Since $L\cup M=\mathbb{Q}$ and $L\cap M=\emptyset$, $L$ and $M$ form a separation of $\mathbb{Q}$ and so it is not connected.
> $\Re$ is connected. We show this by contradiction, so assume that $U,V$ form a separation of $\Re$. Now let $x\in U,y\in V$ and assume $x<y$ WLOG. We define:$$\Huge A=\{a\in[x,\infty):[x,a]\subseteq U\}$$We see that both $x\in A$ and $a\in A$ implies $a<y$, so $y$ is an upper bound for this set. Therefore $A$ has a supremum that we label $s=\sup A$. We consider the two possibilities $s\in U$ or $s\in V$:
> > If $s\in U$ then as $U$ is open there exists some $\epsilon>0$ such that $(s-\epsilon,s+\epsilon)\subseteq U$. $s-\epsilon$ is by definition not an upper bound so there must exist some $a>s-\epsilon$ that belongs to $A$. That is, $[x,a]\subseteq U$. Also $(s-\epsilon,s+\epsilon/2]\subseteq(s-\epsilon,s+\epsilon)\subseteq U$, the union $[x,s+\epsilon/2]\subseteq U$ and therefore $s+\epsilon/2\in A$ and $s$ cannot be an upper bound for $A$.
> > If $s\in V$ then as $V$ is open there exists some $\epsilon>0$ such that $(s-\epsilon,s+\epsilon)\subseteq V=X\setminus U$. Therefore for $b\in(s-\epsilon,s+\epsilon),b\notin U$ which means that $[x,b]\not\subseteq U$ and $b\notin A$. Therefore $s-\epsilon$ is the upper bound for $A$ and $s$ is not the supremum.
> Both cases lead to a contradiction, so $\Re$ is connected.


If $h:X\rightarrow Y$ is continuous and $X$ is connected then $h(X)\subseteq Y$ is also connected, that is to say continuity preserves connectedness. We prove this by contradiction, so assume $h(X)$ has a separation $U,V$. We claim that $h^{-1}(U),h^{-1}(V)$ then form a separation of $X$. We have that $U\cup V=h(X)$ so we can apply $h^{-1}$ to both sides to get $h^{-1}(U)\cup h^{-1}(V)=h^{-1}(h(X))=X$. We have that $U\cap V=\emptyset$, so $h^{-1}(U)\cap h^{-1}(V)=h^{-1}(\emptyset)=\emptyset$. We must now show that $h^{-1}(U),h^{-1}(V)$ are open in $X$. Since $h(X)$ has the subspace topology from $Y$, $U$ and $V$ being open in $h(X)$ is equivalent to $U=U'\cap h(X)$ and $V=V'\cap h(X)$ for some open $U',V'$ that are open in $Y$. Then:$$\Huge\begin{align}
h^{-1}(U)&=h^{-1}(U'\cap h(X))=h^{-1}(U')\\
h^{-1}(V)&=h^{-1}(V'\cap h(X))=h^{-1}(V')
	\end{align}$$And since $h$ is continuous, both of these sets are open in $X$. This forms the separation on $X$, which is a contradiction. Therefore there must not be a separation in $h(X)$.

This has a corollary that states for a homeomorphism $h:X\rightarrow Y$ with $X$ connected, $Y$ is connected. This is simply an application of the above with $h(X)=Y$.

If $X$ is a topological space then we call a subset $A\subseteq X$ clopen if it is both closed and open.

Let $X$ be a topological space, then the following form a tautology:
> $X$ is connected
> The only clopen subsets of $X$ are $\emptyset, X$
> There is no continuous surjective function from $X$ to a discrete space with more than one point

Proofs:
1. The first and second statements are equivalent as if there is a clopen subset $A\subseteq X$ with $A\neq\emptyset,X$ then $A$ and $X\setminus A$ form a separation. Also if $U,V$ is a separation of $X$ then $U,V$ are both clopen and non-empty. Therefore the first and second statements are equivalent.
2. The first and third statements are equivalent as for connected $X$ and continuous, surjective $f:X\rightarrow Y$ where $Y$ has at least two elements and the discrete topology it is trivial that $Y$ is not connected, however by continuity preserves connectedness $Y$ is connected. This is a contradiction, so no such $f$ exists. Suppose there exists a separation $U,V$. Let $Y$ be the set $\{0,1\}$ with the discrete topology and define:$$\Huge f(x)=\begin{cases}0&x\in U\\1&x\in V\end{cases}$$then $f$ is surjective and continuous