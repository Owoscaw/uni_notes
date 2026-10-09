
# Special relativity:

The symmetries we expect for our field theory form the [[Spacetime and Tensors#Lorentz group|Poincare group]] (rotations, boosts, translations). These come from special relativity, working in the space $\Re^{1,3}$ with metric signature $(-,+,+,+)$. Special relativity is based on two principles:
> All laws of physics are the same in all inertial frames
> The speed of light is the same in all inertial frames

We denote a general element of our space as $(t,x,y,z)=X^\mu\in\Re^{1,3}$. Our Lorentz boost in $x^1$ then looks like:$$\Huge X^\mu\to X^{'\mu}=\begin{pmatrix}x^{'0} \\ x^{'1}\\ x^{'2} \\ x^{'3}\end{pmatrix}=\gamma\begin{pmatrix}x^0-vx^1 \\ x^1-vx^0 \\ x^2-vx^0 \\ x^3-vx^0\end{pmatrix}$$In the rest frame of the particle, the worldline is parametrised by $(x^0,x^1,x^2,x^3)=(z,0,0,0)$. In the rest frame of an observer, the worldline is parametrised by $(x^0,x^1,x^2,x^3)=(\gamma z,-v\gamma z,0,0)$. 

A photon has a worldline parametrised by$$\Huge\begin{pmatrix}x^0 \\ x^1 \\ x^2 \\ x^3\end{pmatrix}=\begin{pmatrix}z \\ z \\ 0 \\ 0\end{pmatrix}\to\begin{pmatrix}x^{'0} \\ x^{'1}\\ x^{'2} \\ x^{'3}\end{pmatrix}=\gamma\begin{pmatrix}(1-v)z \\ (1-v)z \\ 0 \\ 0\end{pmatrix}$$
We define the Minkowski metric as$$\Huge\eta_{\mu\nu}=\begin{pmatrix}-1  & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}_{\mu\nu}$$so that we can write a covector:$$\Huge X_\mu=(x_0,x_1,x_2,x_3)=\eta_{\mu\nu}X^\nu=(-x^0,x^1,x^2,x^3)_\mu$$Note that the Minkowski metric satisfies $\eta^{\mu\nu}\eta_{\nu\rho}=\delta^\mu_\rho$. We can then define our pseudo inner product on $X^\mu,Y^\mu\in\Re^{1,3}$:$$\Huge X\cdot Y=X^\mu Y_\mu=X^\mu\eta_{\mu\nu}Y^\nu=X^T\eta Y$$We now find the linear transformations $\Lambda$ of $\Re^{1,3}$ leaving this inner product invariant, after some calculation:$$\Huge\begin{align*}
\Lambda^T\eta\Lambda&=\eta\\
\Lambda_\nu^\mu\eta_{\mu\rho}\Lambda^\rho_\sigma=\eta_{\nu\sigma}
\end{align*}$$These form the [[Lie Groups and Algebras#Lie groups|Lie group]] $O(1,3)$, satisfying the properties:
> $det\Lambda=\pm1$
> $\Lambda^\mu_\nu\eta_{\mu\rho}\Lambda^{\rho}_\sigma=\eta_{\nu\sigma}$, setting $\nu=\sigma=0$ shows us:$$\Huge(\Lambda_0^0)^2-(\Lambda_1^1)^2-(\Lambda_2^2)^2-(\Lambda_3^3)^2=1$$

This suggests an obvious decomposition into $4$ disconnected components as$$\Huge (\Lambda_0^0)^2\geq1\implies\Lambda_0^0\geq1\text{ or }\Lambda_0^0\leq-1$$combined with $\det\Lambda=\pm1$ gives $4$ total combinations. We are interested in $SO(1,3)^+$, the proper orthochronous Lorentz group:$$\Huge SO(1,3)^+=\{\Lambda\in O(1,3):\det\Lambda=1,\Lambda_0^0\geq1\}$$