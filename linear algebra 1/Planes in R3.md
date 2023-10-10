Planes in the [[Vector space definitions|vector space]] $\Re^3$ can be described in three ways; Parametric, Normal Vector, and Cartesian:

# Parametric:

The plane $\Pi\subseteq\Re^3$ can be described by a point on the plane, $\underline a\in\Pi$, and two non-collinear vectors $\underline d_1,\underline d_2\in\Re^3$ that are both parallel to $\Pi$:
$$\Huge \Pi=\left\{\underline a+\lambda_1\underline d_1+\lambda_2\underline d_2:\lambda_1,\lambda_2\in\Re\right\}$$
# Normal vector:

The plane $\Pi\in\Re^3$ can be describes by a point $\underline a\in\Pi$ and a vector $\underline n$ that is normal to the plane. Let $\underline X$ represent a general point on the plane:
$$ \Pi=\left\{\underline X\in\Re^3:\underline X-\underline a\perp\underline n\right\}=\left\{\underline X\in\Re^3:(\underline X-\underline a)\cdot\underline n=0\right\}=\left\{\underline X\in\Re^3:\underline X\cdot\underline n=\underline a\cdot\underline n\right\}$$
# Cartesian:

The cartesian description of a plane is another way to write the normal vector description of a plane. That is, $\Pi\in\Re^3$ can be described as the set of all general points $\begin{pmatrix}x\\y\\z\end{pmatrix}\in\Re^3$ that satisfy:
$$\Huge \begin{pmatrix}x\\y\\z\end{pmatrix}\cdot\underline n=\underline a\cdot\underline n=n_1x+n_2y+n_3y=\mathcal{l}$$
# Conversion:

The parametric description of a place can be determined, given its cartesian form. Knowing $ax+by+cz=\underline a\cdot\underline n$ allows the following manipulation given $c\neq0$:
$$\Huge z=\frac{\mathcal{l}}{c}-\frac{a}{c}x-\frac{b}{c}y$$
$$\Huge \begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}x\\y\\\frac{\mathcal{l}}{c}-\frac{a}{c}x-\frac{b}{c}y\end{pmatrix}=\begin{pmatrix}0\\0\\\frac{\mathcal{l}}{c}\end{pmatrix}+x\begin{pmatrix}1\\0\\-\frac{a}{c}\end{pmatrix}+y\begin{pmatrix}0\\1\\-\frac{b}{c}\end{pmatrix}$$
Now this is in the form of a parametric description for a p