
A matrix is a rectangular array of real numbers. The $(i,j)$th element of a matrix $M$ is written as $M_{i,j}$, meaning the element of $M$ in the $i$th row and $j$th column. Matrices with a single column are the same as vectors, matrices with a single row are called row vectors.

A matrix $M$ has a transpose $M^T$ defined such that the $(i,j)$th entry of $M$ is the $(j,i)$th entry of $M^T$. That is:
$$\Huge (M^T)_{i,j}=M_{j,i}$$
A matrix is symmetric if it is equal to it's transpose.

The set of all $m\times n$ matrices is written as $M_{m\times n}(\Re)$, and $M_n(\Re)$ is written for all square $n\times n$ matrices. All symmetric matrices are square.

If $f(i, j)$ is an expression involving $i$ and $j$, then $(f(i,j))_{m\times n}$ is written for the $m\times n$ matrix with the $(i,j)$th entry being $f(i,j)$. Often, $A\in M_{m\times n}(\Re)$ is written as $A=(a_{i,j})_{m\times n}$, or $(a_{i,j})$

# Special matrices:

We define $0=0_{m\times n}\in M_{m\times n}(\Re)$ to be the matrix with all entries of 0, that is $0_{m\times n}=(0)_{m\times n}$. This is the $m\times n$ zero matrix:
$$\Huge 0_{m\times n}=\begin{pmatrix}0&\dots&0\\\vdots&\ddots&\vdots\\0&\dots&0\end{pmatrix},$$
For $r,s\in\mathbb{Z}$, we define $\delta_{r,s}$ to be 