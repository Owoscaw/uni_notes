
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
p_1&=-\left(\rho_1\frac{\partial \phi_1}{\partial t}+\frac{\rho_1}{2}|\underline{\nabla}\phi_1|^2+\rho_1gz\right)\\
p_2&=-\left(\rho_2\frac{\partial \phi_2}{\partial t}+\frac{\rho_2}{2}|\underline{\nabla}\phi_2|^2+\rho_2gz\right)
\end{align*}$$We then impose $p_1=p_2$ at the interface to give us the new dynamic boundary condition:$$\Huge\rho_1\frac{\partial \phi_1}{\partial t}+\frac{\rho_1}{2}|\underline{\nabla}\phi_1|^2+\rho_1g\eta=\rho_2\frac{\partial \phi_2}{\partial t}+\frac{\rho_2}{2}|\underline{\nabla}\phi_2|^2+\rho_2g\eta$$

## Linearisation:
Now we linearise the equations and consider small disturbances to the steady state $\eta=0$. This process is similar to our water waves analysis and we get:$$\Huge\begin{align*}
\underline{\nabla}^2\phi_1&=0&z>0\\
\underline{\nabla}^2\phi_2&=0&z<0\\
\phi_1,\phi_2&\to0&z\to\pm\infty\\
\frac{\partial \eta}{\partial t}&=\frac{\partial \phi_1}{\partial z}=\frac{\partial \phi_2}{\partial z}&z=0\\
\rho_1\frac{\partial \phi_1}{\partial t}+\rho_1g\eta&=\rho_2\frac{\partial \phi_2}{\partial t}+\rho_2g\eta&z=0
\end{align*}$$
## Solutions:
We now look for travelling wave solutions that are periodic in $x$:$$\Huge \phi_1(x,z,t)=Z_1(z)e^{i(kx-\omega t)}$$for the potential above the interface. Substituting this into our first linearised equation and using our limiting boundary condition gives:$$\Huge Z_1(z)=A_1e^{-kz}\implies\phi_1(x,z,t)=A_1e^{-kz}e^{i(kx-\omega t)}$$Below the interface, we need an ansatz that has the same $x$-dependence so that it will move in phase with the fluid above the interface. Therefore we try:$$\Huge \phi_2(x,z,t)=Z_2(z)e^{i(kx-\omega t)}$$then we apply the limiting boundary condition to get:$$\Huge \phi_2(x,z,t)=A_2e^{kz}e^{i(kx-\omega t)}$$
These two potentials obviously match at $z=0$ and are in phase, and will both decay away from the interface in both directions.

For the interface itself, we can rearrange the dynamic boundary condition for $\eta$. A faster approach is to spot that $\eta$ should have form:$$\Huge \eta(x,t)=\eta_0e^{i(kx-\omega t)}$$Substituting into the dynamic BC gives:$$\Huge -i\omega\eta_0=-kA_1=kA_2$$So we impose $A_1=-A_2=A$ and:$$\Huge \eta(x,t)=\frac{kA}{i\omega}e^{i(kx-\omega t)}$$
## Dispersion relation:
Finally, we substitute our expressions for the potential and the interface into our continuous pressure condition:$$\Huge\begin{align*}
-i\omega\rho_1A+\rho_1g\frac{kA}{i\omega}&=i\omega\rho_2A+\rho_2g\frac{kA}{i\omega}\\
\implies\omega^2&=\frac{\rho_2-\rho_1}{\rho_1+\rho_2}gk
\end{align*}$$This is the dispersion relation for linear waves at the interface. This shows the system will support travelling waves with phase speed $c=\omega/k$ given that $\rho_2>\rho_1$. That is to say, the system is stable if the lower fluid has greater density.

We saw that this relation for water waves in deep water is $\omega^2=gk$, so these new interface waves are the same was water waves with a modified wave speed. In fact when $\rho_1=0$ the dispersion relation reduces to exactly this.

If we force the denser fluid to be on top, $\rho_1>\rho_2$, then:$$\Huge\omega=\pm i\sigma,\,\,\sigma=\sqrt{\frac{\rho_1-\rho_2}{\rho_1+\rho_2}}gk$$We know that the interface height behaves like $\eta\sim e^{i\omega t}$. If $\omega$ is real, the perturbation will produce travelling waves. However in this case $\omega$ has some imaginary part, so the perturbation will exponentially decay or grow depending on the sign.

Taking this to be the case, the corresponding perturbations have form $\eta(x,t)\sim e^{\pm\sigma t}$ and will exhibit exponential growth. We call $\sigma$ the growth rate, this is the Rayleigh-Taylor instability.

In the full system, it is plausible that the nonlinear terms could inhibit the exponential growth, so we look at numerical solutions to the Euler equations to check:
> Taking $\rho_1=1,\rho_2=3$ the system is stable and the interface just oscillates at the frequency of perturbation.
> Taking $\rho_1=3,\rho_2=1$ the system is unstable and we can observe the Rayleigh-Taylor instability.![[density_normalized.gif]]Notice how disturbances develop at small scale first, as these scales will have the largest growth rate $\sigma$.

# The Kelvin-Helmholtz instability:

We now look at another instability with the same setup as before, however the fluids are now moving horizontally at different speeds. This fluid is being sheared, such shear layers form very frequently in our atmosphere and oceans. 

Generally, these layers have some finite thickness where flow changes from one speed to another. This will generate some finite vorticity, however we assume that the layer is concentrated to an interface (we allow for a discontinuity in speed). The interface therefore has infinite vorticity, called a vortex sheet. The flow is then given by:$$\Huge \underline{u}(x,z,0)=\begin{cases}U_1\hat{\underline{e}}_x&z>0 \\
U_2\hat{\underline{e}}_x&z<0\end{cases}$$for constants $U_1,U_2$. We assume both fluids are inviscid and incompressible. For simplicity we assume both flows have the same density $\rho=\rho_0$, which can be relaxed to give an even more complex dispersion relation.

Note that the interface is not initially stationary. Given that we are perturbing around the static equilibrium (constant $\phi$), it is convenient to work in a reference frame that imposes a stationary interface. We therefore shift to a moving reference frame at the average speed of the flow $1/2(U_1+U_2)$. In this frame, the interface appears stationary and:$$\Huge \underline{u}(x,z,0)=\begin{cases}U\hat{\underline{e}}_x&z>0 \\
-U\hat{\underline{e}}_x&z<0\end{cases}$$where $U=1/2(U_1-U_2)$.![[Instability 2026-01-15 18.50.54.excalidraw]]
## Governing equations:
Denoting the interface as $z=\eta(x,t)$ with $\eta(x,0)=0$ we get the following governing equations:
> Potential flow: We again assume that the perturbed flow is irrotational and incompressible:$$\Huge\begin{align*}
\underline{u}_1&=U\hat{\underline{e}}_x+\underline{\nabla}\phi_1\\
\underline{u}_2&=-U\hat{\underline{e}}_x+\underline{\nabla}\phi_2\\
\underline{\nabla}^2\phi_1&=0,\,\,z>\eta\\
\underline{\nabla}^2\phi_2&=0,\,\,z<\eta
\end{align*}$$
> Uniform flow away from the interface: We assume:$$\Huge\begin{align*}
\underline{u}_1\to U\hat{\underline{e}}_x&\implies\phi_1\to0,\,\,z\to\infty\\
\underline{u}_2\to U\hat{\underline{e}}_x&\implies\phi_2\to0,\,\,z\to-\infty
\end{align*}$$
> No flow through the surface at $z=\eta(x,t)$: The kinematic boundary condition is the same as before:$$\Huge\frac{\partial \phi_1}{\partial z}=\frac{D\eta}{Dt}=\frac{\partial \phi_2}{\partial z},\,\,z=\eta$$
> Continuous pressure at the interface: We need to apply Bernoulli's principle for unsteady potential flow and therefore must convert the velocity fields into potentials:$$\Huge \underline{u}_1=\underline{\nabla}(Ux+\phi_1),\,\,\underline{u}_2=\underline{\nabla}(-Ux+\phi_2)$$We proceed by applying the principle on these potentials:$$\Huge\begin{align*}
\frac{\partial }{\partial t}(Ux+\phi_1)+\frac{p_1}{\rho_0}+\frac{1}{2}|\underline{\nabla}(Ux+\phi_1)|^2+gz&=0&z>\eta\\
\frac{\partial }{\partial t}(-Ux+\phi_2)+\frac{p_2}{\rho_0}+\frac{1}{2}|\underline{\nabla}(-Ux+\phi_2)|^2+gz&=0&z<\eta
\end{align*}$$Again we impose equal pressure at the interface, so we rearrange to find:$$\large \rho_0\frac{\partial \phi_1}{\partial t}+\frac{\rho_0}{2}|U\hat{\underline{e}}_x+\underline{\nabla}\phi_1|^2+\rho_0g\eta=\rho_0\frac{\partial \phi_2}{\partial t}+\frac{\rho_2}{2}|-U\hat{\underline{e}}_x+\underline{\nabla}\phi_2|^2+\rho_0g\eta$$We expand the second terms of each side similarly:$$\Huge |U\hat{\underline{e}}_x+\underline{\nabla}\phi_1|^2=U^2+2U\frac{\partial \phi}{\partial x}+|\underline{\nabla}\phi_1|^2$$Which then gives us:$$\Huge \frac{\partial \phi_1}{\partial t}+\frac{U^2}{2}+U\frac{\partial \phi_1}{\partial x}+\frac{1}{2}|\underline{\nabla}\phi_1|^2=\frac{\partial \phi_2}{\partial t}+\frac{U^2}{2}-U\frac{\partial \phi_2}{\partial x}+\frac{1}{2}|\underline{\nabla}\phi_2|^2$$So our condition becomes:$$\Huge \frac{\partial \phi_1}{\partial t}+U\frac{\partial \phi_1}{\partial x}+\frac{1}{2}|\underline{\nabla}\phi_1|^2=\frac{\partial \phi_2}{\partial t}-U\frac{\partial \phi_2}{\partial x}+\frac{1}{2}|\underline{\nabla}\phi_2|^2$$

## Linearisation:
We must modify our linearisation as the kinematic boundary condition has been changed. As before we have:$$\Huge\begin{align*}
\underline{\nabla}^2\phi_1&=0&z>0\\
\underline{\nabla}^2\phi_2&=0&z<0
\end{align*}$$However now, the kinematic BC is:$$\Huge\begin{align*}
\frac{D\eta}{Dt}&=\frac{\partial \eta}{\partial t}+(\underline{u}_1\cdot\underline{\nabla})\eta\\
&=\frac{\partial \eta}{\partial t}+U\frac{\partial \eta}{\partial x}+\underline{\nabla}\phi\cdot\underline{\nabla}\eta
\end{align*}$$So the final term disappears in the linearisation, however the second term does not. Therefore our new linearised kinematic BC becomes:$$\Huge\begin{align*}
\frac{\partial \eta}{\partial t}&=\frac{\partial \phi_1}{\partial z}-U\frac{\partial \eta}{\partial x}&z=0\\
\frac{\partial \eta}{\partial t}&=\frac{\partial \phi_2}{\partial z}+U\frac{\partial \eta}{\partial x}&z=0
\end{align*}$$Linearising the dynamic BC then gives:$$\Huge \frac{\partial \phi_1}{\partial t}+U\frac{\partial \phi_1}{\partial x}=\frac{\partial \phi_2}{\partial t}-U\frac{\partial \phi_2}{\partial x},\,\,z=0$$
## Solutions:
As before, our system supports travelling wave potential solutions of the form:$$\Huge \phi_1(x,z,t)=A_1e^{-kz}e^{i(kx-\omega t)},\,\,\phi_2(x,z,t)=A_2e^{kz}e^{i(kx-\omega t)}$$Now we solve for the interface using our ansatz $\eta(x,t)=\eta_0e^{i(kx-\omega t)}$ in the modified kinematic BC:$$\Huge\begin{align*}
-i\omega\eta_0&=-kA_1-ik\eta_0U\\
-i\omega\eta_0&=kA_2+ik\eta_0U
\end{align*}$$so we have:$$\Huge A_1=i\eta_0\left(\frac{\omega}{k}-U\right),\,\,A_2=i\eta_0\left(-\frac{\omega}{k}-U\right)$$
## Dispersion relation:
Using our solutions in the dynamic BC gives us:$$\Huge\begin{align*}
-i\omega A_1+ikUA_1&=-i\omega A_2-ikUA_2\\
\implies A_1(\omega-kU)&=A_2(\omega+kU)\\
\implies\left(\frac{\omega}{k}-U\right)(\omega-Uk)&=\left(-\frac{\omega}{k}-U\right)(\omega+Uk)\\
\implies\omega^2+U^2k^2&=0
\end{align*}$$Therefore we have exponential growth/decay modes with:$$\Huge \omega=\pm i\sigma,\,\,\sigma=Uk$$This instability is known as the Kelvin-Helmholtz instability. We see that larger $U$ leads to larger $\sigma$ and that the largest wave numbers (highest $k$) grow the fastest. In practice, surface tension, viscosity, and density differences between the layers can counteract this growth factor.

Again we turn to the full nonlinear system to observe this behaviour. The discretised Euler equations are solved numerically with periodic side boundaries and a small perturbation to the initial condition. The instability breaks the vortex sheet up into discrete vortices:![[Kelvin-Helmholtz_Instability.gif]]


These examples demonstrate that we can gain a great deal of intuition from analysing the linear stability of fluid equilibria. This methodology gives us a tool to test other configurations, however we should always keep in mind the limitations of our assumptions. Proving stability/instability to one kind of perturbation does not necessarily mean the system is stable/unstable to other kinds of perturbations or when further physics are included.