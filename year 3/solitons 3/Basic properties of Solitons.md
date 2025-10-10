
# The KdV equation:

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

In general, $n$ balls in a row move to the right with speed $n$. This is the equivalent to the speed being proportional to the height of the soliton in the KdV equation.