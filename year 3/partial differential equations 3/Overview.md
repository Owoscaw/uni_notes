
As any good study begins, we start by [[Introduction to PDEs#Classification of PDEs|classifying PDEs]]. To do this, we look at the order (highest derivative) in each equation as well as their linearity:
> Linear: Coefficients of the unknown function and derivatives depend only on independent variables.
> Semi-Linear: Highest order derivative is linear with coefficient as above.
> Quasi-Linear: As above, but coefficient can depend on lower derivatives.
> Fully Non-Linear: Does not fit

We first focus on solving first-order [[Introduction to PDEs#Quasi-linear PDEs|quasi-linear]] PDEs. We must develop the [[The Method of Characteristics#General setting|Method of Characteristics]], which builds upon theories of ODEs:
> We define characteristics as parameter-paths along which a PDE reduces into a system of ODEs.
> This method requires the [[The Method of Characteristics#Local well posedness of first order quasi-linear PDEs|non-characteristic]] condition, ensuring that the leading vector field of parameters points away from the initial [[The Method of Characteristics#General setting|Cauchy-curve]] so that information is able to "flow" into the domain.
> From this, we can find [[year 3/partial differential equations 3/term 1/Conservation laws#Breakdown of classical solutions|conservation laws]] that allow for breakdowns of classical solutions can be studied. This leads to the definition of [[Weak formulation#Rankine-Hugoniot condition and shocks|shocks]] which we use to describe the propagation of discontinuities.

Moving on to linear second-order PDEs, we focus on the problems of well-posedness. That is, we look at the conditions where a solution exists, uniqueness, as well as continuous dependence on data:
> [[Poisson's equation]] is the prototypical [[Partial differential equations#Elliptic PDEs|elliptic PDE]], which we build on by defining the fundamental solution and [[Green's method#Green's function via delta function|Green's functions]] to find explicit solutions. The special case $f=0$ is known as [[Laplace's Equation]]. From this we can define harmonic functions, which satisfy properties like [[Laplace's Equation#Mean-Value formulae in $ Re n$|mean-value formulae]] and maximum principles.