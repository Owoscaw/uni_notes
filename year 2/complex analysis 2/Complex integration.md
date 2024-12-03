
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