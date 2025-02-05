
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

## Hausdorff space:
A topological space $X$ is called Hausdorff if whenever $x,y\in X$ with $x\neq y$ there exists open sets $U,V\subseteq X$ with $x\in U,y\in V$ and $U\cap V=\emptyset$.

Let $(M,d)$ be a metric space, then $M$ is a Hausdorff space. The proof is trivial, however there do exist some topological spaces that are not Hausdorff spaces.

For example, let $X$ be a set with more than one element with the indiscrete topology. Then $X$ is not a Hausdorff space. Here we have $\tau=\{\emptyset, X\}$ and we have $x,y\in X$ with $x\neq y$. The only open set containing $x$ is $X$ and the same is true for $y$, however $X\cap X=X\neq\emptyset$, so the space is not Hausdorff.

## Furstenberg's  topology on $\mathbb{Z}$:
A subset $U\subseteq\mathbb{Z}$ is defined to be open if for every $a\in U$ there exists a non-zero $d\in\mathbb{Z}$ with $a+d\mathbb{Z}\subseteq U$. In this topology, the role of an open ball is defined as a set:$$\Huge a+d\mathbb{Z}=\{\dots,a-2d,a-d,a,a+d,a+2d,\dots\}$$We first show that this is indeed a topology:
> $\emptyset$ is trivially open and $\mathbb{Z}$ is open because for any $a\in\mathbb{Z}$ we can pick some $d$ and have $a\in a+d\mathbb{Z}\subseteq\mathbb{Z}$
> Consider open sets $U_i,i\in\mathbb{I}$. If $a\in\bigcup_{i\in I}U_i$, then $a\in U_j$ for some $j\in I$, therefore there exists some $d$ such that $a+d\mathbb{Z}\subseteq U_j\subseteq\bigcup_{i\in I}U_i$, making the arbitrary union open
> If $a\in U_1\cap U_2$ then there are $d_1,d_2$ such that $a+d_1\mathbb{Z}\subseteq U_1$ and $a+d_2\mathbb{Z}\subseteq U_2$ but then:$$\Huge a+d_1d_2\mathbb{Z}\subseteq a+d_1\mathbb{Z}\subseteq U_1,\,\,a+d_1d_2\mathbb{Z}\subseteq a+d_2\mathbb{Z}\subseteq U_2$$So we have $a+d_1d_2\mathbb{Z}\subseteq U_1\cap U_2$ is open

This shows that the topology is valid, we now show that it is also Hausdorff. To do this, take any $a,b\in\mathbb{Z}$ with $a\neq b$. We then aim to find two open sets that separate them. Let $U=a+2(b-a)\mathbb{Z}$ and $V=b+2(b-a)\mathbb{Z}$. We aim to show that $U,V$ are disjoint. Suppose that they are not disjoint, then if $z\in U\cap V\neq\emptyset$ then $z=a+2(b-a)n=b+2(b-a)m$ for some $m\neq n\in\mathbb{Z}$. This implies that $b-a=2(b-a)(n-m)$, meaning that $n-m=\frac{1}{2}$, which is impossible as they are integers. Therefore the assumption that $U,V$ are not disjoint is false, and we have that $U\cap V=\emptyset$, making the topology Hausdorff as required.

# Continuity:

We can generalise the idea of [[Continuity|continuity]] to topological spaces. Let $X,Y$ be topological spaces then:
> A function $f:X\rightarrow Y$ is called continuous if for every open subset $V\subset Y$, the inverse image $f^{-1}(V)$ is open in $X$.
> Let $a\in X$. The function $f$ is called continuous at $a$ if for every open set $V\subseteq Y$ with $f(a)\in V$, there is an open set $U\subseteq X$ with $a\in U\subseteq f^{-1}(V)$.

A function $f:X\rightarrow Y$ is continuous if and only if it is continuous at all points in $X$. The first direction of implication is trivial, let $a\in X$ and $V$ be open. $f(a)\in V\subseteq Y$, we assume that the inverse image is open in $X$ so we can take $U=f^{-1}(V)$ for the second requirement. Let $V\subseteq Y$ be open, and consider any $a\in f^{-1}(V)$, so $f(a)\in V$. We assume the existence of an open set $U_a$ with $a\in U_a\subseteq f^{-1}(V)\subseteq X$. We then notice that:$$\Huge f^{-1}(V)=\bigcup_{a\in f^{-1}(V)}\{a\}\subseteq\bigcup_{a\in f^{-1}(V)}U_a\subseteq f^{-1}(V)$$So these inclusions must be equalities, that is $f^{-1}(V)=\bigcup_{a\in f^{-1}(V)}U_a$ is a finite union of open sets, and must be open. Therefore this notion of continuity is consistent with our definition.

Let $X$ be a topological space and $A\subseteq X$. The inclusion $i:A\rightarrow X$ is continuous, if $A$ is given the subspace topology. To prove this statement, let $U\subset X$ be an open set. Then $i^{-1}(U)=U\cap A$, which is open in the subspace topology on $A$ as required.

We can also define continuity with closed sets as follows. Let $f:X\rightarrow Y$ be a function between topological spaces $X$ and $Y$. Then $f$ is continuous if and only if $f^{-1}(A)$ is closed for every $A\subseteq Y$ closed. The proof is trivial and relies on the fact that for any set $A\subseteq Y$ we have $f^{-1}(A)=X\setminus f^{-1}(Y\setminus A)$.

## n-sphere:
We define the $n$-sphere as:$$\Huge S^n=\{(x_1,\dots,x_{n+1})\in\Re^{n+1}:x_1^2+\dots+x_{n+1}^2=1\}$$
In the standard topology on $\Re^{n+1}$, the $n$-sphere is a closed subset. The function defined by $f:\Re^{n+1}\rightarrow\Re^n$ with $f(x_1,\dots,x_{n+1})=x_1^2+\dots+x_{n+1}^2$ is continuous and the set $\{1\}$ is closed. Since $S^n=f^{-1}(\{1\})$, the pre-image of a closed set, it must be closed.

Note that we can also work with matrices. For $n\in\mathbb{Z}$ we have that $M_{n,n}(\Re)\cong\Re^{n^2}$. Using the standard topology on this space, we can consider the general linear group $GL_n(\Re)$, the special linear group $SL_n(\Re)$, the orthogonal group $O(n)$, and the special orthogonal group $SO(n)$ as sets in the topological space $M_{n,n}(\Re)$:
> $GL_n(\Re)=\{A\in M_{n,n}(\Re):\det(A)\neq0\}$ is open in $M_{n,n}(\Re)$
> $SL_n(\Re)=\{A\in M_{n,n}(\Re):\det(A)=1\}$ is closed in $M_{n,n}(\Re)$

These sets are defined using the function $\det:M_{n,n}(\Re)\rightarrow\Re$. For a matrix $A=(a_{ij})$ we have:$$\Huge \det(A):=\sum_{\sigma\in\text{Sym}(n)}\left(\text{sgn}(\sigma)\prod_{i=1}^na_{i\sigma(i)}\right)$$Which is a polynomial in terms of the matrix entries $a_{ij}$, and so continuous. Now since $GL_n(\Re)=\det^{-1}(\Re\setminus\{0\})=\det^{-1}((-\infty,0)\cup(0,\infty))$ is the pre-image of an open set, it is open. Since $SL_n(\Re)=\det^{-1}(\{1\})$ is the pre-image of a closed set, it is closed.

## Homeomorphisms:
Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis Penis 

Let $X,Y$ be topological spaces. A continuous function $h:X\rightarrow Y$ is called a homeomorphism if $h$ is bijective and $h^{-1}$ is continuous. In which case, $X,Y$ are called homeomorphic, written as $X\cong Y$.

Note that $h$ also induces a bijection between $\tau_X$ and $\tau_Y$: If $U\subseteq Y$ is open, then since $h$ is continuous we have $h^{-1}(U)$ is open in $X$. Also if $U\subseteq X$ is open, then since $h^{-1}$ is continuous we have $(h^{-1})^{-1}(U)=h(U)$ is open in $Y$. Moreover, this bijection commutes with unions and intersections. In this sense, homeomorphisms are maps that are topologically preserving.

For example, the interval $(0,1)$ is homeomorphic to $\Re$. We know that the function $f:(\frac{-\pi}{2},\frac{\pi}{2})\rightarrow(-\infty,\infty)$ given by $f(x)=\tan x$ is bijective and continuous, as well as its inverse $f^{-1}(x)=\arctan x$. So we define $g:(0,1)\rightarrow(-\frac{\pi}{2},\frac{\pi}{2})$ as $g(x)=\pi x-\frac{\pi}{2}$, which is a linear map (and therefore continuous, bijective). Then $f\circ g$ is the homeomorphism between $(0,1)$ and $\Re$.

## Furstenberg's proof of infinite primes:
Note the following about the Furstenberg toplogy:
> Since $a+d\mathbb{Z}$ is infinite, and open set is infinite, therefore any set with finite complement cannot be closed.
> For fixed $d$, the sets $d\mathbb{Z},1+d\mathbb{Z},\dots,(d-1)+d\mathbb{Z}$ are all open, and they partition $\mathbb{Z}$. Therefore each set $i+d\mathbb{Z}$ for $i=0,\dots,d-1$ has the union of the others as a complement:$$\Huge d\mathbb{Z}=\mathbb{Z}\setminus\bigcup_{i=1}^{d-1}(i+d\mathbb{Z})$$

This suggests that every integer except for $\pm 1$ is either a prime or a multiple of a prime. So we have that:$$\Huge \mathbb{Z}\setminus\{-1,+1\}=\bigcup_{p\text{ prime}}p\mathbb{Z}$$If there were only finitely many primes, the RHS would be a finite union of closed sets and therefore closed. However the LHS is an open set, so there must be an infinite number of primes.