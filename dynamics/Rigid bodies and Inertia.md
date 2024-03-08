
A rigid body is a collection of masses such that the distance between the masses is fixed. If the body is not rotating, it behaves like a single particle. Consider masses $m_1,\dots,m_N$ at positions $\underline r_1,\dots, \underline r_N$. The single particle has mass $M=m_1+\dots+m_N$ and the position of the centre of mass is $\underline R=\frac{1}{M}(m_1 \underline r_1+\dots+m_N \underline r_N)$, the weighted position of masses.

Consider a rigid body rotating about a fixed axis, each $m_i$ moves in a circle as an angle $\theta$ changes. The configuration as a function of time is described as $\theta(t)$, all $m_i$ have the same angular velocity $\dot\theta$. Circular motion means that each $m_i$ has speed $v_i= \underline r_i|\dot\theta|$, making the total kinetic energy:$$\Huge K=\sum_i\frac{1}{2}m_iv_i^2=\frac{1}{2}\sum_i m_i \underline r_i^2|\dot\theta|^2$$The quantity $I=\sum_i m_i \underline r_i^2$ is called the moment of inertia $I$ of the body about the given axis:$$\Huge K=\frac{1}{2}I\dot\theta^2,\,\,I=\sum_im_ir_i^2$$
# Dynamics and Energy:

For a continuous rigid body, the sum needs to be replaced with an integral. Consider a uniform rigid rod of mass $M$ and length $L$ pivoted about an axis at one end, perpendicular. The moment of inertia is found by laying the rod on the $x$-axis at $x=0$. Consider a small length of the rod, $dx$, at a distance $x$ from the origin. This will have moment of inertia $dI=\frac{Mx^2}{L}dx$, so we write:$$\Huge I=\int_0^L\frac{Mx^2}{L}dx=\frac{1}{3}ML^2$$As one would expect, the centre of mass is at the centre of the rod. Note that the moment of inertia depends on the position of the axis.

## Kinetic energy:
The position of a rigid body, rotating about a fixed axis, is specified by an angle $\theta(t)$, making its angular velocity $\dot \theta$. The speed of a particle at a distance $r$ from the axis is $v=r|\dot \theta|$, making its kinetic energy:$$\Huge K=\frac{1}{2}mv^2=\frac{1}{2}mr^2\dot \theta^2$$Considering the sum or integral over a whole body gives:$$\Huge K=\frac{\dot \theta^2}{2}I$$Where $I$ is the moment of inertia. Note that since this body is rigid, all particles have the same $\dot \theta$.

## Total energy:
If the external forces are conservative, one can define a potential energy $V$ by summing or integrating over all particles, then $E=K+V$ is conserved. Using $\dot E=0$ gives the equation of motion:$$\Huge I\ddot \theta=-V'(\theta)$$
## Simple pendulum example:
For a simple pendulum, the 