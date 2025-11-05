
Conservation laws provide the most fundamental characterisation for a physical system; they tell us what quantities remain constant over time. In the context of solitons, they explain why the motion of [[Basic properties of Solitons|true solitons]] is so restricted. The general form of conservation law takes the form of a spatial integral of functions on $u$ and its derivatives:$$\Huge Q=\int_\Re\rho(u,u_x,\dots,u_t,\dots)dx,\,\,\frac{dQ}{dt}=0$$
# Standard methodology:

The standard method for constructing a conserved charge involves finding functions $\rho,j$ of $u$ and its derivatives such that the equations of motion for $u$ imply the local conservation law/continuity equation:$$\Huge \frac{\partial \rho}{\partial t}+\frac{\partial j}{\partial x}=0,\,\,j\to C\text{ as }x\to\pm\infty$$With the same constant $C$ at both $+\infty$ and $-\infty$. Then we see:$$\Huge \frac{d}{dt}\int_\Re\rho\,dx=\int_\Re\frac{\partial \rho}{\partial t}dx=-\int_\Re\frac{\partial j}{\partial x}dx=-[j]_{-\infty}^\infty=0$$Hence:$$\Huge Q=\int_\Re\rho\,dx$$is a conserved charge. The integrand $\rho$ is called the conserved charge density, and $j$ is called the conserved current density.

# Conserved quantities for [[Travelling Waves#The sine-Gordon equation|sine-Gordon]]:

We define the total energy:$$\Huge E=\int_\Re\varepsilon\,dx$$And ask if it is conserved for the sine-Gordon field, where the energy density is:$$\Huge \varepsilon=\frac{1}{2}u_t^2+\frac{1}{2}u_x^2+(1-\cos u)$$Here, $\varepsilon$ plays the role of $\rho$. We therefore aim to find a current density function that obeys a continuity equation with the limit condition above. The equation of motion for the sine-Gordon field is:$$\Huge u_{tt}-u_{xx}+\sin u=0$$We can then compute:$$\Huge\begin{align*}
\frac{\partial \varepsilon}{\partial t}&=u_tu_{tt}+u_xu_{xt}+\sin u\,u_t\\
&=u_t(u_{tt}+\sin u)+u_xu_{xt}\\
&=u_t(u_{xx})+u_xu_{xt}\\
&=\frac{\partial }{\partial x}(u_tu_x)=\frac{\partial }{\partial x}(-j)
\end{align*}$$Since boundary conditions for the sine-Gordon field imply $u_tu_x\to0$ as $x\to\pm\infty$ we deduce that energy is conserved:$$\Huge \frac{d}{dt}E=\frac{d}{dt}\int_\Re\varepsilon\,dx=\int_\Re \frac{\partial }{\partial x}(-j)dx=[-j]_{-\infty}^\infty=0$$
# Conserved quantities for [[Basic properties of Solitons#The KdV equation|KdV]]:

Recall the KdV field equation:$$\Huge u_t+6uu_x+u_{xxx}=0$$which can be rewritten as:$$\Huge \frac{\partial }{\partial t}(u)+\frac{\partial }{\partial x}(3u^2+u_{xx})=0$$Boundary conditions for the KdV equation force $u,u_x,u_{xx},\dots\to0$ as $x\to\pm\infty$, so we deduce that:$$\Huge Q_1=\int_\Re u\,dx$$is conserved. This is because we have written the equation of motion in the exact form of a continuity equation with $\rho=u,j=3u^2+u_{xx}$. Next we ask if $\rho=u^2$ is conserved:$$\Huge \begin{align*}
(u^2)_t&=2uu_t\\
&=-12u^2u_x-2uu_{xxx}\\
&=-4(u^3)_x-2uu_{xxx}\\
&=(-4u^2-2uu_{xx})_x+2u_xu_{xx}\\
&=(-4u^3-2uu_x+u_x^2)_x
\end{align*}$$Therefore:$$\Huge Q_2=\int_\Re u^2dx$$is conserved with $\rho=u^2,j=4u^3+2uu_x-u_x^2$. We now ask the same of $u^3$:$$\Huge\begin{align*}
(u^3)_t&=3u^2u_t\\
&=-18u^3u_x-3u^2u_{xxx}\\
\text{up to total }x\text{-derivative}&=6uu_xu_{xx}\\
&=-u_tu_{xx}-u_{xxx}u_{xx}\\
\text{up to total }x\text{-derivative}&=u_{tx}u_x=\frac{1}{2}(u_x^2)_t
\end{align*}$$So we rearrange to find a third conserved charge:$$\Huge Q_3=\int_\Re u^3-\frac{1}{2}u_x^2\,dx$$Here, $Q_1,Q_2,Q_3$ are interpreted as the mass, momentum, and energy of the wave respectively. Surprisingly, some old mathematicians found $8$ more conserved charges all of the form:$$\Huge Q_n=\int_\Re(u^n+\dots)dx$$This begs the questions:
> Are there infinitely many conserved charges?
> Is there a systematic way to find them?

# The Gardner transform:

Suppose that the KdV field $u(x,t)$ can be expressed in terms of another function:$$\Huge u=\lambda-v^2-v_x$$where $\lambda\in\Re$ is a parameter. Substituting this into the KdV equation:$$\Huge\begin{align*}
0&=(\lambda-v^2-v_x)_t+6(\lambda-v^2-v_x)(\lambda-v^2-v_x)_x+(\lambda-v^2-v_x)_{xxx}\\
&=\dots\\
&=-\left(2v+\frac{\partial }{\partial x}\right)(v_t+6(\lambda-v^2)v_x+v_{xxx})
\end{align*}$$That is, if $v$ solves:$$\Huge u_t+6(\lambda-v^2)v_x+v_{xxx}=0$$then $u$ solves the KdV equation.