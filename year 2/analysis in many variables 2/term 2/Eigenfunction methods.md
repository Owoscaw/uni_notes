
Consider PDEs of the form:$$\Huge \frac{\partial u}{\partial t}=Lu+h(x,t)$$Where $L$ is some [[Differential operators|differential operator]] in $x$. We consider $u(x,t)$ to be a one dimensional scalar model on a domain $x\in[a,b]$ and $t>0$.

We have many degrees of freedom in this model:

## The operator:
One such is the operator $L$. The differential operator $L$ must satisfy linearity. That is $L(u_1+u_2)=L(u_1)+L(u_2)$, implying the [[Partial differential equations#Linear equations and superposition|principle of superposition]].

## Source term:
Another parameter is the "source" term given by $h(x,t)$. This has no $u$ dependence and provides some external change in $\frac{\partial u}{\partial t}$. If $h(x,t)=0$, the problem is called homogenous, if it is non-zero the problem is called inhomogeneous. If $u_h$ solves $h(x,t)=0$ and $u_{ih}$ solves $h(x,t)\neq0$ then $u=u_h+u_{ih}$ solves the problem.

## Boundary conditions:
Boundary conditions (BC) are also required. If $L$ is an $n$th order operator, then $n$ BCs are also required. We denote each boundary condition as a linear operator:$$\Huge BC_i([u,a,b])=0$$For example, we could denote a BC as follows:$$\Huge BC_1([u,a,b])=\frac{\partial u}{\partial x}\vert_{x=a}=0$$A homogenous BC requires $u$ or its derivatives to be $0$ on the boundary. An inhomogeneous BC required $u$ or its derivatives to be some other value at the boundary.

## Initial conditions:
Finally, the problem requires a start point called the initial condition. That is, $u(x,0)$ is given by some function:$$\Huge u(x,0)=g(x)$$
# Solution:

We make the following assumptions that are justified later:
> Our solution can be written in separable form:$$\Huge u(x,t)=\sum_{n=0}^\infty c_n(t)y_n(x),\,\,h(x,t)=\sum_{n=0}^\infty h_n(t)y_n(x)$$Which makes the model:$$\Huge \sum_{n=0}^\infty\frac{dc_n}{dt}y_n(x)=\sum_{n=0}^\infty c_n(t)Ly_n(x)+\sum_{n=0}^\infty h_n(t)y_n(x)$$
> The functions $y_n(x)$ satisfy:$$\Huge Ly_n(x)=-\lambda_ny_n(x)$$Where $L$ is acting as a spatial operator only. This allows the sums to be written in the form:$$\Huge \sum_{n=0}^\infty\left(\frac{d c_n}{dt}+\lambda_nc_n(t)-h_n(t)\right)y_n(x)=0$$
> Each $y_n(x)$ are linearly independent, the sum can only be zero when each individual term is zero

So for each $n$ we require that:$$\Huge\frac{d c_n(t)}{dt}+\lambda_nc_n(t)-h_n(t)=0$$Which can always be solved for $c_n(t)$, as $h_n(t)$ is always known. We solve this using the [[First order differential equations#Test for exactness|integrating factor]] method to get the solution:$$\Huge c_n(t)=e^{-\lambda_nt}\left(a_n+\int_1^te^{\lambda_nt'}h_n(t')dt'\right)$$The homogenous solution is given by the term with constants $a_n$, while the inhomogeneous solution is given by the integral term. To determine the constants of integration $a_n$ we must use the initial condition:$$\Huge u(x,0)=\sum_{n=0}^\infty c_n(0)y_n(x)=g(x)$$Now since the boundary conditions were linear we have:$$\Huge BC_iu=\sum_{n=0}^\infty c_n(t)BC_iy_n(x)=0\implies BC_iy_n(x)=0$$This is because the boundary conditions act only on the spatial variables. So in order to fully solve the equation, one must solve the eigenvalue equation:$$\Huge Ly_n=-\lambda_ny_n,\,\,BC_iy_n=0$$

# Example via Fourier series:

Taking:$$\Huge L=\frac{\partial^2 }{\partial x^2},\,\,BC_1=\frac{\partial }{\partial x}\vert_{x=a}=0,\,\,BC_2=\frac{\partial }{\partial x}\vert_{x=b}=0$$This must solve:$$\Huge \frac{d^2y_n}{dx^2}=-\lambda_n y_n,\,\,\frac{d y_n}{dx}\vert_{x=a}=\frac{d y_n}{dx}\vert_{x=b}=0$$A specific solution to this is given by:$$\Huge y_n(x)=a_n\cos\left(\frac{n\pi(x-a)}{b-a}\right),\,\,\lambda_n=\frac{n^2\pi^2}{(b-a)^2}$$For arbitrary $n\in\mathbb{N}$. The argument above states that the solution to:$$\Huge \frac{\partial u}{\partial t}=\frac{d^2u}{dx^2}+h(x,t)$$Is given by:$$\Huge u(x,t)=\sum_{n=0}^\infty c_n(t)\cos\left(\frac{n\pi(x-a)}{b-a}\right)$$Note that for fixed $t$ this is simply a [[Fourier Series]]. This motivates us to represent the forcing function, $h(x,t)$, as the following:$$\Huge h(x,t)=\sum_{n=0}^\infty h_n(t)\cos\left(\frac{n\pi(x-a)}{b-a}\right)$$With:$$\Huge h_n(t)=\frac{l}{b-a}\int_a^bh(x,t)\cos\left(\frac{n\pi(x-a)}{b-a}\right)dx$$With $l=2$ for $n\neq0$ and $l=1$ for $n=0$. We can also do the same for initial conditions:$$\Huge g(x)=\sum_{n=0}^\infty c_n(0)\cos\left(\frac{n\pi(x-a)}{b-a}\right)$$With:$$\Huge c_n(0)=\frac{l}{b-a}\int_a^bg(x)\cos\left(\frac{n\pi(x-a)}{b-a}\right)dx$$However this requires $h(x,t)$ to be composed of a series of cosines and be subject to the same boundary conditions as $u(x,t)$. Taking $a=0,b=1$ and:$$\Huge h(x,t)=\sin(\omega t)\cos(3\pi x),\,\,g(x)=x-1/2$$Therefore all $h_n(t)=0$ except for $h_3(t)$. Then the coefficients of the solution at $t=0$ are given by:$$\Huge c_n(x,0)=2\int _0^1(x-1/2)\cos(n\pi x)dx=\frac{2(\cos(n\pi)-1)}{n^2\pi^2}$$For $n>0$ and $c_0(x,0)=0$. If $n=3$ we see:$$\large\begin{align}
c_3(t)&=e^{-\lambda_3t}\left(a_n+\int _1^te^{\lambda_3t'}\sin(\omega t')dt'\right)\\
&=e^{-\lambda_3t}\left(a_n+\left[e^{\lambda_3t}\frac{\lambda_3\sin(\omega t)-\omega\cos(\omega t)}{\omega^2+\lambda_3^2}\right]_1^t\right)\\
&=e^{-\lambda_3t}\left(a_n+\frac{e^{\lambda_3t}(\omega\cos(\omega)-\lambda_3\sin(\omega))+e^{\lambda_3t}(\lambda_3\sin(\omega t)-\omega\cos(\omega t))}{\omega^2+\lambda_3^2}\right)
\end{align}$$Where $a_n$ is set by the initial condition $c_3(0)$. When $t$ is large the exponential terms decay and we are left with:$$\Huge c_3(t)\approx\frac{\omega\cos\omega-\lambda_3\sin\omega+\lambda_3\sin(\omega t)-\omega\cos(\omega t)}{\omega^2+\lambda_3^2}$$So we see for large $t$, the effect of the choice of $h(x,t)$ dominates and the initial condition has no impact. This relied on the orthogonality of the Fourier series, which ensures linear independence of the series representation.

# Analysis of the eigenvalue problem:

We now focus on the solutions to:$$\Huge Ly_n=\lambda_ny_n$$We aim to show that the solutions form an orthogonal basis and find a coefficient formula for general $L$.

## Function spaces:
Consider the space of all well behaved functions on $a\leq x\leq b$. We define the inner product on this space for functions $u(x),v(x)$:$$\Huge \langle u,v\rangle=\int_a^bu(x)\overline{v(x)}dx$$The norm of a function is then $||u||=\sqrt{\langle u,u\rangle}$.

## Weighting functions:
Sometimes the inner product definition includes a real, positive, weighting function defined as:$$\Huge \langle u,v\rangle=\int_a^b p(x)u(x)\overline{v(x)}dx$$Which corresponds to the eigenvalue problem:$$\Huge Ly_i(x)=\lambda_ip(x)y_i(x)$$
## Adjoint operators:
The [[Determinants and Adjoints#Adjoints|adjoint]] matrix $A^*$ of a matrix $A$ is defined by:$$\Huge (Au)\cdot v=u\cdot(A^*v)\text{ or }A^{-1}=\frac{1}{\det A}A^*$$Where $\underline x=A^{-1}\underline v$ is the solution to $A\underline x=\underline v$. We can extend this notion to function spaces by defining the adjoint operator:$$\Huge \langle Ly,w\rangle=\langle y,L^*w\rangle$$for functions $y,w$ defined on $x\in[a,b]$.

Take for example $Ly=\frac{d^2y}{dx^2},y(a)=0,y'(b)-3y(b)=0$. We then aim to find a function $L^*w$ and boundary conditions such that:$$\Huge\int_a^bwy''dx=\int_a^byL^*wdx$$Which we can solve through integration by parts:$$\Huge\begin{align}
\int_a^bwy''dx&=[wy']_a^b-\int_a^bw'y'dx\\
&=[wy'-w'y]_a^b+\int_a^bw''ydx\\
&=[wy'-w'y]_a^b+\langle y,L^*w\rangle
\end{align}$$Where we have $L^*=\frac{d^2}{dx^2}$. To ensure that this remains an adjoint, we require that the boundary terms vanish. That is, $[wy'-w'y']_a^b=0$:$$\Huge\begin{align}
[wy'-w'y']_a^b&=w(b)y'(b)-w'(b)y(b)-w(a)y'(a)+w'(a)y(a)\\
&=y(b)(3w(b)-w'(b))-w(a)y'(a)+w'(a)\cdot0\\
&=y(b)(3w(b)-w'(b))-w(a)y'(a)
\end{align}$$These terms must vanish for all $y(b),y'(a)$ so we can infer the following conditions on $w$:
>$3w(b)-w'(b)=0$
>$w(a)=0$

This together with $L^*=\frac{d^2}{dx^2}=L$ forms the solution.

Note that if $L=L^*$ and $BC=BC^*$ the problem is self adjoint. If $BC\neq BC^*$, the operator can still be called self adjoint.

# Eigenfunction properties:

Eigenfunctions of the adjoint problem have the same eigenvalues to the original problem, that is:$$\Huge Ly=\lambda y\implies\exists w:L^*w=\lambda w$$This simply follows from the definition:$$\Huge \langle Ly,w\rangle=\lambda \langle y,w\rangle=\langle y,L^*w\rangle=\langle y,\lambda w\rangle\implies Lw=\lambda w$$

We propose that eigenfunctions corresponding to different eigenvalues are orthogonal. That is if $Ly_j=\lambda_jy_j$ and $Ly_k=\lambda_ky_k$ then for $\lambda_j\neq\lambda_k$ we have $\langle y_j,w_k\rangle=0$:$$\Huge\begin{align}
\lambda_j \langle y_j,w_k\rangle&=\langle \lambda_jy_j,w_k\rangle\\
&=\langle Ly_j,w_k\rangle\\
&=\langle y_j,L^*w_k\rangle\\
&=\langle y_j,\lambda_kw_k\rangle\\
&=\lambda_k\langle y_j,w_k\rangle
\end{align}$$However $\lambda_j\neq\lambda_k$ so we must have $\langle y_j,w_k\rangle=0$ as required.

## Inhomogeneous problems in terms of an operator:
We aim to construct a solution to the following Boundary Value Problem (BVP):$$\Huge Lu=f(x),\,\,BC_i[u]=0$$with linear, homogeneous, separated boundary conditions represented by the second condition. Consider $h(x,t)$ and the assumed decomposition using the eigenfunction:$$\Huge\begin{align}
\sum_{n=0}^\infty h_n(t)y_n(x)&=h(x,t)\\
\sum_{n=0}^\infty h_n(t)\frac{Ly_n(x)}{\lambda_n}&=h(x,t)\\
L\sum_{n=0}^\infty h_n(t)\frac{y_n(x)}{\lambda_n}&=h(x,t)\\
\implies u=\sum_{n=0}^\infty h_n(t)\frac{y_n(x)}{\lambda_n}&,\,\,f=h(x,t)
\end{align}$$Which is solved by the eigenvalue problem:$$\Huge Lu=f$$Note that this can be problematic if some $\lambda_n=0$. To solve this eigenvalue problem we use the following steps:
> Solve the eigenvalue problem $Ly=\lambda y$ with $BC_1(a)=0,BC_2(b)=0$
> Solve the adjoint problem $L^*w=\lambda w$ with $BC_1^*(a)=0,BC_2^*(b)=0$
> Assume a solution in the form:$$\Huge y=\sum_{n=0}^\infty c_ny_n(x)$$To determine the constants $c_n$ we apply the inner product to $Ly=f$:$$\Huge\begin{align}
Ly&=f(x)\\
\implies\langle Ly,w_k\rangle&=\langle f,w_k\rangle\\
\langle y,L^*w_k\rangle&=\langle f,w_k\rangle\\
\langle y,\lambda_kw_k\rangle&=\langle f,w_k\rangle\\
\implies\lambda_k \langle \sum c_ny_n,w_k\rangle&=\langle f,w_k\rangle \\
\lambda_kc_k \langle y_k,w_k\rangle&=\langle f,w_k\rangle\\
\implies c_k&=\frac{\langle f,w_k\rangle}{\lambda_k \langle y_k,w_k\rangle}
\end{align}$$Where we have used the assumed series solution and the orthogonality of $y_n,w_k$. 

Note that if the problem is fully self adjoint then $w_k=y_k$ and we have:$$\Huge \lambda_kc_k \langle y_k,y_k\rangle=\langle f,y_k\rangle$$In some sense, this generalises the Fourier series for any operator $L$.

# Simple solutions:

Take for example the second order constant coefficient differential equation:$$\Huge Ly=ay''+by'+cy=\lambda y$$We try $y=e^{mx}$, which reduces the equation to:$$\Huge am^2+bm+(c-\lambda)=0$$Which has solutions $m_+,m_-$. This implies that the solution takes form:$$\Huge y=A_1e^{m_+x}+A_2e^{m_-x}$$Then $BC_1$ relates $A_1,A_2$ and $BC_2$ can be used to determine a formula for $\lambda$. We can also normalise $\langle y,y\rangle=1$ to determine specific $A_1,A_2$.

## Cauchy-Euler:
Take the Cauchy-Euler equation defined as:$$\Huge Ly=ax^2y''+bxy'+cy=\lambda y$$We try $y=x^m$ which reduces the equation to:$$\Huge am(m-1)+bm+(c-\lambda)=0$$Which has solutions $m_+,m_-$. This implies that the solution takes form:$$\Huge y=A_1x^{m_+x}+A_2x^{m_-x}$$Then the same steps are taken to determine $A_1,A_2,\lambda$.

# Inhomogeneous boundary conditions:

Consider the following:$$\Huge Lu=f,\,\,B_1u=\gamma_1,\,\,B_2u=\gamma_2$$This makes the derivation of $L^*$ and adjoint boundary conditions not-so straightforward. To deal with this we can decompose the problem:$$\Huge Lu_1=f(x),\,\,B_1u_1=0,\,\,B_2u_1=0$$And:$$\Huge Lu_2=0,\,\,B_1u_2=\gamma_1,\,\,B_2u_2=\gamma_2$$Then by linearity we have $u=u_1+u_2$. Previous methods then apply to each problem.

## Incorporated method:
Another method to solving these types of problems is the incorporated method. When using the adjoint identity:$$\Huge \langle Ly,w\rangle=\langle y,L^*w\rangle+[BC_i^*]_a^b$$we do not require each $BC_i$ evaluated at the boundary to vanish.

Take for example $y''=f(x)$ with $0\leq x\leq 1$ and $y(0)=\alpha,y(1)=\beta$. The method then follows:
> Solve the eigenproblem $y''=\lambda y$ with $y(0)=0$ and $y(1)=0$. This has solution $y_k(x)=\sin(k\pi x)$ with $\lambda_k=-k^2\pi^2$.
> Follow the method for determining coefficients:$$\Huge\begin{align}
y''&=f(x)\\
\implies\int_0^1w_ky''\,dx&=\int_0^1w_kf\,dx\\
[y'w_k-yw_k']_0^1+\int_0^1w_k''y\,dx&=\int_0^1w_kf\,dx\\
[y'w_k-yw_k']_0^1+\lambda_k\int_0^1w_ky\,dx&=\int_0^1w_kf\,dx\\
[y'w_k-yw_k']_0^1-k^2\pi^2c_k\int_0^1\sin^2(k\pi x)\,dx&=\int_0^1w_kf\,dx
\end{align}$$Where we have used the assumed series solution and the fact that this problem is self adjoint ($y_k=w_k$). Now we have that $\int_0^1\sin^2(k\pi x)dx=1/2$. This reduces the equation to:$$\large
\begin{align}[y'w_k-yw_k']_0^1&=-k\pi\cos(k\pi)y(1)+k\pi\cos(0)y(0)\\
\implies-\beta k\pi(-1)^k+\alpha k\pi-\frac{1}{2}k^2\pi^2c_k&=\int_0^1f(x)\sin(k\pi x)dx
\end{align}$$If $f(x)$ is known we can then solve for $c_k$, giving the solution in terms of a series.

# Linear algebra connection:

The [[Vector Product|dot product]] is analogous to our notion of inner product between functions, as well as the norm. The same is true for orthogonal vectors and orthogonal functions as well as the eigenvalue problem given by $A\underline v=\lambda\underline v$ and the eigenfunction product given by $Ly=\lambda y$. In the latter case, the matrix $A$ is analogous to the differential operator $L$.

In linear algebra, a matrix of size $n\times n$ has at most $n$ complex eigenvalues, whereas if the differential operator $L$ is order $n$, there are still infinite eigenvalues.

# Sturm-Liouville theory:

The Sturm-Liouville theory of second order concerns weighted boundary value problems of the form:$$\Huge Ly=\lambda r(x)y$$Where $r(x)\geq0$ and $L$ is of the form:$$\Huge Ly=-\frac{d }{dx}\left(p(x)\frac{d y}{dx}\right)+q(x)y,\,\,a\leq x\leq b$$The functions $p,q,r$ are assumed to have real values. One can show that $L$ is self adjoint, the problem is fully self adjoint if the boundary conditions take form:$$\Huge\begin{align}
\alpha_1y(a)+\alpha_2y'(a)&=0\\
\alpha_3 y(b)+\alpha_2y'(b)&=0
\end{align}$$Note that the definition of the inner product with a weighting function is slightly different:$$\Huge \langle y,w\rangle=\int_a^br(x)yw\,dx$$