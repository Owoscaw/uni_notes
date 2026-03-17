

So far, we have been considering infinite-dimensional systems. Many methods, particularly the idea of a [[Evolving scattering data#Lax pairs|Lax pair]] can be applied to finite-dimensional classical integrable Hamiltonian systems.

# Finite-dimensional Hamiltonian systems:

A finite-dimensional Hamiltonian system is defined as:
> A set of [[Calculus of variations#Configuration space and generalised coordinates|generalised coordinates]] $q_{i=1,\dots,n}$ and momenta $p_{i,\dots,n}$ that completely specify the configuration of the system at time $t$.
> A function $H(q,p)$ defined on phase space (where $q,p$ parametrise the space of coordinates/momenta) called the Hamiltonian. 
> Time evolution equations are then [[Hamiltonian Formalism#Hamilton's equations|Hamilton's equations]]:$$\Huge\begin{align*}
\dot q_i&=\frac{\partial H}{\partial p_i}\\
\dot p_i&=-\frac{\partial H}{\partial q_i}
\end{align*}$$

Note that we can take $n\to\infty$ to define an infinite dimensional discrete Hamiltonian system. Most if not all of what we discuss will also apply to that case. Let us consider the example of $n$ point particles with masses $m_i$ in a potential $V(q_1,\dots,q_n)$:
> The Hamiltonian is then$$\Huge H(q,p)=\sum_{i=1}^n\frac{p_i^2}{2m_i}+V(q_1,\dots,q_n)$$and Hamilton's equations become:$$\Huge \dot q_i=\frac{p_i}{m_i},\,\,\dot p_i=-\frac{\partial V(q_1,\dots,q_n)}{\partial q_i}$$
> These reproduce Newton's equations$$\Huge m_i\ddot q_i=-\frac{\partial V(q_1,\dots,q_n)}{\partial q_i}$$to first order.

We can associate to a particular Hamiltonian system a bilinear antisymmetric form on the space of differentiable functions $q,p$ called the Poisson bracket:$$\Huge\{f,g\}=\sum_{i=1}^n\left(\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}-\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}\right)$$Clearly $\{f,g\}=-\{g,f\}$ and $\{f,f\}=0$. 

Hamilton's equations imply that any $f(q,p)$ that does not explicitly depend on time evolves as:$$\Huge\begin{align*}
\frac{d}{dt}f(q(t),p(t))&=\sum_{i=1}^n\dot q_i\frac{\partial f}{\partial q_i}+\dot p_i\frac{\partial f}{\partial p_i}\\
&=\sum_{i=1}^n\frac{\partial H}{\partial p_i}\frac{\partial f}{\partial q_i}-\frac{\partial H}{\partial q_i}\frac{\partial f}{\partial p_i}\\
&=\{H(q,p),f(q,p)\}
\end{align*}$$Functions that have no explicit time dependence and have vanishing Poisson bracket with $H(q,p)$ are therefore conserved. The antisymmetry of the Poisson bracket means that the Hamiltonian is conserved as long as it has no explicit time dependence:$$\Huge \frac{d}{dt}H(q(t),p(t))=\{H(q(t),p(t)),H(q(t),p(t))\}=0$$This ensures energy is conserved.

Note that if $\{F,H\}=0$ then not only is $F(q,p)$ conserved under time evolution, but $H(q,p)$ is conserved under a different time evolution with a time $s$ with Hamiltonian $F(q,p)$. In this case, the Hamilton equations are:$$\Huge\begin{cases}\frac{d}{ds}q_i=\frac{\partial F}{\partial p_i} \\
\frac{d}{ds}p_i=-\frac{\partial F}{\partial q_i}\end{cases}\implies \frac{d}{ds}H(q,p)=\{F(q,p),H(q,p)\}=0$$This also means that we can evolve along each time separately and in either order we find the same point in spacetime. We say that $F,H$ are an involution and generate commuting flows, where one is the $t$-evolution with Hamiltonian $H$ and the other is the $s$-evolution with Hamiltonian $F$.

A finite-dimensional Hamiltonian system $\{q_{i=1,\dots,n},p_{i=1,\dots,n},H(q_i,p_i)\}$ is called completely integrable if it has $n$ independent [[KdV hierarchy and conservation laws#Connection to conservation laws|conserved quantities]] $Q_i(q,p)$ that are mutually in involution, that is:$$\Huge \{Q_i,Q_j\}=0,\,\,\forall i,j=1,\dots,n$$One of these conserved quantities is always $H$. For such systems we can find a new set of coordinates $\varphi_i$ and momenta $Q_i$ on phase space such that the Hamiltonian only depends on the $Q_i$:$$\Huge H=H(Q)\implies\begin{cases}\dot\varphi=\frac{\partial H}{\partial Q_i} \\
\dot Q=-\frac{\partial H}{\partial \varphi_i}=0\end{cases}$$These are called action $(Q_i)$ angle $(\varphi_i)$ variables. This name comes from the fact that if surfaces of constant $H$ are compact, then the $\varphi_i$ parametrise periodic orbits and can be thought of as angular variables. 

The integrability of these systems can be established by constructing a Lax pair $L,M$ satisfying:$$\Huge \dot L=[M,L]$$Here $L,M$ are $n\times n$ matrices instead of differential operators. We will see that the $n$ conserved quantities correspond to the eigenvalues of the Lax matrix $L$.

The Lax equation above is formally solved by$$\Huge L(t)=U(t)L(0)U(t)^{-1}$$where the time evolution operator $U(t)$ is the unique solution of the ODE:$$\Huge\begin{align*}
\dot U(t)&=M(t)U(t)\\
U(0)&=\mathbb{1}
\end{align*}$$Proven as follows:
$$\Huge\begin{align*}
\dot L&=\frac{d}{dt}(UL(0)U^{-1})\\
&=\dot U L(0)U^{-1}+UL(0)\dot{U^{-1}}\\
&=\dot UL(0)U^{-1}-UL(0)U^{-1}\dot UU^{-1}\\
&=\dot U U^{-1}UL(0)U^{-1}-UL(0)U^{-1}\dot UU^{-1}\\
&=ML-ML=[M,L]
\end{align*}$$Where we use results from differentiating $UU^{-1}=\mathbb{1}$. The time evolution operator $U$ is unitary if $M$ is anti-Hermitian. This formal solution can be used to prove that the eigenvalues of $L$ do not depend on time.

To see this we consider the characteristic polynomial of $L$. This is an $n$th degree monic polynomial with roots corresponding to the $n$ eigenvalues $\lambda_{i=1,\dots,n}$ of $L$. $L$ can be diagonalised by conjugation with some unitary matrix $V$:$$\Huge L=V\Lambda V^{-1},\,\,\Lambda=\begin{pmatrix}\lambda_1 & 0 & \dots & 0 \\ 0 & \lambda_2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_n\end{pmatrix}=\text{diag}(\lambda_1,\dots,\lambda_n)$$Therefore:$$\Huge\begin{align*}
P_L(\lambda)&=\det(\lambda\mathbb{1}-L)\\
&=\det(\lambda\mathbb{1}-V\Lambda V^{-1})\\
&=\det(\lambda VV^{-1}-V\Lambda V^{-1})\\
&=\det((\lambda V-V\Lambda)V^{-1})\\
&=\det(V(\lambda\mathbb{1}-\Lambda)V^{-1})\\
&=\det(V)\det(\lambda\mathbb{1}-\Lambda)\det(V^{-1})\\
&=\det(\lambda\mathbb{1}-\Lambda)\\
&=\prod_{i=1}^n(\lambda-\lambda_i)\\
&=\lambda^n-c_1\lambda^{n-1}+c_2\lambda^{n-2}-\dots+(-1)^n\prod_{i=1}^n\lambda_i
\end{align*}$$
Since time evolution is also given by conjugation by the unitary operator $U(t)$, the same argument holds:$$\Huge\begin{align*}
P_{L(t)}(\lambda)&=\det(\lambda\mathbb{1}-U(t)L(0)U(t)^{-1})\\
&=\det(\lambda\mathbb{1}-L(0))\\
&=P_{L(0)}(\lambda)
\end{align*}$$Which implies that the eigenvalues $\lambda_i$ of $L(t)$ are independent of time, as required.

Equivalently, we can take the $n$ conserved quantities to be the coefficients $c_k$ of the characteristic polynomial$$\Huge c_k=\sum_{1\leq i_1<i_1<\dots<i_k\leq n}\lambda_{i_1}\lambda_{i_2}\dots\lambda_{i_k}$$or as the power sum symmetric polynomials:$$\Huge s_k=\sum_{i=1}^n\lambda_i^k=\text{tr}(L^k),\,\,k=1,\dots,n$$The two sets of polynomials are related by the Girard-Newton identities:$$\Huge kc_k=\sum_{i=1}^k(-1)^{i-1}c_{k-i}s_i$$Note that the conservation of $s_k$ can be proven through a derivative of $L^k$. 

Finally, the eigenvalue equation $$\Huge L(t)\psi(t)=\lambda\psi(t)$$is solved formally by$$\Huge \psi(t)=U(t)\psi(0)$$where $\psi(0)$ is an eigenvector at $t=0$:$$\Huge\begin{align*}
L(t)\psi(t)&=U(t)L(0)U(t)^{-1}U(t)\psi(0)\\
&=U(t)L(0)\psi(0)\\
&=U(t)\lambda\psi(0)\\
&=\lambda U(t)\psi(0)=\lambda\psi(t)
\end{align*}$$