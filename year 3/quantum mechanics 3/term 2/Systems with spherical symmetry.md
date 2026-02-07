
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

