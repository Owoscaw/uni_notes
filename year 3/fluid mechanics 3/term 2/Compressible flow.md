
So far we have considered [[Dynamics of ideal fluids#Incompressible Euler equations|incompressible fluids]], which is a good approximation for water and oil, but fails for gasses in most contexts. We will see that we gain sound waves and shocks from allowing fluid to be compressible.

Recall the continuity and momentum equations for an inviscid fluid:$$\Huge\begin{align*}
\frac{\partial \rho}{\partial t}+\underline{\nabla}\cdot(\rho\underline{u})&=0\\
\frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}&=-\frac{1}{\rho}\underline{\nabla}\rho+\underline{f}
\end{align*}$$If the fluid is compressible, then $\rho$ can vary in space and time. Now we have $5$ unknown functions but only $4$ governing equations. To close the system, we need another physical equation. We will achieve this by positing a dependence of pressure on density and/or temperature.

# Barotropic fluids:

A simpler, but useful, approximation is when pressure depends solely on density:$$\Huge p=P(\rho)$$Such fluids are known as barotropic.

## Conservation of energy:
Having made this assumption, we now need to check whether this still leads to physical flows. In particular, energy (of some form) should be conserved. For incompressible flows we saw that kinetic energy was conserved, however this will not be the case.

In the absence of a body force, energy $E$ is conserved as long as we allow kinetic energy to convert into internal energy $e$. The exact form of this is$$\Huge E=\int_V\rho\left(\frac{1}{2}|\underline{u}|^2+e(\rho)\right)dV,\,\,e(\rho)=\int_0^\rho\frac{P(\sigma)}{\sigma^2}d\sigma$$assuming that no fluid enters the control volume ($\underline{u}\cdot\underline{\hat{n}}=0$ on the boundary). We call $e(\rho)$ the internal energy density or specific internal energy.

Let us consider these forms by proving that $E$ is conserved. We consider each term separately$$\Huge\begin{align*}
\frac{d}{dt}\int_V\frac{1}{2}\rho|\underline{u}|^2dV&=\int_V\frac{1}{2}\frac{\partial }{\partial t}(\rho|\underline{u}|^2)dV\\
&=\int_V\left(\frac{1}{2}|\underline{u}|^2\frac{\partial \rho}{\partial t}+\rho\underline{u}\cdot\frac{\partial \underline{u}}{\partial t}\right)dV\\
&=\int_V\left(\frac{1}{2}|\underline{u}|^2\frac{\partial \rho}{\partial t}+\rho\underline{u}\cdot\left(-(\underline{u}\cdot\underline{\nabla})\underline{u}-\frac{1}{\rho}\underline{\nabla}P\right)\right)dV
\end{align*}$$We use the same trick for incompressible fluids and use the identity$$\Huge (\underline{u}\cdot\underline{\nabla})\underline{u}=(\underline{\nabla}\times\underline{u})\times\underline{u}+\frac{1}{2}\underline{\nabla}(|\underline{u}|^2)$$along with the observation that the cross product term disappears when dotted with $\underline{u}$$$\Huge \frac{d}{dt}\int_V\frac{1}{2}\rho|\underline{u}|^2dV=\int_V\left(\frac{1}{2}|\underline{u}|^2\frac{\partial \rho}{\partial t}-\rho\underline{u}\cdot\underline{\nabla}\left(\frac{1}{2}|\underline{u}|^2\right)-\underline{u}\cdot\underline{\nabla}P\right)dV$$we manipulate the middle term using $$\Huge \underline{A}\cdot\underline{\nabla}f=\underline{\nabla}\cdot(f\underline{A})-f\underline{\nabla}\cdot\underline{A}$$and then use the divergence theorem on the final term to get$$\large \frac{d}{dt}\int_V\frac{1}{2}\rho|\underline{u}|^2dV=\int_V\left(\frac{1}{2}|\underline{u}|^2\frac{\partial \rho}{\partial t}+\frac{1}{2}|\underline{u}|^2\underline{\nabla}\cdot(\rho\underline{u})-\underline{u}\cdot\underline{\nabla} P\right)dV-\int_S\frac{1}{2}|\underline{u}|^2\rho\underline{u}\cdot d\underline{S}$$The first two terms on the right form a multiple of the continuity equation and so disappear. The final term is integrating a multiple of $\underline{u}\cdot\underline{\hat{n}}$ around the boundary, however $\underline{u}\cdot\underline{\hat{n}}=0$ on the boundary, leaving$$\Huge \frac{d}{dt}\int_V\frac{1}{2}\rho|\underline{u}|^2dV=-\int_V\underline{u}\cdot\underline{\nabla}P\,dV$$We can interpret this as saying kinetic energy is converted away when the pressure forces ($-\underline{\nabla}P$) act directly against the velocity. Note that we have not used our barotropic fluid assumption yet.

Now we consider the internal energy term. From the chain rule we get$$\Huge \frac{\partial e}{\partial t}=\frac{de}{d\rho}\frac{\partial \rho}{\partial t}=\frac{P}{\rho^2}\frac{\partial \rho}{\partial t}$$and so$$\Huge\begin{align*}
\frac{d}{dt}\int_V\rho e\,dV&=\int_V\left(e\frac{\partial \rho}{\partial t}+\rho\frac{\partial e}{\partial t}\right)dV\\
&=\int_V\left(e+\frac{P}{\rho}\right)\frac{\partial \rho}{\partial t}dV\\
&=-\int_V\left(e+\frac{P}{\rho}\right)\underline{\nabla}\cdot(\rho\underline{u})dV\\
&=\int_V\rho\underline{u}\cdot\underline{\nabla}\left(e+\frac{P}{\rho}\right)dV-\int_S\left(e+\frac{P}{\rho}\right)\rho\underline{u}\cdot d\underline{S}\\
&=\int_V\rho\underline{u}\cdot\left(\frac{de}{d\rho}+\frac{P'(\rho)}{\rho}-\frac{P}{\rho^2}\right)\underline{\nabla}\rho\,dV\\
&=\int_V\rho\underline{u}\cdot\left(\frac{P}{\rho^2}+\frac{P'(\rho)}{\rho}-\frac{P}{\rho^2}\right)\underline{\nabla}\rho\,dV\\
&=\int_V\rho\underline{u}\cdot\frac{P'(\rho)}{\rho}\underline{\nabla}\rho\,dV\\
&=\int_V\underline{u}\cdot\underline{\nabla}P\,dV
\end{align*}$$which is equal and opposite to the equation we found for kinetic energy, proving total energy is conserved.

## Bernoulli's principle revised:
As we incompressible flows, we can find a conserved energy-related quantity along streamlines, generalising Bernoulli's principle.

Recall that we derived Bernoulli's principle by writing down the momentum equation for a conservative body force $\underline{f}=-\underline{\nabla}\Phi$$$\Huge \frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}=-\frac{1}{\rho}\underline{\nabla}p-\underline{\nabla}\Phi$$and using our favorite vector identity on the second term to write the whole RHS as a gradient. This was all well and good when $\rho$ was constant, however now it will be harder to write the pressure term as a gradient.

We introduce $h(\rho)$ so that the momentum equation becomes$$\Huge \frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}=-\underline{\nabla}h-\underline{\nabla}\Phi$$we then ask of the form of $h$$$\Huge\begin{align*}
\underline{\nabla}h(\rho)&=\frac{1}{\rho}\underline{\nabla}P(\rho)\\
\frac{dh}{d\rho}\underline{\nabla}\rho&=\frac{1}{\rho}\frac{dP}{d\rho}\underline{\nabla}\rho\\
\frac{dh}{d\rho}&=\frac{1}{\rho}\frac{dP}{d\rho}\implies h(\rho)=\int_0^\rho\frac{P'(\sigma)}{\sigma}d\sigma
\end{align*}$$and our previous method then works to generalise Bernoulli's principle, giving us the energy head$$\Huge H=h(\rho)+\frac{1}{2}|\underline{u}|^2+\Phi$$
## Thermodynamics:
A common model for pressure is$$\Huge P(\rho)=k\rho^\gamma$$which represents an ideal gas undergoing an adiabatic process (no heat added). The constant $\gamma$ is called the adiabatic index and depends on the number of degrees of freedom of the molecules making up the gas. Specifically, $\gamma=(n_\text{dof}+2)/n_\text{dof}$. Diatomic molecules have $n_\text{dof}=5$ ($3$ translational, $2$ rotational), so $\gamma\approx1.4$ for air. 

Furthermore, thermodynamics tells us that the entropy $S$ of an ideal gas satisfies$$\Huge S=c_V\log(P\rho^{-\gamma})+\text{constant}$$In the adiabatic ideal gas model, $P\rho^{-\gamma}$ is constant, and thus this assumption corresponds to assuming that no heat is transferred between fluid particles. That is to say, heating/cooling of a fluid region is purely through compression/expansion of the fluid.

Meanwhile, the internal energy density $e$ is related to temperature by$$\Huge e=\frac{c_VT}{\mu}$$where $c_V$ is the molar heat capacity at constant volume, and $\mu$ is the mass per mole of a substance. For an ideal gas, $c_V=\frac{1}{2}n_\text{dof}R$ where $R$ is the universal gas constant. If we combine this relation with the definition of $e$, we find that this is a generalisation of $pV=nRT$.

Consider a passenger jet flying through air. Assuming that air is an ideal gas, we ask how hot the nose of the jet liner gets. At the nose, there is a stagnation point in the flow and so $u_1=0$. Compared to a point above the fuselage and ignoring gravity, Bernoulli's principle dictates$$\Huge h_1=h_2+\frac{1}{2}u_2^2$$We know that the temperature of air at cruising altitude is about $-50$ degrees. For an ideal gas$$\Huge h(\rho)=\int_0^\rho\frac{P'(\sigma)}{\sigma}d\sigma=\int_0^\rho k\gamma\sigma^{\gamma-2}d\sigma=\frac{k\gamma}{\gamma-1}\rho^{\gamma-1}=\frac{\gamma P}{(\gamma-1)\rho}$$and$$\Huge e(\rho)=\int_0^\rho\frac{P(\rho)}{\sigma^2}d\sigma=\int_0^\rho k\sigma^{\gamma-2}d\sigma=\frac{k\rho^{\gamma-1}}{\gamma-1}=\frac{P}{(\gamma-1)\rho}=\frac{h(\rho)}{\gamma}$$but we also have$$\Huge e(\rho)=\frac{c_VT}{\mu}\implies h(\rho)=\frac{c_V\gamma T}{\mu}$$so we can now relate the temperatures by$$\Huge T_1=T_2+\frac{u_2^2\mu}{2\gamma c_V}$$Assuming the jet moves at $220\text{ms}^{-1}$, $\gamma=1.4$, $\mu=0.029\text{kg mol}^{-1}$, $c_V\approx21\text{JK}^{-1}\text{mol}^{-1}$. We therefore find$$\Huge T_1\approx-26^\circ\text{C}$$so we see only mild heating occurs. Using the speed Concorde used to fly at, $605\text{ms}^{-1}$, we see that $T_1=130$ degrees, a lot hotter.
 