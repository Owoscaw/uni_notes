
# Regular curves, Length, and Tangent vectors:

A function $f:I\rightarrow\Re$ is called smooth if it can be differentiated infinitely many times.

Let $I$ be an interval and $\underline \alpha:I\rightarrow\Re^n$ be a map:
> We write $\underline \alpha(u)=(\alpha_1(u),\dots,\alpha_n(u))$, then $\underline \alpha$ is a smooth curve if all component functions $\alpha_i(u)$ are smooth maps
> The image of $I$ under $\underline \alpha$  ($\underline a(I)\subset\Re^n$)is called the trace of $\underline \alpha$
> The vector $\underline \alpha'(u)=(\alpha_1'(u),\dots,\alpha_n'(u))\in\Re^n$ is the tangent vector of $\underline \alpha$, where each $\alpha_i'$ are the derivatives of the component functions with respect to $u$
>  $\underline \alpha$ is said to be regular if $\underline \alpha'(u)\neq\underline 0$ for all $u\in I$, $\underline \alpha$ is said to be singular at $u_0\in I$ if $\underline \alpha'(u_0)=\underline 0$. That is, the tangent vector to the curve vanishes precisely at all of its singular points
>  If $\underline \alpha$ is regular, the unit tangent vector to $\underline \alpha$ at $u$ is:$$\Huge \underline t(u)=\frac{\underline \alpha'(u)}{||\underline \alpha'(u)||}$$we also write $\underline t=\underline t_{\underline \alpha}$ to emphasise when we need to specify the curve
>  If $||\underline \alpha'(u)||=1\forall u\in I$ we say that $\underline \alpha$ has a unit speed parametrisation

Take for example the helix defined by $\underline \alpha:\Re\rightarrow\Re^3$ with $\underline \alpha(u)=(\cos(u),\sin(u),u)$, the tangent vector for this curve is $\underline \alpha'(u)=(-\sin(u),\cos(u),1)$ and we have $||\underline \alpha'(u)||=\sqrt{2}$. So we see that this curve has constant but not unit speed.