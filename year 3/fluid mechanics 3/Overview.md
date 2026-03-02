
From the definition of fluids as a continuum of particles and systematically adding physical laws and constraints we can model increasingly complex behaviour:
> The [[Kinematics of Fluids#What is a fluid?|continuum hypothesis]] defines a fluid as a continuous substance described by a density field $\rho$ and a velocity field $\underline{u}$. We adopt two perspectives to describe these fields motion:
> > The Eulerian perspective observes the fluid at fixed points in space.
> > The Lagrangian perspectives tracks individual particles moving through time.
> We develop the [[Kinematics of Fluids#The material derivative|material derivative]] $D/Dt$ as the bridge between these perspectives, allowing for the calculation of the rate of change of a property in the fluid following a particle.
> We then apply the following physical constraints:
> > Applying conservation of mass leads to the [[Kinematics of Fluids#Conservation of mass|continuity equation]]. Note that for most fluids, this is simplified assuming incompressibility $\underline{\nabla}\cdot\underline{u}=0$.
> > We first define a way to quantify rotation, the [[Kinematics of Fluids#Vorticity|vorticity]] $\underline{\omega}=\underline{\nabla}\times\underline{u}$. We often demand that this is zero, however we can also calculate the [[Kinematics of Fluids#Circulation|circulation]] $\Gamma$ as the integral of velocity around a closed curve.
> > Assuming a flow is both incompressible and irrotational, we can let the velocity be defined as the gradient of a [[Kinematics of Fluids#Potential flows|velocity potential]] $\phi$. These are solved by [[Laplace's equation]].
> Moving on from kinematic definitions, we investigate the dynamics of fluids by defining the forces acting on a fluid. This is described in the [[Dynamics of ideal fluids#Incompressible Euler equations|Euler equations]].
> Building off of the Euler equation, we define the energy head H as a constant quantity along streamlines in [[Dynamics of ideal fluids#Bernoulli's principle|Bernoulli's principle]].
> We can model [[Water waves|water waves]] using a potential flow and our dynamics with oscillations on a free surface. From this, we define concepts such as the [[Water waves#Dispersion relation|dispertion relation]].

These all work well for a fluid under ideal assumptions, however this is not enough for us. We therefore change certain aspects of our model:
> By analysing a free surface in equilibrium, we find that small perturbations can lead to exponential growth and destabilisation in the free surface. This can happen in the [[Instability#The Rayleigh-Taylor instability|Rayleigh-Taylor]] and [[Instability#The Kelvin-Helmholtz instability|Kelvin-Helmholtz]] instabilities.
> By allowing for [[Compressible flow|compressible flow]], we can model gasses which introduces the notion of [[Compressible flow#Sound waves|sound waves]] as small-amplitude pressure oscillations and [[Compressible flow#Nonlinearity|shocks]].
> We can introduce the internal friction using the [[Dynamics of viscous fluids#Stress tensor symmetry|stress tensor]]. This leads to the [[Dynamics of viscous fluids#The Navier-Stokes equations|Navier-Stokes equations]], which are the defining equations for viscous fluid motion.  