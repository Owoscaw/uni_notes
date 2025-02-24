
Assume the existence of an [[Calculus of variations#Action principle|action]] $S[u,u_x,u_t]$ acting on one spatial and one temporal dimension. Here $u(x,t)\in\Re$ can be thought of as a map between $x,t$ and the reals, that is $u:\Re^2\mapsto\Re$. $u_x$ and $u_t$ are the [[Partial derivatives|partial derivatives]] of $u$ w.r.t. each variable. The action can be written as:$$\Huge S=\int L(u(x,t),u_x(x,t),u_t(x,t),x,t)dt\,dx$$Note that $x,t$ do not vary, they are not [[Calculus of variations#Configuration space and generalised coordinates|generalised coordinates]]. In the context of field theory:$$\frac{\partial }{\partial t}(f(u,u_x,u_t,x,t))=\lim_{\epsilon\to0}\frac{f(u(x,t+\epsilon),u_x(x,t+\epsilon),(u_t(x,t+\epsilon),x,t+\epsilon)-f(u,u_x,u_t,x,t)}{\epsilon}$$
# Euler-Lagrange equations for fields:

We claim that the transformation in the path $u_s\rightarrow u_s+\delta u$ causes the change in the action principle to be quadratic in $\delta u$, that is $\delta S=\mathcal{O}((\delta u)^2)$:$$\large\begin{align}
S=\int L(u,u_x,u_t,x,t)dt\,dx\rightarrow S'=\int L(u+\delta u,u_x+\delta u_x,u_t+\delta u_t,x,t)dt\,dx
\end{align}$$Now we [[Taylor series#Taylor's theorem|Taylor expand]] in $\delta u$:$$\large\begin{align}
S'&=S+\int\left(\frac{\partial L}{\partial u}\delta u+\frac{\partial L}{\partial u_x}\delta u_x+\frac{\partial L}{\partial u_t}\delta u_t\right)dt\,dx+\mathcal{O}((\delta u)^2)\\&=S+\int\left(\frac{\partial L}{\partial u}\delta u+\frac{\partial L}{\partial u_x}\frac{\partial }{\partial x}\left(\delta u\right)+\frac{\partial L}{\partial u_t}\frac{\partial }{\partial t}(\delta u)\right)dt\,dx+\mathcal{O}((\delta u)^2)\\
&=S+\int\frac{\partial L}{\partial u}\delta u-\frac{\partial }{\partial x}\left(\frac{\partial L}{\partial u_x}\right)\delta u-\frac{\partial }{\partial t}\left(\frac{\partial L}{\partial u_t}\right)\delta u+\frac{\partial }{\partial x}\left(\frac{\partial L}{\partial u_x}\right)\delta u\\
&+\frac{\partial }{\partial t}\left(\frac{\partial L}{\partial u_t}\right)\delta u\,\,dt\,dx\\
&=S+\int\delta u\left(\frac{\partial L}{\partial u}-\frac{\partial }{\partial x}\left(\frac{\partial L}{\partial u_x}\right)-\frac{\partial }{\partial t}\left(\frac{\partial L}{\partial u_t}\right)\right)dt\,dx+\int\delta u\frac{\partial L}{\partial u_x}dt\\
&+\int\delta u\frac{\partial L}{\partial u_t}dx\\
&=S+\int\delta u\left(\frac{\partial L}{\partial u}-\frac{\partial }{\partial x}\left(\frac{\partial L}{\partial u_x}\right)-\frac{\partial }{\partial t}\left(\frac{\partial L}{\partial u_t}\right)\right)dt\,dx\\
\delta S&=S'-S=\int\delta u\left(\frac{\partial L}{\partial u}-\frac{\partial }{\partial x}\left(\frac{\partial L}{\partial u_x}\right)-\frac{\partial }{\partial t}\left(\frac{\partial L}{\partial u_t}\right)\right)dt\,dx+\mathcal{O}((\delta u)^2)\\
&=\int\delta u(0)dt\,dx+\mathcal{O}((\delta u)^2)=\mathcal{O}((\delta u)^2)
\end{align}$$So we have the Euler-Lagrange equations:$$\Huge \frac{\partial L}{\partial u}-\frac{\partial }{\partial x}\left(\frac{\partial L}{\partial u_x}\right)-\frac{\partial }{\partial t}\left(\frac{\partial L}{\partial u_t}\right)=0$$Note that this applies for a continuous $u_x,u_t$ instead of the discrete coordinates for [[Lagrangians for classical mechanics|classical Lagrangians]]. Clearly with $n$ fields we have $n$ generalised equations of motion:$$\Huge \frac{\partial L}{\partial u^{(i)}}-\frac{\partial }{\partial x}\left(\frac{\partial L}{\partial u_x^{(i)}}\right)-\frac{\partial }{\partial t}\left(\frac{\partial L}{\partial u_t^{(i)}}\right)=0$$However if a field depends on more that one coordinate, we can replace $(t,x)$ with a set of $d$ coordinates $x_i$:$$\Huge \frac{\partial L}{\partial u^{(i)}}-\sum_{k=0}^d\frac{\partial }{\partial x_k}\left(\frac{\partial L}{\partial u_k^{(i)}}\right)=0$$For all $i$, where $u_k^{(i)}=\frac{\partial u^{(i)}}{\partial x_k}$.

# The wave equation in $d=1$:

We define the massless scalar action:$$\Huge L(u,u_x,u_t)=\frac{1}{2}\rho u_t^2-\frac{1}{2}\tau u_x^2$$Where the density ($\rho$) and tension ($\tau$) are positive. We can easily compute the Euler-Lagrange equations:$$\Huge\begin{align}
0&=\frac{\partial L}{\partial u}-\frac{\partial }{\partial t}\left(\frac{\partial L}{\partial u_t}\right)-\frac{\partial }{\partial x}\left(\frac{\partial L}{\partial u_x}\right)\\
&=0-\frac{\partial }{\partial t}(\rho u_t)-\frac{\partial }{\partial x}(-\tau u_x)\\
&=\rho u_{tt}-\tau u_{xx}
\end{align}$$Where $u_{tt},u_{xx}$ represent the second partial derivatives of $u$ with respect to $t,x$. This is known as the wave equation. This is sometimes written as:$$\Huge u_{tt}-c^2u_{xx}=0$$Where we define $c^2=\frac{\tau}{\rho}$. Now we look for a general solution to the equation in this form:

## D'Alembert's solution:
Let $x_+=x+ct,x_-=x-ct$ implying that $u=u(x_+(x,t),x_-(x,t))$, then we have:$$\Huge\begin{align}
u_t&=\frac{\partial u}{\partial t}=\frac{\partial u}{\partial x_+}\frac{\partial x_+}{\partial t}+\frac{\partial u}{\partial x_-}\frac{\partial x_-}{\partial t}\\
&=c\left(\frac{\partial u}{\partial x_+}-\frac{\partial u}{\partial x_-}\right)\\
u_{tt}&=\frac{\partial }{\partial t}(u_t)=c\frac{\partial }{\partial t}\left(\frac{\partial u}{\partial x_+}-\frac{\partial u}{\partial x_-}\right)\\
&=c\frac{\partial }{\partial t}\left(\frac{\partial u}{\partial x_+}\right)-c\frac{\partial }{\partial t}\left(\frac{\partial u}{\partial x_-}\right)\\
&=c\frac{\partial }{\partial x_+}\left(\frac{\partial u}{\partial x_+}\right)\frac{\partial x_+}{\partial t}-c\frac{\partial }{\partial x_-}\left(\frac{\partial u}{\partial x_+}\right)\frac{\partial x_-}{\partial t}\\
&=c^2\frac{\partial ^2u}{\partial x_+^2}-c^2\frac{\partial ^2u}{\partial x_+\partial x_-}-c\left(c\frac{\partial ^2u}{\partial x_+\partial x_-}-c\frac{\partial^2u}{\partial x_-^2}\right)\\
&=c^2\left(\frac{\partial ^2u}{\partial x_+^2}-2\frac{\partial ^2u}{\partial x_+\partial x_-}+\frac{\partial ^2u}{\partial x_-^2}\right)
\end{align}$$Similarly, one can show that:$$\Huge u_{xx}=\frac{\partial^2 u}{\partial x^2}=\frac{\partial ^2u}{\partial x_+^2}+2\frac{\partial ^2u}{\partial x_+\partial x_-}+\frac{\partial ^2u}{\partial x_-^2}$$Now the Euler-Lagrange equation becomes:$$\Huge 0=u_{tt}-c^2u_{xx}=-4c^2\frac{\partial ^2u}{\partial x_+\partial x_-}\implies\frac{\partial ^2u}{\partial x_+\partial x_-}$$Now by integrating with respect to $x_+$ first:$$\Huge \int\frac{\partial ^2u}{\partial x_+\partial x_-}dx_+=\frac{\partial u}{\partial x_-}=h(x_-)$$For some function $h:\Re\mapsto\Re$. Now integrating with respect to $x_-$ we get:$$\Huge \int\frac{\partial u}{\partial x_-}dx_-=u(x_+,x_-)=\int h(x_-)dx_-=f(x_-)+g(x_+)$$So we have:$$\Huge u(x_-,x_+)=f(x_-)+g(x_+)$$With $f(x_-)=\int h(x_-)dx_-$. Finally we can substitute $x$ back in and state the solution:$$\Huge u(x,t)=f(x-ct)+g(x+ct)$$For arbitrary function $f,g:\Re\mapsto\Re$.

## Solutions in terms of initial conditions:
Let $u(x,0)=\varphi(x)=f(x)+g(x)$ and $u_t(x,0)=\psi(x)=-cf'(x)+cg'(x)$. We have two equations, and two unknowns. To solve for $f,g$ notice that from the second condition we have:$$\huge -f(x)+g(x)=\frac{1}{c}\int_{-\infty}^x\psi(s)ds+d$$Now we can cancel terms with the first condition:$$\Huge\begin{align}
2g(x)&=\varphi(x)+d+\frac{1}{c}\int_{-\infty}^x\psi(s)ds\\
2f(x)&=\varphi(x)-d-\frac{1}{c}\int_{-\infty}^x\psi(s)ds
\end{align}$$Now we can substitute these into the original equation:$$\large u(x,t)=f(x-ct)+g(x+ct)=\frac{1}{2}\left(\varphi(x-ct)+\varphi(x+ct)+\frac{1}{c}\int_{x-ct}^{x+ct}\psi(s)ds\right)$$

# [[Symmetries, Noether's theorem, and conservation laws#Noether's theorem|Noether's theorem]] for fields:

We generalise the Lagrangians of the form:$$\Huge L(u,u_x,u_t)=\frac{1}{2}\rho u_t^2-\frac{1}{2}\tau u_x^2$$And work in $d$ space dimensions instead of the single $x$ dimension. We introduce coordinates $x_0,x_1,\dots,x_d$ where $(x_1,\dots,x_d)$ define the space and $x_0$ defines the time. So $u$ takes parameters $u(x_0,x_1,\dots,x_d)$.

We define a transformation acting on $u$ to be generated by:$$\Huge u\rightarrow u+\epsilon a(u)$$This beckons the notion of a transformation being symmetric if $\delta L=\mathcal{O}(\epsilon^2)$. Now that we have a notion of symmetry for fields, we can state Noether's theorem.

If $a(u)$ generates a symmetry then we have that:$$\Huge \underline{\nabla}\cdot(a\underline \Pi)=\sum_{i=0}^d\frac{\partial }{\partial x_i}(a\Pi_i)=0$$With $\underline{\nabla}\cdot(a\underline \Pi)$ representing the [[Differential operators#Differentiating vector fields|divergence]] of the vector field $a\underline\Pi$ where $a\underline\Pi$ is defined as the Noether current, equal to $a$ times the generalised momentum vector $\underline \Pi$ defined as:$$\Huge \Pi_i=\frac{\partial L}{\partial u_i},\,\,u_i=\frac{\partial u}{\partial x_i}$$Now to prove this theorem, we look at the variation of the Lagrangian density. Since $a(u)$ generates a symmetry we have that the variation of the Lagrangian density is of order $\mathcal{O}(\epsilon^2)$. We can compute this by looking at its expansion with respect to the variation of the fields:$$\Huge\begin{align} 
\delta L&=\frac{\partial L}{\partial u}\delta u+\sum_{i=0}^d\frac{\partial L}{\partial u_i}\delta u_i\\
&=\frac{\partial L}{\partial u}\epsilon a+\sum_{i=0}^d\frac{\partial L}{\partial u_i}\epsilon a_i\\
&=\epsilon\left(\frac{\partial L}{\partial u} a+\sum_{i=0}^d\frac{\partial L}{\partial u_i} a_i\right)\\
&=\epsilon\left(\sum_{i=0}^da\frac{\partial }{\partial x_i}\left(\frac{\partial L}{\partial u_i}\right)+\frac{\partial L}{\partial u_i}\frac{\partial a}{\partial x_i}\right)\\
&=\epsilon\sum_{i=0}^d\frac{\partial }{\partial x_i}\left(\frac{\partial L}{\partial u_i}a\right)
\end{align}$$Where we have used the fact $a_i=\frac{\partial a}{\partial x_i}$ and the fact that the summand became the total derivative of $\frac{\partial L}{\partial u_i}a$ with respect to $x_i$. Now since $\delta L$ vanishes to first order in epsilon, that is $\mathcal{O}(\epsilon^2)$, the sum must equal zero, so we get:$$\Huge \sum_{i=0}^d\frac{\partial }{\partial x_i}\left(\frac{\partial L}{\partial u_i}a\right)=\sum_{i=0}^d\frac{\partial }{\partial x_i}(a\Pi_i)=0$$Hence we have shown that $\underline{\nabla}\cdot\underline\Pi=0$, concluding the proof.

We can now give definition to the Noether current associated to a transformation generated by $a(u)$:$$\Huge \underline J=a\underline\Pi\implies J_i=a\Pi_i=a\frac{\partial L}{\partial u_i}$$Writing this as the Noether current we can rewrite Noether's theorem as:$$\Huge \sum_{i=0}^d\frac{\partial J_i}{\partial x_i}=0$$The Noether charge $Q$ is defined to be:$$\Huge Q=\int_{-\infty}^\infty\dots\int_{-\infty}^\infty J_0\,dx_1\dots dx_d$$Assuming that the space is defined by $\Re^d$ with coordinates $x_1,\dots,x_d$ and:$$\Huge \lim_{x_k\to\pm\infty}J_i=0$$For all $k,i\in\{1,\dots,d\}$. Under these assumptions one can prove that for a symmetry generated by some $a(u)$:$$\Huge \frac{d Q_a}{dt}=0$$Where $Q_a$ represents the Noether charge associated to the transformation generated by $a(u)$. To prove this observe:$$\large\begin{align}
\frac{d Q}{dt}&=\frac{d }{dt}\int_{-\infty}^\infty\dots\int_{-\infty}^\infty J_0\,dx_1\dots dx_d\\
&=\int_{-\infty}^\infty\dots\int_{-\infty}^\infty\frac{\partial J_0}{\partial x_0}dx_1\dots dx_d\\
&=-\int_{-\infty}^\infty\dots\int_{-\infty}^\infty\sum_{i=1}^d
\frac{\partial J_i}{\partial x_i}dx_1\dots dx_d\\
&=-\int_{-\infty}^\infty\dots\int_{-\infty}^\infty J_1(\infty)-J_1(-\infty)dx_2\dots dx_d-\sum_{i=2}^d\int_{-\infty}^\infty\dots\int_{-\infty}^\infty\frac{\partial J_i}{\partial x_i}dx_1\dots dx_d\\
&=-\sum_{i=1}^d\int_{-\infty}^\infty\dots\int_{-\infty}^\infty J_i(\infty)-J_i(-\infty)dx_{i-1}dx_{i+1}\dots dx_d\\
&=-\sum_{i=1}^d\int_{-\infty}^\infty\dots\int_{-\infty}^\infty 0\,dx_{i-1}dx_{i+1}\dots dx_d\\
&=-\sum_{i=1}^d0=0
\end{align}$$
So we have that $Q$ is indeed invariant in time.

Using the example of the one dimensional string with associated Lagrangian:$$\Huge L(u,u_x,u_t)=\frac{1}{2}\rho u_t^2-\frac{1}{2}\tau u_x^2$$We can define a symmetry $u\rightarrow u+\epsilon$ with $a=1,x_0=t,x_1=x$. Then the Noether current becomes:$$\Huge\begin{align} 
\underline J&=(a\Pi_0,a\Pi_1)=\left(a\frac{\partial L}{\partial u_t},a\frac{\partial L}{\partial x}\right)\\
&=(\rho u_t,-\tau u_x)
\end{align}$$Allowing the construction of the associated Noether charge:$$\Huge Q=\int_{-\infty}^\infty\rho u_t\,dx$$We can now check that this is indeed conserved:$$\Huge\begin{align}
\frac{d Q}{dt}&=\frac{d }{dt}\int_{-\infty}^\infty\rho u_t\,dx\\
&=\int_{-\infty}^\infty\frac{\partial }{\partial t}(\rho u_t)dx\\
&=\int_{-\infty}^\infty\rho u_{tt}\,dx\\
&=\tau\int_{-\infty}^\infty u_{xx}\,dx\\
&=\tau\int_{-\infty}^\infty\frac{\partial u_x}{\partial x}dx=\tau[u_x]_{-\infty}^\infty=\tau(0-0)=0
\end{align}$$Using the fact that $\rho u_{tt}=\tau u_{xx}$ and that the assumption $\lim_{x_k\to\pm\infty}\frac{\partial u}{\partial x_i}=0$.

# Energy-Momentum tensor:

Now that Noether's theorem has been generalised to work on a field, we can consider the generalisation of energy conservation for a field. The energy-momentum $T_{ij}$ tensor is defined to be:$$\Huge T_{ij}=\frac{\partial L}{\partial u_j}\frac{\partial u}{\partial x_i}-\delta_{ij}L$$Where $\delta$ is the [[Matrix definition#Special matrices|kroneker delta]] function. We then have the theorem:$$\Huge \sum_{j=0}^d\frac{\partial T_{ij}}{\partial x_j}=0$$To prove this, we simply compute using the chain rule:$$\Huge\begin{align}
\frac{\partial L}{\partial x_i}&=\frac{\partial L}{\partial u}\frac{\partial u}{\partial x_i}+\sum_{j=0}^d\frac{\partial L}{\partial u_j}\frac{\partial u_j}{\partial x_i}\\
&=\sum_{j=0}^d\left(\frac{\partial }{\partial x_j}\left(\frac{\partial L}{\partial u_j}\right)\frac{\partial u}{\partial x_i}+\frac{\partial L}{\partial u_j}\frac{\partial u_j}{\partial x_i}\right)\\
&=\sum_{j=0}^d\frac{\partial }{\partial x_j}\left(\frac{\partial L}{\partial u_j}\frac{\partial u}{\partial x_i}\right)=\sum_{j=0}^d\delta_{ji}\frac{\partial L}{\partial x_j}
\end{align}$$Where we have noticed the total derivative inside the summand. This implies that:$$\Huge\begin{align}
\sum_{j=0}^d\left(\frac{\partial }{\partial x_j}\left(\frac{\partial L}{\partial u_j}\frac{\partial u}{\partial x_i}-\delta_{ij}L\right)\right)&=0\\
\sum_{j=0}^d\frac{\partial T_{ij}}{\partial x_j}&=
\end{align}$$Using the definition of $T_{ij}$, as required.

We take the one dimensional string as an example again. Computing the energy-momentum tensor we have:$$\Huge T_{00}=T_{tt}=\frac{\partial L}{\partial u_t}u_t-\delta_{00}L=\rho u_t^2-L=\frac{1}{2}\rho u_t^2+\frac{1}{2}\tau u_x^2$$We define such quantity as the energy density of the system. One can compute the other indices:$$\Huge T_{01}=T_{tx}=\frac{\partial L}{\partial u_x}\frac{\partial u}{\partial t}-\delta_{01}L=(-\tau u_x)u_t$$And show that:$$\Huge T=\begin{pmatrix}\frac{1}{2}\rho u_t^2+\frac{1}{2}\tau u_x^2&\tau u_xu_t\\\rho u_xu_t&-\frac{1}{2}\rho u_t^2-\frac{1}{2}\tau u_x^2\end{pmatrix}$$Now we can say that:$$\Huge \sum_{j=0}^d\frac{\partial }{\partial x_j}T_{ij}=\frac{\partial }{\partial x_0}T_{i0}+\frac{\partial }{\partial x_1}T_{i1}=0$$Now we observe each case for $i$:$$\Huge \begin{align}
\frac{\partial }{\partial x_0}T_{00}+\frac{\partial }{\partial x_1}T_{01}&=\frac{\partial }{\partial t}T_{tt}+\frac{\partial }{\partial x}T_{tx}=0\\
\frac{\partial }{\partial x_0}T_{10}+\frac{\partial }{\partial 1}T_{11}&=\frac{\partial }{\partial t}T_{xt}+\frac{\partial }{\partial x}T_{xx}=0
\end{align}$$These are the conservation laws for this energy-momentum tensor describing the one dimensional string. Now we can define the energy quantity:$$\Huge E_{(a,b)}(t)=\int_{a}^b\frac{1}{2}\rho u_t^2+\frac{1}{2}\tau u_x^2\,dx$$To represent the total energy contained within an interval along the string. Now notice that:$$\Huge\begin{align} 
E_{(a,b)}(t)&=\int_a^bT_{tt}\,dx\\\implies\frac{d }{dt}E_{(a,b)}&=\int_a^b\frac{\partial T_{tt}}{\partial t}dx=-\int_a^b\frac{\partial }{\partial x}T_{tx}dx\\
&=-[T_{tx}]_a^b\\
&=[\tau u_xu_t]_a^b=T_{tx}(a)-T_{tx}(b)
\end{align}$$So we see that the rate of energy flow through the interval $(a,b)$ is equal to a sort of energy flow vector associated with $T_{tx}$ at the boundaries of the interval. How interesting. Taking $(a,b)=\Re$ we see that:$$\Huge \frac{d E_\Re}{dt}=[\tau u_xu_t]_{-\infty}^\infty=\tau u_x(\infty)u_t(\infty)-\tau u_x(-\infty)u_t(-\infty)=0-0=0$$Using the assumption that the limit of each coordinate is zero. We have shown that the total energy of the string is zero.

# Monochromatic waves and Flux:

We define a right moving monochromatic wave to be a solution of the wave equation, $u_{tt}=c^2u_{xx}$ of the form:$$\Huge u(x,t)_k=\Re(Ae^{ik(x-ct)})=\Re(|A|e^{ik(x-ct)+\theta})=|A|\cos(ik(x-ct)+\theta)$$There is a similar definition of a left moving monochromatic wave using $x+ct$ in the exponential. Considering the energy flow vector found above, we compute partial derivatives:$$\Huge\begin{align}
T_{tx}&=-\tau u_xu_t\\
u_x&=-k|A|\sin(k(x-ct)+\theta)\\
u_t&=kc|A|\sin(k(x-ct)+\theta)\\
T_{tx}&=\tau k^2|A|^2c\sin^2(k(x-ct)+\theta)\geq0
\end{align}$$This motivates the notion of an average energy flow:$$\Huge \frac{kc}{2\pi}\int^{\frac{2\pi}{kc}}_0T_{tx}\,dt=\frac{1}{2}\tau ck^2|A|^2>0$$With left moving monochromatic waves, we get the opposite direction inequalities. 

# Boundaries:

Previously we considered the one dimensional string across the whole real line. We now restrict this to a string from $x=-\infty$ to $x=0$. We assume that no energy is transferred from the string to the boundary, that is there is no energy flux to the boundary:$$\Huge\lim_{x\to0^-}T_{tx}(x,t)=\lim_{x\to0^-}(-\tau u_xu_t)=0$$This can be satisfied by letting:
>$\lim_{x\to 0^-}u_t(x,t)=0$
>$\lim_{x\to0^-}u_x(x,t)=0$

## Dirichlet's boundary condition:
We consider $\lim_{x\to0^-}u_t(x,t)=0$, that is $u_t(0,t)=0$ as we only consider smooth functions. Imposing this condition makes D'Alembert's solution:$$\Huge u(x,t)=f(x-ct)+h(-x-ct)$$With $h(\zeta)=g(-\zeta)$ and $u_t(0,t)=0\implies u(0,t)$ is constant. For convenience, we choose this constant to be $0$:$$\Huge u(0,t)=f(-ct)+h(-ct)=0\implies f(\zeta)=-h(\zeta)$$Allowing us to write D'Alembert's solution as:$$\Huge u(x,t)=f(x-ct)-f(-x-ct)$$That is, $f$ is an odd function for constant time, $u(x,t)=-u(-x,t)$:![[year 2/term 1/drawings/dirichlet]]
## Neumann's (free) boundary condition:
We consider $\lim_{x\to0^-}u_x(x,t)=u_x(0,t)=0$. We write D'Alembert's solution in the same form but now consider the condition on $u_x$:$$\Huge u_x(0,t)=f'(-ct)-h'(-ct)=0$$Therefore $f(\zeta)=h(\zeta)+\text{constant}$, we choose said constant to be $0$. Now the displacement becomes:$$\Huge u(x,t)=f(x-ct)+f(-x-ct)$$So we have $u(x,t)=u(-x,t)$, $u$ is an even function:![[neumann]]

# Junctions:

The natural extension of boundaries are junctions. Instead of not letting any energy flow through the boundary, we impose a junction condition to allow some energy transfer. This will result in the wave propagating past the junction as well as reflecting at the junction. This can be modelled by a spring between $u(0,t)$ and $(0,0)$. We then require:
> $\lim_{x\to0^-}u(x,t)=\lim_{x\to0^+}u(x,t)$
> The total energy of the string is conserved at $x=0$. Considering a small interval $(-\epsilon,\epsilon)$ around $x=0$:$$\Huge \lim_{\epsilon\to0}E_{(-\epsilon,\epsilon)}=\frac{1}{2}\kappa(u(0,t))^2$$

![[junction]]

By definition of energy flux we know:$$\Huge \frac{d }{dt}\left(\lim_{\epsilon\to0}E_{(-\epsilon,\epsilon)}\right)=\lim_{x\to0^-}T_{tx}(x,t)-\lim_{x\to0^+}T_{tx}(x,t)$$Our solution then takes form:$$\Huge u(x,t)=\begin{cases}\Re((e^{ipx}+Re^{-ipx})e^{-ipct})&x\leq0\\\Re(Te^{ipx}e^{-ipct})&x>0\end{cases}$$Notice the two cases for the reflected and transmitted wave. Continuity condition implies:$$\Huge\begin{align}
\lim_{x\to0^-}u(x,t)&=\lim_{x\to0}\Re((e^{ipx}+Re^{-ipx})e^{-ipct})\\
&=\Re((1+R)e^{-ipct})\\
&=\Re(Te^{-ipct})\\
&=\lim_{x\to0}\Re(Te^{ipx}e^{-ipct})=\lim_{x\to0^+}u(x,t)
\end{align}$$This must hold for all time, so $u_t$ must also be continuous. That is to say:$$\Huge T=1+R\implies\lim_{x\to0^-}u_t(x,t)=\lim_{x\to0^+}u_t(x,t)$$Using this, we can simplify the second junction condition by taking the time derivative of energy:$$\Huge\begin{align} 
\frac{d }{dt}\left(\lim_{\epsilon\to0}E_{(-\epsilon,\epsilon)}\right)&=\frac{d}{dt}\left(\frac{1}{2}\kappa(u(0,t))^2\right)=\kappa u(0,t)u_t(0,t)\\
\implies\kappa u(0,t)u_t(0,t)&=-\tau u_t(0,t)\left(\lim_{x\to0^-}u_x(x,t)-\lim_{x\to0^+}u_x(x,t)\right)\\
\implies\kappa u(0,t)&=-\tau\left(\lim_{x\to0^-}u_x(x,t)-\lim_{x\to0^+}u_x(x,t)\right)\\
\implies\kappa\Re(Te^{-ipct})&=\tau\left(\Re(ipTe^{-ipct})-\Re(ip(1-R)e^{-ipct})\right)\\
&=\tau\Re(ip(T+R-1)e^{-ipct})\\
\implies\kappa T&=\tau ip(T+R-1)\\
\implies R&=\frac{\kappa}{2ip\tau-\kappa},\,\,T=\frac{2ip\tau}{2ip\tau-\kappa}
\end{align}$$Now we have solved for the parameters that determine the reflected and transmitted waves. To make sure that this answer is reasonable, we take some limits on the parameters:
> Taking $\kappa\to0$ we would expect the wave to propagate through the junction with no energy loss. That is, there is no reflected wave and the full wave is transmitted:$$\Huge R=\frac{0}{2ip\tau-0}=0,\,\,T=\frac{2ip\tau}{2ip\tau-0}=1$$As expected.
> Taking $\kappa\to\infty$ we would expect no transmitted wave and the full reflected wave:$$\Huge R=\frac{\infty}{2ip\tau-\infty}=-1,\,\,T=\frac{2ip\tau}{2ip\tau-\infty}=0$$So we see that no wave is transmitted, and the entire wave is reflected at the junction with opposite orientation. This is equivalent to [[Fields and the wave equation#Dirichlet's boundary condition|Dirichlet's boundary condition]].
> We can now consider the limits of energy flux, given by $\frac{1}{2}\tau cp^2$. The limiting cases here are $p=0$, the wave carries no energy, and $p\to\infty$. We first take $p=0$:$$\Huge R=\frac{\kappa}{0-\kappa}=-1,\,\,T=\frac{0}{0-\kappa}=0$$The wave is fully reflected with opposite orientation. This is equivalent to Dirichlet's boundary condition as relative to the wave, the spring may as well be a boundary.
> Now we take $p\to\infty$:$$\Huge R=\frac{\kappa}{\infty-\kappa}=0,\,\,T=\frac{\infty}{\infty-\kappa}=1$$The wave is fully transmitted through the junction. Relative to the very energetic wave, the spring may as well not be there as it takes so little (relative) energy to excite.