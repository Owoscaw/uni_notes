
# The Lorentz group and its [[Lie Groups and Algebras#Lie algebras|Lie algebra]]:

The Lorentz group is one of the most important Lie groups in physics, it arises in a similar way to most of the groups we have previously discussed. In this case, it arises from a symmetry group that respects some quadratic form, the "invariant length" of [[Lorentz transformations#Time dilation and length contraction|special relativity]].

The fundamental postulate of relativity is that the speed of light is the same in all inertial frames. Let us take two points $\underline{p},\underline{q}$ in space-time through which a ray of light passes and assume that they have coordinates $t_\underline{p},\underline{x}_\underline{p}$ and $t_\underline{q},\underline{x}_\underline{q}$ in one inertial frame and coordinates $t_\underline{p}',\underline{x}_\underline{p}'$ and $t_\underline{q}',\underline{x}_\underline{q}'$ in another. Hence we require:$$\Huge c^2=(\underline{x}_\underline{p}-\underline{x}_\underline{q})^2/(t_\underline{p}-t_\underline{q})^2=(\underline{x}_\underline{p}'-\underline{x}_\underline{q}')^2/(t_\underline{p}'-t_\underline{q}')^2$$That is:$$\Huge -c^2(t_\underline{p}-t_\underline{q})^2+(\underline{x}_\underline{p}-\underline{x}_\underline{q})^2=0$$must be invariant under a change of frames. It is not hard to find a coordinate transformation that satisfies this (a rotation in $SO(3)$ acting on purely spatial coordinates works). If time is involved in the coordinate chance, we need to take the relative minus sign into account. A example of this would be acting with the matrix:$$\Huge\Lambda_{01}=\begin{pmatrix}\cosh(\lambda) & -\sinh(\lambda) & 0 & 0 \\ -\sinh(\lambda) & \cosh(\lambda) & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}$$One can check that this keeps $-(ct)^2+x_1^2$ invariant:$$\large\begin{align*}
-(ct)^2+x_1^2&\to-(ct')^2+(x_1')^2\\
&=-(\cosh(\lambda)ct-\sinh(\lambda)x_1)^2+(-\sinh(\lambda)ct+\cosh(\lambda)x_1)^2\\
&=-(ct)^2(\cosh^2(\lambda)-\sinh^2(\lambda))+x_1^2(\cosh^2(\lambda)-\sinh^2(\lambda))\\
&=-(ct)^2+x_1^2
\end{align*}$$as required. Note that the origin of the primed system at $x_1'=0$ satisfies:$$\Huge -\sinh(\lambda)ct+\cosh(\lambda)x_1=0$$so that it moves in the regular system with velocity:$$\Huge v=x_1/t=c\frac{\sinh(\lambda)}{\cosh(\lambda)}=c\tanh(\lambda)=c\frac{e^\lambda-e^{-\lambda}}{e^\lambda+e^{-\lambda}}<c$$For this reason, $\lambda$ is called the rapidity. Instead of using such transformations to find time dilation, we examine the structure this induces.

The Lorentz group $L$ is the group of linear maps on $\Re^4$ that preserve the quadratic form:$$\Huge|x|^2_M=-(x^0)^2+(x^1)^2+(x^2)^2+(x^3)^2$$where $(ct,x,y,z)=(x^0,x^1,x^2,x^3)$. $\Re^4$ equipped with this quadratic form is also called $\Re^{1,3}$ or [[Spacetime and Tensors#Minkowski space|Minkowski space]]. It is appropriate to then call the Lorentz group $O(1,3)$. We have seen that the principle of relativity is obeyed under $\Re^3$ rotations as well as "boosts" which mediate between relatively moving systems.

For two coordinate systems with a relative velocity $v$, the coordinate change is defined as a boost. A boost associated with two relatively moving inertial frames with relative speed $v$ is a Lorentz transformation $B$ with $B(\underline{v})_0^0=\cosh(\lambda),B(\underline{v})_0^i=-v^i/c\cosh\lambda$ and:$$\Huge B(\underline{v})_k^i=\delta_k^i+\frac{(\cosh\lambda)^2}{1+\cosh\lambda}\frac{v^iv^k}{c^2}$$where $\tanh\lambda=|\underline{v}|/c$. 

In order to facilitate the preservation of the minus sign in this definition, we define $(ct,x,y,z)=(x^0,x^1,x^2,x^3)$ as the four vector of coordinates combining spatial and temporal coordinates:$$\Huge x_\mu=\eta_{\mu\nu}x^\nu,\,\,\eta=\begin{pmatrix}-1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}$$using summation convention. $\eta$ is clearly self inverse and satisfies:$$\Huge x^\mu=\eta^{\mu\nu}x_\nu$$Note that:$$\Huge\eta_{\mu\nu}\eta^{\nu\rho}=\delta_\mu^\rho$$These definitions allow us to write the length $|x|_M$ of a vector in Minkowski space as:$$\Huge |x|_M^2=x^\mu x^\nu\eta_{\mu\nu}=x_\mu x^\mu=x_\mu x_\nu\eta^{\mu\nu}$$
Let $\Lambda$ have components $\Lambda_\nu^\mu$ and assume $\Lambda$ linearly maps a four vector $\underline{x}$ to another $\underline{x}'$ by:$$\Huge (x^\mu)'=\Lambda_\sigma^\mu x^\sigma$$Now if $\Lambda$ is in the Lorentz group, we require $|x'|_M^2=|x|_M^2$:$$\Huge |x'|_M^2=\Lambda_\sigma^\mu x^\sigma\Lambda_\rho^\nu x^\rho\eta_{\mu\nu}=x^\sigma x^\rho\Lambda_\sigma^\mu\eta_{\mu\nu}\Lambda_\rho^\nu=x^\mu x^\nu\eta_{\mu\nu}$$or, equivalently:$$\Huge \Lambda_\sigma^\mu\Lambda_\rho^\nu\eta_{\mu\nu}=\eta_{\sigma\rho}$$or, in matrix notation:$$\Huge\Lambda^T\eta\Lambda=\eta\implies\eta\Lambda^T\eta=\Lambda^{-1}$$We can use this result to find:$$\Huge \Lambda\eta\Lambda^t=\eta$$as well. Therefore $\Lambda$ is the same as $\Lambda^{-1}$ up to the insertion of $\eta$ matrices. We then have the transformation behaviour:$$\Huge\begin{align*}
x^\mu\to(x^\mu)'&=\Lambda_\nu^\mu x^\nu\\
x_\mu=\eta_{\mu\rho}x^\rho\to x_\mu'&=\eta_{\mu\rho}(x^\rho)'\\
&=\eta_{\mu\rho}\Lambda_\nu^\rho x^\nu\\
&=\eta_{\mu\rho}\Lambda_\nu^\rho\eta^{\nu\sigma}x_\sigma\\
&=x_\sigma(\eta\Lambda^T\eta)_\mu^\sigma\\
&=x_\sigma(\Lambda^{-1})_\mu^\sigma
\end{align*}$$
Objects $x^\mu$ transforming as above are called Lorentz vectors, while objects transforming like $x_\mu$ are called Lorentz covectors. We can think of the matrix $\eta$ as a map that sends every vector to a covector and vice-versa.

Whenever we contract upper and lower indices, we have get something that is invariant under the Lorentz group. By extension, it is customary to put upper/lower indices on objects that have the same transformation behaviour as $x^\mu,x_\mu$. The same rule for constructing invariants then exists there as well.

Let us now examine the global structure of the Lorentz group $L$. Clearly, the determinant of $\Lambda$ is $\pm1$, so we get two disconnected components $L_\pm$ as we did for $SO(3)$. The component $L_+$ connected to the identity is called the proper Lorentz group. Furthermore $(0,0)$ component of $\eta\Lambda^T\eta\Lambda=\mathbb{1}$ implies that:$$\Huge 1=(\Lambda_0^0)^2-(\Lambda_1^0)^2-(\Lambda_2^0)^2-(\Lambda_3^0)^2$$so that $(\Lambda_0^0)^2\geq1$ which again has two components:
> $L^\uparrow$ where $\Lambda_0^0\geq1$ are called the orthochronous Lorentz transformations
> $L^\downarrow$ where $\Lambda_0^0\leq-1$ are called the non-orthochronous Lorentz transformations

The orthochronous transformations keep the flow of time in the same direction. We therefore have four components. The maps $\Lambda_T=\text{diag}(-1,1,1,1)$ (time reversal) and $\Lambda_P=\text{diag}(1,-1,-1,-1)$ (parity) generate the whole group together with $L^\uparrow_+$. We can use $\Lambda_T,\Lambda_P,\Lambda_T\Lambda_P$ to map any group element to $L_+^\uparrow$, which implies we can write any group element in $L$ as a product of $\Lambda\in L_+^\uparrow$ with $\Lambda^a_T\Lambda^b_P$ for $a,b\in(0,1)$.  

The component of $L$ that is continuously connected to the identity is the proper orthochronous Lorentz group $L_+^\uparrow$ which admits the following decomposition:
> We propose that every proper orthochronous Lorentz transformation $\Lambda\in L_+^\uparrow$ has a unique decomposition as:$$\Huge\Lambda=B(\underline{v})\begin{pmatrix}1 &  \\  & R\end{pmatrix}$$where $B(\underline{v})$ is a boost with parameter:$$\Huge v^i/c=\Lambda_0^i/\Lambda_0^0$$and $R$ is an element of $SO(3)$ given by:$$\Huge R^{ik}=\Lambda^i_k-\frac{1}{1+\Lambda_0^0}\Lambda_0^i\Lambda_k^0$$
> To prove this, first observe that:$$\Huge\sum_i(\Lambda_0^i/\Lambda_0^0)^2=\frac{(\Lambda_0^0)^2-1}{(\Lambda_0^0)^2}<1$$
> A boost associated to the speed $\underline{v}/c$ hence makes sense. By the definition of a boost, it follows that $B_0^0(\underline{v})=\cosh\lambda=\Lambda_0^0$ and $B_i^0(\underline{v})=-v^i/c\cosh\lambda=\Lambda_i^0$ and hence:$$\Huge B_j^i(\underline{v})=\delta_j^i+\frac{1}{1+\Lambda_0^0}\Lambda_i^0\Lambda_j^0$$
> We now show that $$\Huge \mathcal{R}=B(-\underline{v})\Lambda=B^{-1}(\underline{v})\Lambda$$is indeed a rotation and $\mathcal{R}=1\oplus R$, which finishes the proof:$$\Huge \begin{align*}
\mathcal{R}_0^0&=(\Lambda_0^0)^2-\sum_i(\Lambda_0^i)^2=1\\
\mathcal{R}_i^0&=\Lambda_0^0\Lambda_i^0-\sum_j\Lambda_0^j\Lambda_i^j=0\\
\mathcal{R}_k^i&=\Lambda_k^i-\frac{1}{1+\Lambda_0^0}\Lambda_0^i\Lambda_k^0
\end{align*}$$where we use $\Lambda^T\eta\Lambda=\eta$ repeatedly. This is a rotation with the right block-diagonal structure as claimed.

To understand the global structure of $L_+^\uparrow=SO(1,3)_\uparrow$, we can repeat the trick we used when describing the relationship between $SO(3)$ and $SU(2)$. For a four vector we write it as a matrix $M_x$ with $M_x^\dagger=M_x$:$$\Huge M_x=\begin{pmatrix}x^0+x^3 & x^1-ix^2 \\ x^1+ix^2 & x^0-x^3\end{pmatrix}$$We can now formulate a map $SL(2,\mathbb{C})\rightarrow L$ by sending $g\in SL(2,\mathbb{C})$:$$\Huge g\rightarrow F(g),\,\,F(g)M_x=gM_xg^\dagger$$We propose that this is a surjective group homomorphism from $SL(2,\mathbb{C})$ to $L_+^\uparrow$.

Finally, we can find the Lie algebra of the Lorentz group. As we have seen, a general Lorentz transformation is uniquely given in terms of an element of $SO(3)$ and a boost. We hence conclude that the Lorentz group is a real six-dimensional manifold, which fits with the fact that a real $4\times4$ matrix has $16$ components and $\Lambda^T\eta\Lambda=\eta$ imposes $10$ independent constraints. Using rotation and boost matrices gives us paths in the group, and one can show that the Lie algebra is generated by the six matrices:$$\large\begin{align*}
l^{01}&=\begin{pmatrix}0 & -1 & 0 & 0\\
-1 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\end{pmatrix},\,\,l^{02}=\begin{pmatrix}0 & 0 & -1 & 0\\
0 & 0 & 0 & 0\\
-1 & 0 & 0 & 0\\
0 & 0 & 0 & 0\end{pmatrix},\,\,l^{03}=\begin{pmatrix}0 & 0 & 0 & -1\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
-1 & 0 & 0 & 0\end{pmatrix}\\
l^{12}&=\begin{pmatrix}0 & 0 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & -1 & 0 & 0\\
0 & 0 & 0 & 0\end{pmatrix},\,\,l^{13}=\begin{pmatrix}0 & 0 & 0 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & 0 & 0\\
0 & -1 & 0 & 0\end{pmatrix},\,\,l^{23}=\begin{pmatrix}0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & -1 & 0\end{pmatrix}
\end{align*}$$Summarised by:$$\Huge (l^{\mu\nu})^\alpha_\beta=\eta^{\mu\alpha}\delta^\nu_\beta-\eta^{\nu\alpha}\delta^\mu_\beta$$Note that $\mu,\nu$ in the above label different elements of the Lie algebra, and $\alpha,\beta$ are the components of the corresponding matrix. One can find that they obey the Lie algebra:$$\Huge [l^{\mu\nu},l^{\rho\sigma}]=-\eta^{\mu\rho}l^{\nu\sigma}-\eta^{\nu\sigma}l^{\mu\rho}+\eta^{\mu\sigma}l^{\nu\rho}+\eta^{\nu\rho}l^{\mu\sigma}$$
# Representations of the Lorentz group:

Let us now investigate [[Representations#Definitions|representations]] of the Lorentz group. We already saw the defining representation$$\Huge x^\mu\rightarrow\Lambda_\nu^\mu x^\nu,\,\,\Lambda^T\eta\Lambda=\eta$$so that$$\Huge x^\mu x_\mu=x^\mu\eta_{\mu\nu}x^\nu=(-x^0)^2+(x^1)^2+(x^2)^2+(x^3)^2$$stays invariant. Now we ask about other representations of this group. Note that $SO(3)$ is a subgroup of $L_+^\uparrow$ and that the fundamental representation of its spin group, $SU(2)$, had physical significance as a spinor.

As $SO_+(1,3)=L_+^\uparrow$ has $SL(2,\mathbb{C})$ as a double covering group, we make the definition of the spin group $\text{Spin}(1,3)$ as the group equal to $SL(2,\mathbb{C})$. It is a fact of life that what matters to describing relativistic processes are representations of $SL(2,\mathbb{C})=\text{Spin}(1,3)$ instead of representations of $L$.

## Spinors of the Lorentz group:
For $SO(3)$ we found irreducible representations by using the Lie algebra of $SO(3)$, which is the same Lie algebra as $SU(2)$. Not all representations of this algebra were also representations of $SO(3)$, the extra ones were exactly the "spin $1/2$" spinorial representations of $SU(2)$ of physical significance. We use a similar strategy here, leading us to the spinors of the Lorentz group.

Recall the Lorentz algebra $$\Huge [l^{\mu\nu},l^{\rho\sigma}]=-\eta^{\mu\rho}l^{\mu\sigma}-\eta^{\mu\sigma}l^{\mu\rho}+\eta^{\mu\sigma}l^{\nu\rho}+\eta^{\nu\rho}l^{\mu\sigma}$$and let $\gamma^\mu$ for $\mu=0,1,2,3$ be matrices that obey the algebra$$\Huge \{\gamma^\mu,\gamma^\nu\}=\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu=2\eta^{\mu\nu}\mathbb{1}$$Then we construct a representation of the Lorentz algebra using the matrices$$\Huge S^{\mu\nu}=\frac{1}{4}[\gamma^\mu,\gamma^\nu]$$To prove that this is actually a representation of the algebra, we must check that the $S^{\mu\nu}$ satisfy the Lorentz algebra. First note that the relation $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$ implies $\gamma^\mu\gamma^\nu=-\gamma^\nu\gamma^\mu$ for $\mu\neq\nu$ and $(\gamma^\mu)^2=\eta^{\mu\mu}\mathbb{1}$. We can now work out the commutator of $[S^{\mu\nu},S^{\rho\sigma}]$. First note that $\mu\neq\nu$ and $\rho\neq\sigma$ as otherwise $S$ vanishes. Therefore $S^{\mu\nu}=\frac{1}{2}\gamma^\mu\gamma^\nu$ and $S^{\rho\sigma}=\frac{1}{2}\gamma^\rho\gamma^\sigma$. Let us assume $\mu,\nu,\rho,\sigma$ are all different$$\Huge \begin{align*}
[S^{\mu\nu},S^{\rho\sigma}]&=\frac{1}{4}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma-\gamma^\rho\gamma^\sigma\gamma^\mu\gamma^\nu)\\
&=\frac{1}{4}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma-\gamma^\mu\gamma^\rho\gamma^\sigma\gamma^\nu)\\
&=\frac{1}{4}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma-\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)=0
\end{align*}$$where we simply rearrange $\gamma$ matrices to produce two $-$ signs at a time. Now we assume that $\mu=\rho$:$$\Huge\begin{align*}
[S^{\mu\nu},S^{\rho\sigma}]&=\frac{1}{16}[[\gamma^\mu,\gamma^\nu],[\gamma^\rho,\gamma^\sigma]]\\
&=\frac{1}{16}[[\gamma^\mu,\gamma^\nu],[\gamma^\mu,\gamma^\sigma]]\\
&=\frac{1}{16}[2\gamma^\mu\gamma^\nu,2\gamma^\mu\gamma^\sigma]\\
&=\frac{1}{4}(\gamma^\mu\gamma^\nu\gamma^\mu\gamma^\sigma-\gamma^\mu\gamma^\sigma\gamma^\mu\gamma^\nu)\\
&=\frac{1}{4}(-(\gamma^\mu)^2\gamma^\nu\gamma^\sigma+(\gamma^\mu)^2\gamma^\sigma\gamma^\nu)=-\eta^{\mu\mu}S^{\nu\sigma}
\end{align*}$$which is exactly what we saw in the algebra with $\mu=\rho$. The other cases are proven similarly.

Algebras of the type $\{\gamma^a,\gamma^b\}=2\eta^{ab}$ where $\eta^{ab}$ is a symmetric diagonal matrix with entries $\pm1$ are known as Clifford algebras. We saw an example of this in the Pauli matrices, which obey a Clifford algebra generated by three elements with $\eta^{ab}=\text{diag}(1,1,1)$.

When trying to find explicit examples of the four $\gamma^\mu$ for $\mu=0,1,2,3$, the above remark is a useful hint. It turns out we need at least $4\times4$ matrices, one possible choice being the Dirac matrices. We define the Dirac matrices as$$\Huge \gamma^0=\begin{pmatrix}0 & \mathbb{1}_2 \\ -\mathbb{1}_2 & 0\end{pmatrix},\,\,\gamma^i=\begin{pmatrix}0 & \sigma_i \\ \sigma_i & 0\end{pmatrix},\,\,i=1,2,3$$where $\sigma_i$ are the Pauli matrices$$\Huge \sigma_1=\begin{pmatrix}0 & 1  \\ 1 & 0\end{pmatrix},\,\,\sigma_2=\begin{pmatrix}0 & -i \\ i & 0\end{pmatrix},\,\,\sigma_3=\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$$
We propose that the Dirac matrices obey $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}\mathbb{1}_4$. Using the Dirac matrices, the algebra generators $S^{\mu\nu}$ are therefore$$\Huge S^{0i}=\frac{1}{2}\begin{pmatrix}\sigma_i & 0 \\ 0 & -\sigma_i\end{pmatrix},\,\,S^{jk}=\frac{i}{2}\epsilon_{jkl}\begin{pmatrix}\sigma_l & 0 \\ 0 & \sigma_l\end{pmatrix}$$Now we can define a vector $\psi\in\mathbb{C}^4$ transforming under $\text{Spin}(1,3)$ as$$\Huge \psi\rightarrow\psi'=e^{S^{\mu\nu}\theta_{\mu\nu}}\psi=\Lambda_{1/2}\psi,\,\,\theta_{\mu\nu}\in\Re$$We call this a Dirac spinor. Note that a Dirac spinor transforms in a reducible representation, as the matrices $S^{\mu\nu}$ are block-diagonal. The irreducible representations we find by restricting to the blocks are called the Weyl spinors:

Decomposing $\psi=(\psi_L,\psi_R)$, the objects $\psi_L,\psi_R$ are called the left-handed and right-handed Weyl spinors respectively.

Having defined this representation of the Lorentz group (really a representation of the Lorentz group's spin group), we ask how we can construct Lorentz scalars out of it. Let us denote the complex conjugate of $\psi$ by $\psi^*$. Then an obvious guess would be$$\Huge \psi^*\cdot\psi=\psi_I^*\psi_I$$where $\psi_I$ are the components of $\psi$. The problem here is that$$\Huge \Lambda_{1/2}^\dagger\neq\Lambda_{1/2}^{-1}$$so we need a different guess. For a Dirac spinor $\psi$ with components $\psi_I$ and complex conjugate $\psi^*$, we let$$\Huge \bar\psi=\psi^*\gamma^0\implies\bar\psi_I=\psi_I^*\gamma^0_{IJ}$$then we have that$$\Huge\bar\psi\psi=\psi_I^*\gamma_{IJ}^0\psi_J$$is a Lorentz scalar. To prove this, observe that direct computation shows that$$\Huge\Lambda_{1/2}^\dagger\gamma^0=\gamma^0\Lambda_{1/2}^{-1}$$and so we work out$$\Huge\begin{align*}
\bar\psi\psi&=\psi^*\gamma^0\psi\\
\implies\psi^*\Lambda_{1/2}^\dagger\gamma^0\Lambda_{1/2}\psi&=\psi^*\gamma^0\Lambda_{1/2}^{-1}\Lambda_{1/2}\psi\\
&=\bar\psi\psi
\end{align*}$$as required.

For a Dirac spinor $\psi$ with components $\psi_I$, the expression$$\Huge \bar\psi\gamma^\mu\psi=\psi_I^*\gamma_{IJ}^0\gamma_{JK}^\mu\psi_K$$transforms as a Lorentz vector. Note that this means we can effectively take the $\mu$ index we gave the Dirac matrices seriously. Before showing this we need the following lemma:
> The matrices $\Lambda_{1/2}=e^{S^{\mu\nu}\theta_{\mu\nu}}$ satisfy$$\Huge \Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2}=\Lambda^\mu_\nu\gamma^\nu=(e^{l^{\rho\sigma}\theta_{\rho\sigma}})^\mu_\nu\gamma^\nu$$
> To prove this, we first show that$$\Huge [\gamma^\mu,S^{\rho\sigma}]=(l^{\rho\sigma})^\mu_\nu\gamma^\nu$$Here, $\rho,\sigma$ label the matrices $l$, while $\mu,\nu$ index each matrix. We saw that we can write this as$$\Huge (l^{\rho\sigma})^\mu_\nu=\eta^{\rho\mu}\delta_\nu^\sigma-\eta^{\sigma\mu}\delta^\rho_\nu$$We first take $\mu\neq\rho$ and $\mu\neq\sigma$. The the RHS vanishes and the LHS becomes$$\Huge 2[\gamma^\mu,\gamma^\rho\gamma^\sigma]=2(\gamma^\mu\gamma^\rho\gamma^\sigma-\gamma^\rho\gamma^\sigma\gamma^\mu)=0$$Now we take $\mu=\rho\neq\sigma$ and compute$$\Huge [\gamma^\mu,S^{\rho\sigma}]=2[\gamma^\mu,\gamma^\mu\gamma^\sigma]=\eta^{\mu\mu}\gamma^\sigma$$which is exactly the RHS of what we want to show. Finally we take $\mu=\sigma\neq\rho$ and compute$$\Huge [\gamma^\mu,S^{\rho\sigma}]=2[\gamma^\mu,\gamma^\rho\gamma^\mu]=-\eta^{\mu\mu}\gamma^\rho$$which, again, is exactly the RHS of what we want to show.
> This statement is equivalent to saying for very small $\theta_{\mu\nu}$$$\Huge(\mathbb{1}-S^{\rho\sigma}\theta_{\rho\sigma})\gamma^\mu(\mathbb{1}+S^{\rho\sigma}\theta_{\rho\sigma})=(\delta_\nu^\mu+(l^{\rho\sigma}\theta_{\rho\sigma})^\mu_\nu)\gamma^\nu$$
> We look at this equation considering the vector space of matrices spanned by the $\gamma^\mu$. We can write any element of such a vector space as $A=a_\mu\gamma^\mu$. The RHS can be understood as a linear map acting on $A$ to map it to$$\Huge A'=a_\mu(\delta^\mu_\nu+(l^{\rho\sigma}\theta_{\rho\sigma})^\mu_\nu)\gamma^\nu$$Then the equation dictates that we can also write this map as$$\Huge A'=(\mathbb{1}-S^{\rho\sigma}\theta_{\rho\sigma})A(\mathbb{1}+S^{\rho\sigma}\theta_{\rho \sigma})$$
> Applying this map $n$ times we find that$$\Huge (\mathbb{1}-S^{\rho \sigma}\theta_{\rho \sigma})^n\gamma_\mu(\mathbb{1}+S^{\rho \sigma}\theta_{\rho \sigma})^n=((\mathbb{1}+l^{\rho\sigma}\theta_{\rho\sigma})^n)_\nu^\mu\gamma^\nu$$and so$$\Huge\lim_{n\to\infty}(\mathbb{1}-S^{\rho\sigma}\theta_{\rho\sigma}/n)^n\gamma^\mu(1+S^{\rho\sigma}\theta_{\rho\sigma}/n)^n=\lim_{n\to\infty}((\mathbb{1}+l^{\rho\sigma}\theta_{\rho\sigma}/n)^n)_\nu^\mu\gamma^\nu$$which exactly gives us the exponential description of the matrix.

We can now prove that the expression before the lemma transforms as a Lorentz vector. This is now simple, as we simply work out$$\Huge\begin{align*}
\bar\psi\gamma^\mu\psi\rightarrow\psi^*\gamma^0\Lambda_{1/2}^{-1}\gamma^\mu\Lambda_{1/2}\psi&=\psi^*\gamma^0\Lambda^\mu_\nu\gamma^\nu\psi\\
&=\Lambda^\mu_\nu\bar\psi\gamma^\nu\psi
\end{align*}$$
A corollary of this theorem is that for a Lorentz vector $a^\mu$, the expression $a_\mu\bar\psi\gamma^\mu\psi=\bar\psi\not a\psi$ transforms as a Lorentz scalar. This is proven by the fact that we saw $a^\mu b^\mu$ for Lorentz vectors $a^\mu,b^\mu$ gives us a scalar. In the above theorem we saw that $b^\mu=\bar\psi\gamma^\mu\psi$ is a Lorentz vector, and so the statement follows.

## General Representation Theory:
Working with the Lie algebra $\pmb{so}(1,3)$ of $L_+^\uparrow$ reveals the following. Taking this as a Lie algebra over $\mathbb{C}$ instead of $\Re$ we can define$$\Huge\begin{align*}
A_1=\frac{1}{2}(-l^{23}+il^{01}),\,\,A_2&=\frac{1}{2}(l^{13}+il^{02}),\,\,A_3=\frac{1}{2}(-l^{12}+il^{03})\\
B_1=\frac{1}{2}(-l^{23}-il^{01}),\,\,B_2&=\frac{1}{2}(l^{13}-il^{02}),\,\,B_3=\frac{1}{2}(-l^{12}-il^{03})
\end{align*}$$which satisfy the Lie algebra$$\Huge [A_i,A_j]=\epsilon_{ijk}A_k,\,\,[A_i,B_j]=0,\,\,[B_i,B_j]=\epsilon_{ijk}B_k$$which is simply two copies of the lie algebra $\pmb{sl}(2,\mathbb{C})$. Hence the complexification of $\pmb{so}(1,3)$ is equal to $\pmb{sl}(2,\mathbb{C})\oplus\pmb{sl}(2,\mathbb{C}):\pmb{so}(1,3)\otimes\mathbb{C}$. 

We can classify the irreducible representations of $\pmb{so}(1,3)$ by taking a detour through $\pmb{so}(1,3)\otimes\mathbb{C}$, and it turns out that:
> The complex irreducible representations of $SL(2,\mathbb{C})$ are the tensor products $r_{s_1}\otimes\bar r_{s_2}$, labelled by pairs $(s_1,s_2)$ where $s_i$ take half-integer values. They act on a complex vector space of dimension $(2s_1+1)(2s_2+1)$.
> $(0,0)$ does not transform at all, it is a scalar
> $(1/2,0)$ is a Weyl spinor. This is a representation of $\text{Spin}(1,3)=SL(2,\mathbb{C})$ but not $SO(1,3)_\uparrow$.
> $(0,1/2)$ is another Weyl spinor.
> $(1/2,1/2)$ has dimension four and is a vector. It is the representation we used to define the Lorentz group. Its action is a surjective group homomorphism from $SL(2,\mathbb{C})$ to $L_+^\uparrow$.
> $(1/2,0)\oplus(0,1/2)$ is the reducible representation corresponding to a Dirac spinor.