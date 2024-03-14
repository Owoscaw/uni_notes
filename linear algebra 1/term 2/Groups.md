
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

Set $\mathbb{Z}_n=\{[0],[1],\dots,[n-1]\}$. Under addition this is a finite abelian group with order $n$, sometimes called the $n$th order cyclic group. The behaviour of this group under addition is encoded by the Cayley table:

|  $+$  | $[0]$ | $[1]$ | $[2]$ | $[3]$ |
|:-----:|:-----:|:-----:|:-----:|:-----:|
| $[0]$ | $[0]$ | $[1]$ | $[2]$ | $[3]$ |
| $[1]$ | $[1]$ | $[2]$ | $[3]$ | $[0]$ |
| $[2]$ | $[2]$ | $[3]$ | $[0]$ | $[1]$ |
| $[3]$ | $[3]$ | $[0]$ | $[1]$ | $[2]$ |
This is the table for $\mathbb{Z}_4$. Another finite set can be defined called the Klein group on the set $\{a,b,c,e\}$ with the table:

| $\cdot$ | $e$ | $a$ | $b$ | $c$ |
|:-------:|:---:|:---:|:---:|:--- |
|   $e$   | $e$ | $a$ | $b$ | $c$ |
|   $a$   | $a$ | $e$ | $c$ | $b$ |
|   $b$   | $b$ | $c$ | $e$ | $a$ |
|   $c$   | $c$ | $b$ | $a$ | $e$ |
These can be thought of as rotations by $\pi$ in $\Re^3$

# Isomorphism:

Two groups $G$ and $H$ are isomorphic as groups if there is a bijection $f:G\mapsto H$ that preserves the group operation:$$\Huge f(g_1\cdot_Gg_2)=f(g_1)\cdot_Hf(g_2)$$Where $\cdot_G,\cdot_H$ are the group operations for $G,H$ respectively. This implies that:$$\Huge f(e_G)=e_H$$Where $e_G,e_H$ are the identity elements of groups $G,H$ respectively. We claim that $\mathbb{Z}_4$ is not isomorphic to the Klein group. To see this, first let $g\in G$, then call the order of $G$ the smallest positive integer $n$ such that $g^n=e$. We propose that:
> The identity has order $1$
> In $(\mathbb{Z},+)$, no element except the identity has infinite order
> In $\mathbb{Z}_n$, every element has finite order

We propose that if $G$ and $H$ are isomorphic, then the order of any $g\in G$ corresponds to the order of $f(g)\in H$. This is because, assuming isomorphism, we have that for any $g\in G$, $f(g^n)=f(g)^n=f(e_G)=e_h$, giving us $n\geq m=|f(g)|$. Similarly, $g^m=(f^{-1}(f(g)))^m=f^{-1}(f(g)^m)=f^{-1}(e_H)=e_G$, giving us $m\geq n$. Therefore we get $n=m$, the order must be the same.

Using this fact, we can deduce that $\mathbb{Z}_4$ and the Klein $4$-group are not isomorphic, since in the Klein group, $a,b,c$ all have order $2$, whereas in $\mathbb{Z}_4$ only $[2]$ has order $2$.

Note that $\mathbb{Z}_3^\times$ is not a group since, taking $[1]$ as the identity does not allow for $[0]$ to have an inverse, so we remove $[0]$ and consider $\mathbb{Z}_3^\times=\{[1],[2]\}$. Looking at the group table for this, one can see that it is isomorphic to $\mathbb{Z}_2^+$. In general, $\mathbb{Z}_n^\times$ can be made into a proper group by keeping only integers $k$ such that the greatest common divisor of $k,n$ is $1$.

# Direct product:

Let $G,H$ be two groups. The direct product $G\times H$ is defined by an operator $\bullet$, where elements of $G\times H$ are the ordered pairs $(g,h)$ for $g\in G,h\in H$. The group operation $\bullet_{G\times H}$ works component wise:$$\Huge (g_1,h_1)\bullet(g_2,h_2)=(g_1\cdot_Gg_2,h_1\cdot_Hh_2)$$Where $\cdot_G,\cdot_H$ are the respective group operations on $G,H$. We propose that the direct product of two groups $G,H$ is a group with order:$$\Huge |G\times H|=|G|\cdot|H|$$

# Rotations and subgroups:

Consider [[Real vector spaces|$\Re^n$]] with respect to the standard [[Inner product spaces|inner product]]:$$\Huge (\underline v,\underline w)=\underline w^T \underline v$$Orthogonal transformations are linear transformations $\underline v\mapsto M \underline v$ that preserve lengths and angles. We propose that the group of orthogonal transformations on $\Re^n$ is the group [[Norms and orthogonality#Orthogonality and Unitary diagonalisation|$O(n)$]]. In order for $M$ to be an orthogonal transformation we require that it preserves lengths and angles of any two vectors $\underline v, \underline w\in\Re^n$. That is:$$\Huge \underline w^t \underline v=(M \underline w)^T(M \underline v)= \underline w^TM^TM \underline v\implies M^TM=I$$By definition $M$ must then be a member of $O(n)$, so these such orthogonal transformations represented by $M$ form the orthogonal group, $O(n)$. Note that while $O(1)$ is both finite and abelian wrt matrix multiplication, $O(n)$ for $n\geq 2$ is neither abelian nor finite. This is because we know $SO(2)$ is a subgroup of $O(2)$, and $SO(2)$ is not finite as each element in $SO(2)$ corresponds to a rotation by $\theta\in[0,2\pi)$.

The group of rotations in $\Re^n$ is the subgroup of $O(n)$ with $\det(M)=1$, that is $SO(n)$. Note that $SO(n)$ is not abelian for $n\geq 3$.

Consider a regular polygon in the plane with $n$ sides, the rotations that leave it unchanged form a finite abelian group of order $n$, isomorphic to $\mathbb{Z}_n$. These have matrix representation $M_j\in SO(2)$:$$\Huge M_j=\begin{pmatrix}\cos\left(\frac{2\pi j}{n}\right)&-\sin\left(\frac{2\pi j}{n}\right)\\\sin\left(\frac{2\pi j}{n}\right)&\cos\left(\frac{2\pi j}{n}\right)\end{pmatrix}$$Note that $M_iM_j=M_{i+j}$. The group of all symmetries of the regular $n$-sided polygon in the plane is called the Dihedral group, $D_n$, which is a finite group with order $2n$.

The symmetric group of degree $n$, denoted by $S_n$, is the group whose elements are all permutations that can be performed on $n$ distinct symbols, with group operation being the composition of permutations. The order of this group is $n!$ and $D_n$ is always a subgroup. Any permutation can be written as a composition of transpositions.

The sign of a permutation $\sigma$ is defined to be $+1$ if a permutation contains an even number of transpositions and $-1$ for an odd number:$$\Huge \text{sgn}(\sigma)=\begin{cases}+1&\text{for even transpositions}\\-1&\text{for odd transpositions}\end{cases}$$We can then define the alternating group:$$\Huge A_n=\{\sigma\in S_n:\text{sgn}(\sigma)=+1\}$$Which is a subgroup of $S_n$, with degree $\frac{n!}{2}$.

Euler's principle axis theorem states that every rotation in $\Re^3$ has an axis. That is, if $M\in SO(3)$, there exists a non-zero vector $\underline v$ such that $M \underline v=\underline v$. This is the same as saying that every matrix in $SO(3)$ has $1$ as an [[Eigenvalues, Eigenvectors, and Diagonalisation|eigenvalue]], since we require $M \underline v=(\lambda=1)\underline v$. The eigenvalues of $M$ are roots of $P_m(t)=\det(M-tI)$. This should factorise to $P_M(t)=(\lambda_1-t)(\lambda_2-t)(\lambda_3-t)$ for $\lambda_i\in \mathbb{C}$ 