
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