
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

When we have a degenerate spectrum, we must employ a different method. First we look at twofold degeneracy:

## Twofold degeneracy:
We assume that the unperturbed system $\hat H^{(0)}$ has two states $\psi_a^{(0)}\neq\psi_b^{(0)}$ such that they have identical energies:$$\Huge \hat H^{(0)}|\psi_a^{(0)}\rangle=E^{(0)}|\psi_a^{(0)}\rangle,\,\,\hat H^{(0)}|\psi_b^{(0)}\rangle=E^{(0)}|\psi_b^{(0)}\rangle,\,\,\langle \psi_a^{(0)}|\psi_b^{(0)}\rangle=0$$And hence for $\alpha,\beta\in\Re$:$$\Huge \hat H^{(0)}(\alpha |\psi_a^{(0)}\rangle+\beta |\psi_b^{(0)}\rangle)=E^{(0)}(\alpha |\psi_a^{(0)}\rangle+\beta |\psi_b^{(0)}\rangle)$$When we add a perturbation $\hat H^{(0)}+\lambda\hat H'$ for a state that is a linear combination of degenerate eigenstates, the state splits into non-degenerate states of the perturbed system. One of these states will have higher energy, and one will have lower energy. Note that these states will be eigenstates of both $\hat H^{(0)}$ and $\hat H^{(0)}+\lambda\hat H'$.![[Perturbation theory 2026-05-11 12.37.17.excalidraw]]As $\lambda\to0$ we expect the low eigenstate to "connect" to $|2\rangle$ and visa versa for the high state. The problem then reduces to finding the form of these "good" states $|1\rangle,|2\rangle$ such that:
> $|1\rangle,|2\rangle$ are in the eigenspace of $\hat H^{(0)}$
> In the limit $\lambda\to0$, $|\text{high}\rangle\to|1\rangle$ and $|\text{low}\rangle\to |2\rangle$

To find these states, let us denote eigenstates of $\hat H^{(0)}+\lambda\hat H'=\hat H$ by $|\psi\rangle$:$$\Huge \hat H |\psi(\lambda)\rangle=E(\lambda)|\psi(\lambda)\rangle$$Notice how we have written $\psi$ and $E$ as functions of $\lambda$, so we can take an expansion in powers of $\lambda$:$$\Huge\begin{align*}
E&=E^{(0)}+\lambda E^{(1)}+\lambda^2E^{(2)}+\dots\\
|\psi\rangle&=|\psi^{(0)}\rangle+\lambda |\psi^{(1)}\rangle+\lambda^2 |\psi^{(2)}\rangle+\dots
\end{align*}$$Note that as $\lambda\to0$ it follows that $|\psi^{(0)}\rangle$ will connect to either $|1\rangle$ or $|2\rangle$. Using these forms in our eigenvalue problem gives:$$\Huge\begin{align*}
\hat H |\psi\rangle&=\hat H^{(0)}|\psi^{(0)}\rangle+\lambda(\hat H'|\psi^{(0)}\rangle+\hat H^{(0)}|\psi^{(1)}\rangle)+\dots\\
E |\psi\rangle&=E^{(0)}|\psi^{(0)}\rangle+\lambda(E^{(1)}|\psi^{(0)}\rangle+E^{(0)}|\psi^{(1)}\rangle)+\dots
\end{align*}$$Here, the first terms in each expansion cancel out and so we get at order $\lambda$:$$\Huge\hat H^{(0)}|\psi^{(1)}\rangle+\hat H'|\psi^{(0)}\rangle=E^{(1)}|\psi^{(0)}\rangle+E^{(0)}|\psi^{(1)}\rangle$$We now use the fact that eigenstates of $\hat H^{(0)}$ can be written as a linear combination of the basis eigenstates $\psi_a^{(0)}$ and $\psi_b^{(0)}$:$$\large\begin{align*}
\hat H^{(0)}|\psi^{(1)}\rangle+\hat H'(\alpha |\psi_a^{(0)}\rangle+\beta |\psi_b^{(0)}\rangle)=E^{(0)}
|\psi^{(1)}\rangle+E^{(1)}(\alpha |\psi_a^{(0)}\rangle+\beta |\psi_b^{(0)}\rangle)\end{align*}$$Now we act with the conjugates $\langle \psi_a^{(0)}|$ and $\langle \psi_b^{(0)}|$ to get:$$\Huge\begin{align*}
LHS&=\langle \psi_a^{(0)}|\hat H^{(0)}|\psi^{(1)}\rangle+\alpha \langle \psi_a^{(0)}|\hat H'|\psi_a^{(0)}\rangle+\beta \langle \psi_a^{(0)}|\hat H'|\psi_b^{(0)}\rangle\\
RHS&=E^{(0)} \langle \psi_a^{(0)}|\psi^{(1)}\rangle+\alpha E^{(1)}\langle \psi_a^{(0)}|\psi_a^{(0)}\rangle+\beta E^{(1)}\langle \psi_a^{(0)}|\psi_b^{(0)}\rangle\\
\implies&\alpha H'_{aa}+\beta H'_{ab}=\alpha E^{(1)}
\end{align*}$$Where $\hat H'_{aa}$ and $\hat H'_{ab}$ are the last two terms on the LHS. Similarly by applying the other basis state we find that:$$\Huge \alpha H'_{ba}+\beta H'_{bb}=\beta E^{(1)}$$Noting that these are essentially matrix elements, we can write this as:$$\Huge \begin{pmatrix}H'_{aa} & H'_{ab} \\ H'_{ba} & H'_{bb}\end{pmatrix}\begin{pmatrix}\alpha \\ \beta\end{pmatrix}=E^{(1)}\begin{pmatrix}\alpha \\ \beta\end{pmatrix},\,\,H'_{ij}=\langle \psi_j^{(0)}|\hat H' |\psi_i^{(0)}\rangle$$Therefore the problem of finding the first order corrections to energy, as well as the unperturbed states $|1\rangle,|2\rangle$, reduces to the problem of finding eigenvalues and vectors of the matrix $\hat H'$ written in the basis $\{|\psi_a^{(0)}\rangle,|\psi_b^{(0)}\rangle\}$ (i.e. the eigenstates of the unperturbed system).

Lets do this!$$\Huge\begin{align*}
\det(H'&-E^{(1)}I)=0\iff\det\begin{pmatrix}H'_{aa}-E^{(1)} & H'_{ab}\\
H'_{ba} & H'_{bb}-E^{(1)}\end{pmatrix}=0\\
\implies E^{(1)}&=\frac{1}{2}\left(H'_{aa}+H'_{bb}\pm\sqrt{(H'_{aa}+H'_{bb})^2-4(H'_{aa}H'_{bb}-|H'_{ab}|^2)}\right)\\
E^{(1)}_\text{high}&=E_1^{(1)},\,\,E_\text{low}^{(1)}=E_2^{(1)}
\end{align*}$$This is where the difference in energies comes from, with the higher energy associated with the positive sqrt branch. We can now find the states $|1\rangle,|2\rangle$ by finding the associated eigenvectors of this matrix.

Note that if $\hat H'$ is already diagonal, all of this reduces to the non degenerate case in each direction.

## N-fold degeneracy:
For systems with higher orders of degeneracy, we would not like to have to find eigenvalues/vectors and diagonalise a large matrix. To find a workaround to this, we first need the following theorem:

Assume $\hat A$ is Hermitian,$$\Huge [\hat H^{(0)},\hat A]=[\hat H',\hat A]=0$$, $|\psi_a^{(0)}\rangle$ and $|\psi_b^{(0)}\rangle$ are degenerate eigenstates of $\hat H^{(0)}$, and that they are eigenstates of $\hat A$ with different eigenvalues:$$\Huge \hat A |\psi_a^{(0)}\rangle=\alpha |\psi_a^{(0)}\rangle,\,\,\hat A |\psi_b^{(0)}\rangle=\beta |\psi_b^{(0)}\rangle$$If all this holds, then these degenerate eigenstates are the same as the "good" starting states for the perturbation. The physical context of this theorem is that we find a commuting operator that can distinguish between these eigenstates, while the Hamiltonian could not (as they are degenerate).
## Summary:
If $\beta=\{|\psi_1^{(0)}\rangle,\dots,|\psi_q^{(0)}\rangle\}$ are $q$ eigenstates of $\hat H^{(0)}$ with shared energy $E^{(0)}$, in order to find the "good" states and connections to energy we must:
> Write $\hat H'$ in the basis $\beta$, giving a $q\times q$ matrix
> Find eigenvalues and eigenvectors of this matrix

## $3$-fold degeneracy example:
Consider the unperturbed system of an empty box:$$\Huge V(x)=\begin{cases}0 & 0<x<a,\,\,0<y<a,\,\,0<z<a \\
\infty & \text{otherwise}\end{cases}$$First we find the non-perturbed eigenstates and associated energies using the ansatz $\psi=\psi_x\psi_y\psi_z$, making the Schrodinger equation:$$\Huge\begin{align*}
-\frac{1}{2m}\left(\frac{\partial^2 }{\partial x^2}+\frac{\partial^2}{\partial y^2}+\frac{\partial^2}{\partial z^2}\right)\psi^{(0)}(x,y,z)&=E^{(0)}\psi(x,y,z)\\
\implies-\frac{1}{2m}\left(\frac{\psi_x''(x)}{\psi_x(x)}+\frac{\psi_y''(y)}{\psi_y(y)}+\frac{\psi_z''(z)}{\psi_z(z)}\right)&=E^{(0)}
\end{align*}$$Since each LHS term depends on a different variable, each term must be equal to some constant $E_x^{(0)},E_y^{(0)},E_z^{(0)}$ such that they sum to $E^{(0)}$. Therefore we get the equations:$$\Huge \frac{\psi_x''}{\psi_x}=E_x^{(0)},\,\,\frac{\psi_y''}{\psi_y}=E_y^{(0)},\,\,\frac{\psi_z''}{\psi_z}=E_z^{(0)}$$These have solutions given by $$\Huge \psi_{x_i}=\alpha_{x_i}\sin(p_{x_i}x_i)+\beta_{x_i}\cos(p_{x_i}x_i)$$where $p_{x_i}$ satisfy:$$\Huge \sum_{n=1}^3\frac{p_{x_n}^2}{2m}=E^{(0)}$$For simplicity we impose boundary conditions on only the $x$ direction:$$\Huge\begin{align*}
\psi(0,y,z)&=\psi_x(0)\psi_y(y)\psi_z(z)=0\implies\beta_{x}=0\\
\implies\psi_x(x)&=\alpha_x\sin(p_xx)\\
\psi(a,y,z)&=\psi_x(a)\psi_y(y)\psi_z(z)=0\implies p_xa=n_x\pi\\
\implies p_x&=\frac{n_x\pi}{a}\\
\implies\psi_x^{n_x}(x)&=\alpha_{n_x}\sin\left(\frac{n_x\pi}{a}x\right)
\end{align*}$$This makes the full wavefunction$$\Huge\Psi^{(0)}_{(n_x,n_y,n_z)}(x,y,z)=\alpha_{n_x,n_y,n_z}\sin\left(\frac{n_x\pi}{a}x\right)\sin\left(\frac{n_y\pi}{a}y\right)\sin\left(\frac{n_z\pi}{a}z\right)$$with associated energy:$$\Huge E_{n_x,n_y,n_z}^{(0)}=\frac{\pi^2}{2a^2m^2}(n_x^2+n_y^2+n_z^2)$$Note that the normalisation constant $\alpha$ can be fixed by integrating over the box.

The ground state must be $(1,1,1)$ since each $n_{x_i}\neq0$. This makes the ground state energy:$$\Huge E_{(1,1,1)}^{(0)}=\frac{3}{2}\frac{\pi^2}{m^2a^2}$$For the first excited state we find a $3$-fold degeneracy:$$\Huge E_{(2,1,1)}^{(0)}=E_{(1,2,1)}^{(0)}=E_{(1,1,2)}^{(0)}=3\frac{\pi^2}{a^2m^2}$$
Now let us perturb the system with the Hamiltonian$$\Huge H'=\begin{cases}V_* & 0<x<a/2,\,\,0<y<a/2 \\
0 & \text{otherwise}\end{cases}$$with $V_*<\infty$ so that it is a "semi-permeable" region.