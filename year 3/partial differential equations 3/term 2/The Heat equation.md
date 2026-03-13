
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

It turns out that there are infinitely many solutions of the Heat equation, however many blow up as $|\underline{x}|\to\infty$. Adding in mild growth conditions so that there exists constants $A,a>0$ with $$\Huge |u(\underline{x},t)|\leq Ae^{a|\underline{x}|^2}$$restricts the solution such that there exists at most one. Considering the heat equation with a source term$$\Huge\begin{align*}
u_t-k\Delta u&=f \text{ in }\Re^n\times(0,\infty)
\\
u&=g \text{ at }t=0\end{align*}$$, we see that this is satisfied by:$$\Huge u(\underline{x},t)=\int_{\Re^n}\Phi(\underline{x}-\underline{y})g(\underline{y})d\underline{y}+\int_0^t\int_{\Re^n}\Phi(\underline{x}-\underline{y},t-s)f(\underline{y},s)d\underline{y}\,ds$$
# Energy method:

Similar to Poisson's equation, there is not in general an explicit solution formula for spatial domain subsets of $\Re^n$. We can still determine a lot of qualitative properties of the solution using the energy method and maximum principles.

Let $\Omega\subset\Re^n$ be open, bounded, and connected with smooth boundary. Let $k,T>0$, then there exists at most one smooth solution $u:\bar\Omega\times[0,T]\rightarrow\Re$ of the heat equation:$$\Huge\begin{align*}
u_t-k\Delta u&=f \text{ in }\Omega\times(0,T]
\\
u&=g \text{ on }\partial\Omega\times[0,T]\\
u&=u_0 \text{ on }\Omega\times\{0\}\end{align*}$$We prove this using the energy method:
> Let $u_1,u_2$ be solutions and define $w=u_1-u_2$. Linearity of the heat equation then dictates:$$\Huge\begin{align*}
w_t-k\Delta w&=0 \text{ in }\Omega\times(0,T]\\
w&=0 \text{ on }\partial\Omega\times[0,T]\\
w&=0 \text{ on }\Omega\times\{0\}
\end{align*}$$
> Multiplying by $w$ and integrating by parts over $\Omega$ gives$$\begin{align*}
\int_\Omega ww_td\underline{x}=k\int_\Omega w\Delta wd\underline{x}&\iff\int_\Omega\frac{\partial }{\partial t}\frac{1}{2}w^2d\underline{x}=k\int_{\partial\Omega}w\underline{\nabla}w\cdot\underline{n}dS-k\int_\Omega\underline{\nabla}w\cdot\underline{\nabla}wd\underline{x}\\
&\iff \frac{d}{dt}\frac{1}{2}\int_\Omega w^2d\underline{x}=-k\int_\Omega|\underline{\nabla} w|^2d\underline{x}
\end{align*}$$since $w=0$ on $\partial\Omega$. Defining$$\Huge E(t)=\frac{1}{2}\int_\Omega w^2(\underline{x},t)d\underline{x}$$we have shown that:$$\Huge \frac{dE}{dt}=-k\int_\Omega|\underline{\nabla}w|^2d\underline{x}\leq0$$
> Integrating gives$$\Huge E(t)\leq E(0)=\frac{1}{2}\int_\Omega w^2(\underline{x},0)d\underline{x}=0$$, therefore $0\leq E(t)\leq E(0)=0$ and hence $E(t)=0$ for all $t\in[0,T]$. Therefore we conclude $w=0$ and $u_1=u_2$ as required.


## Gronwall and Sobolev inequalities:
We can also use the energy method to study the asymptotic behaviour of solutions as $t\to\infty$. First we introduce some inequalities:
> The Gronwall inequality: Let $E:[0,\infty)\rightarrow\Re$ be a continuously differentiable function satisfying $\dot E\leq-\lambda E$ for some constant $\lambda\in\Re$. Then $E(t)\leq e^{-\lambda t}E(0)$ for all $t\geq0$. Proof:
> > Multiplying the inequality by the integrating factor $e^{\lambda t}$ and rearranging we find$$\Huge e^{\lambda t}\dot E+e^{\lambda t}\lambda E\leq0\iff \frac{d}{dt}(e^{\lambda t}E)\leq0$$, which we integrate to find:$$\Huge e^{\lambda t}E(t)\leq e^{\lambda\cdot0}E(0)=E(0)\iff E(t)\leq e^{-\lambda t}E(0)$$As required.
> > This result determines that solutions of the differential inequality $\dot E\leq-\lambda E$ are bounded by solutions of the differential equation $\dot E=-\lambda E$, a type of comparison principle.
> Sobolev Embedding theorem: Let $f\in C^1([a,b])$, then for all $x,y\in[a,b]$$$\Huge |f(y)-f(x)|\leq||f'||_{L^2([a,b])}|y-x|^{1/2}$$, that is $f$ is Holder continuous with exponent $1/2$. Proof:
> > By the fundamental theorem of calculus$$\Huge\begin{align*}
|f(y)-f(x)|&=\left|\int_x^yf'(s)ds\right|\\
&=\left|\int_x^y1\cdot f'(s)ds\right|\\
&\leq\left|\int_x^y1^2ds\right|^{1/2}\left|\int_x^y|f'(s)|^2ds\right|^{1/2}\\
&\leq|y-x|^{1/2}||f'||_{L^2([a,b])}
\end{align*}$$
> The Sobolev inequality: There exists a constant $C>0$ such that$$\Huge||f||_{L^\infty([a,b])}\leq C||f||_{H^1([a,b])}$$where $||f||_{H^1([a,b])}=(||f||_{L^2([a,b])}^2+||f'||_{L^2([a,b])})^{1/2}$. Proof:
> > This follows from the proof of Sobolev's embedding theorem. For all $y\in[a,b]$:$$\Huge\begin{align*}
|f(y)|&=|f(x)+f(y)-f(x)|\\
&\leq|f(x)|+|f(y)-f(x)|\\
&\leq|f(x)|+||f'||_{L^2([a,b])}|y-x|^{1/2}
\end{align*}$$
> > Recall the Young inequality $2\alpha\beta\leq\alpha^2+\beta^2$, then we can square our expression to find$$\Huge\begin{align*}
|f(y)|^2&\leq(f(x)|+||f'||_{L^2([a,b])}|y-x|^{1/2})^2\\
&=|f(x)|^2+||f'||_{L^2([a,b])}^2|y-x|+2|f(x)|||f'||_{L^2([a,b])}|y-x|^{1/2}\\
&\leq2(|f(x)|^2+||f'||_{L^2([a,b])}^2|y-x|)
\end{align*}$$where we use the inequality on the last line. Integrating this wrt $x$ over $[a,b]$ yields:$$\Huge\begin{align*}
\int_a^b|f(y)|^2dx&\leq\int_a^b|f(x)|^2dx+2||f'||_{L^2([a,b])}^2\int_a^b|y-x|dx\\
&\leq2\int_a^b|f(x)|^2dx+2||f'||_{L^2([a,b])}^2\int_a^b(b-a)dx\\
&=2||f||_{L^2([a,b])}^2+2(b-a)^2||f'||_{L^2([a,b])}^2\\
&\leq2\max\{1,(b-a)^2\}(||f||_{L^2([a,b])}^2+||f'||_{L^2([a,b])}^2)
\end{align*}$$
> > Diving by $(b-a)$ and taking square roots gives$$\large|f(y)|\leq\left(\frac{2\max\{1,(b-a)^2\}}{b-a}\right)^{1/2}(||f||_{L^2([a,b])}^2+||f'||_{L^2([a,b])}^2)^{1/2}=C||f||_{H^1([a,b])}$$with $C=(2\max\{1,(b-a)^2\}/(b-a))^{1/2}$. Since this holds for all $y\in[a,b]$ we have proven the result.
> > Note that this inequality holds for $\Re$ as well and can be proven using Fourier transforms. Also if $f\in L^2$ and $f'$ is a nonsingular distribution with $f'\in L^2$ the result is also true.
> > This theorem does not work in higher dimensions, we have to make stronger assumptions on $f$ to obtain a $L^\infty$ bound.

Combining these inequalities with the energy method allows us to state the important result that follows. Let $u:\Re\times[0,\infty)\rightarrow\Re$ be smooth and $2\pi$-periodic in $x$. Let $u$ satisfy$$\Huge\begin{align*}
u_t-ku_{xx}&=0,\,\,(x,t)\in(0,2\pi)\times(0,\infty)\\
u(x,0)&=u_0(x),\,\,x\in(0,2\pi)
\end{align*}$$where $u_0:\Re\rightarrow\Re$ is a smooth $2\pi$-periodic function. Let $\bar u_0=\frac{1}{2\pi}\int_0^{2\pi}u_0(x)dx$ denote the average value of $u_0$. Then $u\to\bar u_0$ in $L^\infty([0,2\pi])$ as $t\to\infty$:$$\Huge\lim_{t\to\infty}||u(\cdot,t)-\bar u_0||_{L^\infty([0,2\pi])}=0$$That is, the temperature converges uniformly to the average initial temperature as $t\to\infty$. Proof:
> Let $w=u-\bar u_0$ and observe that$$\Huge\begin{align*}
 \frac{d\bar u}{dt}&=\frac{d}{dt}\frac{1}{2\pi}\int_0^{2\pi}u(x,t)dx\\
&=\frac{1}{2\pi}\int_0^{2\pi}u_t(x,t)dx\\
&=\frac{1}{2\pi}\int_0^{2\pi}ku_{xx}(x,t)dx\\
&=\frac{1}{2\pi}k[u_x]_0^{2\pi}=0
\end{align*}$$since $u_x$ is $2\pi$-periodic. This shows that the average value of $u$ is independent of $t$. Particularly $\bar u(t)=\bar u(0)=\bar u_0$ and so $\bar w=0$.
> By linearity, $w$ must satisfy:$$\Huge\begin{align*}
w_t-kw_{xx}&=0,\,\,(x,t)\in(0,2\pi)\times(0,\infty)\\
w(x,0)&=u_0(x)-\bar u_0
,\,\,x\in(0,2\pi)\end{align*}$$Multiplying this PDE by $w$ and integrating over $[0,2\pi]$ gives$$\large\int_0^{2\pi}ww_tdx=k\int_0^{2\pi}ww_{xx}dx\iff \frac{d}{dt}\frac{1}{2}\int_0^{2\pi}w^2dx=k[ww_x]_0^{2\pi}-k\int_0^{2\pi}w_x^2dx$$by the chain rule and IBP. Boundary terms vanish due to the periodicity of $w,w_x$.
> We write this in terms of the $L^2$ norms as:$$\Huge \frac{d}{dt}\frac{1}{2}||w||_{L^2([0,2\pi])}^2=-k||w_x||^2_{L^2([0,2\pi])}$$Since $\bar w=0$ we can write$$\Huge||w||_{L^2([0,2\pi])}^2=||w-\bar w||_{L^2([0,2\pi])}^2\leq C||w_x||_{L^2([0,2\pi])}^2$$for some constant $C>0$ by the Poincare inequality. 
> Combining these norm equations we can write:$$\Huge \frac{d}{dt}||w||_{L^2([0,2\pi])}^2=-2k||w_x||_{L^2([0,2\pi])}^2\leq-\frac{2k}{C}||w||_{L^2([0,2\pi])}^2$$Defining$$\Huge E(t)=||w||_{L^2([0,2\pi])}^2$$we can write this as$$\Huge \dot E\leq-\lambda E$$with $\lambda=2k/C>0$. This satisfies the Gronwall inequality and so$$\Huge E(t)\leq E(0)e^{-\lambda t}\to0 \text{ as }t\to\infty$$, therefore by definition of $E(t)$ we must have $w\to0$ in $L^2([0,2\pi])$ as $t\to\infty$.
> By differentiating the PDE for $w$ wrt $x$ we obtain:$$\Huge\begin{align*}
w_{xt}-kw_{xxx}&=0  \text{ for }(x,t)\in(0,2\pi)\times(0,\infty)\\
w_x(x,0)&=u_0'(x) \text{ for }x\in(0,2\pi)
\end{align*}$$That is, $w_x$ satisfies the heat equation with zero source term. Additionally $\bar w_x=0$ by periodicity of $w$. Therefore we apply our above argument to $w_x$, yielding $w_x\to0$ in $L^2([0,2\pi])$ as $t\to\infty$. Applying the Sobolev inequality completes the proof:$$\Huge ||w||_{L^\infty([0,2\pi])}^2\leq C||w||_{H^1([0,2\pi])}^2=C||w||_{L^2([0,2\pi])}^2+C||w_x||_{L^2([0,2\pi])}^2\to0$$

We can use the same method to study the same PDE with Dirichlet boundary conditions. Let $\Omega\subset\Re$ be open, bounded, and connected with smooth boundary. Let $u:\bar\Omega\times[0,\infty)\rightarrow\Re$ be a smooth function satisfying$$\Huge\begin{align*}
u_t(\underline{x},t)-k\Delta u(\underline{x},t)&=f(\underline{x}) \text{ for }(\underline{x},t)\in\Omega\times(0,\infty)\\
u(\underline{x},t)&=g(\underline{x}) \text{ for }(\underline{x},t)\in\partial\Omega\times[0,\infty)\\
u(\underline{x},0)&=u_0(\underline{x}) \text{ for }\underline{x}\in\Omega
\end{align*}$$where $f,g,u_0$ are given smooth functions. Let $v:\bar\Omega\rightarrow\Re$ be a smooth, time independent solution of the same equation. Then:$$\Huge\lim_{t\to\infty}||u-v||_{L^2(\Omega)}=0$$That is, if the source term and boundary data are independent of time, then the solution of the heat equation converges in the $L^2$ norm to the solution of Poisson's equation as $t\to\infty$.

This is notable as we see that $u$ tends to a time independent state as $t\to\infty$. More remarkable is that $u\to v$ as $t\to\infty$ for every initial condition $u_0$. This means that the long term behaviour of $u$ is independent of the starting point $u_0$.

Let us consider an example with periodic boundary conditions:
> Let $\Omega=\pi^n$ with $\partial\Omega=\emptyset$ and $u_0\in L^2(\Omega)$, we consider the PDE $\partial_t u+\Delta u=0$ and aim to show that for any $T>0$ and $m\in\{0,1,2,\dots\}$ we have $u(\cdot,T)\in C^m(\Omega)$.
> From the proof of uniqueness for the heat equation we found$$\Huge \partial_t||u(\cdot,t)||_{L^2(\Omega)}^2+2||\underline{\nabla} u(\cdot,t)||_{L^2(\Omega)}^2=0$$and so we integrate this:$$\Huge\begin{align*}
\implies2\int_0^T||\underline{\nabla} u(\cdot,s)||^2_{L^2(\Omega)}ds&=||u_0||_{L^2(\Omega)}^2-||u(\cdot,T)||_{L^2(\Omega)}^2\\
&\leq||u_0||_{L^2(\Omega)}^2+||u(\cdot,T)||^2_{L^2(\Omega)}\\
&\leq2||u_0||_{L^2(\Omega)}^2\\
\implies\int_0^T||u(\cdot,s)||^2_{L^2(\Omega)}ds&\leq||u_0||_{L^2(\Omega)}^2\\
\end{align*}$$
> We claim that there exists some $T_1\in[0,T/2]$ such that$$\Huge ||\underline{\nabla}u(\cdot,T_1)||_{L^2(\Omega)}^2\leq\frac{2}{T}||u_0||_{L^2(\Omega)}^2$$and prove it using contradiction. Assume that no such $T_1$ exists, then:$$\Huge\int_0^T||\underline{\nabla} u(\cdot,s)||_{L^2(\Omega)}^2\geq\int_0^{T/2}||\underline{\nabla} u(\cdot,s)||_{L^2(\Omega)}^2>\frac{2}{T}||u_0||_{L^2(\Omega)}^2\int_0^{T/2}ds$$This is a contradiction, so our ansatz holds.
> Multiplying our PDE by $-(\Delta u)$ and integrating shows us that$$\Huge \frac{1}{2}\partial_t||\underline{\nabla}u||^2+||\Delta u||^2=0$$to which we apply the Poincare inequality to find:$$\Huge \frac{1}{2}\partial_t||\underline{\nabla} u||^2+\frac{1}{c_p}||\underline{\nabla} u||\leq0$$
> Now we use the Gronwall inequality starting from $T_1$:$$\Huge\begin{align*}
||\underline{\nabla} u(\cdot,t)||^2&\leq e^{-(t-T_1)/c_p}||\underline{\nabla} u(\cdot,T_1)||^2\\
&\leq e^{-(t-T_1)/c_p}\frac{2}{T}||u_0||^2
\end{align*}$$Where we used our ansatz. This shows that $\underline{\nabla} u\in L^2(\Omega)$.
> In our integration step after multipling the PDE by $-(\Delta u)$ we found:$$\Huge\begin{align*}
2\int_{t_0}^{t_1}||\Delta u(\cdot,s)||^2ds&=||\underline{\nabla} u(\cdot,t_0)||^2-||\underline{\nabla} u(\cdot,t_1)||^2\\
&\leq2||\underline{\nabla} u(\cdot,T/2)||^2
\end{align*}$$We further apply the energy method by multiplying by $\Delta^2u$ and integrating:$$\Huge\begin{align*}
\int_\Omega\Delta^2u\cdot\partial_t u\,dV&=\int_\Omega\Delta u\cdot\Delta(\partial_t u)dV\\
&=\int_\Omega\frac{1}{2}\partial_t|\Delta u|^2dV\\
&=\frac{1}{2}\partial_t||\Delta u||^2
\end{align*}$$Alternatively we could have written:$$\Huge\begin{align*}
\int_\Omega\Delta^2u\cdot\Delta u\,dV&=\int_\Omega\underline{\nabla}\cdot\underline{\nabla}(\Delta u)\Delta u\,dV\\
&=\int_{\partial\Omega}\Delta u\underline{\nabla}(\Delta u)\cdot dS-\int_\Omega|\underline{\nabla}\Delta u|^2dV\\
&=-||\underline{\nabla}\Delta u||^2\\
\implies\frac{1}{2}\partial_t||\Delta u||^2+||\underline{\nabla}\Delta u||^2&=0
\end{align*}$$
> Combining this with the result from Poincare's lemma:$$\Huge\implies||\Delta u(\cdot,t)||^2\leq||\Delta u(\cdot,T_2)||^2e^{-2(t-T_2)/c_p}$$We can continue in our logic to show that every step we take, we get another power of $T$ in the denominator. If we continued here we would find:$$\Huge||\Delta u(\cdot,t)||^2\leq\frac{8}{T^2}||u_0||^2$$
> This shows that for any $T>0$ and $m\in\{0,1,\dots\}$ we have $(-\Delta)^{m/2}u\in L^2$ if and only if $u\in H^{m/2}$. To promote this to pointwise smoothness ($C^m(\Omega)$) we use the fact that if $u\in H^{m+n/2+\epsilon}$ then $u\in C^m(\Omega)$.

# Maximum principles:

