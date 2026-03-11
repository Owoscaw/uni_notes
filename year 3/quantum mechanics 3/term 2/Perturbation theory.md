
Real physical systems have very complex forms of $V(x)$ and neither $\Psi$ or the energy spectrum can be found analytically. However, to a decent approximation, these systems can be seen as small deformations of some known solvable potential. In this case, we can apply perturbation theory to solve the full system by building on the known solutions of the underlying solvable system.

We assume that the Hamiltonian for the full system is given by $$\Huge\hat H=\hat H^{(0)}+\lambda H'$$where $\hat H^{(0)}$ is the known solvable Hamiltonian, $H'$ is the Hamiltonian of the perturbation, and $\lambda>0$ is a parameter (perturbation parameter) measuring how far away $\hat H^{(0)}$ is from the full system (that is, how big the perturbation is).

# Non-degenerate theory:

In this case, the known $\hat H^{(0)}$ has a non-degenerate energy spectrum:$$\Huge \hat H^{(0)}|\psi_n^{(0)}\rangle=E_n^{(0)}|\psi_n^{(0)}\rangle,\,\,\langle \psi_n^{(0)}|\psi_l^{(0)}\rangle=\delta_{nl}$$That is, if $l\neq n$ we have $E_n\neq E_l$, there is one energy state per wave function. We aim to find all eigenvectors $|\psi_n\rangle$ and energy states $E_n$ for the full $\hat H$ system. Perturbation theory gives a systematic way to find these states in terms of the eigenvectors and energy states of the solvable system. Given that $\lambda<<1$  we write $|\psi_n\rangle,E_n$ as:$$\Huge\begin{align*}
|\psi_n\rangle&=|\psi_n^{(0)}\rangle+\lambda |\psi_n^{(1)}\rangle+\lambda^2 |\psi_n^{(2)}\rangle+\dots\\
E_n&=E_n^{(0)}+\lambda E_n^{(1)}+\lambda^2 E_n^{(2)}+\dots
\end{align*}$$Where $|\psi_n^{(i)}\rangle,E_n^{(i)}$ are the $i$th order correction to the $n$th eigenstate/energy. Our aim is therefore to find these expansion coefficients.

Using these expansions in the eigenvalue problem that defined energy states:$$\Huge\begin{align*}
\hat H |\psi_n\rangle&=(\hat H^{(0)}+\lambda\hat H)(|\psi_n^{(0)}\rangle+\lambda |\psi_n^{(1)}\rangle+\dots)=E_n |\psi_n\rangle\\
&=(E_n^{(0)}+\lambda E_n^{(1)}+\dots)(|\psi_n^{(0)}\rangle+\lambda |\psi_n^{(1)}\rangle+\dots)
\end{align*}$$Equating powers of $\lambda$ gives:$$\Huge\begin{align*}
\lambda^0:\hat H^{(0)}|\psi_n^{(0)}\rangle&=E_n^{(0)}|\psi_n^{(0)}\rangle\\
\lambda^1:\hat H^{(0)}|\psi_n^{(1)}\rangle+\hat H'|\psi_n^{(0)}\rangle&=E_n^{(0)}|\psi_n^{(1)}\rangle+E_n^{(1)}|\psi_n^{(1)}\rangle\\
&\vdots
\end{align*}$$Next we take each equation (we show $\lambda^1$ for simplicity) at left multiply by $\langle \psi_n^{(0)}|$ while using $\langle \psi_n^{(0)}|\psi_n^{(0)}\rangle=1$:$$\Huge\begin{align*}
\langle \psi_n^{(0)}|\hat H^{(0)}|\psi_n^{(1)}\rangle+\langle \psi_n^{(0)}|\hat H' |\psi_n^{(0)}\rangle&=E_n^{(0)} \langle \psi_n^{(0)}|\psi_n^{(1)}\rangle+E_n^{(1)}\langle \psi_n^{(0)}|\psi_n^{(0)}\rangle\\
E_n^{(0)} \langle \psi_n^{(0)}|\psi_n^{(1)}\rangle+\langle \psi_n^{(0)}|\hat H' |\psi_n^{(0)}\rangle&=E_n^{(0)} \langle \psi_n^{(0)}|\psi_n^{(1)}\rangle+E_n^{(1)}\\
\implies E_n^{(1)}&= \langle \psi_n^{(0)}|\hat H' |\psi_n^{(0)}\rangle
\end{align*}$$We see that the first order correction to energy is the expectation value of the perturbation Hamiltonian $H'$ in the non-perturbed state $|\psi_n^{(0)}\rangle$. 

We now aim to find the first order correction to the eigenstate $|\psi_n^{(1)}\rangle$. We can write the equation we got for $\lambda^1$ terms as:$$\Huge (\hat H^{(0)}-E_n^{(0)})|\psi_n^{(1)}\rangle=(E_n^{(1)}-\hat H')|\psi_n^{(0)}\rangle$$To solve this for the state correction, we use the fact that the vectors $|\psi_n^{(0)}\rangle$ for all $n$ span the full eigenbasis. Therefore we can write our correction as a linear combination of these vectors:$$\Huge|\psi_n^{(1)}\rangle=\sum_{j}\alpha^n_j |\psi_j^{(0)}\rangle$$Putting this into our equation gives$$\Huge\begin{align*}
\sum_j\alpha_j^n(\hat H^{(0)}-E_n^{(0)})|\psi_j^{(0)}\rangle&=(E_n^{(1)}-\hat H')|\psi_n^{(0)}\rangle\\
\implies\sum_j\alpha_j^n(E_j^{(0)}-E_n^{(0)})|\psi_j^{(0)}\rangle&=
\end{align*}$$where we are solving for the coefficients $\alpha_j^n$. Now we act with $\langle \psi_q^{(0)}|$ on the left to get:$$\Huge\begin{align*}
\sum_j\alpha_j^n(E_j^{(0)}-E_n^{(0)})\langle \psi_q^{(0)}|\psi_j^{(0)}\rangle&=E_n^{(1)}\langle \psi_q^{(0)}|\psi_n^{(0)}\rangle-\langle \psi_q^{(0)}|\hat H' |\psi_n^{(0)}\rangle\\
\implies\sum_j\alpha_j^n(E_j^{(0)}-E_n^{(0)})\delta_{qj}&=E_n^{(1)}\delta_{qn}-\langle \psi_q^{(0)}|\hat H' |\psi_n^{(0)}\rangle\\
\implies\alpha_q^n(E_q^{(0)}-E_n^{(0)})&=
\end{align*}$$Therefore we have two cases:
> $q=n$ implies the LHS is zero and so we recover the equation for the first order energy correction.
> $q\neq n$ allows us to solve for $\alpha_q^n$:$$\Huge\alpha_q^n=\frac{\langle \psi_q^{(0)}|H' |\psi_n^{(0)}\rangle}{E_n^{(0)}-E_q^{(0)}}$$

Using this in our equation for $|\psi_n^{(1)}\rangle$ shows us:$$\Huge |\psi_n^{(1)}\rangle=\sum_{j\neq n}\frac{\langle \psi_j^{(0)}|\hat H' |\psi_n^{(0)}\rangle}{E_n^{(0)}-E_j^{(0)}}|\psi_j^{(0)}\rangle$$This is the first order correction to the eigen energy state $|\psi_n\rangle$ of the full Hamiltonian. This is well defined for all $j\neq n$ as the system is non-degenerate and we have different eigen energies for each state. 

It turns out that corrections for energy give more accurate results than corrections to the state, so we stop here and use the unperturbed energy with the first order correction.

Let us look at an example of an infinite potential well where we add a "step" potential $V_0$ as a perturbation:
![[Perturbation theory 2026-03-11 16.25.54.excalidraw]]
> Before perturbation we have$$\Huge V_0(x)=\begin{cases}\infty & x>a,\,\,x<0 \\
0 & 0<x<a\end{cases}$$which we have solved previously to find:$$\Huge\begin{align*}
\Psi_n^{(0)}(x)&=\sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right)\\
E_n^{(0)}&=\frac{n^2\pi^2}{2ma^2}
\end{align*}$$
> We then add the perturbation:$$\Huge V_0(x)+V'(x)=\begin{cases}\infty & x>a,\,\,x<0 \\
V_*\neq0 & 0<x<a\end{cases}$$This makes the perturbed Hamiltonian:$$\Huge H'=\begin{cases}V_* & 0<x<a \\
0 & \text{otherwise}\end{cases}$$
> We can now compute the corrections to the unperturbed states:$$\Huge\begin{align*}
E_n^{(1)}&=\langle \psi_n^{(0)}|H' |\psi_n^{(0)}\rangle\\
&=\int_0^aH'\psi_n^*(x)\psi_n(x)dx\\
&=V_*\int_0^a\psi_n^*(x)\psi_n(x)dx=V_*\\
\implies E_n&=E_n^{(0)}+V_*
\end{align*}$$Where I have omitted the superscript and used the fact that $\psi_n(x)$ is normalised.
> We could consider a different perturbation:$$\Huge V_0(x)+V'(x)=\begin{cases}\infty &  x<0,\,\,x>a \\
V_* & 0<x<a/2 \\
0 & a/2<x<a\end{cases}$$In this case we compute:$$\Huge\begin{align*}
E_n^{(1)}&=\langle \psi_n^{(0)}|H'|\psi_n^{(0)}\rangle\\
&=\int_0^aH'\psi_n^*(x)\psi_n(x)dx\\
&=V_*\int_0^{a/2}\psi_n^*(x)\psi_n(x)dx\\
&=V_*\frac{2}{a}\int_0^{a/2}\sin^2\left(\frac{n\pi}{a}x\right)dx=V_*/2\\
\implies E_n&=E_n^{(0)}+V_*/2
\end{align*}$$

# Degenerate theory:

