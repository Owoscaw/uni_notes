A linear map from [[Real vector spaces|vector spaces]] $V$ to $W$ is a function $T:V\mapsto W$ that satisfies the following properties, where $+_v,+_w$ denotes addition in $V$ and $W$ respectively :
> $T(\underline v_1 +_v\underline v_2)=T(\underline v_1)+_wT(\underline v_2)\,\,\forall\underline v_1,\underline v_2\in V$ 
> $T(\lambda\underline v)=\lambda T(\underline V)\,\,\forall\lambda\in\Re,\underline v\in V$

Note also that $0$ must be sent to $0$, that is:$$\Huge T(\underline 0_v)=T(0\cdot\underline 0_v)=0\cdot T(\underline 0_v)=\underline 0_w$$
For example, suppose that $A\in M_{m\times n}(\Re)$. We then defined $T=T_A:\Re^n\mapsto\Re^n,\,T:\underline v\mapsto A\underline v$. We can then check this:
>$T(\underline v_1+\underline v_2)=A(\underline v_1+\underline v_2)=A\underline v_1+A\underline v_2=T(\underline v_1)+T(\underline v_2)$. We know this from the distributive law of matrix multiplication. This linear map holds under addition.
>$T(\lambda\underline v)=A(\lambda\underline v)=\lambda(A\underline v)=\lambda T(\underline v)$. We know this from the commutative law of scalar multiplication for matrices. This linear map holds under scalar multiplication.

Suppose vector spaces $V$ and $W$ and let $\{\underline v_1,\dots,\underline v_n\}$ be a basis for $V$. Then we have:
> A linear map $T:V\mapsto W$ is determined by its values on the basis, $T(\underline v_1),\dots,T(\underline v_n)$.
> Conversely, given arbitrary vectors $\underline w_1,\dots,\underline w_n\in W$ there exists a linear map $T:V\mapsto W$ with $T(\underline v_1)=w_1,\dots,T(\underline v_n)=w_n$.

Suppose $\underline v\in V$, then $\underline v$ can be written as $\underline v=\lambda_1\underline v_1+\dots+\lambda_n\underline v_n$ for some $\lambda_i\in\Re$, so $T(\underline v)=T(\lambda_1\underline v_1+\dots+\lambda_n\underline v_n)=\lambda_1T(\underline v_1)+\dots+\lambda_nT(\underline v_n)$. So the map is fully characterised by $T(\underline v_1),\dots,T(\underline v_n)$, as any vector that undergoes this map is expressed as a linear combination of basis elements that have undergone the map. For the second part of the proof, note that the linear combination of basis elements uniquely defines any $v\in V$. So we define:$$\Huge T(\underline v)=\lambda_1\underline w_1+\dots+\lambda_n\underline w_n$$This shows that $T$ is well defined, by the uniqueness of each $\lambda_i\in\Re$. If $\underline u_1,\underline u_2\in V,\lambda,\mu\in\Re$, then suppose that $\underline u_1=\lambda_1\underline v_1+\dots+\lambda_n\underline v_n$ and $\underline u_2=\mu_1\underline v_1+\dots+\mu_n\underline v_n$. Then $T(\underline u_1+\underline u_2)=T((\lambda_1+\mu_1)\underline v_1+\dots+(\lambda_n+\mu_n)\underline v_n)=(\lambda_1+\mu_1)\underline w_1+\dots+(\lambda_n+\mu_n)\underline w_n=T(\underline u_1)+T(\underline u_2)$. We also have that $T(\lambda\underline u_1)=\lambda T(\underline u_1)$, so the map is linear.


A map $T:\Re^m\mapsto\Re^n$ is linear if and only if there is a matrix $A\in M_{n\times m}(\Re)$ such that $T(\underline x)=A\underline x$ for all $x\in\Re^m$. Note that $T:\underline x\mapsto A\underline x$ is linear. Suppose that this transformation is linear, then:$$ T\begin{pmatrix}\lambda_1\\\vdots\\\lambda_m\end{pmatrix}=T(\lambda_1\underline e_1+\dots+\lambda_m\underline e_m)=\lambda_1T(\underline e_1)+\dots+\lambda_mT(\underline e_m)=\begin{pmatrix}T(\underline e_1)&\dots&T(\underline e_m)\end{pmatrix}\begin{pmatrix}\lambda_1\\\vdots\\\lambda_m\end{pmatrix}$$
So let $A$ be this LHS matrix, then we have:T(λ1⋮λm)=A(λ1⋮λm)
This is a known linear map, so this map $T$ must also be linear.

# Properties of linear maps:

Suppose $T:U\mapsto V$, $S:V\mapsto W$ are linear maps. Then the composition $S\circ T:U\mapsto W$ is also linear. In particular, when $U=\Re^u,V=\Re^v,W=\Re^w$ and $T,S$ are represented by $A\in M_{v\times u},B\in M_{u\times w}(\Re)$ respectively, we have:(S∘T)(x)=(BA)x,BA∈Mw×uProven as follows: Let $\underline u_1,\underline u_2,\underline u\in U_1,\lambda\in\Re$. Then $(S\circ T)(\underline u_1+\underline u_2)=S(T(\underline u_1+\underline u_2))=S(T(\underline u_1)+T(\underline u_2))=S(T(\underline u_1))+S(T(\underline u_2))=S\circ T(\underline u_1)+S\circ T(\underline u_2)$, showing that $S\circ T$ is closed under addition. Also $S\circ T(\lambda\underline u)=S(T(\lambda\underline u))=S(\lambda T(\underline u))=\lambda S(T(\underline u))=\lambda S\circ T(\underline u)$, showing that $S\circ T$ is also closed under scalar multiplication. So $S\circ T$ is also a linear map.

For the statement with real vector spaces we have:(S∘T)(x―)=S(T(x―))=S(Ax―)=B(Ax―)=(BA)x―By associativity of matrix multiplication, we have that $S\circ T$ represents the composition of two linear maps.

# Isomorphism:

If $T:V\mapsto W$ is a linear map, we call $T$ an isomorphism if and only if $T$ is [[Functions, Domain and Range#Bijectivity|bijective]]. In this case we call $V$ and $W$ isomorphic and write $V\cong W$. We then suppose that if $T$ is isomorphic, then $T^{-1}:W\mapsto V$ is also isomorphic. This transformation is obviously bijective, but it is not obvious that it is linear, so we let $\underline w_1,\underline w_2,\underline w\in W,\lambda\in\Re$ and show:
> $\underline v_1=T^{-1}(\underline w_1),\underline v_2=T^{-1}(\underline w_2)\implies T(\underline v_1)=\underline w_1,T(\underline v_2)=w_2$ so we then write:$$\Huge T(\underline v_1+\underline v_2)=T(\underline v_1)+T(\underline v_2)=\underline w_1+\underline w_2$$$$\Huge \underline v_1+\underline v_2=T^{-1}(\underline w_1+\underline w_2)=T^{-1}(\underline w_1)+T^{-1}(\underline w_2)$$Now we set $\underline v=T^{-1}(\underline w)$. Then:$$\Huge T(\lambda\underline v)=\lambda T(\underline v)=\lambda\underline w\implies\lambda T^{-1}(\underline w)=\lambda\underline v=T^{-1}(\lambda\underline w)$$
> Therefore $T^{-1}$ is also a linear map.



Suppose that $V$ has a basis $\{\underline v_1,\dots,\underline v_n\}$. Then the coordinate map $\Phi:V\mapsto\Re^n$ is an isomorphism:$$\Huge \lambda_1\underline v_1+\dots+\lambda_n\underline v_n=\begin{pmatrix}\lambda_1\\\vdots\\\lambda_n\end{pmatrix}$$
We know that $\Phi$ is linear, so we check that it is bijective:$$\Huge \text{If}\,\,\begin{pmatrix}\lambda_1\\\vdots\\\lambda_n\end{pmatrix}\in\Re^n\,\,\text{then}\,\,\Phi(\lambda_1\underline v_1+\dots\lambda_n\underline v_n)=\begin{pmatrix}\lambda_1\\\vdots\\\lambda_n\end{pmatrix}$$Also if $\underline v,\underline w\in V$ where $\underline v\neq\underline w$, then if $\underline v=\lambda_1\underline v_1+\dots+\lambda_n\underline v_n$ and $\underline w=\mu_1\underline v_1+\dots+\mu_n\underline v_n$ then for at least one $i,\lambda_i\neq\mu_i$. This implies that $\Phi(\underline v)$ and $\Phi(\underline w)$ differ in the $i$th dimension.

In order to transform a vector in $\Re^n$ to a vector in $\Re^m$, the following diagram can be used:![[vector space transformation example]]
Let $A$ be such transformation. $A$ is then defined by $\Psi\circ T\circ\Phi^{-1}$. We give this transformation form:$$\Huge A:\Re^n\mapsto\Re^n:\underline x\mapsto A\underline x:A\in M_{m\times n}(\Re)$$Given bases for $U$ and $V$, coordinate maps are defined as $\Phi:U\xrightarrow{\cong}\Re^n$ and $\Psi:V\xrightarrow{\cong}\Re^m$. Suppose that $T:U\mapsto V$ is linear, then the matrix that maps this transformation is known as the matrix of $T$ with respect to the bases of $U$ and $V$. This matrix is given by:$$\Huge A=\begin{pmatrix}\Psi T(\underline u_1)&\Psi T(\underline u_2)&\dots&\Psi T(\underline u_n)\end{pmatrix}$$Where $\{\underline u_1,\dots,\underline u_n\}$ is the basis of $U$.

# Image, rank, kernel, nullity:

Given a linear map $T:U\mapsto V$, we define the image of $T$:$$\Huge im(T):=\{T(\underline u):\underline u\in U\}\subseteq V$$And the kernel of $T$:$$\Huge ker(T):=\{\underline u\in U:T(\underline u)=\underline0\}\subseteq U$$These are proven to be subsets as follows: Suppose $\underline v,\underline v_1,\underline v_2\in im(T)$ and $\underline u,\underline u_1,\underline u_2\in ker(T)$ and $\lambda\in\Re$. Then we define $\underline v=T(\underline w),\underline v_1=T(\underline w_1),\underline v_2=T(\underline w_2)$ for some $\underline w,\underline w_1,\underline w_2\in U$. So:
> $\underline v_1+\underline v_2=T(\underline w_1)+T(\underline w_2)=T(\underline w_1+\underline w_2)\in im(T)$
> $\lambda\underline v=\lambda T(\underline w)=T(\lambda\underline w)\in im(T)$
> So we have that $im(T)$ is closed under addition and scalar multiplication.
> $T(\underline u_1+\underline u_2)=T(\underline u_1)+T(\underline u_2)=\underline 0+\underline 0=\underline 0$
> So $\underline u_1+\underline u_2\in ker(T)$, similarly $T(\lambda\underline u)\in ker(T)$
> We have that both $im(T)$ and $ker(T)$ are closed under addition and scalar multiplication. These spaces by definition contain $\underline 0$, so this makes them vector subspaces.

Generalising this, we have that for a linear map $T:V\mapsto W$ and a basis for $V$ of $\{v_1,\dots,v_n\}$, then we get that:$$\Huge im(T)=span(T(v_1),\dots,T(v_n))$$
The proof of this is immediate. We also have that the following are pairwise equivalent:
>$ker(T)=\{0\}$
>$T$ is injective
>For linearly independent vectors $v_1,\dots,v_n\in V$, then the images $T(v_1),\dots,T(v_n)$ are linearly independent in $W$

This is proven as follows. Assume that $ker(T)=\{0\}$ and assume that $T(v_1)=T(v_2)$ for some $v_1,v_2\in V$, that is $T$ is not injective. Then $0=T(v_1)-T(v_2)=T(v_1-v_2)$, but since $ker(T)=\{0\}$ then we get $v_1=v_2$, a contradiction. This implies that if $ker(T)=\{0\}$ then $T$ is injective. Now we assume that $T$ is injective. Consider $\lambda_1T(v_1)+\dots+\lambda_kT(v_k)=0\implies T(\lambda_1v_1+\dots+\lambda_kv_k)=0$. Since $T$ is injective and $T(0)=0$ we must have that $\lambda_1v_1+\dots+\lambda_kv_k=0$. Since these vectors are linearly independent, we see that the only solution is $\lambda_1=\dots=\lambda_k$, so the images of these vectors also satisfy linear independence. Now we can assume the statement just proven. Suppose that $T(v)=0$, now $\{T(v)\}$ is not linearly independent as we can write that for any $\lambda\in\Re$, $\lambda T(v)=\lambda0=0$. Therefore $\{v\}$ cannot be linearly independent, so we get that the only vector in $V$ that satisfies $T(v)=0$ is $v=0$, showing that $ker(T)=\{0\}$.

The above has a corollary where for a linear map $T:V\mapsto W$ where $ker(T)=\{0\}$. Assume $dim(V)=n$ with basis $\{v_1,\dots,v_n\}$. Then we have that $\{T(v_1),\dots,T(v_n)\}$ are a basis for $im(T)$, in particular:$$\Huge dim(im(T))=dim(V)$$Leading to the definitions:$$\Huge rk(T):=dim(im(T)),\,\,null(T):=dim(ker(T))$$

On the same vector spaces define the maps $\phi:V'\mapsto V$, $\psi:W\mapsto W'$ such that both are isomorphic. Then:$$\Huge rk(\psi\circ T\circ\phi)=rk(T),\,\,null(\psi\circ T\circ\phi)=null(T)$$Since $\phi$ is a bijection, then $im(\phi)=V$, hence $im(\psi\circ T\circ\phi)=\psi(im(T))$. But since $ker(\psi)=\{0\}$, applying $\psi$ does not change the rank of the image by the above corollary. Another consequence of this is that $ker(\psi\circ T\circ\phi)=ker(T\circ\phi)$. This is the set of vectors $v'\in V'$ such that $T(\phi(v'))=0$, that is the set of points in the kernel of $T$ that are of form $\phi(v')$. Thus $ker(\psi\circ T\circ\phi)=\phi^{-1}(ker(T))$, by the same argument as before this has the same dimension of $ker(T)$, giving us the result above. This can be used with the [[Real vector spaces#Rank theorem|rank nullity theorem]] of matrices to determine the rank and nullity of associated linear maps:

## Rank nullity for linear maps:

Let $V,W$ be two finite dimensional vector spaces with $T:V\mapsto W$ then we propose:$$\Huge dim(V)=rk(T)+null(T)$$
$T$ can be viewed as a linear map from $\Re^n$ to $\Re^m$ for some $n,m$. This means that $T$ can be represented by a matrix $A\in M_{m\times n}(\Re)$. The coordinate maps must be isomorphisms, so the rank and nullity of the map is unchanged under any associated coordinate map. Thus the statement above immediately follows from the rank nullity theorem for matrices. This can also be argued directly:![[rank nullity for maps]]
Finally, we can completely categorise vector spaces by their dimension. For two finite dimensional vector spaces, $V$ and $W$ we have:$$\Huge V\cong W\iff dim(V)=dim(W)$$
This is because if $T:V\mapsto W$ is an isomorphism then $ker(T)=\{0\}$ and $im(T)=W$. By rank nullity, $dim(V)=dim(W)$. Conversely, if their dimension is equal then suppose that each space has a basis $\{v_1,\dots,v_n\}$ and $\{w_1,\dots,w_n\}$ respectively. Then define a map $V\mapsto W$ such that $v_i\mapsto w_i$ and $W\mapsto V$ such that $w_i\mapsto v_i$. Each of these is the inverse of the other, and hence isomorphisms. This shows that any two vector spaces of the same dimension are essentially the same space.

# Change of basis and of coordinates:

Let $T:\Re^n\mapsto\Re^m$ be a linear map. Suppose that with respect to the standard bases, $T$ is represented by a matrix $A$. Let $S=\{v_1,\dots,v_n\}$ be a basis of $\Re^n$ and let $P=(v_1,\dots,v_n)$. Let $S'=\{w_1,\dots,w_m\}$ be a basis for $\Re^m$ and let $Q=(w_1,\dots,w_m)$. Then with respect to $S$ and $S'$, then $T$ is represented by $B=Q^{-1}AP$, proven as follows:

Suppose that $x\in\Re^n$ is given with respect to the standard basis:$$\Huge x=x_1e_1+\dots+x_ne_n=\begin{pmatrix}x_1\\\vdots\\x_n\end{pmatrix}$$This can then be given with respect to $\{v_1,\dots,v_n\}$:$$\Huge x=\tilde x_1v_1+\dots+\tilde x_nv_n=\tilde x_1P(e_1)+\dots+\tilde x_nP(e_n)=P(\tilde x_1e_1+\dots+\tilde x_ne_n)$$So we can write this as:$$\Huge \begin{pmatrix}x_1\\\vdots\\x_n\end{pmatrix}=P\begin{pmatrix}\tilde x_1\\\vdots\\\tilde x_n\end{pmatrix}$$Similarly, $y\in\Re^m$ can be represented with respect to the two bases:$$\Huge \begin{pmatrix}y_1\\\vdots\\y_m\end{pmatrix}=Q\begin{pmatrix}\tilde y_1\\\vdots\\\tilde y_m\end{pmatrix}$$Suppose that $y=T(x)$, then a coordinate in $\Re^m$ can be represented as a coordinate in $\Re^n$:$$\Huge \begin{pmatrix}y_1\\\vdots\\y_m\end{pmatrix}=A\begin{pmatrix}x_1\\\vdots\\x_n\end{pmatrix}$$Putting all of this together gives:$$\Huge \begin{pmatrix}\tilde y_1\\\vdots\\\tilde y_m\end{pmatrix}=Q^{-1}\begin{pmatrix}y_1\\\vdots\\y_m\end{pmatrix}=Q^{-1}A\begin{pmatrix}x_1\\\vdots\\x_n\end{pmatrix}=Q^{-1}AP^{-1}\begin{pmatrix}\tilde x_1\\\vdots\\\tilde x_n\end{pmatrix}$$Hence the transformation $T$ with respect to the new bases is given by the matrix $Q^{-1}AP^{-1}$.