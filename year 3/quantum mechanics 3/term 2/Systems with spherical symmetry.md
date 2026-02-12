
In terms of general potential $V=V(x,y,z)$ is a function of $x,y,z$. If we assume that the system is spherically symmetric $V=V(r)$, we can gain deeper insight. We assume spherical symmetry because we understand that [[Spin|rotations]] of $2\pi$ around any axis leave particles unchanged. 

For a quantum particle, the equivalent justification is that the full [[Time evolution of QM states#Time evolution and the importance of the $ hat H$ eigenbasis|Hamiltonian]] $\hat H$ satisfies:$$\Huge [\hat H,\hat L^2]=0,\,\,[\hat L_z,\hat H]=0$$This implies that the operators $\hat L^2,\hat L_z$ commute with hat $\hat H$. Therefore a measurement of $\hat H$ followed by either $\hat L_z$ or $\hat L^2$ is the same as the reverse order. This is where our symmetry arises.

Commutation implies that the energy eigenstates are also energy eigenstates of $\hat L^2,\hat L_z$. For spherically symmetry systems, we label these states with [[QM in R3#Eigenfunctions of angular momentum|quantum numbers]] $l,m$. 

# Solving Schrodinger equation:

The Schrodinger equation for a spherical system is:$$\Huge -\frac{1}{2m}\underline{\nabla}^2\Psi(r,\theta,\varphi)+V(r)\Psi(r,\theta,\varphi)=E\Psi(r,\theta,\varphi)$$The Laplacian in spherical coordinates becomes:$$\Huge\underline{\nabla}^2=\frac{1}{r^2}\frac{\partial }{\partial r}\left(r^2\frac{\partial }{\partial r}\right)-\frac{\hat L^2}{r^2}$$In order to solve this equation, we make a factorisation ansatz:$$\Huge \Psi(r,\theta,\varphi)=R(r)Y(\theta,\varphi)$$Note that we normalise $R,Y$ separately. Using these pieces, the equation becomes:$$ -\left(\frac{1}{r^2}Y(\theta,\varphi)(r(R'(r)))\right)+\frac{1}{r^2}R(r)(\hat L^2Y(\theta,\varphi))+2mV(r)R(r)Y(\theta,\varphi)=2mEY(\theta,\varphi)R(r)$$We separate the dependence on each side to obtain:$$\Huge \left\{\frac{1}{R(r)}(r^2R'(r))'+2mr^2(E-V(r))\right\}_r+\left\{-\frac{\hat L^2Y(\theta,\varphi)}{Y(\theta,\varphi)}\right\}_\theta=0$$So each term must be constant. This essentially splits our equations in the radial $(\theta,\varphi)$ and the $r$ dependence:$$\Huge\begin{align*}
\hat L^2(\theta,\varphi)Y(\theta,\varphi)&=\eta Y(\theta,\varphi)\\
(r^2R'(r))'-2mr^2(V(r)-E)&=\eta R(r)
\end{align*}$$Here, the first equation defines an eigen-equation for $\hat L^2$, which we know [[QM in R3#Eigenfunctions of angular momentum|solutions]] for:
> The eigenproblem becomes$$\Huge \eta=l |l+1\rangle$$for any $l\in\mathbb{N}$. This has spherical harmonic solutions$$\Huge Y=Y_{l,m},\,\,m\in\{-l,\dots,l\}$$

In order to solve the radial equation:
> We first rewrite the equation using the change of variables:$$\Huge R(r)=\frac{U(r)}{r}\implies R'(r)=\frac{rU'(r)-U(r)}{r^2}\implies(r^2R')'=ru''$$
> Hence our equation becomes$$\Huge -\frac{\hbar^2}{2m}U''(r)+\left(V(r)+\frac{\hbar^2}{2m}\frac{l(l+1)}{r^2}\right)U(r)=EU(r)$$, which looks similar to a Schrodinger equation in $1D$ for some potential:$$\Huge V_\text{eff}(r)=V(r)+\frac{\hbar^2}{2m}\frac{l(l+1)}{r^2}$$![[Systems with spherical symmetry 2026-02-07 23.28.56.excalidraw]]Note that the original potential graphed is that of the hydrogen atom, $V(r)=-e/r$.
> Hence our radial equation now becomes:$$\Huge -\frac{\hbar^2}{2m}U''(r)+V_\text{eff}(r)U(r)=EU(r)$$
> In order to solve this, we need to specify the original $V(r)$ to be that of the Hydrogen atom.

# The Hydrogen atom:

The Hydrogen atom system was pivotal in the development of quantum mechanics as it allowed quantum mechanical systems to be experimented with, and ended up proving the quantum mechanical nature of the hydrogen atom. We consider one electron $e^-$ and one nucleus $p^+$. This is a complex two body system however since $m_{p^+}>>m_{e}$, we approximate the system by fixing $p^+$ and allow $e^-$ to orbit in a spherically symmetric potential:![[Systems with spherical symmetry 2026-02-07 23.43.11.excalidraw]]
We now have everything we need to solve the system for the wave function $\Psi$ and $E$. We begin by rewriting the equation with our coulomb potential:$$\Huge \frac{\hbar^2}{2m}\frac{1}{E}U''(r)=-\left(1-\frac{e^2}{2\pi\epsilon_0\kappa}\frac{1}{\kappa r}-\frac{\hbar^2}{2mE}\frac{l(l+1)}{r^2}\right)U(r)$$We redefine $r\rightarrow\rho=\kappa r$ to get the equation$$\Huge -\frac{1}{\kappa^2}U''(r)=-\left(1-\rho_0\rho+\frac{1}{\kappa^2}\frac{l(l+1)}{r^2}\right)U(r)$$, where $\kappa=\frac{\sqrt{2mE}}{E}$ and $\rho_0(E)=\frac{e^2\kappa}{4\pi\epsilon_0}$. Hence the equation becomes:$$\Huge \frac{dU(r)}{d\rho^2}=\left(1-\frac{\rho_0}{\rho}+\frac{l(l+1)}{\rho^2}\right)U(\rho)$$
In order to solve this equation, we look at its asymptotic behaviour:
> $\rho\rightarrow\infty$ reduces the equation to$$\Huge \frac{d U(\rho)}{d\rho^2}=U(\rho)\implies U(\rho)=Ae^{-\rho}+Be^{\rho}$$, where we set $B=0$ as we would see divergence at $+\infty$. Therefore we find:$$\Huge U(\rho)\sim_{\rho\to\infty} Ae^{-\rho}$$
> $\rho\to0$ reduces the equation to$$\Huge \frac{dU(\rho)}{d\rho^2}=\frac{l(l+1)}{\rho^2}U(\rho)\implies U(\rho)=a\rho^{l+1}+B\rho^{-l}$$, where we set $B=0$ as we would see divergence at $0$. Therefore we find that:$$\Huge U(\rho)\sim_{p\to-\infty}a\rho^{l+1}$$
> Let us now introduce another equation $v(\rho)$ to "absorb" the asymptotic behaviour:$$\Huge U(\rho)=p^{l+1}e^{-\rho}v(\rho)$$

Let us use this form of $U(\rho)$ in the equation for $U$:$$\Huge \rho \frac{d^2v(\rho)}{d\rho^2}+2(l+1-\rho)\frac{dv(\rho)}{d\rho}+(\rho_0-2(l+1))v(\rho)=0$$We want to solve this on general grounds, since we expect that any wave function is analytic. Analytic functions have a regular [[Power series#Power series as a function|power series expansions]], so we propose:$$\Huge v(\rho)=\sum_{j=0}^\infty a_j\rho^j$$Plugging this in to our equation and equating coefficients to zero in front of each power of $\rho^j$, the equation to solve essentially becomes:$$\Huge \sum_{j=0}^\infty(\#a_j+\tilde\#a_{j+1})\rho^j=0$$Which defines the recursion relation:$$\Huge a_{j+1}=\frac{2(j+l+1)-\rho_0}{(j+1)(j+2l+2)}a_j$$Note that if $j>>1$, which will be relevant for the $p\rightarrow\infty$ asymptotic:$$\Huge a_{j+1}\approx\frac{2}{j}a_j\implies a_{j+1}\approx\frac{2^j}{j!}A,\,\,A=a_0$$Assuming this asymptotic behaviour is relevant for any $\rho$ (assumption), we find$$\Huge v(\rho)\approx A \sum_{j=0}^\infty\frac{2^j}{j!}\rho^j=Ae^{2\rho}\to_{\rho\to\infty}\infty$$, which poses a major problem. This would cause $\Psi$ to diverge for large $\rho$.

To avoid this problem, we assume the existence of some $j_\text{max}:a_{j_\text{max}}+1=0$. Using this in the recurrence relation gives the expression$$\Huge 2(j_\text{max}+l+1)-\rho_0(E)=2n-\rho_0(E)=0$$, where we define $n=j_\text{max}+l+1$ so that $n=1,2,\dots$. We have found an equation$$\Huge \rho_0(E)=2n$$that fixes the energy of a hydrogen atom, giving us quantised energy states labelled by the principal quantum number $n$. Hence for the energy of the hydrogen atom$$\Huge E_n=-\left(\frac{m}{2\hbar^2}\left(\frac{e^2}{4\pi\epsilon_0}\right)^2\right)\frac{1}{n^2}=\frac{E_1}{n^2}$$, where we introduce the constant $E_1$. This is known as Bohr's formula. The constant $E_1$ provided ground state energy of the hydrogen atom. This state is associated with the electron $e^-$ being kicked out from the hydrogen atom, an easily measurable quantity. Scientists found the value of this constant experimentally, proving the quantum mechanical nature of the hydrogen atom.

Another natural constant that appears is$$\Huge a=\frac{4\pi\epsilon_0\hbar^2}{e^2m}\approx0.54\times10^{-10}\text{m}$$, introduced by Bohr in his model of the Hydrogen atom. This is the Bohr radius, the minimal distance at which $e^-$ can be away from the nucleus.

## Wave functions:
In terms of the angular $Y_{lm}$ and radial $R(r)$ parts of the wave function, we see that $\Psi$ is labelled by three quantum numbers:$$\Huge\begin{align*}
\Psi_{nlm}(r,\theta,\varphi)&=R_{nl}(r)Y_{lm}(\theta,\varphi)\\
R_{nl}(r)&=\frac{1}{r}U_{nl}(\rho)=\frac{1}{r}\rho^{l+1}e^{-\rho}v_{nl}(\rho)
\end{align*}$$We ask what are the allowed eigenstates for this wave function. The fact that $j_\text{max}\geq0$ fixes $l,m$ for a given $n$:
> Taking $n=1$ we see that $l=0\implies n=0$ and so the radial function $Y_{00}=\frac{1}{\sqrt{4\pi}}$ takes form. This also implies $j_\text{max}=0$ and so $v_{nl}=\text{constant}$. Putting this together, we can find the groundstate wavefunction$$\Huge \Psi_{100}=\frac{1}{\sqrt{\pi a^3}}e^{-r/a}$$, where $a$ is the Bohr radius. This has a maximum at $r=a$, so the probability to find $e^-$ is largest at the Bohr radius.
> Taking $n=2$, $j_\text{max}=1-l\geq0\implies l\leq1\implies l=0$ or $l=1$, so $m=0$ or $m-\{-1,0,1\}$ respectively. The allowed states then become:$$\Huge\Psi_{200},\Psi_{210},\Psi_{211},\Psi_{21(-1)}$$These look like:![[Systems with spherical symmetry 2026-02-12 01.46.10.excalidraw]]
> At generic $n$, we have $n^2$ possible states. That is, the energy spectrum id degenerate with degeneracy $n^2$.

We have the important properties:
> For $n=1,2,\dots$ we have infinite energy states, given by: $$\Huge E_n=\frac{E_1}{n^2}$$
> $E_n<0$, since the electron is in a potential well.
> We see that energy levels become closer and tend to a continuum as $n\to\infty$: $$\Huge E_{n+1}-E_n\approx\frac{1}{(n+1)^2}-\frac{1}{n^2}\to_{n\to\infty}0$$