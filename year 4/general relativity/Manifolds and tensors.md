
# Introducing tensors:
In our quest to formulate straight lines, we could consider another [[Special relativity#Curves and $4$-vectors|vector]]-like object: the gradient of a function. This can be thought of as the normal to the surface $f=\text{constant}$. For a function $f(x^\mu)$, it's gradient $\partial_\mu f$ is a vector:$$\Huge\tilde\partial_\mu f=\frac{\partial x^\nu}{\partial \tilde x^\mu}\partial_\nu f$$Compared to a $4$-vector $(\tilde V^\mu=\frac{\partial \tilde x^\mu}{\partial x^\nu}V^\nu)$, we see that the gradient transforms in the opposite way. The set of all such vectors forms a vector space, called the cotangent space as it is the dual space to the tangent space. General elements in this space are called covectors. 

Given an element of the tangent space $\omega_\mu$ and an element of the cotangent space $V^\mu$, the product $\omega_\mu V^\mu$ is simply a scalar, independent of coordinates. We can therefore think of cotangent vectors as linear maps from vectors to numbers or visa versa. In order to form an invariant object from two tangent vectors, one must introduce the metric $\eta_{\mu\nu}$. We can also think of an inner product as defining a map from the vector space to its dual, for each tangent vector $W^\nu$ we can define its covector $\omega_\rho=\eta_{\rho\nu}W^\nu$.

If $\omega_\mu=\partial_\mu f$ and $V^\mu=\frac{dx^\mu}{d\lambda}$, the product$$\Huge V^\mu\omega_\mu=\frac{dx^\mu}{d\lambda}\partial_\mu f=\frac{df}{d\lambda}$$can be interpreted as the gradient of $f$ along the curve $x^\mu(\lambda)$. Both vectors and covectors transform linearly under coordinate transformations. Tensors are simply more general objects described in terms of a set of components that transform linearly under coordinate transformations.

Consider linear maps from the tangent space to itself in the most general sense, $W=T(V)$. Given a basis on the vector space, such maps can be represented by a matrix:$$\Huge W^\mu=T^\mu_\nu V^\nu$$This should be independent of basis, and therefore coordinates, so we require $\tilde W_\mu=\tilde T^\mu_\nu\tilde V^\nu$ for some matrix $\tilde T^\mu_\nu$. This implies:$$\Huge \tilde T^\mu_\nu=\frac{\partial \tilde x^\mu}{\partial x^\rho}T^\rho_\sigma\frac{\partial x^\sigma}{\partial \tilde x^\nu}$$As a consequence of this:$$\Large\begin{aligned}
\implies\tilde W^\mu&=\left(\frac{\partial \tilde x^\mu}{\partial x^\rho}T^\rho_\sigma\frac{\partial x^\sigma}{\partial \tilde x^\nu}\right)\left(\frac{\partial \tilde x^\nu}{\partial x^\beta}V^\beta\right)\\
&=\frac{\partial \tilde x^\mu}{\partial x^\rho}T^\rho_\sigma\delta^\sigma_\beta V^\beta\\
&=\frac{\partial \tilde x^\mu}{\partial x^\rho}(T^\rho_\sigma V^\sigma)=\frac{\partial \tilde x^\mu}{\partial x^\rho}W^\rho
\end{aligned}$$As required. In matrix notation, this is equivalent to $\tilde T=\Lambda T\Lambda^{-1}$. The index position is used to keep track of how an object transforms under coordinate transformations. For example, $T^\mu_\nu$ behaves like a vector in the upper index and like a covector in the lower index.
> Such objects are $[1,1]$ tensors ($1$ up index, $1$ down index)
> Vectors are $[1,0]$ tensors
> Covectors are $[0,1]$ tensors
> Scalars are $[0,0]$ tensors

These objects are so useful since they allow us to make coordinate-independent statements. Tensor equations are linear relations between components of tensors of same type. As these equations are independent of coordinate system, they are true in all coordinate systems if they are true in one. 

### Tensor equation rules:
> All quantities must be components of tensors
> The number and positions of free indices in each term must match so that tensorts of the same type are related (i.e. $V^\mu=\omega_\mu$ is not valid)
> Terms may have an arbitrary number of contracted indices, however must appear in pairs of up and down. That is, the sum implied by $V^\mu=T^\mu_\nu\lambda_\nu$ is invalid as $\lambda$ should have an upper $\nu$ index
> Indices may be renamed
> Order of tensors does not matter