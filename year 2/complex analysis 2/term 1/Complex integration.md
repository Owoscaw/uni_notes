
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
\end{align}$$Let $\gamma$ be a contour and let $a=a_0<a_1<\dots<a_n=b$ be a partition of $[a,b]$ such that $\gamma_i=\gamma|_{[a_{i-1},a_i]}$ is $C^1$. Then:$$\ \int_\gamma f(z)dz=\sum_{i=1}^n\int_{\gamma_i}f(z)dz=\sum_{i=1}^nF(\gamma(a_i))-F(\gamma(a_{i-1}))=F(\gamma(a_n))-F(\gamma(a_0))=F(\gamma(b))-F(\gamma(a))$$As required. Note that if $f$ is continuous and $f=F'$ where $F$ is holomorphic then $\int_\gamma f(z)dz$ only depends on $\gamma(b)$ and $\gamma(a)$ and not the actual contour $\gamma$. Note that path independence is implied by the condition $\int_\gamma f(z)dz=0$ when $\gamma$ is a closed contour. Indeed if $\gamma_1$ and $\gamma_2$ start and end at the same point that $\gamma_1\cup(-\gamma_2)$ is a closed contour. Then we have:$$\large 0=\int_{\gamma_1\cup(-\gamma_2)}f(z)dz=\int_{\gamma_1}f(z)dz-\int_{\gamma_2}f(z)dz\implies\int_{\gamma_1}f(z)dz=\int_{\gamma_2}f(z)dz$$That is, every integration is path independent.

As an example, observe $\int_{|z|=r}z^ndz$ for $n\in\mathbb{Z}$. We know that for any $n\neq-1$ then the antiderivative of $z^n$ is $\frac{z^{n+1}}{n+1}$, an entire function when $n+1>0$ and holomorphic in $\mathbb{C}^*$ when $n+1<0$. Both domains contain $|z|=r$ so by the Fundamental Theorem of Calculus we know that:$$\Huge\int_{|z|=r}z^ndz=0$$Where $n+1=0$ there only exists a holomorphic anti derivative given by $\log z$ when a branch cut is removed. Note that in such a domain, $|z|=r$ cannot be contained and the Fundamental Theorem of calculus cannot be used.


## Estimation lemma and contour length:
Let $\gamma:[a,b]\mapsto\mathbb{C}$ be a contour. The length of $\gamma$ is defined by:$$\Huge L(\gamma)=\int_a^b|\gamma'(t)|dt$$Analogous to the [[Line integrals#Arclength|arclength]] of a line integral. We can then propose the estimation lemma. Let $F:U\mapsto\mathbb{C}$ be continuous and $\gamma:[a,b]\mapsto\mathbb{C}$ be a contour, then:$$\Huge\left|\int_\gamma f(z)dz\right|\leq(\sup_{z\in\gamma}|f(z)|)L(\gamma)$$This is analogous to the [[year 1/analysis 1/term 2/Integration#Properties|boundedness of the integral]]. To prove this, we start by showing that for any $g:[a,b]\mapsto\mathbb{C}$ continuous we have:$$\Huge\left|\int_a^b g(t)dt\right|\leq\int_a^b|g(t)|dt$$Indeed there exist $\theta\in(-\pi,\pi]$ such that:$$\Huge\begin{align}
\left|\int_a^bg(t)dt\right|&=e^{i\theta}\int_a^bg(t)dt\\
&=\Re\left(e^{i \theta}\int_a^bg(t)dt\right)\\
&=\Re\left(\int_a^be^{i\theta}g(t)dt\right)\\
&=\int_a^b\Re(e^{i\theta}g(t))dt\\
&\leq\int_a^b|e^{i\theta}g(t)|dt=\int_a^b|g(t)|dt
\end{align}$$Using the fact that $\Re(z)\leq|z|$, as required. Given a continuous function $f$ and some $C^1$ curve $\gamma$ we have:$$\Huge\begin{align}
\left|\int_\gamma f(z)dz\right|&=\left|\int_a^bf(\gamma(t))\gamma'(t)dt\right|\\
&\leq\int_a^b|f(\gamma(t))||\gamma'(t)|dt\\
&\leq\sup_{t\in[a,b]}|f(t)|\int_a^b|\gamma'(t)|dt=\sup_{z\in\gamma}|f(z)|L(\gamma)
\end{align}$$By definition, proving the theorem as required for any $C^1$ curve. To fully prove this for any contour, partition $[a,b]$ such that $a=a_0<a_1<\dots<a_n=b$, then:$$\Huge\begin{align}
\left|\int_\gamma f(z)dz\right|&=\left|\sum_{i=1}^n\int_{\gamma_i}f(z)dz\right|\\
&\leq\sum_{i=1}^n\left|\int_{\gamma_i}f(z)dz\right|\\
&\leq\sum_{i=1}^n\sup_{z\in\gamma_i}|f(z)|L(\gamma_i)\\
&\leq\sup_{z\in\gamma}|f(z)|\sum_{i=1}^nL(\gamma_i)=\sup_{z\in\gamma}|f(z)|L(\gamma)
\end{align}$$As required.

Let $U\subset\mathbb{C}$ be an open set and let $g:U\mapsto\Re$ be a continuous real valued function. For any $\gamma:[a,b]\mapsto U$ we can then define:$$\Huge\int_\gamma g(z)d|z|=\int_a^bg(\gamma(t))|\gamma'(t)|dt$$When proving the estimation lemma we showed:$$\Huge\left|\int_\gamma f(z)dz\right|\leq\int_a^b|f(z)|d|z|$$

# Complex Fundamental Theorem of Calculus:

Let $f:D\mapsto\mathbb{C}$ be continuous on a domain $D$. If $\int_\gamma f(z)dz=0$ for all closed contours $\gamma$ in $D$, then there exists a holomorphic $F:D\mapsto\mathbb{C}$ such that:$$\Huge F'(z)=f(z)$$
Let $a\in D$ be a given point. For any $z\in D$, there exists a path $\gamma_{a,z}$ that starts at $a$ and ends at $z$. This is always true since $D$ is a domain, making it path connected. We define:$$\Huge F(z)=\int_{\gamma_{a,z}}f(\xi)d\xi$$Such $F$ is well defined since the condition that $\int_\delta f(\xi)d\xi=0$ for any closed contour $\delta$ implies that is $\gamma_1$ and $\gamma_2$ are contours that start and end at the same point then:$$\Huge\int_{\gamma_1}f(\xi)d\xi=\int_{\gamma_2}f(\xi)d\xi$$That is, any contour that connects $a$ and $z$ would give the same value of the integration over said contour. Let $\delta_{z_0,z}$ be any contour that connects $z_0$ and $z$. Notice that $\gamma_{a,z_0}\cup\delta_{z_0,z}$ is a contour that starts at $a$ and ends at $z$. We can then state:$$\Huge\begin{align}
\int_{\gamma_{a,z}}f(\xi )d\xi&=\int_{\gamma_{a,z_0}\cup\delta_{z_0,z}}f(\xi)d\xi\\
&=\int_{\gamma_{a,z_0}}f(\xi)d\xi +\int_{\delta_{z_0,z}}f(\xi)d\xi\\
\implies F(z)&=F(z_0)+\int_{\delta_{z_0,z}}f(\xi)d\xi\\
\implies F(z)-F(z_0)&=\int_{\delta_{z_0,z}}f(\xi)d\xi
\end{align}$$For any contour $\delta_{z_0,z}$ that starts at $z_0$ and ends at $z$. Now consider the open ball $B_r(z_0)\subset D$, which exists since $D$ is open. As we consider the limit as $z\to z_0$ we can assume $z\in B_r(z_0)$ since $|z-z_0|<r$ in the limiting case. This implies that the curve:$$\Huge l(t)=z_0+t(z-z_0)$$For $t\in[0,1]$ is a straight line from $z$ to $z_0$, and is therefore completely contained within $B_r(z_0)$. This implies:$$\Huge F(z)-F(z_0)=\int_l f(\xi)d\xi$$Now the derivative of the line $l'(t)=z-z_0$ is trivial. As such we have:$$\Huge\begin{align}
\Huge F(z)-F(z_0)&=\int_0^1f(z_0+t(z-z_0))(z-z_0)dt\\
&=(z-z_0)\int_0^1f(z_0+t(z-z_0))\\
\implies\frac{F(z)-F(z_0)}{z-z_0}&=\int_0^1f(z_0+t(z-z_0))dt
\end{align}$$We cannot take the limit intuitively, so:$$\Huge\begin{align}
\left|\frac{F(z)-F(z_0)}{z-z_0}-f(z_0)\right|&=\left|\int_0^1f(z_0+t(z-z_0))dt-f(z_0)\right|\\
&=\left|\int_0^1f(z_0+t(z-z_0))-f(z_0)dt\right|\\
&\leq\sup_{t\in[0,1]}|f(z_0+t(z-z_0))-f(z_0)|L({[0,1]})
\end{align}$$Now since:$$\Huge \left|\frac{z_0+t(z-z_0)}{z(t)}-z_0\right|=t|z-z_0|\leq|z-z_0|$$Then since $f$ is continuous we have:$$\Huge\sup_{t\in[0,1]}|f(z_0+t(z-z_0))-f(z_0)|\to_{z\to z_0}0$$Now since we have:$$\Huge 0\leq\left|\frac{F(z)-F(z_0)}{z-z_0}-f(z_0)\right|\leq\sup_{t\in[0,1]}|f(z(t))-f(z_0)|$$In the limiting case we get:$$\Huge0\leq\lim_{z\to z_0}\frac{F(z)-F(z_0)}{z-z_0}\leq0$$And can therefore conclude:$$\Huge \lim_{z\to z_0}\frac{F(z)-F(z_0)}{z-z_0}=f(z)=F'(z)$$Since $z_0\in D$ was arbitrary, we have the proof as required. Since $D$ is a domain, suppose that $F_1$ and $F_2$ are antiderivatives of the same function then:$$\Huge(F_1-F_2)'=0$$Implying that $F_1-F_2$ is a constant
 