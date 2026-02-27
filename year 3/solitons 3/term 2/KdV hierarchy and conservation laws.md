

# Deriving and generalising the [[Basic properties of Solitons#The KdV equation|KdV]] equation:

It is natural to ask if there are any other [[Evolving scattering data#Time evolution of scattering data|evolution equations]] for $u(x,t)$ such that the eigenvalues of$$\Huge L(u)=\frac{\partial^2}{\partial x^2}+u(x,t)$$are constant in time. That is, we are looking for equations such that each $L(u)$ at different times are isospectral. Such equations are known as isospectral flows. The idea of the [[Evolving scattering data#Lax pairs|Lax pair]] allows us to find them. 

Note that the only equivalence we needed to prove eigenvalues were constant in time was$$\Huge u_t=N(u)\iff L(u)_t=[M(u),L(u)]$$, no other information regarding $M$ was needed. Note that $M(u)$ is not completely arbitrary, as $L_t=u_t$ is a multiplicative operator, $[M,L]$ must also be a multiplicative operator. This means that all $D=\partial_x$ must cancel out in the commutator. If they do cancel, $[M,L]$ will be a polynomial in $u,u_x,u_{xx},\dots$. Setting this equal to $u_t$ gives the desired evolution equation.

Recall the following tools that will help us find these operators:
> The [[Inner product spaces#Complex inner products|Hermitian inner product]] of functions $\phi(x),\chi(x)$ is defined as$$\Huge \langle \phi,\chi\rangle=\int_{-\infty}^\infty\overline{\phi(x)}\chi(x)dx$$, using this notation we can write $L=D^2+u$ as$$\Huge \langle \phi,L_\chi\rangle=\langle L\phi,\chi\rangle$$for all $\phi,\chi$.
> For a differential operator $A$, we define the [[Eigenfunction methods#Adjoint operators|adjoint]] of $A$ to be the operator $A^\dagger$ such that$$\Huge \langle \phi,A_\chi\rangle=\langle A^\dagger\phi,\chi\rangle$$for all $\phi,\chi$. $A^\dagger$ is akin to the transpose of a matrix, and satisfies:$$\Huge (A^\dagger)^\dagger,\,\,(AB)^\dagger=B^\dagger A^\dagger,\,\,[A,B]^\dagger=[B^\dagger,A^\dagger]$$Operators satisfying $A=A^\dagger$ are called self-adjoint, while operators satisfying $A^\dagger=-A$ are called skew-adjoint.

If $A$ is just a multiplication by a real function, then $A^\dagger=A$, which must be true for $[L,M]$ and therefore $[L,M]^\dagger=[L,M]$. This together with $L=L^\dagger$ gives:$$\Huge\begin{align*}
[L,M]&=[L,M]^\dagger\\
&=[M^\dagger,L^\dagger]\\
&=[M^\dagger,L]\\
&=-[L,M^\dagger]\\
\implies [L,M+M^\dagger]&=0
\end{align*}$$That is, the symmetric part of $M$ must commute with $L$. Since the part of $M$ that does not commute with $L$ that makes a difference to the equation $L_t+[L,M]=0$ we can assume $M$ is antisymmetric:$$\Huge M(u)^\dagger=M(u)$$This ensures $\langle \psi,\psi\rangle$ is constant under time evolution $\psi_t=M(u)\psi$. So we require:
> $M(u)^\dagger=M(u)$
> $[M(u),L(u)]$ is multiplicative

As $M$ is a differential operator in $x$, we can write it as$$\Huge M=\sum_{j=0}^n\gamma_j(x)D^j+D^j\gamma_j(x)$$where $\gamma_j(x)$ are real functions of $x$. If $\alpha(x)$ is a real function, then $\alpha(x)^\dagger=\alpha(x)$ and $D^\dagger=-D$, which implies:$$\Huge\begin{align*}
(D^{2j})^\dagger&=D^{2j}\\
(D^{2j-1})^\dagger&=-D^{2j-1}
\end{align*}$$Promoting the antisymmetric part of $M$ to $M$ itself, we write:$$\Huge M=\sum_{\begin{align*}
j&\in\mathbb{N}\\
0<2&j-1\leq n
\end{align*}}(\gamma_{2j-1}(x)D^{2j-1}+D^{2j-1}\gamma_{2j-1}(x))$$One can check that $[M,L]$ being multiplicative forces the leading term in $D$ to be constant, so our general guess for $M$ is$$\Huge\begin{align*}
M_m(x)&=\sum_{j=1}^m(\beta_j(x)D^{2j-1}+D^{2j-1}\beta_j(x))\\
&=-2^{2(m-1)}D^{2m-1}+\sum_{j=1}^{m-1}(\beta_j(x)D^{2j-1}+D^{2j-1}\beta_j(x))
\end{align*}$$for real functions $\beta_j(x)$ and relabeling $\gamma_{2j-1}=\beta_j$. 

We now have no choice but to compute. We will find that $N_m(u)=[M_m,L]$ is a polynomial in $u,u_x,\dots$ and that setting $L_t+[L,M_m]=0$ will give a KdV-like equation with $x$ derivatives up to $2m-1$:
> $m=0$ implies $M_0(u)=0$ and so $[M_0(u),L(u)]=0=N_0(u)$. The PDE for $u$ is then$$\Huge u_t=0$$, which makes $L(u)=D^2+u$ isospectral at different $t$, but trivially.
> $m=1$ implies $M_1(u)=-D$ and so:$$\Huge [M_1(u),L(u)]=[-D,D^2+u]=-u_x=N_1(u)$$The PDE for $u$ becomes the advection equation$$\Huge u_t+u_x=0$$, which has general solution:$$\Huge u(x,t)=u(x-t,0)$$This is a travelling wave moving with constant velocity $1$.
> $m=2$ implies $M_2(u)=-4D^3+\beta_1D+D\beta_1$ and therefore:$$ \begin{align*}
[M_2(u),L(u)]&=[-4D^3+\beta_1D+D\beta_1,D^2+u]\\
&=[-4D^3+2\beta_1D+\beta_{1,x},D^2+u]\\
&=-4[D^3,u]-2[D^2,\beta_1]D+2\beta_1[D,u]-[D^2,\beta_{1,x}]\\
&=-4(3u_xD^2+3u_{xx}D+u_{xxx})-2(2\beta_{1,x}D+\beta_{1,xx})D\\
&+2\beta_1u_x-(2\beta_{1,xx}D+\beta_{1,xxx})\\
&=-4(3u_x+\beta_{1,x})D^2-4(3u_{xx}+\beta_{1,xx})D+(-4u_{xxx}+2\beta_1u_x-\beta_{1,xxx})
\end{align*}$$Requiring this to be multiplicative, the left coefficients of $D^2$ and $D$ must vanish. Therefore we find$$\Huge 3u_x+\beta_{1,x}=0\implies\beta_1=-3u+k$$for some constant $k$. Doing the same for the $D$ term we find that the multiplicative term becomes$$\Huge -4u_{xxx}-\beta_{1,xxx}+2\beta_1u_x=-u_{xxx}-6uu_x+2ku_x=N_2(x)$$, and so the associated PDE is:$$\Huge u_t-u_{xxx}-6uu_x=2ku_x$$This is simply the KdV equation if $k=0$. 

This shows that the KdV equation is the third member of a hierarchy of PDEs given by $u_t=N_m(u)=[M_m(u),L(u)]$.


# Connection to conservation laws:

Recall that the KdV equation has an infinite sequence of [[year 3/solitons 3/term 1/Conservation laws|conserved charges]]$$\Huge Q_n=\int_{-\infty}^\infty \rho_ndx$$where the conservation of $Q_n$ is proven by showing that$$\Huge \frac{\partial }{\partial t}\rho_n+\frac{\partial }{\partial x}j_n=0$$when KdV holds, for some current density with$$\Huge [j_n]_{-\infty}^\infty=0$$We can normalise the charge densities $\rho_n$ so that the $u^n$ term has coefficient $1$. This gives us two infinite sequences:
> A sequence $Q_1,\dots$ of conserved charges for the KdV equation
> An infinite sequence $N_0,N_1,\dots$ of polynomials in $u$ and its $x$ derivatives such that setting $u_t=N_n(u)$ leaves eigenvalues of $D^2+u(x,t)$ constant

One possibility is that each evolution equation $u_t=K_n(u)$ has its own set of conserved charges for that equation alone. However this is boring, so let us introduce some new tools that will help us.

## Functional derivatives:
Suppose that $f$ is some function of $u$ and its $x$ derivatives, then$$\Huge F[u]=\int_{-\infty}^\infty f(u,u_x,\dots)dx$$is an example of a functional of $u$. Consider a small variation $\delta u(x)$ of $u$ such that $u(x)\rightarrow u(x)+\delta u(x)$ with $\delta u(x)\to0$ at infinity. We demand similar conditions on the $x$ derivatives of $\delta u$ so that the varied field still obeys boundary conditions. This makes $F[u]$ become:$$\Huge\begin{align*}
F[u+\delta u]&=\int_{-\infty}^\infty f(u+\delta u,(u+\delta u)_x,\dots)dx\\
&=\int_{-\infty}^\infty f(u+\delta u,u_x+\delta u_x,\dots)dx\\
&=\int_{-\infty}^\infty f+\frac{\partial f}{\partial u}\delta u+\frac{\partial f}{\partial u_x}\delta u_x+\dots dx\\
&=F[u]+\int_{-\infty}^\infty\frac{\partial f}{\partial u}\delta u+\frac{\partial f}{\partial u_x}\delta u_x+\frac{\partial f}{\partial u_{xx}}\delta u_{xx}+\dots dx\\
&=F[u]+\int_{-\infty}^\infty\left(\frac{\partial f}{\partial u}-\frac{\partial }{\partial x}\frac{\partial f}{\partial u_x}+\frac{\partial^2}{\partial x^2}
\frac{\partial f}{\partial u_{xx}}+\dots\right)\delta u\,dx\end{align*}$$where the boundary term in IBP vanishes due to the boundary conditions on $\delta u$. The term in the last line multiplying $\delta u(x)$ is known as the functional derivative of $F[u]$, written as $\delta F[u]/\delta u(x)$. More precisely, the functional derivative is defined by$$\Huge F[u+\delta u]=F[u]+\int_{-\infty}^\infty\frac{\delta F[u]}{\delta u(x)}\delta u\,dx+\mathcal{O}(\delta u^2)$$, equivalent to $f(x+\delta x)=f(x)+\frac{df}{dx}\delta x$ for ordinary functions. For functionals defined above, our calculation shows that:$$\Huge \frac{\delta F[u]}{\delta u}=\frac{\partial f}{\partial u}-\frac{\partial }{\partial x}\frac{\partial f}{\partial u_x}+\frac{\partial^2}{\partial x^2}\frac{\partial f}{\partial u_{xx}}+\dots$$
The conserved quantities $Q_n[u]$ are examples of functionals of $u$, and so we can calculate their functional derivatives:$$\Huge\begin{align*}
\frac{\delta Q_1[u]}{\delta u}&=\frac{\delta}{\delta u}\int_{-\infty}^\infty u\,dx=1\\
\frac{\delta Q_2[u]}{\delta u}&=\frac{\delta}{\delta u}\int_{-\infty}^\infty u^2dx=2u\\
&\vdots
\end{align*}$$Taking the $x$ derivative of these shows that they match, up to an overall scale, the equations of the KdV hierarchy. 

The normalisation of the charges and the scale of $t$ can defined to make this precise. This defines Gardner's general result:$$\Huge u_t=\frac{\partial }{\partial x}\frac{\delta}{\delta u}\left(-\frac{C_m}{2}Q_{m+1}[u]\right)\iff u_t=N_m(u)$$This connects the $m+1$th KdV conservation law to the $m$th equation in the KdV hierarchy, so our sequences are indeed the same. The factor $-C_m/2$ where $C_m$ is the $m$th Catalan number is to ensure that the normalisation conventions match.

If $u_m(x,t)$ evolves by the $m$th KdV equation, then all $Q_n$ are conserved quantities for it. That is, all equations in the KdV hierarchy share the same infinite sequence of conserved quantities. Indeed as $x\to\pm\infty$$$\Huge M_m(u)\rightarrow-\frac{1}{2}(2D)^{2m-1}$$determines the [[Evolving scattering data#Time evolution of scattering data|time evolution of scattering data]]:$$\Huge\begin{align*}
R(k;t)&=R(k;0)e^{(2ik)^{2m-1}t}\\
T(k;t)&=T(k;0)\\
c_n(t)&=c_n(0)e^{-\frac{1}{2}(2\mu_n)^{2m-1}t}\\
d_n(t)&=d_n(0)e^{\frac{1}{2}(2\mu_n)^{2m-1}t}
\end{align*}$$The time independence of the transmission coefficient for $V=-u$ leads to infinitely many conservation laws from the coefficients of the formal power series of the solution to the Riccati equation$$\Huge S_x+2ikS-S^2=u$$, or equivalently the Gardner transform. Being related to the eigenvalue equation $L(u)\psi=-k^2\psi$ for the Lax operator $L(u)$, the conservation laws are also common to the entire KdV hierarchy.

Setting one "time" for each equation in the hierarchy, so that instead of $u_m(x,t)$ with $\frac{\partial }{\partial t}u_m=N_m(u)$ we have $u(x,t_1,t_2,\dots)$ with$$\Huge \frac{\partial }{\partial t_m}u=N_m(u)=-\frac{C_m}{2}\frac{\partial }{\partial x}\frac{\delta Q_{m+1}[u]}{\delta u},\,\,\forall m=0,1,2,\dots$$From here we evolve (flow) $u(x,t_1,t_2,\dots)$ in $t_i$, then $t_j$. It turns out we end up with the same function of $x$ as if we evolve in $t_j$ then $t_i$. This is known as the idea of commuting flows.