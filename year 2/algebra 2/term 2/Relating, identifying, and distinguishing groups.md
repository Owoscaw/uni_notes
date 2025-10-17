
A homomorphism of [[Basics of groups|group]]s is a map $\varphi:G\rightarrow G'$ between two groups, $G$ and $G'$ such that:$$\Huge \varphi(g_1g_2)=\varphi(g_1)\varphi(g_2)\,\,\forall g_1,g_2\in G$$
An isomorphism of groups is a homomorphism of groups that is bijective. Groups $G,G'$ are isomorphic to each other if there exists an isomorphism between them, in such case we write:$$\Huge G\cong G'$$

The kernel of a group homomorphism is the set:$$\Huge \ker\varphi=\{g\in G:\varphi(g)=e\}$$The image of a group is the set:$$\Huge \text{im }\varphi=\{\varphi(g):g\in G\}$$
Given a group homomorphism $\varphi:G\rightarrow G'$, the kernel $\ker\varphi$ is then a normal [[Basics of groups#Subgroups|subgroup]] of $G$.

# Quotient groups:

Let $N$ be a normal subgroup of $G$. Then we define the quotient group of $G$ with respect to $N$ as the group induced from $G$ on the cosets:$$\Huge G/N=\{gN:g\in G\}$$with the group operation:$$\Huge g_1N\cdot g_2N=g_1g_2N$$To show that this is well defined, we aim to show that for $g_1N=h_1N,g_2N=h_2N$ we have $g_1g_2N=h_1h_2N$. We have that $g_1\in h_1N\implies g_1=h_1n_1$ for some $n_1\in N$. Similarly we have $g_2=h_2n_2$ for some $n_2\in N$. Then:$$\Huge\begin{align}
g_1g_2N&=h_1n_1h_2n_2N\\
&=h_1h_2\tilde n_1n_2N\\
&=h_1h_2N
\end{align}$$So the operation is well defined.
 
# First Isomorphism Theorem for groups:

Let $\varphi:G\rightarrow G'$ be a group homomorphism. Then:$$\Huge G/\ker\varphi\cong\text{im }\varphi$$To prove this, let $\bar\varphi:G/\ker\varphi\rightarrow\,G'$ with $g\cdot\ker\varphi\mapsto\varphi\,g$. We must check that this is well defined, a homeomorphism, and a bijection.

Let $p$ be prime. Then each group $G$ of order $p$ is isomorphic to $(\mathbb{Z}/p,+)$. To prove this, notice that if $|G|=p$ then $G$ is [[Families of groups#Cyclic groups|cyclic]]. We have $G=\langle g\rangle$ where $g^p=e$ and $g^m\neq e$ for $1\leq m\leq p-1$. Consider the map $\varphi:\mathbb{Z}\rightarrow G$ with $m\mapsto g^m$. This is a surjective group homomorphism. Then $\ker\varphi$ is given by all the multiples of $p$, that is:$$\Huge \ker\varphi=p\mathbb{Z}$$now the First Isomorphism Theorem applies and we see that:$$\Huge \mathbb{Z/}p\mathbb{Z}\cong\,G$$
Each cyclic group of order $n$ is isomorphic to $(\mathbb{Z}/n,+)$ and each infinite cyclic group is isomorphic to $(\mathbb{Z},+)$. The proof of these statements is similar to the above.

# Direct products of groups:

The direct product $G\times H$ of two groups is also a group:$$\Huge G\times H=\{(g,h):g\in G,h\in H\}$$The group structure is induced from $G$ and $H$:
> $(g_1,h_1)\circ(g_2,h_2)=(g_1g_2,h_1h_2)$
> $e_{G\times H}=(e_G,e_H)$
> $(g,h)^{-1}=(g^{-1},h^{-1})$

There is an isomorphism between $\mathbb{Z}/2\times\mathbb{Z}/3$ and $\mathbb{Z}/6$. Such an isomorphism is defined by:$$\Huge\begin{align}
\mathbb{Z}/6&\rightarrow\mathbb{Z}/2\times\mathbb{Z}/3\\
\bar 1&\mapsto(\bar 1,\bar 1)\\
a\mod 6&\mapsto(a\mod 3,a\mod 3)
\end{align}$$
For $m,n\geq1$ we have:$$\Huge \mathbb{Z}/mn\cong\mathbb{Z}/m\times\mathbb{Z}/n\iff\gcd(m,n)=1$$To prove this, take $I=(m)_\mathbb{Z},J=(n)_\mathbb{Z},I+J=\mathbb{Z}$ and let $d=\gcd(m,n)>1$. We put $m'=m/d,n'=n/d$. Then we aim to prove that any element in $\mathbb{Z}/m\times\mathbb{Z}/n$ has order dividing $(mn)/d=m'n'd$. This is equivalent to the statement:$$\Huge m'n'd(\bar a,\bar b)=(m'n'd\bar a,m'n'd\bar b)=(n'(m\bar a),m'(n\bar b))=(\bar 0,\bar 0)$$by definition. So we see that $mn$ is the order of any element in the group, proving the statement as required?

An isomorphism preserves:
> The order of a group
> The set of orders of elements
> The size of its center
> The property of being abelian
> The property of having proper subgroups and their sizes

Note that for two subsets $E_1,E_2$ of a group $G$ we write:$$\Huge E_1\circ E_2=\{a\circ b:a\in E_1,b\in E_2\}$$With this, let $H$ and $K$ be two subgroups of $G$ such that the following hold:
> $H\circ K=G$
> $H\cap K=\{e\}$
> $hk=kh\,\,\forall h\in H,\forall k\in K$

Then we have:$$\Huge G\cong H\times K$$
# Groups as permutation groups:

The group of rotational symmetries of the unit cube in $\Re^3$ is isomorphic to [[Families of groups#Permutation groups|$S_4$]].

# Cayley's Theorem:

Each group $G$ is isomorphic to a subgroup of some permutation group $S_X$. In fact, such $X$ can be taken to be the set $G$.

To prove this, assign a permutation of $G$ to each $g\in G$ by "left translation":$$\Huge L_g:G\rightarrow G,\,\,h\mapsto g\circ h$$for all $h\in G$. We must first check that $L_g$ is a bijection, so assume $L_g(h_1)=L_g(h_2)$ for $h_1,h_2\in G$. Then we have $gh_1=gh_2\implies h_1=h_2$ by applying $g^{-1}$ from the left. So we have injectivity, we move on to show surjectivity. Assume $k\in G$ and write $L_g(h)=k$ for some $h\in G$. Then we have $gh=k$ and putting $h=g^{-1}k$ we have surjectivity. Now write:$$\Huge G'=\{L_g\in S_G:g\in G\}\subset S_G$$We must then show that $G'<S_G$ with the binary operation induced from $S_G$:
>$G'\neq\emptyset$ as we have $L_e=e_{S_G}$
>$G'$ is closed under composition of bijections as for $L_g,L_h\in G'$ for $g,h\in G$ we have, for all $a\in G$, $L_g\circ L_h(a)=L_g(ha)=g(ha)=(gh)a=L_{gh}(a)$
>$G'$ is closed under inverses as $L_g\circ L_{g^{-1}}(a)=L_g(g^{-1}a)=g(g^{-1}a)=a$ for all $a\in G$

So we have that:$$\Huge\begin{align}
\psi:G&\rightarrow G'\\
g&\mapsto L_g
\end{align}$$is a group homomorphism. We claim that $\psi$ is indeed an isomorphism of groups. $\psi$ is trivially surjective so we only show injectivity. Assume $\psi(g)=\psi(h)$, then $L_g(a)=L_h(a)$ for all $a\in G$. Now we have $ga=ha$, taking $a=e$ we get injectivity, showing that $\psi$ is a group isomorphism as required.