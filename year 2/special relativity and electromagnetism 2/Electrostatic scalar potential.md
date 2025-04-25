# Scalar potential:

In general solutions, symmetry does not always lead to an electric that is curl free, so the condition $\underline{\nabla}\times\underline E=\underline 0$ has to be dealt with directly. We choose any function $\phi$ and set:$$\Huge \underline E=-\underline{\nabla}\phi$$which solves the equation, the proof is:$$\Huge \underline{\nabla}\times\underline E=-\underline{\nabla}\times\underline{\nabla}\phi=\underline 0$$using the fact that the curl of the gradient of any function vanishes. Such a function is called the electrostatic scalar potential. We now verify that [[Electrostatics#Gauss' law|Gauss' law]] remains satisfied:$$\Huge \nabla^2\phi=-\rho/\epsilon_0$$That is, the electrostatic scalar potential must satisfy the Poisson equation. This equation determines a unique $\phi$ for each $\rho$ up to the addition of a constant. We fix this constant by requiring that $\rho\to0$ as $r\to\infty$. Note that in a region of space where charge density vanishes ($\rho=0$) we see that scalar potential must satisfy the Laplace equation:$$\Huge \nabla^2\phi=0$$Such solutions are known as harmonic functions.

As an example, take a point charge $q$ at the origin, that is $\rho=q\delta(r)$:$$\Huge \nabla^2\phi=-q\delta(r)/\epsilon_0$$where $\delta$ is the [[Electromagnetism#Vector calculus and Dirac delta|Dirac delta]] function. We see that this reduces to the Laplace equation everywhere except $r=0$. Charge density is spherically symmetric so we take $\phi$ to be a function of $r$ only. Since we require that $\phi\to0$ as $r\to\infty$ then the simplest solution to try is $\phi=k/r$ for constant $k$:$$\Huge \begin{align}
\nabla^2\phi&=\partial_i\partial_i(kr^{-1})\\
&=-k\partial_i(x_ir^{-1}r^{-2})\\
&=-k\partial_i(x_ir^{-3})\\
&=-k((\partial_ix_i)r^{-3}-3x_ix_ir^{-1}r^{-4})\\
&=-k(\delta_{ii}r^{-3}-3r^{-3})\\
&=-k(3r^{-3}-3r^{-3})=0
\end{align}$$as required. This solves the equation for any $k$ at $r\neq0$ however we must find the correct value for this constant so that the solution correctly handles the Dirac delta function at the origin. To do this we must integrate the Poisson equation over the volume $V$ bounded by a [[Electromagnetism#Vector calculus and Dirac delta|Gaussian surface]] that is a sphere of radius $r$ at the origin:$$\Huge\begin{align}
\int_V\underline{\nabla}\cdot\underline{\nabla}\phi\,dV=-\frac{q}{\epsilon_0}\int_V\delta(r)\,dV=-\frac{q}{\epsilon_0}=\int_S\underline{\nabla}\phi\cdot\underline{dS}
\end{align}$$Now $\partial_i\phi=k\partial_ir^{-1}=-kx_ir^{-1}r^{-2}=-kx_ir^{-3}$ hence $\underline{\nabla}\phi=-kr^{-2}\underline{\hat{r}}$ which makes the integral:$$\large -\frac{q}{\epsilon_0}=-k\int_Sr^{-2}\underline{\hat{r}}\cdot\underline{dS}=-kr^{-2}\int_SdS=-kr^{-2}4\pi r^2=-4\pi k\implies k=\frac{q}{4\pi\epsilon_0}$$This makes the scalar potential for a point charge $q$ at the origin:$$\Huge\phi=\frac{q}{4\pi\epsilon_0r}$$with the electric field:$$\Huge \underline E=-\underline{\nabla}\phi=\frac{q\underline{\hat{r}}}{4\pi\epsilon_0r^2}$$

# Scalar potential of a [[Electrostatics#Electric dipoles|dipole]]:

As the Poisson equation $\nabla^2\phi=-\rho/\epsilon_0$ is linear in both $\rho$ and $\phi$ then the scalar potential of the sum of two charge densities is simply the sum of their individual scalar potentials. As an example, we can apply this to calculate the scalar potential of a dipole with dipole moment $\underline p$. For a charge $q$ at the origin and a charge $-q$ at $r=-h$ the scalar potential is:$$\Huge\begin{align}
\phi&=\frac{q}{4\pi\epsilon_0r}-\frac{q}{4\pi\epsilon_0|\underline r+\underline h|}\\
&=\frac{q}{4\pi\epsilon_0}(r^{-1}-|\underline r+\underline h|^{-1})\\
&=\frac{q}{4\pi\epsilon_0}(r^{-1}-(r^{-1}+\underline h\cdot\underline{\nabla}r^{-1}+\mathcal{O}(h)))\\
&=\frac{q}{4\pi\epsilon_0}(\underline h\cdot\underline{\hat{r}}r^{-2}+\mathcal{O}(h))
\end{align}$$Now taking the limit as $h\to0$ with the dipole moment $\underline p=q\underline h$ fixed gives the scalar potential of the dipole:$$\Huge \phi=\frac{\underline p\cdot\underline{\hat{r}}}{4\pi\epsilon_0r^2}=\frac{\underline p\cdot\underline r}{4\pi\epsilon_0r^{3}}$$Note that this scalar potential is not spherically symmetric.

# Multi-pole expansion:

Given an arbitrary charge density $\rho(\underline r)$ which we assume is localised around the origin so that it vanishes outside of some region $V$, it is possible to write a formal expression for the scalar potential in terms of a [[Surface and volume integrals#Volume integrals|volume integral]] over the region $V$. To do this, we first define [[Green's method#Green's function via delta function|Green's function]] $G(\underline r,\underline r')$ of the [[Index notation#Second derivatives|Laplacian]] to be the solution to:$$\Huge \nabla^2G(\underline r,\underline r')=\delta(\underline r-\underline r')$$Note that the Laplacian only differentiates with respect to coordinates associated with $\underline r$, not $\underline r'$ so this vector can be thought of as a parameter. If the Green's function is known, then the Poisson equation for the scalar potential with arbitrary source $$\Huge \nabla^2\phi(\underline r)=-\frac{\rho(\underline r)}{\epsilon_0}$$is solved by:$$\Huge \phi(\underline r)=-\frac{1}{\epsilon_0}\int_VG(\underline r,\underline r')\rho(\underline r')dV'$$where $dV'$ represents integration over the $\underline r'$ coordinate. This is proven as follows:$$\Huge\begin{align}
\nabla^2\phi(\underline r)&=-\frac{1}{\epsilon_0}\int_V\nabla^2G(\underline r,\underline r')\rho(\underline r')dV'\\
&=-\frac{1}{\epsilon_0}\int_V\delta(\underline r-\underline r')\rho(\underline r')dV'\\
&=-\frac{1}{\epsilon_0}(\rho(\underline r))
\end{align}$$which is the Poisson equation exactly. Here we used the fact that the Laplacian is independent of $\underline r'$ and so can be moved inside the integrand, as well as the definition of Green's function and the properties of the delta function.