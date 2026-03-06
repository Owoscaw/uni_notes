
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