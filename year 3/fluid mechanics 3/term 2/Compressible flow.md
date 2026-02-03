
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


# Sound waves:

The most important feature of a compressible fluid is that it supports pressure oscillations (sound waves). We proceed to study these oscillations using linearisation.

## Small amplitude sound waves:
We start from the unforced compressible barotropic Euler equations:$$\Huge\begin{align*}
\frac{\partial \rho}{\partial t}+\underline{\nabla}\cdot(\rho\underline{u})&=0\\
\frac{\partial \underline{u}}{\partial t}+(\underline{u}\cdot\underline{\nabla})\underline{u}&=-\frac{1}{\rho}\underline{\nabla}p\\
p&=P(\rho)
\end{align*}$$and proceed to consider disturbances around a base state with uniform density $\rho_0$, uniform pressure $p_0=P(\rho_0)$, and zero velocity. Replacing $\rho\rightarrow\rho_0+\epsilon\rho_1,p\rightarrow p_0+\epsilon p_1$, and $\underline{u}=\epsilon\underline{u}_1$ for our linearisation gives$$\Huge\begin{align*}
\epsilon\frac{\partial \rho_1}{\partial t}+\epsilon\rho_0\underline{\nabla}\cdot\underline{u}_1+\epsilon^2\underline{\nabla}\cdot(\rho_1\underline{u}_1)&=0\\
\epsilon\frac{\partial \underline{u}_1}{\partial t}+\epsilon^2(\underline{u}_1\cdot\underline{\nabla})\underline{u}_1&=-\frac{\epsilon}{\rho_0+\epsilon\rho_1}\underline{\nabla}p_1\\
p_0+\epsilon p_1&=P(\rho_0+\epsilon\rho_1)
\end{align*}$$To linearise the awkward terms on the RHS, we use the Taylor expansions:$$\Huge\begin{align*}
\frac{1}{\rho_0+\epsilon\rho_1}&=\frac{1}{\rho_0}\left(\frac{1}{1+\epsilon\frac{\rho_1}{\rho_0}}\right)\\
&=\frac{1}{\rho_0}\left(1-\epsilon\frac{\rho_1}{\rho_0}+\epsilon^2\frac{\rho_1^2}{\rho_0^2}+\dots\right)\\
P(\rho_0+\epsilon\rho_1)&=P(\rho_0)+\epsilon\rho_1P'(\rho_0)+\frac{\epsilon^2\rho_1^2}{2}P''(\rho_0)+\dots\\
&=p_0+\epsilon\rho_1P'(\rho_0)+\dots
\end{align*}$$so the linearised equations become$$\Huge\begin{align*}\frac{\partial \rho}{\partial t}+\rho_0\underline{\nabla}\cdot\underline{u}&=0\\
\frac{\partial \underline{u}}{\partial t}&=-\frac{1}{\rho_0}\underline{\nabla}p\\
p&=P'(\rho_0)\rho
\end{align*}$$To derive an equation for the pressure perturbation $p$, we differentiate the first equation wrt time and substitute into the second:$$\Huge\frac{\partial^2\rho}{\partial t^2}=-\rho_0\underline{\nabla}\cdot\frac{\partial \underline{u}}{\partial t}=\underline{\nabla}^2p$$Substituting in $\rho=p/P'(\rho_0)$ then implies$$\Huge \frac{\partial^2p}{\partial t}=c_0^2\underline{\nabla}^2p,\,\,c_0=\sqrt{P'(\rho_0)}$$which is simply the three-dimensional wave equation and $c_0$ is called the sound speed.
> Assuming an ideal gas, $P(\rho)=kp^\gamma$, the sound speed becomes$$\Huge c_0=\sqrt{k\gamma\rho_0^{\gamma-1}}$$We know that $T=e\mu/c_V$ and saw that$$\Huge e(\rho_0)=\int_0^{\rho_0}\frac{P(\sigma)}{\sigma^2}d\sigma=\frac{k\rho_0^{\gamma-1}}{\gamma-1}$$and so we introduce $c_0$ as a function of $e$ and introduce $T$:$$\Huge c_0=\sqrt{\gamma(\gamma-1)e(\rho_0)}=\sqrt{\gamma(\gamma-1)\frac{c_VT}{\mu}}$$Given that $\gamma=(n_\text{dof}+2)/n_\text{dof}$ and $c_V=\frac{1}{2}n_\text{dof}R$, we get$$\Huge c_0=\sqrt{\frac{\gamma RT}{\mu}}$$So for an ideal gas, sound speed is only a function of temperature. For air, $\gamma=1.4,R=8.3\text{JK}^{-1}\text{mol}^{-1}$, and $\mu=0.0029\text{kg mol}^{-1}$, so we calculate$$\Huge c_0=\begin{cases}332\text{ m s}^{-1} & T=273\text{ K} \\
344\text{ m s}^{-1} & T=293\text{ K}\end{cases}$$

To find an equation for $\phi$, we take the curl of our second equation to get$$\Huge \underline{\nabla}\times\left(\frac{\partial \underline{u}}{\partial t}\right)=\underline{\nabla}\times\left(-\frac{1}{\rho_0}\underline{\nabla}p\right)\implies\frac{\partial \underline{\omega}}{\partial t}=\underline{0}$$, which shows that sound waves do not change the [[Kinematics of Fluids#Vorticity|vorticity]]. So if we start with no vorticity, we continue to have no vorticity. This means that we can express the velocity in terms of a potential$$\Huge \underline{u}(\underline{x},t)=\underline{\nabla}\phi(\underline{x},t)$$where $\phi(\underline{x},t)$ is known as the acoustic velocity potential. To find the equation that this satisfies, note that our linearisation leads to$$\Huge\begin{align*}
\underline{\nabla}\frac{\partial \phi}{\partial t}&=-\underline{\nabla}\left(\frac{1}{\rho_0}p\right)\\
&=-\underline{\nabla}\left(c_0^2\frac{1}{\rho_0}\rho\right)
\end{align*}$$Differentiating wrt time and substituting into our other equation gives$$\Huge\underline{\nabla}\frac{\partial^2\phi}{\partial t^2}=-\underline{\nabla}\left(c_0^2\frac{1}{\rho_0}\frac{\partial \rho}{\partial t}\right)=\underline{\nabla}(c_0^2\underline{\nabla}^2\phi)$$Ignoring the arbitrary function of time, we have$$\Huge \frac{\partial^2\phi}{\partial t^2}=c_0^2\underline{\nabla}^2\phi$$which is the same equation as $p$. In acoustics, we solve a wave equation for allowable forms of $\phi$ subject to certain boundary conditions. We then recover $\underline{u},p,\rho$ from$$\Huge \underline{u}=\underline{\nabla}\phi,\,\,p=-\rho_0\frac{\partial \phi}{\partial t},\,\,\rho=\frac{1}{c_0^2}p$$
## $1D$ travelling wave solutions:
If we assume that $\phi=\phi(x,t)$, then the wave equation for $\phi$ reduces to$$\Huge \frac{\partial^2\phi}{\partial t^2}=c_0^2\frac{\partial^2\phi}{\partial x^2}$$which admits a travelling wave solution of the form$$\Huge\phi(x,t)=F(x-c_0t)+G(x+c_0t)$$and when given $\phi(x,0)$, one can find particular forms using a Fourier expansion. However, we have two constraints on $\phi$ given by specifying pressure $p$ as well as $\underline{u}$ at $t=0$. Therefore our initial value problem becomes:$$\Huge\begin{align*}
\frac{\partial^2\phi}{\partial t^2}&=c_0^2\frac{\partial^2\phi}{\partial x^2}\\
\phi(x,0)&=\phi_0(x)\\
\frac{\partial \phi}{\partial t}(x,0)&=\dot\phi_0(x)
\end{align*}$$At $t=0$, we have$$\Huge\phi_0(x)=F(x)+G(x)$$which makes the second condition$$\Huge\begin{align*}
\dot\phi_0(x)&=-c_0F'(x)+c_0G'(x)\\
\implies\int_a^x\dot\phi_0(s)ds&=-c_0F(x)+c_0G(x)
\end{align*}$$for some arbitrary point $a$. This gives us the functional form for $F,G$. Using this in our solution and assuming that $a$ is between diverging points defined by $x-c_0t,x+c_0t$ we get$$\large\begin{align*}
\phi(x,t)&=\frac{1}{2}\phi_0(x-c_0t)-\frac{1}{2c_0}\int_a^{x-c_0t}\dot\phi_0(s)ds+\frac{1}{2}\phi_0(x+c_0t)+\frac{1}{2c_0}\int_a^{x+c_0t}\dot\phi_0(s)ds\\
&=\frac{1}{2}(\phi_0(x-c_0t)+\phi_0(x+c_0t))+\frac{1}{2c_0}\int_{x-c_0t}^{x+c_0t}\dot\phi_0(s)ds
\end{align*}$$This solution is known as D'Alembert's solution. Let us try an example:
> Consider a Gaussian pulse:$$\Huge u(x,0)=0,\,\,p(x,0)=\rho_0e^{-x^2/a^2}$$These initial conditions correspond to $\phi_0(x)=0$ and$$\Huge\dot\phi_0(x)=-\frac{1}{\rho_0}p(x,0)=-e^{-x^2/a^2}$$Appling D'Alembert's solution gives$$\Huge\begin{align*}
\phi(x,t)&=-\frac{1}{2c_0}\int_{x-c_0t}^{x+c_0t}e^{-s^2/a^2}ds\\
&=-\frac{1}{2c_0}\int_0^{x+c_0t}e^{-s^2/a^2}ds+\frac{1}{2c_0}\int_0^{x-c_0t}e^{-s^2/a^2}ds\\
&=\frac{a\sqrt\pi}{4c_0}\left(-\text{erf}\left(\frac{x+c_0t}{a}\right)+\text{erf}\left(\frac{x-c_0t}{a}\right)\right)
\end{align*}$$where $\text{erf}$ is the error function, defined by$$\Huge\text{erf}(x)=\frac{2}{\sqrt\pi}\int_0^xe^{-s^2}ds$$
> Differentiating our solution wrt time, we can find the corresponding pressure perturbation:$$\Huge p(x,t)=-\rho_0\frac{\partial \phi}{\partial t}=\frac{\rho_0}{2}\exp\left(-\frac{(x+c_0t)^2}{a^2}\right)+\frac{\rho_0}{2}\exp\left(-\frac{(x-c_0t)^2}{a^2}\right)$$
> As expected, the initial disturbance leads to two identical pressure pulses of the same shape moving in opposite directions at constant speed $c_0$. 
> Solving the non-linearised system numerically shows that our model holds up well for early times, however in reality $c$ can vary over space and time.

## $1D$ standing wave solutions:
Now we have an idea of the general properties of sound wave, let us introduce more effects. We start by introducing walls, so we assume our domain is now of the form $\{x:0<x<L\}$. As for water waves, we then look for standing wave solutions of the form$$\Huge\phi(x,t)=X(x)\sin(\omega t)$$Substituting this into our linear wave equation for $\phi$ gives us the ODE:$$\Huge-\omega^2X=c_0^2X''$$which has the solution$$\Huge X(x)=A\sin(kx)+B\cos(kx),\,\,k=\frac{\omega}{c_0}$$Our solution $\phi$ must satisfy suitable boundary conditions at $x=0$ and $x=L$, which depend on the problem. These will either be of the form of a constraint on pressure or velocity:
> Let us explore an example modelling a tube with two open ends where $p=0$ but $\underline{u}$ is unconstrained. The boundary conditions are then on $p$:$$\Huge p(x,t)=-\rho_0\frac{\partial \phi}{\partial t}=-\rho_0\omega X(x)\cos(\omega t)$$so in order to satisfy them, our solution must be$$\Huge X(x)=A_n\sin\left(\frac{n\pi x}{L}\right)$$where the wavenumber $k$ is now of the form $k=n\pi/L$.
> There is therefore a discrete spectrum of possible modes with $\omega=c_0k=c_0n\pi/L$. Each mode has the form$$\Huge\phi(x,t)=A_n\sin\left(\frac{n\pi x}{L}\right)\sin\left(\frac{c_0n\pi t}{L}\right)$$

## $3D$ travelling wave solutions:
Let us now generalise these concepts to $\Re^3$. We saw that the wave equation admits a solution of a superposition of two oppositely moving waves. In $\Re^3$, the solution will be a superposition of plane waves travelling in many different directions. Each component will have form$$\Huge \phi(\underline{x},t)=F(\underline{k}\cdot\underline{x}-\omega t)$$for some fixed vector $\underline{k}$ whose direction represents the direction of motion. Differentiating this expression, we find:$$\Huge\begin{align*}
\frac{\partial^2\phi}{\partial t^2}&=\omega^2 F''(\underline{k}\cdot\underline{x}-\omega t)\\
\underline{\nabla}^2\phi&=\frac{\partial^2\phi}{\partial x^2}+\frac{\partial^2\phi}{\partial y^2}+\frac{\partial^2\phi}{\partial z^2}\\
&=(k_x^2+k_y^2+k_z^2)F''(\underline{k}\cdot\underline{x}-\omega t)
\end{align*}$$So this will be a solution to our system, providing that $\omega$ satisfies the dispersion relation$$\Huge \omega^2=c_0^2|\underline{k}|^2$$The corresponding velocity perturbation is then$$\Huge \underline{u}(\underline{x},t)=\underline{\nabla}\phi=\underline{k}F'(\underline{k}\cdot\underline{x}-\omega t)$$, so we see that oscillations are in the direction of propagation aligned with $\underline{k}$. 

Consider a travelling plane wave reflecting off of a wall:
> If we place a rigid wall at $y=0$, let us propagate an incoming wave diagonally towards it in the $\underline{k}_i=(k_x,-k_y)$ direction:$$\Huge\implies\phi_i(x,y,t)=\exp(ik_xx-ik_yy-i\omega t)$$
> To find the wave on the whole domain, we use two methods:
> > Firstly we use separation of variables:$$\Huge \phi(x,y,t)=X(x)Y(y)\exp(-i\omega t)$$
> > Recall that we expect a superposition of waves, so we should find $\phi_i$ inside our solution.
> > Inserting our separation into our wave equation, we get$$\Huge-\omega^2=c_0^2\left(\frac{X''}{X}+\frac{Y''}{Y}\right)$$, which we further separate:$$\Huge -\frac{X''}{X}=\frac{Y''}{Y}+\frac{\omega^2}{c_0^2}=k_x^2$$
> > The solutions then have form:$$\Huge X(x)=A\exp(ik_xx)+B\exp(-ik_xx)$$
> > Rewriting our $Y$ equation as$$\Huge\frac{Y''}{Y}=k_x^2-\frac{\omega^2}{c_0^2}=-k_y^2\implies k_y^2=\frac{\omega^2}{c_0^2}-k_x^2$$, we see that our solution has form:$$\Huge Y(y)=C\exp(ik_yy)+D\exp(-ik_yy)$$
> > Our full solution is then:$$\phi(x,y,t)=(A\exp(ik_xx)+B\exp(-ik_xx))(C\exp(ik_yy)+D\exp(-ik_yy))\exp(-i\omega t)$$
> > The constants are determined by additional conditions:
> > > Firstly we impose the condition at the wall:$$\Huge v=\frac{\partial \phi}{\partial y}=0\implies Y'(0)=0$$and so it follows that:$$\Huge ik_yC-ik_yD=0\implies C=D$$
> > > Secondly, we note that if we expand our solution we get $4$ terms. We expect $\phi_i$ to be one of these terms, which is in fact the case with $AD=1$. Then the $BC$ term is a leftward, downward moving wave. This is not allowed, so we set $B=0$
> > This fixes our solution:$$\Huge\begin{align*}
\phi(x,y,t)&=X(x)Y(y)\exp(-i\omega t)\\
&=\exp(ik_xx)(\exp(ik_yy)+\exp(-ik_yy))\exp(-i\omega t)\\
&=\exp(ik_xx-ik_yy-i\omega t)+\exp(ik_xx+ik_yy-i\omega t)
\end{align*}$$where the terms represent $\phi_i$ and the reflected wave respectively. 
> > We are then left with the incidence wave with direction $\underline{k}_i=(k_x,-k_y)$ and a reflected wave with direction $\underline{k}_r(k_x,k_y)$.
> Our second method is the method of images. Just as we did with potential flows, we can take the same approach and guarantee that $v=0$ at the wall by superimposing the incident wave $\phi_i$ with an image wave $\tilde\phi$ that is travelling in the same direction in $x$, but opposite in $y$. Thus we can directly postulate the same solution.

## $3D$ waveguide solutions:
We saw that in $1$ dimension on a finite domain, a discrete spectrum of standing wave modes was admitting. Similarly for a domain of finite width (waveguide), a discrete spectrum of propagating modes is admitted:
> Let us assume a $2D$ domain with walls at $y=0,y=a$. We look for a solution propagating in $x$ of the form$$\Huge \phi(x,y,t)=Y(y)\exp(ik_xx-i\omega t)$$
> Substituting this into the wave equation, we find$$\Huge -\omega^2Y=c_0^2(Y''-k_x^2Y)\implies Y''=-k_y^2Y,\,\,k_y^2=\frac{\omega^2}{c_0^2}-k_x^2$$
> The boundary conditions impose $v=0$ on $y=0,y=a$ so we need $Y'(0)=Y'(a)=0$. This shows that$$\Huge Y(y)=A_n\cos(k_yy),\,\,k_y=\frac{n\pi}{a}$$, a discrete spectrum of modes is admitted. 
> The allowed modes then take form$$\Huge \phi(x,y,t)=A_n\cos\left(\frac{n\pi y}{a}\right)\exp(ik_xx-i\omega t)$$, provided that $\omega$ satisfies the dispersion relation$$\Huge \omega=c_0\sqrt{k_x^2+\frac{n^2\pi^2}{a^2}}$$

This tells us a few things:
> The dispersion relation leads to a minimum frequency. For any mode $n$:$$\Huge \omega>c_0\sqrt{\frac{n^2\pi^2}{a^2}}=c_0\frac{n\pi}{a}$$So taking $n=0$, we have a wave with no $y$-dependence (giving a plane wave) and our constraint is always satisfied. For higher modes, this is not true. That is, for $\omega\leq c_0\pi/a$, only a plane wave can propagate. 
> The phase speed in the $x$-direction $\omega/k_x$ is a function of $n$, so sound waves of different frequencies progress along the waveguide at different speeds.
> Note that this phase speed in the $x$-direction is faster than the speed of sound since $\omega/k_x>c_0$, so the wave becomes slower in the $y$-direction to compensate. Observe that our dispersion relation dictates $\omega=c_0|\underline{k}|$. To calculate the speed we therefore need to use $|\underline{k}|$, not $k_x$.
> This is because the mode is actually made of two travelling waves travelling at an angle and propagating off of the walls. To see this, note that$$\begin{align*}
\cos\left(\frac{n\pi y}{a}\right)\exp(ik_xx-i\omega t)&=\frac{1}{2}\left(\exp\left(\frac{in\pi y}{a}\right)+\exp(-\frac{in\pi y}{a})\right)\exp(ik_xx-i\omega t)\\
&=\frac{1}{2}\exp\left(\frac{in\pi y}{a} +ik_xx-i\omega t\right)+\frac{1}{2}\exp\left(-\frac{in\pi y}{a}+ik_xx-i\omega t\right)
\end{align*}$$, so each wave has wavenumber$$\Huge |\underline{k}|=\sqrt{k_x^2+\frac{n^2\pi^2}{a^2}}$$and so their phase speed is $\omega/|\underline{k}|=c_0$ as expected. The waves therefore bounce off of the wall at the angle$$\Huge \alpha=\pm\arctan\left(\frac{k_y}{k_x}\right)=\pm\arctan\left(\frac{n\pi}{k_x a}\right)$$

We can generalise this approach to $3D$ waveguides such as tubes with square or circular cross sections. Therefore let us consider a cylindrical waveguide:
> Here, we assume the domain is an infinite tube of radius $a$:$$\Huge \Omega=\{(r,\theta,z):0\leq r<a,0\leq \theta<2\pi,-\infty<z<\infty\}$$
> So we look for axisymmetric solutions of the form $\phi(r,z,t)=R(r)\exp(ik_zz-i\omega t)$. In cylindrical coordinates, the wave equation gives:$$\Huge -\omega^2R=c_0^2\left(\frac{1}{r}\frac{d}{dr}(rR')-k_z^2R\right)$$Which we rearrange to give$$\Huge r^2R''+rR'+\left(\frac{\omega^2}{c_0^2}-k_z^2\right)r^2R=0$$
> Comparing this to Bessel's equation of order $\alpha$ for a function $u(s)$ and its solution:$$\Huge s^2u''+su'+(s^2-\alpha^2)u=0\implies u(s)=AJ_\alpha(s)+BY_\alpha(s)$$So we see that our equation is simply Bessel's equation of order $0$ when we change variables:$$\Huge s=\left(\frac{\omega^2}{c_0^2}-k_z^2\right)^{1/2}r$$
> Our solution is therefore the Bessel function $R(s)=AJ_0(s)$:$$\Huge R(r)=AJ_0\left(\left(\frac{\omega^2}{c_0^2}-k_z^2\right)^{1/2}r\right)$$
> It remains to impose the boundary condition $u_r=0$ on $r=a$, meaning $R'(a)=0$:$$\Huge \implies J'_0\left(\left(\frac{\omega^2}{c_0^2}-k_z^2\right)^{1/2}a\right)=0$$
> As $J_0$ has a discrete sequence of turning points, this will give us a discrete spectrum of $\omega$. Let $j_n$ be the $n$th turning point of $J_0$, then:$$\Huge \phi(r,z,t)=A_nJ_0\left(\frac{j_n r}{a}\right)\exp(ik_zz-i\omega t),\,\,\omega=c_0\sqrt{k_z^2+\frac{j_n^2}{a^2}}$$ 

