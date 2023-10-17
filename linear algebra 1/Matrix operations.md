
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

# Axioms of matrix addition

Similarly to [[Vector addition and multiplication|axioms of vector operations]], matrix operations give the following identities:
> Existence of additive identity ($I$):$$\large \exists 0_{m\times n}\in M_{m\times n}(\Re):\forall X\in M_{m\times n}(\Re)\,\,\text{we have}\,\,0_{m\times n}+X=X=X+0_{m\times n}$$
> Commutativity ($II$):$$\Huge \forall X,Y\in M_{m\times n}(\Re)\,\,\text{we have}\,\,X+Y=Y+X$$
> Existence of additive inverses ($III$):$$\large \forall X\in M_{m\times  n}(\Re)\,\exists\,(-X)\in M_{m\times n}(\Re):X+(-X)=0_{m\times n}=(-X)+X$$
> 	Associativity ($IV$):$$\Huge \forall X,Y,Z\in M_{m\times n}(\Re),\,\,(X+Y)+Z=X+(Y+Z)$$


# Axioms of scalar multiplication

> Existence of zero ($I$):$$\Huge \forall X\in M_{m\times n}(\Re),\,\,0\cdot X=0_{m\times n}$$
> Existence of one ($II$):$$\Huge \forall X\in M_{m\times n}(\Re),\,\,1\cdot X=X$$
> Associativity ($III$):$$\Huge \forall X\in M_{m\times n}(\Re),\forall\lambda,\mu\in\Re,\,\,(\lambda\mu)X=\lambda(\mu X)$$
> Distributivity ($IV$):$$\Huge\forall X,Y\in M_{m\times n}(\Re),\forall\lambda,\mu\in\Re:$$$$\Huge (\lambda+\mu)X=\lambda X+\mu X,\,\,\lambda(X+Y)=\lambda X+\lambda Y$$

# Matrix multiplication:

Matrix multiplication is a function that takes two matrices as input, and outputs a third matrix:$$\Huge \times:M_{m\times n}(\Re)\times M_{n\times p}(\Re)\mapsto M_{m\times p}(\Re)$$
It is defined for $A=(a_{i,j})_{m\times n},B=(b_{i,j})_{n\times p}$:
$$\Huge (AB)_{i,j}=a_{i1}b_{j1}+a_{i2}b_{j2}+\dots+a_{in}b$$