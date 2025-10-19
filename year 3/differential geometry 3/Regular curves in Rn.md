
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

Let $\underline{\alpha}:I\rightarrow\Re^n$ be a smooth curve and $[a,b]\subset I$. Then the length of $\underline{\alpha}([a,b])$ is given by:$$\Huge L(\underline{\alpha}|_{[a,b]})=\int_a^b||\underline{\alpha}'(u)||du$$Proof is given heuristically:$$\Huge\begin{align*}
\sum_{i=0}^{m-1}||\underline{\alpha}(u_{i+1})-\underline{\alpha}(u_i)||&=\sum_{i=0}^{m-1}\left|\left|\frac{\underline{\alpha}(u_{i+1})-\underline{\alpha}(u_i)}{u_{i+1}-u_i}\right|\right|(u_{i+1}-u_i)\\
&=_{m\to\infty}\int_a^b||\underline{\alpha}'(u)||du
\end{align*}$$

# Reparametrisations and unit speed curves:

Let $\underline{\alpha}:I\rightarrow\Re^n$ be a smooth regular curve. A parameter change for $\underline{\alpha}$ is a map $h:J\rightarrow I$ where $J\subset\Re$ is an open interval such that:
> $h$ is smooth
> $h'(t)\neq0$ for all $t\in J$
> $h(J)=I$

Moreover, we call $\tilde{\underline{\alpha}}=\underline{\alpha}\circ h:J\rightarrow\Re^n$ a reparametrisation of $\underline{\alpha}$. The reparametrisation is orientation preserving if $h'>0$ and orientation reversing if $h'<0$. We aim to show that every smooth regular curve has a unit speed reparametrisation.

Let $\underline{\alpha}:I\rightarrow\Re^n$ be a smooth regular curve, $u_0\in I$, and $l:I\rightarrow\Re$ defined by:$$\Huge l(u)=\int_{u_0}^u||\underline{\alpha}'(t)||dt$$Let $J=l(I)\subset\Re$, then the curve $\underline{\alpha}\circ l^{-1}:J\rightarrow\Re^n$ is unit speed. Note that unit speed curves are also called arc length parametrised curves, and constant speed curves are also called proportional to arc length parametrised curves. To prove this, we first show that $l:I\rightarrow J\subset\Re$ is invertible. Note that:$$\Huge l'(u)=||\underline{\alpha}'(u)||>0$$as $\underline{\alpha}$ is a regular curve. Therefore $l$ is strictly increasing and must be bijective, so $l^{-1}:J\rightarrow I$ exists:$$\Huge (l^{-1})'(s)=\frac{1}{l'(l^{-1}(s))}=\frac{1}{||\underline{\alpha}'(l^{-1}(s))||}$$Now let $\underline{\beta}=\underline{\alpha}\circ l^{-1}$, so by the chain rule we have:$$\Huge \underline{\beta}'(s)=(\underline{\alpha}'\circ l^{-1})(s)\cdot(l^{-1})'(s)=\frac{\underline{\alpha'}(l^{-1}(s))}{||\underline{\alpha'}(l^{-1}(s))||}$$which implies $||\underline{\beta}'(s)||=1$ and $\underline{\beta}$ is a unit speed curve.

Note that curve regularity is essential in the proof, since if $\underline{\alpha}'(u)=0$ for some $u\in I$ then there will be a division by $0$. Note that length is invariant under reparametrisation. 

Let $\underline{\alpha}:I\rightarrow\Re^n$ be a smooth regular curve and $\tilde{\underline{\alpha}}=\underline{\alpha}\circ h:J\rightarrow\Re^n$ be a reparametrisation of $\underline{\alpha}$ with parameter change $h:J\rightarrow I$. Let $[a,b]\subset I$ and $[c,d]=h^{-1}([a,b])$. Then we have:$$\Huge L(\underline{\alpha}|_{[a,b]})=L(\tilde{\underline{\alpha}}|_{[c,d]})$$

# Plane curves:

We aim to introduce the notion of curvature for smooth plane curves. The basic approach is to compare the curve at a point to a fitted circle and to define the curvature as the reciprocal of the radius of said circle. Singular points must be avoided as there is no reasonable definition of curvature at singular points.

Let $\underline{\alpha}:I\rightarrow\Re^2$ be a smooth regular plane curve. Then the unit normal vector of $\underline{\alpha}$ at $u$ is obtained by anti-clockwise rotation of the unit tangent vector $\underline{t}(u)$ of $\underline{\alpha}$ at $u$ by $\pi/2$. That is, if $\underline{t}(u)=(x,y)$ then:$$\Huge \underline{\hat{n}}(u)=\underline{t}(u)\begin{pmatrix}\cos\pi/2 & \sin\pi/2 \\ -\sin\pi/2 & \cos\pi/2\end{pmatrix}=(x,y)\begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}=(-y,x)$$
Note that for unit speed curves, the change of the unit tangent vector $\underline{t}'(s)=\underline{\alpha}''(s)$ of $\underline{\alpha}$ at $s\in I$ is parallel to the unit normal vector $\underline{\hat{n}}(s)$. Formally, we let $\underline{\alpha}:I\rightarrow\Re^2$ be a smooth unit speed plane curve. Then the vector $\underline{t}'(s)$ is parallel to $\underline{\hat{n}}(s)$. We have that $\underline{t}(s)=\underline{\alpha}'(s)$, so the proof is an immediate consequence of the fact:$$\Huge\underline{\alpha}'(s)\cdot\underline{\alpha}'(s)=||\underline{\alpha}'(s)||=1$$differentiating wrt $s$ gives:$$\Huge \underline{\alpha}''(s)\cdot\underline{\alpha}'(s)+\underline{\alpha}'(s)\cdot\underline{\alpha}''(s)=2\underline{t}'(s)\cdot\underline{t}(s)=0$$which implies that $\underline{t}'(s)$ is perpendicular to $\underline{t}(s)$ and therefore must be parallel to $\underline{\hat{n}}(s)$. Since for a unit speed plane curve $\underline{\alpha}$, $\underline{t}'(s)$ is proportional to $\underline{\hat{n}}(s)$, we define the curvature of $\underline{\alpha}$ at $s$ as the proportionality factor.

For a straight line in $\Re^2$ we have $\underline{t}'(s)=0$ and the proportionality factor is $0$, which is expected as we want straight lines to have no curvature.

The signed curvature $\kappa(s)$ of a unit speed plane curve $\underline{\alpha}:I\rightarrow\Re^2$ at $s\in I$ is defined by:$$\Huge \underline{t}'(s)=\kappa(s)\underline{\hat{n}}(s)$$For a given unit speed plane curve $\underline{\alpha}:I\rightarrow\Re^2$ we can compute $\kappa(s)$ for $s\in I$:$$\Huge\begin{align*}
\underline{t'}(s)\cdot\underline{\hat{n}}(s)&=\kappa(s)\underline{\hat{n}}(s)\cdot\underline{\hat{n}}(s)=\kappa(s)||\underline{\hat{n}}(s)||^2=\kappa(s)
\end{align*}$$Writing $\alpha(s)=(x(s),y(s))$ we have $\underline{t}(s)=(x'(s),y'(s))$ and $\underline{\hat{n}}(s)=(-y'(s),x'(s))$, so the curvature becomes:$$\Huge\begin{align*}
\kappa(s)&=\underline{t}'(s)\cdot\underline{\hat{n}}(s)\\
&=(x''(s),y''(s))\cdot(-y'(s),x'(s))\\
&=-y'(s)x''(s)+x'(s)y''(s)
\end{align*}$$