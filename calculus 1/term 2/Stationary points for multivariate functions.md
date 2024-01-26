
For a function of one variable, a stationary point is defined to be a point where $f'(x)=0$. There are two types of extema for functions of one variable, minima and maxima. For functions of two or more variables, there are three types of extrema: minima, maxima, and saddle points. For a function of two variables, there will be a stationary point whenever the tangent plane is zero. Generalising to $n$ variables, there will be a stationary point when the $n-1$ hyperplane is zero.

Let $f(x_1,\dots,x_n):\Re^n\mapsto\Re$. $f$ has a stationary point at $\underline a$ if $f$ is differentiable at $\underline a$ and:$$\Huge \underline\nabla f=\left(\frac{\partial f}{\partial x_1},\dots,\frac{\partial f}{\partial x_n}\right)=0$$For example:![[stationary points example]]
# Distinguishing extrema:

For a function of one variable, with a stationary point at $x=x_0$, the nature of the stationary point is determined by the behaviour of the function around $x_0$: $f(x_0+\delta x)=f(x_0)+\delta xf'(x_0)+\frac{(\delta x)^2}{2}f''(x_0)+\dots$, the first derivative vanishes since $f'(x_0)=0$, so we observe $\delta f=f(x_0+\delta x)-f(x_0)=\frac{(\delta x)^2}{2}f''(x_0)+\dots$. Higher orders than $(\delta x)^2$ will tend to zero faster then the first term as $\delta x\to 0$, so the second order term dominates:
> If $f''(x_0)>0\implies\delta f>0\implies x_0$ is a minimum
> If $f''(x_0)<0\implies\delta f<0\implies x_0$ is a maximum
> If $f''(x_0)=0\implies x_0$ is a degenerate stationary point

