

# Special relativity recap:

Before we introduce [[Manifolds and tensors|manifolds]], we describe spacetime in the context of special relativity as a four dimensional set whose elements are labelled by $3$ spatial and $1$ temporal dimension. We call points in spacetime events, and a particle's path is written as a parametrised $1$D set of events - called the worldline. Note we will use$$\Huge\eta_{\mu\nu}=\begin{pmatrix}-1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}$$as our [[Special relativity#Relativistic notation|Minkowski metric]], allowing us to write the [[Special relativity#Lorentz transformations|invariant interval]] as:$$\Huge (\Delta s)^2=\eta_{\mu\nu}\Delta x^\mu\Delta x^\nu$$For timelike particles, this interval will clearly be negative which prompts the definition of proper time:$$\Huge (\Delta\tau)^2=-(\Delta s)^2$$This has a crucial feature:
> The proper time between two events measures the time elapsed as seen by an observer moving on a straight path between the events.

# Manifolds recap:

For general trajectories, proper time will differ from coordinate time. Not all of these trajectories can be made from straight line segments, so we introduce the [[Thermodynamics#Generalised displacements|differential]] interval (line element)$$\Huge ds^2=\eta_{\mu\nu}dx^\mu dx^\nu$$for infinitesimal coordinate displacements $dx^\mu$. All other notions can be found in [[Manifolds and tensors]].

Consider the worldline of a single particle, which we specify by a map $\mathbb{R}\to M$ where $M$ is the manifold representing spacetime. We think of the particles as a parametrised curve $x^\mu(\lambda)$, and focus on [[Special relativity#Curves and $4$-vectors|timelike]] particles with paths $\tau(\lambda)$ which are invertible given good choice of parameter. In this parametrisation, we write the four velocity $U^\mu$ as:$$\huge U^\mu=\frac{dx^\mu}{d\tau}$$The line element $d\tau^2=-\eta_{\mu\nu}dx^\mu dx^\nu$ (note the sign change) is the infinitesimal for our particle, whose form allows for the automatic normalisation of four velocity:$$\huge
\ \eta_{\mu\nu}{}^{}U^\mu U^\nu=-1$$This is a reflection of the fact that our definition of four velocity can be thought of as a velocity through a spacetime manifold through which one always travels at unit velocity. From this we define the momentum four vector:$$\huge p^\mu=mU^\mu$$
# Tensors on manifolds:

Having defined vectors and covectors in copious detail, let us explore in more depth how tensors behave on manifolds. Recall the canonical example of a one-form, the gradient of a function $f$:$$\huge df:\,\,df\left(\frac{d}{d\lambda}\right)=\frac{df}{d\lambda}$$Through this machinery we defined [[Manifolds and tensors#Vectors, covectors, and tensors|vectors and covectors]] in differential form and wrote bases for $T_p,T_p^*$ in terms of $\omega=\omega_\mu dx^\mu$ and $\partial_\nu$. A $(k,l)$ tensor is then a multilinear map from $k$ covectors and $l$ vectors to $\mathbf{R}$ Its component expression can be expressed as the tensor acting on the set of basis vectors, equivalent to the expansion on the following line:$$\Large\begin{aligned}
\ T^{\mu_1\dots\mu_k}{}_{\nu_1\dots\nu_k}&=T(dx^{\mu_1},\dots,dx^{\mu_k},\partial_{\nu_1},\dots,\partial_{\nu_l})\\
\implies T&= T^{\mu_1\dots\mu_k}{}_{\nu_1\dots\nu_l}\partial_{\mu_1}\otimes\dots\otimes\partial_{\mu_k}\otimes dx^{\nu_1}\dots\otimes dx^{\nu_l}
\end{aligned}$$
ASK WHY THE INDICES ARE REVERSED ^^^ Under Lorentz transformations, this general tensor transforms like:$$\Large\ T^{\mu_1'\dots\mu_k'}{}_{\nu_1'\dots\nu_l'}=\frac{\partial x^{\mu_1'}}{\partial x^{\mu_1}}\dots\frac{\partial x^{\nu_l}}{\partial x^{\nu_l'}}\ T^{\mu_1\dots\mu_K}{}_{\nu_1\dots\nu_l}$$Generally, the various tensor operations we define on flat space hold in more general settings with three important exceptions:
> Partial derivatives
> The metric
> Levi-Civita tensor

## Partial derivatives:
The partial derivative of a tensor is no generally a new tensor, as we can see by looking at the partial derivative of the one-form $\partial_\mu W_\nu$ under a new coordinate system:$$\Large\begin{aligned}
\frac{\partial }{\partial x^{\mu'}}W_{\nu'}&=\frac{\partial x^\mu}{\partial x^{\mu'}}\frac{\partial }{\partial x^\mu}\left(\frac{\partial x^\nu}{\partial x^{\nu'}}W_\nu\right)\\
&=\frac{\partial x^\mu}{\partial x^{\mu'}}\frac{\partial x^\nu}{\partial x^{\nu'}}\frac{\partial W_\nu}{\partial x^\mu}+W_\nu\frac{\partial x^\mu}{\partial x^{\mu'}}\frac{\partial^2 x^\nu}{\partial x^\mu\partial x^{\nu'}}
\end{aligned}$$This does not fit our known behaviour of tensors under Lorentz transformations, so this partial derivative is not a tensor. This motivates the definition of new kinds of derivatives, like the [[Non-abelian gauge theories#Fields|covariant derivative]].

## The metric:

# Energy-Momentum tensor:

The energy of a particle described above is given by $E=p^0$, the timelike component of four momentum. In a moving frame we can find components of $p^\mu$ by taking Lorentz transformations:$$\huge p^\mu\to(\gamma m,v\gamma m,0,0)$$For a particle moving with velocity $v$ along the $x$-axis. Note that $p^0$ and $p^1$ correspond to rest + kinetic energy and Newtonian momentum for small $v$. Outside of that approximation, we write:$$\Large p_\mu p^\mu=-m^2,\,\,E=\sqrt{m^2+p^2}\,\,(p^2=\delta_{ij}p^ip^j)$$We should look for an $F=ma$ in this formulation, naturally motivation the definition of a four vector $f^\mu$ satisfying:$$\Large f^\mu=m\frac{d^2}{d\tau^2}x^\mu(\tau)=\frac{d}{d\tau}p^\mu(\tau)$$Note that we can now find tensorial verions of any force we want, however one will find that the requirements for an equation to be a tensor equation restricts the form signficantly.

A single momentum four-vector field is insufficient to describe energy and momentum of our modern understanding of "fluid systems", so we seek to define the energy-momentum tensor $T^{\mu\nu}$:
>This is a symmetric $(2,0)$ tensor that will contain all the energy-like information of a system.
>This tensor describes the flux of four-momentum $p^\mu$ across a surface of constant $x^\nu$
>$T^{00}$ the "flux of $p^0$ (energy)" across $x^0$ (time) is simply energy density $\rho$.
>Similarly, $T^{0i}=T^{i0}$ is the momentum density.
>Other diagonals give the force exerted by a spacetime fluid element in each direction.

We will encounter this later, however let it stir in your mind what this represents...

# Field theory summary:

Note we summarise our field theory knowledge with the Maxwell equations instead of a simple scalar field, because the chapter $4$ insight we will make is a pain in the ass to write :)

Recall the Lagrangian formulation that led to [[Abelian gauge theories#Relativistic Maxwell's equations|this]] form of Maxwell's equations:$$\huge\partial_\mu F^{\nu\mu}=J^\nu$$Note the order of indices on the Faraday tensor. We will see that imposing the action on our Lagrangian$$\huge\mathcal{L}=-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}+A_\mu J^\mu$$will lead to an energy-momentum tensor for electromagnetism:$$\Large T^{\mu\nu}_{EM}=F^{\mu\lambda}F^\nu{}_\lambda-\frac{1}{4}\eta^{\mu\nu} F^{\lambda\sigma}F_{\lambda\sigma}$$Using the EOM, one can show that these tensors are conserved ($\partial_\mu T^{\mu\nu}=0$). We consider electromagnetism and scalar fields as fundamental, they make up our current understanding of nature. The standard model consists of [[Non-abelian gauge theories#The Standard Model|Gauge fields]], Higgs fields, and fermions:
> Gauge fields describe forces in nature, including strong and weak nuclear forces as well as electromagnetism and are all matrix valued.
> Higgs fields are the aformentioned scalar fields, are matrix valued.
> Fermions include leptons and quarks, and are not described by tensor fields but rather by a [[The Lorentz Group#Spinors of the Lorentz group|spinor]] field.

General relativity is a classical field theory who's dynamical field is the metric tensor. Our aim will be to explore the nature of curved geometries, which we characterise by the spacetime metric. Before putting these notions to work, we introduce the theory of gravitation.