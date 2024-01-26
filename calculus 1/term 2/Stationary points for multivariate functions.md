
For a function of one variable, a stationary point is defined to be a point where $f'(x)=0$. There are two types of extema for functions of one variable, minima and maxima. For functions of two or more variables, there are three types of extrema: minima, maxima, and saddle points. For a function of two variables, there will be a stationary point whenever the tangent plane is zero. Generalising to $n$ variables, there will be a stationary point when the $n-1$ hyperplane is zero.

Let $f(x_1,\dots,x_n):\Re^n\mapsto\Re$. $f$ has a stationary point at $\underline a$ if $f$ is differentiable at $\underline a$ and:$$\Huge \underline\nabla f=\left(\frac{\partial f}{\partial x_1},\dots,\frac{\partial f}{\partial x_n}\right)=0$$For example:![[stationary points example]]
# Distinguishing extrema:

For a function of one variable, with a stationary point at $x=x_0$, the nature of the stationary point is determined by the behaviour of the function around $x_0$: $f(x_0+\delta x)=f(x_0)+\delta xf'(x_0)+\frac{(\delta x)^2}{2}f''(x_0)+\dots$, the first derivative vanishes since $f'(x_0)=0$, so we observe $\delta f=f(x_0+\delta x)-f(x_0)=\frac{(\delta x)^2}{2}f''(x_0)+\dots$. Higher orders than $(\delta x)^2$ will tend to zero faster then the first term as $\delta x\to 0$, so the second order term dominates:
> If $f''(x_0)>0\implies\delta f>0\implies x_0$ is a minimum
> If $f''(x_0)<0\implies\delta f<0\implies x_0$ is a maximum
> If $f''(x_0)=0\implies x_0$ is a degenerate stationary point

## Methods of finding stationary points:
Let $f(x,y)$ have a stationary point at $(x_0,y_0)$:
>If $\delta f=f(x_0+\delta x,y_0+\delta y)-f(x_0,y_0)>0$ for $(\delta x,\delta y)\neq(0,0)$, then $(x_0,y_0)$ is a minimum
>If $\delta f=f(x_0+\delta x,y_0+\delta y)-f(x_0,y_0)<0$ for $(\delta x,\delta y)\neq(0,0)$, then $(x_0,y_0)$ is a maximum
>if $\delta f$ takes either sign for the above constraint, then it is a saddle point

This is shown by observing the taylor series about $(x_0,y_0)$:$$\small f(x_0+\delta x,y_0+\delta y)=f(x_0,y_0)+f_x(x_0,y_0)\delta x+f_y(x_0,y_0)\delta y+\frac{1}{2}((\delta x)^2f_{xx}+2\delta x\delta yf_{xy}(x_0,y_0)+(\delta y)^2)f_{yy}(x_0,y_0))+\dots$$The $f_x$ and $f_y$ terms will vanish, which gives:$$ \delta f=f(x_0+\delta x,y_0+\delta y)-f(x_0,y_0)=\frac{1}{2}((\delta x)^2f_{xx}(x_0,y_0)+2\delta x\delta yf_{xy}(x_0,y_0)+(\delta y)^2f_{yy}(x_0,y_0))+\dots$$This term will dominate as $\delta x,\delta y\to 0$, so we let:$$\Huge Q(x,y)=f_{xx}x^2+2f_{xy}xy+f_{yy}y^2$$This is called the quadratic form and can be written as:$$\Huge Q(x,y)=\begin{pmatrix}x&y\end{pmatrix}\begin{pmatrix}f_{xx}&f_{xy}\\f_{xy}&f_{yy}\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}$$The matrix seen here is called the Hessian matrix. This can be generalised for $n$ variables, where the Hessian matrix is defined by:$$\Huge H_{ij}=\frac{\partial^2f}{\partial x_i\partial x_j}$$Note that order of differentiation does not matter, so we get $H_{ij}=H_{ji}$, making it a real symmetric [[Matrix definition|matrix]]. So finally $\delta f=\frac{1}{2}Q(\delta x,\delta y)$:
>If $Q(\delta x,\delta y)>0\,\,\forall(\delta x,\delta y)\neq (0,0)$, then $(x_0,y_0)$ is a minimum
>If $Q(\delta x,\delta y)<0\,\,\forall(\delta x,\delta y)\neq (0,0)$, then $(x_0,y_0)$ is a maximum
>If $Q(\delta x,\delta y)$ takes both signs, then $(x_0,y_0)$ is a saddle point.

You can divide through $Q(x,y)$ by $x^2$ and solve for $\frac{y}{x}$ to get:$$\Huge \frac{y}{x}=\frac{-2f_{xy}\pm\sqrt{4f_{xy}^2-4f_{xx}f_{yy}}}{2f_{xx}}$$This has two real solutions (and therefore a saddle point) if the expression inside the square root is positive, that is $f_{xy}^2>f_{xx}f_{yy}$, writing this in terms of the Hessian:$$\Huge \det(H)=\begin{vmatrix}f_{xx}&f_{xy}\\ f_{xy}&f_{yy}\end{vmatrix}=f_{xx}f_{yy}-f_{xy}^2<0$$Therefore a stationary point is a saddle point if $\det(H)<0$. If this is not the case and the determinant is positive, then there are no line of points where $Q(x,y)=0$ as $Q\approx 2\delta f$ is always greater than zero ($f$ has a minimum) or always less than zero ($f$ has a maximum). To distinguish these cases, observe:$$\Huge Q(\delta x,0)=f_{xx}(\delta x)^2$$Therefore if $f_{xx}>0$ then $Q$ is always greater than zero since it will not change sign (no real roots), making $f$ a minimum. Similarly if $f_{xx}<0$ then $Q$ is always less than zero, making $f$ a maximum. Tabulating these results:
> If $\det(H)<0$ then the stationary point is a saddle point
> If $\det(H)>0$ and $f_{xx}>0$ then the stationary point is a minimum
> If $\det(H)>0$ and $f_{xx}>0$ then the stationary point is a maximum
> If $\det(H)=0$, that is the rank of $H$ is less than $2$, then the stationary point is degenerate