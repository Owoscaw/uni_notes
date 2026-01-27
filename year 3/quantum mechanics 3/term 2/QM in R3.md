
# Generalisation to $\Re^3$:

Previously, we have explored quantum mechanics along the real line. We now move to generalise quantum mechanics to three spatial dimension. Our basic [[Operators and Measurement#Operator multiplication|operators]] here are $\hat{\underline{x}_i}$ and $\hat{\underline{p}_i}$, position and momentum in three dimensions instead of one. These operators still satisfy $$\Huge [\underline{\hat x}_i,\underline{\hat p}_i]=i\hbar\delta_{ij},\,\,[\underline{\hat x}_i,\underline{\hat x}_j]=0,\,\,[\underline{\hat p}_i,\underline{\hat p}_j]=0$$For specific computation, we still refer to their $x$-representation$$\Huge \underline{\hat x}_i\rightarrow\underline{x}_i,\,\,\underline{\hat p}_i\rightarrow-i\hbar\partial_i$$Our object of interest is still a wavefunction, however this is now a function of three variables, $|\psi\rangle=|\psi(x,y,z)\rangle$. Dynamics to do with $\psi$ are now fixed by solving $3$-dimensional versions of the [[Time evolution of QM states#Schrodinger equation motivation|time independent Schrodinger equation]]$$\Huge \hat H |\psi\rangle=E |\psi\rangle,\,\,\hat H=\frac{\underline{\hat p}^2}{2m}+\hat V(\underline{\hat x})$$which becomes, applying the $x$-representation$$\Huge -\frac{\hbar^2}{2m}(\partial_x^2+\partial_y^2+\partial_z^2)\psi(x,y,z)+V(x,y,z)\psi(x,y,z)=E\psi(x,y,z)$$Note that this is simply generalising the Schrodinger equation by introducing kinetic energy in $\Re^3$ instead of $\Re$ (this is what the first term represents). As before, $$\Huge|\psi(x,y,z)|^2d\underline{x}$$represents the probability to find a particle in the volume $d\underline{x}$ around the point $(x,y,z)$. The particle has to be somewhere in space, so we still get$$\Huge\iiint_{\Re^3}|\psi(x,y,z)|^2d\underline{x}=1$$Note that if a particle is localised in some region, i.e. a box with infinite potential walls, then the region of integration can be taken to be said region.

# Quantum angular momentum:

Before interpreting angular momentum in a quantum mechanical light, let us first recall the classical definition of angular momentum $\underline{L}$. If a classical particle with velocity $\underline{v}$ and momentum $\underline{p}$ moves along some path, it carries angular momentum $\underline{L}$ with respect to some origin$$\Huge \underline{L}=\underline{r}\times\underline{p}\iff\begin{cases}L_x=yp_z-zp_y \\
L_y=zp_x-xp_y \\
L_z=xp_y-yp_x\end{cases}\iff L_i=\epsilon_{ijk}x_jp_k$$In the quantum case, each $L_i$ become operators $\hat L_i$ using the [[Generalisation to infinite dimensional Hilbert spaces#Angular momentum and correspondence|correspondence principle]]$$\Huge x_i\rightarrow\hat x_i,\,\,p_i\rightarrow\hat p_i\rightarrow-i\hbar\partial_i$$and hence we have$$\Huge \hat L_i=\epsilon_{ijk}\hat x_j\hat p_k$$Note that in classical mechanics, the components of $\underline{L}$ can be any three real numbers, we ask what restrictions on these components are applied in quantum mechanic. For a free particle in no potential, $\hat x,\hat p$ can take any real number as in classical mechanics, however we are interested in $\hat L$. We ask of the allowed eigenvalues of the $\hat L_i$ operators. There are no restrictions on the eigenvalues of the $\hat x,\hat p$ operators. To explore this, we first note the following properties of $\hat L_i$:
> $[\hat L_i,\hat L_j]=i\hbar\epsilon_{ijk}\hat L_k$, which can be proven by expanding using the commutator definition. This means that each $\hat L_i$ does not commute with the next.
> $\implies$ Since each operator does not commute, they cannot be diagonalised simultaneously.
> $\implies$ The particle cannot have definite value for two different components of angular momentum.
> $[\hat L^2,\hat L_i]=[\hat L_x^2+\hat L_y^2+\hat L_z^2,\hat L_i]=0$

Therefore we see it is not possible for a particle to have definite values of $\underline{\hat L}$ at the same time. It is possible for a particle to be in a state which is simultaneously an eigenstate of total angular momentum $\hat L^2$ and one of the components $\hat L_i$ (this is what the last property implies). An eigenstate of each $\hat p_i$ is given by$$\Huge \psi_{p_xp_yp_z}=e^{i(p_xx+p_yy+p_zz)}$$
Hence for angular momentum, all we can do is find simultaneous eigenstates of $\hat L^2$ and one $\hat L_i$:$$\Huge\begin{align*}
\hat L^2 |\lambda,m\rangle&=\lambda |\lambda,m\rangle\\
\hat L_i |\lambda,m\rangle&=m |\lambda,m\rangle
\end{align*}$$where $|\lambda,m\rangle$ denotes an eigenstate of both operators with eigenvalues $\lambda,m$ respectively and we set $\hbar=1$. So the question becomes, what conditions are imparted on $\lambda,m$ and the eigenstate $|\lambda,m\rangle$. First let us note that $\lambda$ and $m$ are not independent, in fact it is obvious that $\sqrt\lambda\geq m$ as $m$ itself would be a length in the vector $|\underline{L}|=\sqrt{\lambda}$. 

In the quantum mechanical case, we can find a restriction on the eigenvalues:$$\Huge\begin{align*}
\langle\hat L^2-\hat L_z^2\rangle&=\langle \lambda,m|\hat L^2-\hat L_z^2 |\lambda,m\rangle\\
&=(\lambda-m^2) \langle \lambda,m|\lambda,m\rangle\\
&=\langle \lambda,m|\hat L_x^2+\hat L_y^2 |\lambda,m\rangle\geq0\\
\implies\lambda&\geq m^2
\end{align*}$$Therefore there is a maximal value that $\hat L_z$ can have, which we denote with $l\neq\lambda$$$\Huge -l\leq m\leq l$$
In order to determine $\lambda,m$ and $|\lambda,m\rangle$, we need the [[Quantum S.H.O.#Ladder operators|raising/lowering]] operators$$\Huge \hat L_{\pm}=\hat L_x\pm i\hat L_y\implies\hat L_+^*=\hat L_-$$which has the properties:$$\Huge\begin{align*}
[\hat L_z,\hat L_\pm]&=\pm\hat L_\pm\\
[\hat L_+,\hat L_-]&=2\hat L_z\\
[\hat L^2,\hat L_\pm]&=0
\end{align*}$$
Consider acting with $\hat L_z$ on the eigenstate after acting with $\hat L_+$:$$\Huge\begin{align*}
\hat L_z(\hat L_+ |\lambda,m\rangle)&=(L_+\hat L_z+\hat L_+)|\lambda,m\rangle\\
&=(m\hat L_++\hat L_+)|\lambda,m\rangle\\
&=(m+1)\hat L_+ |\lambda,m\rangle
\end{align*}$$That is, $\hat L_+$ raises the value of $m$ by $1$:$$\Huge \hat L_+ |\lambda,m\rangle=A |\lambda,m+1\rangle$$and similarly$$\Huge \hat L_- |\lambda,m\rangle=B |\lambda,m-1\rangle$$To gain some insight using this, consider:$$\Huge\begin{align*}
\hat L_-\hat L_+&=(\hat L_x-i\hat L_y)(\hat L_x+i\hat L_y)\\
&=\hat L_x^2+\hat L_y^2+i[\hat L_x,\hat L_y]\\
&=\hat L_x^2+\hat L_y^2-\hat L_z\\
&=\hat L^2-\hat L_z^2-\hat L_z
\end{align*}$$Now consider applying this to the state with maximal $m_\text{max}=l$:$$\Huge\begin{align*}
\hat L_-\hat L_+ |\lambda,l\rangle&=0\text{ as }l\text{ is maximal}\\
(\hat L^2-\hat L_z^2-\hat L_z) |\lambda,l\rangle&=\\
(\lambda-l^2-l) |\lambda,l\rangle&=\\
\implies\lambda&=l(l+1)
\end{align*}$$By convention, we write $l$ instead of the quantum number $\lambda$ as $\lambda$ is dependent on $m$ in this way.$$\Huge |\lambda=l(l+1),m\rangle\rightarrow |l,m\rangle,\,\,\hat L^2 |l,m\rangle=l(l+1)|l,m\rangle$$So we now investigate the allowed values of $m$. We have seen that for a given total angular momentum $l$, the allowed values of the $z$-component are$$\large |l,-l\rangle\to_{\hat L_+}\dots\rightarrow_{\hat L_+} |l,m-1\rangle\to_{\hat L_+}|l,m\rangle\rightarrow_{\hat L_+}|l,m+1\rangle\to_{\hat L_+}\dots\rightarrow_{\hat L_+} |l,l\rangle$$so then $m$ takes values in $\{-l,\dots,l\}$ for a total of $2l+1$ states. Note that this is not always the case, for example the [[Quantum S.H.O.#Number operator and ground state|quantum SHO]] has infinite states as $n\to\infty$. 

Hence we see that $\hat L_z$ has a quantised spectrum, bounded from the top and bottom by the total value of $\underline{L}$. 

## Summary:
So far, we have determined restrictions on $\lambda,m$ eigenvalues:
> $\hat L^2 |\lambda,m\rangle=\lambda |\lambda,m\rangle$ allowed us to figure out $\hat L^2|l,m\rangle=l(l+1)|l,m\rangle$ where $\lambda=l(l+1)$ and we switched notation.
> $\hat L_z |\lambda,m\rangle=m |\lambda,m\rangle$ allowed us to find $\hat L_z |l,m\rangle=m |l,m\rangle$.
> Then for given total momentum $l$ we found the allowed values for $\hat L_z$ to be$$\Huge m\in(-l,-l+1,\dots,l-1,l)$$
> We introduces $\hat L_\pm$ operators to build the $|l,m\rangle$ eigenstates.

It remains to find the constants we introduced in our raising/lowering operators:$$\Huge\begin{align*}
\hat L_+ |l,m\rangle&=A |l,m+1\rangle\\
\hat L_- |l,m\rangle&=B |l,m-1\rangle
\end{align*}$$To do this, we take the conjugate expression:$$\Huge\begin{align*}
(\hat L_+ |l,m\rangle)^\dagger&= \langle l,m|\hat L_-\\
&=(A |l,m+1\rangle)^\dagger\\
&= \langle l,m+1|A
\end{align*}$$and now take the square:$$\Huge\begin{align*}
|\hat L_+|l,m\rangle|^2&=(\hat L_+ |l,m\rangle)^\dagger(\hat L^+ |l,m\rangle)\\
&=\langle l,m|\hat L_-\hat L_+ |l,m\rangle=A^2 \langle l,m|l,m\rangle=A^2\\
&= \langle l,m|\hat L^2-\hat L_z^2-\hat L_z |l,m\rangle\\
&=(l^2-m^2-m)\\
\implies A&=\sqrt{l(l+1)-m(m+1)}
\end{align*}$$Doing this process for the $\hat L_-$ operator gives a similar result:$$\Huge\implies B=\sqrt{l(l+1)-m(m-1)}$$Hence our operators take form:$$\Huge\begin{align*}
\hat L_+ |l,m\rangle&=\sqrt{l(l+1)-m(m+1)}|l,m+1\rangle\\
\hat L_- |l,m\rangle&=\sqrt{l(l+1)-m(m-1)}|l,,m-1\rangle
\end{align*}$$
## Example:
Let us investigate a free particle with total angular momentum $l=1$:
> First, we define the Hilbert space of allowed states for our particle as the span of the following eigenvectors:$$\Huge\mathcal{H}_{l=1}=\text{span}\left\{|1,m=1\rangle=\begin{pmatrix}1 \\ 0 \\ 0\end{pmatrix},|1,0\rangle=\begin{pmatrix}0 \\ 1 \\ 0\end{pmatrix},|1,-1\rangle=\begin{pmatrix}0 \\ 0 \\ 1\end{pmatrix}\right\}$$This exactly satisfies our restriction for $m\in\{-l,\dots,l\}$ with $l=1$.
> We can find a representation of angular momentum in each axis in this space:$$\Huge \begin{align*}
\hat L_z |l,m\rangle&=m |l,m\rangle\\
\implies\hat L_z |1,1\rangle=1 |1,1\rangle,\,\,\hat L_z |1,0\rangle&=0 |1,0\rangle,\,\,\hat L_z |1,-1\rangle=-1 |1,-1\rangle\\
\implies \hat L_z&=\begin{pmatrix}1 & 0 & 0\\
0 & 0 & 0\\
 0 & 0 & -1\end{pmatrix}
\end{align*}$$To find each $\hat L_x,\hat L_y$ we can use the raising/lowering operator using the identity$$\Huge\hat L_\pm |l,m\rangle=\sqrt{l(l+1)-m(m\pm1)}|l,m\pm1\rangle$$So we compute$$\Huge\begin{align*}
\hat L_+ |1,1\rangle=0,\,\,\hat L_+ |1,0\rangle&=\sqrt 2 |1,1\,\,\,\hat L_+ |1,-1\rangle\sqrt 2 |1,0\rangle\\
\implies \hat L_+&=\begin{pmatrix}0 & \sqrt 2 & 0\\
0 & 0 & \sqrt 2\\
0 & 0 & 0\end{pmatrix}\\
\implies \hat L_-=(\hat L_+)^\dagger
&=\begin{pmatrix}0 & 0 & 0\\
\sqrt 2 & 0 & 0\\
0 & \sqrt 2 & 0\end{pmatrix}\end{align*}$$And hence we have:$$\Huge\begin{align*}
\hat L_x&=\frac{1}{2}(\hat L_++\hat L_-)=\frac{1}{2}\begin{pmatrix}0 & \sqrt 2 & 0\\
\sqrt 2 & 0 & \sqrt 2\\
0 & \sqrt 2 & 0\end{pmatrix}\\
\hat L_y&=\frac{1}{2i}(\hat L_+-\hat L_-)=-\frac{i}{2}\begin{pmatrix}0 & \sqrt 2 & 0\\
-\sqrt 2 & 0 & \sqrt 2\\
0 & -\sqrt 2 & 0\end{pmatrix}
\end{align*}$$

# Eigenfunctions of angular momentum:

We have found$$\Huge\begin{align*}
\hat L^2|l,m\rangle&=l(l+1) |l,m\rangle\\
L_z |l,m\rangle&=m |l,m\rangle
\end{align*}$$and that for a given total angular momentum $\lambda=l(l+1)$, allowed values of $m$ (the $z$-projection) are discretised to the set $\{-l,\dots,l\}$, making the eigenstates$$\Huge \{|l,-l\rangle,|l,-l+1\rangle,\dots, |l,l-1\rangle, |l,l\rangle\}$$We also found the specific forms of our operators $\hat L_\pm$ that helped us construct the whole spectrum$$\Huge \hat L_\pm |l,m\rangle=\sqrt{l(l+1)-m(m\pm 1)} |l,m\pm 1\rangle$$We now wish to find the explicit form of the $|l,m\rangle$ vector, that is the $x$-representation of $|l,m\rangle$. It is natural to work in spherical coordinates with$$\Huge\begin{align*}
x&=r\sin\theta\cos\varphi\\
y&=r\sin\theta\sin\varphi\\
z&=r\cos\theta\\
\underline{r}&=(r,\theta,\varphi)
\end{align*}$$So the question then becomes, what is the explicit form of$$\Huge \langle \underline{r}|l,m\rangle=\psi_{l,m}(r,\theta,\varphi)$$
To do this, we must first find the forms of the $\hat L_z,\hat L^2$ operators in spherical coordinates:$$\Huge\hat L_z\rightarrow\hat L_z=-i\left(x\frac{\partial }{\partial y}-y\frac{\partial }{\partial x}\right)=i\frac{\partial }{\partial \varphi}$$hence we have$$\Huge\hat L_z |l,m\rangle=m |l,m\rangle\rightarrow -i\frac{\partial }{\partial \varphi}\psi_{l,m}(r,\theta,\varphi)=m\psi_{l,m}(r,\theta,\varphi)$$Note that this is simple the operation of multiplying to the left by $\langle \underline{r}|$. Similarly$$\Huge\hat L^2\rightarrow\hat L^2=\left(-\frac{1}{\sin\theta}\frac{\partial }{\partial \theta}\left(\sin\theta\frac{\partial }{\partial \theta}\right)-\frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2}\right)$$and hence$$\ \hat L^2 |l,m\rangle=l(l+1) |l,m\rangle\rightarrow\left(-\frac{1}{\sin\theta}\frac{\partial }{\partial \theta}\left(\sin\theta\frac{\partial }{\partial \theta}\right)-\frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2}\right)\psi_{l,m}(r,\theta,\varphi)=l(l+1)\psi_{l,m}(r,\theta,\varphi)$$So the problem becomes solving these two equations for $\psi_{l,m}$. To do this we need the ansatz:
> We split variables in the following way$$\Huge\psi_{l,m}(r,\theta,\varphi)=R(r)\eta_{l,m}(\theta)\Phi_m(\varphi)$$where $R(r)$ is called the radial function, and the rest of the terms (that depend on $l,m$!) the angular part. 

Plugging these into our equations shows us that we have no condition on $R(r)$, as there is no $r$ dependency in any of our equations. For the angular part:
> The $\hat L_z$ equation dictates$$\Huge\begin{align*}
\hat L_z\psi_{l,m}(r,\theta,\varphi)&=\hat L_z(R(r)\eta_{l,m}(\theta)) \hat L_z\Phi_{m}(\varphi)\\
&=(R(r)\eta_{l,m}(\theta))\hat L_z\Phi_{m}(\varphi)\\
&=-(R(r)\eta_{l,m}(\theta))i\frac{\partial }{\partial \varphi}\Phi_{m}(\varphi)=m\Phi_m(\varphi)\\
\implies\Phi_m'(\varphi)&=im\Phi_m(\varphi)\\
\implies\Phi_m(\varphi)&=\frac{1}{\sqrt{2\pi}}e^{im\varphi}
\end{align*}$$where we chose an arbitrary constant. Note that if we shift $\varphi\rightarrow\varphi+2\pi$, we should be in the same point in space, meaning that $\psi$ should be unchanged. Due to the form of the $\Phi_m(\varphi)$, we must have that $m$ is an integer. This directly implies that $l$ is also an integer.
> The $\hat L^2$ equation dictates$$\large\begin{align*}
 \hat L^2\psi_{l,m}(r,\theta,\varphi)&=R(r)\hat L^2(\eta_{l,m}(\theta)\Phi_m(\varphi))\\
&=\left(-\frac{1}{\sin\theta}\frac{\partial }{\partial \theta}(\sin \theta\eta_{l,m}(\theta))\Phi_m\left(\varphi\right)-\frac{1}{\sin^2\theta}\Phi_m''(\varphi)\eta_{l,m}(\theta)\right)R(r)\\
&=l(l+1)R(r)\eta_{l,m}(\theta)\Phi_m(\varphi)
 \end{align*}$$multiplying through by $\sin^2\theta/\Phi\eta$ and separating $\theta,\varphi$ dependency gives$$\Huge -\sin\theta(\sin\theta\eta_{l,m}'(\theta))'\frac{1}{\eta_{l,m}(\theta)}-l(l+1)\sin^2\theta=\frac{\Phi_m''(\varphi)}{\Phi_m(\varphi)}$$
> Now using our form of $\Phi$ tells us that the RHS is equal to $-m$, so we rearrange to find$$\Huge \sin\theta\frac{\partial }{\partial \theta}(\sin \theta\,\eta_{l,m}'(\theta))+(l(l+1)\sin^2\theta-m^2)\eta_{l,m}(\theta)=0$$This is a known equation with solutions taking form of special functions called the associated [[Linear Differential Equations#Legendre's equation|Legendre polynomials]]. 
> Hence the full solution for $\psi_{l,m}$ is $$\Huge\psi_{l,m}(r,\theta,\varphi)=R(r)Y_{l,m}(\theta,\varphi)$$where$$\Huge Y_{l,m}(\theta,\varphi)=d_{l,m}e^{im\varphi}\eta_{l,m}(\theta)$$, $R(r)$ is fixed by the Schrodinger equation, $Y_{l,m}(\theta,\varphi)$ is fully fixed by symmetries $l,m$
, and $d_{l,m}$ is a constant (fixed by normalisation of $\psi_{l,m}$).

Normalising $\psi_{l,m}$ shows$$\large\iiint_{\Re^3}|\psi_{l,m}(r,\theta,\varphi)|^2d^3\underline{r}=1\iff\left(\int_0^\infty|R(r)|^2 dr\right)\left(\iint|Y_{l,m}|^2\sin\theta\,d\theta\,d\varphi\right)=1$$however, we normally require that each angular and radial function are separately normalised. If the angular part is normalised, then the associated $Y_{l,m}$ is known as a spherical harmonic.

We can find explicit formulations for $\psi$ by looking at different $l$ values:
> $l=0$ gives the angular function $Y_{0,0}(\theta,\varphi)=\frac{1}{\sqrt{4\pi}}$, corresponding to$$\Huge \psi_{0,0}(r,\theta,\varphi)=\frac{R(r)}{\sqrt{4\pi}}$$
> $l=1$ allows for $m\in\{-1,0,1\}$ and gives the angular functions $$\Huge Y_{1,0}(\theta,\varphi)=i\sqrt{\frac{3}{4\pi}}\cos\theta,\,\,Y_{1,\pm1}(\theta,\varphi)=\pm i\sqrt{\frac{3}{8\pi}}e^{\pm i\varphi}\sin\theta$$, the first of which corresponds to$$\Huge |\psi_{1,0}|^2\sim\cos^2\theta R^2(r)$$which has no $\varphi$ dependence, so is invariant under rotations around the $z$-axis. The other angular functions correspond to solutions invariant under rotations around the $x,y$-axis respectively:
>![[QM in R3 2026-01-27 18.47.56.excalidraw]]