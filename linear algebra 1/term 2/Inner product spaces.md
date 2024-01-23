
An inner product gives geometric relations between vectors, for example the angle between them. They can also induce a norm, the length of a vector. We require a function that maps two vectors to a real, and is linear in both arguments. A bilinear form $B$ on a [[Real vector spaces|real vector space]] $V$ is a mapping $B:V\times V\mapsto\Re$, any $\underline u,\underline v\in V\mapsto B(\underline u,\underline v)\in\Re$:
>$B(\underline u + \underline v,\underline w)=B(\underline u,\underline w)+B(\underline v,\underline w)$
>$B(\underline w,\underline u + \underline v)=B(\underline w,\underline u)+B(\underline w,\underline v)$
>$B(\lambda\underline u,\underline v)=\lambda B(\underline u,\underline v)=B(\underline u,\lambda\underline v)$

Hence $B$ is linear in both arguments. Given a basis for $\Re^n$ of form $\{\underline v_1,\dots,\underline v_n\}$ defined as $V$ and let $\underline u=x_1\underline v_1+\dots+x_n\underline v_n,\,\,\underline v=y_1\underline v_1+\dots+y_n\underline v_n$ and let $B$ be a bilinear form. Then:$$\large B(\underline u,\underline v)=B\left(\sum_{j=1}^nx_j\underline v_j,\sum_{i=1}^ny_i\underline v_i\right)=\sum_{i,j=1}^ny_iB(\underline v_j,\underline v_i)x_j=\sum_{i,j=1}^ny_iA_{ij}x_j=\underline y^TA\underline x$$Where $A_{ij}=B(\underline v_j,\underline v_i)$, the matrix representing the bilinear form $B$ wrt the basis $\{\underline v_j\}$. For the dot product with respect to the standard basis, $A=I_n$.

So we define an inner product on a real vector space $V$, $(\cdot,\cdot):V\times V\mapsto\Re$ that assigns a real number to a pair of vectors such that:
>$(\underline u,\underline v)=(\underline v,\underline u)$, symmetry
>$(\underline u+\underline v,\underline w)=(\underline u,\underline w)+(\underline v,\underline w)$
>$(\lambda\underline u,\underline v)=\lambda(\underline u,\underline v)$
>$(\underline v,\underline v)\geq 0$ with $\underline v=0$ if and only if $(\underline v,\underline v)=0$

Properties 2 and 3 together with symmetry imply that $(\cdot,\cdot)$ is a bilinear form. $V$ endowed with $(\cdot,\cdot)$ is a real inner product space
