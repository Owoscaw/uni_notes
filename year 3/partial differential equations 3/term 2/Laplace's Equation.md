
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
&=\frac{1}{\alpha(n)r^n}\int_0^rn\alpha(n)\rho^{n-1}\int^*_{\partial B_\rho(\underline{x})}u(\underline{z})dS(\underline{z})\,d\rho\\
&=\frac{n}{r^n}\int_0^r\rho^{n-1}\int_{\partial B_\rho(\underline{x})}^*u(\underline{z})dS(\underline{z})d\rho
\end{align*}$$

# Maximum principles:

We now prove the first two properties of harmonic functions in all dimensions. First we must recall a few of our definitions of open/closedness:
> Let $\Omega\subseteq\Re^n$, we say that $U\subseteq\Omega$ is an open subset of $\Omega$ if $U=\Omega\cap\mathcal{O}$ for some open set $\mathcal{O}\subseteq\Re^n$. 
> A set $V\subseteq\Omega$ is a closed subset of $\Omega$ if $V=\Omega\cap\mathcal{C}$ for some closed set $\mathcal{C}\subseteq\Re^n$.
> A set $\Omega\subseteq\Re^n$ is disconnected if it can be written as the union of two disjoint nonempty subsets of $\Omega$, otherwise it is connected. This comes with an equivalence:
> > $\Omega$ is connected
> > The only subsets of $\Omega$ that are both open and closed subsets are $\Omega$ and $\emptyset$

We can now state our maximum principles. Let $\Omega\subset\Re^n$ be open, bounded, and connected. Let $u:\bar\Omega\rightarrow\Re,u\in C^2(\Omega)\cap C(\bar\Omega)$ be harmonic in $\Omega$, then:
> The weak maximum principle, $u$ attains its maximum on the boundary of $\Omega$:$$\Huge\max_{\bar\Omega}u=\max_{\partial\Omega}u$$
> The strong maximum principle, if $u$ attains its maximum in $\Omega$ then $u$ is constant. That is, if there exists $\underline{x}_0\in\Omega$ such that$$\Huge u(\underline{x}_0)=\max_{\bar\Omega}u$$, then $u$ is constant.

Note that the assumption $u\in C(\bar\Omega)$ ensures that the maximum of $u$ over $\bar\Omega$ exists:
> We first prove the strong maximum principle. Let $\underline{x}_0\in\Omega$ satisfy$$\Huge u(\underline{x}_0)=\max_{\bar\Omega}u=M$$and define $S\subseteq\Omega$ to be the set of points in $\Omega$ where $u$ attains its maximum:$$\Huge S=\{\underline{x}\in\Omega:u(\underline{x})=M\}=u^{-1}(\{M\})\cap\Omega$$
> Note that since $S$ is nonempty (as $\underline{x}_0\in S$ by definition). Let $\underline{x}\in S$ and $B_r(\underline{x})\subset\Omega$, then by the second mean-value formula:$$\Huge M=u(\underline{x})=\int_{B_r(\underline{x})}^*u(\underline{y})d\underline{y}\leq\int_{B_r(\underline{x})}Md\underline{y}=M$$
> Therefore we have an equality$$\Huge \int_{B_r(\underline{x})}^*u(\underline{y})d\underline{y}=\int_{B_r(\underline{x})}^*Md\underline{y}$$, meaning that $u(\underline{y})=M$ for all $\underline{y}\in B_r(\underline{x})$. Consequently, $B_r(\underline{x})\subset S$ and so $S$ is an open set.
> Therefore $S=\Omega\cap S$ is an open subset of $\Omega$. The set $u^{-1}(\{M\})$ is the preimage of the closed set $\{M\}$ under the continuous map $u$ and so is closed. Therefore $S=u^{-1}(\{M\})\cap\Omega$ is a closed subset of $\Omega$. We have shown that $S$ is nonempty, open, and a closed subset of the connected set $\Omega$. Therefore $S=\Omega$, implying $u=M=\text{constant}$ in $\Omega$, as required.
> The weak maximum principle is a direct consequence of the strong maximum principle.

Note that one can apply the maximum principles to $-u$ to attain corresponding minimum principles for $u$. 

We previously proved the [[Poisson's equation#Energy Method|uniqueness for Poisson's equation]] using the energy method, however we also provide a proof using the weak maximum principle:
> Let $\Omega\subset\Re^n$ be open, bounded, and connected. There exists at most one solution $u\in C^2(\Omega)\cap C(\bar\Omega)$ of the Dirichlet problem$$\Huge -\Delta u=f\text{ in }\Omega,\,\,u=g\text{ on }\Omega$$, where $f\in C(\Omega),g\in C(\partial\Omega)$.
> Suppose that $u_1$ and $u_2$ are solutions and let $w=u_1-u_2$, then $w$ satisfies:$$\Huge \Delta w=0\text{ in }\Omega,\,\,w=0\text{ on }\partial\Omega$$
> Since $w$ is harmonic, the weak maximum principle implies that$$\Huge \max_{\bar\Omega}w=\max_{\partial\Omega}w=0$$, therefore $w\leq0$. We can apply the same argument to $\bar\omega=-w=u_2-u_1$. As above, $\bar w$ is harmonic and $\bar w=0$ on $\partial\Omega$. Therefore by the weak maximum principle $\bar w\leq0$, however $\bar w=-w$ which implies $w\geq0$. Therefore $w=0$, as required.

Note that maximum principles can be used to prove uniqueness theorems, bounds on solutions, and comparison principles:
> Suppose that $\Delta u_1=\Delta u_2=0$ in $\Omega$, $u_1=g_1,u_2=g_2$ on $\partial\Omega$. If $g_1\leq g_2$ on $\partial\Omega$ then we have that $u_1\leq u_2$ in $\Omega$. 
> The proof of this is trivial.

Similar to complex analytic functions, the existence of a particular second derivative $\Delta u$ implies all subsequent derivatives exist. That is, harmonic functions are infinitely smooth:
> Let $\Omega\in\Re^n$ be open, $\Delta u=0$ in $\Omega$, $u\in C^2(\Omega)$, then we have both:
> $u\in C^\infty(\Omega)$
> $u$ is analytic in $\Omega$. That is, $\forall x_0\in\Omega\exists r(x_0):\forall x\in B_r(x_0)$:$$\Huge u(x)=u(x_0)+Du|_{x_0}(x-x_0)+\dots$$Where the sum here converges.

We can draw another analogue to $\mathbb{C}$ analytic functions by stating the Boundedness/Liouville theorem for harmonic functions:
> If $u:\Re^n\rightarrow\Re$ is harmonic and bounded, then $u(x)=\text{constant}$.
> To prove this, fix some $x,y\in\Re^n$ and put $\delta=|x-y|$. Consider $B_r(x),B_{r+\delta}(y)$ and, noting that $B_r(x)\subset B_{r+\delta}(y)$, compute:$$\begin{align*}
u(x)-u(y)&=\frac{1}{|B_r|}\int_{B_r(x)}u(s)ds-\frac{1}{|B_{r+\delta}|}\int_{B_{r+\delta}(y)}u(s)ds\\
&=\frac{1}{|B_r|}\int_{B_r(x)}u(s)ds-\frac{1}{|B_{r+\delta}|}\int_{B_r(x)}u(s)ds-\frac{1}{|B_{r+\delta}|}\int_{B_{r+\delta}(y)\setminus B_r(x)}u(s)ds\\
&=\left(\frac{1}{|B_r|}-\frac{1}{|B_{r+\delta}|}\right)\int_{B_r(x)}u(s)ds-\frac{1}{|B_{r+\delta}|}\int_{B_{r+\delta}(y)\setminus B_r(x)}u(s)ds
\end{align*}$$
> Now suppose $|u(x)|\leq M$ for all $x\in\Re^n$, then for any $V\subset\Re^n$ it makes sense that $|\int_V u(s)ds|\leq |V|M$. So we write:$$\Huge\begin{align*}
 u(x)-u(y)&\leq\left(\frac{1}{|B_r|}-\frac{1}{|B_{r+\delta}|}\right)|B_r|+\frac{|B_{r+\delta}(y)\setminus B_r(x)|}{|B_{r+\delta}|}M\\
&=2\left(1-\frac{|B_r|}{|B_{r+\delta}|}\right)M
\end{align*}$$
> Taking $r\to\infty$ with $x,y$ fixed makes $|B_r|/|B_{r+\delta}|\to1$ and $|u(x)-u(y)|\to0$. Since $x,y$ were arbitrary, we must have that $u(x)=u(y)$ for all $x,y\in\Re^n$. That is, $u(x)=\text{constant}$. 

# Maximum principles for Elliptic PDEs:

These maximum and minimum principles hold for a broad class of elliptic PDEs. First we look at the example of Poisson's equation $-\Delta u=f$ for the case where $f$ is signed.

First we define Subharmonic and Superharmonic functions. Let $\Omega\subseteq\Re^n$ be open. We say that $u\in C^2(\Omega)$ is subharmonic in $\Omega$ if $-\Delta u(\underline{x})\leq0$ for all $\underline{x}\in\Omega$. Conversely, we define the superharmonic as $u\in C^2(\Omega)$ with $-\Delta u(\underline{x})\geq0$ for all $\underline{x}\in\Omega$.

## Sub/superharmonic functions in $1D$:
In one dimension, $u$ is subharmonic if $-u''\leq0$. For example suppose that $-u''(x)=f$ and $f<0$ is constant. Then $u$ is a quadratic polynomial of the form $u(x)=ax^2+bx+c$ with $a=-f/2>0$. Therefore $u$ attains its maximum over any interval at the boundary of the interval. Its minimum is not necessarily attains at the boundary however. 

Similarly if $u$ is a superharmonic function satisfying $-u''(x)=f$ where $f>0$ is constant, then $u$ attains its minimum over any interval at the boundary of the interval, and its maximum is not necessarily attained at the boundary. This generalises to higher dimensions and to nonconstant $f$.

Writing this formally, let $\Omega\subset\Re^n$ be open, bounded, and connected and let $u\in C^2(\Omega)\cap C(\bar\Omega)$:
> If $u$ is subharmonic, then it satisfies the weak maximum principle$$\Huge\max_{\bar\Omega}u=\max_{\partial\Omega}u$$
> If $u$ is superharmonic, then it satisfies the weak minimum principle$$\Huge\min_{\bar\Omega}u=\min_{\partial\Omega}u$$

Moreover, subharmonics satisfy the strong maximum principle and superharmonics satisfy the strong minimum principle. This is proven in much the same way for harmonic functions, except with the presence of a mean-value inequality in the proof. These principles generalise further to second-order elliptic PDEs of the form $Lu=f$ for the case where $f$ has a sign:
> Let $\Omega\subset\Re^n$ be open, bounded, and connected. Let $f\in C(\Omega)$ and $u\in C^2(\Omega)\cap C(\bar\Omega)$ satisfy $Lu=f$, where $L$ is a linear second-order elliptic operator of the form$$\Huge Lu=-\sum_{i,j=1}^na_{ij}u_{x_ix_j}+\sum_{j=1}^nb_ju_{x_j}+c(x)u=-A:D^2u+\underline{b}\cdot\underline{\nabla}u$$, where $a_{ij}$ and $b_j$ are continuous functions on $\Omega$ and $A$ is symmetric and uniformly positive definite. That is, $a_{ij}(\underline{x})=a_{ji}(\underline{x})$ for all $\underline{x}\in\Omega$ and there exists a constant $\alpha>0$ such that $\underline{y}^\top A(\underline{x})\underline{y}\geq\alpha|\underline{y}|^2$ for all $\underline{y}\in\Re^n,\underline{x}\in\Omega$. In this case we have no mean-value formulae, but can still state our maximum principles:
> > Let $\Omega\subset\Re^n$ be open, bounded, and connected. For $f\in C(\Omega)$ let $u\in C^2(\Omega)\cap C(\bar\Omega)$ solve $Lu=f$. Then if $f\geq0$, $u$ satisfies the weak maximum principle$$\Huge\max_{\bar\Omega}u=\max_{\partial\Omega}u$$
> > $u$ also satisfies the strong maximum principle, $\exists x_0\in\Omega$ such that $u(x_0)=\max_{\bar\Omega}u$ then $u$ is constant in $\Omega$.
> > 


