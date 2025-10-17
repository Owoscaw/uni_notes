A partial differential equation (PDE) involves many variables and their [[Partial derivatives|partial derivatives]]. One such PDE is the heat equation:$$\Huge \frac{\partial u}{\partial t}=D\left(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}\right)$$This equation describes heat by a scalar function $u(x,y,t)$, the dependent variable. The behavior of the dependent variable is based on the independent variables: $x$, $y$, and $t$. These differ from ordinary [[First order differential equations|differential equations]], as PDEs involve many independent variables. The order of an ODE is the highest order derivative that appears in the equation. A PDE is linear if it is linear in the dependent variable, and nonlinear otherwise.

# Solutions:

A solution to a PDE in some region $R$ of the space of independent variables is a function, $u$, that possesses all the partial derivatives present in the PDE and satisfies said PDE on $R$. Consider the heat equation defined above. There are two spatial variables $x,y$ and one time variable $t$. We assume a square domain where $x,y\in[0,L]$, making $R=[0,L]\times[0,L]\times(0,\infty)$. A solution to this PDE is given:$$\Huge u(x,y,t)=e^{-D\left(\frac{n^2+m^2}{L^2}\right)t}\cos\left(\frac{n\pi x}{L}\right)\cos\left(\frac{m\pi x}{L}\right)$$With $n,m\in\mathbb{Z}$. All required partial derivatives exist, and the solution can be shown to satisfy the PDE. Note that another solution is given by:$$\Huge u(x,y,t)=e^{-D\left(\frac{n^2+m^2}{L^2}\right)t}\sin\left(\frac{n\pi x}{L}\right)\sin\left(\frac{m\pi x}{L}\right)$$ Boundary conditions also need to be specified. Boundary conditions specify how $u$ behaves at $\partial R$, the boundary of $R$. Consider the spatial domain of the heat equation:![[spatial domain]]Boundary conditions need to be specified for each $u$ seen above. Typically we fix $u(0,y,t),u(0,x,t),u(L,y,t),u(L,x,t)$, We must also fix $\underline{\nabla}u\cdot\underline{\hat{n}}$:$$\Huge\begin{align}
\frac{\partial u}{\partial x}(0,y,t)=\frac{\partial u}{\partial x}(L,y,t)=\frac{\partial u}{\partial y}(x,0,t)=\frac{\partial u}{\partial y}(x,L,t)=0
\end{align}$$Note that the cosine solution to the heat equation cannot satisfy these boundary conditions, as $\cos(0)\neq0$. Solutions to PDEs are not fully defined without their boundary conditions. In this case, the trivial $n=m=0$ solution is reserved for the cosine solution so that it remains defined. Morphogensis. This has very profound effects. Some equations can have general solutions, but cannot exist without boundary conditions.

# Linear equations and superposition:

We now sum over all solutions to the heat equation:$$\Huge u(x,y,t)=\sum_{n=0}^\infty\sum_{m=0}^\infty C_{nm}e^{-D\left(\frac{n^2+m^2}{L^2}\pi^2\right)t}\cos\left(\frac{n\pi x}{L}\right)\cos\left(\frac{m\pi y}{L}\right)$$Setting $t=0$ we see that this is equivalent to a [[Fourier Series|Fourier series]]. We confirm this solves the heat equation:$$\Huge\begin{align}
\frac{\partial^2u}{\partial x^2}&=-\frac{n^2\pi^2}{L^2}\sum_{n=0}^\infty\sum_{m=0}^\infty C_{nm}e^{-D\left(\frac{n^2+m^2}{L^2}\pi^2\right)t}\cos\left(\frac{n\pi x}{L}\right)\cos\left(\frac{m\pi y}{L}\right)\\
&=-\frac{n^2\pi^2}{L^2}u\\
\frac{\partial^2u}{\partial y^2}&=-\frac{m^2\pi^2}{L^2}u\\
\frac{\partial u}{\partial t}&=-D\left(\frac{n^2+m^2}{L^2}\right)\pi^2u\\
\implies\frac{\partial u}{\partial t}&=-D\left(-\frac{n^2\pi^2}{L^2}-\frac{m^2\pi^2}{L^2}\right)u=D\left(\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}\right)
\end{align}$$So this sum is indeed a solution to the heat equation:
> At $t=0$ this solution is a Fourier series, and can represent any smooth function
> Terms in this sum are linearly independent, meaning in term has its own unique contribution to $u(x,y,t)$


An important set of physical models have solutions in the form:$$\Huge u(x,t)=\sum_{n=0}^\infty T_n(t)S_n(x)$$Where $T_n$ is the $n$th temporal function, and $S_n$ is the $nth$ spatial function.

# Linearity operator:

We define the linear operator $L$ that acts on scalar functions as:$$\Huge L=\frac{\partial }{\partial t}-D\frac{\partial^2}{\partial x^2}$$A special cases of the heat equation is given by $Lu$. Linearity demands:$$\Huge L\left(\sum_{n=0}^\infty u_n\right)=\sum_{n=0}^\infty Lu_n$$

# Elliptic, parabolic, and hyperbolic equations:

Consider general second order linear PDEs:$$\Huge \sum_{i,j=1}^nA_{ij}\partial_i\partial_ju+\sum_{i=1}^nB_i\partial_iu+Cu+D=0$$Where $\partial_i=\frac{\partial }{\partial x_i},\partial_i\partial_j=\frac{\partial^2}{\partial x_ix_j}$. PDEs are classified by the highest order coefficients $A_{ij}$. Since $\partial_i\partial_j=\partial_j\partial_i$ we can write $A_{ij}$ as a symmetrical matrix, meaning it has $n$ real [[Eigenvalues, Eigenvectors, and Diagonalisation|eigenvalues]]. Let $a$ be the number of eigenvalues that are $0$, and let $b$ be the number of positive eigenvalues.

## Classification:
> Elliptic equations are such that $a=0$, $b=0\text{ or }n$
> Parabolic equations are such that $a>0, b\leq n-1$. This means that $\det A=0$.
> Hyperbolic equations are such that $a=0,b=1\text{ or }n-1$

Take for example the following PDE:$$\Huge 3\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}+4\frac{\partial^2u}{\partial z^2}+4\frac{\partial^2u}{\partial y\partial t}=0$$Here we have $A=\begin{pmatrix}3&0&0\\0&1&2\\0&2&4\end{pmatrix}$. This has eigenvalues $\lambda=0,3,5$ so $a=1$, making this PDE parabolic.

## Elliptic PDEs:
The main example of an elliptic PDE is Poisson's equation:$$\Huge \nabla^2u=f(x)$$Where $\nabla^2$ is the [[Index notation#Second derivatives|Laplacian]]. One specific solution is given by:$$\Huge f(\underline x)=Q\delta(x,y)+Q\delta(x-x_c,x-y_c)$$Where $\delta(x,y)$ is the Dirac delta function. In this case the equation describes a static electric field with two point charges of value $Q$. A solution to this equation in $\Re^2$ is given by:$$\Huge u(x,y)=\int_\Re G(x,y,x',y')f(x,y)dx'dy'$$Where $G(x,y,x',y')=\frac{1}{2\pi}\ln(|r|)$  and $$\Huge |r|=\sqrt{(x-x')^2+(y-y')^2+(z-z')^2}$$This function $G$ is called Green's function. Elliptic PDEs tend to be smooth, globally responsive, and time independent.

## Parabolic PDEs:
The heat equation is an example of a parabolic PDE:$$\Huge \frac{\partial u}{\partial t}=D\nabla^2u$$This is parabolic with $A=\begin{pmatrix}1&0\\0&1\end{pmatrix}=I$. Writing this equation in the form:$$\Huge \frac{\partial u}{\partial t}-\nabla^2u=0\implies A=\begin{pmatrix}0&0&0\\0&-1&0\\0&0&-1\end{pmatrix}\implies\det A=0$$Parabolic PDEs tend to be smooth, globally responsive, and time dependent.

## Hyperbolic PDEs:
The wave equation is an example of a hyperbolic PDE:$$\Huge \frac{\partial^2u}{\partial t^2}=c^2\nabla^2u$$A solution to the wave equation is given by:$$\Huge u(x,t)=f(x-ct)+g(x+ct)$$For arbitrary functions $f,g$. To verify this, we can use the chain rule and set $z=x-ct$ and $z^*=x+ct$:$$\Huge\begin{align}
\frac{\partial u}{\partial t}&=\frac{df}{dz}\frac{\partial z}{\partial t}+\frac{dg}{dz^*}\frac{\partial z^*}{\partial t}=c\left(-\frac{df}{dz}+\frac{dg}{dz^*}\right)\\
\frac{\partial u}{\partial x}&=\frac{df}{dz}\frac{\partial z}{\partial x}+\frac{dg}{dz^*}\frac{\partial z^*}{\partial x}=\frac{df}{dz}+\frac{dg}{dz^*}\\
\frac{\partial^2u}{\partial t^2}&=c^2\left(\frac{d^2f}{dz^2}+\frac{d^2g}{d(z^*)^2}\right)\\
\frac{\partial^2u}{\partial x^2}&=\frac{d^2f}{dz^2}+\frac{d^2g}{d(z^*)^2}
\end{align}$$So we see that this solution satisfies the wave equation. Note that $f,g$ were totally arbitrary and can be any function. These solutions are called travelling waves. Note that "weak solutions" may exist that solve the wave equation, but are not very differentiable. Hyperbolic PDEs tend to be time dependent, and solutions travel in characteristic directions at finite speeds. Solutions may be discontinuous.

# Non-linear PDEs:

Non-linear PDEs can also be classified into Elliptic, Parabolic, or Hyperbolic. However solution methodologies like superposition do not apply to non-linear PDEs.