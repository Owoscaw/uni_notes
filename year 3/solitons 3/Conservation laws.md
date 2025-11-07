
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
\end{align*}$$That is, if $v$ solves:$$\Huge u_t+6(\lambda-v^2)v_x+v_{xxx}=0$$then $u$ solves the KdV equation. For $\lambda=0$ this reduces to the "wrong sign" KdV equation and:$$\Huge u=-v^2-v_x$$is known as the Miura transform, found by Miura in 1968. Gardner's idea was to change Miura's transform by setting:$$\Huge v=\epsilon w+\frac{1}{2\epsilon},\,\,\lambda=\frac{1}{4\epsilon^2}$$for some real constant $\epsilon\neq0$. Then:$$\Huge \lambda-v^2=\frac{1}{4\epsilon^2}-\left(\epsilon w+\frac{1}{2\epsilon}\right)^2=-w-\epsilon^2w^2$$which implies the relation between $u$ and $w$:$$\Huge u=-w-\epsilon w_x-\epsilon^2w^2$$known as the Gardner Transform.

In terms of $w$, the KdV equation becomes:$$\Huge \left(2\epsilon w+\frac{1}{\epsilon}+\frac{\partial }{\partial x}\right)(\epsilon w_t-6(w+\epsilon^2w^2)\epsilon w_x+\epsilon w_{xxx})=0$$or:$$\Huge \left(1+\epsilon\frac{\partial }{\partial x}+2\epsilon^2w\right)(w_t-6(w+\epsilon^2w^2)w_x+w_{xxx})=0$$In particular, any $w$ that solves the reduced equation:$$\Huge w_t-6(w+\epsilon^2w^2)w_x+w_{xxx}=0$$produces a field $u$ that solves the KdV equation via the Gardner transform. 

Now fix $u$ as a solution to the KdV equation, and we see that $w$ varies with $\epsilon$ so that the above equations hold:
> $\epsilon=0$ reduces the equation to the KdV equation with a reversed middle term, leading to $u=-w$.
> $\epsilon\neq0$ raises two issues:
> > To obtain $w$ in terms of $u$ we need to solve the differential equation described above.
> > The differential operator $1+\epsilon\frac{\partial }{\partial x}+2\epsilon^2w$ is non-trivial and therefore might have a non-vanishing kernel so we cannot immediately take the reduced equation as fact.

Gardner's insight was that we can remedy both issues by viewing $w$ as a formal power series in $\epsilon$:$$\Huge w(x,t)=\sum_{n=0}^\infty w_n(x,t)\epsilon^n=w_0(x,t)+w_1(x,t)\epsilon+\dots$$Substituting this into the relation between $u$ and $w$:$$\Huge\begin{align*}
u=&-(w_0+w_1\epsilon+\dots)-\epsilon(w_0+w_1\epsilon+\dots)_x\\
&-\epsilon^2(w_0+w_1\epsilon+\dots)^2\\
=&-w_0-\epsilon w_1-\epsilon^2w_2-\epsilon^3w_3+\dots\\
&-\epsilon w_{0,x}-\epsilon^2w_{1,x}-\epsilon^3w_{2,x}+\dots\\
&-\epsilon^2w_0^2-\epsilon^32w_0w_1+\dots
\end{align*}$$Since $u$ is fixed, it is of order $\epsilon^0$ and we can therefore compare terms:$$\Huge\begin{align*}
\epsilon^0&:w_0=-u\\
\epsilon^1&:w_1=-w_{0,x}=u_x\\
\epsilon^2&:w_2=-w_{1,x}-w_0^2=-u_{xx}-u^2\\
\epsilon^3&:w_3=-w_{2,x}-2w_0w_1=u_{xxx}+4uu_x\\
\vdots
\end{align*}$$Which recursively determines all of the coefficients $w_n$ in the power series in terms of $u$.

Since $w$ is a power series in $\epsilon$, the reduced equation in $w$ can also be written as a power series:$$\Huge (w_t-6(w+\epsilon^2w^2)w_x+w_{xxx})=z(x,t)=\sum_{n=0}^\infty z_n(x,t)\epsilon^n$$The same logic applies to the differential operator acting on this in the full equation:$$\Huge A=\mathbb{1}+\epsilon\frac{\partial }{\partial x}+2\epsilon^2w=\mathbb{1}+\sum_{n=1}^\infty A_n\epsilon^n$$Where $\mathbb{1}$ is the identity operator and each $A_n$ are linear differential operators with:$$\Huge A_1=\frac{\partial }{\partial x},\,\,A_2=2w_0,\,\,A_3=2w_1,\dots$$Now we can rewrite the full KdV equation in terms of $w$ as a multiplication between power series:$$\Huge\begin{align*}
0&=\left(\mathbb{1}+\sum_{n=1}^\infty A_n\epsilon^n\right)\left(\sum_{k=0}^\infty z_k\epsilon^k\right)\\
&=z_0+\epsilon z_1+\epsilon^2z_2+\epsilon^3z_3+\dots\\
&+\epsilon A_1z_0+\epsilon^2A_1z_1+\epsilon^3A_1z_2+\dots\\
&+\epsilon^2A_2z_0+\epsilon^3A_2z_1+\dots\\
&+\epsilon^3A_3z_0+\dots
\end{align*}$$which we solve order by order:$$\Huge\begin{align*}
\epsilon^0&:z_0=0\\
\epsilon^1&:z_1=-A_1z_0\\
\epsilon^2&:z_2=-A_1z_1-A_2z_0=0\\
\epsilon^3&:z_3=-A_1z_2-A_2z_1-A_3z_0=0\\
\vdots
\end{align*}$$Therefore we have shown that, order by order in $\epsilon$, the full KdV equation in $w$ holds. Now we notice that this is simply a continuity equation:$$\Huge \frac{\partial }{\partial t}w+\frac{\partial }{\partial x}(-3w^2-2\epsilon^2w^3+w_{xx})=0$$Since $w,w_x,w_{xx},\dots\to0$ as $x\to\pm\infty$ order by order in powers of $\epsilon$, the charge:$$\Huge \tilde Q=\int_\Re w\,dx$$is conserved. We write this in terms of the power series:$$\Huge\tilde Q=\int_\Re\sum_{n=0}^\infty w_n\epsilon^ndx=\sum_{n=0}^\infty\epsilon^n\int_\Re w_n\,dx=\sum_{n=0}^\infty\epsilon^n\tilde Q_n$$And since $\tilde Q$ is conserved for all $\epsilon$, it must hold that each $\tilde Q_n$ are conserved. Therefore we have shown that there are infinitely many conserved charges for the KdV equation, making it integrable.