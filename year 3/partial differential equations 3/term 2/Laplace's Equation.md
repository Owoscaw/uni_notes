
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

We verify the last property directly by integrating. Assuming $u>0$ for $(x-r,x+r)$ then by linearity of $u$:$$\Huge\begin{align*}
\frac{1}{2r}\int_{x-r}^{x+r}u(y)dy&=\frac{1}{2r}\left(2r\frac{u(x-r)+u(x+r)}{2}\right)\\
&=\frac{u(x-r)+u(x+r)}{2}=u(x)
\end{align*}$$
In higher dimensions, linear polynomials $u(\underline{x})=\underline{c}\cdot\underline{x}+d$ are harmonic. Note that harmonic functions are not necessarily linear. For example, $u(x,y)=\sin x\sinh y$ is harmonic but not linear. Nevertheless, all harmonic functions satisfy the above properties.

# Mean-Value formulae:

We will prove the last two properties of harmonic functions in any dimension. Let $v:\Re^n\rightarrow n$ and recall$$\Huge\int^*_{B_r(\underline{x})}v(\underline{y})d\underline{y}=\frac{1}{|B_r(\underline{x})|}\int_{B_r(\underline{x})}v(\underline{y})d\underline{y}=\frac{\int_{B_r(\underline{x})}v(\underline{y})d \underline{y}}{\int_{B_r(\underline{x})}1d\underline{y}}$$denotes the average (mean-value) of $v$ over the ball $B_r(\underline{x})$. A similar result exists for the average value over the surface of the ball:$$\Huge \int^*_{\partial B_r(\underline{x})}v(\underline{y})d\underline{y}=\frac{\int_{\partial B_r(\underline{x})}v(\underline{y})d\underline{y}}{\int_{\partial B_r(\underline{x})}1dS(\underline{y})}$$
Let $\Omega\subset\Re^n$ be open. If $u\in C^2(\Omega)$ is harmonic in $\Omega$, then $$\Huge u(\underline{x})=\int^*_{\partial B_r(\underline{x})}u(\underline{y})dS(\underline{y})=\int^*_{B_r(\underline{x})}u(\underline{y})d\underline{y}$$for each ball $B_r(\underline{x})\subset\Omega$. Therefore $u(\underline{x})$ is the average of $u$ over any sphere any over any ball in $\Omega$ centered at $\underline{x}$. Proof:
> We prove the theorem for $n=2$:$$\Huge u(\underline{x})=\int^*_{\partial B_r(\underline{x})}u(\underline{y})dL(\underline{y})=\varphi(r)$$Note that the proof for general $n$ is essentially the same.
> Observe that the LHS is independent of $r$, and so $\varphi(r)=\text{constant}\implies\varphi'(r)=0$. Recalling that for a parametrised curve, parametrised by $\underline{r}:[a,b]\rightarrow\Gamma,s\rightarrow\underline{r}(s)$, then the integral of a function $f:\Gamma\rightarrow\Re$ along $\Gamma$ is defined as:$$\Huge \int_\Gamma f(\underline{y})dL(\underline{y})=\int_a^bf(\underline{r}(s))|\dot{\underline{r}}(s)|ds$$
> We parametrised $\partial B_r(\underline{x})$ using polar coordinates with:$$\Huge \underline{r}:[0,2\pi]\rightarrow\partial B_r(\underline{x}),\,\,\underline{r}(\theta)=\underline{x}+r(\cos\theta,\sin\theta)$$
> Using this, we compute:$$\Huge\begin{align*}
\varphi(r)&=\int^*_{\partial B_r(\underline{x})}u(\underline{y})dL(\underline{y})=\frac{1}{|\partial B_r(\underline{x})|}\int_{\partial B_r(\underline{x})}u(\underline{y})dL(\underline{y})\\
&=\frac{1}{2\pi r}\int_0^{2\pi}u(\underline{r}(\theta))|\dot{\underline{r}}(\theta)|d\theta\\
&=\frac{1}{2\pi r}\int_0^{2\pi}u(\underline{x}+r(\cos\theta,\sin\theta))r\,d\theta\\
&=\frac{1}{2\pi}\int_0^{2\pi}u(\underline{x}+r(\cos\theta,\sin \theta))d\theta
\end{align*}$$
> Then using the chain rule gives:$$\Huge\begin{align*}
\varphi'(r)&=\frac{d}{dr}\frac{1}{2\pi}\int_0^{2\pi}u(\underline{x}+r(\cos\theta,\sin \theta))d\theta\\
&=\frac{1}{2\pi}\int_0^{2\pi}\underline{\nabla}u(\underline{x}+r(\cos\theta,\sin\theta))\cdot(\cos\theta,\sin\theta)d\theta
\end{align*}$$The unit outward-pointing normal to $\partial B_r(\underline{x})$ at a point $\underline{y}$ is given by:$$\Huge \underline{n}(\underline{y})=\frac{\underline{y}-\underline{x}}{|\underline{y}-\underline{x}|}=\frac{\underline{y}-\underline{x}}{r}\implies \underline{n}(\underline{r}(\theta))=\frac{\underline{r}(\theta)-\underline{x}}{r}=(\cos\theta,\sin \theta)$$And so we write:$$\Huge\begin{align*}
\varphi'(r)&=\frac{1}{2\pi}\int_0^{2\pi}\underline{\nabla} u(\underline{r}(\theta))\cdot\underline{n}(\underline{r}(\theta))d\theta\\
&=\frac{1}{2\pi r}\int_0^{2\pi}\underline{\nabla} u(\underline{r}(\theta))\cdot\underline{n}(\underline{r}(\theta))|\dot{\underline{r}}(\theta)|d\theta\\
&=\frac{1}{2\pi r}\int_{\partial B_r(\underline{x})}\underline{\nabla} u(\underline{y})\cdot\underline{n}(\underline{y})dL(\underline{y})\\
&=\frac{1}{2\pi r}\int_{B_r(\underline{x})}\underline{\nabla}(\underline{\nabla} u(\underline{y}))d\underline{y}\\
&=\frac{1}{2\pi r}\int_{B_r(\underline{x})}\Delta u(\underline{y})d\underline{y}=0
\end{align*}$$
> Therefore $\varphi'(r)=0$ and so the mean-value formula follows immediately:$$\Huge \varphi(r)=\text{constant}=\lim_{\rho\to0}\varphi(\rho)=\lim_{\rho\to0}\int^*_{\partial B_\rho(\underline{x})}u(\underline{y})dL(\underline{y})=u(\underline{x})$$