
A system of linear equations can be solved using a matrix given the following. For $m$ systems of linear equations, in $n$ variables, the equations are set up as follows:
$$\Huge a_{11}x_1+a_{12}x_2+\dots+a_{1n}x_n=b_1$$
$$\huge a_{21}x_1+a_{22}x_2+\dots+a_{2n}x_n=b_1$$
$$\Huge a_{m1}x_1+a_{m2}x_2+\dots +a_{mn}x_n=b_m$$
This can be written as:
$$\Huge \sum_{j=1}^na_{ij}x_j=b_j,\,\text{for}\,\,i=1,\dots,m$$
Here we have $n$ variables with $m$ equations. This is also written as the [[Scalar Product|scalar product]]:$$\Huge \underline a_i\cdot \underline x=\begin{pmatrix}a_{i1}\\a_{i2}\\\vdots\\a_{in}\end{pmatrix}\cdot\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}=b_i,\,\text{for}\,i=1,\dots,m$$
The solution to these equations can be called a "hyperplane" in $\Re^n$, where each equation forms a normal vector for one of these "hyperplanes". The set of solutions that satisfy all of these equations can be found by formulating them into a [[Matrix definition|matrix]]. A sequence of EROs (Elementary Row Operations) is then performed to convert the matrix into RREF (Row Reduced Echelon Form), then the solution can be read off. The equations listed above can be written as the matrix:$$\Huge A=\$$