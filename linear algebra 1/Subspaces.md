
A subspace, $U$, of [[Vector space definitions|$\Re^n$]] is a subset, $U\subseteq\Re^n$ that satisfies:
> $\underline 0\in U$, existence of the origin
> If $\underline u,\underline v\in U$, then $\underline u+\underline v\in U$, closure under addition
> If $\underline v\in U$ and $\lambda\in\Re$, then $\lambda\underline v\in U$, closure under scalar multiplication

Trivial examples of subspaces are $\{\underline 0\}\subseteq\Re^n$, and $\Re^n\subseteq\Re^n$. [[Lines in R3|Lines]] and [[Planes in R3|planes]] are examples of subspaces, they can be defined in any vector space, not just $\Re^2$ or $\Re^3$.

Given [[Matrix definition|$A\in M_{m\times n}(\Re)$]], then the solution set is homogeneous to the system $A\underline x=\underline 0$:$$\Huge U=\left\{\underline x\in\Re^n:A\underline x=\underline 0\right\}\subseteq\Re^n$$ 
To prove this, we show solutions in $U$ satisfy all conditions for a subspace:
>Let $\underline u,\underline v\in U$, then:$$\Huge A(\underline u+\underline v)=A\underline u+A\underline v=\underline 0+\underline 0=\underline 0,\,\text{therefore}\,\,\underline u+\underline v\in U$$
>Let $\underline u\in U,\lambda\in\Re$:$$\Huge A(\lambda\underline u)=\lambda(A\underline u)=\lambda\underline 0=\underline 0,\,\text{therefore}\,\,\lambda\underline u\in U$$
>Also note $A\underline 0=\underline 0$, so $\underline 0\in U$, the subspace is not empty.

The solution to an inhomogeneous system $A\underline x=\underline b$, where $\underline b=0$ is an affine subspace, the solution set is of form:$$\Huge \underline c+U:=\left\{\underline c+\underline u\right\}$$
