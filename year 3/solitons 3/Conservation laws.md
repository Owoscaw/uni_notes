
Conservation laws provide the most fundamental characterisation for a physical system; they tell us what quantities remain constant over time. In the context of solitons, they explain why the motion of [[Basic properties of Solitons|true solitons]] is so restricted. The general form of conservation law takes the form of a spatial integral of functions on $u$ and its derivatives:$$\Huge Q=\int_\Re\rho(u,u_x,\dots,u_t,\dots)dx,\,\,\frac{dQ}{dt}=0$$
# Standard methodology:

The standard method for constructing a conserved charge involves finding functions $\rho,j$ of $u$ and its derivatives such that the equations of motion for $u$ imply the local conservation law/continuity equation:$$\Huge \frac{\partial \rho}{\partial t}+\frac{\partial j}{\partial x}=0,\,\,j\to C\text{ as }x\to\pm\infty$$With the same constant $C$ at both $+\infty$ and $-\infty$. Then we see:$$\Huge \frac{d}{dt}\int_\Re\rho\,dx=\int_\Re\frac{\partial \rho}{\partial t}dx=-\int_\Re\frac{\partial j}{\partial x}dx=-[j]_{-\infty}^\infty=0$$Hence:$$\Huge Q=\int_\Re\rho\,dx$$is a conserved charge. The integrand $\rho$ is called the conserved charge density, and $j$ is called the conserved current density.

# Conserved quantities for [[Travelling Waves#The sine-Gordon equation|sine-Gordon]]:

We define the total energy:$$\Huge E=\int_\Re\varepsilon\,dx$$And ask if it is conserved for the sine-Gordon field, where the energy density is:$$\Huge \varepsilon=\frac{1}{2}u_t^2+\frac{1}{2}u_x^2+(1-\cos u)$$Here, $\varepsilon$ plays the role of $\rho$