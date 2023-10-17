
# Addition:

Matrix addition is a function that takes two $m\times n$ [[Matrix definition|matrices]], and outputs a third matrix with the same dimensions:
$$\Huge +:M_{m\times n}(\Re)\times M_{m\times n}(\Re)\mapsto M_{m\times n}(\Re)$$
$$\Huge (X,Y)\mapsto X+Y$$
This is defined by:
$$\Huge X+Y=(x_{i,j})+(y_{i,j})=(x_{i,j}+y_{i,j})$$
This is component-wise addition of each element in $X$ and $Y$. This is well defined if both matrices have the same dimensions. Addition is not defined when each matric has different dimension.

# Scalar multiplication:

Scalar multiplication is a function that takes a scalar and a matrix, and outputs a matrix of same dimension:
$$\Huge \cdot:\Re\times M_{m\times n}(\Re)\mapsto M_{m\times n}(\Re)$$
$$\Huge (\lambda, A)\mapsto \lambda A$$
This is similarly defined as:$$\Huge (\lambda A)_{i,j}=\lambda A_{i.j},\,\,\forall 1\leq i\leq m,\,1\leq j\leq n$$
If $X^T=-X$, then $X$ is a skew-symmetric matrix.

# Properties of matrix addition:

Similarly to [[Vector addition and multiplication|axioms of vector operations]], matrix operations give the following identities:
> Existence of zero ($I$):$$\large \exists 0_{m\times n}\in M_{m\times n}(\Re):\forall X\in M_{m\times n}(\Re)\,\,\text{we have}\,\,0_{m\times n}+X=X=X+0_{m\times n}$$
> Commutativity of addition ($II$):$$\Huge \forall X,Y\in M_{m\times n}(\Re)\,\,\text{we have}\,\,X+Y=Y+X$$
> Existence of the negative ($III$):$$\large \forall X\in M_{m\times  n}(\Re)\,\exists\,(-X)\in M_{m\times n}(\Re):X+(-X)=0_{m\times n}=(-X)+X$$


# Properties of scalar multiplication:

> Existence of zero ($I$):$$\Huge 0\cdot X=0_{}$$
