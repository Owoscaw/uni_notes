
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
