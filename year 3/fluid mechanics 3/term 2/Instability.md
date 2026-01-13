
We move on to generalise the [[Water waves|water wave]] analysis studied previously. We saw that there was an equilibrium state which produced oscillations about itself when perturbed. As the resulting motion didn't grow, we called the equilibrium "stable". This state was stable to linear perturbations, so we call it linearly stable.

We aim to consider different initial states, in which we have different kinds of stability:![[Instability 2026-01-13 21.10.47.excalidraw]]
Here, the red ball is stable to both small and large perturbations, it will oscillate back and forth in it's potential well. If there is friction, it will eventually lose energy and find equilibrium again. This is an example of a linearly and nonlinearly stable state.

The blue ball is unstable to both small and large perturbations, either way the ball will lose potential energy to gain kinetic energy.

The green ball is stable to small perturbations, but unstable to large ones. We say that it is linearly stable, but nonlinearly unstable. We proceed by studying linear stability.

# The Rayleigh-Taylor instability:

We now observe an instability that occurs at an interface between two fluids of different densities. We suppose that the two fluids are [[Kinematics of Fluids#Incompressibility|incompressible]] and irrotational with initial density:$$\Huge \rho(x,z,0)=\begin{cases}\rho_1&z>0 \\
\rho_2&z<0\end{cases}$$with downwards gravitational force:![[Instability 2026-01-13 21.17.56.excalidraw]]Note that this is simply a generalisation of the water waves analysis, with a second fluid above the interface $z=\eta(x,t)$. The RHS picture shows the system after perturbation, if the system is stable then we should see that $\eta$ takes the form of a wave. If not, then $\eta$ will grow exponentially and the system is unstable.

## Governing equations:
> Potential flow for both fluids: Assuming irrotational flow, we have $\underline{u}_1=\underline{\nabla}\phi_1$ and $\underline{u}_2=\underline{\nabla}\phi_2$ with:$$\Huge\begin{cases}\underline{\nabla}^2\phi_1=0&z>\eta \\
\underline{\nabla}^2\phi_2=0&z<\eta\end{cases}$$
> No motion far away from the interface: We assume:$$\Huge\begin{align*}
\underline{u}_1&\to\underline{0}\implies\phi_1\to0,\,\,z\to\infty\\
\underline{u}_2&\to\underline{0}\implies\phi_2\to0,\,\,z\to-\infty
\end{align*}$$
> No flow through the interface: The kinematic BC holds at the interface, so:$$\Huge \frac{\partial \phi_1}{\partial z}=\frac{D\eta}{Dt}=\frac{\partial \phi_2}{\partial z},\,\,z=\eta(x,t)$$
> Continuous pressure at the interface: [[Dynamics of ideal fluids#Bernoulli's principle|Bernoulli's principle]] for unsteady potential flow implies:$$\Huge \frac{\partial \phi}{\partial t}+\frac{p}{\rho_0}+\frac{1}{2}|\underline{\nabla}\phi|^2+gz=0$$throughout the fluid. We do not assume that pressure is constant at the interface, instead we assume its continuity. We then rearrange for $p$ below and above the interface:$$\Huge\begin{align*}

\end{align*}$$