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

