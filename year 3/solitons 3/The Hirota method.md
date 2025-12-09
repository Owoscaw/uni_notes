
The Hirota method is an alternative to the [[Backlund transformations#Definition|Backlund transformation]] as a way to generate multi-soliton solutions. It was originally developed to write $N$-soliton solutions for the [[Basic properties of Solitons#The KdV equation|KdV]] equation and was then generalised. We focus on the KdV equation.

# Motivations:

Substituting $u=w_x$ into the KdV equation gives:$$\Huge w_{xt}+6w_xw_{xx}+w_{xxxx}=0$$which we integrate wrt $x$:$$\Huge \implies w_t+3w_x^2+w_{xxx}=g(t)$$we drop this $x$-constant function $g(t)$ as it can be absorbed into a redefinition of $w$ that does not change $u=w_x$:$$\Huge w(x,t)=w'(x,t)+\int_{t_0}^tg(t')dt'$$Using the new $w$, we have:$$\Huge w_t+3w_x^2+w_{xxx}=0$$For small $w$, the $w_x^2$ term is negligible and the equation becomes linear. More formally, we look for a series solution $w=\epsilon w_1+\epsilon^2w_2+\dots$. Substituting in we have:$$\Huge \begin{align*}
\epsilon^1&:w_{1t}+w_{1xxx}=0\\
\epsilon^2&:w_{2t}+3w_{1x}^2+w_{2xxx}=0\\
\vdots
\end{align*}$$In principle we can solve these equations, as we did for the [[year 3/solitons 3/Conservation laws#The Gardner transform|Gardner transform]]. However:
> An infinite amount of equations must be solved for an exact formula for $w$
> The method could be saved if it happened that $w_m=0$ for all $m>n$ for some $n$. Then the approximate solution up to order $n$ would be exact.
> This does not happen.

A close relative of the KdV equation is Burger's equation:$$\Huge u_t+uu_x-\lambda u_{xx}=0$$for a parameter $\lambda$. We can turn this into the linear heat equation by substituting $u=-2\lambda v_x/v$:$$\Huge v_t=\lambda v_{xx}$$Recalling the one-soliton solution and writing $u=w_x$, we have:$$\Huge w=2\mu\tanh(\mu(x-x_0-4\mu^2t))$$Integrating the RHS wrt $x$, using $\tanh y= \frac{d}{dy}\log\cosh y$ to find:$$\Huge u=2 \frac{\partial^2}{\partial x^2}\log\cosh(\mu(x-x_0-4\mu^2t))$$Now letting $X=x-x_0-4\mu^2t$:$$\Huge\begin{align*}
u&=2\frac{\partial^2}{\partial x^2}\log\frac{e^{-\mu X}(1+e^{2\mu X})}{2}\\
&=2\frac{\partial^2}{\partial x^2}(-\mu X-\log 2+\log(1+e^{2\mu X}))\\
&=2\frac{\partial^2}{\partial X^2}\log(1+e^{2\mu(x-x_0-4\mu^2t)})
\end{align*}$$This is the form of the one-soliton solution of KdV that we will now refer to.

# KdV equation in bilinear form:

Inspired by this new form, we substitute:$$\Huge w=2\frac{\partial }{\partial x}\log f=\frac{f_x}{f}\iff u=2\frac{\partial^2}{\partial x^2}\log f$$into the $w=u_x$ KdV equation:$$\Huge \begin{align*}
\frac{1}{2}w_t&=\frac{f_{xt}f-f_xf_t}{f^2}\\
\frac{1}{2}w_x&=\frac{f_{xx}f-f_x^2}{f^2}\\
\frac{1}{2}w_{xxx}&=\frac{f_{xxxx}}{f}-4\frac{f_{xxx}f_x}{f^2}-3\frac{f_{xx}^2}{f^2}+12\frac{f_{xx}f_x^2}{f^3}-6\frac{f_x^4}{f^4}\\
\implies0&=\frac{f_{xt}}{f}-\frac{f_xf_t}{f^2}+3\frac{f_{xx}^2}{f^2}-4\frac{f_{xx}^2}{f^2}-4\frac{f_{xxx}f_x}{f^2}+\frac{f_{xxxx}}{f}
\end{align*}$$Multiplying through by $f^2$, we get the quadratic form of the KdV equation:$$\Huge ff_{xt}-f_xf_t+3f_{xx}^2-4f_xf_{xxx}+ff_{xxxx}=0$$