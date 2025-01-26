
The idea of groups is to analyse the intuitive notion of symmetries. Here are some examples:![[reflections]]Here, each shape after the last gains more symmetries. Note that the circle has infinite symmetry along any axis of reflection and rotation about the center. A composition of symmetries is again a symmetry. Note that the action of performing no action (corresponding to a symmetry composed with its inverse) is also a symmetry.

We can now define the group. A group is a pair $(G,\circ)$ where $G$ is a set and $\circ$ is a [[Rings, subrings, and fields#Binary operations|binary operation]] on $G$ with the following properties:
> Associativity: $(a\circ b)\circ c=a\circ(b\circ c)\,\forall a,b,c\in G$
> Existence of the identity: $g\circ e=e\circ g=g\,\forall g\in G$
> Existence of the inverse: $\forall g\in G\exists h\in G$ such that $g\circ h=h\circ g=e$

Furthermore, an abelian group also satisfies $g\circ h=h\circ g$ for all $g,h\in G$. For example, $(\Re,+)$ forms an abelian group with $0\in\Re$ as the identity element, and the inverse of $a\in\Re$ is $-a$. Taking the [[Integral domains, units, and polynomial rings#Units|units]] of $\Re$, that is $\Re^X=\Re\setminus\{0\}$ we cannot use addition as the binary operator, so we use multiplication. We claim that $(\Re^X,\times)$ is an abelian group. The identity for this group must be $1$ as the operator is $\times$. This identity indeed belongs to $\Re^x$ and the inverse of each $a\in\Re^X$ is $\frac{1}{a}\in\Re^X$, so this indeed forms a group.

# Subgroups:

A subset $H$ of $G$ is said to be a subgroup of $(G,\circ)$ if it is itself a group under the same operation. A subgroup is proper if $H\neq\{e\}$ and $H\neq G$. Note that the operator between a group and a subgroup should be distinguished as the sources and targets are different.

A subset $H\subseteq G$ becomes a subgroup if the three conditions are met:
> $H\neq\emptyset$
> $h_1,h_2\in H\implies h_1\circ h_2\in H$
> $h\in H\implies h^{-1}\in H$

We denote this as $(H,\circ)<(G,\circ)$. Examples:
> The group $(\{0\}, +)$ is a subgroup of $(\mathbb{Z},+)$
> Let $T=\left\{\begin{pmatrix}a&0\\0&d\end{pmatrix}:a,d\in\Re^X\right\}$, then $(T,\times_{GL})$ is a subgroup of $(GL_2(\Re),\times_{GL})$. The subgroup is closed under matrix multiplication since:$$\Huge \begin{pmatrix}a_1&0\\0&d_1\end{pmatrix}\times_{GL}\begin{pmatrix}a_2&0\\0&d_2\end{pmatrix}=\begin{pmatrix}a_1a_2&0\\0&d_1d_2\end{pmatrix}$$Whenever $a_1,a_2,d_1,d_2$ are non-zero scalars, $a_1a_2,d_1d_2$ are also non-zero scalars. The inverse of the matrix is $\begin{pmatrix}1/a&0\\0&1/d\end{pmatrix}$, which is indeed in $T$ as the inverses of $a,d$ given by $1/a,1/d$ are also non-zero scalars.

# Cosets and Lagrange's theorem:

Let $H$ be a subgroup of the finite group $G$. Then:$$\Huge |H|||G|$$That is, the order of $H$ divides the order of $G$. To prove this, we must first define cosets.

Let $H<G$. Then for any $g\in G$ call $g\circ H=\{g\circ h:h\in H\}$ the left coset of $g$ with respect to $H$ in $G$. We propose that all left cosets with respect to the subgroup $H<G$ have the same cardinality. Moreover, this cardinality is $|H|$. 

Any coset has the form $g\circ H$ for some $g\in G$. For this $g$ consider the map:$$\Huge \beta_g:H\rightarrow g\circ H,\,\,g\mapsto g\circ h$$We check if this is a bijection. First we check injectivity. If $g\circ h_1=g\circ h_2$ then by composition on the left by $g^{-1}$ we find $g^{-1}\circ(g\circ h_1)=g^{-1}\circ(g\circ h_2)$. Using associativity and $g^{-1}\circ g=e$ we have that $h_1=h_2$, so the map is injective. Surjectivity is obvious from the definition of the coset since each $x\in g\circ H$ has form $x=g\circ h$ for some $h\in H$. Therefore we can write $x=\beta_g(h)$, proving bijectivity. Therefore we must have that the cardinality of all left cosets is $|H|$.

We also define the right coset as follows. Let $H<G$. Then for any $g\in G$ call $H\circ g=\{h\circ g:h\in H\}$ the right coset of $g$ with respect to $H$.

# Normal subgroups:

A subgroup $H$ of a group $G$ is called normal in $G$ if $gH=Hg$ for any $g\in G$. We denote this as $H$