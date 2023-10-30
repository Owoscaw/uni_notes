
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

