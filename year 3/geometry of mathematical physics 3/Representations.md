
# Definitions:

Let $V$ be a [[Vector space definitions|vector space]], then we denote the group of linear, invertible maps $V\rightarrow V$ as $GL(V)$. For $V=\Re^n$ we get $GL(V)=GL(n,\Re)$. A representation $R$ of a group $G$ is a group homomorphism $R:G\rightarrow GL(V)$. The idea is that even if $G$ is some abstract group, the representation $R$ of $G$ assigns some linear transformation.

We say that $G$ acts on elements of $V$ in the representation $R$ as:$$\Huge\forall g\in G,\,\,R(g)\in GL(V)\text{ acts on }\underline{v}\in V$$
Note that $R$ is a homomorphism between groups:$$\Huge R(g_1\circ_Gg_2)=R(g_1)\circ_{GL(V)}R(g_2)$$but does not need to be injective, that is we may lose some information about $G$. The trivial representation for a group is defined as:$$\Huge 1(g)=1\in GL(\Re)$$
## $SU(n)$:
The fundamental representation of $SU(n)$ is defined as:$$\Huge \forall g\in SU(n):\,\,R(g)=g\in GL(n,\mathbb{C})$$Here we simply have $V=\mathbb{C}^n$. We denote a representation of $SU(n)$ by its dimension, $\mathbf{n}$. We also define the antifundamental representation by $\bar R(g)=\bar g$, denoted by $\bar{\mathbf{n}}$.

## $SO(n)$:
The fundamental representation of $SO(n)$ is defined as:$$\Huge \forall M\in SO(n):\,\,\,R(M)=M$$acting on the vector space $V=\Re^n$. It makes no sense to define the antifundamental here, as we are only acting on real-valued matrices.

# Lie groups:

For all [[Lie Groups and Algebras#Lie groups|Lie groups]], there is an associated vector space defined as its Lie algebra. We define the adjoint representation of $G$ as:$$\Huge \text{Ad}:G\rightarrow GL(\pmb g),\,\,\text{Ad}(h)[\gamma]=h\gamma h^{-1},\,\,\forall h\in G,\forall\gamma\in\pmb g$$This map takes $h\in G$ to $\text{Ad}(g)\in GL(\pmb g)$, an invertible and linear map. To specify $\text{Ad}(h)$ we need to know how it acts on the elements $\gamma\in\pmb g$. 

## $U(1)$ example:
Take $G=U(1)$ for example, we [[U(1),SU(2),SO(3)#$U(1)$|saw]] that the most general element is written as $e^{i\theta}$, and $\pmb{u(1)}=\{i\phi:\phi\in\Re\}$. Then we observe:$$\Huge\text{Ad}(e^{i\theta})[i\phi]=e^{i\theta}(i\phi)e^{-i\theta}=i\phi$$This is the trivial representation.
## $SU(2)$ example:
For $SU(2)$, we saw that we could write any element in its Lie algebra $\pmb{su(2)}$ as a linear combination of $i\sigma_i$, where $\sigma_i$ are the Pauli matrices. Then for $g\in SU(2)$ we have:$$\Huge \text{Ad}(g)[\gamma]=g\gamma g^{-1}=ig(\underline{\alpha}\cdot\underline{\sigma})g^{-1}$$This is exactly the action we used to [[U(1),SU(2),SO(3)#$SO(3)$ versus $SU(2)$|map]] $SU(2)$ to $SO(3)$.

# Properties of representations:

## Faithfulness:
A representation is called faithful if $R$ is injective. We saw examples of [[U(1),SU(2),SO(3)#$SO(3)$ versus $SU(2)$|SU(2)]] acting faithfully on $\mathbb{C}^2$ and non-faithfully on $\Re^3$. 

We can act with $SU(2)$ faithfully on $\mathbb{C}^4$ by using the block diagonal representation:$$\Huge r:g\rightarrow\begin{pmatrix}g & 0 \\ 0 & g\end{pmatrix}$$This seems redundant, and we want to distinguish between such cases and those that truly give something new. A way to phrase this is by using invariant subspaces. 

## Invariance:
A subspace $W\subseteq V$ is called invariant if $r(g)w\in W$ for all $g\in G$ and all $w\in W$.

Returning to the $SU(2)$ example, we can decompose $V=\mathbb{C}^2\oplus\mathbb{C}^2\oplus\dots$ and every summand is itself an invariant subspace.

## Irreducibility:
A representation $r:G\rightarrow GL(V)$ is irreducible if the only invariant subspaces are $V$ and $\{0\}$. Otherwise, it is called reducible.

Mapping all $\pmb g\in G$ to $\mathbb{1}\in GL(V)$ is a group homomorphism, so this trivial representation always exists. This is the "most unfaithful" as possible and reducible. Every subspace of $V$ is an invariant subspace. Objects transforming in this representation are called scalars or singlets. They are often referred to as "living in the $\mathbb{1}$ of $G$".

## Unitarity:
A representation $r:G\rightarrow GL(V)$ is unitary if $V$ has an inner form $\langle\cdot,\cdot\rangle$ and $\langle x,y\rangle=\langle r(g)x,r(g)y\rangle$ for all $g\in G$ and all $x,y\in V$. The defining representation of $SU(n)$ is faithful, irreducible, and unitary.

This seems like a natural concept, associating preservation of the inner form with unitary matrices. The power of this lies in the following theorem:

Let $r:G\rightarrow GL(V)$ be a finite-dimensional unitary representation. Then it can be completely decomposed into irreducible representations $r_i(G):$$$\Huge r(G)=\bigoplus_i r_i(G),\,\,V=\bigoplus_i V_i,\,\,r_i(G)\in GL(V_i)$$We can think of $r(G)$ as respecting the block diagonal form in an appropriate basis of $V$. Proof:
> Let $r(G)$ be a reducible representation and consider any of its invariant subspaces $W$. The main step of the proof is to show that the orthogonal complement:$$\Huge W^\perp=\{v\in V:\langle v,w\rangle=0,\,\,\forall w\in W\}$$is also an invariant subspace. 
> For any $r(g)$ we define its dual $r^*(g)$ as:$$\Huge\langle v,r(g)u\rangle=\langle r^*(g)v,u\rangle$$for all $v,u\in V$. It follows that:$$\Huge \langle v,u\rangle=\langle r(g)v,r(g)u\rangle=\langle r^*(g)r(g)v,u\rangle$$so that $r^*(g)r(g)=\mathbb{1}$.
> Now for all $w\in W,v\in W^\perp$ and all $g\in G$ we have:$$\Huge 0=\langle v,w\rangle=\langle v,r(g)w\rangle=\langle r^*(g)v,w\rangle=\langle(r(g))^{-1}v,w\rangle$$where $(r(g))^{-1}$ is the inverse of the matrix $r(g)\in GL(V)$. As every element in $G$ has an inverse and $(r(g))^{-1}=r(g^{-1})$ we write:$$\Huge0=\langle r(g)v,w\rangle$$for all $w\in W,v\in W^\perp$ and all $g\in G$. This means whatever $g$ acts on $v\in W^\perp$, we stay in $W^\perp$, making it an invariant subspace.
> Now we decompose:$$\Huge r(G)=r_W(G)\oplus r_{W^\perp}(G),\,\,V=W\oplus W^\perp$$as both $W,W^\perp$ are invariant subspaces. If both $r_W(G)$ and $r_{W^\perp}(G)$ are irreducible, we are done. Otherwise we simply run the same argument again to achieve a finer decomposition. This iteration must terminate as $V$ is finite dimensional.

This is trivial for unitary representations. However for dealing with inner forms that are not respected by $r(g)$, we must generate a new inner form that does:

Let $G$ be a compact Lie group and $r(G)$ a finite-dimensional representation on a vector space with inner form $\langle\cdot,\cdot\rangle$. Then there exists an inner form invariant under $r(G)$ and hence can be completely decomposed. Proof:
> Let $\langle\cdot,\cdot\rangle$ be some inner form on $V$. As $G$ is a compact group $\langle r(g)v,r(g)w\rangle$ is bounded for fixed $v,w$. This cannot diverge for $g\rightarrow\hat g$ anywhere on $G$ as $\hat g$ cannot be in $G$. But it follows from $G$ being topologically closed that any sequence of group elements $g_i\in G$ has a limit that is also in $G$. Hence there must be a maximal value of $\langle r(g)v,r(g)w\rangle$ for fixed $v,w$ that we can use as the bound.
> Furthermore $G$ is some bounded subspace in $\Re^m$ for some $m$ for the matrix Lie groups we are using, and as such has finite volume. We can then integrate a bounded function over it and receive a finite answer. In particular we can use any realisation of $G$ as a subset $\Re^n$ to define:$$\Huge \langle v,w\rangle_G=\int_G \langle r(g)v,r(g)w\rangle dV$$Here, we are averaging over the action of the group on $\langle v,w\rangle$. We act with a group element $h$ on $v,w$:$$\large \langle r(h)v,r(h)w\rangle_G=\int_G \langle r(g)r(h)v,r(g)r(h)w\rangle dV=\int_G \langle r(gh)v,r(gh)w\rangle dV$$where we have used that $r$ is a group homomorphism. Now if $g$ sweeps the whole group, so will $gh$ for any $h\in G$. In particular, every group element $g'$ can be uniquely written as $g'=gh$ for some $g$ by taking $g=g'h^{-1}$. Hence:$$\Huge \langle r(h)v,r(h)w\rangle_G=\int_G \langle r(gh)v,r(gh)w\rangle dV=\int_G \langle v,w\rangle dV=\langle v,w\rangle _G$$

# Schur's lemma:

Let $r$ be an irreducible representation of $G$ on a finite-dimensional complex vector space $V$, and let $T:V\rightarrow V$ be a linear map such that:$$\Huge r(g)T=Tr(g)$$for all $g\in G$. Then either:
> $T=0$
> $T=c\mathbb{1}$ for some complex number $c$

## Proof:
First observe that $\ker T$ is an invariant subspace. If $v\in\ker T$ we have:$$\Huge 0=Tv=r(g)Tv=Tr(g)v$$so $r(g)\ker T$ as well. As we have assumed that $r$ is irreducible, $\ker T=V$ or $\ker T=\{0\}$. If $\ker T=V$ it follows that $T=0$, so the first case is realised.

Now we assume that $\ker T=\{0\}$. As a complex matrix, $T$ has at least one non-zero eigenvalue. Let such value be $c$ and the associated eigenvector be $v_c$. Now consider the map $\hat T=T-c\mathbb{1}$ for which $v_c\in\ker T$. We have:$$\Huge r(g)\hat T=\hat Tr(g)$$as the identity commutes with every matrix. Now we can observe that $\ker\hat T$ is an invariant subspace and hence must be $\{0\}$ or $V$. We already know that $\ker\hat T\neq0$ so it must be that $\ker\hat T=V$, implying that $\hat T=0$ and that $T=c\mathbb{1}$.

## Schur's lemma with [[Principles of QM|QM]]:
Suppose that $\hat H$ is the Hamiltonian for a Quantum mechanical system and that $\hat H$ has a symmetry with respect to some group $G$:$$\Huge \implies \exists\hat Q(g):[\hat H,\hat Q(g)]=0,\,\,\forall g\in G$$Then we have the setup for Schur's lemma, therefore in any irreducible representation of a symmetric group, we have:$$\Huge \hat H=c\mathbb{1}$$for some $c\in \mathbb{C}$. This is equivalent to the fact that the spectrum of $\hat H$ can be decomposed into eigenspaces, corresponding to irreducible representations of symmetry groups.

# Irreducible representations:

## $U(1)$:
All of the irreducible representations of $U(1)$ are unitary and $1$-dimensional. For $n\in\mathbb{Z}$ we define:$$\Huge r_n:U(1)\rightarrow GL(1,\mathbb{C}),\,\,r_n(e^{i\psi}\in U(1))=e^{in\psi}$$as the irreducible representations of $U(1)$. The proof of this involves Schur's lemma and the fact that $U(1)$ is abelian. Finding irreducible representations of abelian groups is rather trivial, we will see that for non-abelian groups, this process is much harder.

## Lie algebras:
Recall that the representation of a group $G$ is a map $R:G\rightarrow GL(V)$ that preserves group structure. The representation of a lie algebra $\pmb g$ will be a map that preserves the structure of the Lie algebra, namely the Lie bracket $[,]$.

We define the Lie algebra homomorphism as a linear map $f:\pmb g\rightarrow\pmb h$ between Lie algebras such that:$$\Huge f([\gamma,\delta]_{\pmb g})=[f(\gamma),f(\delta)]_{\pmb h},\,\,\forall \gamma,\delta\in\pmb g$$The representation of a Lie algebra $\pmb g$ is then a Lie algebra homomorphism:$$\Huge \rho:\pmb g\rightarrow GL(V)$$with $V$ a finite dimensional vector space over $\Re$ or $\mathbb{C}$. Such representation is reducible if there exists some $W\subseteq V$ invariant with $W\neq\{0\}$ or $V$. That is, $\rho(\gamma)\underline{w}\in W$ for all $\underline{w}\in W,\gamma\in\pmb g$. If $\rho$ is not reducible, then it is an irreducible representation.

If $g(t)$ is a path in $G$ such that $g(0)=\mathbb{1}$:![[Representations 2025-11-25 16.30.35.excalidraw]]More formally, let $R:G\rightarrow GL(V)$ be a finite dimensional representation of $G$. Then there exists an associated $\rho:\pmb g\rightarrow GL(V)$ Lie algebra representation such that:$$\Huge R(e^{t\gamma})=e^{t\rho(\gamma)},\,\,\forall \gamma\in\pmb g$$that is, $\rho(\gamma)=\frac{\partial }{\partial t}(R(e^{t\gamma}))|_{t=0}$. There are two steps to prove this:
> First we prove that $\rho$ is linear. To do this, consider the path in $G$:$$\Huge g(t)=e^{t\gamma}\cdot e^{i\delta}$$We then consider the derivative of its representation evaluated at $t=0$:$$\Huge\begin{align*}
\frac{\partial }{\partial t}(R(g(t)))|_{t=0}&=\frac{\partial }{\partial t}(R(e^{t\gamma}\cdot e^{t\delta}))|_{t=0}\\
&=\frac{\partial }{\partial t}(R(e^{t\gamma})\cdot R(e^{t\delta}))|_{t=0}\\
&=\frac{\partial }{\partial t}(R(e^{t\gamma}))|_{t=0}R(\mathbb{1})+R(\mathbb{1})\frac{\partial }{\partial t}(R(e^{t\delta}))|_{t=0}\\
&=\rho(\gamma)+\rho (\delta)
\end{align*}$$where we have used the fact that representations preserve group structure on the second line. We also have:$$\Huge\begin{align*}
e^{t\delta}\cdot e^{t\delta}&=\sum_{k=0}^\infty\frac{(t\gamma)^k}{k!}\sum_{l=0}^\infty\frac{(t\delta)^l}{l!}\\
&=(1+t\gamma+\dots)(1+t\delta+\dots)\\
&=\sum_{n=0}^\infty\frac{(t(\gamma+\delta))^n}{n!}+\frac{t^2}{2}(\gamma\delta-\delta\gamma)+\mathcal{O}(t^3)
\end{align*}$$Returning to our derivative calculation:$$\Huge\begin{align*}
\frac{\partial }{\partial t}(R(g(t)))|_{t=0}&=\frac{\partial }{\partial t}(R(e^{t(\gamma+\delta)}+t^2(\dots)))|_{t=0}\\
&=\frac{\partial }{\partial t}(R(e^{t(\gamma+\delta)}))|_{t=0}\\
&=\rho(\gamma+\delta)
\end{align*}$$Showing that $\rho$ is a linear map. It remains to show that $\rho$ is a Lie algebra homomorphism.

### Examples:

The trivial representation $\rho:\pmb g\rightarrow GL(V)$ where $V=\Re$ and $\rho(\delta)=0$ for all $\delta\in\pmb g$ is indeed an irreducible representation.

The adjoint representation $\text{ad}:\pmb g\rightarrow GL(\pmb g)$ with $\text{ad}(\delta)[\gamma]=[\delta,\gamma]\in\pmb g$ for all $\gamma\in\pmb g$ is the Lie algebra version of the adjoint representation.