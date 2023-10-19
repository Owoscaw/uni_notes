
# Addition:

Matrix addition is a function that takes two $m\times n$ [[Matrix definition|matrices]], and outputs a third matrix with the same dimensions:
$$\Huge +:M_{m\times n}(\Re)\times M_{m\times n}(\Re)\mapsto M_{m\times n}(\Re)$$
$$\Huge (X,Y)\mapsto X+Y$$
This is defined by:
$$\Huge X+Y=(x_{i,j})+(y_{i,j})=(x_{i,j}+y_{i,j})$$
This is component-wise addition of each element in $X$ and $Y$. This is well defined if both matrices have the same dimensions. Addition is not defined when each matric has different dimension.

# Axioms of matrix addition

> Existence of additive identity ($I$):$$\large \exists 0_{m\times n}\in M_{m\times n}(\Re):\forall X\in M_{m\times n}(\Re)\,\,\text{we have}\,\,0_{m\times n}+X=X=X+0_{m\times n}$$
> Commutativity ($II$):$$\Huge \forall X,Y\in M_{m\times n}(\Re)\,\,\text{we have}\,\,X+Y=Y+X$$
> Existence of additive inverses ($III$):$$\large \forall X\in M_{m\times  n}(\Re)\,\exists\,(-X)\in M_{m\times n}(\Re):X+(-X)=0_{m\times n}=(-X)+X$$
> 	Associativity ($IV$):$$\Huge \forall X,Y,Z\in M_{m\times n}(\Re),\,\,(X+Y)+Z=X+(Y+Z)$$


# Scalar multiplication:

Scalar multiplication is a function that takes a scalar and a matrix, and outputs a matrix of same dimension:
$$\Huge \cdot:\Re\times M_{m\times n}(\Re)\mapsto M_{m\times n}(\Re)$$
$$\Huge (\lambda, A)\mapsto \lambda A$$
This is similarly defined as:$$\Huge (\lambda A)_{i,j}=\lambda A_{i.j},\,\,\forall 1\leq i\leq m,\,1\leq j\leq n$$
If $X^T=-X$, then $X$ is a skew-symmetric matrix.

# Axioms of scalar multiplication

> Existence of zero ($I$):$$\Huge \forall X\in M_{m\times n}(\Re),\,\,0\cdot X=0_{m\times n}$$
> Existence of one ($II$):$$\Huge \forall X\in M_{m\times n}(\Re),\,\,1\cdot X=X$$
> Associativity ($III$):$$\Huge \forall X\in M_{m\times n}(\Re),\forall\lambda,\mu\in\Re,\,\,(\lambda\mu)X=\lambda(\mu X)$$
> Distributivity ($IV$):$$\Huge\forall X,Y\in M_{m\times n}(\Re),\forall\lambda,\mu\in\Re:$$$$\Huge (\lambda+\mu)X=\lambda X+\mu X,\,\,\lambda(X+Y)=\lambda X+\lambda Y$$

# Matrix multiplication:

Matrix multiplication is a function that takes two matrices as input, and outputs a third matrix. Both matrices have to share the dimension parameter $n$. That is, however tall one matrix is, the other must be just as wide??:$$\Huge \times:M_{m\times n}(\Re)\times M_{n\times p}(\Re)\mapsto M_{m\times p}(\Re)$$
It is defined for $A=(a_{i,j})_{m\times n},B=(b_{i,j})_{n\times p}$:
$$\Huge (AB)_{i,j}=a_{i1}b_{j1}+a_{i2}b_{j2}+\dots+a_{in}b_{jn}=\sum_{k=1}^na_{ik}b_{jk}$$

# Axioms of matrix multiplication:

Let $\lambda, \lambda^{'} \in\Re$, $X, X^{'}\in M_{m\times n}(\Re)$, $Y, Y^{'}\in M_{n\times p}(\Re)$, $Z\in M_{p\times q}(\Re)$:
> Existence of zero ($I$):$$\Huge 0_{p\times m}X=0_{p\times n},\,\,X0_{n\times p}=0_{m\times p}$$
> Existence of one (identity $II$):$$\Huge I_mX=X=XI_n$$
> Scalar associativity ($III$):$$\Huge \lambda(XY)=(\lambda X)Y=X(\lambda Y)$$
> Associativity ($IV$):$$\Huge (XY)Z=X(YZ)$$
> Distributivity ($V$):$$\Huge (X+X^{'})Y=XY+X^{'}Y,\,\,X(Y+Y^{'})=XY+XY^{'}$$$$\Huge \lambda(X+X^{'})=\lambda X+\lambda X^{'},\,\,(\lambda+\lambda^{'})X=\lambda X+\lambda^{'}X$$

Associativity is not intuitive, so it is proven by the following:
$$\large((XY)Z)_{i,j}=\sum_{k=1}^p(xy)_{ki}z_{kj}=\sum_{k=1}^p\left(\sum_{r=1}^nx_{ir}y_{kr}\right)z_{kj}=\sum_{k=1}^p\sum_{r=1}^nx_{ir}y_{kr}z_{kj}$$
$$\large (X(YZ))_{i,j}=\sum_{r=1}^nx_{ir}(yz)_{jr}=\sum_{r=1}^nx_{ir}\left(\sum_{k=1}^py_{kr}z_{kj}\right)=\sum_{r=1}^n\sum_{k=1}^px_{ir}y_{kr}z_{kj}$$
$$\large\sum_{k=1}^p\sum_{r=1}^nx_{ir}y_{kr}z_{kj}=\sum_{r=1}^n\sum_{k=1}^px_{ir}y_{kr}z_{kj},\,\text{interchanging order of summation}$$
$$\Huge \text{so}\,\,((XY)Z)_{i,j}=(X(YZ))_{i,j}\,,\,\,(XY)Z=X(YZ)$$

In general, $XY\neq YX$. This is because if $X\in M_{m\times n}(\Re),\,Y\in M_{n\times p}(\Re)$, then $XY$ is well defined, however $YX$ is only defined if $m=p$. If $m=p$, but $p\neq n$ then $XY$ and $YX$ will have different dimensions. Also if $XY=0_{m\times n}$, it is not necessarily the case that either $X$ or $Y$ are the zero matrix for their given dimensions.

# Inverses:

If $A\in M_n(\Re)$, $A$ is invertible or non-singular if and only if there exists such a matrix $B\in M_n(\Re)$ that satisfies $AB=I_n=BA$. If $B$ exists, it is called the inverse of $A$, $B=A^{-1}$. If no such $B$ exists, then $A$ does not have an inverse and is called a singular matrix.