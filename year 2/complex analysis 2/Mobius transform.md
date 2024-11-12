A Mobius map is a map of the form:$$\Huge M(z)=\frac{az+b}{cz+d}$$With $ad-bc\neq0$. Note that if $c=d=0$ this map is not defined at any point. Then if either $c\neq0$ or $d\neq0$, the condition $ad-bc=0$ suggests $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ has a zero [[Determinants and Adjoints#General definition|determinant]], and since the second row is not $\underline 0$ there must exists some $\alpha\in\Re$ such that $\alpha\begin{pmatrix}a&b\end{pmatrix}=\begin{pmatrix}c&d\end{pmatrix}$, that is $a=\alpha c$ and $b=\alpha d$, which implies $\frac{az+b}{cz+d}=\alpha$. So without this condition, the map is either constant or not defined anywhere.

Recall the General Linear Group defined to be:$$\Huge GL_2(\mathbb{C})=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}:a,b,c,d\in\mathbb{C}, ad-bc\neq0\right\}$$We can then define the Mobius transformation, given any $T\in GL_2$ we define $M_T:\mathbb{C}\mapsto\hat{\mathbb{C}}$ as :$$\Huge M_T(z)=\frac{az+b}{cz+d}$$If $cz+d\neq0$. If $cz+d=0$ we set $M_T\left(-\frac{d}{c}\right)=\infty$ when $c\neq0$. We can extend the map to $\hat{\mathbb{C}}$ by setting:$$\Huge M_T(\infty)=\begin{cases}\frac{a}{c}&c\neq0\\\infty&c=0\end{cases}$$This function is called the Mobius transform.

Note that $f(z)=\frac{1}{z}$ is a Mobius transform with $T=\begin{pmatrix}0&1\\1&0\end{pmatrix}$. Writing $z=re^{i\theta}$ we see that $f(z)=\frac{1}{r}e^{-i\theta}$. We see that the map takes segments of a circle with radius $r$ to a segment on a circle of radius $\frac{1}{r}$. Similarly, the map takes a ray of angle $\theta$ to a ray of angle $-\theta$. 

The set of Mobius transformations form a group under composition, furthermore:
> $M_{T_1}\circ M_{T_2}=M_{T_1T_2}$
> $(M_T)^{-1}=M_{T^{-1}}$
> For any $k\in\mathbb{C}^*$ we have that $M_{kT}=M_T$. We conclude that $M_T=I$ if and only if $T=k\begin{pmatrix}1&0\\0&1\end{pmatrix}$.

The third statement shows that Mobius transformations are only uniquely defined by a matrix up to a scalar constant. Since an inverse to $T$ always exists, any Mobius transformation is a bijection from $\hat{\mathbb{C}}$ to itself. 

If $c=0$ then the Mobius transformation $M_T$ gives a [[Complex differentiation#Biholomorphic|biholomorphic]] map $M_T:\mathbb{C}\tilde{\mapsto}\mathbb{C}$. If $c\neq0$ then $M_T$ gives a biholomorphic map $M_T:\mathbb{C}\setminus\left\{-\frac{d}{c}\right\}\tilde{\mapsto}\mathbb{C}\setminus\left\{\frac{a}{c}\right\}$.

The bijection property of the associated domains follows from the fact that $(M_T)^{-1}=M_{T^{-1}}$ and $T^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$. This inverse matrix automatically exists by the restriction for Mobius transforms. Since $(M_T)^{-1}$ is a Mobius map, it is sufficient to show that a Mobius map is holomorphic on its domain. If $c=0$ then $d\neq0$ and $M_T(z)=\frac{az+b}{d}$, which is a linear map and therefore holomorphic. If $c\neq0$:$$ M_T(z)=\frac{az+b}{cz+d}=\frac{\frac{a}{c}(cz+d-d)+b}{cz+d}=\frac{a}{c}+\frac{-\frac{a}{c}d+b}{cz+d}=\frac{a}{c}-\frac{ad-bc}{c(cz+d)}=\frac{a}{c}-\frac{\det T}{c(cz+d)}$$Which implies:$$\Huge M_T'(z)=\frac{\det T}{(cz+d)^2}$$So the derivative exists, making $M_T(z)$ holomorphic, and therefore biholomorphic.

# Finding Mobius transforms:

Since $M_T=M_{kT}$ for all $k\in \mathbb{C}^*$ there is redundancy in the variables, so intuitively there are only $3$ pieces of information required to construct a Mobius transform.

Given distinct points $z_0,z_1,z_2,z_3\in\mathbb{C}$, the cross ratio of these points is defined by:$$\Huge (z_0,z_1;z_2,z_3)=\frac{(z_0-z_2)(z_1-z_3)}{(z_0-z_3)(z_1-z_2)}$$This can be extended when one of the points is infinity by removing it:$$\Huge (\infty,z_1;z_2,z_3)=\frac{z_1-z_3}{z_1-z_2}$$
## Three point theorem:
Let $\{z_1,z_2,z_3\}$ and $\{w_1,w_2,w_3\}$ be two sets of ordered distinct points in $\hat{\mathbb{C}}$. Then there exists a unique Mobius transformation $f$ such that $f(z_i)=w_i$ for $i=1,2,3$.

The uniqueness of such transformation relies on the fixed point lemma. Let $T\in GL_2(\mathbb{C})$. If $M_T:\hat{\mathbb{C}}\mapsto \hat{\mathbb{C}}$ is not the identity map then $M_T$ has at most $2$ fixed points in $\hat{\mathbb{C}}$, where $z_0$ is a fixed point of the map $f$ if $f(z_0)=z_0$. In other words, if a Mobius transformation has three fixed points in $\hat{\mathbb{C}}$, then it is the identity.

To prove this, observe $z$ is a fixed point if and only if $z=M_T(z)=\frac{az+b}{cz+d}$. This rearranges to give $cz^2+(d-a)z-b=0$. If $c\neq0$ this is a quadratic equation with $2$ solutions in the complex plane. If $c=0$ and $d\neq a$ there is only one solution with $z=\frac{b}{d-a}$. If $d=a$ then $b=0$, which implies that $T$ is the identity up to a scalar multiplier. So we have the fixed point lemma as required.

We show the existence of the Mobius transformation under the three point theorem. Define $F(z)=(z_1,z_1;z_2,z_3)$. $F$ is a Mobius transformation with $T=\begin{pmatrix}k&-k\\1&-1\end{pmatrix},k=\frac{z_1-z_3}{z_1-z_2}$. Note that $F(z_1)=1,F(z_2)=0,F(z_3)=\infty$. Similarly define $G=(w_1,w_1;w_2,w_3)$ and we get analogous results to $F$. We see that $F(z_i)=\{1,0,\infty\}=G(w_i)$ so we can then define the map $G^{-1}\circ F$ to be the Mobius transform that maps from $z_i$ to $w_i$:$$\Huge G^{-1}\circ F(z_i)=w_i$$We have shown the existence of such a Mobius map. We now show uniqueness. Assume $M_1$ and $M_2$ are Mobius such that $M_1(z_i)=M_2(z_i)$. Then $M_2^{-1}\circ M_1(z_i)=z_i$, and by the fixed point lemma $M_2^{-1}\circ M_1=I$, implying that the maps are the same