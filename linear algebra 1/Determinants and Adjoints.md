
The determinant of a square matrix is a function:
$$\Huge det:M_{n\times n}(\Re)\mapsto\Re$$
For small $n$:
>For $n=1$, $det(a)=a$. Here $A$ is invertible with $A^{-1}=(a^{-1})$, so $A$ is invertible $\iff a\neq 0$.
>For $n=2$, $det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc$, so $A$ is invertible $\iff ad-bc\neq 0$.
>For $n=3$, consider:$$\Huge A=\begin{pmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{pmatrix},\,\underline a=\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix},\,\underline b=\begin{pmatrix}b_1\\b_2\\b_3\end{pmatrix},\,\underline c=\begin{pmatrix}c_1\\c_2\\c_3\end{pmatrix}$$
>$A\underline x=l$ has a unique solution ($A^{-1}$ exists) $\iff$[[Scalar triple product|$\underline a\cdot(\underline b\times\underline c)$]] $\neq 0$, so we define $det\,A=\underline a\cdot(\underline b\times\underline c)$:$$ det\,A=\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix}\cdot\begin{pmatrix}b_2c_3-b_3c_2\\b_3c_1-b_1c_3\\b_1c_2-b_2c_1\end{pmatrix}=a_1det\begin{pmatrix}b_2&b_3\\c_2&c_3\end{pmatrix}-a_2det\begin{pmatrix}b_1&b_3\\c_1&c_3\end{pmatrix}+a_3det\begin{pmatrix}b_1&b_2\\c_1&c_2\end{pmatrix}$$
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
> $E_i=M_r(\mu)$, set $\lambda_i=\mu=det(M_r(\mu))$
> $E_i=A_{rs}(\mu)$, set $\lambda_i=1=det(A_{rs}(\mu))$
> $E_i=P_{rs}$, set $\lambda_i=-1=det(P_{rs})$

So we have $det(A^\prime)=\lambda_l\dots\lambda_1det(A)$, and $f(A^\prime)=\lambda_l\dots\lambda_1f(A)$. Also $det(A)=\lambda_l^{-1}\dots\lambda_1^{-1}det(A^\prime)$ as well as $f(A)=\lambda_l^{-1}\dots\lambda_1^{-1}f(A^\prime)$. In RREF, $A^\prime$ is either $I_n$ or has a row of zeroes. In each case:
>$A^\prime=I_n:f(A^\prime)=1=det(A^\prime)$
>$A^\prime$ has a row of zeroes: $f(A^\prime)=0=det(A^\prime)$

Hence $det(A)=f(A)$, making $det(A)$ the unique function that satisfies all the properties above. To turn any square matrix $A$ into $I_n$, $A_{rs}(\lambda)$ and $M_r(\lambda)$ are used, $P_{rs}$ is never used. This can be used to track what the determinant of the original matrix was.

$A$ is called upper triangular $\iff$ all entries below the diagonal are $0$. If $A$ is an upper or lower $n\times n$ matrix with diagonal entries $a_{11},a_{22},\dots,a_{nn}$:$$\Huge det(A)=\prod_{k=1}^na_{kk}$$
So to compute the determinant of a general $A\in M_n(\Re)$ matrix, EROs can be used to turn $A$ into upper or lower triangular form, then the above product can be calculated. The EROs must be used to modify the determinant as well as the matrix, as above.

# Theorems with determinants:

## Inverse matrices:

For $A\in M_n(\Re)$, if $det(A)\neq 0\iff A$ is [[Matrix operations and inverses#Inverses|invertible]]. We write $A^\prime=E_l\dots E_2E_1A$, where $A^\prime$ is in RREF. $$\Huge det(A^\prime)=\lambda_l\dots\lambda_2\lambda_1det(A)$$$$\Huge det(A)\neq0\iff det(A^\prime)\neq0\iff A^\prime=I_n$$
Therefore $A^{-1}$ exists with $A^{-1}=E_l\dots E_2E_1$, note each $\lambda_i\neq0$.

## Products of matrices:

For $A,B\in M_n(\Re)$, $det(AB)=det(A)det(B)$. Suppose $A,B$ are both invertible and expressible as products of elementary matrices.$$\Huge A=E_1\dots E_k,\,B=F_1\dots F_l$$
Where each $E_i,F_j$ are appropriate elementary matrices for $1\leq i\leq k,1\leq j\leq k$. Note that:
$$\Huge det(AB)=det(E_1\dots E_kF_1\dots F_l)=det(E_1)det(E_2\dots E_kF_1\dots F_l)$$$$\Huge \implies det(AB)=det(E_1)\dots det(E_k)det(F_1)\dots det(F_l)$$$$\Huge \implies det(AB)=det(E_1\dots E_k)det(F_1\dots F_l)=det(A)det(B)$$
This has a corollary where if $A$ is not invertible, then $AB$ is not invertible. Assume $A$ is not invertible, it follows that $det(A)=0$. Then $0=det(A)=det(A)det(B)=det(AB)$, so $AB$ is not invertible.

## Transpose:

If $A\in M_n(\Re)$, then $det(A^t)=det(A)$. Every row operation on $A$ is equivalent to a column operation on $A^t$. We know $A$ is invertible $\iff A^t$ is invertible, that is $(A^t)^{-1}=(A^{-1})^t$. If $A$ is invertible, then $A=E_1\dots E_s$. where each $E_i$ is an elementary matrix. $$\Huge det(A)=det(E_1\dots E_s)=det(E_1)\dots det(E_s)$$
Using the above theorem. Also $A^t=(E_1\dots E_s)^t=E_s^t\dots E_1^t$. Note $(M_r(\lambda))^t=M_r(\lambda),\,(P_{rs})^t=P_{rs},\,(A_{rs}(\lambda))^t=A_{sr}(\lambda)$, therefore the determinants of transposed elementary matrices are unchanged. So:$$\Huge det(A^t)=det(E_s^t)\dots det(E_1^t)=det(E_1)\dots det(E_s)=det(A)$$

# Adjoints:

Given $A\in M_n(\Re)$, the adjoint of $A$ is defined by:$$\Huge (adj(A))_{rs}:=(-1)^{r+s}det(A_{s,r})$$
This is equivalent to the transpose of the matrix of signed cofactors. Also:$$\Huge A\cdot adj(A)=det(A)\cdot I_n=adj(A)\cdot A$$
This has a corollary, given $det(A)\neq 0$:
$$\Huge A\cdot\left(\frac{1}{det(A)}adj(A)\right)=I_n=\left(\frac{1}{det(A)}adj(A)\right)\cdot A$$
Therefore this gives another method to compute the inverse:
$$\Huge A^{-1}=\frac{1}{det(A)}adj(A)$$
To prove this, we compute $A\cdot adj(A)$. Each entry is defined by:$$\Huge (A\cdot adj(A))_{rs}=\sum_{k=1}^na_{rk}(adj(A))_{ks}=\sum_{k=1}^na_{rk}(-1)^{k+s}det(A_{s,k})$$
When $r=s$:$$\Huge \sum_{k=1}^na_{rk}(-1)^{k+s}det(A_{s,k})=\sum_{k=1}^na_{sk}(-1)^{k+s}det(A_{s,k})=det(A)$$
As this is an expansion along the $r=s$th row. When $r\neq s$, replace the $s$th row of $A$ with the $r$th row of $A$:$$\Huge B=\begin{pmatrix}\underline a_1\\\vdots\\\underline a_r\\\vdots\\\underline a_r\\\vdots\\\underline a_n\end{pmatrix}$$
Since $B$ has a repeated row, it satisfied one of the properties of the determinant. Namely that when two rows are equal or multiples of one another, the determinant is zero. Note that:$$\Huge \sum_{k=1}^na_{rk}(-1)^{k+s}det(A_{s,k})=det(B)=0,\,\text{given}\,r\neq s$$
So we have:$$\Huge \sum_{k=1}^na_{rk}(-1)^{k+s}det(A_{s,k})=\begin{cases}det(A)&\text{if}\,\,\,r=s\\0&\text{otherwise}\end{cases}$$
So this takes value $det(A)$ along the diagonal, $0$ otherwise. This is equivalent to $det(A)I_n$.

# Cramer's rule:

Give $A\in M_n(\Re),\,\underline b\in\Re^n$ and that $A$ is invertible. Then $A\underline x=\underline b$ has a unique solution, that is $\underline x=A^{-1}\underline b$. The coordinates of this unique solution are given by:$$\Huge x_i=\frac{det\begin{pmatrix}\underline a_1&\underline a_2&\dots&\underline b&\dots&\underline a_n\end{pmatrix}}{det(A)}$$
This is shown as follows:$$\Huge \underline x=A^{-1}\underline b=\frac{1}{det(A)}adj(A)\underline b$$
So we have:
$$\Huge x_i=\frac{1}{det(A)}\sum_{k=1}^nadj(A)_{ik}\,b_{k1}=\frac{1}{det(A)}\sum_{k=1}^n(-1)^{i+k}det(A)_{k,i}\,b_k$$
This expression is equivalent to the expansion down the $i$th column:
$$\Huge x_i=\frac{1}{det(A)}det\begin{pmatrix}\underline a_1&\underline a_2&\dots&\underline a_{i-1}&\underline b&\underline a_{i+1}&\dots&\underline a_n\end{pmatrix}$$

# Geometric interpretation of determinants:


The determinant has the following relationship to the area of a parallelogram formed by two vectors and the origin in [[Vector space definitions|$\Re^2$]]:
![[geometric determinant]]
A parallelopiped is formed in $\Re^3$ formed by the vectors $\underline 0,\underline u, \underline v,\underline w$ and all their possible combinations, $P$. The volume is given by the product of the base and the height of the parallelopiped:$$\Huge \text{Vol}(P)=\text{Base}\times\text{Height}=|\underline v\times\underline w||\underline u|sin\,\theta$$
Where $\theta$ is the angle made between $\underline u$ and the plane formed by $\underline v$ and $\underline w$:$$\Huge \text{Vol}(P)=|\underline v\times\underline w||\underline u|cos\left(\frac{\pi}{2}-\theta\right)=|\underline u\cdot(\underline v\times\underline w)|=|det\begin{pmatrix}\underline u&\underline v&\underline w\end{pmatrix}|$$
Where $\underline u\cdot(\underline v\times\underline w)$ is the [[Scalar triple product|scalar triple product]]. This process generalises to a parallelopiped in [[Vector space definitions|$\Re^n$]], where the volume of an $n$-dimensional parallelopiped spanned by the vectors $\underline v_1,\dots,\underline v_n$:$$\Huge P=\left\{\lambda_1\underline v_1+\dots+\lambda_n\underline v_n:\lambda_i\in\{0,1\}\right\}$$The parallelopiped is formed by this set of combinations of vectors. Its volume is then given by:$$\Huge \text{Vol}(P)=\left|det\begin{pmatrix}\underline v_1&\dots&\underline v_n\end{pmatrix}\right|$$
