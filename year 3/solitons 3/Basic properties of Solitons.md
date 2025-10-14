
# The KdV equation:

The nonlinear partial differential equation:$$\Huge u_t+6uu_x+u_{xxx}=0$$
is known as the Korteweg-De Vries equation and was the first to initially capture the behavior of solitons. The real field $u(x,t)$ represents the height of a wave in space and time. This equation is first order in $t$, so the solution is determined by an initial condition $u(x,0)$.

With the initial condition $u(x,0)=\frac{2}{\cosh^2(x)}$ we can explore the properties of the KdV equation:
> Dropping the nonlinear term $6uu_x$ gives the linearised KdV equation:$$\Huge u_t+u_{xxx}=0$$Here, the initial localised wave disperses and $u\to0$ as $t\to+\infty$
> Dropping the dispersive $u_{xxx}$ gives the dispersionless KdV equation:$$\Huge u_t+6uu_x=0$$Here, the nonlinearity causes the wave to "pile up" and break after finite time
> Keeping all of the terms causes the previous two effects to cancel each other out, and we see the "travelling wave" behavior.

A more generalised class of initial conditions is given by:$$\Huge u(x,0)=\frac{N(N+1)}{\cosh^2(x)},\,\,N>0$$Numerical experiments show that:
> $N\in\mathbb{Z}$ causes the initial wave to split into $N$ solitons moving to the right with no dispersion
> $N\notin\mathbb{Z}$ causes the initial wave to split into $\lceil N\rceil$ solitons moving to the right plus dispersing waves
> 

In either case, the different solitons move at different speeds, with the following behavior:
> $\text{speed}\propto\text{height}$
> $\text{width}\propto\text{height}^{-1/2}$
# Soliton properties:

From the KdV equation with initial state $u(x,t=0)=\frac{N(N+1)}{\cosh^2(x)}$ we see that if $N$ is an integer, $N$ solitons are initially released. If $N$ is not an integer, some solitons disperse over time. More generally:
> Soliton speed is proportional to its height
> Shapes are preserved when solitons pass over each other

We can now refine the idea of a soliton. A soliton is a solution of a wave equation [[Introduction to PDEs#The vibration of a string|PDE]] that exhibits the following behavior:
> Localised (lump of energy)
> Localised form preserved over time
> Form is preserved under interaction with other solitons

Note that not all nonlinear PDEs have such solutions, however those that do are called integrable.

# Ball and Box model:

The ball and box model is a simplified model for a soliton equation that is much easier to compute than the KdV equation. Firstly we replace continuous states with an infinite line of boxes, now we put a finite number of balls into the boxes with at most one per box. The "ball and box" rule is then used to evolve the system a single discrete step in time:
> Working from left to right, move the leftmost unmoved ball to the next available (empty) box to its right
> Continue until every ball has been moved
> Once complete, a time step has been completed

In general, $n$ balls in a row move to the right with speed $n$. This is the equivalent to the speed being proportional to the height of the soliton in the KdV equation. Note that while the solitons in this model satisfy all properties to be a soliton, they undergo a phase shift depending on which soliton was bigger (bigger moves forward, smaller moves back).