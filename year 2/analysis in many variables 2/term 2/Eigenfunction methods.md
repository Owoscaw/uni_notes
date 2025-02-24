
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

The Sturm-Liouville (SL) theory of second order concerns weighted boundary value problems of the form:$$\Huge Ly=\lambda r(x)y$$Where $r(x)\geq0$ and $L$ is of the form:$$\Huge Ly=-\frac{d }{dx}\left(p(x)\frac{d y}{dx}\right)+q(x)y,\,\,a\leq x\leq b$$The functions $p,q,r$ are assumed to have real values. One can show that $L$ is self adjoint, the problem is fully self adjoint if the boundary conditions take form:$$\Huge\begin{align}
\alpha_1y(a)+\alpha_2y'(a)&=0\\
\alpha_3 y(b)+\alpha_2y'(b)&=0
\end{align}$$Note that the definition of the inner product with a weighting function is slightly different:$$\Huge \langle y,w\rangle=\int_a^br(x)yw\,dx$$
## Inhomogeneous SL problems:
Since the SL operator is self adjoint, the eigenfunction expansion is straightforward:$$\Huge\begin{align}
Ly&=f(x)\\
\langle Ly,y_k\rangle&=\langle f,y_k\rangle\\
\langle y,Ly_k\rangle&=\langle f,y_k\rangle\\
\implies \langle y,\lambda_kry_k\rangle&=\langle f,y_k\rangle\\
\implies\lambda_kc_k \langle y_k,ry_k\rangle&=\langle f,y_k\rangle
\end{align}$$where we have assumed a series solution in the last implication. This solution has associated coefficient formula:$$\Huge y(x)=\sum_{k=0}^\infty c_ky_k(x),\,\,c_k=\frac{\langle f,y_k\rangle}{\lambda_k \langle y_k,ry_k\rangle }$$
## Transforming an operator to SL form:
Assume we have the operator:$$\Huge Ly=a_2(x)y''(x)+a_1(x)y'(x)+a_0(x)y(x)$$If $a_2(x)\neq0$ it is possible to convert $L$ to SL form. To do this, we use the integrating factor method:$$\Huge \mu a_2y''+\mu a_1y'+\mu a_0y\rightarrow-\frac{d }{dx}(p'y)+qy$$---

Now we have:$$\Huge \hat Ly=-\frac{d }{dx}(py')+qy$$and we are solving the eigenfunction problem:$$\Huge \hat Ly=\mu f$$
## SL properties:
> Orthogonality:$$\Huge \int_a^by_k(x)y_j(x)r(x)dx=0$$
> Eigenvalues are real, as $p,q,r$ are real. We can use $L=\bar L$ with $Ly_K=\lambda_ky_k$ to show this:$$\Huge\begin{align}
L\bar y_k&=\bar\lambda_k\bar y_k\\
\langle y_k,L\bar y_k\rangle&=\bar\lambda_k \langle y_k,r\bar y_k\rangle\\
&=\langle Ly_k,\bar y_k\rangle\\
&=\lambda_k \langle ry_k,\bar y_k\rangle\\
&=\lambda_k \langle y_k,r\bar y_k\rangle\\
\implies\lambda_k&=\bar\lambda_k
\end{align}$$So each $\lambda_k$ is real. Moreover if $0\leq x\leq b$ is finite, then the eigenvalues are discrete and countable with $\lim_{k\to\infty}\lambda_k=\infty$.
>Eigenfunctions are complete, that is the $\{y_k\}$ form a complete set. For any $f(x)$ with $\int_\Re f^2r\,dx<\infty$ (square integrable functions) we can write $f(x)=\sum_{n=0}^\infty c_ny_n(x)$. We take the inner product with $r(x)y_k(x)$:$$\Huge\begin{align}
\langle ry_k,f\rangle&=\langle ry_k,\sum c_jy_j\rangle\\
&=\sum c_k \langle ry_k,y_j\rangle\\
&=c_j \langle ry_j,y_j\rangle
\end{align}$$by orthogonality. This set of functions $y_k$ can represent the $h(x,t)$ in the PDE model.

## Regular SL problems:
Assume:
>$p(x),r(x)>0$ on $a\leq x\leq b$
>$q(x)\geq0$
>BCs have $\alpha_1\alpha_2\leq0,\alpha_3\alpha_4\geq0$

We can then show that $\lambda_k\geq0$ using the fact that $\langle y_k,Ly_k-\lambda_kry_k\rangle=0$:$$\Huge\begin{align}
\langle y_k,Ly_k-\lambda_kry_k\rangle&=-\int_a^by(py')'dx+\int_a^byqydx-\int_a^by\lambda rydx\\
&=\int_a^by(py')'dx+\int_a^bqy^2dx-\lambda\int_a^bry^2dx\\
&=[-pyy']_a^b+\int_a^bp(y')^2dx+\int_a^bqy^2dx-\lambda\int_a^bry^2dx\\
&=0\\
\implies\lambda&=\frac{\left[\int_a^bp(y')^2+qy^2dx-[pyy']_a^b\right]}{\int_a^bry^2dx}\geq0
\end{align}$$This shows that without a forcing function $h(x,t)$ we have $c_n(t)=e^{-\lambda_nt}$ then since $\lambda\geq0$ we see that each mode exponentially decays with time.

# Fredholm alternative:

The Fredholm alternative holds that either the homogenous adjoint problem $L^*w=0$ has a non-trivial solution, or the inhomogeneous boundary value problem $Ly=f(x)$ with relevant boundary conditions has a unique solution.

If we have a non-trivial solution to $L^*w=0$, then either $\langle w,f\rangle=0$ and there is a non-unique solution to the problem $Ly=f$ with relevant boundary conditions. Or, this integral does not vanish and there is no solution to the problem $Ly=f(x)$ with relevant boundary conditions.

Consider the adjoint identity $\langle Lu,w\rangle= \langle u,L^*w\rangle$. If $L^*w=0$ then $\langle Lu,w\rangle=0$. If $w$ is non-trivial, this implies that $Lu=0$, in which case it is impossible to solve $Lu=f(x)$ for non-trivial $f$. However if $\langle Lu,w\rangle=\langle f(x),w\rangle=0$ for some non-trivial $w$ then $Lu$ is not necessarily zero. This implies the condition $\langle w,f\rangle=0$ up to a constant.

However if $w$ were originally trivial then there is no constraint on $Lu$, since $\langle Lu,0\rangle=0$ for any $Lu$, which does not determine if $Lu=f(x)$ can be solved.

Take for example the inhomogeneous BVP:$$\Huge \frac{d^2y}{dx^2}+g_0^2y=\sin(x)$$with constant $g_0$ and boundary conditions $y(x)=y(\pi)=0$. This is a fully self adjoint problem, so we proceed to solve the homogeneous problem $L^*w=0$:$$\Huge \frac{d^2w}{dx^2}+g_0^2w=0,\,\,w(0)=w(\pi)=0$$for $g_0>0$, the general solution is:$$\Huge w(x)=A\sin(g_0x)+B\cos(g_0x)$$the boundary condition $w(0)=0$ implies that $B=0$. The second condition requires either $A=0$ or $g_0\in\mathbb{Z}_0$. So assume that $g_0$ is indeed an integer, now we must consider the alternative:$$\Huge \langle w,\sin(x)\rangle=\int_0^\pi\sin(g_0x)\sin(x)dx=\frac{\sin(g_0\pi)}{g_0^2-1}$$so if $g_0\neq\pm1$ then this is zero, implying that the problem can be solved. If $g_0=1$ we see that the integral is not zero, implying that the problem cannot be solved. To test this, we aim to find the general solution. The complementary function that solve the homogeneous problem is given by the above. For the particular solution we seek a function of the form:$$\Huge y_p(x)=a_1\sin(x)+a_2\cos(x)$$this gives:$$\Huge (a_1(g_0^2-1)-1)\sin(x)+a_2(g_0^2-1)\cos(x)=0$$if $g_0\neq1$ then we can set $a_2=0$ and $a_1=1/(g_0^2-1)$ which gives the full solution:$$\Huge y(x)=A\sin(g_0x)+B\cos(g_0x)+\frac{1}{g_0^2-1}\sin(x)$$Therefore we have a unique solution when $g_0\notin\mathbb{Z}$ and non-unique when it is, due to the freedom of $A,B$.

If $g_0=1$ then it is clear that the condition on $a_1,a_2$ cannot be satisfied. In this case we try:$$\Huge y_p=a_1x\sin(x)+a_2x\cos(x)$$which gives:$$\Huge 2a_1\cos(x)-(2a_2+1)\sin(x)=0$$so we require $a_1=0$ and $a_2=-\frac{1}{2}$, making the general solution:$$\Huge y(x)=A\sin(x)+B\cos(x)-\frac{1}{2}x\cos(x)$$however!! this does not satisfy boundary conditions, so the Fredholm alternative still holds.

# Extended coefficient formula:

Earlier we saw the general coefficient formula:$$\Huge \lambda_kc_k \langle y_k,w_k\rangle=\langle f,w_k\rangle$$Now we consider the issue arising from $\lambda_k=\lambda_0=0$ in the context of the Fredholm alternative. If $w_0=0$ then there is no problem, however if $w_0\neq0$ and $\langle f,w_k\rangle=0$ then there is non-uniqueness of the coefficients, leading to a non-unique solution.

# Extended model:

Recall the parabolic time-dependent model:$$\Huge \frac{\partial u}{\partial t}=Lu+h(x,t)$$We have seen how to solve equations in the form $Ly+f=0$ which has a series solution:$$\Huge u(x)=\sum_{n=0}^\infty c_ny_n(x)$$
## Time dependence:
We now extend this to include time-dependence:$$\Huge u(x,t)=\sum_{n=0}^\infty c_n(t)y_n(x)$$Note that the same $y_n(x)$ are present. The same eigen-expansion method can then be used for both time-independent and time-dependent cases. For the time dependent case we have:$$\Huge \frac{d c_n(t)}{dt}+\lambda_nc_n(t)-h_n(t)=0$$with:$$\Huge h_n(t)\langle y_n,w_n\rangle=\langle h(x,t),w_n\rangle$$Note that the inner product only integrates over $x$, however the value will change dependent on $t$.

Take for example the problem defined by:$$\Huge \frac{\partial^2y}{\partial t^2}=Ly+h(x,t),\,\,u(x,0)=g_1(x),\,\,\frac{\partial u}{\partial t}\vert_{t=0}=g_2(x)$$Note the extra initial condition. Now we follow the same steps:
>Assume a series solution:$$\Huge u(x,t)=\sum_{n=0}^\infty c_n(t)y_n(x),\,\,Ly_n=-\lambda_ny_n$$
>Substitute into equation and decompose:$$\Huge h(x,t)=\sum_{n=0}^\infty h_n(t)y_n(x)$$
>Solve the coefficient formula:$$\Huge \frac{d^2c_n}{dt^2}+\lambda_nc_n-h_n=0$$

In this case, the homogenous part takes form:$$\Huge c_{nh}(t)=a_{1n}\sin(t\sqrt{\lambda_n})+a_{2n}\cos(t\sqrt{\lambda_n})$$If $\lambda>0$ with constants $a_{1n}$ and $a_{2n}$ defined by initial conditions, the inhomogeneous solution can be found.

More generally we can consider the linear operator to be time dependent, which gives the following equation:$$\Huge L_tc_n+\lambda c_n-h_n(t)=0$$or, writing $L^+=L-\lambda$:$$\Huge L^+c_n=h_n(t)$$

## Higher order spatial operators:
Consider the model:$$\Huge \frac{\partial u}{\partial t}=Lu+h(\underline x,t)$$where $u(\underline x,t)$ depends on some $m$-dimensional vector $\underline x\in\Re^m$, and for $t>0$ the operator $L:\Re^m\rightarrow\Re^m$ is an $m$-dimensional spatial operator. The solution then takes form:$$\Huge u(\underline x,t)=\sum_{\underline n\in\mathbb{N}^m}c_{\underline n}(t)y_{\underline n}(\underline x)$$where each $y_n$ satisfy:$$\Huge Ly_{\underline n}(\underline x)=-\lambda y_{\underline n}(\underline x)$$This requires the inner product to be defined as:$$\Huge \langle u(\underline x),v(\underline x)\rangle=\int_Du(\underline x)\overline{v(\underline x)}dV$$where $D\in\Re^n$ is an $n$-dimensional domain, and $dV$ is the volume element.

## Solving higher dimensional problems on box-domains:
Consider $D=[0,L_1]\times[0,L_2]\times\dots\times[0,L_m]$. Then recall the heat kernel:$$\Huge L=\nabla^2\implies\nabla^2u=\frac{\partial^2u}{\partial x_1^2}+\frac{\partial^2u}{\partial x_2^2}+\dots+\frac{\partial^2u}{\partial x_m^2}$$We can impose Dirichlet boundary conditions on such problem, that is:$$\large\begin{align}
u(L_1,x_2,\dots,x_m)=u(x_1,L_2,x_3,\dots,x_m)=\dots=u(x_1,x_2,\dots,L_m)=0
\end{align}$$then the solution to:$$\Huge \frac{\partial^2u}{\partial x_1^2}+\frac{\partial^2u}{\partial x_2^2}+\dots+\frac{\partial^2u}{\partial x_m^2}=-\lambda_nu$$is given by:$$\Huge y_n=C_{n_1,n_2,\dots n_m}\prod_{k=1}^m\sin\left(\frac{n_k\pi x_k}{L_k}\right)$$for $n_i\in\mathbb{Z}$ and eigenvalues given by:$$\Huge \lambda_{\underline n}=\pi^2\left(\frac{n_1^2}{L_1^2}+\dots+\frac{n_m^2}{L_m^2}\right)$$
## Disc domains:
Consider the Laplacian eigen-problem in polar coordinates $(r,\theta)$:$$\Huge \nabla^2y_n+\lambda_ny_n=\frac{1}{r}\frac{\partial }{\partial r}\left(r\frac{\partial w_k}{\partial r}\right)+\frac{1}{r^2}\frac{\partial^2w_k}{\partial \theta^2}+\lambda_ny_n=0$$We then impose Neumann boundary conditions $\nabla y_n\cdot\underline{\hat{n}}=0$. The domain is then defined as a radius of $R$, that is $r\in[0,R]$ and $\theta\in[0,2\pi]$. The solution is found by separation of variables, $y_n(r,\theta)=R(r)P(\theta)$. Substituting this in we get:$$ \frac{1}{r}\frac{\partial }{\partial r}\left(r\frac{\partial (RP)}{\partial r}\right)+\frac{1}{r^2}\frac{\partial^2(RP)}{\partial \theta^2}+\lambda_nRP=P\frac{1}{r}\frac{d}{dr}\left(r\frac{dR}{dr}\right)+R\frac{1}{r^2}\frac{d^2P}{d\theta^2}+\lambda_nRP=0$$We then multiply by $r^2/RP$ to get:$$\large \frac{r}{R}\frac{\partial }{\partial r}\left(r\frac{dR}{dr}\right)+\frac{1}{P}\frac{\partial^2P}{\partial \theta^2}+\lambda_nr^2=0\implies\frac{r}{R}\frac{d}{dr}\left(r\frac{dR}{dr}\right)+\lambda_nr^2=-\frac{1}{P}\frac{d^2P}{d\theta^2}=C_\theta$$This is true as the $r$ dependence and the $\theta$ dependence have been separated, so each side is constant:$$\Huge \frac{1}{Rr}\frac{d}{dr}\left(r\frac{dR}{dr}\right)=\lambda_n-\frac{C_\theta}{r^2},\,\,-\frac{1}{P}\frac{d^2P}{d\theta^2}=C_\theta$$And we have boundary conditions:$$\Huge R(L_r)=0,\,\,P(0)=P(2\pi),\,\,\frac{dP}{d\theta}(0)=\frac{dP}{d\theta}(2\pi)$$We can now solve for the $R,P$ modes.

### P modes:
It is clear the the $P$ mode only has sinusoidal solutions, so we write:$$\Huge P(\theta)=A\cos(\theta\sqrt{C_\theta})+B\sin(\theta\sqrt{C_\theta})$$The first boundary condition implies:$$\Huge A\cos(0)+B\sin(0)=A=A\cos(2\pi \sqrt{C_\theta})+B\sin(2\pi\sqrt{C_\theta})$$which imposes the condition that $\sqrt{C_\theta}\in\mathbb{Z}$. The second boundary condition implies:$$ -A\sqrt{C_\theta}\sin(0)+B\sqrt{C_\theta}\cos(0)=B\sqrt{C_\theta}=A\sqrt{C_\theta}\sin(2\pi\sqrt{C_\theta})+B\sqrt{C_\theta}\cos(2\pi\sqrt{C_\theta})$$which again requires $\sqrt{C_\theta}\in\mathbb{Z}$. Then the solution for $P$ is given by:$$\Huge P(\theta)=A\cos(n\theta)+B\sin(n\theta),\,\,n\in\mathbb{Z}_0$$
### R modes:
The equation for $R$ is given by:$$\Huge r^2\frac{d^2R}{dr^2}+r\frac{dR}{dr}+(\lambda_nr^2-l^2)R=0$$where we have written $C_\theta=l^2$. This is simply Bessel's equation, its solutions $J_n(\lambda_n r),Y_n(\lambda_n,r)$ are obtained using a series expansion. Note that $Y_n(\lambda_n,r)$ each have asymptotes, so we cannot have a bounded solution with these. If we consider $r\in[l_{r_1},l_{r_2}]$ the unbounded behavior of $Y_n(\lambda_n,r)$ is not an issue. We now impose boundary conditions:$$\Huge R_n(l_r)=0\implies J_n(l_r\sqrt{\lambda_n})=0$$There are infinitely many values of both $J_n$ and $\lambda_n$ so we write $\lambda_{k,n}$, making the $R$ solution:$$\Huge R_n(r)=\sum_{k=1}^\infty A_{k,n}J_n(r\sqrt{\lambda_{k,n}})$$Which makes the total solution:$$\Huge y_n(r,\theta)=\sum_{k=1}^\infty\sum_{n=0}^\infty J_n(r\sqrt{\lambda_{k,n}})(A_{k,n}\cos(n\theta)+B_{k,n}\sin(n\theta))$$