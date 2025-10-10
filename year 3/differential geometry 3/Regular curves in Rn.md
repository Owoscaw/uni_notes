
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

## Curve length
Consider the closed interval $[a,b]$. We aim to find the length of the curve between $\underline \alpha(a)$ and $\underline \alpha(b)$. To do this we partition $[a,b]$ such that $u_1=a<u_2<\dots<u_{m-1}<u_m=b$. The length can be approximated by:$$\Huge L\approx\sum_{i=0}^{m-1}||\underline \alpha(u_{i+1})-\underline \alpha(u_i)||$$Note that by the triangle inequality, this sum will always be a lower bound for the actual length of the curve. We now aim to refine the partition to find a better lower bound. This can not be done for every curve, so we must introduce the notion of a rectifiable curve:

A curve $\underline \alpha:I\rightarrow\Re^n$ is said to be rectifiable on $[a,b]$ if for any partition of the interval, the supremum:$$\large L(\underline \alpha|_{[a,b]})=\sup\left\{\sum_{i=0}^m||\underline \alpha(u_{i+1})-\underline \alpha(u_i)||:m\in\mathbb{N},\,a=u_1<\dots<u_m=b\right\}$$if finite. In which case, $L(\underline \alpha|_{[a,b]})$ is the arclength of $\underline \alpha$ between $\underline \alpha(a)$ and $\underline \alpha(b)$.

An example of a non-rectifiable curve is the Von-Koch snowflake, defined iteratively as follows:![[Regular curves in Rn 2025-10-10 14.50.37.excalidraw]]Iterating infinitely many times forms the Von-Koch snowflake. The sum of all of these "cones" at each iteration follows the formula $(4/3)^k$, which obviously blows up as $k\to\infty$, therefore the supremum of $L$ is not finite and the curve is not rectifiable.