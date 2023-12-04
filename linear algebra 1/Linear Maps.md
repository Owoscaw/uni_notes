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
So let $A$ be this LHS matrix, then we have:$$\Huge T\begin{pmatrix}\lambda_1\\\vdots\\\lambda_m\end{pmatrix}=A\begin{pmatrix}\lambda_1\\\vdots\\\lambda_m\end{pmatrix}$$
This is a known linear map, so this map $T$ must also be linear.

# Properties of linear maps:

Suppose $T:U\mapsto V$, $S:V\mapsto W$ are linear maps. Then the composition $S\circ T:U\mapsto W$ is also linear. In particular, when $U=\Re^u,V=\Re^v,W=\Re^w$ and $T,S$ are represented by $A\in M_{v\times u},B\in M_{u\times w}(\Re)$ respectively, we have:$$\Huge (S\circ T)(x)=(BA)x,\,\,BA\in M_{w\times u}$$Proven as follows: Let $\underline u_1,\underline u_2,\underline u\in U_1,\lambda\in\Re$. Then $(S\circ T)(\underline u_1+\underline u_2)=S(T(\underline u_1+\underline u_2))=S(T(\underline u_1)+T(\underline u_2))=S(T(\underline u_1))+S(T(\underline u_2))=S\circ T(\underline u_1)+S\circ T(\underline u_2)$, showing that $S\circ T$ is closed under addition. Also $S\circ T(\lambda\underline u)=S(T(\lambda\underline u))=S(\lambda T(\underline u))=\lambda S(T(\underline u))=\lambda S\circ T(\underline u)$, showing that $S\circ T$ is also closed under scalar multiplication. So $S\circ T$ is also a linear map.

For the statement with real vector spaces we have:$$\Huge (S\circ T)(\underline x)=S(T(\underline x))=S(A\underline x)=B(A\underline x)=(BA)\underline x$$By associativity of matrix multiplication, we have that $S\circ T$ represents the composition of two linear maps.

# Isomorphism:

If $T:V\mapsto W$ is a linear map, we call $T$ an isomorphism if and only if $T$ is [[Functions, Domain and Range#Bijectivity|bijective]]. In this case we call $V$ and $W$ isomorphic and write $V\cong W$. We then suppose that if $T$ is isomorphic, then $T^{-1}:W\mapsto V$ is also isomorphic. This transformation is obviously bijective, but it is not obvious that it is linear, so we let $\underline w_1,\underline w_2,\underline w\in W,\lambda\in\Re$ and show:
> $\underline v_1=T^{-1}(\underline w_1),\underline v_2=T^{-1}(\underline w_2)\implies T(\underline v_1)=\underline w_1,T(\underline v_2)=w_2$ so we then write:$$\Huge T(\underline v_1+\underline v_2)=T(\underline v_1)+T(\underline v_2)=\underline w_1+\underline w_2$$$$\Huge \underline v_1+\underline v_2=T^{-1}(\underline w_1+\underline w_2)=T^{-1}(\underline w_1)+T^{-1}(\underline w_2)$$Now we set $\underline v=T^{-1}(\underline w)$. Then:$$\Huge T(\lambda\underline v)=\lambda T(\underline v)=\lambda\underline w\implies\lambda T^{-1}(\underline w)=\lambda\underline v=T^{-1}(\lambda\underline w)$$
> Therefore $T^{-1}$ is also a linear map.



Suppose that $V$ has a basis $\{\underline v_1,\dots,\underline v_n\}$. Then the coordinate map $\Phi:V\mapsto\Re^n$ is an isomorphism:$$\Huge \lambda_1\underline v_1+\dots+\lambda_n\underline v_n=\begin{pmatrix}\lambda_1\\\vdots\\\lambda_n\end{pmatrix}$$
We know that $\Phi$ is linear, so we check that it is bijective:$$\Huge \text{If}\,\,\begin{pmatrix}\lambda_1\\\vdots\\\lambda_n\end{pmatrix}\in\Re^n\,\,\text{then}\,\,\Phi(\lambda_1\underline v_1+\dots\lambda_n\underline v_n)=\begin{pmatrix}\lambda_1\\\vdots\\\lambda_n\end{pmatrix}$$Also if $\underline v,\underline w\in V$ where $\underline v\neq\underline w$, then if $\underline v=\lambda_1\underline v_1+\dots+\lambda_n\underline v_n$ and $\underline w=\mu_1\underline v_1+\dots+\mu_n\underline v_n$ then for at least one $i,\lambda_i\neq\mu_i$. This implies that $\Phi(\underline v)$ and $\P$

