
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
L(u)_t&=M(u)L(u)-L(u)M(u)\\
&=[M(u),L(u)]
\end{align*}$$
> Now we let $\lambda,\psi$ be an eigenvalue and eigenfunction of $L$, so that $L\psi=\lambda\psi$. Taking the time derivatives of this equation, we rearrange to find:$$\Huge\begin{align*}
L_t\psi+L\psi_t&=\lambda_t\psi+\lambda\psi_t\\
\implies\lambda_t\psi&=\lambda_t\psi+L\psi_t-\lambda\psi_t\\
&=(ML-LM)\psi+(L-\lambda)\psi_t\\
&=(M\lambda-LM)\psi+(L-\lambda)\psi_t\\
&=(L-\lambda)(\psi_t-M\psi)
\end{align*}$$
> Now consider the inner product on square integrable functions of $x$:$$\Huge\langle \psi_1,\psi_2\rangle=\int_\Re\bar{\psi_1}(x)\psi_2(x)dx$$Since this is self adjoint, and eigenvalues of a self adjoint operators are real:$$\Huge\begin{align*}
\lambda_t \langle \psi,\psi\rangle&=\langle \psi,(L-\lambda)(\psi_t-M\psi)\rangle\\
&=\langle (L-\lambda)\psi,(\psi_t-M\psi)\rangle=0
\end{align*}$$Here, we used the fact that $L\psi=\lambda\psi$. Since $0<\langle \psi,\psi\rangle<\infty$, we deduce that:$$\Huge \lambda_t=0$$
> Now we show that $(L-\lambda)\psi=0$ continues to be true if $\psi$ changes according to $\psi_t=M\psi$. We calculate:$$\Huge\begin{align*}
\frac{\partial }{\partial t}((L-\lambda)\psi)&=L_t\psi+L\psi_t-\lambda_t\psi-\lambda\psi_t\\
&=L_t\psi+L\psi_t-\lambda\psi_t\\
&=L_t\psi+LM\psi-\lambda M\psi\\
&=L_t\psi+LM\psi-M\lambda\psi\\
&=L_t\psi+LM\psi-ML\psi\\
&=(L_t-[M,L])\psi=0
\end{align*}$$
> This shows that if $\psi_t=M\psi$ and $\psi$ starts off as an eigenfunction at $t=0$, then it remains an eigenfunction:$$\Huge (L-\lambda)\psi=\text{constant wrt }t=(L-\lambda)\psi|_{t=0}=0$$Here, $L$ and $M$ are known as a Lax pair.

## Lax pair for KdV:

We have already found $L(u)=\frac{\partial^2}{\partial x^2}+u(x,t)$ for the $L$ operator, where $u$ evolves according to the [[Basic properties of Solitons#The KdV equation|KdV]] equation, so it remains to find $M$ such that:$$\Huge u_t=N(u)=-6uu_x-u_{xxx}\iff L(u)_t=[M(u),L(u)]$$Since $L$ does not depend on time, we have that $L(u)_t=u_t$ and so:$$\Huge [M(u),L(u)]=N(u)=-6uu_x-u_{xxx}$$For now we make a guess about $M$'s form, and will derive a more systematic approach later. We use $D=\frac{\partial }{\partial x},D^2=\frac{\partial^2}{\partial x^2}$ in the following:$$\Huge M(u)=-(4D^3+6uD+3u_x)$$Note that here, $D$ is acting like an operator so acts on everything to its right. Operators act on functions, so it makes sense to write $[D,u]f$ as the action of the commutator between $D,u$ on some function $f$:$$\Huge\begin{align*}
[D,u]f&=(Du-uD)f\\
&=D(uf)-u(Df)\\
&=(Du)f+u(Df)-u(Df)=u_xf\\
\implies[D,u]&=u_x
\end{align*}$$That is, the action of this commutator is simply right multiplication by $u_x$. This can be rephrased as$$\Huge Du=uD+u_x$$, which shows us how to commute $D$ through $u$. More generally, we have that$$\Huge [D^n,u]=\sum_{m=0}^{n-1}{n\choose m}u_{x\dots x}D^m$$where the lower index on $u$ is repeated $n-m$ times. Note that we require $[D^m,D^n]=0$ and $[g(x),h(x)]=0$ for all $n,m$ and functions $g,h$. Using the commutator identities $$\Huge\begin{align*}
[A,BC]&=[A,B]C+B[A,C]\\
[AB,C]&=A[B,C]+[A,C]B
\end{align*}$$we can calculate our relevant commutator:$$\Huge\begin{align*}
L=D^2+u,\,\,M&=-(4D^3+6uD+3u_x)\\
\implies-[M(u),L(u)]&=[4D^3+6uD+3u_x,D^2+u]\\
&=4[D^3,u]+6[uD,D^2]+6[uD,u]+3[u_x,D^2]\\
&=4[D^3,u]+6[u,D^2]D+6u[D,u]+3[u_x,D^2]\\
&=4(u_{xxx}+3u_{xx}D+3u_xD^2)-6(u_{xx}+2u_{x}D)D\\
&+6uu_x-3(u_{xxx}+2u_{xx}D)\\
&=u_{xxx}+6uu_{x}
\end{align*}$$As required. This completes the proof that $u$ solves KdV if and only if $L_t=[M,L]$. Here, our Lax pair is $L,M$ written above.

# Time evolution of scattering data:

We have seen that if $u$ evolves by the KdV equation, then:
> Eigenvalues $\lambda$ of $L(u)=D^2$ with $u$ constant in $t$.
> Eigenfunctions $\psi$ evolve by $\psi_t=M(u)\psi$

We ask how the scattering data associated to $V=-u$ evolve with time. To find out, we observe the asymptotics of the time-evolution equation $\psi_t=M(u)\psi$ as $x\to\pm\infty$. Since $u,u_x\to0$ at $x\to\pm\infty$ for all $t$, we have that$$\Huge M(u)\approx-4D^3$$, which is independent of $u(x,t)$. Therefore we can evolve scattering data in $t$ without knowing what $u$ evolves to. 