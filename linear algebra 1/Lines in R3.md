Lines can be described in 3 main ways: parametric, cartesian, and by two [[Planes in R3|planes]].

# Parametric:

If $L\in\Re^3$ is a line, it can be described by the set of points:
$$\Huge L=\left\{\underline a+\lambda\underline d:\lambda\in\Re\right\}$$
$$\Huge L=\left\{\begin{pmatrix}x\\y\\z\end{pmatrix}:\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix}+\lambda\begin{pmatrix}d_1\\d_2\\d_3\end{pmatrix},\,\lambda\in\Re\right\}$$
Where $\underline a\in L$, and $\underline d\neq\underline 0$ is a vector parallel to $L$.

# Cartesian:

Given a line, $L\in\Re^3$, described as above, its cartesian description is given by:
$$\Huge \begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix}+\lambda\begin{pmatrix}d_1\\d_2\\d_3\end{pmatrix},so:$$
$$\Huge x=a_1+\lambda d_1,\,y=a_2 \lambda,\,z=a_3+\lambda d_3$$
Rearranging for $\lambda$:
$$\Huge \lambda =\frac{x-a_1}{d_1}=\frac{y-a_2}{d_2}=\frac{z-a_3}{d_3}$$
This relies on $\lambda, d_1, d_2, d_3\neq 0$. Note that:
$$\Huge d_i=0\implies(x/y/z)=a_i$$

# By two planes:

Let two planes be defined by $\Pi_1,\Pi_2\subset\Re^3$. Given that their normal vectors, $\underline n_1, \underline n_2$ are not collinear, their intersection forms a line:
$$\large \Pi_1=\left\{\begin{pmatrix}x\\y\\z\end{pmatrix}:a_1x+b_1y+c_1z=\mathcal{l}_1\right\},\,\Pi_2=\left\{\begin{pmatrix}x\\y\\z\end{pmatrix}:a_2x+b_2y+c_2z=\mathcal{l}_2\right\}$$
$\Pi_1\cap\Pi_2$ form a line, given that $\begin{pmatrix}a_1\\b_1\\c_1\end{pmatrix}$ and $\begin{pmatrix}a_2\\b_2\\c_2\end{pmatrix}$ are not collinear:
$$\Huge L=\left\{\begin{pmatrix}x\\y\\z\end{pmatrix}:a_1x+b_1y+c_1z=\mathcal{l}_1\,\,and\,\,a_2x+b_2y+c_2z=\mathcal{l}_2\right\}$$
$\underline d$ is a vector parallel to $L$, so it is also normal to both plane's normal vectors, that is:
$$\Huge \underline d=\underline n_1\times\underline n_2=\begin{pmatrix}a_1\\b_1\\c_1\end{pmatrix}\times\begin{pmatrix}a_2\\b_2\\c_2\end{pmatrix}=\begin{pmatrix}b_1c_2-b_2c_1\\c_1d_2-c_2a_1\\\end{pmatrix}$$