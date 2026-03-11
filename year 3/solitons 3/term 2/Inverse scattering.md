
It remains to reassemble the KdV field $u(x,t)$, or equivalently the Schrodinger potential $V(x;t)=-u(x,t)$ from the [[Evolving scattering data#Time evolution of scattering data|time-evolved scattering data]]. This is the inverse scattering/reassembly step in [[Scattering theory#Physical interpretation|our method]]. We are essentially sitting at infinity, throwing particles at our potential and trying to deduce the form of $V(x)$ by measuring how they return.

It turns out it is enough to know $R(k)$ for real $k$ together with the $N$ discrete eigenvalues $-\mu_j^2,j=1,\dots,N$ and the normalising coefficients $c_j,j=1,\dots,N$. The full set$$\Huge\{R(k),\{\mu_n,c_n\}_{n=1}^N\}$$is precisely the scattering data we evolved. There are two important special cases:
> $N=0$, where $V(x)$ has no bound states
> $R(k)=0$ for all $k$, $V(x)$ is reflectionless but there is still information about $V(x)$ hidden in the bound state eigenvalues and normalisation coefficients.

# The Marchenko equation:

We want to solve the inverse scattering problem for a given scattering data at $x=-\infty$ to determine the potential $V(x)$ and hence the KdV field. The recipe to do this is as follows:
> Construct the function $$\Huge F(\xi)=\int_{-\infty}^\infty R(k)e^{-ik\xi}\frac{dk}{2\pi}+\sum_{n=1}^Nc_n^2e^{\mu_n\xi}$$from the scattering data.
> Solve the Marchenko equation$$\Huge K(x,z)+F(x+z)+\int_{-\infty}^xK(x,y)F(y+z)dy=0$$to determine the unknown function $K(x,z)$ for all $z\leq x$.
> Finally, determine the Schrodinger potential from$$\Huge V(x)=2\frac{d}{dx}K(x,x)$$, the KdV field is then given by $u=-V$. Note that $K(x,x)$ is defined by demanding one-sided continuity of $K(x,z)$ as the left-sided limit of $K(x,z)$ at $z=x$:$$\Huge K(x,x)=\lim_{z\to x^-}K(x,z)$$

This process applies at some fixed KdV time $t$, however we can use our time evolution results$$\Huge\begin{align*}
R(k;t)&=R(k;0)e^{-8ik^3t}\\
c_n(t)&=c_n(0)e^{-4\mu_n^3t}
\end{align*}$$where $k,\mu_n$ are independent of time. To find the field at time $t$ we just apply the above starting from:$$\Huge\begin{align*}
F(\xi;t)&=\int_{-\infty}^\infty R(k;t)e^{-ik\xi}\frac{dk}{2\pi}+\sum_{n=1}^Nc_n(t)^2e^{\mu_n\xi}\\
&=\int_{-\infty}^\infty R(k;0)e^{-ik(\xi+8k^2t)}\frac{dk}{2\pi}+\sum_{n=1}^Nc_n(0)^2e^{\mu_n(\xi-8\mu_n^2t)}
\end{align*}$$This solves our problem (at least in principle). In practice, the term involving $R$ in the definition of $F$, with the integral over $k$, makes the calculation of $F$ hard when $t>0$. For reflectionless potentials this term is absent and $F(\xi;t)$ can be read off at any time. This yields the pure multisoliton solutions that can also be found through [[Backlund transformations#Definition|Backlund]] or [[The Hirota method#Motivations|Hirota]]. Even when $R$ is nonzero, it can be shown that the term involving $R$ tends to $0$ at late times $t\to\infty$ at any fixed position in space:![[Inverse scattering 2026-03-06 19.06.16.excalidraw]]The result of this process is a sort of "nonlinear Fourier analysis".

# The single KdV soliton:

Consider a reflectionless potential with a single bound state encoded in $\{\mu_1,c_1\}=\{\mu,c\}$, then for fixed $t$$$\Huge F(\xi)=c^2e^{\mu\xi}$$and the Marchenko equation reads:$$\Huge K(x,z)+c^2e^{\mu(x+z)}+\int_{-\infty}^xK(x,y)c^2e^{\mu(y+z)}dy=0$$We must solve this for $z\leq x$. First we factorise $e^{\mu x}$ $$\Huge K(x,z)+e^{\mu x}\left(c^2e^{\mu x}+\int_{-\infty}^xK(x,y)c^2e^{\mu(y+z)}dz\right)=0$$and notice that the bracketed term is independent of $z$, meaning we can write$$\Huge K(x,z)=h(x)e^{\mu x}$$for some $h(x)$. Substituting this form and dividing through by $e^{\mu z}$ we get the condition on $h$:$$\Huge\begin{align*}
0&=h(x)+c^2e^{\mu x}+c^2\int_{-\infty}^xh(x)e^{2\mu y}dy\\
&=h(x)\left(1+c^2\int_{-\infty}^xe^{2\mu y}dy\right)+c^2e^{\mu x}\\
\implies h(x)&=-\frac{c^2e^{\mu x}}{1+\frac{c^2}{2\mu}e^{2\mu x}}
\end{align*}$$Setting $c^2=2\mu e^{-2\mu x_0}$ we obtain$$\Huge h(x)=-2\mu\frac{e^{\mu(x-2x_0)}}{1+e^{2\mu(x-x_0)}}$$and therefore for $z\leq x$:$$\Huge K(x,z)=-2\mu\frac{e^{\mu(x+z-2x_0)}}{1+e^{2\mu(x-x_0)}}$$Therefore our potential has form$$\Huge V(x)=2\frac{d}{dx}K(x,x)=-2\mu^2\text{sech}^2(\mu(x-x_0))$$and $u=-V$ is indeed a snapshot of a single KdV soliton at time $t$ with center at $x=x_0$. We can easily incorporate time evolution using $$\Huge c(t)^2=c(0)^2e^{-8\mu^3t}=2\mu e^{-2\mu(x_0-4\mu^2t)}$$which makes the KdV field at time $t$:$$\Huge u(x,t)=-V(x,t)=2\mu^2\text{sech}^2(\mu(x-x_0-4\mu^2t))$$

# The $N$-soliton KdV solution:

Let us consider a reflectionless potential $R(k)=0$ with $N$ bound states encoded in $\{\mu_n,c_n\}_{n=1}^N$, then:$$\Huge F(\xi)=\sum_{n=1}^Nc_n^2e^{\mu_n\xi}$$Since $$\Huge F(x+z)=\sum_{n=1}^Nc_n^2e^{\mu_nx}e^{\mu_nz}$$is a sum of factorised terms, we look for a solution where $K(x,z)$ is also a sum of factorised terms. We encode this using vector and matrix notation, setting$$\Huge E(x)=\begin{pmatrix}c_1e^{\mu_1x} \\ \vdots \\ c_Ne^{\mu_Nx}\end{pmatrix},\,\,H(x)=\begin{pmatrix}c_1h_1(x) \\ \vdots \\ c_Nh_N(x)\end{pmatrix}$$where $H(x)$ is to be determined. With this notation defined, we write$$\Huge F(x+z)=E(x)^\top E(z)$$and look for $K(x,z)$ of the form:$$\Huge K(x,z)=H(x)^\top E(z)=\sum_{n=1}^Nc_n^2h_n(x)e^{\mu_nz}$$Substituting this into the Marchenko equation shows:$$\Huge \begin{align*}
0&=K(x,z)+F(x+z)+\int_{-\infty}^xK(x,y)F(y+z)dy\\
&=H(x)^\top E(z)+E(x)^\top E(z)+H(x)^\top\int_{-\infty}^\infty E(y)E(y)^\top E(z)dy\\
&=\left(H(x)+E(x)+\int_{-\infty}^xE(y)E(y)^\top H(x)dy\right)^\top E(z)
\end{align*}$$If we set the bracketed term to $0$ and solve, we will have found a solution. It turns out that this is true when$$\Huge \Gamma(x)H(x)=-E(x)$$where $\Gamma(x)$ is an $N\times N$ matrix$$\Huge \Gamma(x)=\mathbb{1}_{N\times N}+\int_{-\infty}^x E(y)E(y)^\top dy$$with matrix elements:$$\Huge\begin{align*}
\Gamma(x)_{mn}&=\delta_{mn}+\int_{-\infty}^x c_me^{\mu_my}c_ne^{\mu_ny}dy\\
&=\delta_{mn}+c_mc_n\frac{e^{(\mu_m+\mu_n)y}}{\mu_m+\mu_n}
\end{align*}$$Note that we have:$$\Huge \frac{d}{dx}\Gamma(x)=E(x)E(x)^\top$$
Therefore we can solve for $H$$$\Huge H(x)=-\Gamma(x)^{-1}E(x)$$and so the form of $K(x,z)$ must become:$$\Huge\begin{align*}
K(x,z)&=E(z)^\top H(x)\\
&=-E(z)^\top \Gamma(x)^{-1}E(x)\\
&=-\text{tr}(\Gamma(x)^{-1}E(x)E(z)^\top)
\end{align*}$$Therefore$$\Huge\begin{align*}
K(x,x)&=-\text{tr}(\Gamma(x)^{-1}E(x)E(x)^\top)\\
&=-\text{tr}\left(\Gamma(x)^{-1}\frac{d}{dx}\Gamma(x)\right)\\
&=-\text{tr}\left(\frac{d}{dx}\log\Gamma(x)\right)\\
&=-\frac{d}{dx}\text{tr}(\log\Gamma(x))\\
&=-\frac{d}{dx}\log(\det\Gamma(x))
\end{align*}$$, where we used the identities:$$\Huge \text{tr}\left(\frac{d}{dx}\log\Gamma\right)=\text{tr}\left(\Gamma^{-1}\frac{d}{dx}\Gamma\right),\,\,\text{tr}(\log\Gamma)=\log(\det\Gamma)$$This implies that the KdV field is given by$$\Huge u=-2\frac{d}{dx}K(x,x)=2\frac{d^2}{dx^2}\log(\det\Gamma(x))$$, reinstating time dependence through $\Gamma$  shows$$\Huge u(x,t)=2\frac{\partial^2}{\partial x^2}\log(\det\Gamma(x;t))$$with:$$\Huge \Gamma(x;t)_{mn}=\delta_{mn}+c_m(t)c_n(t)\frac{e^{(\mu_m+\mu_n)x}}{\mu_m+\mu_n}$$
Note that these formulae are very similar to the $N$-soliton KdV solution we found using [[The Hirota method#The $N$-soliton solution|Hirota]]'s method. To show they are identical, we use Sylvester's determinant theorem$$\Huge \det(\mathbb{1}_{N\times N}+AB)=\det(\mathbb{1}_{N\times N}+BA)$$for any pair of $N\times N$ matrices. We take$$\Huge A_{mn}=c_me^{\mu_mx}\delta_{mn},\,\,B_{mn}=\frac{c_ne^{\mu_nx}}{\mu_m+\mu_n}$$and so$$\Huge (AB)_{mn}=\frac{c_mc_ne^{(\mu_m+\mu_n)x}}{\mu_m+\mu_n},\,\,(BA)_{mn}=\frac{c_n^2e^{2\mu_nx}}{\mu_m+\mu_n}$$, therefore we can write$$\Huge u(x,t)=2\frac{\partial^2}{\partial x^2}\log(\det S(x;t))$$with$$\Huge\begin{align*}
S(x;t)_{mn}&=\delta_{mn}+\frac{1}{\mu_m+\mu_n}c_n^2(t)e^{2\mu_nx}\\
\implies S(x;t)_{mn}&=\delta_{mn}+\frac{2\mu_n}{\mu_m+\mu_n}e^{2\mu_n(x-x_{0,n}-4\mu_n^2t)}
\end{align*}$$where we replaced $c_n(0)$ with $x_{0,n}$ by setting:$$\Huge c_n(0)^2=2\mu_ne^{-2\mu_nx_{0,n}}$$These equations give the general form of the $N$-soliton solution of the KdV equation.