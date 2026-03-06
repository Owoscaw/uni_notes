
The heat, or diffusion, equation has form$$\Huge u_t-k\Delta u=f$$where $k>0$ is known as the diffusion coefficient. The unknown $u(\underline{x},t)$ can represent the temperature of a substance, or concentration of a chemical, etc. The RHS $f(\underline{x},t)$ represents the heat/chemical source.

Time independent solutions satisfy [[Poisson's equation]], and in fact many properties are shared between the two, like [[Laplace's equation#Maximum principles|maximum principles]]. We will see that diffusion equations have very different conservation law properties. The heat equation is the prototypical example of a [[Partial differential equations#Parabolic PDEs|parabolic PDE]].

Let $\Omega\subseteq\Re^n$ be open, $T>0$, and $a_{ij},b_j,c:\Omega\times(0,T)\rightarrow\Re$ for $i,j\in\{1,\dots,n\}$. Let $A$ be the matrix-valued function defined by $[A(\underline{x},t)]_{ij}=a_{ij}(\underline{x},t)$ and $\underline{b}$ the vector-valued function defined by $[\underline{b}(\underline{x},t)]_j=b_j(\underline{x},t)$. We now define the linear, second-order differential operator $L$$$\Huge Lu=-\sum_{i,j=1}^na_{ij}u_{x_ix_j}+\sum_{j=1}^nb_ju_{x_j}+cu=-A:D^2u+\underline{b}\cdot\underline{\nabla}u+cu$$for $u:\Omega\times(0,T)\rightarrow\Re$. PDEs of the form $u_t(\underline{x},t)+Lu(\underline{x},t)=f(\underline{x},t)$ are called parabolic if $A(\underline{x},t)$ is symmetric and uniformly positive definite. That is, $a_{ij}(\underline{x},t)=a_{ji}(\underline{x},t)$ for all $\underline{x}\in\Omega,t\in(0,T)$ and $\exists\alpha>0:\underline{y}^\top A(\underline{x},t)\underline{y}\geq\alpha|\underline{y}|^2$ for all $\underline{y}\in\Re^n,\underline{x}\in\Omega,t\in(0,T)$. For the heat equation:$$\Huge L=-k\Delta,\,\,A=kI,\,\,\underline{b}=0,\,\,c=0$$

# Fourier Series and the Heat Equation in $\Re\setminus2\pi\mathbb{Z}$:

Let us recall the notion of a [[Fourier Series]], which will help us solve linear, constant coefficient PDEs on periodic domains. First let us consider an interval $[0,L]$:


## Fourier series on $[0,L]$:
Let $L>0$ and $v\in L^2([0,L])$ and define $v_N\in L^2([0,L])$ by$$\Huge v_N(x)=\sum_{n=-N}^N\hat v_ne^{i\frac{2\pi n}{L}x}$$where the Fourier coefficients $\hat v_n$ are defined by:$$\Huge \hat v_n=\frac{1}{L}\int_0^Lv(x)e^{-i\frac{2\pi n}{L}x}dx$$Then $v_N$ converges to $v$ as $N\to\infty$ in the $L^2$-norm:$$\Huge \lim_{N\rightarrow\infty}||v-v_N||_{L^2([0,L])}=0$$Writing$$\Huge v(x)=\sum_{n=-\infty}^\infty\hat v_ne^{i\frac{2\pi n}{L}x}$$, we call the RHS the Fourier series of $v$. The notation we use here is a bit deceptive, the infinite sum denotes the $L^2$-limit of the [[Fourier Series#Partial sum|partial sum]] functions $v_N$. In general, $v_N$ may not converge pointwise to $v$. In particular, if $v:\Re\rightarrow\Re$ is $L$-periodic and [[Poisson's equation#Existence|Holder continuous]], then $v_N$ converges pointwise to $v$.

We can think of $\{e^{i\frac{2\pi n}{L}x}\}_{n\in\mathbb{Z}}$ as an orthonormal basis of the inner product space $L^2([0,L];\mathbb{C})$ of complex valued, square-integrable functions on $[0,L]$ with the inner product:$$\Huge (f,g)=\frac{1}{L}\int_0^Lf(x)\overline{g(x)}dx$$We can write the Fourier coefficients as $\hat v_n=(v,e^{i\frac{2\pi n}{L}x})$ using this inner product. That is to say, $\hat v_n$ are the components of $v$ wrt the basis we have discussed. We can write the Fourier series of $v$ as $$\Huge v(x)=\sum_{n=-\infty}^\infty(v,e^{i\frac{2\pi n}{L}x})e^{i\frac{2\pi n}{L}x}$$, highlighting the basis interpretation of the Fourier series.

Consider the heat equation with periodic boundary conditions on $[0,2\pi]$ and initial temperature distribution $g$:$$\Huge\begin{align*}
u_t&=ku_{xx}&(x,t)&\in(0,2\pi)\times(0,\infty)\\
u(0,t)&=u(2\pi,t)&t&\in[0,\infty]\\
u(x,0)&=g(x)&x&\in(0,2\pi)
\end{align*}$$If we think of $x$ as an angle, then this models heat distribution in a metal ring. Writing $u,g$ as a Fourier series in $x$ with $L=2\pi$$$\Huge u(x,t)=\sum_{n=-\infty}^\infty\hat u_n(t)e^{inx},\,\,g(x)=\sum_{n=-\infty}^\infty\hat g_n e^{inx}$$where:$$\Huge \hat u_n(t)=\frac{1}{2\pi}\int_0^{2\pi}u(x,t)e^{-inx}dx,\,\,\hat g_n=\frac{1}{2\pi}\int_0^{2\pi}g(x)e^{-inx}dx$$We can compute $\hat g_n$ from the initial data, so we aim to find the Fourier coefficients $\hat u_n$. Formally, we differentiate the Fourier series as:$$\Huge u_t(x,t)=\sum_{n=-\infty}^\infty \hat u_n'(t)e^{inx},\,\,u_{xx}(x,t)=-\sum_{n=-\infty}^\infty n^2\hat u_n(t)e^{inx}$$Substituting these into the heat equation gives$$\Huge \sum_{n=-\infty}^\infty\hat u_n'(t)e^{inx}=-k\sum_{n=-\infty}^\infty n^2\hat u_n(t)e^{inx}$$, which we multiply by $e^{-imx}/2\pi$ and integrate over $[0,2\pi]$ to get:$$\Huge \hat u_n'=-km^2\hat u_m=0\,\,\forall m\in\mathbb{Z}$$Similarly, the initial condition $u(x,0)=g(x)$ implies $\hat u_n(0)=\hat g_n$ for all $n\in\mathbb{Z}$. We have reduced the PDE to a family of uncoupled ODEs, indexed by $n\in\mathbb{Z}$:$$\Huge \hat u_n'(t)=-kn^2\hat u_n(t),\,\,\hat u_n(0)=\hat g_n$$Recalling that $x'=\lambda x$ has solution $x(t)=x(0)e^{\lambda t}$ we can write the solution for $\hat u_n$:$$\Huge \hat u_n(t)=\hat u_n(0)e^{-kn^2t}=\hat g_ne^{-kn^2t}$$This makes our solution for the heat equation:$$\Huge u(x,t)=\sum_{n=-\infty}^\infty\hat g_ne^{-kn^2t}e^{inx}$$In general we will not be able to find $\hat g_n$, however we can read off that in the $t\to\infty$ limit:$$\Huge u(x,t)\to\hat g_0=\frac{1}{2\pi}\int_0^{2\pi}g(x)dx$$
# Fourier Transform and Heat equation on $\Re^n$:

When the spatial domain of the heat equation on $\Re^n$, we can find an explicit solution using the Fourier transform. For a function $v\in L^1(\Re^n)$ we define its Fourier transform $\hat v:\Re^n\rightarrow\mathbb{C}$ by$$\Huge\hat v(\underline{\xi})=\frac{1}{(2\pi)^{n/2}}\int_{\Re^n}v(\underline{x})e^{i\underline{\xi}\cdot\underline{x}}d\underline{x}$$and its inverse Fourier transform $\tilde v:\Re^n\rightarrow\mathbb{C}$ by:$$\Huge\tilde v(\underline{x})=\frac{1}{(2\pi)^{n/2}}\int_{\Re^n}v(\underline{\xi})e^{i\underline{\xi}\cdot\underline{x}}d\underline{\xi}$$
> For the one-dimensional case, the Fourier transform $\hat v(\xi)$ reduces to the simpler formula for the Fourier coefficients $\hat v_n$ with $2\pi n/L$ replaced by $\xi$ and the domain $[0,L]$ replaced by $\Re$. We refer to $\xi$ as the frequency variable, the domain of $\hat v$ as frequency space (or Fourier space), and the domain of $v$ as physical space.
> The assumption that $v\in L^1(\Re^n)$ ensures that $\hat v\in L^\infty(\Re^n)$:$$\Huge\begin{align*}|\hat v(\underline{\xi})|&\leq\frac{1}{(2\pi)^{n/2}}\int_{\Re^n}|v(\underline{x})||e^{-i\underline{\xi}\cdot\underline{x}}|d\underline{x}\\
&=\frac{1}{(2\pi)^{n/2}}\int_{\Re^n}|v(\underline{x})|d\underline{x}\\
&=\frac{1}{(2\pi)^{n/2}}||v||_{L^1(\Re^n)}\\
\implies||\hat v||_{L^\infty(\Re^n)}&\leq\frac{1}{(2\pi)^{n/2}}||v||_{L^1(\Re^n)}<\infty\end{align*}$$The definition of the Fourier transform does not make sense for $v\in L^2(\Re^n)\setminus L^1(\Re^n)$ in general since the integral defining $\hat v$ need not be finite.

Let $v:\Re\rightarrow\Re$ be the Gaussian function $v(x)=e^{-ax^2},a>0$. We now compute its Fourier transform:$$\Huge\begin{align*}
\hat v(\xi)&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty e^{-ax^2}e^{-i\xi x}dx\\
&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty e^{-a(x^2+\frac{i\xi}{a}x)}dx\\
&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty e^{-a\left(\left(x+\frac{i\xi}{2a}\right)^2+\frac{\xi^2}{4a^2}\right)}dx\\
&=\frac{1}{\sqrt{2\pi}}e^{-\frac{\xi^2}{4a}}\int_{-\infty}^\infty e^{-a\left(x+\frac{i\xi }{2a}\right)^2}dx\\
&=\frac{1}{\sqrt{2\pi}}e^{-\frac{\xi^2}{4a}}\int_{-\infty}^\infty e^{-ax^2}dx\\
&=\frac{1}{\sqrt{2\pi}}e^{-\frac{\xi^2}{4a}}\sqrt{\frac{\pi}{a}}=\frac{1}{\sqrt{2a}}e^{-\frac{\xi^2}{4a}}
\end{align*}$$Therefore the Fourier transform of a Gaussian is another Gaussian. Observe that if $a>0$ is large, then $v$ is tightly distributed around the origin and $\hat v$ is spread out. The opposite is true, this is a sort of uncertainty principle; a function cannot be localised in both frequency and physical space:
> The Fourier transform of a derivative in one dimension is$$\Huge\hat u'(\xi)=i\xi \hat u(\xi)$$for $u,u'\in L^1(\Re)$. This extends to higher order derivatives as well as functions of several variables:$$\Huge\hat{\frac{\partial^\alpha u}{\partial x_1^{\alpha_1}\dots\partial x_n^{\alpha_n}}}(\underline{\xi})=(i\xi_1)^{\alpha_1}\dots(i\xi_n)^{\alpha_n}\hat u(\underline{\xi})$$
> For functions $u,v\in L^1(\Re^n)$ the Fourier transform of their convolution is:$$\Huge\hat{u*v}=(2\pi)^{n/2}\hat u\hat v$$
> Let $u\in L^1(\Re^n)\cap L^2(\Re^n)$, then:$$\Huge||\hat u||_{L^2(\Re^n)}=||u||_{L^2(\Re^n)}||\tilde u||_{L^2(\Re^n)}$$That is, the Fourier transform preserved the $L^2$ norm. As a side effect, the $L^2$ inner product is also preserved.

## The Fundamental Solution of the Heat Equation:
We use the Fourier transform to solve:$$\Huge\begin{align*}
u_t&=ku_{xx}\,\,(x,t)\in\Re\times(0,\infty)\\
u(x,0)&=g(x)\,\,x\in\Re
\end{align*}$$By linearity of the Fourier transform and other properties we find:$$\Huge \hat u_t=\hat{k u_{xx}}\iff\hat u_t(\xi,t)=k(i\xi)^2\hat u(\xi,t)=-k\xi^2\hat u(\xi,t)$$For the initial condition:$$\Huge\hat u(\xi,0)=\hat g(\xi)$$The PDE has been reduced to a one-parameter family of uncoupled ODEs indexed by $\xi$. Recalling that $\dot x=\lambda x$ has a solution $x(t)=x(0)e^{\lambda t}$, we apply this with $x=\hat u,\lambda=-k\xi^2$:$$\Huge \hat u(\xi,t)=\hat u(\xi,0)e^{-k\xi^2t}=\hat g(x)e^{-k\xi^2t}$$Therefore we can find $u$ by taking the inverse Fourier transform of this:$$\Huge u=\tilde{\hat u}=\tilde{\hat g(\xi)e^{-k\xi^2t}}$$To do this, we recognise that the RHS is a product of Fourier transforms, following from the fact that a Fourier transform of a Gaussian is a Gaussian:$$\Huge \implies e^{-k\xi^2t}=\sqrt{2a}\hat{e^{-ax^2}},\,\,a=\frac{1}{4kt}$$Therefore, since the product of Fourier transforms is the Fourier transform of a convolution:$$\Huge\begin{align*}
\hat g(\xi)e^{-k\xi^2t}&=\sqrt{2a}\hat g(\xi)\hat{e^{-ax^2}}(\xi)\\
&=\sqrt{2a}\frac{1}{\sqrt{2\pi}}\hat{g*e^{-ax^2}}(\xi)\\
&=\sqrt{\frac{a}{\pi}}\hat{g*e^{-ax^2}}(\xi)
\end{align*}$$Using this in our ODE and taking the inverse Fourier transform gives:$$\Huge\hat u(\xi,t)=\sqrt{\frac{a}{\pi}}\hat{g*e^{-ax^2}}(\xi)\iff u(x,t)\sqrt{\frac{a}{\pi}}g*e^{-ax^2}$$As convolution is commutative, we arrive at our solution:$$\Huge\begin{align*}
u(x,t)&=\frac{1}{\sqrt{4\pi kt}}g*e^{-\frac{x^2}{4kt}}\\
&=\frac{1}{\sqrt{4\pi kt}}e^{-\frac{x^2}{4kt}}*g\\
&=\frac{1}{\sqrt{4\pi kt}}\int_\Re e^{-\frac{(x-y)^2}{4kt}}g(y)dy
\end{align*}$$This derivation relies on the fact that the spatial domain of the PDE is all of $\Re$ and that the PDE is linear with constant coefficients, ensuring that the ODEs for the Fourier coefficients $\hat u$ are uncoupled. We can write the solution in the form $u=\Phi*g$ where $\Phi$ is the Gaussian:$$\Huge\Phi(x,t)=\frac{1}{\sqrt{4\pi kt}}e^{-\frac{x^2}{4kt}}$$This allows us to define the Fundamental solution for the heat equation $\Phi:\Re^n\times(0,\infty)\rightarrow\Re$ defined by:$$\Huge\Phi(\underline{x},t)=\frac{1}{(4\pi kt)^{n/2}}e^{-\frac{|\underline{x}|^2}{4kt}}$$One can show that $\Phi$ satisfies the heat equation in any dimension, however it is unclear what initial condition this satisfies. For the $n=1$ case we must have$$\Huge\int_{-\infty}^\infty\Phi(x,t)dx=1$$, additionally we observe$$\Huge\lim_{t\to0}\Phi(x,t)=\begin{cases}\infty & x=0 \\
0 & x\neq0\end{cases}$$since exponential decay kills polynomial blow up. This suggests that $\Phi\to\delta$ as $t\to0$ so in the sense of distributions it follows that:$$\Huge u=\Phi*g\to_{t\to0}\delta*g=g$$This is the interpretation of the initial condition, $u$ has initial value $g$. This derivation can be extended to $\Re^n$ and leads to the following result.

Let $k>0$ and $g\in C(\Re^n)$ be bounded. Define $u:\Re^n\times(0,\infty)\rightarrow\Re$ by$$\Huge u(\underline{x},t)=\frac{1}{(4\pi kt)^{n/2}}\int_{\Re^n}e^{-\frac{|\underline{x}-\underline{y}|^2}{4kt}}g(\underline{y})d\underline{y}=\Phi*g$$where $\Phi$ is the fundamental solution of the heat equation in $\Re^n$. Then we have:
> $u$ is infinitely differentiable $u\in C^\infty$
> $u$ satisfies the heat equation $u_t=k\Delta u$ in $\Re^n\times(0,\infty)$
> $u$ has initial value $g$, for each $\underline{x}_0\in\Re^n$:$$\Huge\lim_{\begin{align*}
(\underline{x},t)&\to(\underline{x}_0,0)\\
x\in\Re^n&,t>0
\end{align*}}u(\underline{x},t)=g(\underline{x}_0)$$

The solution we defined here has the following properties:
> Infinite speed of propagation: If $g\geq0$ and there exists $\underline{x}_0\in\Re^n$ such that $g(\underline{x}_0)>0$, then $u(\underline{x},t)>0$ for all $\underline{x}\in\Re^n$ and all $t>0$. That is, if temperature is initially positive somewhere, then after an infinitesimally small time the temperature is positive everywhere. One can interpret this as heat travelling with infinite speed.
> Convergence to equilibrium: If we assume $g\in L^1(\Re^n)$ then $$\Huge|u(\underline{x},t)|\leq\frac{1}{(4\pi kt)^{n/2}}||g||_{L^1(\Re^n)}$$for all $\underline{x}\in\Re^n,t>0$. 
> Smoothing property: While the initial distribution $g$ is only continuous, the solution is infinitely differentiable for all $t>0$. Therefore the heat equation has the property of instantly smoothing the initial data, opposite to the behaviour of conservation laws.