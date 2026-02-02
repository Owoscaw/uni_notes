
Let $\Omega\subseteq\Re^n$ be open, Poisson's equation is then the PDE:$$\Huge -\Delta u=f$$for a given $f:\Omega\rightarrow\Re$. If $f=0$ then $\Delta u=0$ and we say that $u$ is harmonic. Poisson's equation is the prototypical example of an [[Partial differential equations#Elliptic PDEs|elliptic PDE]].

# Elliptic PDEs:

Let $\Omega\subseteq\Re^n$ be open and $a_{ij},b_j,c:\Omega\rightarrow\Re$ for $i,j\in\{1,\dots,n\}$. Let $A$ be the matrix-valued function defined by:$$\Huge [A(\underline{x})]_{ij}=a_{ij}(\underline{x})$$ and let $\underline{b}$ be the vector-valued function defined by:$$\Huge [\underline{b}(\underline{x})]_j=b_j(\underline{x})$$We now define the second order linear differential operator $L$:$$\Huge Lu=-\sum_{i,j=1}^na_{ij}u_{x_ix_j}+\sum_{j=1}^nb_ju_{x_j}+cu=-A:D^2u+\underline{b}\cdot\underline{\nabla}u+cu$$for $u:\Omega\rightarrow\Re$. We say that $u$ is elliptic if $A$ is symmetric and uniformly positive definite. That is, $a_{ij}(\underline{x})=a_{ji}(\underline{x})$ for all $\underline{x}\in\Omega$ and there exists some $\alpha>0$ such that $\underline{y}^TA(\underline{x})\underline{y}\geq\alpha|\underline{y}|^2$ for all $\underline{y}\in\Re^n,\underline{x}\in\Omega$. PDEs of the form $Lu(\underline{x})=f(\underline{x})$ are called elliptic. Poisson's equation satisfies this definition with $L=-\Delta,A=I,\underline{b}=\underline{0},c=0,\alpha=1$.

Linear, second order PDEs in two independent variables $(n=2)$ have form:$$\Huge Au_{x_1x_1}+2Bu_{x_1x_2}+Cu_{x_2x_2}+Du_{x_1}+Eu_{x_2}+Fu=f$$where the coefficients $A\dots F$ depend on the independent variables $(x_1,x_2)$. It is easy to check that if this PDE is elliptic, then $B^2-AC<0$. By the classification of conic sections,$$\Huge Ax_1^2+2Bx_1x_2+Cx_2^2+Dx_1+Ex_2+F=0$$defines an ellipse in the $x_1,x_2$ plane. This is where the name "elliptic" comes from. 

# Poisson's equation on $[a,b]$:

In one dimension, $\Delta u=u''$ and Poisson's equation takes form:$$\Huge -u''=f$$In which case we can find a solution simply by integrating, which we cannot do for higher dimensions. We begin by finding the solution subject to zero Dirichlet BCs:$$\Huge\begin{cases}-u''(x)=f(x)&x\in(a,b) \\
u(x)=0&x=a,b\end{cases}$$where $u:[a,b]\rightarrow\Re$ and $f\in C([a,b])$. We now use the fundamental theorem of calculus to integrate over $[a,z]$:$$\Huge \int_a^zu''(y)dy=-\int_a^zf(y)dy\iff u'(z)=u'(a)-\int_a^zf(y)dy$$now integrating over $[a,x]$:$$\Huge\begin{align*}
\int_a^xu'(z)dz&=\int_a^xu'(a)-\int_a^zf(y)dy\,dz\\
\iff u(x)-u(a)&=(x-a)u'(a)-\int_a^x\int_a^zf(y)dy\,dz\\
\iff u(x)&=(x-a)u'(a)-\int_a^x\int_a^zf(y)dy\,dz
\end{align*}$$This is not yet an explicit solution as $u'(a)$ appears on the RHS, however we can use the fact that $u(b)=0$:$$\Huge \begin{align*}
u(b)&=(b-a)u'(a)-\int_a^b\int_a^zf(y)dy\,dz=0\\
\implies u'(a)&=\frac{1}{b-a}\int_a^b\int_a^zf(y)dy\,dz
\end{align*}$$and so our explicit solution becomes:$$\Huge u(x)=\frac{x-a}{b-a}\int_a^b\int_a^zf(y)dy\,dz-\int_a^x\int_a^zf(y)dy\,dz$$However this is ugly, and we can tidy it up by changing the order of integration:$$\large\begin{align*}
u(x)&=\frac{x-a}{b-a}\int_a^b\int_y^bf(y)dz\,dy-\int_a^x\int_y^xf(y)dz\,dy\\
&=\frac{x-a}{b-a}\int_a^b(b-y)f(y)dy-\int_a^x(x-y)f(y)dy\\
&=\frac{x-a}{b-a}\left(\int_a^x(b-y)f(y)dy+\int_x^b(b-y)f(y)dy\right)-\int_a^x(x-y)f(y)dy\\
&=\int_a^x\left(\frac{(x-a)(b-y)}{b-a}-(x-y)\right)f(y)dy+\int_x^b\frac{(x-a)(b-y)}{b-a}f(y)dy\\
&=\int_a^x\frac{(y-a)(b-x)}{b-a}f(y)dy+\int_x^b\frac{(x-a)(b-y)}{b-a}f(y)dy
\end{align*}$$which we can write as:$$\Huge u(x)=\int_a^bG(x,y)f(y)dy,\,\,G(x,y)=\begin{cases}\frac{(y-a)(b-x)}{b-a}&y\leq x \\
\frac{(x-a)(b-y)}{b-a}&y\geq x\end{cases}$$We call $G$ a Green's function. Observe that $G(x,y)=G(y,x)$ is symmetric. Away from $x=y$, $G$ is twice differentiable and satisfies the one-dimensional Laplace equation in $x$ and $y$ ($G_{xx}=G_{yy}=0$ for $y\neq x$). The partial derivatives $G_x,G_y$ suffer a jump discontinuity across this line. The same procedure is used to solve Poisson's equation on $[a,b]$ with Neumann BCs as well as mixed BCs.

## Green's functions:
Let $\Omega\subseteq\Re^n$ be open and bounded with smooth boundary. It can be shown that if $u\in C^2(\bar\Omega)$ satisfies $-\Delta u=f$ in $\Omega$ and $u=g$ on $\partial\Omega$ where $f,g$ are continuous, then there exists a Green's function $G$:$$\Huge u(\underline{x})=\int_\Omega G(\underline{x},\underline{y})f(\underline{y})d\underline{y}-\int_{\partial\Omega}\underline{\nabla}_\underline{y}G(\underline{x},\underline{y})\cdot\underline{n}(\underline{y})g(\underline{y})dS(\underline{y})$$As above, this is symmetric and satisfies Laplace's equation in $\underline{x}$ and $\underline{y}$ away from $\underline{x}=\underline{y}$.

# Poisson's equation in $\Re^n$:

We now consider Poisson's equation in all of $\Re^n$ for $n\geq1$:$$\Huge-\Delta u(\underline{x})=f(\underline{x}),\,\,\underline{x}\in\Re^n$$If this equation has a solution, it cannot be unique as $u+v$ for any harmonic function $v$ will also be a solution. In order to obtain a unique solution, we must specify additional constraints. 

## Fundamental solution in $\Re^n$:
To derive the fundamental solution for $n\geq2$, we seek a radial solution of $\Delta u=0$. That is, we look for a solution of the form $u(\underline{x})=h(|\underline{x}|)$. Recall that:$$\Huge \frac{\partial }{\partial x_j}|\underline{x}|=\frac{x_j}{|\underline{x}|},\,\,\underline{\nabla}|\underline{x}|=\frac{\underline{x}}{|\underline{x}|}$$Therefore we write:$$\Huge\begin{align*}
\frac{\partial u}{\partial x_j}&=h'\frac{x_j}{|\underline{x}|},\,\,\underline{\nabla}u=h'\frac{\underline{x}}{|\underline{x}|}\\
\implies\frac{\partial^2u}{\partial x_j^2}&=h''\frac{x_j^2}{|\underline{x}|^2}+h'\frac{1}{|\underline{x}|}-h'x_j\frac{1}{|\underline{x}|^2}\frac{x_j}{|\underline{x}|}
\end{align*}$$And so:$$\Huge\begin{align*}
\Delta u&=\sum_{j=1}^n\frac{\partial^2u}{\partial x_j^2}=h''\frac{1}{|\underline{x}|^2}\sum_{j=1}^nx_j^2+h'\frac{n}{|\underline{x}|}-h'\frac{1}{|\underline{x}|^3}\sum_{j=1}^nx_j^2\\
&=h''+\frac{n-1}{|\underline{x}|}h'
\end{align*}$$Letting $r=|\underline{x}|$, we have shown that:$$\Huge \Delta u=0\iff h''(r)+\frac{n-1}{r}h'(r)=0$$This is a linear, first-order ODE in $h'$, so we solve by integrating factor:$$\Huge \exp\left(\int\frac{n-1}{r}dr\right)=\exp((n-1)\ln r)=r^{n-1}$$which gives:$$\Huge r^{n-1}h''+(n-1)r^{n-2}h'=0\iff \frac{d}{dr}(r^{n-1}h')=0$$Integrating this gives $h'(r)=Ar^{1-n}$ for some constant $A$, integrating further gives:$$\Huge h(r)=\begin{cases}A\ln r+B&n=2 \\
\frac{A}{2-n}r^{2-n}+B&n\geq3\end{cases}$$for some constant $B$. This makes our solution for $u$:$$\Huge u(\underline{x})=h(|\underline{x}|)=\begin{cases}A\ln|\underline{x}|+B&n=2 \\
\frac{A}{2-n}|\underline{x}|^{2-n}+B&n\geq3\end{cases}$$It is easy to check that this satisfies $\Delta u(\underline{x})=0$ for $\underline{x}\neq\underline{0}$. At the origin, $u$ is singular. By making a particular choice of $A,B$ we arrive at the following important solution.

The fundamental solution of Poisson's equation in $\Re^n$ is the map $\Phi:\Re^n\setminus\{\underline{0}\}\rightarrow\Re$ defined by:$$\Huge\Phi(\underline{x})=\begin{cases}-\frac{1}{2\pi}\ln|\underline{x}|&n=2 \\
\frac{1}{n(n-2)\alpha(n)}\frac{1}{|\underline{x}|^{n-2}}&n\geq3\end{cases}$$where:$$\Huge \alpha(n)=\frac{\pi^{n/2}}{\Gamma(\frac{n}{2}+1)}$$and where $\Gamma:(0,\infty)\rightarrow\Re$ is the Gamma function, defined by:$$\Huge \Gamma(s)=\int_0^\infty x^{s-1}e^{-x}dx$$Observe that $\Gamma(1)=1$. Using integrating by parts, one can check that $\Gamma$ satisfies $\Gamma(s+1)=s\Gamma(s)$. It can be shown that $\alpha(n)$ is the volume of the unit ball $B_1(\underline{0})$ in $\Re^n$:$$\Huge \alpha(n)=\int_{B_1(\underline{0})}1d\underline{x}$$It follows from a change of variables that $\alpha(n)r^n$ is the volume of a ball of radius $r$ in $\Re^n$. The surface area of a unit ball in $\Re^n$ is $n\alpha(n)$:$$\Huge n\alpha(n)=\int_{\partial B_1(\underline{0})}1dS$$
## Properties of the fundamental solution:
> $\Delta\Phi(\underline{x})=0$ for $\underline{x}\neq\underline{0}$
> $\Phi(\underline{x})\to\infty$ as $\underline{x}\to\underline{0}$
> $\Phi$ has an integrable singularity at the origin. For any $R>0$:$$\Huge\int_{B_R(\underline{0})}|\Phi(\underline{x})|d\underline{x}<\infty$$
> $\underline{\nabla}\Phi$ also has an integrable singularity at the origin.

The second derivatives of $\Phi$ are not so well behaved. If $\Delta\Phi$ were an integrable function, then for any $\epsilon>0$:$$\Huge\begin{align*}
-\int_{B_\epsilon(\underline{0})}\Delta\Phi d\underline{x}&=-\int_{B_\epsilon(\underline{0})}\text{div}(\underline{\nabla}\Phi)d\underline{x}\\
&=-\int_{\partial B_\epsilon(\underline{0})}\underline{\nabla}\Phi\cdot\underline{n}dS\\
&=\frac{1}{n\alpha(n)}\int_{\partial B_\epsilon(\underline{0})}\frac{\underline{x}}{|\underline{x}|^n}\cdot\frac{\underline{x}}{\epsilon}dS(\underline{x})\\
&=\frac{1}{n\alpha(n)}\int_{\partial B_\epsilon(\underline{0})}\frac{1}{\epsilon|\underline{x}|^{n-2}}dS(\underline{x})\\
&=\frac{1}{n\alpha(n)}\frac{1}{\epsilon^{n-1}}\int_{\partial B_\epsilon(\underline{0})}1dS\\
&=\frac{1}{n\alpha(n)}\frac{1}{\epsilon^{n-1}}\text{area}(\partial B_\epsilon(\underline{0}))\\
&=\frac{1}{n\alpha(n)}\frac{1}{\epsilon^{n-1}}n\alpha(n)\epsilon^{n-1}=1
\end{align*}$$However $\Delta\Phi(\underline{x})=0$ for all $\underline{x}\neq \underline{0}$, so the conditions $\int_{B_\epsilon(\underline{0})}\Delta\Phi d\underline{x}=-1$ and $\Delta\Phi(\underline{x})=0$ for $\underline{x}\neq\underline{0}$ are incompatible, suggesting that $\Delta\Phi$ is not an integrable function, but rather:$$\Huge -\Delta\Phi=\delta$$in the sense of distributions. This means that:$$\Huge -\int_{\Re^n}\Phi(\underline{y})\Delta\psi(\underline{y})d\underline{y}=\psi(\underline{0}),\,\,\forall\psi\in C_c^\infty(\Re^n)$$This is a direct result of taking $f=\psi,\underline{x}=\underline{0}$. 

## Function spaces:
Before continuing, recall the definition of the [[Distributions#Test functions|support]] of a function:
> We define the space of locally integrable functions on $\Re^n$ to be:$$\large L^1_\text{loc}(\Re^n)=\left\{\varphi:\Re^n\rightarrow\Re:\int_K|\varphi(\underline{x})|d\underline{x}<\infty\text{ for any compact set }K\subseteq\Re^n\right\}$$
> Let $k$ be a non-negative number. We let $$\Huge C_c^k(\Re^n)=\{f:\Re^n\rightarrow\Re:f\in C^k(\Re^n),\text{ supp}(f)\text{ is compact}\}$$denote the set of $k$ times continuously differentiable functions on $\Re^n$ with compact support. For $k=0$ we use the shorthand $C_c(\Re^n)$.

It is easy to see that $L^1(\Re^n)\subsetneqq L^1_\text{loc}(\Re^n)$, for example any constant function is in the locally supported set, but not $L^1(\Re^n)$.

We propose that $C_c(\Re^n)\subset L^\infty(\Re^n)$. To prove this, let $f\in C_c(\Re^n)$ and observe the definition:$$\Huge ||f||_{L^\infty(\Re^n)}=\sup_{\underline{x}\in\Re^n}|f(\underline{x})|=\sup_{\underline{x}\in\text{supp}(f)}|f(\underline{x})|<\infty$$Since continuous functions are bounded on compact sets, $f$ is continuous and $\text{supp}(f)$ is compact, by assumption.

Let $\varphi\in L^1_\text{loc}(\Re^n)$ and $f\in C_c(\Re^n)$. The convolution of $\varphi$ and $f$ is defined as $\varphi*f:\Re^n\rightarrow\Re$:$$\Huge (\varphi*f)(\underline{x})=\int_{\Re^n}\varphi(\underline{x}-\underline{y})f(\underline{y})d\underline{y}$$which has the following properties:
> $\varphi*f$ is well defined:$$\Huge|(\varphi*f)(\underline{x})|<\infty,\,\,\forall\underline{x}\in\Re^n$$
> Convolution is commutative:$$\Huge\varphi*f=f*\varphi$$
> If $\varphi\in L^1(\Re^n)$ then $\varphi*f\in L^\infty(\Re^n)$.
> More generally, if $\varphi L^p(\Re^n),f\in L^q(\Re^n)$ with $p,q\in[1,\infty]$, then $\varphi*f\in L^r(\Re^n)$ where:$$\Huge 1+\frac{1}{r}=\frac{1}{p}+\frac{1}{q}$$also:$$\Huge ||\varphi*f||_{L^r(\Re^n)}\leq||\varphi||_{L^p(\Re^n)}||f||_{L^q(\Re^n)}$$

Let $f\in C_c^2(\Re^n)$ be twice continuously differentiable with compact support. Define$$\Huge u=\Phi*f$$then $u\in C^2(\Re)$ and satisfies:$$\Huge -\Delta u(\underline{x})=f(\underline{x}),\,\,\underline{x}\in\Re^n$$We prove this for the $n=2$ case:
> By the symmetry of convolution:$$\Huge u(\underline{x})=(\Phi*f)(\underline{x})=(f*\Phi)(\underline{x})=\int_{\Re^2}\Phi(\underline{y})f(\underline{x}-\underline{y})d\underline{y}$$and therefore$$\Huge \Delta u(\underline{x})=\Delta\int_{\Re^2}\Phi(\underline{y})f(\underline{x}-\underline{y})d\underline{y}$$
> We now show that we can bring the Laplacian operator $\Delta$ inside the integral. Let $\underline{e}_1=(1,0),\underline{e}_2=(0,1)$ be the standard basis vectors for $\Re^2$. Letting $h>0$ and applying the mean value theorem to $g(h)=f(\underline{x}+h\underline{e}_i-\underline{y})$ gives:$$\Huge\begin{align*}
\frac{f(\underline{x}+h\underline{e}_i-\underline{y})-f(\underline{x}-\underline{y})}{h}&=\frac{g(h)-g(0)}{h-0}\\
&=g'(\xi)
\\
&=\underline{\nabla}f(\underline{x}+\xi\underline{e}_i-\underline{y})\cdot\underline{e}_i\\
&=f_{x_i}(\underline{x}+\xi\underline{e}_i-\underline{y})
\end{align*}$$for some $\xi=\xi(\underline{x},\underline{y})\in(0,h)$. Therefore:$$\large \frac{f(\underline{x}+h\underline{e}_i-\underline{y})-f(\underline{x}-\underline{y})}{h}-f_{x_i}(\underline{x}-\underline{y})=f_{x_i}(\underline{x}+\xi\underline{e}_i-\underline{y})-f_{x_i}(\underline{x}-\underline{y})$$Observe that $f_{x_i}$ is uniformly continuous since $f_{x_i}$ is continuous and has compact support. By the definition of uniform continuity, for all $\epsilon>0$ there exists $\delta(\epsilon)>0$ such that:$$\Huge |f_{x_i}(z_2)-f_{x_i}(z_1)|<\epsilon$$whenever $|z_2-z_1|<\delta(\epsilon)$. Choose some $0<h<\delta(\epsilon)$, then $|(\underline{x}+\xi\underline{e}_i-\underline{y})-(\underline{x}-\underline{y})|=\xi<h<\delta(\epsilon)$ and so:$$\Huge\left|\frac{f(\underline{x}+h\underline{e}_i-\underline{y})-f(\underline{x}-\underline{y})}{h}-f_{x_i}(\underline{x}-\underline{y})\right|<\epsilon,\,\,\forall\underline{x},\underline{y}\in\Re^2$$Consequently:$$\Huge \sup_{\underline{y}\in\Re^2}\Huge\left|\frac{f(\underline{x}+h\underline{e}_i-\underline{y})-f(\underline{x}-\underline{y})}{h}-f_{x_i}(\underline{x}-\underline{y})\right|<\epsilon,\,\,\forall h<\delta(\epsilon)$$That is to say, the sequence of functions:$$\Huge F_h^{\underline{x}}(\underline{y})=\frac{f(\underline{x}+h\underline{e}_i-\underline{y})-f(\underline{x}-\underline{y})}{h}$$converges uniformly as $h\to0$ to $F^{\underline{x}}(\underline{y})=f_{x_i}(\underline{x}-\underline{y})$. Since $f$ has compact support, we can write $u(\underline{x})$ as:$$\Huge u(\underline{x})=\int_{K_\underline{x}}\Phi(\underline{y})f(\underline{x}-\underline{y})d\underline{y}$$where $K_\underline{x}\subset\Re^2$ is any compact set containing $\{\underline{x}-\underline{z}:\underline{z}\in\text{supp}(f)\}$.
> For $0<h<1$ we have$$\large\frac{u(\underline{x}+h\underline{e}_i)-u(\underline{x})}{h}-\int_{\Re^2}\Phi(\underline{y})f(\underline{x}-\underline{y})d\underline{y}=\int_K\Phi(\underline{y})(F_h^{\underline{x}}(\underline{y})-F^\underline{x}(\underline{y}))d\underline{y}$$where $K\subset\Re^2$ is any compact set containing $\bigcup_{h\in[0,1]}K_{\underline{x}+h\underline{e}_i}$. Therefore$$\large\left|\frac{u(\underline{x}+h\underline{e}_i)-u(\underline{x})}{h}-\int_{\Re^2}\Phi(\underline{y})f_{x_i}(\underline{x}-\underline{y})d\underline{y}\right|\leq||F_h^\underline{x}-F^\underline{x}||_{L^\infty(\Re^n)}\int_K\Phi(\underline{y})d\underline{y}\to0$$as $h\to0$, since $F_h^\underline{x}$ converges uniformly to $F^\underline{x}$ and $\Phi\in L^1_\text{loc}(\Re^2)$. Hence the partial derivatives $u_{x_i}$ exist for $i\in\{1,2\}$ and:$$\Huge u_{x_i}(\underline{x})=\int_{\Re^2}\Phi(\underline{y})f_{x_i}(\underline{x}-\underline{y})d\underline{y}$$Moreover, $u_{x_i}$ is continuous since $f_{x_i}$ is continuous with compact support. Therefore $u\in C_c^1(\Re^2)$. Using the same argument for $u_{x_i}$, we find that:$$\Huge u_{x_ix_j}(\underline{x})=\int_{\Re^2}\Phi(\underline{y})f_{x_ix_j}(\underline{x}-\underline{y})d\underline{y}$$and that $u\in C^2(\Re^2)$. In particular,$$\Huge\Delta u(\underline{x})=\int_{\Re^2}\Phi(\underline{y})\Delta f(\underline{x}-\underline{y})d\underline{y}=\int_\Re^2\Phi(\underline{y})\Delta_{\underline{x}}f(\underline{x}-\underline{y})d\underline{y}$$as claimed.
> Now by the chain rule:$$\Huge\begin{align*}
\underline{\nabla}_\underline{y}f(\underline{x}-\underline{y})&=-\underline{\nabla}_\underline{x}f(\underline{x}-\underline{y})\\
\Delta_\underline{y}f(\underline{x}-\underline{y})&=\Delta_\underline{x}f(\underline{x}-\underline{y})\\
\implies\Delta u(\underline{x})&=\int_{\Re^2}\Phi(\underline{y})\Delta_\underline{y}f(\underline{x}-\underline{y})d\underline{y}
\end{align*}$$
> Now the remaining proof is simple, we use integration by parts to move the Laplacian from $f$ on to $\Phi$ and use the fact that $\Delta\Phi=0$ for all $\underline{x}\neq0$. The singularity at the origin however means this calculation must be done carefully.
> Let $0<\epsilon<1$. We then split the integral above in two parts:$$\large \Delta(\underline{x})=\int_{B_\epsilon(\underline{0})}\Phi(\underline{y})\Delta_\underline{y}f(\underline{x}-\underline{y})d\underline{y}+\int_{\Re^2\setminus B_\epsilon(\underline{0})}\Phi(\underline{y})\Delta_\underline{y}f(\underline{x}-\underline{y})d\underline{y}=I_\epsilon+J_\epsilon$$
> First we estimate $I_\epsilon$:$$\Huge\begin{align*}
|I_\epsilon|&=\left|\int_{B_\epsilon(\underline{0})}\Phi(\underline{y})\Delta_\underline{y}f(\underline{x}-\underline{y})d\underline{y}\right|\\
&\leq\int_{B_\epsilon(\underline{0})}|\Phi(\underline{y})||\Delta_\underline{y}f(\underline{x}-\underline{y})|d\underline{y}\\
&\leq\sup_{\underline{y}\in B_\epsilon(\underline{0})}|\Delta_\underline{y}f(\underline{x}-\underline{y})|\int_{B_\epsilon(\underline{0})}|\Phi(\underline{y})|d\underline{y}\\
&\leq\sup_{\underline{z}\in\Re^2}|\Delta f(\underline{z})|\int_{B_\epsilon(\underline{0})}|\Phi(\underline{y})|d\underline{y}\\
&=|||\Delta f||_{L^\infty(\Re^2)}||\Phi||_{L^1(B_\epsilon(\underline{0}))}
\end{align*}$$
> Observe that $\Delta f\in C_c(\Re^2)$ and so $||\Delta f||_{L^\infty(\Re^2)}<\infty$. Switching to polar coordinates, we compute:$$\Huge\begin{align*}
||\Phi||_{L^1(B_\epsilon(\underline{0}))}&=\int_{B_\epsilon(\underline{0})}|\Phi(\underline{y})|d\underline{y}\\
&=-\frac{1}{2\pi}\int_{B_\epsilon(\underline{0})}\ln|\underline{y}|d\underline{y}\\
&=-\frac{1}{2\pi}\int_{0}^{2\pi}\int_0^\epsilon r\ln r\,dr\,d\theta\\
&=-\int_0^\epsilon\ln r\,r\,dr\\
&=-\frac{r^2}{2}\ln r|_{0}^\epsilon+\int_0^\epsilon(\ln r)'\frac{r^2}{2}dr\\
&=-\frac{\epsilon^2}{2}\ln\epsilon+\frac{1}{2}\int_0^\epsilon r\,dr\\
&=-\frac{\epsilon^2}{2}\ln\epsilon+\frac{\epsilon^4}{4}
\end{align*}$$Therefore, $||\Phi||_{L^1(B_\epsilon(\underline{0}))}\to0$ as $\epsilon\to0$. This is because $\epsilon^2$ tends to $0$ faster than $|\ln\epsilon|$ goes to $\infty$. Combining our equations tells us that $I_\epsilon$ also tends to $0$ as $\epsilon\to0$.
> We now analyse $J_\epsilon$. Recalling the IBP formula:$$\Huge\int_\Omega\varphi(\underline{y})\text{div}\underline{g}(\underline{y})d\underline{y}=\int_{\partial\Omega}\varphi(\underline{y})\underline{g}(\underline{y})\cdot\underline{n}(\underline{y})dL(\underline{y})-\int_\Omega\underline{\nabla}\varphi(\underline{y})\cdot\underline{g}(\underline{y})d\underline{ y}$$where $\underline{n}$ is the outward normal vector field to $\partial\Omega$. Applying this formula with $\varphi(\underline{y})=\Phi(\underline{y}),\underline{g}(\underline{y})=\underline{\nabla}_\underline{y}f(\underline{x}-\underline{y})$ and $\Omega=\Re^2\setminus B_\epsilon(\underline{0})$ (noting that $\partial(\Re^2\setminus B_\epsilon(\underline{0}))=\partial B_\epsilon(\underline{0})$), we obtain:$$\large\begin{align*}
J_\epsilon&=\int_{\Re^2\setminus B_\epsilon(\underline{0})}\Phi(\underline{y})\Delta_\underline{y}f(\underline{x}-\underline{y})d\underline{y}\\
&=\int_{\Re^2\setminus B_\epsilon(\underline{0})}\Phi(\underline{y})\text{div}_\underline{y}\underline{\nabla}_\underline{y}f(\underline{x}-\underline{y})d\underline{y}\\
&=\int_{\partial B_\epsilon(\underline{0})}\Phi(\underline{y})\underline{\nabla}_\underline{y}f(\underline{x}-\underline{y})\cdot\underline{n}(\underline{y})dL(\underline{y})-\int_{\Re^2\setminus B_\epsilon(\underline{0})}\underline{\nabla}\Phi(\underline{y})\cdot\underline{\nabla}_\underline{y}f(\underline{x}-\underline{y})d\underline{y}\\
&=K_\epsilon+L_\epsilon
\end{align*}$$where $\underline{n}(\underline{y})$ is the outward-pointing unit normal to $\partial(\Re^2\setminus B_\epsilon(\underline{0}))$ at $\underline{y}$ and the inward-pointing unit normal to $\partial B_\epsilon(\underline{0})$ at $\underline{y}$. That is, it can be written as $\underline{n}(\underline{y})=-\underline{y}/|\underline{y}|=-\underline{y}/\epsilon$ since $\partial B_\epsilon(\underline{0})=\{\underline{y}\in\Re^2:|\underline{y}|=\epsilon\}$. Applying the Cauchy-Schwarz inequality we get$$\Huge |\underline{\nabla}_\underline{y}f(\underline{x}-\underline{y})\cdot\underline{n}(\underline{y})|\leq|\underline{\nabla}_\underline{y}f(\underline{x}-\underline{y})||\underline{n}(\underline{y})|=|\underline{\nabla}_\underline{y}f(\underline{x}-\underline{y})|$$Therefore:$$\Huge\begin{align*}
|K_\epsilon|&\leq\int_{\partial B_\epsilon(\underline{0})}|\Phi(\underline{y})||\underline{\nabla}_\underline{y}f(\underline{x}-\underline{y})\cdot\underline{n}(\underline{y})|dL(\underline{y})\\
&\leq\int_{\partial B_\epsilon(\underline{0})}|\Phi(\underline{y})||\underline{\nabla}_\underline{y}f(\underline{x}-\underline{y})|dL(\underline{y})\\
&\leq\sup_{y\in\partial B_\epsilon(\underline{0})}|\underline{\nabla}_\underline{y}f(\underline{x}-\underline{y})|\int_{\partial B_\epsilon(\underline{0})}|\Phi(\underline{y})|dL(\underline{y})\\
&\leq\sup_{z\in\Re^2}|\underline{\nabla} f(z)|\int_{\partial B_\epsilon(\underline{0})}|\Phi(\underline{y})|dL(\underline{y})\\
&=||\underline{\nabla} f||_{L^\infty(\Re^2)}||\Phi||_{L^1(\partial B_\epsilon(\underline{0}))}
\end{align*}$$Observe that $\underline{\nabla}f\in C_c(\Re^2)$ and so $||\underline{\nabla}f||_{L^\infty(\Re^2)}<\infty$. The boundary integral of $\Phi$ is easy to compute:$$\Huge\begin{align*}
||\Phi||_{L^1(\partial B_\epsilon(\underline{0}))}&=-\frac{1}{2\pi}\int_{\partial B_\epsilon(\underline{0})}\ln|\underline{y}|dL(\underline{y})\\
&=-\frac{1}{2\pi}\int_{\partial B_\epsilon(\underline{0})}\ln\epsilon\,dL(\underline{y})\\
&=-\frac{1}{2\pi}\ln\epsilon\int_{\partial B_\epsilon(\underline{0})}dL(\underline{y})\\
&=-\frac{1}{2\pi}\ln\epsilon(2\pi\epsilon)=-\epsilon\ln\epsilon
\end{align*}$$Therefore $||\Phi||_{L^1(\partial B_\epsilon(\underline{0}))}\to0$ as $\epsilon\to0$. Combining these equations shows that $K_\epsilon\to0$. It only remains to compute $L_\epsilon$, which we do using integration by parts$$\large\begin{align*}
L_\epsilon&=-\int_{\Re^2\setminus B_\epsilon(\underline{0})}\underline{\nabla}\Phi(\underline{y})\cdot\underline{\nabla}_\underline{y}f(\underline{x}-\underline{y})d\underline{y}\\
&=-\int_{\partial(\Re^2\setminus B_\epsilon(\underline{0}))}\underline{\nabla}\Phi(\underline{y})f(\underline{x}-\underline{y})\cdot\underline{n}(\underline{y})dL(\underline{y})+\int_{\Re^2\setminus B_\epsilon(\underline{0})}\Delta\Phi(\underline{y})f(\underline{x}-\underline{y})d\underline{y}\\
&=\int_{\partial B_\epsilon(\underline{0})}\underline{\nabla}\Phi(\underline{y})f(\underline{x}-\underline{y})\cdot\frac{\underline{y}}{\epsilon}dL(\underline{y})\\
&=-\int_{\partial B_\epsilon(\underline{0})}\frac{1}{2\pi}\frac{\underline{y}}{|\underline{y}|^2}f(\underline{x}-\underline{y})\cdot\frac{\underline{y}}{\epsilon}dL(\underline{y})\\
&=-\frac{1}{2\pi\epsilon}\int_{\partial B_\epsilon(\underline{0})}f(\underline{x}-\underline{y})dL(\underline{y})\\
&=-\frac{1}{2\pi\epsilon}\int_{\partial B_\epsilon(\underline{x})}f(z)dL(z)\\
&=-\int^*_{\partial B_\epsilon(\underline{0})}f(z)dL(z)
\end{align*}$$where the integral on the last line denotes the average of $f$ over $\partial B_\epsilon(\underline{x})$. Therefore this integral converges to $f(\underline{x})$ as $\epsilon\to0$.
> Combining our equations, $L_\epsilon\to-f(\underline{x})$ as $\epsilon\to0$ and$$\Huge \Delta u(\underline{x})=I_\epsilon+J_\epsilon=I_\epsilon+K_\epsilon+L_\epsilon\to-f(\underline{x})$$as $\epsilon\to0$, as required.

It remains to prove that the average of a function over the surface of a ball converges to the value at the center of the ball as radius tends to $0$. Let $g:\Re^n\rightarrow\Re$ be continuous and let $\underline{x}_0\in\Re^n$. Then$$\Huge \int^*_{\partial B_\epsilon(\underline{x}_0)}g(z)dS(z)\to g(\underline{x}_0),\,\,\epsilon\to0$$Proven under the assumption that $g$ is continuously differentiable:
> Observe that:$$\Huge\begin{align*}
\left|\int^*_{\partial B_\epsilon(\underline{x}_0)}g(z)dS(z)-g(\underline{x}_0)\right|&=\left|\int^*_{\partial B_\epsilon(\underline{x}_0)}(g(z)-g(\underline{x}_0))dS(z)\right|\\
&\leq\int^*_{\partial B_\epsilon(\underline{x}_0)}|g(z)-g(\underline{x}_0)|dS(z)
\end{align*}$$
> By the fundamental theorem of calculus and the chain rule$$\Huge\begin{align*}
|g(z)-g(\underline{x}_0)|&=\left|\int_0^1 \frac{d}{dt}g((1-t)\underline{x}_0+tz)dt\right|\\
&=\left|\int_0^1\underline{\nabla}g((1-t)\underline{x}_0+tz)\cdot(z-\underline{x}_0)dt\right|\\
&\leq\int_0^1|\underline{\nabla}g((1-t)\underline{x}_0+tz)||z-\underline{x}_0|dt\\
&\leq\max_{l(\underline{x}_0,z)}|\underline{\nabla}g||z-\underline{x}_0|
\end{align*}$$where $l(\underline{x}_0,z)$ is the line joining $\underline{x}_0$ to $z$. Let $\epsilon<1$ and let $M=\max_{B_1(\underline{x}_0)}|\underline{\nabla}g|$.
> We conclude that$$\Huge\left|\int^*_{\partial B_\epsilon(\underline{x}_0)}g(z)dS(z)-g(\underline{x}_0)\right|\leq\int^*_{\partial B_\epsilon(\underline{x}_0)}M|z-\underline{x}_0|dS(z)=M\epsilon\to0$$as $\epsilon\to0$, proving the result.

Note that the solution formula $u=\Phi*f$ has the same form as the Green's function representation with $\Omega=\Re^n$ and $G(\underline{x},\underline{y})=\Phi(\underline{x}-\underline{y})$. This solution can also be derived using the Fourier transform.

If $n\geq3$, it can be shown that if $u$ is any bounded solution of $-\Delta u=f$ in $\Re^n$, then $u=\Phi*f+C$ for some constant $C$. This follows from Liouville's theorem for harmonic functions. For $n=2$, $\Phi(\underline{x})=-\frac{1}{2\pi}\ln|\underline{x}|\to\infty$ as $|\underline{x}|\to0$ and so $u=\Phi*f$ may be unbounded.

## Fundamental solution in $\Re^n, n=1$:
The one dimensional case is not representative of the general case, however we include it for completeness. Let $f\in C_c^2(\Re)$ be twice continuously differentiable with compact support. We define$$\Huge \Phi(x)=\begin{cases}x&x\leq0 \\
0 & x\geq0\end{cases}$$and $u=\Phi*f$. Then $u\in C^2(\Re)$ and $u$ satisfies$$\Huge -u''(x)=f(x),\,\,x\in\Re$$We call $\Phi$ the fundamental solution of Poisson's equation in $\Re$. Note that for all $a,b\in\Re$, $u(x)=(\Phi*f)(x)+ax+b$ satisfies the equation.

# The Poincare inequality:

Before we move on to study Poisson's equation in general subsets of $\Re^n$, we first prove an important integral inequality. This is Poincare's inequality and dictates that there exists a constant $C>0$ such that$$\Huge \int_a^b|f(x)-\bar f|^2dx\leq C^2\int_a^b|f'(x)|^2dx$$for all $f\in C^1([a,b])$, where $\bar f$ denotes the average of $f$ over $[a,b]$:$$\Huge\bar f=\frac{1}{b-a}\int_a^bf(x)dx$$Note that we can write the Poincare inequality in terms of $L^2$ norms as$$\Huge ||f-\bar f||_{L^2([a,b])}\leq C||f'||_{L^2([a,b])}$$Remarks:
> The constant $C$ is independent of $f$, and depends only on the domain $[a,b]$. This can be seen without proving the inequality, as it can be shown that $C=(b-a)\tilde C$ for some constant $\tilde C>0$ independent of $a,b$ through a change of variables. Consequently, $C$ increases as the length of the interval $[a,b]$ increases.
> The Poincare inequality is false if we replace the LHS of the equation with $||f||_{L^2([a,b])}$. That is, there does not exist a constant $C>0$ such that$$\Huge||f||_{L^2([a,b])}\leq C||f'||_{L^2([a,b])}$$for all $f\in C^1([a,b])$. This is seen by taking $f$ to be a nonzero constant function, then the RHS is zero but the LHS is positive. If we restrict the class of functions to those that vanish on the boundary of the interval, this inequality turns out to be true.
> The Poincare inequality is true in any $L^p$ norm. For $1\leq p\leq\infty$, there exists a constant $C>0$ such that$$\Huge ||f-\bar f||_{L^p([a,b])}\leq C||f'||_{L^p([a,b])}$$for all $f\in C^1([a,b])$. Consider the case with $p=\infty$:$$\Huge \max_{[a,b]}|f-\bar f|\leq C\max_{[a,b]}|f'|$$It follows that$$\Huge \max_{[a,b]}|f|=\max_{[a,b]}|\bar f+f-\bar f|\leq|\bar f|+\max_{[a,b]}|f-\bar f|\leq|\bar f|+C\max_{[a,b]}|f'|$$That is, we can estimate the maximum absolute value of $f$ in terms of its average value and maximum slope.
> The Poincare inequality is true in any dimension.

We now prove the Poincare inequality:
> Recalling the MVT for integrals, let $f,g\in C([a,b])$ and $g\geq0$:$$\Huge\int_a^bf(x)g(x)dx=f(c)\int_a^bg(x)dx$$for some $c\in(a,b)$. Applying this with $g=1$ gives$$\Huge\bar f=\frac{1}{b-a}\int_a^bf(x)dx=\frac{1}{b-a}f(x)\int_a^bdx=f(c)$$for some $c\in(a,b)$. That is, $f$ attains its average at point $c$.
> By the fundamental theorem of calculus:$$\Huge f(x)-\bar f=f(x)-f(x)=\int_c^xf'(y)dy$$therefore:$$\Huge\begin{align*}
|f(x)-\bar f|&=\left|\int_c^xf'(y)dy\right|\\
&=\left|\int_c^x1\cdot f'(y)dy\right|\\
&\leq\left|\int_c^x1^2dy\right|^{1/2}\left|\int_c^x|f'(y)|^2dy\right|^{1/2}\\
&\leq|x-c|^{1/2}\left(\int_a^b|f'(y)|^2dy\right)^{1/2}
\end{align*}$$
> Taking the square integral of this gives$$\Huge\begin{align*}
\int_a^b|f(x)-\bar f|^2dx&\leq\int_a^b\left(|x-c|\int_a^b|f'(y)|^2dy\right)dx\\
&=\int_a^b|x-c|dx\int_a^b|f'(y)|^2dy\\
&\leq\int_a^b(b-a)dx\int_a^b|f'(y)|^2dy\\
&=(b-a)^2\int_a^b|f'(y)|^2dy
\end{align*}$$which is exactly the Poincare inequality with $C=b-a$.

The version of the Poincare inequality proven above is useful for PDEs with periodic of Neumann boundary conditions. We now introduce a version useful for PDEs with Dirichlet boundary conditions. There exists a constant $C>0$ such that$$\Huge\int_a^b|f(x)|^2dx\leq C^2\int_a^b|f'(x)|^2dx$$for all $f\in C^1([a,b])$ satisfying $f(a)=f(b)=0$. In terms of the $L^2$ norm, this is written as$$\Huge||f||_{L^2([a,b])}\leq C||f'||_{L^2([a,b])}$$

Let $\Omega\subset\Re^n$ be open and bounded. There exists a constant $C>0$ such that$$\Huge||f||_{L^2(\Omega)}\leq C||\underline{\nabla} f||_{L^2(\Omega)}$$for all $f\in C^1(\bar\Omega)$ satisfying $f=0$ on $\partial\Omega$. The proof of this follows from the Poincare inequality in one dimension. For simplicity we prove $n=2$ on $\Omega=(a,b)\times(c,d)$:$$\Huge\begin{align*}
\int_\Omega|f(\underline{x})|^2d\underline{x}&=\int_c^d\int_a^b|f(x,y)|^2dx\,dy\\
&\leq\int_c^d C^2\int_a^b|f_x(x,y)|^2dx\,dy\\
&\leq C^2\int_c^d\int_a^b(|f_x(x,y)|^2+|f_y(x,y)|^2)dx\,dy\\
&=C^2\int_\Omega|\underline{\nabla} f(\underline{x})|^2d\underline{x}
\end{align*}$$as required. For general domains $\Omega\subset\Re^2$, the idea of the proof is to extend the domain of $f$ to the whole rectangle by defining $f(\underline{x})=0$ outside $\Omega$. Then the proof above yields the desired result since the $L^2$-norm of $f$ and $\underline{\nabla}f$ will be unchanged. The same proof works for higher dimensions as well. Remarks:
> The constant $C$ depends on the domain $\Omega$. It can be shown that we can choose $C$ such that $C\leq\text{diam}(\Omega)$ where $\text{diam}(\Omega)=\sup\{|\underline{x}-\underline{y}|:\underline{x},\underline{y}\in\Omega\}$ is the diameter of $\Omega$.
> This theorem can be extended to any $L^p$-norm. That is, for $1\leq p\leq\infty$ there exists a constant $C>0$ such that $$\Huge||f||_{L^p(\Omega)}\leq C||\underline{\nabla}f||_{L^p(\Omega)}$$for all $f\in C^1(\bar\Omega)$ such that $f=0$ on $\partial\Omega$. 
> The Poincare inequality is not true if $\Omega=\Re^n$. It is however true if $f,\underline{\nabla}f\in L^2(\Omega)$ and if $\Omega$ is bounded between two parallel hyperplanes.
> The optimal Poincare constant is the smallest value of $C>0$ for which the Poincare inequality holds. Let us denote this value by $C_p$ and let$$\Huge V=\{\varphi\in C^1(\bar\Omega):\varphi=0\text{ on }\partial\Omega,\varphi\neq0\}$$, then we find that$$\Huge\frac{1}{C}\leq\frac{||\underline{\nabla}f||_{L^2(\Omega)}}{||f||_{L^2(\Omega)}}\,\,\forall f\in V\implies\frac{1}{C}\leq\inf_{f\in V}\frac{||\underline{\nabla}f||_{L^2(\Omega)}}{||f||_{L^2(\Omega)}}$$therefore we can set$$\Huge\frac{1}{C_p}=\inf_{f\in V}\frac{||\underline{\nabla}f||_{L^2(\Omega)}}{||f||_{L^2(\Omega)}}$$This expression can be used to show that $1/C_p^2$ is the smallest eigenvalue $\lambda_1$ of the operator $-\Delta$ on $V$. To be precise, $1/C_p^2$ is the smallest value of $\lambda\in\Re$ such that$$\Huge -\Delta u=\lambda u\text{ in }\Omega,u=0\text{ on }\partial\Omega$$for some $u\in C^2(\bar\Omega),u\neq0$.
 