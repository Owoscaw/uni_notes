
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
\frac{dh}{d\rho}\underline{\nabla}\rho&=\frac{1}{\rho}
\end{align*}$$