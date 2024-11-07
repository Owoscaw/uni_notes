There are several generalisations of the [[year 1/analysis 1/term 2/Integration#Fundamental theorem of Calculus|fundamental theorem of calculus]] that apply to vector calculus. One of which is the fundamental theorem of [[Line integrals|line integrals]]:

# Fundamental theorem of line integrals:

If $f:\Re^n\mapsto\Re$ is a $C^1$ scalar field and $C$ is an oriented curve with parametrisation $\underline x(t)$ for $t\in[t_0,t_1]$:$$\Huge \int_C\underline{\nabla}f\cdot\hat{\underline t}dl=f(\underline x(t_1))-f(\underline x(t_2))$$We prove this for $n=3$:$$\Huge\begin{align} \int_C\underline{\nabla}f\cdot\hat{\underline t}dl&=\int_{t_0}^{t_1}\underline{\nabla}f\cdot\frac{d \underline x}{dt}dt\\
&=\int_{t_0}^{t_1}\left(\frac{\partial f}{\partial x}\frac{d x}{dt}+\frac{\partial f}{\partial y}\frac{d y}{dt}+\frac{\partial f}{\partial z}\frac{d z}{dt}\right)dt\\
&=\int_{t_0}^{t_1}\frac{d f}{dt}dt\\
&=f(t_1)-f(t_0)=f(\underline x(t_1))-f(\underline x(t_0))
\end{align}$$Where we have used the chain rule to make the integrand a total derivative.

A vector field $f:\Re^n\mapsto\Re^n$ is called conservative if it can be written as $\underline f=\underline{\nabla}g$ for some $C^1$ scalar field $g:\Re^n\mapsto\Re$. Such a scalar field is called a scalar potential of $\underline f$. Take for example:![[scalar potential example]]Note that $\underline f=\underline{\nabla}g$ only defines $g$ up to a constant, hence the presence of the constant in the scalar potential $g(x,y)$.

## Path independence:
A vector field is conservative if and only if it has path independent line integrals between any pair of points:![[path independence proof]]Here we have used the [[year 1/analysis 1/term 2/Integration#MVT for integrals|MVT]] for integrals. The proof is analogous for other components of $g$.