
# Scattering data for general potentials:

So far we [[Scattering theory#Examples|have seen]] that for any localised initial data $u(x,0)$ for the KdV equation, the auxiliary time-independent Schrodinger equation $$\Huge -\psi''(x)+V(x)\psi(x)=k^2\psi(x)$$with potential $V(x)=-u(x,0)$ has either:
> A continuous spectrum of non-negative eigenvalues $E=k^2\geq0$ and eigenfunctions$$\Huge \psi(x)\approx\begin{cases}e^{ikx}+R(k)e^{-ikx} & x\to-\infty \\
T(k)e^{ikx} & x\to+\infty\end{cases}$$normalised such that the incoming flux is $1$.
> A (possibly empty) discrete spectrum of negative eigenvalues $E=k^2=-\mu_n^2<0$ indexed by $n=1,2,\dots,N$. These look like:$$\Huge\psi_n(x)\approx\begin{cases}c_ne^{\mu_nx} & x\to-\infty \\
d_ne^{-\mu_nx} & x\to+\infty\end{cases}$$So far the $\psi_n$ functions have been normalised so that $d_n=1$, however now we normalise them so that:$$\Huge \langle \psi_n,\psi_n\rangle=\int_\Re|\psi_n(x)|^2dx=1$$

Once $\psi_n$ is normalised this way, the number $c_n$ is called the normalising coefficient and is needed to reconstruct $V(x)=-u(x)$. More precisely, to reconstruct $V(x)$ we need to know the eigenvalues and the asymptotics of the eigenfunctions as $x\to-\infty$:$$\Huge S=\{R(k),\{\mu_n,c_n\}_{n=1}^N\}$$This set is known as the scattering data:
> Clearly, $u$ determines the scattering data completely.
> $u$ can be reconstructed uniquely from the scattering data.

## Examples of scattering data:
> Taking $V(x)=a\delta(x)$ we have:$$\Huge R(k)=\frac{a}{2ik-a}$$For $a<0$, there is a single bound state $\psi(x)=Ae^{-\mu|x|}$ with $\mu=-a/2>0$. Normalising determines $A^2/\mu=1$ and so $A=\sqrt{\mu}=\sqrt{-a/2}$. Thus the general scattering data for $u(x,0)=-a\delta(x)$ is:$$\Huge S(0)=\begin{cases}\{R(k)=\frac{a}{2ik-a}\} & a\geq0 \\
\{R(k)=\frac{a}{2ik-a},\{\mu_1=-a/2,c_1=\sqrt{-a/2}\}\} & a<0\end{cases}$$
> Taking $V(x)=-n(n+1)\text{sech}^2(x)$ for $n\in\mathbb{Z}_{\geq0}$, we find $R(k)=0$ since the potential is [[Scattering theory#Reflectionless potentials|reflectionless]]. To find the bound states, we have $\psi_m(x)=AP_n^m(\tanh(x))$ for $m=1,\dots,n$ and $A$ is a normalisation constant that we fix by imposing$$\Huge 1=\int_\Re|\psi_m(x)|^2dx=A^2\int_{-1}^1P_n^m(y)^2\frac{dy}{1-y^2}=A^1\frac{(n+m)!}{m(n-m)!}$$, where we use the standard properties of $P_n^m$. In addition, $P$ has asymptotics$$\Huge P_n^m(\tanh(x))\approx(-1)^n\frac{(n+m)!}{m!(n-m)!}e^{mx},\,\,x\to-\infty$$Hence the asymptotics of the normalised bound state is:$$\Huge \psi_m(x)\approx(-1)^n\frac{1}{m!}\sqrt{\frac{m(n+m)!}{(n-m)!}}e^{mx},\,\,x\to-\infty$$The full scattering data is therefore:$$\large S(0)=\left\{R(k)=0,\left\{\mu_m^{(n)}=m,c_m^{(n)}=(-1)^n\frac{1}{m!}\sqrt{\frac{m(n+m)!}{(n-m)!}}\right\}^n_{m=1}\right\}$$

# Lax pairs:

We want to solve the initial value problem for a PDE$$\Huge u_t=N(u)$$where $N(u)$ is a function of $u$ and its spatial derivatives, and with boundary conditions $u,u_x,\dots\rightarrow0$ as $x\to\pm\infty$. For the KdV equation, $N(u)=-6uu_x-u_{xxx}$.

Let us think of $\psi_{xx}+u\psi=\lambda\psi$ at some fixed $t$ as an eigenvalue problem$$\Huge L(u)\psi=\lambda\psi$$, where $L(u)$ is the differential operator:$$\Huge L(u)=\frac{\partial^2}{\partial x^2}+u(x,t)$$
Since $L$ depends on $u$, and hence on $t$, the eigenfunctions $\psi$ and eigenvalues $\lambda$ might be different at later times. To remedy this, we turn to the facts:
> If $u(x,t)$ evolves by the KdV equation, then the set of eigenvalues $\{\lambda\}$ of $L(u)$ is independent of $t$.
> There is a set of eigenfunctions $\psi$ of $L(u)$ which evolves in $t$ simply as$$\Huge \psi_t=M(u)\psi$$, where $M(u)$ is some differential operator.

To prove this, we first assume that an operator $M(u)$ can be found such that the time evolution of $L(u(x,t))$ is given by:
> $$\Huge\begin{align*}

\end{align*}$$