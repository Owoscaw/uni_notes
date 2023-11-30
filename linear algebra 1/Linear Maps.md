A linear map from [[Real vector spaces|vector spaces]] $V$ to $W$ is a function $T:V\mapsto W$ that satisfies the following properties, where $+_v,+_w$ denotes addition in $V$ and $W$ respectively :
> $T(\underline v_1 +_v\underline v_2)=T(\underline v_1)+_wT(\underline v_2)\,\,\forall\underline v_1,\underline v_2\in V$ 
> $T(\lambda\underline v)=\lambda T(\underline V)\,\,\forall\lambda\in\Re,\underline v\in V$

Note also that $0$ must be sent to $0$, that is:$$\Huge T(\underline 0_v)=T(0\cdot\underline 0_v)=0\cdot T(\underline 0_v)=\underline 0_w$$
For example, suppose that $A\in M_{m\times n}(\Re)$. We then defined $T=T_A:\Re^n\mapsto\Re^n,\,T:\underline v\mapsto A\underline v$. We can then check this:
>$T(\underline v_1+\underline v_2)=A(\underline v_1+\underline v_2)=A\underline v_1+A\underline v_2=T(\underline v_1)+T(\underline v_2)$. We know this from the distributive law of matrix multiplication. This linear map holds under addition.
>$T(\lambda\underline v)=A(\lambda\underline v)=\lambda(A\underline v)=\lambda T(\underline v)$. We know this from the commutative law of scalar multiplication for matrices. This linear map holds under scalar multiplication.

Suppose vector spaces $V$ and $W$ and let $\{\underline v_1,\dots,\underline v_n\}$ be a basis for $V$. Then we have:
> A linear map $T:V\mapsto W$ is determined by its values on the basis, $T(\underline v_1),\dots,T(\underline v_n)$.
> Conversely, given arbitrary vectors $\underline w_1,\dots,\un$