
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

# Relativistic field equations:

For any relativistic field theory of a single scalar field $u$ in one spatial $(x)$ and one temporal $(t)$ dimension has the quantity:$$\Huge E=\int_\Re\varepsilon\,dx=\int_\Re\frac{1}{2}u_t^2+\frac{1}{2}u_x^2+V(u)dx$$conserved, given the equation of motion $u_{tt}-u_{xx}=-V'(u)$ is satisfied. The scalar potential $V(u)$ determines the specific theory:$$\Huge V(u)=\begin{cases}\frac{1}{2}m^2u^2&\text{Klein-Gordon} \\
1-\cos u&\text{sine-Gordon} \\
\frac{\lambda}{2}(u^2-a^2)^2&\phi^4\text{ theory} \\
\vdots\end{cases}$$
[[Symmetries, Noether's theorem, and conservation laws#Noether's theorem|Noether]] showed that the conservation of energy follows from the invariance of the theory under arbitrary time translations $t\rightarrow t+c$. Similarly, invariance under space translations $x\rightarrow x+c'$ implies the conservation of momentum.

We now make the switch to light-cone coordinates:$$\Huge x^\pm=\frac{1}{2}(t\pm x)\iff\begin{cases}t=x^++x^- \\
x=x^+-x^-\end{cases}$$which are named after the fact that trajectories of [[Spacetime and Tensors|light rays]] are $x^+=\text{constant}$ or $x^-=\text{constant}$ for left moving or right moving rays respectively. By the chain rule we can calculate:$$\Huge\partial_\pm=\frac{\partial }{\partial x_\pm}=\frac{\partial t}{\partial x^\pm}\frac{\partial }{\partial t}+\frac{\partial x}{\partial x^\pm}\frac{\partial }{\partial x}=\frac{\partial }{\partial t}\pm\frac{\partial }{\partial x}=\partial_t\pm\partial_x$$This implies $\partial_+\partial_-=\partial_t^2-\partial_x^2$, so we can write the equation of motion as:$$\Huge u_{+-}=-V'(u)$$Now suppose there exists a couple of densities $T,X$ such that given the equation of motion, we have:$$\Huge\partial_-T=\partial_+X$$Which is exactly the continuity equation in light-cone coordinates ($p=T-X,-j=T+X$). Provided that the limiting values of $-T-X$ as $x\to\pm\infty$ agree so that [[year 3/solitons 3/term 1/Conservation laws#Standard methodology|these]] equations hold, we have that:$$\Huge\int_\Re T-X\,dx$$is a conserved quantity. 

We aim to construct examples of such $(T,X)$ pairs. Suppose that $T$ is a polynomial in $x^+$-derivatives of $u$. That is, we are looking for polynomial conserved densities. We mostly disregard total $x^+$-derivatives in $T$, that is two polynomial conserved densities that differ by a total $x^+$-derivative are considered to be equivalent. If $(T,X)$ solves the continuity equation and $T'=T+\partial_+U$ then:$$\Huge\partial_-T'=\partial_-T+\partial_-\partial_+U=\partial_+X'$$where $X'=X+\partial_-U$. Hence $(T',X')$ is another solution to the continuity equation. As long as the limits of $U$ as $x\to\pm\infty$ are equal, the exact same conserved quantity is found:$$\Huge\begin{align*}
\int_\Re T'-X'\,dx-\int_\Re T-X\,dx&=\int_\Re\partial_+U-\partial_-U\,dx\\
&=\int_\Re2\partial_xU\,dx\\
&=[2U]_{-\infty}^\infty=0
\end{align*}$$
We define the rank/Lorentz spin of a single term in a general polynomial in $u$ and its light-cone derivatives as the number of $\partial_+$ derivatives minus the number of $\partial_-$ derivatives. For example, the polynomial $(u_+)^3u_-u_{++-}$ has Lorentz spin $3-1+(2-1)=3$. Special relativity dictates that objects of different spin transform differently under the Lorentz group of symmetries of relativistic field equations.

Note that terms with different Lorentz spins will never cancel against each other in the light-cone continuity equation, since using the equation of motion to convert an occurrence of $u_{+-}$ into $-V'(u)$ does not affect the rank. As a result of this, each spin can be considered separately and so for $s=0,1,\dots$ we look for different solutions $(T_{s+1},X_{s-1})$ to the continuity equation, where $T_{s+1}$ is a polynomial in the $x^+$-derivatives of $u$ with Lorentz spin $s+1$, where $X_{s-1}$ has Lorentz spin $s-1$. The corresponding conserved charge will be written as:$$\Huge Q_s=\int_\Re T_{s+1}-X_{s-1}\,dx$$
As $x\to\pm\infty$ we assume that all derivatives of $u$ tend to $0$, but $u$ itself may tend to other values. Note that for each pair $(T_{s+1},X_{s-1})$ the roles of $x^+,x^-$ can be swapped throughout to find a partner pair $(T_{-s-1},X_{-s+1})$ where $T_{-s-1}$ is a polynomial in $x^-$ derivatives with Lorentz spin $-s-1$. We now proceed spin by spin:
>$s=0$ implies that $T_1=u_+$, the unique polynomial density of spin $1$, up to a multiplicative factor that can be absorbed into the normalisation of the charge. This solves the continuity equation with $X_{-1}=u_-$, as:$$\Huge\partial_-u_+=u_{-+}=u_{+-}=\partial_+u_-$$The corresponding conserved charge is then the topological charge:$$\Huge Q_0=\int_\Re u_+-u_-\,dx=2\int_\Re u_x\,dx=2[u]_{-\infty}^\infty$$
>$s=1$ implies that $T_2\supset\{u_{++},u+^2\}$, that is $T_2$ is a linear combination of each term in the set. However we notice that $u_{++}=(u_+)_+$ is a total derivative, and since $u_+\to0$ as $x\to\pm\infty$ by our assumption, we disregard this term WLOG and consider $T_2=u_+^2$, then:$$\Huge\partial_-u_+^2=2u_+u_{+-}=-2V'(u)u_+=-2\partial_+V(u)=\partial_+X_0$$where we define $X_0=-2V(u)$. Therefore the quantity:$$\Huge Q_1=\int_\Re T_2-X_0\,dx=\int_\Re u_+^2+2V(u)dx$$is conserved for any $V$. Swapping $x^+$ and $x^-$ reveals $T_{-2}=u_-^2$ as another conserved density with the same $X_0$, giving another conserved quantity:$$\Huge Q_{-1}=\int_\Re T_{-2}-X_0\,dx=\int_\Re u_{-}^2+2V(u)dx$$Taking the sum and difference and normalising gives two more conserved charges:$$\Huge\begin{align*}
\frac{1}{4}(Q_1+Q_{-1})&=\int_\Re\frac{1}{4}(u_+^2+u_-^2)+V(u)dx\\
&=E=\int_\Re\frac{1}{2}(u_t^2+u_x^2)+V(u)dx\\
\frac{1}{4}(Q_{-1}-Q_1)&=\int_\Re\frac{1}{4}(u_-^2-u_+^2)dx\\
&=P=-\int_\Re u_tu_x\,dx
\end{align*}$$which are interpreted as the energy $E$, and momentum $P$.
>$s=2$ implies that $T_3\supset\{u_{+++},u_{++}u_+,u_+^3\}$, however $u_{+++}$ and $u_{++}u_+$ are clearly total derivatives of functions that vanish at spatial infinity and can be disregarded. So WLOG we take $T_3=u_+^3$ and:$$\Huge\partial_-u_+^3=3u_+^2u_{+-}=-3V'(u)u_+^2$$which cannot be a total $x^+$-derivative as the highest $x^+$ derivative of $u$ does not appear linearly. Therefore there are no conserved charges $Q_2$ of spin $2$ built out of polynomial conserved densities.
>$s=3$ implies that $T_4\supset\{u_{++++},u_{+++}u_+,u_{++}^2,u_{++}u_+^2,u_+^4\}$. We drop $u_{++++}$ and $u_{++}u_+^2$ as they are clearly total derivatives of functions that vanish at spatial infinity. Moreover $u_{+++}u_+=-u_{++}^2+(u_{++}u_+)_+$ so we disregard either $u_{+++}u_+$ or $u_{++}^2$ WLOG. The most general expression of $T_4$ up to a total $x^+$-derivative is therefore:$$\Huge T_4=u_{++}^2+\frac{1}{4}\lambda^2u_+^4$$where $\lambda$ is a constant that we determine:$$\Huge\begin{align*}
\partial_-T_4&=2u_{++}u_{++-}+\lambda^2u_+^3u_{+-}\\
&=-2u_{++}(V'(u))_+-\lambda^2u_+^3V'(u)\\
&=-2u_{++}u_+V''(u)-\lambda^2u_+^2V'(u)
\end{align*}$$Here, the highest derivative in the first term occurs linearly, allowing a total derivative to be extracted using a trick from integration by parts:$$\Huge\begin{align*}
\partial_-T_4&=-(u_+^2V''(u))_++u_+^3V'''(u)-\lambda^2u_+^3V'(u)\\
&=-(u_+^2V''(u))_++u_+^3(V'''(u)-\lambda^2V'(u))
\end{align*}$$Now as the $u_+$ term appears non-linearly in the second term, we have that this is a total $x_+$-derivative if and only if the factor:$$\Huge V'''(u)-\lambda^2V'(u)=0$$If this holds, we have $X_2=-u_+^2V''(u)$ and:$$\Huge Q_3=\int_\Re T_4-X_2\,dx=\int u_{++}^2+\frac{1}{4}\lambda^2u_+^4+u_+^2V''(u)dx$$is a conserved charge of spin $3$. If the factor does not equal zero, then there are no extra conserved charges of spin $3$.

In summary, the relativistic field theories of a single scalar field $u$ which have an extra conserved charge of spin $3$ are those with a scalar potential $V(u)$ that satisfies $V'''(u)-\lambda^2V'(u)$. We can examine the possibilities for values of $\lambda$:
> $\lambda^2=0$ implies that $V(u)=A+B(u-v_0)^2$, where $A,B$ are constant. Up to a linear redefinition of $u$, this scalar potential leads to the Klein-Gordon equation. This describes a free field and is not interesting.
> $\lambda^2=0$ implies that $V(u)=A+Be^{\lambda u}+Ce^{-\lambda u}$ where $A,B,C$ are constant:
> > If only one of $B,C$ are non-vanishing then the equation of motion becomes:$$\Huge C=0\implies u_{+-}=-B\lambda e^{\lambda u},\,\,B=0\implies u_{+-}=C\lambda e^{-\lambda u}$$By a linear redefinition of $u$, we can always rewrite the equation of motion as the Liouville equation:$$\Huge u_{+-}=e^u$$
> > If neither $B$ or $C$ vanish, then by a linear redefinition of $u$ we can write the equation of motion as either:
> > > The sine-Gordon equation if $\lambda^2<0$:$$\Huge u_{+-}=-\sin u$$
> > > The sinh-Gordon equation if $\lambda^2>0$:$$\Huge u_{+-}=\sinh u$$

The last two equations are special. They have hidden conservation laws that generic interacting relativistic field equations of the form $u_{+-}=-V'(u)$ lack. It is possible to show that the extra charge we found for the sine-Gordon equation is the first of an infinite sequence.