
Laplace's equation is simply the [[Poisson's equation|Poisson's]] equation with $f=0$:$$\Huge\Delta u=0$$Solutions to this are known as harmonic functions, which turn out to be very well behaved.

# Harmonic functions in $1D$:

Laplace's equation in a single dimension is$$\Huge u''=0$$, which clearly has solution $u:\Re\rightarrow\Re$ of the form$$\Huge u(x)=cx+d$$for $c,d\in\Re$. It is easy to see that these have the properties:
> On any interval $[a,b]$, $u$ attains its maximum and minimum at the boundary.
> If $u$ also attains its maximum or minimum at a point in $(a,b)$, then $u=\text{constant}$.
> If $u$ is bounded on $\Re$, then $u=\text{constant}$.
> $u\in C^\infty$
> $u$ is analytic.

We also have the less obvious properties:
> For all $r>0,u(x)=\frac{1}{2}(u(x+r)+u(x-r))$. That is, the average of $u$ over the boundary of the ball $B_r(x)=(x-r,x+r)$ is the value of $u$ at the center of that ball.
> For all $r>0,u(x)=\frac{1}{2r}\int_{x-r}^{x+r}u(y)dy$. This is the above statement recast for general dimensions.

The first two properties are known as the maximum principles, and the last two are known as the mean-value principles. We verify the last property directly by integrating. Assuming $u>0$ for $(x-r,x+r)$ then by linearity of $u$:$$\Huge\begin{align*}
\frac{1}{2r}\int_{x-r}^{x+r}u(y)dy&=\frac{1}{2r}\left(2r\frac{u(x-r)+u(x+r)}{2}\right)\\
&=\frac{u(x-r)+u(x+r)}{2}=u(x)
\end{align*}$$
In higher dimensions, linear polynomials $u(\underline{x})=\underline{c}\cdot\underline{x}+d$ are harmonic. Note that harmonic functions are not necessarily linear. For example, $u(x,y)=\sin x\sinh y$ is harmonic but not linear. Nevertheless, all harmonic functions satisfy the above properties.

# Harmonic functions in $2D$:

We identify $(x,y)\in\Re^3$ with $z\in\mathbb{C}$ with $z=x+iy$. We write $f:\mathbb{C}\rightarrow\mathbb{C}$ for$$\Huge f(x+iy)=u(x,y)+iv(x,y)$$with $u,v:\Re^2\rightarrow\Re^2$. If $f$ is complex analytic, then both $u,v$ are [[Complex differentiation#Cauchy-Riemann equations|harmonic]]. 

# Mean-Value formulae in $\Re^n$:

We will prove the last two properties of harmonic functions in any dimension. Let $v:\Re^n\rightarrow n$ and recall$$\Huge\int^*_{B_r(\underline{x})}v(\underline{y})d\underline{y}=\frac{1}{|B_r(\underline{x})|}\int_{B_r(\underline{x})}v(\underline{y})d\underline{y}=\frac{\int_{B_r(\underline{x})}v(\underline{y})d \underline{y}}{\int_{B_r(\underline{x})}1d\underline{y}}$$denotes the average (mean-value) of $v$ over the ball $B_r(\underline{x})$. A similar result exists for the average value over the surface of the ball:$$\Huge \int^*_{\partial B_r(\underline{x})}v(\underline{y})dS(\underline{y})=\frac{\int_{\partial B_r(\underline{x})}v(\underline{y})dS(\underline{y})}{\int_{\partial B_r(\underline{x})}1dS(\underline{y})}$$
Let $\Omega\subset\Re^n$ be open. If $u\in C^2(\Omega)$ is harmonic in $\Omega$, then $$\Huge u(\underline{x})=\int^*_{\partial B_r(\underline{x})}u(\underline{y})dS(\underline{y})=\int^*_{B_r(\underline{x})}u(\underline{y})d\underline{y}$$for each ball $B_r(\underline{x})\subset\Omega$. Therefore $u(\underline{x})$ is the average of $u$ over any sphere any over any ball in $\Omega$ centered at $\underline{x}$. Proof:
> Fix some $\underline{x},r$ so that $B_r(\underline{x})\subset\Omega$ and let $\varphi(r)$ be given by:$$\Huge\varphi(r)=\int^*_{\partial B_r(\underline{x})}u(\underline{y})dS(\underline{y})$$Note that the $r$ dependence is implicit in $dS(y)$. To make it explicit we make a change of variables to $\underline{y}=\underline{x}+r\hat{\underline{y}}$ where $r\in\Re$ and $|\hat{\underline{y}}|=1$. This makes the integral:$$\Huge \varphi(r)=\int^*_{\partial B_1(0)}u(\underline{x}+r\hat{\underline{y}})dS(\hat{\underline{y}})$$
> Then $\varphi'(r)$ becomes, using our change of variables:$$\Huge\begin{align*}
\varphi'(r)&=\frac{d}{dr}\int^*_{\partial B_1(0)}u(\underline{x}+r\hat{\underline{y}})dS(\hat{\underline{y}})\\
&=\int^*_{\partial B_1(0)}\frac{d}{dr}u(\underline{x}+r\hat{\underline{y}})dS(\hat{\underline{y}})\\
&=\int^*_{\partial B_1(0)}\underline{\nabla}u(\underline{x}+r\hat{\underline{y}})\cdot\hat{\underline{y}}\,dS(\hat{\underline{y}})\\
&=\int^*_{\partial B_1(0)}\underline{\nabla}u(\underline{x}+r\hat{\underline{y}})\cdot d\underline{S}(\hat{\underline{y}})\\
&=\int^*_{\partial B_r(\underline{x})}\underline{\nabla}u(\underline{y})\cdot d\underline{S}(\underline{y})\\
&=\frac{1}{|\partial B_r|}\int_{\partial B_r(\underline{x})}\underline{\nabla}u(\underline{y})\cdot d\underline{S}(\underline{y})\\
&=\frac{1}{|\partial B_r|}\int_{B_r(\underline{x})}\underline{\nabla}\cdot\underline{\nabla}u(\underline{y})\,d\underline{y}=0
\end{align*}$$
> Therefore $\varphi$ is constant and so $\varphi(r)=\lim_{r\to0}\varphi(r)=u(\underline{x})$, as required. 
> For the other formula, we compute$$\Huge\begin{align*}
\int^*_{B_r(\underline{x})}u(\underline{y})d\underline{y}&=\frac{1}{|B_r|}\int_{B_r(\underline{x})}u(\underline{y})d\underline{y}\\
&=\frac{1}{|B_r|}\int_0^r\int_{\partial B_\rho(\underline{x})}u(\underline{z})dS(\underline{z})\,d\rho\\
&=\frac{1}{|B_r|}\int_0^r|\partial B_\rho|\int^*_{\partial B_\rho(\underline{x})}u(\underline{z})dS(\underline{z})\,d\rho\\
&=\frac{1}{\alpha(n)r^n}\int_0^rn\alpha(n)\rho^{n-1}\int^*_{\partial B_\rho(\underline{x})}u(\underline{z})dS(\underline{z})\,d\rho
\end{align*}$$
