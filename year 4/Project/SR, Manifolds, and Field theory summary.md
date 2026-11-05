

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
Under Lorentz transformations, this general tensor transforms like:$$\Large\ T^{\mu_1'\dots\mu_k'}{}_{\nu_1'\dots\nu_l'}=\frac{\partial x^{\mu_1'}}{\partial x^{\mu_1}}\dots\frac{\partial x^{\nu_l}}{\partial x^{\nu_l'}}\ T^{\mu_1\dots\mu_K}{}_{\nu_1\dots\nu_l}$$Generally, the various tensor operations we define on flat space hold in more general settings with three important exceptions:
> Partial derivatives
> The metric
> Levi-Civita tensor

## Partial derivatives:
The partial derivative of a tensor is no generally a new tensor, as we can see by looking at the partial derivative of the one-form $\partial_\mu W_\nu$ under a new coordinate system:$$\Large\begin{aligned}
\frac{\partial }{\partial x^{\mu'}}W_{\nu'}&=\frac{\partial x^\mu}{\partial x^{\mu'}}\frac{\partial }{\partial x^\mu}\left(\frac{\partial x^\nu}{\partial x^{\nu'}}W_\nu\right)\\
&=\frac{\partial x^\mu}{\partial x^{\mu'}}\frac{\partial x^\nu}{\partial x^{\nu'}}\frac{\partial W_\nu}{\partial x^\mu}+W_\nu\frac{\partial x^\mu}{\partial x^{\mu'}}\frac{\partial^2 x^\nu}{\partial x^\mu\partial x^{\nu'}}
\end{aligned}$$This does not fit our known behaviour of tensors under Lorentz transformations, so this partial derivative is not a tensor. This motivates the definition of new kinds of derivatives, like the [[Non-abelian gauge theories#Fields|covariant derivative]].

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

# Tensor densities:

Recall the definition of the completely antisymmetric Levi-Civita symbols:$$\Large\epsilon_{\mu_1\dots\mu_n}=\begin{cases}+1 & \mu_1\dots\mu_n\text{ is an even permutation} \\
-1 & \mu_1\dots\mu_n\text{ is an odd permutation} \\
0 & \text{otherwise}\end{cases}$$This is by definition independent of coordinate system, however we can relate is transformation behaviour to that of a normal tensor by considering a matrix $M^\mu_{\mu'}\in M_{n\times n}(\mathbb{C})$. The determinant $|M|$ obeys:$$\Large\epsilon_{\mu_1'\dots\mu_n'}|M|=\underline{\epsilon}_{\mu_1\dots\mu_n}M^{\mu_1}_{\mu_1'}\dots M^{\mu_n}_{\mu_n'}$$Setting $M^\mu_{\mu'}=\frac{\partial x^\mu}{\partial x^{\mu'}}$ it follows that$$\Large\epsilon_{\mu_1'\dots\mu_n'}=\left|\frac{\partial x^{\mu'}}{\partial x^\mu}\right|\epsilon_{\mu_1\dots\mu_n}\frac{\partial x^{\mu_1}}{\partial x^{\mu_1'}}\dots\frac{\partial x^{\mu_n}}{\partial x^{\mu_n'}}$$where we used the fact that the matrix $\frac{\partial x^{\mu'}}{\partial x^\mu}$ is the inverse of $\frac{\partial x^\mu}{\partial x^{\mu'}}$ and the inverse matrix' determinant is just the inverse determinant. So we see that the Levi-Civita symbol transforms in a way similar to tensors, except for the determinant factor in the front. Objects that transform like this are known as tensor densities.

One can check that the determinant of the metric $g=|g_{\mu\nu}|$ transforms like:$$\Large g(x^\mu)=\left|\frac{\partial x^{\mu'}}{\partial x^\mu}\right|^{-2}g(x^\mu)$$The power to which the Jacobian in the front is raised to is known as the weight of the tensor density. The Levi-Civita symbol has weight $1$, and the metric has weight $-2$. To convert tensor densities to real tensors, one can multiply by $|g|^{w/2}$ where $w$ is the weight of the tensor density. We therefore define the Levi-Civita tensor as:$$\Large\tilde\epsilon_{\mu_1\dots\mu_n}=\sqrt{|g|}\epsilon_{\mu_1\dots\mu_n}$$We often end up contracting $p$ indices on $\epsilon^{\mu_1\dots\mu_n}$ with $\epsilon_{\mu_1\dots\mu_n}$, which can be expressed in terms of an antisymmetric product of Kronecker deltas$$\Large\epsilon^{\mu_1\dots\mu_p\alpha_1\dots\alpha_{n-p}}\epsilon_{\mu_1\dots\mu_p\beta_1\dots\beta_{n-p}}=(-1)^sp!(n-p)!\delta^{\alpha_1}_{\beta_1}\dots\delta^{\alpha_{n-p}}_{\beta_{n-p}}$$where $s$ is the number of eigenvalues of the metric (Lorentzian metrics take $s=1$).

# Differential forms:

We introduce a class of tensors known as differential forms. A differential $p$-form is a $[0,p]$ tensor that is completely antisymmetric, making scalars $0$ forms and covectors $1$ forms. The space of all $p$-forms is denoted by $\Lambda^p$, over a manifold we write this as $\Lambda^p(M)$. The number of linearly independent $p$-forms on an $n$-dimensional vector space is $n!/(p!(n-p)!)$. The idea of defining these is to use them in differentiation and integration without any geometric structure.

Given a $p$-form $A$ and $q$-form $B$, we can form a $(p+q)$-form called the wedge product $A\wedge B$ by taking the antisymmetrised tensor product:$$\Large(A\wedge B)_{\mu_1\dots\mu_{p+q}}=\frac{(p+q)!}{p!q!}A_{[\mu_1\dots\mu_p}B_{\mu_{p+1}\dots\mu_{p+q}]}$$Therefore the wedge product of two $1$-forms is:$$\Large(A\wedge B)_{\mu\nu}=2A_{[\mu}B_{\nu]}=A_\mu B_\nu-A_\nu B_\mu$$Note also:$$\huge A\wedge B=(-1)^{pq}B\wedge A$$

## Exterior derivatives:
The exterior derivative $d$ allows us to differentiate $p$-form fields to obtain $(p+1)$-form fields, defined as a properly normalised, antisymmetrised partial derivative:$$\Large (dA)_{\mu_1\dots\mu_{p+1}}=(p+1)\partial_{[\mu_1}A_{\mu_2\dots\mu_{p+1}]}$$The gradient $\partial_\mu\phi$ is simply the exterior derivative of a $0$-form $(d\phi)_\mu$. These obey a kind of Leibniz rule when applied to a $p$-form $\omega$ and $q$-form $\eta$:$$\Large d(\omega\wedge\eta)=(d\omega)\wedge\eta+(-1)^p\omega\wedge(d\eta)$$
This exterior derivative itself is a tensor, even in curved spacetime. The offending term in the transformation behaviour of the normal partial derivative is eliminated by the antisymmetry of the exterior derivative. 

## Hodge duality:
We define the Hodge star operator on an $n$-dimensional manifold as a map from $p$-forms to $(n-p)$ forms$$\Large (*A)_{\mu_1\dots\mu_{n-p}}=\frac{1}{p!}\ \epsilon^{\nu_1\dots\nu_p}{}_{\mu_1\dots\mu_{n-p}}A_{\nu_1\dots\nu_p}$$, mapping $A$ to the dual of $A$. Unlike our other operators, this depends on the metric of the manifold (as we had to raise some indices on the Levi-Civita tensor). Applying this operator twice gives$$\huge**A=(-1)^{s+p(n-p)}A$$where $s$ is the count of $-$ signs in the eigenvalues of the metric. Fax:
> Hodge duality is distinct from the relationship between vectors and covectors. The idea of Hodge duality is that of a transformation from one space to another applied twice returns to the original space, holding true for the relationship between $p$ and $(n-p)$ forms.
> The Hodge dual of a wedge product of two $1$-forms gives another $1$-form:$$\Large*(U\wedge V)_i= \epsilon_{i}{}^{jk}U_jV_k$$This is just the conventional cross product. The presence of the Levi-Civita symbol explains why the cross product changes sign under parity (swapping of basis vectors). 

## Integration on manifolds:
An important application of differential forms and tensor densities appears in integration over manifolds. We know that the volume element $d^nx$ picks up a Jacobian factor in $\Re^n$ under change of coordinates:$$\huge d^nx'=\left|\frac{\partial x^{\mu'}}{\partial x^\mu}\right|d^nx$$From the point of view of differential forms, this formula is explained from the fact that on an $n$-dimensional manifold $M$, the integrand is understood as an $n$-form. That is to say, an integral over an $n$-dimensional region $\Sigma\subset M$ is a map from an $n$-form field $\omega$ to the reals:$$\huge\int_\Sigma:\omega\to \Re$$This makes sense when considering a one dimensional $1$-form $\omega=\omega(x)dx$.

The role of the volume element is to assign every infinitesimal region an infinitesimal real number. A key feature of these infinitesimal regions is that they can be taken to be rectangular parallelepiped, however this does not make sense in the presence of curvature.

Our parallelepiped specified by $n$ vectors ($U,V,W$) defining it's edges should act like a map from said vectors to the reals, $d\mu(U,V,W)\in\Re$. It should also be linearly scalable by real numbers, that is $d\mu(aU,bV,cW)=abc\,d\mu(U,V,W)$. We also expect linearity in terms of adding vectors, convincing us that the volume element is a true $[0,n]$ tensor. This is antisymmetric as we defined an orientable element, interchanging two vectors should change the sign. To do calculations with this volume element, we must make this more rigorous:
> We identify the volume element $d^nx$ as an antisymmetric tensor density constructed via wedge products:$$\Large d^nx=dx^0\wedge\dots\wedge dx^{n-1}$$
> A coordinate transformation changes components, but not $1$-forms. The functions appearing on the RHS are the coordinate functions themselves, making the tensor density is a coordinate-dependent object.
> From the definition of the wedge product, we can write the transformation behaviour of this object:$$\Large\begin{aligned}
n!\,dx^0\wedge\dots\wedge dx^{n-1}&=\tilde\epsilon_{\mu_1\dots\mu_n}dx^{\mu_1}\wedge\dots\wedge dx^{\mu_n}\\
&=\tilde\epsilon_{\mu_1\dots\mu_n}\frac{\partial x^{\mu_1}}{\partial x^{\mu_1'}}\dots\frac{\partial x^{\mu_n}}{\partial x^{\mu_n'}}dx^{\mu_1'}\wedge\dots\wedge dx^{\mu_n'}\\
&=\left|\frac{\partial x^\mu}{\partial x^{\mu'}}\right|\tilde\epsilon_{\mu_1'\dots\mu_n'}dx^{\mu_1'}\wedge\dots\wedge dx^{\mu_n'}
\end{aligned}$$Showing that the volume element $d^nx$ transforms like a tensor density. 
> It is straightforward to construct an invariant volume element as we did with tensor densities before$$\Large\sqrt{|g'|}dx^{0'}\wedge\dots\wedge dx^{(n-1)'}=\sqrt{|g|}dx^0\wedge\dots\wedge dx^{n-1}$$, we can write this volume element in the explicit one-form basis to find:$$\large\begin{aligned}
\epsilon&=\epsilon_{\mu_1\dots\mu_n}dx^{\mu_1}\otimes\dots\otimes dx^{\mu_n}\\
&=\frac{1}{n!}\epsilon_{\mu_1\dots\mu_n}dx^{\mu_1}\wedge\dots\wedge dx^{\mu_n}\\
&=\frac{\sqrt{|g|}}{n!}\tilde\epsilon_{\mu_1\dots\mu_n}dx^{\mu_1}\wedge\dots\wedge dx^{\mu_n}\\
&=\sqrt{|g|}dx^0\wedge\dots\wedge dx^{n-1}=\sqrt{|g|}d^nx
\end{aligned}$$That is, the volume element is simply the Levi-Civita tensor.
> This machinery allows us to construct the integral of a scalar function simply:$$\large I=\int\phi(x)\sqrt{|g|}d^nx=\int\phi(x)\epsilon$$