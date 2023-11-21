
A real [[Vector space definitions|vector space]] is a non-empty set $V$ with two operations:
> Addition:$$\Huge V\times V\mapsto V$$
> Scalar multiplication:$$\Huge \Re\times V\mapsto V$$

These operations must further satisfy the axioms of a real vector space. Any vector [[Subspaces|subspace]] of $\Re^n$, including $\Re^n$ itself, is also a vector space. The set of all $m\times n$ matrices, $M_{m\times n}(\Re)$ is a vector space. All [[Functions, Domain and Range|functions]] are vector spaces, as we have for a function $f:\Re\mapsto\Re$:$$\Huge (f+g)(t):=f(t)+g(t),\,\,(\lambda f)(t)=\lambda f(t)$$

# Axioms:

The following axioms are associated with the addition function:
>The existence of the additive identity, there is a vector $0$ in $V$ such that for all $v\in V$, $v+0=0+v=v$.
>Commutativity, $v+w=w+v$ for all $v,w\in V$.
>The existence of additive inverses, for every $v\in V$ there exists $-v$ such that $v+(-v)=0=(-v)+v$.
>Associativity, $u+(v+w)=(u+v)+w$ for all $u,v,w\in V$

The following axioms are associated with the scalar multiplication function:
> $0v=0$ for all $v\in V$
> $1v=v$ for all $v\in V$
> Associativity, $(\lambda\mu)v=\lambda(\mu v)$ for all $v\in V$, $\lambda,\mu\in\Re$
> Distributivity, For all $\lambda,\mu\in\Re$ and $v,w\in V$ we have $(\lambda+\mu)v=\lambda v+\mu v$ and $\lambda(v+w)=\lambda v+\lambda w$
> 

# Vector subspaces:

A vector subspace of a vector space $V$ is a non-empty that is a non-empty subset that is itself a vector space with respect to the operations associated with $V$. We say that a non-empty subset $U$ of a vector space $V$ is a vector subspace of $V$ if and only if the following conditions are met:
> For all $u_1,u_2\in U$, then $u_1+u_2\in U$, closure under addition.
> For all $u\in U$ and $\lambda\in\Re$, then $\lambda u\in U$, closure under scalar multiplication.
> $0\in U$, existence of the origin. 

## Bases and dimensions:

Linear combinations, linear spans, [[Subspaces#Spanning sets|spanning sets]], and [[Subspaces#Linear independence|linear independence]] are defined exactly the same way for a vector space $V$ as they are for $\Re^n$. They lead to the following concept.

A finite basis for a vector space $V$ is a finite subset of vectors $\{v_1,\dots,v_k\}\in V$ such that:
> $v_1,\dots,v_k$ are linearly independent
> $V=span(v_1,\dots,v_k)$

Not every vector space has a basis. 

Every [[Matrix definition|matrix]] $A\in M_{m\times n}(\Re)$ can be written in terms of each of it's entries. Let $E_{rs}=(e_{ij})$ be the matrix with $e_{rs}=1$ and $e_{ij}=0$ when $(i,j)\neq(r,s)$. Then $E_{rs}$ form a basis for the $m$ by $n$ matrices, every matrix can be expressed as a linear combination:$$\Huge A=a_{11}E_{11}+\dots+a_{mn}E_{mn}=\sum_{i=1}^m\sum_{j=1}^na_{ij}E_{ij}$$
# Various lemmas:

For vectors $u_1,\dots,u_k\in V$, then $span(u_1,\dots,u_k)$ is a vector subspace of $V$. Assume that $u_1$ can be expressed as a linear combination of other vectors in the set, then $span(u_1,\dots,u_k)=span(u_2,\dots,u_k)$.

Suppose that $\{u_1,\dots,u_k\}$ is a set that is not linearly independent. Then for some $1\leq i\leq k$, we have:$$\Huge u_i\in span(u_1,\dots,u_{i-1},u_{i+1},\dots,u_k)$$
Which further implies:$$\Huge span(u_1,\dots,u_k)=span(u_1,\dots,u_{i-1},u_{i+1},\dots,u_k)$$
Since there is some linear dependence within the set, then:$$\Huge \sum_{j=1}^k\lambda_ju_j=0$$
Has a solution with at least one $\lambda_j$ being non zero. Then the linear dependence relationship can be rearranged to:$$\Huge u_i=\sum_{j=1}^{i-1}-\frac{\lambda_j}{\lambda_i}u_j+\sum_{j=i+1}^k-\frac{\lambda_j}{\lambda_i}u_j$$
This is a linear combination of the vectors $u_1,\dots,u_{i-1},u_{i+1},\dots,u_k$, so it is in the span, as required.

Suppose that $u_1,\dots,u_k$ are linearly independent in a vector subspace $V$ and let $u\in V$ such that $u\notin span(u_1,\dots,u_k)$, then the vectors $u_1,\dots,u_k,u$ are linearly independent.

# Assorted Theorems:

## Existence of a finite base:

Every vector space that is spanned by finitely many vectors has a basis.

## What is a basis:

Let $u_1,\dots,u_k$ be vectors in a vector space $V$, then the following statements are pairwise equivalent:
> The vectors $u_1,\dots,u_k$ form a (finite) basis of $V$ ($I$)
> The vectors $u_1,\dots,u_k$ form a maximal linear independent set in $V$ ($II$)
> Any vector $u\in V$ can be uniquely expressed as: ($III$)$$\Huge u=\lambda_1u_1+\dots+\lambda_ku_k$$
> The vectors $u_1,\dots,u_k$ form a minimal spanning set of $V$ ($IV$)

This is proven as follows:
![[basis proof]]

# Steinitz Exchange Lemma:

A vector space is finite-dimensional if and only if it has a finite basis. This also means that the vector space has a finite spanning set.

Let $V$ be a vector space and $S=\{\underline u_1,\dots,\underline u_k\}\subseteq V$ be a spanning set of $V$, that is $V=span(S)$. Also let $\{\underline v_1,\dots,\underline v_l\}\subseteq V$ be linearly independent. Then there exist distinct elements $\underline u_{i_1},\dots,\underline u_{i_l}\in S$, $l$ elements are chosen from $S$ such that for each $1\leq j\leq l$:$$\Huge (S\setminus\{\underline u_{i_1},\dots,\underline u_{i_j}\})\cup\{\underline v_1,\dots,\underline v_j\}\,\,\text{spans} \,\,V$$
This has corollaries:
> $k\geq l$, as $l$ elements are taken from a set with $k$ elements. For this to be possible, the statement $k\geq l$ must be true.
> If $\{\underline u_1,\dots,\underline u_s\},\{\underline v_1,\dots,\underline v_t\}\subseteq V$ are both bases for $V$, then $s=t$. Since $\{\underline u_1,\dots,\underline u_s\}$ spans $V$ and $\{\underline v_1,\dots,\underline v_t\}$ is linearly independent, then we have $s\geq t$ by above. Switch their roles then you get $t\geq s$. The only scenario in which this is satisfied is when $t=s$.

If $V$ is finite-dimensional, then we define $\dim(V)\in\mathbb{N}_0$ to be the number of elements in any basis of $V$., the Steinitz Exchange Lemma shows that this is equal for all basis. We can then prove the Steinitz Exchange Lemma:
![[SET proof]]

Let $V$ be a finite dimension vector space and $U$ a vector subspace of $V$, then:
> $U$ is finite dimensional
> $dim(U)\leq dim(V)$
> $dim(U)=dim(V)\iff U=V$
![[finite dimension proof]]

The other two results follow from this.

Let $V$ be a vector space of dimension $k$, then let $v_1,\dots,v_l\in V$. Then we have:
> If $l>k$, then $v_1,\dots,v_l$ are linearly dependent
> If $l<k$, then $v_1,\dots,v_l$ does not span $V$
> If $l=k$, then the following statements are a tautology:
> >$v_1,\dots,v_l$ form a basis of $V$ $(I)$
> >$v_1,\dots,v_l$ are linearly independent ($II$)
> >$v_1,\dots,v_l$ span $V$ ($III$)

This is proven as follows:
![[basis tautology]]