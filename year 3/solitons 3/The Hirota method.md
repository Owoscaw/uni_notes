
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
## Hirota's bilinear operator:

Hirota defined a bilinear differential operator $D$ which maps a pair of functions $(f,g)$ into a single function $D(f\cdot g)$. If we work on $C^\infty$ functions, then:$$\Huge\begin{align*}
D:C^\infty\times C^\infty&\rightarrow C^\infty\\
(f,g)&\rightarrow D(f\cdot g)
\end{align*}$$For integers $m,n\geq0$, we define Hirota's bilinear differential operator $D_t^mD_x^n$ by:$$\large [D_t^mD_x^n(f\cdot g)](x,t)=\left(\frac{\partial }{\partial t}-\frac{\partial }{\partial t'}\right)^m\left(\frac{\partial }{\partial x}-\frac{\partial }{\partial x'}\right)^nf(x,t)g(x',t')|_{(x',t')=(x,t)}$$
Let us look at some examples:
> $m=1,n=0$:$$\Huge\begin{align*}
[D_t(f\cdot g)](x,t)&=\left(\frac{\partial }{\partial t}-\frac{\partial }{\partial t'}\right)f(x,t)g(x',t')\\
&=f_t(x,t)g(x',t')-f(x,t)g_{t'}(x',t')\\
&=f_t(x,t)g(x,t)-f(x,t)g_t(x,t)
\end{align*}$$that is, $D_t(f\cdot g)=f_tg-fg_t$ and $D_t(f,f)=0$. There is a similar result for $D_x$.
> Now we look at $n=m=1$:$$\Huge \begin{align*}
[D_tD_x(f\cdot g)](x,t)&=\left(\frac{\partial }{\partial t}-\frac{\partial }{\partial t'}\right)\left(\frac{\partial }{\partial x}-\frac{\partial }{\partial x'}\right)f(x,t)g(x',t')\\
&=\left(\frac{\partial }{\partial t}-\frac{\partial }{\partial t'}\right)(f_x(x,t)g(x',t')-f(x,t)g_{x'}(x',t'))\\
&=f_{xt}g-f_tg_x-f_xg_t+fg_{xt}
\end{align*}$$that is, $D_tD_x(f\cdot f)=2(ff_{tx}-f_tf_x)$.

This is promising, as the RHS of the last expression reproduces the first two terms in the quadratic form of the KdV equation up to a factor. We proceed to compute:$$\Huge D_x^2(f\cdot g)=f_{xx}g-2f_xg_x+fg_{xx}\implies D^2_x(f\cdot f)=2(ff_{xx}-f_x^2)$$Which allows us to find:$$\Huge D_x^4(f\cdot g)=f_{xxxx}g-4f_{xxx}g_x+6f_{xx}g_{xx}-4f_xg_{xxx}+fg_{xxxx}$$Note that this is similar to $\partial_x^4$, with alternating signs. We therefore have:$$\Huge D_x^4(f\cdot f)=2(ff_{xxxx}-4f_xf_{xxx}+3f_{xx}^2)$$and we see that the KdV equation can be written as:$$\Huge (D_tD_x+D_x^4)(f\cdot f)=0$$where the bilinear operator $D_tD_x+D_x^4$ is defined by linearity on the space of operators of Hirota's type. The above equation is known as the bilinear form of the KdV equation.

Observe that we can formally factor the Hirota operator as:$$\Huge\begin{align*}
D_tD_x+D_x^4&=(D_t+D_x^3)D_x\\
\implies (D_tD_x+D_x^4)(f,g)&=(\partial_t-\partial_{t'}+(\partial_x-\partial_{x'})^3)f(x,t)g(x',t')
\end{align*}$$
# Solutions:

We need two ideas to find multi-soliton solutions, a solution and a way to add a soliton. If we take $f=1$, then the KdV field is the vacuum $u=0$. If we instead take:$$\Huge f=1+e^{2\mu(x-x_0-4\mu^2t)}$$then $u$ is the one-soliton travelling wave solution of the KdV equation. Since Hirota's operator is bilinear, this suggests that multi-soliton solutions may be obtained from and $f$ which is a sum of exponentials of linear functions of $x,t$, with $1=e^0$ as the trivial case. Before continuing, we must check the Hirota formalism by rederiving this one-soliton solution.
## The 1-soliton:
We try:$$\Huge f=1+e^\theta,\,\,\theta=ax+bt+c$$for constants $a,b,c$. If $\theta_i=a_ix+b_it+c_i$ then we have:$$\Huge D_t^mD_x^n(e^{\theta_1}\cdot e^{\theta_2})=(b_1-b_2)^m(a_1-a_2)^ne^{\theta_1+\theta_2}$$In particular:$$\Huge\begin{align*}
D_t^mD_x^n(e^\theta\cdot e^\theta)&=0\\
D_t^mD_x^n(e^\theta\cdot1)&=(-1)^{m+n}D_t^mD_x^n(1\cdot e^\theta)=b^ma^ne^\theta
\end{align*}$$Therefore the bilinear form of the KdV equation for $f=1+e^\theta$ is:$$\Huge\begin{align*}
0&=(D_tD_x+D_x^4)(1+e^\theta\cdot1+e^\theta)\\
&=(D_tD_x+D_x^4)((1\cdot1)+(1\cdot e^\theta)+(e^\theta\cdot 1)+(e^\theta\cdot e^\theta))\\
&=2(D_tD_x+D_x^4)(e^\theta\cdot 1)\\
&=2(ba+a^4)e^\theta=2a(b+a^3)e^\theta
\end{align*}$$Given that $e^\theta$ is nonzero, there are two ways to satisfy this equation:
> $a=0$ makes $f$ independent of $x$ and therefore $u=0$, trivial.
> $b=-a^4$, then:$$\Huge f=1+e^{ax-a^3t+c}\implies u=2\frac{\partial^2}{\partial x^2}\log(1+e^{ax-a^3t+c})$$which is exactly the one-soliton solution with $v=a^2$ up to redefinition of constants.

