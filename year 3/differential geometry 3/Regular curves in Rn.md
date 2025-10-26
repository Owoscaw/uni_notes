
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
Take for example a circle of radius $r>0$. We assume that it is centered at the origin, then a unit speed parametrisation is given by:$$\Huge \underline{\alpha}(s)=\left(r\cos\left(\frac{s}{r}\right),r\sin\left(\frac{s}{r}\right)\right)=(x(s),y(s))$$Then we have:$$\Huge\begin{align*}
(x'(s),y'(s))&=\left(-\sin\left(\frac{s}{r}\right),\cos\left(\frac{s}{r}\right)\right)\\
(x''(s),y''(s))&=\left(-\frac{1}{r}\cos\left(\frac{s}{r}\right),-\frac{1}{r}\sin(\frac{s}{r})\right)
\end{align*}$$We can now compute the curvature:$$\Huge\kappa(s)=-\left(\cos\frac{s}{r}\right)\left(-\frac{1}{r}\cos(\frac{s}{r})\right)+\left(-\sin\left(\frac{s}{r}\right)\right)\left(-\frac{1}{r}\sin\left(\frac{s}{r}\right)\right)=\frac{1}{r}$$fitting the requirement that a circle of radius $r$ should have curvature $1/r$. One can check that if we reverse the parametrisation, the curvature comes out to be $-1/r$. This reflects a general fact that reversing a parametrisation causes the curvature to change sign. In general, if a curve turns to the left, then $\kappa>0$, and if a curve turns to the right then $\kappa<0$.

General smooth regular plane curves $\underline{\alpha}:I\rightarrow\Re^2$ are usually not arc length parametrised, it is desirable to have an explicit formula for curvature without the need for reparametrisation:

Let $\underline{\alpha}:I\rightarrow\Re^2$ be a smooth regular plane curve with $\underline{\alpha}(u)=(x(u),y(u))$:$$\Huge \kappa=\frac{x'y''-x''y''}{((x')^2+(y')^2)^{3/2}}$$To prove this, we first consider:$$\Huge s=l(u)=\int_{u_0}^u||\underline{\alpha}'(t)||dt$$then we have $u=l^{-1}(s)$, and $\underline{\beta}=\underline{\alpha}\circ l^{-1}$ is an arc length reparametrisation of $\underline{\alpha}$ with tangent vector $\underline{t}$ and unit normal $\underline{\hat{n}}$. The curvature of $\underline{\alpha}$ at $u$ agrees with the curvature of $\underline{\beta}$ at $s$. Since $\underline{\beta}$ is unit speed:$$\Huge\begin{align*}
\underline{t}(s)=\underline{\beta}'(s)&=(\underline{\alpha}\circ l^{-1})'(s)\\
&=\underline{\alpha}'(l^{-1}(s))(l^{-1})(s)\\
&=\frac{\underline{\alpha}'(l^{-1}(s))}{||\underline{\alpha}'(l^{-1}(s))||}\\
&=\frac{\underline{\alpha}'(u)}{||\underline{\alpha}'(u)||}
\end{align*}$$Since $\underline{\alpha}(u)=(x(u),y(u))$, we have that $\underline{\alpha}'(u)=(x'(u),y'(u))$ and therefore:$$\Huge \underline{t}(s)=\frac{(x'(u),y'(u))}{||\underline{\alpha}'(u)||},\,\,\underline{\hat{n}}(s)=\frac{(-y'(u),x'(u))}{||\underline{\alpha}'(u)||}$$with $||\underline{\alpha}'(u)||=\sqrt{(x'(u))^2+(y'(u))^2}$. We must now calculate $\underline{t}'(s)$, so by the chain rule and the fact that $\frac{du}{ds}(s)=(l^{-1})'(s)=\frac{1}{||\underline{\alpha}'(u)||}$:$$\Huge \frac{d\underline{t}}{ds}(s)=\frac{d\underline{t}}{du}(u)\cdot\frac{du}{ds}(s)=\frac{1}{||\underline{\alpha}'(u)||}\cdot\frac{d}{du}\left(\frac{(x'(u),y'(u))}{\sqrt{(x'(u))^2+(y'(u))^2}}\right)$$We continue omitting the argument $u$:$$\large\begin{align*}
\frac{d}{du}\left(\frac{(x',y')}{\sqrt{(x')^2+(y')^2}}\right)&=\frac{\sqrt{(x')^2+(y')^2}(x'',y'')-\frac{x'x''+y'y''}{\sqrt{(x')^2+(y')^2}}(x',y')}{(x')^2+(y')^2}\\
&=\frac{((x')^2+(y')^2)(x'',y'')-(x'x''+y'y'')(x',y')}{||\underline{\alpha}'||^3}\\
&=\frac{x'y''-x''y'}{||\underline{\alpha}||^3}(-y',x')\\
&=\frac{x'y''-x''y'}{||\underline{\alpha}'||^2}\underline{\hat{n}}(s)=\underline{t}'(s)
\end{align*}$$Using this in the curvature formula gives:$$\Huge\begin{align*}
\kappa(s)&=\underline{t}'(s)\cdot\underline{\hat{n}}(s)\\
&=\frac{x'(u)y''(u)-x''(u)y'(u)}{||\underline{\alpha}'(u)||^3}||\underline{\hat{n}}(s)||^2\\
&=\frac{x'(u)y''(u)-x''(u)y'(u)}{((x'(u))^2+(y'(u))^2)^{3/2}}
\end{align*}$$

Take for example an ellipse. We define an ellipse as the set:$$\Huge \varepsilon_{a,b}=\left\{(x,y)\in\Re^2:\frac{x^2}{a^2}+\frac{y^2}{b^2}=1\right\}$$for fixed $a,b>0$. Note that $a=b=r$ describes the circle of radius $r>0$ centered at the origin. A parametrisation of $\varepsilon_{[a,b]}$ is given by:$$\Huge \underline{\alpha}:\Re\rightarrow\Re^2,\,\,\underline{\alpha}(u)=(a\cos u,b\sin u)$$This is obviously a regular curve as $\underline{\alpha}'(u)=(-a\sin u,b\cos u)\neq0$ for all $u\in\Re$. Note that in the regular case $a\neq b$ there is no closed expression for the arc length, as choosing $u_0=0$, the elliptic integral:$$\Huge l(u)=\int_0^u||\underline{\alpha}'(u)||du=\int_0^u\sqrt{a^2\sin^2u+b^2\cos^2u}\,du$$cannot be expressed in a closed form in terms of elementary functions. Therefore we cannot simply reparametrise an ellipse and calculate its curvature, however we can use the formula we just derived with:$$\Huge\begin{align*}
\underline{\alpha}'(u)&=(x',y')=(-a\sin u,b\cos u)\\
||\underline{\alpha}'(u)||&=\sqrt{a^2\sin^2u+b^2\cos^2u}\\
\underline{\alpha}''(u)&=(-a\cos u,-b\sin u)
\end{align*}$$so we have:$$\Huge\begin{align*}
\kappa(u)&=\frac{x'y''-x''y'}{((x')^2+(y')^2)^{3/2}}\\
&=\frac{(-a\sin u)(-b\sin u)-(-a\cos u)(b\cos u)}{(a^2\sin^2u+b^2\cos^2u)^{3/2}}\\
&=\frac{ab}{(a^2\sin^2u+b^2\cos^2u)^{3/2}}
\end{align*}$$

A geometric interpretation of curvature is that $|\kappa(u)|$ is the reciprocal of the radius of a circle approximating a small neighbourhood $\underline{\alpha}([u-\epsilon,u+\epsilon])$ as best as possible. The sign of $\kappa(u)$ is determined whether this approximating circle lies to the left or to the right of the curve at $\underline{\alpha}(u)$. We call such circle the curvature circle at $\underline{\alpha}(u)$.

Let $\underline{\alpha}:I\rightarrow\Re^2$ be a smooth regular plane curve, $\kappa:I\rightarrow\Re$ be its curvature function, and $\underline{\hat{n}}:I\rightarrow\Re^2$ be its unit normal. Assume $\kappa(u)\neq0$, then the radius of curvature is given by $r(u)=1/|\kappa(u)|$ and:$$\Huge \underline{e}(u)=\underline{\alpha}(u)+\frac{1}{\kappa(u)}\underline{\hat{n}}(u)\in\Re^2$$is called the center of curvature of $\underline{\alpha}$ at $\underline{\alpha}(u)$. The corresponding curvature circle of $\underline{\alpha}$ at $\underline{\alpha}(u)$ is given by:$$\Huge \{P\in\Re^2:||P-\underline{e}(u)||=r(u)\}$$![[Regular curves in Rn 2025-10-19 16.51.36.excalidraw]]

# Four-Vertex Theorem and FToPC:

Let $\underline{\alpha}:I\rightarrow\Re^2$ be a smooth regular plane curve with curvature $\kappa:I\rightarrow\Re$:
> A point $\underline{\alpha}(u_0)$ is called an inflection point of $\underline{\alpha}$ if $\kappa(u_0)=0$
> A point $\underline{\alpha}(u_0)$ is called a vertex of $\underline{\alpha}$ if $\kappa'(u_0)=0$

We saw that the curvature of the ellipse $\underline{\alpha}(u)=(a\cos u,b\sin u)$ with $a,b>0$ was given by:$$\Huge \kappa(u)=\frac{ab}{(a^2\sin^2u+b^2\cos^2u)^{3/2}}>0$$We can graph this compared to the ellipse:![[Regular curves in Rn 2025-10-26 05.28.08.excalidraw]]to see that the ellipse has no inflection points. Since:$$\Huge \kappa'(u)=\frac{3ab(a^2-b^2)\sin(2u)}{2(a^2\sin^2u+b^2\cos^2u)^{5/2}}$$we can conclude that with $a\neq b$ we have that the ellipse has vertices at $u=k\pi/2$ for $k\in\mathbb{Z}$. Restricting $\alpha:I\rightarrow\Re^2$ to $I=[0,2\pi]$ and using the fact that the ellipse is a closed curve, we see that the ellipse has four vertices, namely $(\pm a,0),(0,\pm b)\in\Re^2$. The curvature at these vertices is:$$\Huge (\pm a,0)\rightarrow\kappa(0)=\kappa(\pi)=\frac{a}{b^2},\,\,(0,\pm b)\rightarrow\kappa(\pi/2)=\kappa(3\pi/2)=\frac{b}{a^2}$$This fact is a special case of a more general result for simple smooth closed plane curves, called the Four-Vertex Theorem.

A plane curve $\underline{\alpha}:[a,b]\rightarrow\Re^2$ is called simple if the curve has no self-intersections. That is, $\underline{\alpha}(u_1)=\underline{\alpha}(u_2)$ for $u_1,u_2\in[a,b]$ implies $u_1=u_2$. For a curve to be called smooth, we require $\underline{\alpha}(b)=\underline{\alpha}(a)$ as well as that all one-sided derivatives at the two endpoints agree. An equivalent description for a closed curve $\underline{\alpha}:[a,b]\rightarrow\Re^n$ to be smooth is that it can be periodically extended to a map $\underline{\alpha}:\Re\rightarrow\Re^n$, which is $(b-a)$ periodic and smooth. This implies that in the case of a plane curve that the corresponding curvature function $\kappa:[a,b]\rightarrow\Re$ can also be extended to a smooth $(b-a)$ periodic function $\kappa:\Re\rightarrow\Re^n$.


## Four-Vertex Theorem:
Let $\underline{\alpha}:[a,b]\rightarrow\Re^2$ be a smooth regular simple closed plane curve. Then $\underline{\alpha}$ has at least $4$ vertices.

We do not give the full proof here, instead we offer a proof for the weaker statement that any smooth regular simple closed curve $\underline{\alpha}:[a,b]\rightarrow\Re^2$ has at least two vertices. If $\kappa:[a,b]\rightarrow\Re$ is the corresponding curvature function, it has at least two extremal points in $[a,b]$. If the minimum and maximum agree, then the curvature function is constant and $\underline{\alpha}$ therefore has infinitely many vertices. In any case we can extend $\kappa$ to a smooth $(b-a)$ periodic function $\kappa:\Re\rightarrow\Re$ on the whole real line. Then we see that $\kappa'$ must vanish at the maximum of $\kappa$ in $[a,b]$ and at the minimum of $\kappa$ in $[a,b]$. This guarantees the existence of at least two vertices of $\underline{\alpha}$.

This is a global result for simple closed plane curves. Another classical global result is the Isoperimetric Inequality, which states that a closed curve of length $L$ in the plane encloses the largest area if and only if the curve is a circle:

Let $\underline{\alpha}:[a,b]\rightarrow\Re^2$ be a smooth regular simple closed plane curve of length $L=L(\underline{\alpha})$ and $A$ be the area of the domain enclosed by $\underline{\alpha}$. Then:$$\Huge L^2\geq4\pi A$$with equality if and only if $\underline{\alpha}$ is a circle.

## Fundamental Theorem of Local Theory of Plane Curves:
Given an open interval $I\subset\Re$ and a smooth function $\kappa:I\rightarrow\Re$, $s_0\in I,a\in\Re^2,v_0\in\Re^2$ with $||v_0||=1$. Then there exists a unique smooth unit speed plane curve $\underline{\alpha}:I\rightarrow\Re^2$ with curvature function $\kappa$ and satisfying:$$\Huge\underline{\alpha}(s_0)=a,\,\,\underline{\alpha}'(s_0)=v_0$$That is to say, the curvature function determines the curve uniquely up to orientation preserving isometries. In other words, two unit speed plane curves $\underline{\alpha},\underline{\beta}$ with the same curvature function $\kappa:I\rightarrow\Re$ agree up to a map $f_{A,\underline{b}}$:$$\Huge \underline{\beta}=f_{A,\underline{b}}\circ\underline{\alpha}$$The idea of the proof is to construct the curve from the curvature function $\kappa$ via twofold integration. More formally, $\underline{\alpha}$ can be constructed as follows. Let $\theta_0\in[0,2\pi)$ be chosen to satisfy $v_0=(\cos\theta_0,\sin\theta_0)$. We then define $\theta:I\rightarrow\Re$ by:$$\Huge \theta(s)=\theta_0+\int_{s_0}^s \kappa(t)dt$$The unit tangent vector $\underline{t}:I\rightarrow\Re^2$ of the required unit speed curve $\underline{\alpha}$ is then already constructed and given by:$$\Huge \underline{t}(s)=(\cos(\theta(s)),\sin(\theta(s)))$$This completes the first integration and we construct the curve $\underline{\alpha}:I\rightarrow\Re^2$ by the second integral:$$\Huge\underline{\alpha}(s)=a+\left(\int_{s_0}^s\cos(\theta(t))dt,\int_{s_0}^s\sin(\theta(t))dt\right)$$It is trivial to check that $\underline{\alpha}(s_0)=a$ and $\underline{\alpha}'(s_0)=v_0$. One can then show that the curvature function of the constructed $\underline{\alpha}$ agrees with the given curvature function, completing the proof of existence. We omit the proof of uniqueness.

# Evolutes and involutes:

Returning to the geometric description of $|\kappa(u)|$ of $\underline{\alpha}$ as the reciprocal of the radius of a best-approximating circle of a small neighbourhood $\underline{\alpha}([u-\epsilon,u+\epsilon])$ of the curve and its center given as above, we can see that the centers of curvature $e(u)$ define a new curve under change of parameter. We call this new curve the evolute of $\underline{\alpha}$.

