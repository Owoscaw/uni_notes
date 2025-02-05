
# Topologies:

For any set $X$ we write $\wp(X)=\{A:A\subseteq X\}$ for the power set of $X$, that is, for the set whose elements are all the subsets of $X$.

Let $X$ be a set. A topology on $X$ is a subset $\tau\subseteq\wp(X)$ that satisfies the following:
> $\emptyset,X\subseteq\tau$
> If $U_i\in\tau$ for all $i\in I$, then $\bigcup_{i\in I}U_i\in\tau$
> If $U_1,U_2\in\tau$ then $U_1\cap U_2\in\tau$

It can be shown that the last statement is equivalent to:$$\Huge U_1,\dots,U_n\in\tau\implies\bigcap_{i=1}^nU_i\in\tau$$
The pair $(X,\tau)$ is then called a topological space. The elements of $\tau$ are called open subsets of $X$. A subset $A\subseteq X$ is called closed if its complement $X\setminus A$ is open. Examples:
>Let $(M,d)$ be a [[Metrics|metric space]], and $\tau_d$ the collection of open sets. Then $(M,\tau_d)$ is a topological space. We say that the metric $d$ induces the topology $\tau_d$.
>Let $X$ be any set and $\tau=\wp(X)$. This is called the discrete topology on $X$
>Let $X$ be any set and $\tau=\{\emptyset, X\}$. This is called the indiscrete topology on $X$
>Let $X=\{0,1,2,\dots\}$ and $\tau=\{\emptyset\}\cup\{U\subseteq X:(X\setminus U)\text{ is finite}\}$

One can check the first three topologies hold. We show the fourth. Since $X\setminus X=\emptyset$, which is finite, so we have $X\in\tau$ and $\emptyset\in\tau$. Either all $U_i=\emptyset$, in which case $\bigcup_{i\in I}U_i=\emptyset$ or some $U_{i_0}\neq\emptyset$, in which case:$$\Huge X\setminus\bigcup_{i\in I}U_i=\bigcap_{i\in I}(X\setminus U_i)\subseteq X\setminus U_{i_0}$$Which is a finite set, so the union is open and therefore in $\tau$. For the final property, if either $U_1$ or $U_2$ are $\emptyset$ then so is their intersection. Otherwise $X\setminus(U_1\cap U_2)=(X\setminus U_1)\cup(X\setminus U_2)$ and the union of two finite sets is finite, so $(U_1\cap U_2)$ is open and we see that this is indeed a topological space as required.

Let $X,\tau$ be a topological space. Then $X,\emptyset$ are closed. Furthermore, arbitrary intersections of closed sets are closed, and finite unions of closed sets are closed. The proofs are trivial.

We ask how we should define a topological subspace. That is, given $(X,\tau)$, if $A\subseteq X$ we ask how to set up a topological space $(A,\tau_A)$. For any set $B\subseteq A$, if $B\in\tau$ we would want $B\in\tau_A$. Also we must have $A\in\tau_A$ even if $A\notin\tau$. The solution then comes from saying that $B\in\tau_A$ if and only if $B=A\cap U$ for some $U\in\tau$.

## Topological subspaces:
Let $(X,\tau)$ be a topological space, $A\subset X$, then$$\Huge \tau_A=\{A\cap U:U\in\tau\}$$is a topology, called the induced/subspace topology on $A$. This is indeed a topology since:
> $\emptyset=A\cap\emptyset\in\tau_A$ and $A=A\cap X\in\tau_A$
> Since $\bigcup_{i\in I}U_i\in\tau$ we know $\bigcup_{i\in I}(A\cap U_i)=A\cap\bigcup_{i\in I}U_i\in\tau_A$
> $(A\cap U_1)\cap(A\cap U_2)=A\cap(U_1\cap U_2)\in\tau_A$

We propose that the metrics $d_p$ for $p\in[1,\infty)$ as well as $d_\infty$ all induce the same topology on $\Re^n$. This is known as the standard topology on $\Re^n$

## Hausdorff topologies:
A topological space $X$ is called Hausdorff if whenever $x,y\in X$ with $x\neq y$ there exists open sets $U,V\subseteq X$ with $x\in U,y\in V$ and $U\cap V=\emptyset$.