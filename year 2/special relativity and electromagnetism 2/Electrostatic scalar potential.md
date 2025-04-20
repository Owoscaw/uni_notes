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
\end{align}$$Now $\partial_i\phi=k\partial_ir^{-1}=-kx_ir^{-1}$