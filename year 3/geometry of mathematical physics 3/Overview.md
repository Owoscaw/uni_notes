We explore the structure of our universe by studying group structure and its connection to the standard model. 

We begin by defining Lie groups as a group with smooth, differentiable, group operations. That is, for $x,y\in G$, the maps $(x,y)\rightarrow x\cdot y$ and $x\rightarrow x^{-1}$ must be differentiable. We continue to explore Lie groups as differentiable manifolds, a space that can be covered by a coordinate chart such that the transitions between overlapping charts are smooth. This enables us to use calculus on our groups, allowing us to define paths and tangent vectors. The Lie group formalism provides the global structure of the group, while the Lie algebra determines the local, infinitesimal structure.

We then move on to study representations of groups, formally defined as a group homomorphism $r:G\rightarrow GL(V)$ that assigns an invertible linear map to every group element. These maps are such that the groups abstract relations are preserved in the matrix multiplication of the image:
> The defining, or fundamental, representation of a group is an intrinsic representation available to all Lie groups, where the group acts on its own Lie algebra via conjugation. 
> Faithful representations are such that the homomorphism is injective.
> Trivial representations simply map every element to the identity map.

An important concept in representation theory is the invariant subspace. A subspace $W\subseteq V$ is invariant if acting on any vector in $W$ with any group element results in a vector in $W$. A representation can then be called irreducible if its only invariant subspaces are trivial.

A Lie algebra representation is a homomorphism that preserves the Lie bracket structure. Every group representation uniquely determines a Lie algebra representation $\rho$ through the derivative at the identity:$$\Huge\rho(\gamma)=\frac{d}{dt}r(e^{t\gamma})|_{t=0}$$