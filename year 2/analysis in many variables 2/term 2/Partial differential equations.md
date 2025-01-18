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