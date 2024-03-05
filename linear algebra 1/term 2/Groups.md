
A groups is a set, $G$, with an operation $\cdot:G\times G\mapsto G$ such that the following axioms hold:
# Axioms:

If $x,y\in G$, then $x \cdot y\in G$ (closure)

$(x \cdot y)\cdot z=x \cdot(y \cdot z)$ (associativity)

$G$ contains an identity element $e\in G$ such that $e \cdot x=x \cdot e=x$ for all $x\in G$ (identity)

Each $x\in G$ has an inverse element $x^{-1}\in G$ such that $x \cdot c^{-1}=x^{-1}\cdot x=e$ (inverses)

We also call a group abelian if $x \cdot y= y \cdot x$ for all $x,y\in G$. Note that both $(\Re,+)$ and $(\Re\setminus\{0\},\times)$ are both abelian with identity elements $0$ and $1$ respectively. We propose that $e$ is unique for each group. Say that $e_1,e_2$ are both identities of $G$, therefore $e_1\cdot e_2=e_1$ and $e_1\cdot e_2=e_2$, therefore $e_1=e_2$, every identity element is unique for their respective group. Note that $(M_n(\Re),\times)$ is not an abelian group, since not every matrix has an inverse, but $(M_n(\Re),+)$ is.

Let $(G,\cdot)$ be a group. Then $H\subset G$ is a subgroup of $G$ if $H$ subsets $G$ and $H$ is a group itself with respect to the same operator as $G$

# Finite and infinite groups:

$SU(2)$, the group of special unitary matrices is an example of a group with respect to matrix multiplication. However there are infinitely many elements in this group, as are most matrix groups.

A finite group $G$ is a group with a finite number of elements. The order of $G$, written as $|G|$, is the number of elements in $G$. Lagrange theorised that for a finite group $G$, and a subgroup $H$, then the order of $H$ divides the order of $G$.

For example, consider the group $G=(\mathbb{Z},+)$, an infinite abelian group. Fix an integer $n\in \mathbb{N}$ with $n\geq2$ and consider an equivalence relation on $\mathbb{Z}$: $p\sim q\iff n$ divides $p-q$, that is $p=q+kn$ for some $k\in \mathbb{Z}$. Then set $[p]=\{q\in \mathbb{Z}:q\sim p\}$, this is the congruence class of integers modulus $n$.

Set $\mathbb{Z}_n=\{[0],[1],\dots,[n-1]\}$. Under addition this is a finite abelian group with order $n$, sometimes called the $n$th order cyclic group.