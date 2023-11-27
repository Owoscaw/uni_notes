
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

Let $A\in M_{n\times k}(\Re)$, then:
> The column space of $A$ is the subspace of $\Re^n$ spanned by the columns of $A$. That is, if $A$ is written as the matrix $\begin{pmatrix}\underline c_1&\dots&\underline c_k\end{pmatrix}$, then the column space of $A$ is $span(\underline c_1,\dots,\underline c_2)$ We then define:$$\Huge colrank(A):=dim(columnspace(A))$$
> Similarly, the row space of $A$ is the subspace of $\Re^k$ spanned by the transposes of the rows of $A$. That is, if $A$ is written as the matrix $\begin{pmatrix}\underline r_1\\\vdots\\\underline r_n\end{pmatrix}$, then the row space of $A$ is $span(\underline r_1,\dots,\underline r_n)$ We then define:$$\Huge rowrank(A):=dim(rowspace(A))$$
> The null space, or kernel, of $A$ is the subspace of $\Re^k$ consisting of all solutions to $A\underline x=\underline 0$:, that is $ker(A)=\{\underline x\in\Re^k:A\underline x=\underline 0\}$. We then define:$$\Huge null(A):=dim(ker(A))$$

Suppose that we have $A$ as before, then $P\in M_n(\Re)$ where $P$ is invertible. Then we get:
>$colrank(PA)=colrank(A)$. Suppose $\{\underline v_1,\dots,\underline v_r\}$ is a basis for the column space of $A$. Also suppose that $u\in colspace(PA)$, so $\underline u=(PA)\underline \lambda=P(A\underline\lambda)=P(\mu_1\underline v_1+\dots+\mu_r\underline v_r)=\mu_1P(\underline v_1)+\dots+\mu_r\underline(P\underline v_r)\in span(P\underline v_1,\dots,P\underline v_r)$ for some $\underline \lambda$, since $A\underline\lambda\in colspace(A)$. So we have $colspace(PA)\subseteq span(P\underline v_1,\dots,P\underline v_r)$. So $colrank(PA)\leq r=rank(A)$. Also $colrank(A)=colrank(P^{-1}PA)\leq colrank(PA)$
>$rowspace(PA)=rowspace(A)$. $P$ can be written as a series of elementary row operations, so the rows of $PA$ are linear combinations of the rows of $A$. That is to say $rowspace(PA)\subseteq rowspace(A)$. We also have that $rowspace(A)=rowspace(P^{-1}(PA))\subseteq rowspace(PA)$. By double inclusion we get that these are equal.
>$ker(PA)=ker(A)$. For any $\underline v\in ker(A)$, we have $A\underline v=\underline 0\implies P(A\underline v)=\underline 0\implies (PA)\underline v=\underline 0\implies v\in ker(PA)$, so we have $ker(A)\subseteq ker(PA)$. Also $ker(PA)\subseteq ker(P^{-1}PA)=ker(A)$. By double inclusion we get that these are equal.
>$null(AP)=null(A)$. Suppose that $\{\underline v_1,\dots,\underline v_r\}$ is a basis for $ker(A)$, then if $\underline u\in ker(AP)$. We have $AP\underline u=\underline 0$, hence $A(P\underline u)=\underline 0$, so $P\underline u\in ker(A)$, that is $P\underline u=\lambda_1\underline v_1+\dots+\lambda_r\underline v_r$. Hence $\underline u=\lambda_1(P^{-1}\underline v_1)+\dots+\lambda_r(P^{-1}\underline v_r)$. So $null(AP)\leq r=null(A)$ and $null(A)=nul(APP^{-1})\leq null(AP)$.

## Rank theorem:

$$\Huge rowrank(A)=colrank(A)$$
For $A\in M_{n\times k}(\Re)$, we define:$$\Huge rk(A)=rowrank(A)=colrank(A)$$Then also:$$\Huge rk(A)+null(A)=k$$This is because since doing EROs is left multiplying by elementary matrices, we know that EROs do not change rowrank, colrank, or nullity. When putting $A$ in RREF, rows can be rearranged to make it in the form:$$\Huge A'=\begin{pmatrix}I_r&C\\0_{(n-r)\times r}&0_{(n-r)\times(k-r)}\end{pmatrix}$$For some $r\times(k-r)$ matric $C$. Here, each of the first $r$ rows will define the column space as any column vector with $0$ entries after row $r$. This specifically has dimension $r$. A similar argument goes for the rows, as each $r$ row is linearly independent. Now take $x_{r+1},\dots,x_k$ as free variables, then the general vector in the null space of $A'$ is given by:$$\Huge \underline x=x_{r+1}\begin{pmatrix}-c_1\\1\\0\\\vdots\\0\end{pmatrix}+x_{r+2}\begin{pmatrix}-c_2\\0\\1\\\vdots\\0\end{pmatrix}+\dots+x_k\begin{pmatrix}-c_{k-r}\\0\\0\\\vdots\\1\end{pmatrix}$$Where each $c_i\in\Re^r$ denotes the $i$th column of the matrix $C$. Clearly, these are linearly independent, so we get the result:$$\Huge null(A')=k-r$$Since we know that $rk(A)=r$ and that $null(A)=null(A')$, this can be rearranged to give the result as required. This has a corollary where for any $A\in M_{n\times k}(\Re)$ we have:
> The rank of $A$ is the number of leading $1$s in the RREF of $A$
> The nullity of $A$ is the number of columns in the RREF of $A$ without a leading $1$, that is the number of free variables in the solution set to $A\underline x=\underline 0$


# Sums and intersections of vector subspaces:

Let $V$ be a vector space, and $U,W\subseteq V$ be subspaces of $V$. Then we define:
>$$\Huge U+W:=\left\{v\in V:v=u+w\,\,\text{for some}\,\,u\in U,w\in W\right\}$$
>$$\Huge U\cap W:=\left\{v\in V:v\in U\,\,\text{and}\,\,v\in W\right\}$$

Both $U+W$ and $U\cap W$ are vector subspaces of $V$. Note that:
> If $U=span(u_1,\dots,u_j)$ and $W=span(w_1,\dots,w_k)$, then we have $U+W=span(u_1,\dots,u_j,w_1,\dots,w_k)$. This does not always give a basis for $U+W$.
> For two lines in $\Re^n$ such that $L_1,L_2$ have direction vectors $d_1,d_2$ respectively and pass through the origin, then $L_1+L_2$ is the plane spanned by $d_1$ and $d_2$. (this is a line if they are colinear).

Let $U,W$ be finite dimensional vector subspaces of $V$, then:$$\Huge dim(U)+dim(W)=dim(U+W)+dim(U\cap W)$$Proof:
![[vector intersection proof]]

