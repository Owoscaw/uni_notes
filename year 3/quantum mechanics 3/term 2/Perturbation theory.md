
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