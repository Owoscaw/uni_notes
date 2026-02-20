

# Deriving and generalising the [[Basic properties of Solitons#The KdV equation|KdV]] equation:

It is natural to ask if there are any other [[Evolving scattering data#Time evolution of scattering data|evolution equations]] for $u(x,t)$ such that the eigenvalues of$$\Huge L(u)=\frac{\partial^2}{\partial x^2}+u(x,t)$$are constant in time. That is, we are looking for equations such that each $L(u)$ at different times are isospectral. Such equations are known as isospectral flows. The idea of the [[Evolving scattering data#Lax pairs|Lax pair]] allows us to find them. 

Note that the only equivalence we needed to prove eigenvalues were constant in time was$$\Huge u_t=N(u)\iff L(u)_t=[M(u),L(u)]$$, no other information regarding $M$ was needed. Note that $M(u)$ is not completely arbitrary, as $L_t=u_t$ is a multiplicative operator, $[M,L]$ must also be a multiplicative operator. This means that all $D=\partial_x$ must cancel out in the commutator. If they do cancel, $[M,L]$ will be a polynomial in $u,u_x,u_{xx},\dots$. Setting this equal to $u_t$ gives the desired evolution equation.