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

We show the existence of the Mobius transformation under the three point theorem. Define $F(z)=(z_1,z_1;z_2,z_3)$. $F$ is a Mobius transformation with $T=\begin{pmatrix}k&-kz_2\\1&-z_3\end{pmatrix},k=\frac{z_1-z_3}{z_1-z_2}$. Note that $F(z_1)=1,F(z_2)=0,F(z_3)=\infty$. Similarly define $G=(w_1,w_1;w_2,w_3)$ and we get analogous results to $F$. We see that $F(z_i)=\{1,0,\infty\}=G(w_i)$ so we can then define the map $G^{-1}\circ F$ to be the Mobius transform that maps from $z_i$ to $w_i$:$$\Huge G^{-1}\circ F(z_i)=w_i$$We have shown the existence of such a Mobius map. We now show uniqueness. Assume $M_1$ and $M_2$ are Mobius such that $M_1(z_i)=M_2(z_i)$. Then $M_2^{-1}\circ M_1(z_i)=z_i$, and by the fixed point lemma $M_2^{-1}\circ M_1=I$, implying that the maps are the same. Therefore we have that every Mobius transformation can be uniquely defined with $3$ points.

## Cross ratio preservation:
The cross ration is preserved under the mobius transformation. That is to say if $f:\hat{\mathbb{C}}\mapsto\hat{\mathbb{C}}$ is a mobius transformation we have:$$\Huge (f(z_0),f(z_1);f(z_2),f(z_3))=(z_0,z_1;z_2,z_3)$$
Any mobius transformation is a composition of the following four maps:
> Shift: $z\rightarrow z+b$ for some $b\in\mathbb{C}$
> Stretch: $z\rightarrow\lambda z$ for some $\lambda\in\Re_{>0}$
> Rotation: $z\rightarrow e^{i\theta}$ for some $\theta\in(-\pi,\pi]$
> Inversion: $z\rightarrow \frac{1}{z}$

We note that for any $a\in\mathbb{C}^*$ and $b\in\mathbb{C}$:$$\Huge az+b=|a|e^{i\theta}z+b$$We can see that any transformation $az+b$ is attained by a composition of the above four maps. Also using inversion, we can see that $\frac{1}{az+b}$ is also attained by a composition of the above four maps. So any mobius transformation can be written in the form $az+b$ or $\alpha+\frac{\beta}{az+b}$. To prove the invariance of the cross ratio, it is enough to show that is it preserved under $az+b$ and $\frac{1}{z}$  since the composition of these define every mobius transformation:$$\Huge\begin{align} 
(M(z_0),M(z_1);M(z_2),M(z_3))&=(f_1\circ f_2(z_0)\dots f_1\circ f_2(z_3))\\
&=(f_2(z_0)\dots f_2(z_3))\\
&=(z_0,z_1;z_2,z_3)
\end{align}$$Where on each line we have used the fact that the cross ratio is invariant on each $f_1(z)=az+b$ and $f_2(z)=\frac{1}{z}$. The invariance follows from the definition of the cross ratio and $f_1(z)-f_1(w)=a(z-w)$ as well as $f_2(z)-f_2(w)=-\frac{z-w}{zw}$. 

To find the unique Mobius map $f:\hat{\mathbb{C}}\mapsto\hat{\mathbb{C}}$ such that $(z_1,z_2,z_3)$ maps to $(w_1,w_2,w_3)$ we notice that for any $z\in\mathbb{C}$:$$\Huge (f(z),w_1;w_2,w_3)=(z,z_1;z_2,z_3)$$Expanding and rearranging gives $f$ explicitly. For example, we look for the map that takes $(1,-1,i)$ to $(0,\infty,1)$:![[Mobius example]]
# Domains under the Mobius transformation:

Let $T\in GL_2(\mathbb{C})$ and $D\subseteq\mathbb{C}$ be an open set. Then $M_T\left(D\setminus\{-\frac{d}{c}\}\right)$ is open. Together with the fact that Mobius maps are bijections on $\hat{\mathbb{C}}$ we have that:$$\Huge M_T\left(\partial D\setminus\left\{-\frac{d}{c}\right\}\right)=\partial M_T(D)\setminus\{\infty\}$$When $c=0$ we consider $-\frac{d}{c}$ as $\infty$ which is outside of $\mathbb{C}$ and consequently $A\setminus\{\infty\}=A$ for any $A\subseteq\mathbb{C}$. That is, not only do Mobius maps take open sets to open sets but they also take the boundary to another boundary. The strategy to find $M_T(D)$ then becomes:
> Find $M_T(\partial D)$
> Find $M_T(z_0)$ for $z_0\in D\setminus\partial D$
> $M_T(D)$ is the domain with boundary $M_T(\partial D)$ that contains $M_T(z_0)$

Mobius transformations map circles and lines in $\hat{\mathbb{C}}$ to circles and lines in $\hat{\mathbb{C}}$, where we consider any line to pass through infinity. Sometimes we use the term circline to refer to circles and lines. We can then say that Mobius transformations take circlines to circlines. Moreover a circline will be taken to a line if and only if it contains the point mapped to $\infty$.

For example, we aim to find the images of $\mathbb{D}$, the unit disc,  $\mathbb{H}$, the upper half plan, and $\Omega=\left\{z\in \mathbb{C}:0<\text{Arg}(z)<\frac{\pi}{2}\right\}$ under the Cayley map defined as $f(z)=\frac{z-i}{z+i}$:![[cayley maps]]

## Balls under the mobius transformation:
The map $f(z)=\frac{1}{z}$ takes a circle that does not pass through the origin to a circle. Moreover, if $B$ is an open balls whose closure doesn't contain the origin, then $f(B)$ is once again an open balls. Consequently, if $D\subseteq\mathbb{C}$ is a set, then for any $z_0\in\mathbb{D}\setminus\{0\}$ for which there exists $\epsilon>0$ with $B_\epsilon(z_0)\subseteq D$ we have that there exists $\delta>0$ such that $B_\delta(f(z_0))\subseteq f(D)$. That is, $f$ takes any non-zero interior point of $D$ to an interior point of $f(D)$.

The second claim follows from the first, so it is sufficient to only prove the first. Consider $|z-a|^2=r^2\iff(z-a)(\overline{z-a})=r^2\iff z\bar z-a\bar z-\bar a z+a\bar a=r^2\iff \bar z-a\bar z-\bar az+(|a|^2-r^2)=0$, if $z\neq0$ then we define $w=\frac{1}{z}$ and dividing the above equation by $z\bar z>0$ we get:$$\Huge 1-a\frac{1}{z}-\bar a\frac{1}{\bar z}+(|a|^2-r^2)\frac{1}{|z|^2}=0$$Or, substituting $w$:$$\Huge (|a|^2-r^2)w\bar w-aw-\bar aw+1=0$$Since $z\neq0$ is not on $|z-a|=r$ we can divide by $|a|^2=r^2$ to get:$$\Huge w\bar w-\frac{a}{|a|^2-r^2}w-\overline{\frac{a}{|a|^2-r^2}}\bar w+\frac{1}{|a|^2-r^2}=0$$This is of the same form as before $w$ was introduced with $a'=\overline{\frac{a}{|a|^2-r^2}}$ and $|a'|^2-(r')^2=\frac{1}{|a|^2-r^2}$. So we get:$$\Huge \left|w-\frac{\bar a}{|a|^2-r^2}\right|=\frac{r}{||a|^2-r^2|}$$This is indeed a circle, so we have shown the first claim and therefore the second, proving the entire lemma. Similarly the open ball of radius $r$ centered at $a$ given by $|z-a|<r$ is equivalent to the open ball of radius $\frac{r}{||a|^2-r^2|}$ centered at $\frac{\bar a}{|a|^2-r^2}$.

When $D$ is open, we know that a Mobius transformation takes $D\setminus\left\{-\frac{d}{c}\right\}$ to an open set. It is trivial for shifts, rotations, and scaling. We have just shown that this also holds for inversion, so we can conclude that any Mobius transformation takes an open ball to an open ball.

We ask what happens when the circle does pass through $-\frac{d}{c}$, that is $0$ for $f(z)=\frac{1}{z}$. Again consider $|z-a|=r$ with $0\in\partial B_r(a)\implies r=|a|$. We showed that for any $z\neq0$ the above is equivalent to $(|a|^2-r^2)w\bar w-aw-\bar a\bar w+1=0$ with $w=\frac{1}{z}$. Since $|a|=r$ this becomes $-aw-\bar a\bar w+1=0$, equivalent to $aw+\bar a\bar w=2\Re(aw)$. Now letting $w=x+iy$ and $a=\alpha+i\beta$ we get $2\Re(aw)=\alpha x-\beta y\implies \alpha x-\beta y=\frac{1}{2}$, a line. 

This motivates the following lemma. Given $\gamma,\beta\in\Re$ and $\alpha\in\mathbb{C}$, the equation:$$\Huge \gamma z\bar z-\alpha\bar z-\bar\alpha z+\beta=0$$Describes a circle if $\gamma\neq0$ and $|\alpha|^2-\beta\gamma>0$ or a line if $\gamma=0$ and $\alpha\neq0$. Conversely, any line or circle can be written in this form.

# Circlines under Mobius transformations:

We propose that Mobius transformations map circles and lines in $\hat{\mathbb{C}}$ to circles and lines in $\hat{\mathbb{C}}$, where we consider any line fo pass through infinity. Again shifting, rotating, and scaling are trivial, so we investigate inversion. 