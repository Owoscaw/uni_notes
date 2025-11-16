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

For any Lie algebra, we can choose a basis $\{t_a\}_{a=1}^{\dim\pmb g}$ of "generators" $t_a$. In this basis, the Lie bracket reads:$$\Huge[t_a,t_b]=f_{ab}^c\,t_c$$for $a,b,c\in\{1,\dots,\dim\pmb g\}$. Here, $f_{ab}^c$ are called the structure constants. They express the component of the Lie bracket $[t_a,t_b]$ along the generator $t_c$. Note that this uses the [[Index notation#Scalar products|Einstein summation notation]]. The Jacobi identity then implies that:$$\Huge$$