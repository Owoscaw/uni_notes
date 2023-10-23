
A system of linear equations can be solved using a matrix given the following. For $m$ systems of linear equations, in $n$ variables, the equations are set up as follows:
$$\Huge a_{11}x_1+a_{12}x_2+\dots+a_{1n}x_n=b_1$$
$$\huge a_{21}x_1+a_{22}x_2+\dots+a_{2n}x_n=b_1$$
$$\Huge a_{m1}x_1+a_{m2}x_2+\dots +a_{mn}x_n=b_m$$
This can be written as:
$$\Huge \sum_{j=1}^na_{ij}x_j=b_j,\,\text{for}\,\,i=1,\dots,m$$
Here we have $n$ variables with $m$ equations. This is also written as the [[Scalar Product|scalar product]]:$$\Huge \underline a_i\cdot \underline x=\begin{pmatrix}a_{i1}\\a_{i2}\\\vdots\\a_{in}\end{pmatrix}\cdot\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}=b_i,\,\text{for}\,i=1,\dots,m$$
# Formation

The solution to these equations can be called a "hyperplane" in $\Re^n$, where each equation forms a normal vector for one of these "hyperplanes". The set of solutions that satisfy all of these equations can be found by formulating them into a [[Matrix definition|matrix]]. A sequence of EROs (Elementary Row Operations) is then performed to convert the matrix into RREF (Row Reduced Echelon Form), then the solution can be read off. The equations listed above can be written as the matrix:$$\Huge A=(a_{ij})=\begin{pmatrix}a_{11}&a_{12}&\dots&a_{1n}\\a_{21}&a_{22}&\dots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{m1}&a_{m2}&\dots&a_{mn}\end{pmatrix}\in M_{m\times n}(\Re)$$
$$\Huge \underline b=\begin{pmatrix}b_1\\\vdots\\b_m\end{pmatrix}\in\Re^m,\,\,\underline x=\begin{pmatrix}x_1\\\vdots\\x_m\end{pmatrix}$$
$$\Huge A\underline x=\underline b$$
[[Matrix operations#Matrix multiplication|Matrix multiplication]] between $A$ and $x$ will give the entire original system of linear equations. If $A\in M_n(\Re)$ and $\underline b\in\Re^n$, and $A$ is [[Matrix operations#Inverses|invertible]], then the system of linear equations given above by $(A|\underline b)$ has a unique solution:
$$ A\underline x=\underline b\iff A^{-1}(A\underline x)=A^{-1}\underline b\iff(A^{-1}A)\underline x=A^{-1}\underline b\iff I_n\underline x=A^{-1}\underline b\iff\underline x=A^{-1}\underline b$$


$A$ is known as the coefficient matrix. A matrix is in RREF if and only if:
> The first non-zero entry in any non-zero row is $1$, the leading $1$. ($I$)
> If a row has a leading $1$ in the $j$th column, then all other entries in the $j$th column are zero and all leading $1$s of subsequent rows are to the right of the $j$th column. ($II$)
> Any zero-rows are placed after non-zero rows. ($III$)

In general, a matrix in RREF looks like:
$$\Huge \begin{pmatrix}1&\star&\dots&\star&0&\star&\dots&\star&0&\star&\dots&\star&0&\star&\dots&\star\\0&0&\dots&0&1&\star&\dots&\star&0&\star&\dots&\star&0&\star&\dots&\star\\0&0&\dots&0&0&0&\dots&0&1&\star&\dots&\star&0&\star&\dots&\star\\\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots\\0&0&\dots&0&0&0&\dots&0&0&0&\dots&0&1&\star&\dots&\star\end{pmatrix}$$

# Augmentation:

The "augmented matrix", $(A|\underline b)$, fully represents the equation $A\underline x=\underline b$. This is written by augmenting $\underline b$ onto the end of $A$:
$$\Huge (A|\underline b)=\begin{pmatrix}a_{11}&a_{12}&\dots&a_{1n}&|&b_1\\a_{12}&a_{22}&\dots&a_{2n}&|&b_2\\\vdots&\vdots&\ddots&\vdots&|&\vdots\\a_{m1}&a_{m2}&\dots&a_{mn}&|&b_m\end{pmatrix}$$
The solution set represented by this matrix. Note that the single row matrix $\begin{pmatrix}a_{11}&a_{12}&\dots&a_{1n}|b_1\end{pmatrix}$ represents the equation $a_{11}+a_{12}+\dots+a_{1n}=b_1$. 