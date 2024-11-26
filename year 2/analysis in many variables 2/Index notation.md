The vector $\underline c=\underline a+\underline b$ is written as $c_i=a_i+b_i$ in index notation, where it is understood that the equation holds for $i\in\{1,\dots,n\}$. An index that appears once in each term is called a free index. An index that appears exactly twice in the same term is called a dummy index, and always implies summation.
# Scalar products:

In index notation, the scalar product is written as:$$\Huge \underline a\cdot\underline b=a_jb_j$$Where the repeated index implies a summation from $j=1$ to $j=n$. This form of the scalar product is called the Einstein summation convention. Here, $j$ is a dummy index. For example:$$\Huge (\underline a\cdot \underline b)(\underline c\cdot \underline d)=a_jb_jc_kd_k=\left(\sum_{j=0}^na_jb_j\right)\left(\sum_{k=0}^nc_kd_k\right)$$A more complex example is:$$\Huge\begin{align}
&\underline u+(\underline a\cdot \underline b)\underline v=|\underline a|^2(\underline b\cdot \underline v)\underline a\\
\iff&u_i+(\underline a\cdot \underline b)v_i=|\underline a|^2(\underline b\cdot \underline v)a_i\\
\iff&u_i+a_jb_jv_i=a_ja_jb_kv_ka_i
\end{align}$$Another way to write the scalar product is in quadratic form:$$\Huge\underline a\cdot\underline b=\begin{pmatrix}a_1&\dots&a_n\end{pmatrix}\begin{pmatrix}1&\dots&0\\\vdots&\ddots&\vdots\\0&\dots&1\end{pmatrix}\begin{pmatrix}b_1\\\vdots\\b_n\end{pmatrix}$$In index notation, this is equivalent to:$$\Huge \underline a\cdot\underline b=\delta_{ij}a_ib_j$$Where $\delta$ is the [[Matrix definition#Special matrices|Kronecker delta]] function, the $(i,j)$th element of the identity matrix. We propose that multiplying an expression with free index $i$ by $\delta_{ij}$ is equivalent to replacing $i\rightarrow j$:$$\Huge a_i\delta_{ij}=a_1\delta_{1j}+\dots+a_n\delta_{nj}$$Where we have used the implied summation with $i$ becoming a dummy index. Now $j$ is a free index, and the RHS expression will only have one non-zero term because of the Kronecker delta function:$$\Huge a_i\delta_{ij}=0+\dots+a_j\delta_{jj}+\dots+0=a_j$$For example, $\delta_{ij}\delta_{jk}$ has free indices $i,k$ and dummy index $j$. So multiplying $\delta_{ij}$ by $\delta_{jk}$ is equivalent to replacing $j\rightarrow k$ in $\delta_{ij}$ by the above, so we have:$$\Huge \delta_{ij}\delta_{jk}=\delta_{ik}$$Also $\delta_{ij}\delta_{ji}$ has no free index and two dummy indices $i,j$. We apply the above proposition with $a_j=\delta_{ij}$, so we replace $j\rightarrow i$:$$\Huge \delta_{ij}\delta_{ji}=\delta_{ii}=1+\dots+1=n$$Alternatively, note that $\delta_{ji}=\delta_{ij}$ so a replacement $i\rightarrow j$ will also give the above answer.

# Vector products:

In $\Re^3$ we can write $\underline a\times\underline b$ in index notation using the alternating tensor or Levi-Civita symbol:$$\Huge \epsilon_{ijk}=\begin{cases}0&\text{if any }i,j,k\text{ are equal}\\+1&\text{if }(ijk)=(123),(231),(312)\\-1&\text{if }(ijk)=(132),(321),(213)\end{cases}$$This is $+1$ when $(ijk)$ is a cyclic permutation of $(123)$ and $-1$ when $(ijk)$ is an anti-cyclic permutation of $(123)$. This allows us to write:$$\Huge (\underline a\times\underline b)_i=\epsilon_{ijk}a_jb_k$$Here, $i$ is the free index and $j,k$ are dummy indices. We show the first component:$$\Huge\begin{align}
\epsilon_{1jk}a_jb_k&=\epsilon_{11k}a_1b_k+\epsilon_{12k}a_2b_k+\epsilon_{13k}a_kb_k\\
&=0+\epsilon_{122}a_2b_2+\epsilon_{123}a_2b_3+\epsilon_{131}a_3b_1+\epsilon_{132}a_3b_1+\epsilon_{133}a_3b_3\\
&=a_2b_3-a_3b_3\\
&=(\underline a\times\underline b)\cdot\underline e_1
\end{align}$$We can also use this to show $\underline a\cdot(\underline b\times\underline c)=\underline c\cdot(\underline a\times\underline b)$:$$\Huge\begin{align}
\underline a\cdot(\underline b\times\underline c)&=a_i(\underline b\times\underline c)_i\\
&=a_i(\epsilon_{ijk}b_jc_k)\\
&=\epsilon_{ijk}a_ib_jc_k\\
&=\epsilon_{kij}a_ib_jc_k\\
&=c_k(\epsilon_{kij}a_ib_j)\\
&=c_k(\underline a\times \underline b)_k=\underline c\cdot(\underline a\times\underline b)
\end{align}$$There exists a useful identity for the product of two alternating tensors that share an index, called the $\epsilon-\delta$ identity:$$\Huge \epsilon_{ijk}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$$To prove this, we consider the three cases for the LHS term:$$\Huge \epsilon_{ijk}\epsilon_{klm}=\begin{cases}+1&\text{if }(klm)\text{ is an even permuation of }(ijk)\\-1&\text{if }(klm)\text{ is an odd permutation of }(ijk)\\0&\text{otherwise}\end{cases}$$So we have:$$\Huge\begin{align} 
\epsilon_{ijk}\epsilon_{klm}&=\delta_{ik}\delta_{jl}\delta_{km}-\delta_{ik}\delta_{jm}\delta_{kl}+\delta_{il}\delta_{jm}\delta_{kk}\\
&-\delta_{il}\delta_{jk}\delta_{km}+\delta_{im}\delta_{jk}\delta_{kl}-\delta_{im}\delta_{jl}\delta_{kk}\\
&=\delta_{im}\delta_{jl}-\delta_{il}\delta_{jm}+3\delta_{il}\delta_{jm}-\delta_{il}\delta_{jm}+\delta_{im}\delta_{jl}-3\delta_{im}\delta_{jl}\\
&=(3-2)\delta_{il}\delta_{jm}-(3-2)\delta_{im}\delta_{jl}\\
&=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}
\end{align}$$We can use this to prove the vector triple product, $\underline a\times(\underline b\times\underline c)=(\underline a\cdot\underline c)\underline b-(\underline a\cdot\underline b)\underline c$:$$\Huge\begin{align}
(\underline a\times(\underline b\times\underline c))_i&=\epsilon_{ijk}a_j(\underline b\times\underline c)_k\\
&=\epsilon_{ijk}a_j(\epsilon_{klm}b_lc_m)\\
&=\epsilon_{ijk}\epsilon_{klm}a_jb_lc_m\\
&=(\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl})a_jb_lc_m\\
&=\delta_{il}\delta_{jm}a_jb_lc_m-\delta_{im}\delta_{jl}a_jb_lc_m\\
&=(\delta_{il}b_l)(\delta_{jm}c_m)a_j-(\delta_{im}c_m)(\delta_{jl}b_l)a_j\\
&=b_ic_ja_j-c_ib_ja_j\\
&=(a_jc_j)b_i-(a_jb_j)c_i=(\underline a\cdot\underline c)b_i-(\underline a\cdot \underline b)c_i
\end{align}$$
# Derivatives:

In index notation, we can write derivatives of scalar and vector fields:
> $\underline{\nabla}g$, the [[Differential operators|gradient]] of the scalar field $g$:$$\Huge (\underline{\nabla}g)_i=\frac{\partial g}{\partial x_i}$$
> $\underline{\nabla}\cdot\underline f$, the [[Differential operators#Differentiating vector fields|divergence]] of the vector field $\underline f$:$$\Huge \underline{\nabla}\cdot\underline f=\frac{\partial f_j}{\partial x_j}$$
> $\underline{\nabla}\times\underline f$, the [[Differential operators#Differentiating vector fields|curl]] of the vector field $\underline f$:$$\Huge (\underline{\nabla}\times\underline f)_i=\epsilon_{ijk}\frac{\partial f_k}{\partial x_j}$$

Using this notation, we can verify $\underline{\nabla}\cdot(\underline{\nabla}\times\underline f)=0$:$$\Huge\begin{align}
\underline{\nabla}\cdot(\underline{\nabla}\times\underline f)&=\frac{\partial }{\partial x_j}(\underline{\nabla}\times\underline f)_j\\
&=\frac{\partial }{\partial x_j}\epsilon_{jkl}\frac{\partial f_l}{\partial x_k}\\
&=\epsilon_{jkl}\frac{\partial^2f_l}{\partial x_j\partial x_k}\\
&=\epsilon_{kjl}\frac{\partial^2 f_l}{\partial x_j\partial x_k}\\
&=-\epsilon_{jkl}\frac{\partial^2f_l}{\partial x_j\partial x_k}=-\underline{\nabla}\cdot(\underline{\nabla}\times\underline f)
\end{align}$$Since the expression is equal to its additive inverse, it must be equal to zero. One can also prove other [[Differential operators#Product rules|product rules]] for vector and scalar fields using index notation to give a neater and simpler proof. Note that the operator $(\underline g\cdot\underline{\nabla})\underline f$ has $i$th cartesian component $g_j\frac{\partial f_i}{\partial x_j}$ and can be defined as:$$\Huge (\underline g\cdot\underline{\nabla})\underline f=\lim_{d(S)\to0}\frac{1}{|V|}\oint_S\underline f(\underline g\cdot\underline{\hat{n}})dS$$
> $\underline{\nabla}\times(\underline f\times\underline g)=(\underline g\cdot\underline{\nabla})\underline f-(\underline f\cdot\underline{\nabla})\underline g+\underline f(\underline{\nabla}\cdot\underline g)-\underline g(\underline{\nabla}\cdot\underline f)$
> $\underline{\nabla}(\underline f\cdot\underline g)=(\underline g\cdot\underline{\nabla})\underline f+(\underline f\cdot\underline{\nabla})\underline g+\underline f\times(\underline{\nabla}\times\underline g)+\underline g\times(\underline{\nabla}\times\underline f)$

# Second derivatives:

