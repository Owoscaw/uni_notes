
# Special relativity:

The symmetries we expect for our field theory form the [[Spacetime and Tensors#Lorentz group|Poincare group]] (rotations, boosts, translations). These come from special relativity, working in the space $\Re^{1,3}$ with metric signature $(-,+,+,+)$. Special relativity is based on two principles:
> All laws of physics are the same in all inertial frames
> The speed of light is the same in all inertial frames

We denote a general element of our space as $(t,x,y,z)=X^\mu\in\Re^{1,3}$. Our Lorentz boost in $x^1$ then looks like:$$\Huge X^\mu\to X^{'\mu}=\begin{pmatrix}x^{'0} \\ x^{'1}\\ x^{'2} \\ x^{'3}\end{pmatrix}=\gamma\begin{pmatrix}x^0-vx^1 \\ x^1-vx^0 \\ x^2-vx^0 \\ x^3-vx^0\end{pmatrix}$$In the rest frame of the particle, the worldline is parametrised by $(x^0,x^1,x^2,x^3)=(z,0,0,0)$. In the rest frame of an observer, the worldline is parametrised by $(x^0,x^1,x^2,x^3)=(\gamma z,-v\gamma z,0,0)$. 

A photon has a worldline parametrised by$$\Huge\begin{pmatrix}x^0 \\ x^1 \\ x^2 \\ x^3\end{pmatrix}=\begin{pmatrix}z \\ z \\ 0 \\ 0\end{pmatrix}\to\begin{pmatrix}x^{'0} \\ x^{'1}\\ x^{'2} \\ x^{'3}\end{pmatrix}=\gamma\begin{pmatrix}(1-v)z \\ (1-v)z \\ 0 \\ 0\end{pmatrix}$$
We define the Minkowski metric as$$\Huge\eta_{\mu\nu}=\begin{pmatrix}-1  & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}_{\mu\nu}$$so that we can write a covector:$$\Huge X_\mu=(x_0,x_1,x_2,x_3)=\eta_{\mu\nu}X^\nu=(-x^0,x^1,x^2,x^3)_\mu$$Note that the Minkowski metric satisfies $\eta^{\mu\nu}\eta_{\nu\rho}=\delta^\mu_\rho$. We can then define our pseudo inner product on $X^\mu,Y^\mu\in\Re^{1,3}$:$$\Huge X\cdot Y=X^\mu Y_\mu=X^\mu\eta_{\mu\nu}Y^\nu=X^T\eta Y$$We now find the linear transformations $\Lambda$ of $\Re^{1,3}$ leaving this inner product invariant, after some calculation:$$\Huge\begin{aligned}
\Lambda^T\eta\Lambda&=\eta\\
\Lambda_\nu^\mu\eta_{\mu\rho}\Lambda^\rho_\sigma=\eta_{\nu\sigma}
\end{aligned}$$These form the [[Lie Groups and Algebras#Lie groups|Lie group]] $O(1,3)$, satisfying the properties:
> $det\Lambda=\pm1$
> $\Lambda^\mu_\nu\eta_{\mu\rho}\Lambda^{\rho}_\sigma=\eta_{\nu\sigma}$, setting $\nu=\sigma=0$ shows us:$$\Huge(\Lambda_0^0)^2-(\Lambda_1^1)^2-(\Lambda_2^2)^2-(\Lambda_3^3)^2=1$$

This suggests an obvious decomposition into $4$ disconnected components as$$\Huge (\Lambda_0^0)^2\geq1\implies\Lambda_0^0\geq1\text{ or }\Lambda_0^0\leq-1$$combined with $\det\Lambda=\pm1$ gives $4$ total combinations. We are interested in $SO(1,3)^+$, the proper orthochronous Lorentz group:$$\Huge SO(1,3)^+=\{\Lambda\in O(1,3):\det\Lambda=1,\Lambda_0^0\geq1\}$$
## Lie group/algebra of $SO(1,3)^+$:
Let us consider elements in $SO(1,3)^+$ close to the identity $\Lambda^\mu_\nu=\delta_\nu^\mu\in SO(1,3)^+$. Consider the Lorentz algebra$$\Huge\Lambda_\mu^\nu=\delta^\mu_\nu+\epsilon M^\mu_\nu+\mathcal{O}(\epsilon)^2$$and apply our condition for being in the group. This imposes a condition on $M$:$$\Huge M_{\sigma\nu}+M_{\nu\sigma}=0$$This leaves $6$ DOF, and therefore we have $6$ basis elements that form our space of matrices. One such basis is given by:$$\Large(M^{\rho\sigma})_{\mu\nu}=\delta_\mu^\sigma\delta_\nu^\rho-\delta_\mu^\rho\delta_\nu^\sigma$$Note that this does indeed produce exactly $6$ basis elements, due to the antisymmetry of $M$. Moving a $\mu$ index up, we get our $6$ Lorentz generators:$$\Large (M^{\rho\sigma})^\mu_\nu=\eta^{\sigma\mu}\delta^\rho_\nu-\eta^{\rho\mu}\delta^\sigma_\nu$$
The most general element of the Lorentz algebra $\mathcal{M}$ such that $\Lambda=\exp(\mathcal{M})\in SO(1,3)^+$ is one that satisfies$$\Huge\mathcal{M}(\omega_{\rho\sigma})=\omega_{\rho\sigma}M^{\rho\sigma}$$, where $\omega_{\rho\sigma}\in\Re$ are parameters such that $\omega_{\rho\sigma}=-\omega_{\sigma\rho}$. $3$ of these parameters describe angles of rotation, while the other $3$ describe boosts along each axis.

We wish to understand how we can compose Lorentz transformations. We do this using the Baker-Campbell-Hausdorff formula, which states:$$\Huge e^A\cdot e^B=e^{A+B+\frac{1}{2}[A,B]+\dots}$$So it is necessary to find the commutator $[M^{\mu\nu},M^{\rho\sigma}]$, which we have luckily already done:$$\Large [M^{\mu\nu},M^{\rho\sigma}]=-\eta^{\nu\rho}M^{\mu\sigma}+\eta^{\mu\rho}M^{\nu\rho}+\eta^{\nu\sigma}M^{\mu\rho}-\eta^{\mu\sigma}M^{\nu\rho}$$This is known as the Lorentz algebra, and can be used to find the composition of any two Lorentz transformations.

Consider the matrix$$\Huge (M^{01})^\mu_\nu=\begin{pmatrix}0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}^\mu_\nu$$, we choose a Lorentz transformation parameter $\omega_{\rho\sigma}$ with $\omega_{01}=\omega/2$  ($\omega\in\Re$ generic parameter) and $\omega_{\rho\sigma}=0$ otherwise. Our transformation matrix then becomes:$$\Large\begin{aligned}
\Lambda_B(\omega)&=\exp(\omega_{\rho\sigma}M^{\rho\sigma})\\
&=\exp(\omega_{01}M^{01})\\
&=\sum_{n=0}^\infty\frac{(\omega M^{01})^n}{n!}=\begin{pmatrix}\cosh\omega & \sinh\omega & 0 & 0\\
\sinh\omega & \cosh\omega & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\end{pmatrix}
\end{aligned}$$Note that this choice of parameters is equivalent to a boost in the $x$-direction. Similarly $M^{02},M^{03}$ represent boosts in the $y,z$ directions respectively. Now consider what happens when we choose two spatial coordinates:$$\Large\begin{aligned}
\Lambda_R(\tilde\omega)&=\exp(\tilde\omega M^{23})\\
&=\sum_{n=0}^\infty\tilde\omega^n\frac{(M^{23})^n}{n!}=\begin{pmatrix}1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & \cos\tilde\omega & -\sin\tilde\omega\\
0 & 0 & \sin\tilde\omega & \cos\tilde\omega\end{pmatrix}
\end{aligned}$$Here, we use the fact $(M^{23})^2=\begin{pmatrix}0 & 0 \\ 0 & -\mathbb{1}\end{pmatrix}$ and $(M^{23})^3=-M^{23}$, splitting the sum into even and odd parts. 

## Time reversal and parity:
There are two transformations that are not in $SO(1,3)^+$ but are still Lorentz transformations:
> Time reversal:$$\Large T:(x^0,x^1,x^2,x^3)\to(-x^0,x^1,x^2,x^3),\,\,\Lambda_T=\text{diag}(-1,1,1,1)$$Parity:$$\Large P:(x^0,x^1,x^2,x^3)\to(x^0,-x^1,-x^2,-x^3),\,\,\Lambda_P=\text{diag}(1,-1,-1,-1)$$

We can then recover the full Lorentz group $O(1,3)$ by composing time reversal, parity, and their composition with elements of $SO(1,3)^+$. The most general element $\tilde\Lambda\in O(1,3)$ is written as:$$\Huge\tilde\Lambda=\Lambda_T^{n_T}\Lambda_P^{n_P}$$Here, $n_T,n_P\in\{0,1\}$. 

# Poincare group and scalar fields:

We now consider translations, which are transformations of the form:$$\Large x^\mu\rightarrow x'^\mu=x^\mu-a^\mu,\,\,a^\mu\in\Re^{1,3}$$The Lorentz group, together with this translation group, form the Poincare group. This group acts on spacetime coordinates as:$$\Large x^\mu\rightarrow x'^\mu=\Lambda^\mu_\nu x^\nu-a^\mu$$This group has $10$ generators, $6$ of which given by Lorentz generators, $4$ of which come from translations $P^\mu$. In addition to our $M$ matrix commutator, we get two more conditions to form the Poincare algebra:$$\Large\begin{aligned}
[P^\mu,P^\nu]&=0\\
[P^\mu,M^{\nu\rho }]&=-\eta^{\mu\nu}P^\rho+\eta^{\mu\rho}P^\nu
\end{aligned}$$
Consider a scalar field $\phi:\Re^{1,3}\rightarrow\Re$ transforming under the Poincare group, $\phi:x^\mu\rightarrow\phi(x^\mu)$. This transforms in the scalar representation of the Poincare group:$$\Large\begin{aligned}
x^\mu&\rightarrow x'^\mu=\Lambda^\mu_\nu x^\nu-a^\mu\\
\phi(x^\mu)&\rightarrow\phi'(x^\mu)=\phi(x^\mu)
\end{aligned}$$We want to find conditions on $\phi$ that make it transform in this way. Consider what the above statement is saying:$$\Large\phi'(x')=\phi'(x-a)=\phi(x)\implies\phi'(x)=\phi(x+a)$$Assuming $a$ is infinitesimally small, we can write:$$\Large\phi'(x)=\phi(x)+a^\mu\frac{\partial }{\partial x^\mu}\phi(x)+\mathcal{O}(a^2)$$We then find our variation in $\phi$:$$\Large\begin{aligned}
\delta\phi(x)&=\phi'(x)-\phi(x)\\
&=a^\mu\frac{\partial }{\partial x^\mu}\phi(x)
\end{aligned}$$We should expect to find some operator $\tilde P_\mu$ such that:$$\Large\begin{aligned}\phi'(x)=\phi(x+a)&=\exp(a^\mu\tilde P_\mu)\phi(x)\\
&=\phi(x)+a^\mu\tilde P_\mu\phi(x)+\mathcal{O}(a^2)\\
\implies\tilde P_\mu&=\frac{\partial }{\partial x^\mu}\end{aligned}$$This is the momentum operator, and generates translations.

## Lorentz group on scalar fields:
Let us show the same process for Lorentz transformations:$$\Large\begin{aligned}
x'^\mu&=\Lambda^\mu_\nu x^\nu\\
&=\exp(\omega_{\rho\sigma}M^{\rho\sigma})^\mu_\nu x^\nu\\
\implies\phi'(x')&=\phi'(\Lambda x)=\phi(x)\\
\implies\phi'(x)&=\phi(\Lambda^{-1}x)\\
&=\phi(\exp(-\omega_{\rho\sigma}M^{\rho\sigma})x)\\
&=\exp(\omega_{\rho\sigma}L^{\rho\sigma})\phi(x)
\end{aligned}$$Now let us expand the exponential to linear order (i.e. consider $\omega\to0$):$$\Large\begin{aligned}
\phi'(x)&=\phi(x-\omega_{\rho\sigma}M^{\rho\sigma}x+\mathcal{O}(\omega^2))\\
_\text{Taylor on phi}&=\phi(x)-(\omega_{\rho\sigma}M^{\rho\sigma})^\mu_\nu x^\nu\partial_\mu\phi+\mathcal{O}(\omega^2)\\
_\text{Taylor on exp}&=\phi(x)+\omega_{\rho\sigma}L^{\rho\sigma}\phi(x)+\mathcal{O}(\omega^2)\\
\implies\delta\phi(x)&=\omega_{\rho\sigma}L^{\rho\sigma}\phi(x)\\
&=-(\omega_{\rho\sigma}M^{\rho\sigma})_\nu^\mu x^\nu\partial_\mu\phi(x)
\end{aligned}$$Substituting our basis for $(M^{\rho\sigma})_\nu^\mu=\eta^{\rho\mu}\delta^\rho_\nu-\eta^{\rho\mu}\delta^\sigma_\nu$ (EX!!!) gives us our relation:$$\Huge L^{\rho\sigma}=x^\sigma\partial_\rho-x^\rho\partial_\sigma$$This is exactly our generator of Lorentz transformations on scalar fields. If one can be bothered to compute every commutator between our generators for the Poincare and Lorentz groups, one would find that they satisfy the Poincare algebra we found previously.

# Classical field theory:

In a classical system of $N$ degrees of freedom with generalised coordinates $\underline{q}_a$, our Lagrangian is simply given by:$$\Large\mathcal{L}(q_1,\dots,q_N,\dot q_1,\dots,\dot q_N)=\sum_{a=1}^N\frac{1}{2}m_a\dot q_a^2-V(q_1,\dots,q_N)$$This is just kinetic minus potential terms. Recall the action, defined by the integral$$\Huge S[q_a]=\int_{T_i}^{T_f}\mathcal{L}(\underline{q}_a,\underline{\dot q}_a)dt$$Equations of motion then arise from extremising the action:$$\Large\delta_qS[q_a]\implies\frac{\partial \mathcal{L}}{\partial q_a}-\frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot q_a}\right)=0$$
Now for our scalar fields $\phi(x,t)$, the generalised coordinates become our scalar field and the sum over kinetic terms becomes an integral:$$\Huge L=\int\mathcal{L}(\phi(x^\nu),\partial_\mu\phi(x^\nu))d^3x$$This makes the action:$$\Huge S=\int\mathcal{L}(\phi,\partial_\mu\phi)d^4x$$
The principle of locality demands there be no action at a distance. If we demand$$\Huge\delta_\phi S[\phi]=\int\delta_\phi\mathcal{L}(\phi,\partial_\mu\phi)d^4x=0$$we can write:$$\Large\begin{aligned}
\int\delta\phi\frac{\partial \mathcal{L}}{\partial \phi}+\partial_\mu(\delta\phi)\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi)}d^4x&=0\\
\int\delta\phi\left(\frac{\partial \mathcal{L}}{\partial \phi}-\partial_\mu\left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi)}\right)\right)d^4x&=\\
\implies\frac{\partial \mathcal{L}}{\partial \phi(x)}-\partial_\mu\left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi(x))}\right)&=0
\end{aligned}$$These are the Euler-Lagrange equations for our scalar field $\phi$.

## Actions for real scalar fields:
Firstly, let us impose all of our symmetries (i.e. invariance under Poincare). We first ask if our differential $d^4x$ transforms?
> Under translations $x\to x'-a$, $d^4x\to d^4x$ trivially.
> Under Lorentz transformations $x\to x'=\Lambda x$, $d^4$ transforms with the determinant. That is, $d^4x'=|\det\Lambda|d^4x=d^4x$

Since our differential is invariant, and the Lagrangian is defined to be invariant, we must also have that our action is invariant under the Poincare group.

Secondly, we impost non-trivial dynamics. That is, we require $\mathcal{L}=\mathcal{L}(\phi,\partial_\mu\phi)$ otherwise if we had $\mathcal{L}=\mathcal{L}(\phi)$, equations of motion would give us trivial dynamics:$$\Huge\mathcal{L}(\phi,\partial_\mu\phi)=\frac{1}{2}\partial_\mu\phi\partial^\mu\phi-V(\phi)$$This is analogous to our kinetic minus potential example above. In component form, we can write our general Lagrangian as:$$\huge\mathcal{L}=\frac{1}{2}(\partial_t\phi)^2-\frac{1}{2}(\nabla\phi)\cdot(\nabla\phi)-V(\phi)$$Really, the first term here is the only "kinetic term" while the rest can be thought of as potential terms. Our simplest possible Lagrangian has us introduce the mass term,$$\Huge V(\phi)=\frac{1}{2}m^2\phi^2\,\,\leftarrow\text{  mass term}$$Putting this all together, we find our Lagrangian for a free, massive scalar:$$\Huge\mathcal{L}=-\frac{1}{2}\partial_\mu\phi\partial^\mu\phi-\frac{1}{2}m^2\phi^2$$The EOM of this are simply the Klein-Gordon equations.

# [[Symmetries, Noether's theorem, and conservation laws#Noether's theorem|Noether's theorem]]:

Noether's theorem forms the link between continuous symmetries and conserved currents, one of the most important results in mathematical physics.

## Continuous symmetries:
Consider a free massive complex scalar field. The action is invariant under phase rotations of $\Phi$, by construction:$$\huge\Phi\to e^{i\alpha}\Phi,\,\,\bar \Phi\to e^{-i\alpha}\bar\Phi$$We can verify this explicitly:$$\begin{aligned}\Large S[e^{i\alpha}\Phi,e^{-i\alpha}\bar\Phi]&=\int-e^{-i\alpha}\partial_\mu\bar\Phi e^{i\alpha}\partial^\mu\Phi-m^2e^{-i\alpha}\bar\Phi e^{i\alpha}\Phi\,d^4x\\
&=\int-\partial_\mu\bar\Phi\partial^\mu\Phi-m^2\bar\Phi\Phi\,d^4x=S[\Phi,\bar\Phi]
\end{aligned}$$This is a global $U(1)$ continuous symmety, as $\alpha$ was constant so it will act the same way across all spacetime and $\alpha\in[0,2\pi)$ (a continuous interval). Continuous symmetries admit an infinitesimal transformation$$\Large\Phi\to(1+i\alpha)\Phi+\mathcal{O}(\alpha^2),\,\,\bar\Phi\to(1-i\alpha)\Phi+\mathcal{O}(\alpha^2)$$To highlight the difference between discrete symmetries, look at the charge conjugation ($C$) symmetry:$$\huge\Phi\to\bar\Phi,\,\,\bar\Phi\to\Phi$$This has no notion of an infinitesimal transformation and therefore cannot be used to generalise Noether's theorem. 

Now let us prove Noether's theorem (again):
> Consider a field theory for a set of scalar fields $\phi_a$ for $a=1,\dots,N$ with action $S[\phi_a]$. Now suppose this theory is invariant under a continuous symmetry, that is we have an infinitesimal variation of the fields$$\Large\phi_a(x)\to\phi_a(x)+\epsilon\Delta\phi_a(x)+\mathcal{O}(\epsilon^2)$$where $\epsilon$ is an infinitesimal parameter, under which the action is invariant. That is, $\delta_\epsilon S[\phi_a]=0$.
> Now consider a variation where we allow $\epsilon$ to depend on spacetime:$$\Large\phi_a(x)\to\phi_a(x)+\epsilon(x)\Delta\phi_a(x)+\mathcal{O}(\epsilon^2)$$The action will no longer be invariant, however the variation in the action should still vanish for constant $\epsilon(x)$. Therefore we should expect the variation to take form$$\huge\delta_{\epsilon(x)}S[\phi_a]=\int j^\mu\partial_\mu\epsilon(x)d^4x$$, assuming the field theory is local. Here, $j^\mu(\phi_a,\partial_\nu\phi_a,\dots)$ is a function of the fields and their derivatives and is dependent on the theory. 
> Integrating this by parts