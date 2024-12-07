
Given the notion of [[Complex differentiation]], it is natural to look for a notion of the opposite. On $\Re$, there was only one path from $a$ to $b$. In $\mathbb{C}$ there are infinitely many paths between two points.

Consider a continuous function $f:[a,b]\mapsto\mathbb{C}$ where $[a,b]\subset\Re$:$$\Huge \int_a^bf(t)dt=\int _a^b\Re(f(t))+i\Im(f(t))dt=\int_a^b\Re(f(t))dt+i\int_a^b\Im(f(t))dt$$Take $f(t)=t+it$ on $[0,1]$ as example:$$\Huge \int_0^1(t+it)dt=\int_0^1tdt+i\int_0^1tdt=\frac{1+i}{2}$$Writing $f_1=u_1+iv_1$ and $f_2=u_2+iv_2$, one can show that:
>$$\Huge\int_a^bf_1(t)+f_2(t)dt=\int_a^bf_1(t)dt+\int_a^bf_2(t)dt$$
>$$\Huge \int_a^bcf(t)dt=c\int_a^bf(t)dt$$

These can be proven by using the definition of the integral and linearity on $\Re$. 

# Integration along a path:

Recall the definition of a [[Complex differentiation#Paths and connectedness|path]] $\gamma:[a,b]\mapsto\mathbb{C}$ that is $C^1$ continuous:$$\Huge \gamma'(t)=(\Re(\gamma(t)))'+i(\Im(\gamma(t)))'$$We require that the real and imaginary parts of the path have left and right hand derivatives at the endpoints $a,b$. Take for example $\gamma:[0,2\pi]\to\mathbb{C}$ defined as $\gamma(\theta)=re^{i\theta}$ for some fixed $r>0$. Then $\Re(\gamma(\theta))=r\cos(\theta)$ and $\Im(\gamma(\theta))=r\sin(\theta)$. We then observe:$$\Huge \gamma'(t)=-r\sin\theta+ir\cos\theta=ir(\cos\theta+i\sin\theta)=ire^{i\theta}$$So we have that $\gamma$ is $C^1$ continuous. This path represents a parametrisation of a circle of radius $r$ in an anti clockwise motion. One can define $\gamma(\theta)=re^{-i\theta}$ for a parametrisation in a clockwise motion.

Let $U\subseteq\mathbb{C}$ be an open set and let $f:U\mapsto\mathbb{C}$ be a continuous function. Let $\gamma:[a,b]\mapsto U$ be a $C^1$ curve. We can then define the integral of $f$ along $\gamma$:$$\Huge \int_\gamma f(z)dz=\int_a^bf(\gamma(t))\gamma'(t)dt$$This is analogous to the [[Line integrals#Line integrals of vector fields|line integral]] of a vector field defined by $f(z)$ along a line parametrised by $\gamma(t)$. Assuming $f_1,f_2$ are continuous on $U$ and we have that for any $C^1$ path $\gamma:[a,b]\mapsto U$:
>$$\Huge\int_\gamma f_1(z)+f_2(z)dz=\int_\gamma f_1(z)dz+\int_\gamma f_2(z)dz$$
>For any $c\in\Re$:$$\Huge \int_\gamma cf(z)dz=c\int_\gamma f(z)dz$$
>Defining $(-\gamma):[-b,-a]\mapsto U$ to be $(-\gamma)(t)=\gamma(-t)$:$$\Huge \int_\gamma f(z)dz=-\int_{-\gamma}f(z)dz$$

The first two results follow from linearity of the integral. Taking the path $\gamma(\theta)=re^{i\theta}$ for some fixed $r>0$ we can compute the following examples:
> $\int_\gamma dz=\int_0^{2\pi}ire^{i\theta}d\theta=ir\int_0^{2\pi}\cos\theta d\theta-r\int_0^{2\pi}\sin\theta d\theta=0+0=0$
> $\int_\gamma\bar zdz=\int_0^{2\pi}\overline{re^{i\theta}}ire^{i\theta}d\theta=i^2\int_0^{2\pi}e^{i\theta-i\theta}d\theta=ir^2\int_0^{2\pi}d\theta=2\pi ir^2$
> $\int_\gamma z^ndz=\int_0^{2\pi}(re^{i\theta})^nire^{i\theta}d\theta=ir^{n+1}\int_0^{2\pi}e^{i\theta(n+1)}d\theta=ir^{n+1}e^{n+1}\int_0^{2\pi}e^{i\theta}d\theta=0$

Let $U\subseteq\mathbb{C}$ be an open set, $f:U\mapsto\mathbb{C}$ be a continuous function and let $\gamma:[a,b]\mapsto U$ be a $C^1$ curve. If $\varphi:[a',b']\mapsto[a,b]$ is a continuously differentiable bijection with $\varphi(a')=a$ and $\varphi(b')=b$ we define $\delta:[a',b']\mapsto\mathbb{C}$ by:$$\Huge \delta(t)=\gamma(\varphi(t))=\gamma\circ\varphi(t)$$Then we have:$$\Huge\int_\gamma f(z)dz=\int_\delta f(z)dz$$This can be proven by definition:$$\Huge\begin{align}
\int_\delta f(z)dz&=\int_{a'}^{b'}f(\delta(t))\delta'(t)dt\\
&=\int_{a'}^{b'}f(\gamma(\varphi(t)))\gamma'(\varphi(t))\varphi'(t)dt\\
&=\int_{\varphi(a')}^{\varphi(b')}f(\gamma(s))\gamma'(s)ds\\
&=\int_a^bf(\gamma(t))\gamma'(t)dt=\int_\gamma f(z)dz
\end{align}$$
Now consider $\gamma(\theta)=re^{i\theta}$ for $\theta\in[0,2\pi]$ and $\delta(t)=re^{2\pi it}$ for $t\in[0,1]$. Both parametrisations of the path describe the same shape almost bijectively. Note that $\varphi:[0,1]\mapsto[0,2\pi]$ defined by: $\varphi(\theta)=2\pi\theta$ is indeed a $C^1$ bijection and:$$\Huge \gamma(\varphi(\theta))=re^{2\pi i\theta}=\delta(\theta)\implies\int_\gamma f(z)dz=\int _\delta f(z)dz$$That is, the integral over both paths is the same. This does require $\varphi$ to be a [[Functions, Domain and Range#Bijectivity|bijective function]].

## Contours:
Let $\gamma:[a,b]\mapsto\mathbb{C}$ be a curve, and suppose that there exists $a=a_0<a_1<\dots<a_n=b$ such that the curve $\gamma_i:[a_{i-1},a_i]\mapsto\mathbb{C}$ for $i\in\{1,\dots,n\}$ defined by $\gamma_i(t)=\gamma(t)$ for $t\in[a_{i-1}a_i]$ are $C^1$ curves. We then say that $\gamma$ is piecewise $C^1$, a contour. For such contour we define:$$\Huge \int_\gamma f(z)dz=\sum_{i=1}^n\int_{\gamma_i}f(z)dz$$This allows the following path to be parametrised:![[contour]]This is a well defined definition, allowing us to define the integral over the boundary of a domain $D$. 

# Contour integrals:

Given a domain $D$ such that there exists a bijective contour $\gamma:[a,b]\mapsto\partial D$ with a continuous inverse $\gamma^{-1}:\partial D\mapsto[a,b]$ ($\gamma$ is a [[Homomorphisms|homeomorphism]]) and such that $\gamma'(t)\neq0$ we define:$$\Huge \int_{\partial D}f(z)dz=\int_\gamma f(z)dz$$This is well defined and does not depend on $\gamma$ as every curve can be reparametrised without changing the result of the integral. When $\partial D$ does not have end points, such as the circle, we extend the definition to the case where $\gamma:[a,b)\mapsto\partial D$ is a bijection and $\gamma(a)=\gamma(b)$. For example consider $D=\{z\in\mathbb{C}:|z-c|<r,r>0,c\in\mathbb{C}\}$ we have that:$$\Huge\partial D=\{z\in\mathbb{C}:|z-c|=r,r>0,c\in\mathbb{C}\}$$Which is the bijective image of the $C^1$ curve $\gamma:[0,2\pi)\mapsto\mathbb{C}$:$$\Huge \gamma_{c,r}(\theta)=c+re^{i\theta}$$Consequently:$$\Huge \int _{|z-c|=r}f(z)dz=\int_{\gamma_{c,r}}f(z)dz=\int_0^{2\pi}f(c+re^{i\theta})rie^{i\theta}d\theta$$
Let $\gamma:[a,b]\mapsto\mathbb{C}$ and $\delta:[c,d]\mapsto\mathbb{C}$ be two contour such that $\gamma(b)=\delta(c)$ we define their addition $\gamma\cup\delta$ as the curve:$$\Huge\gamma\cup\delta:[a,b+d-c]\mapsto\mathbb{C}$$Defined as:$$\Huge \gamma\cap\delta(t)=\begin{cases}\gamma(t)&a\leq t\leq b\\\delta(t+c-b)&b\leq t\leq b+d-c\end{cases}$$Then by the definition of integration along a counter and the variable change formula we have:$$\Huge\int_{\gamma\cup\delta}f(z)dz=\int_\gamma f(z)dz+\int_\delta f(z)dz$$This is illustrated as such:![[contour stitching]]
# Complex [[year 1/analysis 1/term 2/Integration#Fundamental theorem of Calculus|FTOC]]:

Let $U\subset\mathbb{C}$ be an open set and let $F:U\mapsto\mathbb{C}$ be [[Complex differentiation#Holomorphicity|holomorphic]] with continuous derivative $f$. Then the any contour $\gamma:[a,b]\mapsto U$ we have:$$\Huge\int_\gamma f(z)dz=F(\gamma(b))-F(\gamma(a))$$And in particular if $\gamma$ is a closed contour ($\gamma(a)=\gamma(b)$) then we have:$$\Huge \int_\gamma f(z)dz=0$$To prove this, assume that $\gamma$ is $C^1$. We then aim to find the integral of $f$ on $\gamma$ defined by:$$\Huge\begin{align}
\int_\gamma f(z)dz&=\int_a^bf(\gamma(t))\gamma'(t)dt\\
&=\int_a^bF'(\gamma(t))\gamma'(t)dt\\
&=\int_a^b\frac{d}{dt}F(\gamma(t))dt\\
&=\int_a^b\Re\left(\frac{d }{dt}F(\gamma(t))\right)dt+i\int_a^b\Im\left(\frac{d}{dt}F(\gamma(t))\right)dt\\
&=\int_a^b\frac{d}{dt}\Re(F(\gamma(t)))dt+i\int_a^b\frac{d}{dt}\Im(F(\gamma(t)))dt\\
&=\left[\Re(F(\gamma(t)))\right]_a^b+i\left[\Im(F(\gamma(t)))\right]_a^b\\
&=F(\gamma(b))-F(\gamma(a))
\end{align}$$Let $\gamma$ be a contour and let $a=a_0<a_1<\dots<a_n=b$ be a partition of $[a,b]$ such that $\gamma_i=\gamma|_{[a_{i-1},a_i]}$ is $C^1$. Then:$$\Huge \int_\gamma f(z)dz=\sum_{i=1}^n\int_{\gamma_i}f(z)dz=\sum_{i=1}^nF(\gamma(a_i))-F(\gamma(a_{i-1}))$$