
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

Let $A\in M_n(\Re)$ and $f(A)=det(A)$. Let $E_1,\dots,E_l$ be [[Gauss-Jordan elimination#Elementary matrices|elementary matrices]] such that $A^\prime=E_l\dots E_1A$ is in [[Gauss-Jordan elimination#RREF|RREF]]. Cases for $E_i$:
> $E_i=M_r(\mu)$, set $\lambda_i=\mu$
> $E_i=A_{rs}(\mu)$, set $\lambda_i=1$
> $E_i=P_{rs}$, set $\lambda_i=-1$

So we have $det(A^\prime)=\lambda_l\dots\lambda_1det(A)$, and $f(A^\prime)=\lambda_l\dots\lambda_1f(A)$. Also $det(A)=\lambda_l^{-1}\dots\lambda_1^{-1}det(A^\prime)$ as well as $f(A)=\lambda_l^{-1}\dots\lambda_1^{-1}f(A^\prime)$. In RREF, $A^\prime$ is either $I_n$ or has a row of zeroes. In each case:
>$A^\prime=I_n:f(A^\prime)=1=det(A^\prime)$
>$A^\prime$ has a row of zeroes: $f(A^\prime)=0=det(A^\prime)$

Hence $det(A)=f(A)$, making $det(A)$ the unique function that satisfies all the properties above. To turn any square matrix $A$ into $I_n$, $A_{rs}(\lambda)$ and $M_r(\lambda)$ are used, $P_{rs}$ is never used. This can be used to track what the determinant of the original matrix was.

$A$ is called upper triangular $\iff$ all entries below the diagonal are $0$. If $A$ is an upper or lower $n\times n$ matrix with diagonal entries $a_{11},a_{22},\dots,a_{nn}$:$$\Huge det(A)=\prod_{k=1}^na_{kk}$$
So to compute the determinant of a general $A\in M_n(\Re)$ matrix, EROs can be used to turn $A$ into upper or lower triangular form, then the above product can be calculated. The EROs must be used to modify the determinant as well as the matrix, as above.

# Relation to [[Matrix operations and inverses#Inverses|inverses]]:

For $A\in M_n(\Re)$, if $det(A)\neq 0\iff A$ is invertible.

For $A,B\in M_n(\Re)$, $det(AB)=det(A)det(B)$. This has a corollary where if $A$ is not invertible, then $AB$ is not invertible. Assume $A$ is not invertible, it follows that $det(A)=0$. Then $0=det(A)=det(A)det(B)=det(AB)$, so $AB$ is not invertible.