# 4-velocity and 4-momentum:

Consider the [[False Paradoxes#Spacetime diagrams|worldline]] of a particle. We then let $dx^\mu=(cdt,d\underline x)$ be the infinitesimal 4-vector between two events on the worldline of said particle:
![[Kinematics and collisions 2025-02-12 11.10.29.excalidraw]]

To find the change in [[Lorentz transformations#Time dilation and length contraction|proper time]] $d\tau$, we must examine the length of the invariant interval:$$\Huge d\tau=\frac{\sqrt{ds^2}}{c}=\frac{1}{c}\sqrt{c^2dt^2-|d\underline x|^2}=dt\sqrt{1-\frac{|\underline v|^2}{c}}=\frac{dt}{\gamma}$$where $\gamma$ is the usual [[Lorentz transformations#Lorentz boosts|Lorentz factor]]. We can then proceed to find the change in proper time between events at time $t_1,t_2$:$$\Huge \Delta\tau=\int_{t_1}^{t_2}d\tau=\int_{t_1}^{t_2}\frac{dt}{\gamma}\leq t_2-t_1=\Delta t$$we consider the trajectory of the particle to be parametrised by proper time, $\tau$. 

We can also find the 4-velocity of the particle:$$\Huge \frac{d x^\mu}{d\tau}=u^\mu=\gamma\frac{d }{dt}(ct,\underline x)=\gamma(c,\underline v)$$which has associated length:$$\Huge |u|^2=u^\mu u_\mu=\gamma^2(c^2-|\underline v|^2)=c^2>0$$So we see that 4-velocity is a time-like future pointing vector.

The 4-momentum of a particle is defined to be a 4-vector:$$\Huge p^\mu=mu^\mu=m\gamma(c,\underline v)$$where $m$ is the rest mass of the particle and is invariant. Note that:$$\Huge p^\mu p_\mu=m^2c^2$$so for a massless particle, we have $p^\mu p_\mu=0$ and the particle must be light-like.

We can also state a relativistic version of Newton's law:$$\Huge \frac{dp^\mu}{d\tau}=F^\mu=(F^0,\underline F)$$for $p^\mu=(p^0,\underline p)$ we can write:$$\Huge \gamma\frac{d }{dt}\underline p=\underline F=\gamma\underline f$$

# Mass-Energy equivalence:

If no external forces act on a particle, then we have conservation of total 4-momentum. For low speeds, we can [[Taylor series|Taylor expand]] the expression for $p^0$:$$\Huge\begin{align}
p^0=m\gamma c&=mc\left(1-\frac{v^2}{c^2}\right)^{-1/2}\\
&=mc\left(1+\frac{1}{2}\frac{v^2}{c^2}+\dots\right)\\
&=\frac{1}{c}\left(mc^2+\frac{1}{2}mv^2+\dots\right)\\
&=\frac{1}{c}E+\mathcal{O}(v^3)
\end{align}$$where we notice that $\frac{1}{2}mv^2$ is the expression for kinetic energy. Therefore we have $p^\mu=(E/C,\underline p)$ with:$$\Huge E=\gamma mc^2$$Note that at rest $(\gamma=1)$ we get Einstein's famous formula $E=mc^2$. Kinetic energy is given by:$$\Huge T=E-mc^2=\gamma mc^2-mc^2=(\gamma-1)mc^2$$
Energy can be written in terms of $3$-momentum to get:$$\Huge p\cdot p=m^2c^2=E^2/c^2-|\underline p|^2$$which rearranges to the relativistic energy momentum relation given by:$$\Huge E^2=m^2c^4+c^2|\underline p|^2$$
For the massless particle (photon), we take $m\to0$ to see that $\gamma\to\infty$ which implies that $v=c$. That is, the photon must travel at the speed of light. 

We can generalise Newton's law of motion so that is applies to relativistic particles:$$\Huge \frac{dp^\mu}{d\tau}=F^\mu$$where the force $F^\mu$ is a [[Spacetime and Tensors#Tensors|contravariant]] $4$-vector. In a given frame one can define the $3$-force $\underline f$ as:$$\Huge \underline f=\frac{d \underline p}{dt}$$For this to be consistent with the generalised force we must have $\underline F=\gamma\underline f$.

# Particle collisions:

We now consider the collision of particles in the absence of any external forces, that is we take $F^\mu=0$. Then the conservation of $4$-momentum dictates:$$\Huge \frac{dp^\mu}{d\tau}=(0,\underline 0)$$
Note that energy and momentum may be different when measured in different inertial frames. The transformation properties that we have derived ensure that if total energy and momentum are conserved in one frame, they are conserved in all inertial frames.

Let the total $4$-momentum of a set of particles be given by $p^\mu=(E/c,\underline p)$ in the frame $\mathcal{R}$. The frame $\mathcal{R}'$ moves with a velocity $\underline v$ with respect to $\mathcal{R}$. Such a frame is called the center of mass frame if the total $4$-momentum in this frame takes form $p'^\mu=(E'/c,\underline 0)$. That is, under the transformation, the total $3$-momentum vanishes. Using the earlier formula for a Lorentz boost in any direction, we can easily check that velocity for the center of mass frame relative to $\mathcal{R}$ is:$$\Huge \underline v=\frac{c^2}{E}\underline p$$
A relativistic collision is called elastic if the masses of all particles are conserved, and inelastic otherwise. The equivalence between energy and mass allows the masses of particles to change by conversion between mass and energy. This is equivalent to conservation of kinetic energy in classical mechanics.

For example, take two particles with mass $m$ that both travel at speed $v=4c/5$ as measured in the frame of a laboratory. They collide head on and fuse to form a particle of mass $M$. We then aim to calculate the ratio $M/m$.![[particle collisions]]