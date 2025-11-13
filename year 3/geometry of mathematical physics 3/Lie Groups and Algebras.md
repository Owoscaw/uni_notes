# Lie groups:

Lie groups unite the structures of [[Groups|groups]] and [[Differentiable Manifolds#Definition|differentiable manifolds]] in a compatible way. A lie group is a group that is also a differentiable manifold such that the group operations:$$\Huge\begin{align*}
\circ &=G\times G\rightarrow G\;\;\;\;\;\;(x,y)\rightarrow x\circ y\\
{}^{-1} &=G\rightarrow G\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\, x\rightarrow x^{-1}
\end{align*}$$are differentiable maps. 

For example, the group $\mathbb{C}^*=\mathbb{C}\setminus\{0\}$ is a Lie group under multiplication. The map:$$\Huge(x,y)\rightarrow xy$$is a differentiable map from $\mathbb{C}^*\times\mathbb{C}^*$ to $\mathbb{C}^*$, and $x\rightarrow 1/x$ is a differentiable map from $\mathbb{C}^*$ to $\mathbb{C}^*$.

We propose that the group $GL(n,\Re)$ of real invertible $n\times n$ matrices is a Lie group under matrix multiplication. Note that these naturally sit inside $\Re^m$ with $m=n^2$:
> To prove this, recall the definition of a 