
The determinant of a square matrix is a function:
$$\Huge det:M_{n\times n}(\Re)\mapsto\Re$$
For small $n$:
>For $n=1$, $det(a)=a$. Here $A$ is invertible with $A^{-1}=(a^{-1})$, so $A$ is invertible $\iff a\neq 0$.
>For $n=2$, $det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc$, so $A$ is invertible $\iff ad-bc\neq 0$.
>For $n=3$, consider:$$\Huge A=\begin{pmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{pmatrix},\,\underline a=\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix},\,\underline b=\begin{pmatrix}b_1\\b_2\\b_3\end{pmatrix},\,\underline c=\begin{pmatrix}c_1\\c_2\\c_3\end{pmatrix}$$
>$A\underline x=l$ has a unique solution ($A^{-1}$ exists) $\iff$[[Scalar triple product|$\underline a\cdot(\underline b\times\underline c)$]] $\neq 0$, so we define $det\,A=\underline a\cdot(\underline b\times\underline c)$:$$ det\,A=\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix}\cdot\begin{pmatrix}b_2c_3-b_3c_2\\b_3c_1-b_1c_3\\b_1c_2-b_2c_1\end{pmatrix}=a_1det\begin{pmatrix}b_2&b_3\\c_2&c_3\end{pmatrix}-a_2det\begin{pmatrix}b_1&b_3\\c_1&c_3\end{pmatrix}+a_3\begin{pmatrix}b_1&b_2\\c_1&c_2\end{pmatrix}$$
>

# General definition:

Given a matrix $A\in M_{n}(\Re)$ we write $A_{r,s}$ for the matrix obtained by deleting the $r$th row and $s$th column. This defines $A_{r,s}$ as the $(r,s)$th minor of $A$. The unsigned $(r,s)$th cofactor of $A$ is $det(A_{r,s})$, the signed $(r,s)$th cofactor of $A$ is then:
$$\Huge (-1)^{r+s}det(A_{r,s})$$
Then $det\,A$ is defined by an expansion along the first row:$$\Huge det(A):=\sum_{j=1}^na_{1j}(-1)^{1+j}det(A_{1,j})$$
Where $det(A_{1,j})$ is the $(1,j)$th unsigned cofactor of $A$. You can also obtain $det\,A$ by expansion along any row, that is for any $1\leq i\leq n$ we have:
$$\Huge det(A):=\sum_{j=1}^na_{ij}(-1)^{i+j}det(A_{i,j})$$
That is the expansion along the $i$th row.

# Properties of the Determinant:

Consider $A=\begin{pmatrix}\underline a_1\\\vdots\\\underline a_r\\\vdots\\\underline a_n\end{pmatrix}$, where each $\underline a_i$ is a row vector. Then the following are true:
> $det\,I_n=1$ $I$
> $det(M_r(\lambda)A)=det\begin{pmatrix}\underline a_1\\\vdots\\\underline \lambda a_r\\\vdots\\\underline a_n\end{pmatrix}=\lambda det\begin{pmatrix}\underline a_1\\\vdots\\\underline a_r\\\vdots\\\underline a_n\end{pmatrix}\lambda det(A)$, linearity in multiplication $II$
> $det\begin{pmatrix}\underline a_1\\\vdots\\\underline a_r+b_r\\\vdots\\\underline a_n\end{pmatrix}=det\begin{pmatrix}\underline a_1\\\vdots\\\underline a_r\\\vdots\\\underline a_n\end{pmatrix}+det\begin{pmatrix}a_1\\\vdots\\\underline b_r\\\vdots\\\underline a_n\end{pmatrix}$, linearity in addition $III$
> Swapping two rows, $det(P_{rs}A)=-det(A)$ $IV$
> $det\,A=0$ if it has two equal rows, or two rows that are multiplies of one another. $V$
> $det\,A=0$ if $A$ has a zero row. $VI$
> $det(A_{rs}(\lambda)A)=det\,A$ $VII$

![[determinant properties proof]]

# Uniqueness:

