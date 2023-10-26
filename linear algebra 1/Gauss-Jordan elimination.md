
A system of linear equations can be solved using a matrix given the following. For $m$ systems of linear equations, in $n$ variables, the equations are set up as follows:
$$\Huge a_{11}x_1+a_{12}x_2+\dots+a_{1n}x_n=b_1$$
$$\huge a_{21}x_1+a_{22}x_2+\dots+a_{2n}x_n=b_1$$
$$\Huge a_{m1}x_1+a_{m2}x_2+\dots +a_{mn}x_n=b_m$$
This can be written as:
$$\Huge \sum_{j=1}^na_{ij}x_j=b_j,\,\text{for}\,\,i=1,\dots,m$$
Here we have $n$ variables with $m$ equations. This is also written as the [[Scalar Product|scalar product]]:$$\Huge \underline a_i\cdot \underline x=\begin{pmatrix}a_{i1}\\a_{i2}\\\vdots\\a_{in}\end{pmatrix}\cdot\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}=b_i,\,\text{for}\,i=1,\dots,m$$
The general process to solve a system of linear equations is:
> Form augmented matrix
> Use EROs to convert the augmented matrix to RREF
> Read off solutions
# Formation

The solution to these equations can be called a "hyperplane" in $\Re^n$, where each equation forms a normal vector for one of these "hyperplanes". The set of solutions that satisfy all of these equations can be found by formulating them into a [[Matrix definition|matrix]]. A sequence of EROs (Elementary Row Operations) is then performed to convert the matrix into RREF (Row Reduced Echelon Form), then the solution can be read off. The equations listed above can be written as the matrix:$$\Huge A=(a_{ij})=\begin{pmatrix}a_{11}&a_{12}&\dots&a_{1n}\\a_{21}&a_{22}&\dots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{m1}&a_{m2}&\dots&a_{mn}\end{pmatrix}\in M_{m\times n}(\Re)$$
$$\Huge \underline b=\begin{pmatrix}b_1\\\vdots\\b_m\end{pmatrix}\in\Re^m,\,\,\underline x=\begin{pmatrix}x_1\\\vdots\\x_m\end{pmatrix}$$
$$\Huge A\underline x=\underline b$$
[[Matrix operations#Matrix multiplication|Matrix multiplication]] between $A$ and $x$ will give the entire original system of linear equations. If $A\in M_n(\Re)$ and $\underline b\in\Re^n$, and $A$ is [[Matrix operations#Inverses|invertible]], then the system of linear equations given above by $(A|\underline b)$ has a unique solution:
$$ A\underline x=\underline b\iff A^{-1}(A\underline x)=A^{-1}\underline b\iff(A^{-1}A)\underline x=A^{-1}\underline b\iff I_n\underline x=A^{-1}\underline b\iff\underline x=A^{-1}\underline b$$
## RREF:

$A$ is known as the coefficient matrix. A matrix is in RREF if and only if:
> The first non-zero entry in any non-zero row is $1$, the leading $1$. ($I$)
> If a row has a leading $1$ in the $j$th column, then all other entries in the $j$th column are zero and all leading $1$s of subsequent rows are to the right of the $j$th column. ($II$)
> Any zero-rows are placed after non-zero rows. ($III$)

In general, a matrix in RREF looks like:
$$\Huge \begin{pmatrix}1&\star&\dots&\star&0&\star&\dots&\star&0&\star&\dots&\star&0&\star&\dots&\star\\0&0&\dots&0&1&\star&\dots&\star&0&\star&\dots&\star&0&\star&\dots&\star\\0&0&\dots&0&0&0&\dots&0&1&\star&\dots&\star&0&\star&\dots&\star\\\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots\\0&0&\dots&0&0&0&\dots&0&0&0&\dots&0&1&\star&\dots&\star\end{pmatrix}$$

# Augmentation and solution:

The "augmented matrix", $(A|\underline b)$, fully represents the equation $A\underline x=\underline b$. This is written by augmenting $\underline b$ onto the end of $A$:
$$\Huge (A|\underline b)=\begin{pmatrix}a_{11}&a_{12}&\dots&a_{1n}&|&b_1\\a_{12}&a_{22}&\dots&a_{2n}&|&b_2\\\vdots&\vdots&\ddots&\vdots&|&\vdots\\a_{m1}&a_{m2}&\dots&a_{mn}&|&b_m\end{pmatrix}$$
The solution set represented by this matrix. Note that the single row matrix $\begin{pmatrix}a_{11}&a_{12}&\dots&a_{1n}|b_1\end{pmatrix}$ represents the equation $a_{11}+a_{12}+\dots+a_{1n}=b_1$. If this augmented matrix is in RREF, then it can be interpreted that variables in columns with leading ones are equal to that row's associated augmented value, subtract all of the other variables in the row. In this sense, variables corresponding to columns without leading 1s are free variables, the variables with leading ones are written in terms of their augment and free variables.

When leading variables are written in terms of free variables, the solution set becomes obvious:
$$\Huge \begin{pmatrix}b_1-a_{12}x_2-a_{13}x_4-\dots-a_{1n}x_n\\b_2-a_{23}x_3-a_{24}x_5-\dots-a_{2n}x_n\\\vdots\\b_m-a_{mm}x_m-a_{m(m+1)}x_{m+1}-\dots-a_{mn}x_{n}\end{pmatrix}$$

# Elementary Row operations:

Elementary row operations, or EROs are defined as follows:
>$P_{rs}$, permute means to switch row $r$ with row $s$.
>$M_r(\lambda)$ , multiply means to multiply all elements in row $r$ by $\lambda\neq 0$.
>$A_{rs}$ , add means to add row $r$ to row $s$.
>$A_{rs}(\lambda)$ is a composition of add and multiply, equivalent to $M_r(\lambda^{-1})\circ A_{rs}\circ M_r(\lambda)$. Here, $\lambda$ times row $r$ is added onto row $s$.

Every matrix can be made into RREF by a finite sequence of EROs. This is shown through an algorithm:
> Find the first non-zero column.
> Go down the first non-zero column until the first non-zero entry, $\lambda$, is found.
> If this is row $r$, with $r\neq 1$, apply $P_{1r}$ so that there is a non-zero entry at the top of the first non-zero column.
> Apply $M_1(\lambda^{-1})$ so that this first entry is a $1$.
> Using $A_{1i}(\mu)$ clear all other non-zero entries in the first non-zero column.

The matrix will now be in the form;
$$\Huge \begin{pmatrix}1&\star&\dots&\star\\0&\star&\dots&\star\\\vdots&\vdots&\ddots&\vdots\\0&\star&\dots&\star\end{pmatrix}\,\text{or}\,\begin{pmatrix}0&\dots&0&1&\star&\dots&\star\\0&\dots&0&0&\star&\dots&\star\\\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots\\0&\dots&0&0&\star&\dots&\star\end{pmatrix}$$
### The algorithm:

Let $A\in M_{m\times n}(\Re)$, the Gauss-Jordan elimination of $A$ is described by repeatedly applying the above basic routine in stages. First, the routine is applied to give a matrix of the following form:
$$\Huge A_1=\begin{pmatrix}1&\star&\dots&\star\\0&\star&\dots&\star\\\vdots&\vdots&\ddots&\vdots\\0&\star&\dots&\star\end{pmatrix}$$
If all of the remaining rows are zero, then $A_1$ is in RREF. If this is not the case, apply the basic routine to a submatrix of $A_1$, ignoring the first row:
$$\Huge \bar A_2=\begin{pmatrix}1&\star&\dots&\star&\star&\star&\dots&\star\\0&0&\dots&0&1&\star&\dots&\star\\0&0&\dots&0&0&\star&\dots&\star\\\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots\\0&0&\dots&0&0&\star&\dots&\star\end{pmatrix}$$
Then apply $A_{21}(\mu)$ if necessary to make the entry above the leading 1 in the second row a zero, this will give another matrix:$$\Huge A_2=\begin{pmatrix}1&\star&\dots&\star&0&\star&\dots&\star\\0&0&\dots&0&1&\star&\dots&\star\\0&0&\dots&0&0&\star&\dots&\star\\\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots\\0&0&\dots&0&0&\star&\dots&\star\end{pmatrix}$$
Now repeat these steps inductively. Assume stages $1$ through $k-1$ ($k-1<m$) have been completed, resulting in the matrix $A_{k-1}$. Stage $k$ ($k\leq m$): 

If rows $k,k+1,\dots,m$ of the matrix $A_{k-1}$ are all zero then $A_{k-1}$ is in RREF. Similarly, if the leading 1 in the ($k-1$)th row is in the $n$th column, it is easy to check of $A_{k-1}$ is in RREF. If this is not the case, apply the basic routine to the submatrix of $A_{k-1}$, ignoring the first $k-1$ rows. This gives a new matrix:$$\Huge \bar A_k=\begin{pmatrix}1&\star&\dots&\star&0&\star&\dots&\star&\star&\dots&\star\\0&0&\dots&0&1&\star&\dots&\star&\star&\dots&\star\\0&0&\dots&0&0&0&\dots&\star&\star&\dots&\star\\\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots&\vdots&\ddots&\vdots\\0&0&\dots&0&0&0&\dots&1&\star&\dots&\star\\0&0&\dots&0&0&0&\dots&0&\star&\dots&\star\\\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots&\vdots&\ddots&\vdots\\0&0&\dots&0&0&0&\dots&0&\star&\dots&\star\end{pmatrix}$$
Apply $A_{kr}(\mu)$ for $r=1,2,\dots,k-1$, if necessary to $\bar A_k$, ensuring that all remaining non-zero entries in the column containing the leading 1 in the $k$th row are now equal to zero. This gives a new matrix, $A_k$ of form:
$$\Huge A_k=\begin{pmatrix}1&\star&\dots&\star&0&\star&\dots&0&\star&\dots&\star\\0&0&\dots&0&1&\star&\dots&0&\star&\dots&\star\\0&0&\dots&0&0&0&\dots&0&\star&\dots&\star\\\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots&\vdots&\ddots&\vdots\\0&0&\dots&0&0&0&\dots&1&\star&\dots&\star\\0&0&\dots&0&0&0&\dots&0&\star&\dots&\star\\\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots&\vdots&\ddots&\vdots\\0&0&\dots&0&0&0&\dots&0&\star&\dots&\star\end{pmatrix}$$
By induction, this process must terminate either before or after stage $m$. If it terminates before, this is because the matrix is now in RREF. If it terminates after, then the matrix $A_m$ must have a leading 1 on every row, so it is easy to check if $A_m$ is in RREF.

This can be done with an augmented matrix as follows:![[RREF example]]
In general for a matrix given by:
$$\Huge A\in M_{2\times n}(\Re)=\begin{pmatrix}a_{11}&a_{12}&\dots&a_{1n}|b_1\\a_{21}&a_{22}&\dots&a_{2n}|b_2\end{pmatrix}$$
> Applying $M_1(a_{11}^{-1})$:$$\Huge \begin{pmatrix}1&\frac{a_{12}}{a_{11}}&\dots&\frac{a_{1n}}{a_{11}}|\frac{b_1}{a_{11}}\\a_{21}&a_{22}&\dots&a_{2n}|b_2\end{pmatrix}$$
> Then applying $A_{12}(-a_{21})$:$$\Huge \begin{pmatrix}1&\frac{a_{12}}{a_{11}}&\dots&\frac{a_{1n}}{a_{11}}|\frac{b_1}{a_{11}}\\0&a_{22}-\frac{a_{12}}{a_{11}}&\dots&a_{2n}-\frac{a_{1n}}{a_{11}}|b_2-\frac{b_1}{a_{11}}\end{pmatrix}$$
> Then applying $M_2((a_{22}-\frac{a_{12}}{a_{11}})^{-1})$:$$\Huge \begin{pmatrix}1&\frac{a_{12}}{a_{11}}&\dots&\frac{a_{1n}}{a_{11}}|\frac{b_1}{a_{11}}\\0&1&\dots&\frac{a_{2n}-\frac{a_{1n}}{a_{11}}}{a_{22}-\frac{a_{12}}{a_{11}}}|\frac{b_2-\frac{b_1}{a_{11}}}{a_{22}-\frac{a_{12}}{a_{11}}}\end{pmatrix}$$
> Then finally applying $A_{21}(-\frac{a_{12}}{a{11}})$:
> $$\Huge \begin{pmatrix}1&0&\dots&\frac{a_{1n}}{a_{11}}-\frac{a_{2n}-\frac{a_{1n}}{a_{11}}}{a_{22}-\frac{a_{12}}{a_{11}}}|\frac{b_1}{a_{11}}-\frac{b_2-\frac{b_1}{a_{11}}}{a_{22}-\frac{a_{12}}{a_{11}}}\\0&1&\dots&\frac{a_{2n}-\frac{a_{1n}}{a_{11}}}{a_{22}-\frac{a_{12}}{a_{11}}}|\frac{b_2-\frac{b_1}{a_{11}}}{a_{22}-\frac{a_{12}}{a_{11}}}\end{pmatrix}$$
> $A$ is now in RREF

EROs can be proven to not change the solution set of a linear system as each operation is equivalent to left-multiplication by an associated matrix, equivalent to each ERO applied to $I_n$. These matrices are called the elementary matrices. Each one of these matrices are invertible:
> $P_{rs}^{-1}=P_{rs}$
> $M_{r}(\lambda)^{-1}=M_{r}(\lambda^{-1})$
> $A_{rs}(\lambda)^{-1}=A_{rs}(-\lambda)$
# Using GJ elimination:

Two linear systems are called equivalent if they share a solution set. Applying EROs to the augmented matrix of a linear system gives an equivalent linear system. An augmented matrix is in RREF if its associated coefficient matrix is also in RREF. Applying the above algorithm on $(A|b)$ allows an equivalent system to be produced, where the solution set is easy to spot. Note that:
> Rows of form $\begin{pmatrix}0&\dots&0|0\end{pmatrix}$ can be deleted.
> Rows of form $\begin{pmatrix}0&\dots&0|k\end{pmatrix}$ for $k\neq 0$ satisfy $0x_1+0x_2+\dots+0x_n=k=0$, a contradiction. In this case, the system has no solutions and is said to be inconsistent.
> When an augmented matrix is in RREF, a variable $x_j$ being a free variables corresponds to column $j$ of the coefficient matrix not containing the leading 1.

Using the example from above, the solution set is found as follows:![[solution set example]]

# Inverse matrices:

If $B$ is invertible then the linear system $A\underline x=\underline b$ has the same solution set as $(BA)\underline x=(B\underline b)$. This is proven as follows:$$\Huge A\underline x=\underline b\implies BA\underline x=B\underline b\implies B^{-1}(BA\underline x)=IA\underline x=A\underline x=B^{-1}B\underline b=\underline b$$

Let $A\in M_{n\times n}(\Re)$ be a square matrix. Then the follwing statements are either all true or all false:
> In the RREF of $A$, every column has a leading $1$. ($I$)
> The RREF of $A$ is $I_n$. ($II$)
> The only solution to $A\underline x=0$ is $\underline x=0$. ($III$)
> $A$ is invertible. ($IV$)

$I\implies II$ as $A$ is square, and each entry in a column with a leading $1$ must be $0$, so the RREF of any square matrix must be $I_n$. $I\implies III$, as if $I$ holds then $II$ holds, so the RREF of $A$ is $I_n$, and $I_n\underline x=0$ has one unique solution, that is $\underline x=0$. $III\implies I$, there are no free variables in $I_n$ as the only non-zero entries are in rows with a leading $1$ (every row). 



