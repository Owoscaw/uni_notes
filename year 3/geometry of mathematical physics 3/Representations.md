
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

# Representations of $SU(2)$:

Given some complex polynomial $P(z)$ in two variables $z=(z_1,z_2)$, we can let $SU(2)$ act on $P(z)$ in this way. If $P(z)$ is a homogenous polynomial of degree $d$ we can write:$$\Huge P(z)=\sum_{k=0}^da_kz_1^kz_2^{d-k}$$The space of such polynomials is a vector space $\Pi_d$ of dimension $d+1$. Letting $SU(2)$ act on $\mathbb{C}^2$ we have a corresponding induced action on the vector space of polynomials.

We propose that the map:$$\Huge r_d(g)P=P(g^{-1}z)$$where $g^{-1}\in SU(2)$ acts on $z=(z_1,z_2)$ as:$$\Huge \begin{pmatrix}z_1 \\ z_2\end{pmatrix}=g^{-1}\begin{pmatrix}z_1 \\ z_2\end{pmatrix}$$defines a representation $r_d$ of $SU(2)$ on the complex vector space $\Pi_d$ of dimension $d+1$.

We can then find representations $\rho_d$ of $\pmb{su}(2)$ that are associated with the $r_d$ described above. We choose $l_j=\frac{i}{2}\sigma_j$ as the generators of the Lie algebra $\pmb{su}(2)$:$$\Huge l_1=\frac{1}{2}\begin{pmatrix}0 & i \\ i & 0\end{pmatrix},\,\,l_2=\frac{1}{2}\begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix},\,\,l_3=\frac{1}{2}\begin{pmatrix}i & 0 \\ 0 & -i\end{pmatrix}$$Their action on the monomials $z_1^kz_2^{d-k}$ is then:$$\Huge\begin{align*}
l_1&:z_1^kz_2^{d-k}\rightarrow -\frac{i}{2}(kz_1^{k-1}z_2^{d-k+1}+(d-k)z_1^{k+1}z_2^{d-k-1})\\
l_2&:z_1^kz_2^{d-k}\rightarrow\frac{1}{2}(-kz_1^{k-1}z_2^{d-k+1}+(d-k)z_1^{k+1}z_2^{d-k-1})\\
l_3&:z_1^kz_2^{d-k}\rightarrow i(d/2-k)z_1^kz_2^{d-k}
\end{align*}$$
For every integer $d\geq0$ there is a single finite dimensional irreducible representation $r_d$ of $SU(2)$ on a complex vector space $\Pi_d$ of dimension $d+1$. These are all of the complex irreducible finite-dimensional representations of $SU(2)$. Proof:
> First we prove a lemma to make life easier:
> > Let $r$ be a complex representation of $SU(2)$ acting on $V$. Then all eigenvalues of $\rho(\sigma_i)$ for $\rho$ the associated representation of $\pmb{su}(2)$ are real.
> > We denote $\exp(i\rho(\sigma_j))=r_j$ and $\rho(\sigma_j)=\rho_j$ so that $\exp(i\rho_j)=r_j$. As $SU(2)$ is compact, we can choose some inner form $\langle\cdot,\cdot\rangle$ on the complex vector space $V$ such that:$$\Huge \langle r_jv,r_jv\rangle=\langle v,v\rangle$$We know we can always choose a basis such that $\rho_i^\dagger=\rho_i$, so let $v$ be an eigenvector of $\rho_j$ with eigenvalue $e_v$ and we find:$$\Huge e_v \langle v,v\rangle=\langle v,\rho_jv\rangle=\langle \rho_jv,v\rangle=\bar e_v \langle v,v\rangle$$therefore $e_v$ is real, proving the lemma.
> We start by enlarging the scope and study representations of the Lie algebra $\pmb{sl}(2,\mathbb{C})=\pmb{su}(2)\otimes\mathbb{C}=\pmb{su}_\mathbb{C}(2)$. We saw that irreducible representations of $\pmb{sl}(2,\mathbb{C})$ correspond to irreducible representations of $\pmb{su}(2)$. We can therefore consider a complex vector space over the Pauli matrices, allowing us to define:$$\Huge H=\frac{1}{2}\rho_d(\sigma_3),\,\,L_\pm=\frac{1}{2}(\rho_d(\sigma_1)\pm i\rho_d(\sigma_2))$$which obey the algebra:$$\Huge [H,L_\pm]=\pm L_\pm,\,\,[L_+,L_-]=2H$$
> We assume that $w_n$ is an eigenvector of $H$ with eigenvalue $n$, so that $Hw_n=nw_n$, then:$$ HL_+w_n=(L_+H+[H,L_+])w_n=(L_+H+L_+)w_n=(L_+n+L_+)w_n=(n+1)(L_+w_n)$$Which defines $L_+w_n$ as another eigenvector of $H$ with eigenvalue $n+1$. A similar computation shows that $L_-w_n$ is an eigenvector with eigenvalue $n-1$. We therefore call $L_+,L_-$ raising and lowering operators respectively.
> Now we apply our lemma and conclude that $H$ only has real eigenvalues. As we are considering a finite-dimensional vector space, one of these eigenvalues must be the largest. We call such value $m$ with $w_m$ associated eigenvector. Then we must have:$$\Huge L_+w_m=0$$That is, we cannot raise it any more. We then act repeatedly with $L_-$ to produce more eigenvectors with smaller eigenvalues. This must terminate at some point, i.e. for some $d\in\mathbb{Z}, (L_-)^{d+1}w_m=0$. A basis for our representations is therefore:$$\Huge w_{m-l}=(L_-)^lw_m,\,\,l=0,\dots,d$$with dimension $d+1$. 
> To find which values can appear, we introduce:$$\Huge \Delta=\frac{1}{2}(\rho_d(\sigma_1)^2+\rho_d(\sigma_2)^2+\rho_d(\sigma_3)^2)=\frac{1}{2}(L_+L_-+L_-L_+)+H^2$$We know that $\sigma_i^2=\mathbb{1}$ in the defining representation. $\Delta=c\mathbb{1}$ from Schur's lemma follows from observing that:$$\Huge [\Delta,H]=[\Delta,L_\pm]=0$$To fix $c$, we observe that:$$\Huge\begin{align*}
\Delta w_m&=(\frac{1}{2}(L_+L_-+L_-L_+)+H^2)w_m\\
&=(L_-L_++H(H+\mathbb{1}))w_m\\
&=m(m+1)w_m
\end{align*}$$Hence $c=m(m+1)$. As $L_-w_{m-d}=0$ and $L_+L_-=\Delta-H(H-1)$ we have that:$$\Huge\begin{align*}
0&=(\Delta-H(H-\mathbb{1}))w_{m-d}\\
&=(m(m+1)-(m-d)(m-d-1))w_{m-d}\\
&=(1+d)(2m-d)w_{m-d}
\end{align*}$$Implying that $2m-d=0$. As $d\in\mathbb{Z}$ we have that $m$ takes half-integer values. By construction, these are finite dimensional irreducible representations of $\pmb{sl}(2,\mathbb{C})$.
> We can easily restrict all of these matrices appearing in the representation to anti-Hermitian ones to find a representation of $\pmb{su}(2)$. As we have that $\rho(\sigma_i)=\rho(\sigma_i^\dagger)$, we get a representation of $\pmb{sl}(2,\mathbb{C})$ as:$$\Huge \sum_ja_j\rho(\sigma_j),\,\,a_j\in\mathbb{C}$$And a representation of $\pmb{su}(2)$ as:$$\Huge \sum_jia_j\rho(\sigma_j),\,\,a_j\in\Re$$
> In order to compare this with the representations $\rho_d$ of $su(2)$ associated to the representations $r_d$ of $SU(2)$ that we know exists, it is convenient to rescale the basis vectors $w_j$ as follows:$$\Huge L_-v_k=(m+k)v_{k-1}$$Which implies:$$\Huge\begin{align*}
L_+v_k&=\frac{1}{m+k+1}L_+L_-v_{k+1}\\
&=\frac{1}{m+k+1}(\Delta-H(H-1))v_{k+1}\\
&=\frac{1}{m+k+1}(m(m+1)-k(k+1))v_{k+1}\\
&=(m-k)v_{k+1}
\end{align*}$$
> In this basis, the action of $l_i$ is then:$$\Huge\begin{align*}
l_1v_{m-k}&=\frac{i}{2}(L_++L_-)v_{m-k}=\frac{i}{2}(kv_{m-k+1}+(d-k)v_{m-k-1})\\
l_2v_{m-k}&=\frac{1}{2}(L_+-L_-)v_{m-k}=\frac{1}{2}(kv_{m-k+1}-(d-k)v_{m-k-1})\\
l_3v_{m-k}&=iHv_{m-k}=i(m-k)v_{d/2-k}
\end{align*}$$where $m=d/2$ for integer $d$. Comparing with the action we saw before we see that representations are identified with:$$\Huge z_1^kz_2^{d-k}\cong(-1)^kv_{m-k}$$Meaning that all representations of $\pmb{su}(2)$ that we found are the associated representations of the group representations $r_d$ we already found.
> We now show that this representation is irreducible. Take any invariant subspace $V$ of $\Pi_d$. By assumption the action of $l_k$ maps any vector of $V$ to another vector of $V$. As $V$ is a complex vector space, complex linear combinations are again in $V$. This implies that if $P\in V$ we also have that any linear combination of$$\Huge l_+^n=\left(z_2\frac{\partial }{\partial z_1}\right)^nP,\,\,l_-^p=\left(z_1\frac{\partial }{\partial z_2}\right)^pP$$is also in $V$. We can hence apply a suitable power of $l_-$ to map $P$ to the single monomial $z_1^d$. Hence this monomial is in $V$, implying that any complex multiple of it is in $V$ also. We can now use $l_+$ to conclude the same for the other monomial. As these formed a basis of $\Pi_d$, it follows that $V=\Pi_d$. The Lie algebra representations $\rho_d$ are hence irreducible.
> This implies that $r_d$ is irreducible as well. If $W\in\Pi_d$ is an invariant subspace of $r_d$, then it must be invariant under $e^{t\rho(\gamma)}$ for all $t$ and $\gamma\in\pmb{su}(2)$. So in particular under $\frac{\partial }{\partial t}e^{t\rho(\gamma)}$ and hence under $\rho_d(su(2))$. But the Lie algebra representation $\rho$ is irreducible as we already know.
> Now we know that all irreducible representations of $SU(2)$, if there were others, the associated Lie algebra representations would have to have shown up in our analysis.

# Representations of $SO(3)$:

As the Lie algebra of $SO(3)$ is the same as the Lie algebra of $SU(2)$, it will have the same irreducible representations. For the groups, recall that there is a $2$ to $1$ map from $SU(2)$ to $SO(3)$ that mapped $\mathbb{1}\in SU(2)$ and $-\mathbb{1}\in SU(2)$ to $\mathbb{1}\in SO(3)$. We can hence construct representations of $SO(3)$ from representations of $SU(2)$ if $r(-\mathbb{1})=\mathbb{1}$. Therefore we look at the action of $r_d(-\mathbb{1})$ on a monomial:$$\Huge r_d(-\mathbb{1}):z_1^kz_2^{d-k}\rightarrow (-1)^dz_1^kz_1^{d-k}$$This map is the identity if and only if $d$ is an even integer. We have seen that every representation of a Lie group gives us an associated representation of its Lie algebra. The above shows that the converse is not true, the representations of $\pmb{so}(3)$ where $m$ is a half-integer cannot come from any representation of $SO(3)$. On the other hand, we can lift any finite-dimensional representation $R$ of $SO(3)$ to one of $SU(2)$. Hence we have the following theorem:
> The $r_d$ for $d=2m,m\in\mathbb{Z}$ are all of the finite dimensional complex irreducible representations of $SO(3)$

# $SO(3),SU(2)$, and spin:

In physics in $\Re^3$, the half-integer $m$ is called the spin. If there is a physical object that transforms in the representation $r_d$, we say that it has spin $m=d/2$. This applies to both field theories, where $SO(3)$ acts on the components of a field, and to [[Principles of QM|quantum mechanics]], where $SO(3)$ acts on states. If $d=0$ we have a one-dimensional representation that does not transform at all, this is the spin $0$ case. 

An ordinary vector in $\Re^3$ transforms in the three-dimensional representation $r_2$ of $SU(2)$, so you would call a field $\phi=(\phi_1,\phi_2,\phi_3)$ transforming like a vector in $\Re^3$ a vector field as well. Here $m=1$, so this is spin $1$.

It is a fact of nature that there are particles with $1/2$ spin. One way to explain this is that in quantum mechanics, multiplying any state vector by a non-zero complex number does not change the current state. This involves the study of projective representations, which are in one-to-one correspondence with ordinary representations of the associated spin groups in $SO(n)$.

The spinor representation is the $2$ of $SU(2)$, and objects transforming in this representation are called spinors of $SO(3)$. The covering group $SU(2)$ of $SO(3)$ is likewise called the spin group $\text{Spin}(3)$.

We saw earlier that we can map $SU(2)$ to $SO(3)$ for the elements of form:$$\Huge g_{SU(2)}=\begin{pmatrix}e^{i\phi/2} & 0 \\ 0 & e^{-i\phi/2}\end{pmatrix},\,\,g_{SO(3)}=\begin{pmatrix}\cos\phi & \sin\phi & 0 \\ -\sin\phi & \cos\phi & 0 \\ 0 & 0 & 1\end{pmatrix}$$Let us assume we are performing a full rotation using the normal rotation group $SO(3)$ in $\Re^3$. In the corresponding $SU(2)$ matrix, this takes us from $\mathbb{1}$ to $\mathbb{-1}$, that is we do not come back to where we started from and need to let $\phi$ range from $0$ to $4\pi$ to return to $\mathbb{1}$. In this sense, a spinor needs to be rotated by two full rotations.

# Representations of $SU(n)$:

For more general Lie groups such as $SU(n)$, there is a richer representation theory. We already know the defining and the adjoint representations. Instead of developing a general theory, we will discuss how we can create richer representations. 

Given a representation of a group $G$, it is implied that representations of any subgroup $H$ exists by simply restricting the homomorphism $r:G\rightarrow GL(V)$ to $H\subset G$. Every group $SU(n)$ for $n>2$ contains many copies of $SU(2)$ using the operators $H,L_+,L_-$. This motivates us to use the method we did to construct representations of $SU(2)$ to $SU(n)$ by writing the Lie algebra $\pmb{su}(n)$ in terms of number operators $H_i$, lowering operators and raising operators. This is called a Cartan-Weyl basis and leads to root systems, which allow us to classify certain classes of Lie algebras.

# Tensor representations:

Given two vector spaces $V,W$, we can form their tensor product $V\otimes W$. Let $\underline{e}_i,i=1,\dots,\dim V$ be a basis of $V$ and $\underline{f}_j,i=j,\dots,\dim W$ be a basis of $W$. Then $V\otimes W$ is a vector space with basis consisting of tuples $(\underline{e}_i,\underline{f}_j)$, or $\underline{e}_i\otimes\underline{f}_j$

It follows from this definition that $\dim(V\otimes W)=\dim V\cdot\dim W$. Computing with tensor products works almost the same with usual products, we have:$$\Huge\begin{align*}
\underline{v}\otimes\underline{w}+\underline{v}'\otimes\underline{w}&=(\underline{v}+\underline{v}')\otimes\underline{w}\\
\underline{v}\otimes\underline{w}+\underline{v}\otimes\underline{w}'&=\underline{v}\otimes(\underline{w}+\underline{w}')
\end{align*}$$and for $c\in\Re$:$$\Huge c(\underline{v}\otimes\underline{w})=(c\underline{v})\otimes\underline{w}=\underline{v}\otimes(c\underline{w})$$However $\underline{v}\otimes\underline{w}\neq\underline{w}\otimes\underline{v}$. The first slot is reserved for vectors from $V$ and the second for vectors from $W$, so writing $\underline{w}\otimes\underline{v}$ does not make sense if $\underline{v}\in V$ and $\underline{w}\in W$. Not every vector in $V\otimes W$ can be written as a product, for example $\underline{v}\otimes\underline{w}+\underline{v}'\otimes\underline{w}'$.

For example, consider $\Re^3\otimes\Re^3$ and let $e_1,e_2,e_3$ be a basis of the first $\Re^3$ and $f_1,f_2,f_3$ of the second. A basis of $\Re^3\otimes\Re^3$ is then:$$\Huge\begin{align*}
e_1&\otimes f_1,\,\,e_2\otimes f_2,\,\,e_1\otimes f_3\\
e_2&\otimes f_1,\,\,e_2\otimes f_2,\,\,e_2\otimes f_3\\
e_3&\otimes f_1,\,\,e_3\otimes f_2,\,\,e_3\otimes f_3
\end{align*}$$whereas $\Re^3\oplus\Re^3$ has a basis $e_1,e_2,e_3,f_1,f_2,f_3$. Note that whereas $\Re^3\oplus\Re^3$ is six-dimensional, $\Re^3\otimes\Re^3$ is nine-dimensional. 

We can think of $\Re^3\otimes\Re^3$ as the vector space of real $3\times3$ matrices. That is, we can write any element of $\Re^3\otimes\Re^3$ as:$$\Huge \underline{v}=\sum_{ij}a_{ij}e_i\otimes f_j$$What makes tensor products interesting in this context is that we can form new representations our of existing ones by "tensoring" the vector spaces they act on.


## $2\otimes\bar 2$:
Take for example $2\otimes\bar 2$. Here we have a vector space $\mathbb{C}^2$ in the fundamental representation of $SU(2)$, and another $\mathbb{C}^2$ in the anti-fundamental. We then take their tensor product. We ask the question of how $SU(2)$ acts on the tensor product. For a vector in $\mathbb{C}^2$ in the defining representation we have:$$\Huge z\rightarrow gz$$and in the anti-fundamental:$$\Huge z\rightarrow\bar g z$$This is how we would write things in a chosen fixed basis $\underline{v}=(z_1,z_2)$, so we may write this more abstractly as (in the fundamental representation):$$\Huge v=\sum_iz_ie_i\rightarrow g_{ij}z_je_i$$We can think of this as either acting with $g$ on z (active interpretation) or acting with $g^T$ on the tuple of basis vectors (passive interpretation):$$\Huge e_j\rightarrow g_{ij}e_i=g_{ji}^Te_i$$We can use either if we like it, which helps us figure out how to act on elements of $\mathbb{C}^2\otimes\mathbb{C}^2$. As the first copy transforms with $g$ and the second with $\bar g$ we have:$$\Huge v=\sum_ia_{ij}e_i\otimes f_j\rightarrow\sum_{ijkl}a_{ij}(g_{ki}e_k)\otimes(\bar g_{lj}f_l)=\sum_{ijkl}g_{ki}a_{ij}\bar g_{lj}e_k\otimes f_l$$so the vectors in this tensor product behave as:$$\Huge a_{ij}\rightarrow\sum_{kl}g_{ik}a_{kl}g_{lj}^\dagger$$that is, if we collect the $a_{ij}$ in a matrix $A$ we get:$$\Huge A\rightarrow gAg^\dagger$$
## Generalisation:
We can repeat the same logic to find how arbitrary representations acting on vector spaces $V$ and $W$ act on $V\otimes W$:

Let $r_V(G)\in GL(V)$ and $r_W(G)\in GL(w)$, and let the components of these matrices be $r_V(G)_{ij}$ and $r_W(G)_{ab}$. Then the tensor product representation $r_{V\otimes W}$ acts on a vector $\underline{U}\in V\otimes W$ with components $U_{ia}$ as:$$\Huge U_{ia}'=r_V(G)_{ij}r_W(G)_{ab}U_{jb}$$
## $2\otimes\bar 2=1\otimes 3$:
Continuing our example, we know that we can decompose the representations actin on $\mathbb{C}^2\otimes\mathbb{C}^2$ into irreducible representations. As we aw, $SU(2)$ acting on $a_{ij}$ as:$$\Huge A\rightarrow A',\,\,a_{ij}'=g_{ik}a_{kl}(g^\dagger)_{lj},\,\,A\rightarrow A'=gAg^\dagger$$The trace of $A$ hence transforms as:$$\Huge \text{tr}A\rightarrow\text{tr}(gAg^{-1})=\text{tr}A$$Now what this implies is that the representation $2\otimes\bar 2$ is reducible, as we can never map matrices with vanishing trace to ones with a non-vanishing trace. The matrices $A$ have form:$$\Huge A=\begin{pmatrix}a_{11} & a_{12} \\ a_{21} & a_{22}\end{pmatrix}$$and we think of each $a_{ij}$ as components of a vector space $V$ isomorphic to $\mathbb{C}^4$ that we chose to write as a matrix. Within this vector space there is a complex three-dimensional subspace $W$ defined by $a_{11}+a_{22}=0$ and as the above shows, the group action on $V$ maps vectors in $W$ to vectors in $W$ ($W$ is invariant). More concretely, $W$ is the subspace of matrices of the form:$$\Huge W=\left\{A:A=\begin{pmatrix}z_1 & z_2 \\ z_3 & -z_1\end{pmatrix},(z_1,z_2,z_3)\in\mathbb{C}^3\right\}$$Similarly, $W^\perp$ is the one-dimensional subspace containing matrices of form:$$\Huge W^\perp=\left\{A:A=\begin{pmatrix}z_4 & 0 \\ 0 & z_4\end{pmatrix},z_4\in\mathbb{C}\right\}$$which again form an invariant subspace under the group action we defined. The inner form under which this is perpendicular is just the stander inner form on $\mathbb{C}^4$, written as $\langle A,A'\rangle=\sum_{ij}\bar a_{ij}a_{ij}'$ using two matrices $A,A'$. Also note for any $A$ we write:$$\Huge A=\begin{pmatrix}z_1 & z_2 \\ z_3 & -z_1\end{pmatrix}+\begin{pmatrix}z_4 & 0 \\ 0 & z_4\end{pmatrix}$$The above shows that $2\otimes\bar 2$ is not irreducible, but decomposes into a one-dimensional and three-dimensional complex representation. That is we write $2\otimes\bar 2=1^\perp\otimes1$. The only thing remaining to show is that $1^\perp$ transforms in the $3$ of $SU(2)$. The action here is the same as the adjoint representation of $SU(2)$, except that we are acting on a 3 dimensional complex vector space instead of a real one. The irreducibility of the adjoint representation implies that there is no invariant complex subspace if we act on $\mathbb{C}^3$ instead of $\Re^3$, so this is the $3$ of $SU(2)$.

More generally, tensor products can be decomposed into irreducible representations:$$\Huge r_{V\otimes W}(G)=\bigoplus_ir_{V_i}(G)$$whenever we know any representation of $G$ can be decomposed into irreducible representations. The change of basis relating the natural basis of the tensor product to a basis showing the decomposition on the RHS of the above equation is a well-known problem, and the coefficients appearing in the change of basis are called "Clebsch-Gordan coefficients". 

There are a number of examples in physics in which $2\otimes\bar 2=1\otimes3,2\otimes2=1\otimes3$ play an important role in organising degrees of freedom of a theory. Two important ones are explained below: