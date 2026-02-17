
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

We will prove the last two properties of harmonic functions in any dimension. Let $v:\Re^n\rightarrow n$ and recall:$$\Huge\texthtbardotlessj$$