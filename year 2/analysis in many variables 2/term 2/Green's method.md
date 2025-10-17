Green's method describes how to solve an inhomogeneous [[Eigenfunction methods#Boundary conditions|BVP]] of the form:$$\Huge Ly=f$$

# Form of the eigenfunction expansion:

A solution to the [[Eigenfunction methods#The operator|PDE model]] takes form:$$\Huge y(x)=\sum_{k=1}^\infty\frac{\langle f,w_k\rangle}{\lambda_k \langle y_k,w_k\rangle}y_k(x)$$when expanded across a range of eigenfunctions $y_k(x)$. We write $n_k=\langle y_k,w_k\rangle$, the normalisation constant, and get:$$\Huge\begin{align}
y(x)&=\sum_{k=1}^\infty\frac{1}{\lambda_kn_k}\int_a^bf(t)w_k(t)dt\,y_k(x)\\
&=\int_a^b\sum_{k=1}^\infty\frac{1}{\lambda_kn_k}w_k(t)y_k(x)\,f(t)\,dt\\
&=\int_a^bg(x,t)f(t)dt
\end{align}$$This $g(x,t)$ is known as the green's function. Note if $L=L^*$ (and therefore $w_k=y_k$) then we have $g(x,t)=g(t,x)$. In this case we call green's function symmetric. One can think of greens method as the continuous analogy of the eigenfunction expansion

## Inverse of a differential operator:
In linear algebra we have that $A\underline x=\underline b\implies\underline x=A^{-1}\underline b$. We have $Lx=f$ for a differential operator $L$. It is intuitive that the solution via green's function should therefore be an integral. Green's method describes how to "invert" a differential operator.

Take for example $Ly=-y''=f(x)$ for $0<x<1$ subject to Dirichlet boundary conditions  ($y(0)=y(1)=0$). This has corresponding greens function:$$\Huge g(x,\xi)=\begin{cases}(1-\xi)x&0<x<\xi\\(1-x)\xi&\xi<x<1\end{cases}$$which solves:$$\Huge y(x)=\int_0^1g(x,\xi)f(\xi)d\xi $$which can be shown via differentiation twice. To do this we use the Leibniz rule:$$\large \frac{d }{dx}\int_{a(x)}^{b(x)}f(x,\xi)d\xi=\int_{a(x)}^{b(x)}\frac{\partial f}{\partial x}(x,\xi)f(\xi)d\xi +\frac{db}{dx}(x)f(x,b)-\frac{da}{dx}(x)f(x,a)$$To get:$$\large\begin{align}
y(x)&=\int_0^1g(x,\xi)f(\xi)d\xi\\
&=\int_0^x(1-x)\xi f(\xi)d\xi+\int_x^1(1-\xi)xf(\xi)d\xi\\
\frac{dy}{dx}&=-\int_0^x\xi f(\xi)d\xi+(1-x)xf(x)+\int_x^1(1-\xi)f(\xi)d\xi-(1-x)xf(x)\\
&=-\int_0^x\xi f(\xi)d\xi+\int_x^1(1-\xi)f(\xi)d\xi\\
\frac{d^2y}{dx^2}&=-xf(x)-(1-x)f(x)=-f(x)
\end{align}$$So this indeed solves the differential equation. Note that it would be easier to differentiate $g(x,\xi)$ directly with:$$\Huge \frac{d y}{dx}=\int_0^1\frac{\partial g}{\partial x}(x,\xi)f(\xi)d\xi,\,\,\frac{d^2y}{dx^2}=\int_0^1\frac{\partial^2g}{\partial x^2}(x,\xi)f(\xi)d\xi$$however this would require a function $\delta(x,\xi)$ that satisfies:$$\Huge\int_0^1\delta(x,\xi)f(\xi)d\xi=-f(x)$$and $$\Huge \frac{\partial^2 g}{\partial x^2}=-\delta(x,\xi)$$This is known as green's equation. Greens function satisfies the following:
> If $x\neq\xi$ then $Lg=-\frac{\partial g}{\partial x^2}=0$
> Boundary conditions
> $g$ is continuous on $x\in[0,1]$
> $g$ is differentiable everywhere except $x=\xi$, where the derivative jumps from $1-\xi$ to $-\xi$. We are interested in the second derivative, which will be zero everywhere other than $x=\xi$. There exists no such function, however fuck that.

# Green's function via delta function:

We are looking for a function $\delta(x-a)$ such that $\delta(x-a)=0$ for all $x\neq a$. This must also satisfy:$$\Huge \int_{a_0}^{a_1}\delta(x-a)f(x)dx=f(a)\text{ if }a\in[a_0,a_1]$$There is no "classical" function that has these properties, however there are some cool approximations:

## Approximating the delta function:
Assume some sequence of functions $f_n(x)$ such that:$$\Huge \int_{a_0}^{a_1}f_n(x)dx=1\,\,\forall n>n_0:\lim_{n\to\infty}f_n(x)=0\,\,\forall x\neq0$$We propose that:$$\Huge f_n(x)=\begin{cases}0&|x|>1/n\\n/2&|x|\leq1/n\end{cases}$$This clearly satisfies the property that $f_n(x)=0$ everywhere except $x=0$ (in the limiting case).

## Properties of the delta function:
We require the delta function to satisfy:$$\Huge \int_{a_0}^{a_1}\delta(x)f(x)dx=\begin{cases}f(0)&0\in[a_0,a_1]\\0&\text{otherwise}\end{cases}$$Consider:$$\Huge \lim_{n\to\infty}\int_{a_0}^{a_1}f_n(x)f(x)dx$$with the function described above. This becomes:$$\Huge\begin{align}
\lim_{n\to\infty}\int_{a_0}^{a_1}f_n(x)f(x)dx&=\lim_{n\to\infty}\int_{-1/n}^{1/n}\frac{n}{2}f(x)dx\\
&=\lim_{n\to\infty}\frac{F(1/n)-F(-1/n)}{2/n}
\end{align}$$where $F(x)=\int_0^xf(s)ds$ is the antiderivative of $f$. Set $s=1/n$ and write:$$\Huge \lim_{n\to\infty}\frac{F(1/n)-F(-1/n)}{2/n}=\lim_{s\to0}\frac{F(s)-F(-s)}{2s}=F'(0)=f(0)$$using the fundamental theorem of calculus. We have shown that in the limiting case, $f_n(x)$ satisfies this "sifting" property.

## Point heat source:
Consider the heat conduction BVP with a point heat source of unit strength at the center of the rod:$$\Huge -y''(x)=\delta(x-1/2),\,\,0<x<1,\,\,y(0)=y(1)=0$$Now since $\delta(x-1/2)=0$ for $x\neq1/2$ we have:$$\Huge -y''(x)=0,\,\,0<x<1/2,\,\,1/2<x<1$$So we can derive conditions by integrating across $x=1/2$:$$\Huge\int_{1/2-}^{1/2+}-y''(x)dx=\int_{1/2-}^{1/2+}\delta(x-1/2)dx$$Then by the sifting property we see that this simplifies to:$$\Huge [-y'(x)]_{1/2-}^{1/2+}=1\implies y'(1/2+)-y'(1/2-)=-1$$Which defines a jump condition on $y'$. We also require that $y$ is continuous at $x=1/2$:$$\Huge [y]_{1/2-}^{1/2+}=0$$This implies the solution:$$\Huge y=\begin{cases}ax+b&0<x<1/2\\cx+d&1/2<x<1\end{cases}$$for constants $a,b,c,d$. We can then find these constants:$$\Huge\begin{align}
y(0)=0&\implies b=0\\
y(1)=0&\implies c=-d
\end{align}$$Then from the conditions at the jump we get:$$\Huge\begin{align}
a=1/2,\,\,c=-1/2
\end{align}$$Which makes the solution:$$\Huge y(x)=\begin{cases}x/2&0<x<1/2\\-x/2+1/2&1/2<x<1\end{cases}$$
## Arbitrary heat source via greens function:
Consider the heat conduction problem with an arbitrary source:$$\Huge -y''(x)=f(x),\,\,0<x<1,\,\,y(0)=y(1)=0$$In this case, we place the point source $f(\xi)\delta(x-\xi)$ at the arbitrary point $x=\xi$. We therefore consider the system:$$\Huge -g''(x,\xi)=\delta(x-\xi),\,\,0<x<1,\,\,g(0,\xi)=g(1,\xi)=0$$Then we have:$$\Huge y(x)=\int_0^1g(x,\xi)f(\xi)d\xi$$Now we solve for $g$, noting that $g''=0$ everywhere except $x=\xi$:$$\Huge g=\begin{cases}ax+b&0<x<\xi\\cx+d&\xi<x<1\end{cases}$$which imposes the jump and continuity conditions:$$\Huge [-y']_{\xi-}^{\xi+}=1,\,\,[y]_{\xi-}^{\xi+}=0$$Solving for constants gives the function:$$\Huge g(x,\xi)=\begin{cases}(1-\xi)x&0<x<\xi\\(1-x)\xi&\xi<x<1\end{cases}$$which is identical to the solution we saw previously. We can also show that:$$\Huge -y''=\int_0^1-g''(x,\xi)f(\xi)d\xi=\int_0^1\delta(x,\xi)f(\xi)=f(x)$$as required.

# General method:
The method for solving $Ly=f$ for second order operator $L$ with $x\in[a,b]$ then goes as follows:
> Solve $Lg=\delta(x-\xi)$ on $a<x<\xi$ and $\xi<x<b$, noting that it is a homogeneous problem everywhere other than $x=\xi$
> Apply jump condition $[g']_{\xi-}^{\xi+}=1$
> Apply continuity condition $[g]_{\xi-}^{\xi+}=0$

# General linear BVP:
Consider an $n$th order linear BVP with arbitrary continuous forcing function:$$\Huge Ly(x)=a_ny^{(n)}(x)+a_{n-1}y^{(n-1)}(x)+\dots+a_1y'(x)+a_0y(x)=f(x)$$for $a<x<b$ where each $a_i=a_i(x)$ is a continuous function and $a_n(x)\neq0$ for all $x$. There are $n$ boundary conditions, each a linear combination of $y$ and derivatives up to $y^{(n-1)}$ evaluated at $x=a,b$.

## General greens' function:
First we solve this equation with homogeneous boundary conditions $BC_iy=0$ for $i=1,\dots,n-1$. To do this we must solve:$$\Huge Lg(x,\xi)=\delta(x-\xi),\,\,B_ig=0,\,\,a<x<b$$As previous we split the domain across $\xi$ to get a homogeneous problem on two separate domains. This requires extra conditions that come from integrating $Lg(x,\xi)=\delta(x-\xi)$ across $x=\xi$:$$\Huge \int_{\xi-}^{\xi+}a_ng^{(n)}(x,\xi)+\dots+a_0g(x,\xi)dx=\int_{\xi-}^{\xi+}\delta(x-\xi)dx$$The RHS integral is clearly $1$, so performing integration by parts on the first LHS term gives:$$\Huge [a_n(x)g^{(n-1)}(x,\xi)]_{\xi-}^{\xi+}+\int_{\xi-}^{\xi+}(a_{n-1}-a_n')g^{(n-1)}+\dots+a_0g\,dx=1$$This is solved by setting the jump condition on the $n-1$th derivative:$$\Huge [g^{(n-1)}(x,\xi)]_{\xi-}^{\xi+}=\frac{1}{a_n(\xi)}$$and we take all lower derivatives to be continuous across this point $x=\xi$:$$\Huge [g^{(j)}(x,\xi)]_{\xi-}^{\xi+}=0,\,\,j=1,\dots,n-2$$This process determines the form of greens function, which is then used to give the solution:$$\Huge y(x)=\int_a^bg(x,\xi)f(\xi)d\xi $$
# Three dimensional greens functions:

## 2D Laplacian:
We aim to solve Poisson's equation in two dimensions:$$\Huge \underline{\nabla}^2u(\underline x)=f(\underline x)$$for $\underline x\in\Re^2$. This is known as the free space problem. To do this, we must solve greens problem in this domain:$$\Huge \underline{\nabla}^2g(\underline x,\underline \xi)=\delta(\underline x-\underline \xi)$$Making the change of coordinates to $\underline y=\underline x-\underline \xi$ (which we can do as derivatives are wrt to $x$) we have:$$\Huge \underline{\nabla}^2g(\underline y)=\delta(\underline y)$$We can then center this problem at the origin and adapt polar coordinates $(r,\theta)$. This then gives us:$$\Huge \underline{\nabla}^2g=\frac{1}{r}\frac{d}{dr}\left(r\frac{dg}{dr}\right)$$Away from the singularity at $r=0$ the homogeneous equation is:$$\Huge \frac{1}{r}\frac{d}{dr}\left(r\frac{dg}{dr}\right)=0$$Integrating once gives:$$\Huge r\frac{dg}{dr}=c_1\implies\frac{dg}{dr}=\frac{c_1}{r}$$And once more gives:$$\Huge g(r)=c_1\ln r+c_2$$We set $c_2=0$ because i want to, then we integrate over a disc of radius $\epsilon$ (equivalent to jump conditions) to determine the other constant:$$\Huge \oint_{\partial B_\epsilon}\underline{\nabla}g\cdot dS=\oint_{\partial B_\epsilon}\frac{c_1}{r}\hat r\cdot dS=2\pi c_1=1\implies c_1=\frac{1}{2\pi}$$Now substituting back $\underline y=\underline x-\underline \xi$ and using the fact that $r=|\underline y|$ we have:$$\Huge g(\underline x,\underline \xi)=\frac{1}{2\pi}\ln|\underline x-\underline \xi|$$Which gives the full solution:$$\Huge u(\underline x)=\int_{\Re^2}g(\underline x,\underline \xi)f(\underline \xi)dV$$