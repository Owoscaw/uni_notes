# Lie groups:

Lie groups unite the structures of [[Groups|groups]] and [[Differentiable Manifolds#Definition|differentiable manifolds]] in a compatible way. A lie group is a group that is also a differentiable manifold such that the group operations:$$\Huge\begin{align*}
\circ &=G\times G\rightarrow G\;\;\;\;\;\;(x,y)\rightarrow x\circ y\\
{}^{-1} &=G\rightarrow G\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\, x\rightarrow x^{-1}
\end{align*}$$are differentiable maps.

For example, the group $\mathbb{C}^*=\mathbb{C}\setminus\{0\}$ is a Lie group under multiplication. The map:$$\Huge(x,y)\rightarrow xy$$is a differentiable map from $\mathbb{C}^*\times\mathbb{C}^*$ to $\mathbb{C}^*$, and $x\rightarrow 1/x$ is a differentiable map from $\mathbb{C}^*$ to $\mathbb{C}^*$.

We propose that the group $GL(n,\Re)$ of real invertible $n\times n$ matrices is a Lie group under matrix multiplication. Note that these naturally sit inside $\Re^m$ with $m=n^2$:
> To prove this, recall that a map is differentiable if it can be locally approximated by a linear map. We ask if this is true for matrix multiplication. For two matrices $P,Q\in GL(n,\Re)$, the group operation is the map:$$\Huge (P,Q)\rightarrow PQ$$
> To examine if this can be approximated by a linear map we change $P$ to $P+\Delta_P$ and $Q$ to $Q+\Delta_Q$:$$\large\begin{align*}
(P+\epsilon\Delta_P,Q+\epsilon\Delta_Q)\rightarrow(P+\epsilon\Delta_P)(Q+\epsilon\Delta_Q)&=PQ+P\epsilon\Delta_Q+\epsilon^2\Delta_P\Delta_Q\\
&\approx\,PQ+\epsilon(P\Delta_Q+\Delta_PQ)
\end{align*}$$which is linear in both $\Delta_P$ and $\Delta_Q$. [[Determinants and Adjoints#Cramer's rule|Cramer's rule]] for constructing inverse matrices similarly shows that $P\rightarrow P^{-1}$ is differentiable.
> Note that closed subgroups $H$ of $GL(n,\Re)$ are again Lie groups, called matrix Lie groups.

This is allows us to find more Lie groups in the form of closed subgroups of $GL(n,\Re)$:
> The orthonormal group $O(n)$ is the group of real $n\times n$ matrices $g$ such that:$$\Huge g^Tg=\mathbb{1}$$The special orthogonal group $SO(n)$ is the subgroup of matrices in $O(n)$ that have determinant $\det g=1$. We propose that both of these are Lie groups. One can prove that these are groups, and are obviously subgroups of $GL(n,\Re)$. The conditions that $g$ has to satisfy in order to be in $O(n)$ only hold true on the closed subset where the defining relation $g^Tg=\mathbb{1}$ holds true. That is, for any matrix that does not satisfy these equations, we can find a ball $GL(n,\Re)$ such that $g^Tg\neq\mathbb{1}$ for every member of this balls. The complement of $O(n)$ in $GL(n,\Re)$ is therefore open, meaning that $O(n)$ is closed. The same argument for $SO(n)$ holds, making both groups Lie groups. Remarks:
> > For $g\in O(n)$ it follows that $\det(g^Tg)=(\det g)^2=\det\mathbb{1}=1$. As $g$ is a real matrix, we hence have that $\det g=\pm 1$. The space of such matrices is hence disjoint with two components, the one containing $\mathbb{1}$ is called $SO(n)$ and is a subgroup. The other component is not a subgroup.
> > Conditions such as $g^Tg=\mathbb{1}$ and $\det g=1$ are typically called "closed conditions" as the sets they define are closed sets in the vector space of all matrices.
> The unitary group $U(n)$ is the group of complex $n\times n$ matrices $g$ such that $U^\dagger U=\mathbb{1}$. The special unitary group $SU(n)$ is the subgroup of matrices in $U(n)$ that have determinant $\det g=1$. Note that this group is simply that containing invertible maps acting on a [[Inner product spaces#Complex inner products|complex vector space]] such that the canonical inner form stays invariant:$$\Huge \bar x\cdot y\rightarrow\bar x'\cdot y'=\bar xg^Tgy=\bar xg^\dagger gy=\bar x\cdot y$$It is therefore immediate that these are Lie groups as these are both closed subgroups of $GL(2n,\Re)$ by identifying $\mathbb{C}$ with $\Re^2$.

# Lie algebras:

The idea of a Lie algebra is to formalise the notion of infinitesimal transformations. We first define the Lie algebras abstractly. A Lie algebra is a $\pmb g$ is a [[Vector space definitions|vector space]] together with a bilinear map, or Lie bracket:$$\Huge[\cdot,\cdot]:\pmb g\times\pmb g\rightarrow\pmb g$$that is antisymmetric $[x,y]=-[y,x]$ and satisfies the Jacobi identity:$$\Huge [x,[y,z]]+[y,[z,x]]+[z,[x,y]]=0$$for all $x,y,z\in\pmb g$. Every Lie group comes equipped with a Lie algebra which is equal to its [[Differentiable Manifolds#Paths|tangent space]] at the identity element:$$\Huge\pmb g=T_\mathbb{1}G$$
This is already a vector space by construction, so to prove this we notice that for matrix Lie groups we can simply take the bilinear form $[,]$ to be the commutator. This clearly satisfies the Jacobi identity. It remains to be shown that the commutator of two Lie algebra elements indeed returns a Lie algebra element, which is proven later on.

A corollary of this definition is that the dimension of the Lie algebra as a vector space is equal to the dimension of its Lie group as a differentiable manifold. Examples:
> The Lie algebra $\pmb u(1)$ of $U(1)$ are the purely imaginary numbers and $[\gamma,\gamma']=0$ for all $\gamma,\gamma'\in\pmb u(1)$.
> The Lie algebra of $\mathbb{C}^*$ are the complex numbers and $[\gamma,\gamma']=0$ for all $\gamma,\gamma'$ in the lie algebra $\pmb c^*$ of $\mathbb{C}^*$.
> The lie algebra $\pmb{su}(n)$ of $SU(n)$ is a real vector space with basis formed by the complex $n\times n$ matrices $\gamma$ such that $\gamma^\dagger=-\gamma$ and $\text{tr}(\gamma)=0$. Note that for $n=2$, we [[U(1),SU(2),SO(3)#$SU(2)$|showed]] that $i\sigma_j$ for each Pauli matrix $\sigma_i$ formed a basis of $SU(2)$. For general $n$, we can easily see that $\dim\pmb{su}(n)=n^2-1$ when interpreting the algebra as a real vector space:
> > There are $n$ purely imaginary numbers on the diagonal and $n(n-1)/2$ complex numbers, and hence $n(n-1)$ real numbers above the diagonal.
> > Due to the anti-hermicity condition the numbers below the diagonal are then uniquely fixed.
> > The tracelessness condition tells us that out of $n^2$ real numbers, one of them can be fixed, showing that indeed $\dim\pmb{su}(n)=n^2-1$
> We saw that $SU(2)$ is a double cover of $SO(3)$, meaning that a small neighbourhood around the identity in $SU(2)$ is isomorphic to a small neighbourhood of the identity in $SO(3)$. These groups therefore have isomorphic Lie algebras.

For any Lie algebra, we can choose a basis $\{t_a\}_{a=1}^{\dim\pmb g}$ of "generators" $t_a$. In this basis, the Lie bracket reads:$$\Huge[t_a,t_b]=f_{ab}^c\,t_c$$for $a,b,c\in\{1,\dots,\dim\pmb g\}$. Here, $f_{ab}^c$ are called the structure constants. They express the component of the Lie bracket $[t_a,t_b]$ along the generator $t_c$. Note that this uses the [[Index notation#Scalar products|Einstein summation notation]]. The Jacobi identity then implies that:$$\Huge f_{ab}^df_{dc}^e+f_{bc}^df_{da}^e+f_{ca}^df_{db}^e=0$$for the structure constants.

For example, a basis for the Lie algebra $\pmb{su}(2)$ of $SU(2)$ is given by $t_a=i\sigma_a$ for $\sigma_a$ representing the Jacobi matrices. We can show that:$$\Huge [i\sigma_a,i\sigma_b]=-[\sigma_a,\sigma_b]=-2\epsilon_{abc}i\sigma_c$$so we can conclude that $f_{ab}^c=-2\epsilon_{abc}$ for $\pmb{su}(2)$.

## Exponential map:
Elements of the Lie algebra are associated with elements of the tangent space of $G$ at the identity and we can think of both Lie algebra and Lie group elements as matrices that can be multiplied. For any $\gamma\in T_\mathbb{1}(G)$ it can be shown that:$$\Huge L(\gamma)|_g=g\gamma$$is a tangent vector at $g$ for any $g\in G$. This defines a so called vector field $L(\gamma)$ that is left-invariant, meaning:$$\Huge g'L(\gamma)|_g=g'g\gamma=L(\gamma)|_{g'g}$$An important property of vector fields is that one can "flow" along them. For example, flowing out from the identity is done by solving:$$\Huge \frac{\partial g(t)}{\partial t}=L(\gamma)|_{g(t)}=g(t)\gamma$$The solution to this is to follow a path:$$\Huge g(t)=e^{t\gamma}$$

Let $G$ be a lie group and $\pmb g$ be its Lie algebra. Then we have:
> $g\gamma g^{-1}\in\pmb g$ for all $\gamma\in\pmb g$ and $g\in G$. To prove this, we construct a path that gives $g\gamma g^{-1}$ as a tangent vector upon differentiation:$$\Huge e^{tg\gamma g^{-1}}=\sum_{k=0}^\infty\frac{(gtg^{-1})^k}{k!}=g\left(\sum_{k=0}^\infty\frac{(t\gamma)^k}{k!}\right)g^{-1}=ge^{t\gamma}g^{-1}$$As the RHS is obviously a path in $G$ (all factors are in $G$), and passes through $\mathbb{1}$ at $t=0$ and:$$\Huge\frac{\partial }{\partial t}(ge^{t\gamma}g^{-1})|_{t=0}=g\gamma g^{-1}$$it follows that $g\gamma g^{-1}\in\pmb g$.
> $[\gamma,\delta]\in\pmb g$ for all $\gamma,\delta\in\pmb g$. To prove this, consider $e^{t\gamma}\delta e^{-t\gamma}$ for $\delta\in\pmb g$. It follows from the first point that this is in $\pmb g$ for all $t$. As a tangent space, the Lie algebra sits inside a particular $n$-dimensional vector space which will sit inside the vector space of $n\times n$ matrices. Therefore it is closed under limits and:$$\Huge \lim_{t\to 0}(e^{t\gamma}\delta e^{-t\gamma}-\delta)/t=\gamma\delta-\delta\gamma=[\gamma,\delta]\implies[\gamma,\delta]\in\pmb{g}$$

Note that the exponential map is not always injective and surjective. We already saw injectivity fail when considering $U(1)$ and $SU(2)$. Consider the following counterexample that shows that surjectivity can fail:
> Elements of the Lie algebra $\pmb{sl}(2,\Re)$ of $SL(2,\Re)$ must obey $e^\gamma=g$ for $g\in SL(2,\Re)$. This implies that $\gamma$ is real by taking complex conjugation. Furthermore:$$\Huge \det e^\gamma=e^{\text{tr}(\gamma)}=1$$implies that $\gamma$ is traceless. Therefore $e^\gamma$ always maps to $SL(2,\Re)$ if the Lie algebra contains traceless, real matrices. Now consider the group element:$$\Huge g=\begin{pmatrix}-4 & 0 \\ 0 & -1/4\end{pmatrix}\in\,SL(2,\Re)$$If an element $\gamma\in\pmb{sl}(2,\Re)$ exists such that $e^\gamma=g$ then we could simply write $\sqrt g=e^{\frac{1}{2}\gamma}$. The eigenvalues of $g$ are $4,1/4$, so the eigenvalues of $\sqrt g$ are therefore $\pm2i,\pm\frac{1}{2}i$. However for $\sqrt g$ to be in $SL(2,\Re)$, it must be a purely real matrix, corresponding to the fact that eigenvalues are given by:$$\Huge \lambda_\pm=-p/2\pm\sqrt{(p/2)^2-q}$$with $p,q\in\Re$. Therefore there must be two eigenvalues that are either real or complex conjugates of each other. This is not true for the matrix we have chosen, showing that no such $\gamma$ exists.

If $G$ is a [[Connectedness|connected]], [[Compactness|compact]] matrix Lie group, the exponential map for $G$ is surjective. To prove this, observe the methodology used to show that the map is surjective for $U(1)$. Then show that for any compact matrix Lie group $G$, every element $g\in G$ lies inside some $U(1)$ subgroup of $G$. This is known as the torus theorem. Once it is established, simply use the generators of $U(1)$ to reach $g$ via the exponential map.

# Classification of compact Lie algebras:

Lie algebras of compact Lie groups are called compact Lie algebras:
> An ideal of a Lie algebra is a subset $I\subset\pmb g$ such that $[l,x]\subset I$ for all $l\in I$ and $x\in G$
> A simple Lie algebra is a Lie algebra with no non-trivial ideals

Any compact Lie algebra can be decomposed into the direct sum of $u(1)$ Lie algebras and of simple Lie algebras:$$\Huge\pmb g=u(1)\oplus\dots\oplus u(1)\oplus\pmb g_1\oplus\dots\oplus\pmb g_l$$
