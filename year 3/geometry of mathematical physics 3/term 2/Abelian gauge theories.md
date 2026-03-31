
We conclude by learning how to formulate gauge theories, a subset of [[Symmetries and Action Principles#Lorentz symmetry and field theories|field theories]] which describe most forces in physics. The standard model of elementary particles is a gauge theory based on the group $G=SU(3)\times SU(2)\times U(1)$, and accounts for the strong, weak, and electromagnetic interaction. We start by looking at gauge theories, the formulation of which is based on an abelian [[Lie Groups and Algebras#Lie groups|Lie group]] called the gauge group. 

# Electromagnetism as a $U(1)$ gauge theory:

We start from a field theory with a $U(1)$ global symmetry and promoting the constant $U(1)$ parameter to a local function of spacetime. Before we do this, let us describe Maxwell's theory of [[Electromagnetism|electromagnetism]] in terms of a relativistic field theory which we base on a gauge symmetry principle. 

## Relativistic Maxwell's equations:
The Maxwell equations describing electric $\underline{E}$ and magnetic $\underline{B}$ fields induced by an electric charge density $\rho$ and current $\underline{j}$ are:$$\Huge\begin{align*}
\underline{\nabla}\cdot\underline{E}&=\rho&\underline{\nabla}\times\underline{B}-\frac{\partial \underline{E}}{\partial t}&=\underline{j}\\
\underline{\nabla}\cdot\underline{B}&=0&\underline{\nabla}\times\underline{E}+\frac{\partial \underline{B}}{\partial t}&=0
\end{align*}$$The equations in the first line are called the inhomogeneous Maxwell equations, since they have sources for electric and magnetic fields in the RHS. The equations in the second line are then obviously named.

The behaviour of Maxwell's equations under [[Lorentz transformations|Lorentz tranformations]] can be found as follows. Starting from an inertial frame with charge distribution of $\rho$ at rest, we perform the boost$$\Huge \Lambda=\begin{pmatrix}\cosh\lambda & \sinh\lambda & 0 & 0 \\ \sinh\lambda & \cosh\lambda & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}$$to another inertial frame moving at a relative speed $\tanh\lambda$, in which there is also a non-zero current $\underline{j}$. Resting charges only source electric fields, while steady currents source magnetic fields, so it is implied that Lorentz transformations will mix up the electric and magnetic fields.

In order to understand how to write the Maxwell equations in a Lorentz invariant way, we first focus on the sources appearing in the RHS of the inhomogeneous Maxwell equations. Charge density $\rho$ and current $\underline{j}$ can be relabeled as a Lorentz $4$-vector $J^\mu$, such that $J^0=\rho$ and $J^i=j^i$. So we write $J^\mu=(\rho,j^1,j^2,j^3)$ The continuity equation transforms as$$\Huge \frac{\partial \rho}{\partial t}+\underline{\nabla}\cdot\underline{j}=0\rightarrow\partial_\mu J^\mu=0$$and since $J^\mu$ is a Lorentz vector, the transformation acts as$$\Huge J^\mu(x)\rightarrow J'^\mu(x)=\Lambda^\mu_\nu J^\nu(\Lambda^{-1}x)$$, which we showed to leave the continuity equation invariant. Note that the similarity between the two lines of equations implies we should do the same Lorentz vector repackaging for the homogeneous Maxwell equations.

Focusing on the LHS of the inhomogeneous Maxwell equations (equal to $J^\mu$), we notice that the spacetime derivatives appear linearly. Therefore we must have $\partial_\nu$ on the LHS, with the index $\nu$ requiring a tensor linear so that $\mu$ remains the free index. One option is to take the LHS to be a gradient $\partial^\mu X$ of a scalar field $X$. However, an equation of this form ($\partial^\mu X=J^\mu$) is ruled our by counting degrees of freedom. This interpretation does not account for the electric and magnetic fields $\underline{E},\underline{B}$ and hence the LHS cannot be produced. In order to match the upper index of $J^\mu$, the derivative $\partial_\nu$ must therefore act on a second rank Lorentz tensor $F^{\mu\nu}$, which is linear in the electric and magnetic fields and contracts the $\nu$ index so that $\mu$ remains free.

$\underline{E},\underline{B}$ have $6$ components in total, whereas a second rank tensor has $16$ components, so we still mismatch the degrees of freedom. We can remedy this by demanding $F^{\mu\nu}$ be antisymmetric, $F^{\mu\nu}=-F^{\nu\mu}$. In this case, it has $6$ components. The inhomogeneous Maxwell equations are then written as$$\Huge \partial_\nu F^{\mu\nu}=J^\mu$$for a second rank antisymmetric tensor $F^{\mu\nu}=-F^{\nu\mu}$ linear in $\underline{E},\underline{B}$. Comparing using the classic Maxwell equations gives:$$\Huge [F^{\mu\nu}]=\begin{pmatrix}0 & E_1 & E_2 & E_3 \\ -E_1 & 0 & B_3 & -B_2 \\ -E_2 & -B_3 & 0 & B_1 \\ -E_3 & B_2 & -B_1 & 0\end{pmatrix}$$Lowering indices to $F_{\mu\nu}=\eta_{\mu\rho}\eta_{\nu\sigma}F^{\rho\sigma}$ we have$$\Huge [F_{\mu\nu}]=\begin{pmatrix}0 & -E_1 & -E_2 & -E_3 \\ E_1 & 0 & B_3 & -B_2 \\ E_2 & -B_3  & 0 & B_1 \\ E_3 & B_2 & -B_1 & 0\end{pmatrix}$$, that is for $i=1,2,3$ we have:$$\Huge F_{i0}=-F_{0i}=E_i,\,\,F_{ij}=\epsilon_{ijk}B_k$$This tensor used to be called the Faraday tensor, but is now known as the field strength tensor. By similar logic, one can find that the homogeneous Maxwell equations are written covariantly as$$\Huge \epsilon^{\mu\nu\rho\sigma}\partial_\nu F_{\rho\sigma}=0$$where $\epsilon^{\mu\nu\rho\sigma}$ is the completely antisymmetric tensor with four indices, normalised such that $\epsilon^{0123}=1$. Written as Lorentz vectors we have:$$\Huge\epsilon_{\mu\nu\rho\sigma}\partial^\nu F^{\rho\sigma}=0,\,\,\partial_\nu F^{\mu\nu}=J^\mu$$
Under a [[The Lorentz Group#The Lorentz group and its Lie Groups and Algebras Lie algebras Lie algebra|Lorentz transformation]], we find:$$\Huge\begin{align*}
J^\mu(\underline{x})&\rightarrow\Lambda^\mu_\nu J^\nu(\Lambda^{-1}\underline{x})\\
F^{\mu\nu}(\underline{x})&\rightarrow\Lambda^\mu_\rho\Lambda^\nu_\sigma F^{\rho\sigma}(\Lambda^{-1}\underline{x})
\end{align*}$$Note that our conservation equation is much easier to derive in relativistic notation:$$\Huge\begin{align*}
\frac{\partial \rho}{\partial t}+\underline{\nabla}j=\partial_\mu J^\mu&=\partial_\mu\partial_\nu F^{\mu\nu}\\
&=-\partial_\mu\partial_\nu F^{\nu\mu}\\
&=-\partial_\nu\partial_\mu F^{\nu\mu}\\
\text{relabelling}&=-\partial_\mu\partial_\nu F^{\mu\nu}=-\partial_\mu J^\mu\\
\implies\partial_\mu J^\mu&=0
\end{align*}$$This is a general application of the logic "symmetric times antisymmetric" equals $0$, where $\partial_\mu\partial_\nu$ is the symmetric object and $F^{\mu\nu}$ was defined to be antisymmetric.

## Maxwell equation and actions:

As we did for other [[Symmetries and Action Principles#Actions for Field Theories|field theroies]], we try to find an action that will reproduce the equations of motion we found. The [[Hamiltonian Formalism|Hamiltonian]] has the physical interpretation as the total energy of a system, so a good guess is$$\Huge\begin{align*}
H&=\int\underline{E}^2+\underline{B}^2\,d^3x\\
\implies\mathcal{L}&=\underline{E}^2+\underline{B}^2\cong F_{\mu\nu}F^{\mu\nu}=F^{\rho\sigma}F^{\mu\nu}\eta_{\rho\mu}\eta_{\sigma\nu}
\end{align*}$$Using this as our action, we find the equations of motion:$$\Huge\begin{align*}
\frac{\partial \mathcal{L}}{\partial F^{\mu\nu}}-\partial_\rho\frac{\partial \mathcal{L}}{\partial (\partial_\rho F^{\mu\nu})}&=0\\
\implies F_{\mu\nu}&=0
\end{align*}$$Note that this is actually $6$ equations, for each combination of $\mu,\nu$ and index of $F$. We derived a total of $8$ equations for our equations of motion previously.

In a star-shaped region of $\Re^4$, the repackaged homogeneous Maxwell equations imply that we can write the Faraday tensor as:$$\Huge F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$$This is analogous to the classical case where $\underline{\nabla}\times\underline{F}=0\implies\underline{F}=\underline{\nabla}\phi$ for a simply connected domain. In general, this method is outlined in the Poincare lemma. Here, we are packaging $A^\mu=(\phi,A^1,A^2,A^3)$ Taking this to be true, equations become:$$\Huge\begin{align*}
\epsilon_{\mu\nu\rho\sigma}\partial^\nu(\partial^\rho A^\sigma-\partial^\sigma A^\rho)&=\epsilon_{\mu\nu\rho\sigma}(\partial^\nu\partial^\rho A^\sigma-\partial^\nu\partial^\sigma A^\rho)\\
&=\text{antisymmetric}\times\text{symmetric}=0
\end{align*}$$So this repackaging satisfies the homogeneous Maxwell equations. We promote $A$ to the dynamical field, so we write the equations of motion as:$$\Huge \frac{\partial \mathcal{L}}{\partial A_\mu}-\partial_\nu\frac{\partial \mathcal{L}}{\partial (\partial_\nu A_\mu)}=0$$These should reproduce our repackaged inhomogeneous Maxwell equations. 

We propose that the correct Lagrangian that will reproduce these equations is given by:$$\Huge\begin{align*}
\mathcal{L}&=-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}+A_\mu J^\mu\\
F_{\mu\nu}&=\partial_\mu A_\nu-\partial_\nu A_\mu\\
\implies\frac{\partial \mathcal{L}}{\partial A_\mu}&=\frac{\partial }{\partial A_\mu}(A_\rho J^\rho)\\
&=\delta^\mu_\rho J^\rho=J^\mu\\
\implies\frac{\partial \mathcal{L}}{\partial (\partial_\nu A_\mu)}&=-\frac{1}{4}\frac{\partial }{\partial (\partial_\nu A_\mu)}(\partial_\rho A_\sigma-\partial_\sigma A_\rho)(\partial^\rho A^\sigma-\partial^\sigma A^\rho)\\
&=-\frac{1}{4}\frac{\partial }{\partial (\partial_\nu A_\mu)}(\partial_\rho A_\sigma-\partial_\sigma A_\rho)(\partial_\epsilon A_\tau-\partial_\tau A_\epsilon)\eta^{\rho\epsilon}\eta^{\sigma\tau}\\
&=-\frac{1}{4}(\delta^\nu_\rho\delta^\nu_\sigma-\delta^\nu_\sigma\delta^\mu_\rho)(\partial_\epsilon A_\tau-\partial_\tau A_\epsilon)\eta^{\rho\epsilon}\eta^{\sigma\tau}\\
&-\frac{1}{4}(\partial_\rho A_\sigma-\partial_\sigma A_\rho)(\delta^\nu_\epsilon\delta^\mu_\tau-\delta^\nu_\tau\delta^\mu_\epsilon)\eta^{\rho\epsilon}\eta^{\sigma\tau}\\
&=-\frac{1}{4}(\eta^{\nu\epsilon}\eta^{\mu\tau}-\eta^{\mu\epsilon}\eta^{\nu\tau})(\partial_\epsilon A_\tau-\partial_\tau A_\epsilon)\\
&-\frac{1}{4}(\partial_\rho A_\sigma-\partial_\sigma A_\rho)(\eta^{\rho\nu}\eta^{\rho\mu}-\eta^{\rho\mu}\eta^{\rho\nu})\\
&=-\frac{1}{4}(\partial^\nu A^\mu-\partial^\mu A^\nu-\partial^\mu A^\nu+\partial^\nu A^\mu)+\text{similar}\\
&=-\frac{1}{2}(\partial^\nu A^\mu-\partial^\mu A^\nu)+\text{same terms}\\
&=-\partial^\nu A^\mu+\partial^\mu A^\nu=-F^{\nu\mu}\\
\implies J^\mu-\partial_\nu F^{\mu\nu}&=0
\end{align*}$$Where we used the Euler-Lagrange equations in the last line, proving our proposition.

## Gauge symmetry:
This trick we used has an interesting consequence, the physical fields we measure are $\underline{E},\underline{B}$. These are the components of $F_{\mu\nu}$, not the dynamical field $A_\mu$ that we used to define actions. It turns out that $A_\mu$ is not uniquely defined, we are free to shift $A_\mu(x)$ by the derivative of any smooth function $\alpha(x)$$$\Huge A_\mu(x)\rightarrow A_\mu(x)+\partial_\mu\alpha(x)$$without altering the physical fields:$$\Huge\begin{align*}
F_{\mu\nu}&=\partial_\mu A_\nu-\partial_\nu A_\mu\\
&\rightarrow\partial_\mu(A_\mu+\partial_\mu\alpha)-\partial_\nu(A_\nu+\partial_\nu)\\
&=\partial_\mu A_\nu-\partial_\nu A_\mu+\partial_{\mu\nu}\alpha-\partial_{\nu\mu}\alpha\\
&=F_{\mu\nu}
\end{align*}$$
A symmetry for which the parameters of the transformation depend on spacetime is called a Gauge symmetry. The above equation is the gauge transformation of $A_\mu$ and we call $A_\mu$ a gauge field. These field configurations that differ by a gauge transformation are considered physically equivalent.

Performing a gauge transformation on the action gives:$$\Huge\begin{align*}
S[A_\mu]\rightarrow S[A_\mu+\partial_\mu\alpha]&=\int-\frac{1}{4}F^{\mu\nu}F_{\mu\nu}+A_\mu J^\mu+(\partial_\mu\alpha)J^\mu\,d^4x\\
&=S[A_\mu]+\int(\partial_\mu\alpha)J^\mu\,d^4x\\
\implies\delta_\alpha S[A_\mu]&=\int(\partial_\mu\alpha)J^\mu\,d^4x\\
&=-\int\alpha(\partial_\mu J^\mu)d^4x=0
\end{align*}$$
Note that we can write$$\Huge A_\mu\rightarrow A_\mu+\partial_\mu\alpha=e^{i\alpha}(A_\mu +i\partial_\mu)e^{-i\alpha}$$so that we can associate gauge transformations to [[U(1),SU(2),SO(3)#$U(1)$|$U(1)$]] but with a spacetime dependent parameter $\alpha$. We call $U(1)$ the gauge group. The field $A_\mu$ is transforming in the [[Representations#Definitions|adjoint representation]] except from the derivative term.

# $U(1)$ global symmetry:

Consider a complex scalar field $\phi(x)$. The action$$\Huge\begin{align*}
S_0[\phi,\bar \phi]&=\int\mathcal{L}_0(\phi,\bar\phi,\partial_\mu\phi,\partial_\mu\bar\phi)d^4x\\
\mathcal{L}_0&=-|\partial_\mu\phi|^2-V(\phi,\bar\phi)\\
&=-|\partial_\mu\phi|^2-U(|\phi|^2)\\
&=|\dot\phi|^2-|\underline{\nabla}\phi|^2-U(|\phi|^2)
\end{align*}$$is invariant under global $G=U(1)$ transformations$$\Huge g:\phi(x)\rightarrow e^{i\alpha}\phi(x)$$where $\alpha\sim\alpha+2\pi$ is a constant parameter and $g=e^{i\alpha}\in U(1)$ is a constant group element. The restriction to $U(1)$ invariance demands the scalar potential $V(\phi,\bar\phi)$ depends only on the invariant $|\phi|^2$. As the scalar field is multiplied by a single power of the $U(1)$ group element, we say it has charge $1$:
> The continuous $U(1)$ symmetry ensures the existence of the conserved current and conserved charge$$\Huge\begin{align*}
j^\mu&=-i(\bar\phi\partial^\mu\phi-\phi\partial^\mu\bar\phi)\\
\partial_\mu j^\mu&=0\\
Q&=\int j^0\,d^3x\\
\frac{d}{dt}Q&=0\end{align*}$$by [[Symmetries and Action Principles#Noether's theorem|Noether's theorem]].
> A global symmetry relates physically distinct configurations.

# $U(1)$ gauge symmetry:

To make the global symmetry local, we promote $\alpha$ to a function of spacetime $\alpha(x)$. The parameter $\alpha(x)$ should approach $0$ sufficiently fast at infinity. Trying to write a kinetic term for $\phi$, we find that under a $U(1)$ gauge transformation$$\Huge\partial_\mu\phi\rightarrow\partial_\mu\phi'=\partial_\mu(e^{i\alpha}\phi)=e^{i\alpha}(\partial_\mu+i(\partial_\mu\alpha)\phi)$$since $\alpha$ is spacetime dependent. Therefore the kinetic term $-|\partial_\mu\phi|^2$ is not invariant under $U(1)$ gauge transformations.

To remedy this, we replace $\partial_\mu\phi$ with the gauge covariant derivative, defined as:$$\Huge D_\mu\phi=\partial_\mu\phi-iA_\mu\phi$$This introduces a new field $A_\mu$ (gauge field) which transforms under gauge transformations precisely to cancel the unwanted second term:$$\Huge\begin{align*}
A_\mu\rightarrow A_\mu'&=A_\mu+\partial_\mu\alpha\\
\implies D_\mu\phi=
(\partial_\mu\phi-iA_\mu\phi)&\rightarrow(\partial_\mu\phi'-iA_\mu'\phi')\\
&=e^{i\alpha}(\partial_\mu\phi+i(\partial_\mu\alpha)\phi-iA_\mu\phi-i(\partial_\mu\alpha)\phi)\\
&=e^{i\alpha}(\partial_\mu\phi-iA_\mu\phi)=e^{i\alpha}D_\mu\phi\end{align*}$$It is clear to see that replacing $\partial_\mu$ with $D_\mu$ makes the gauge kinetic term of $\phi$ invariant under $U(1)$ gauge transformations.

Now we need to introduce a new gauge invariant kinetic term for our new field $A_\mu$. We do this by demanding the Maxwell Lagrangian. We find that$$\Huge\begin{align*}
S[\phi,\bar\phi,A_\mu]&=\int\mathcal{L}(\phi,\bar\phi,A_\nu,\partial_\mu\phi,\partial_\mu\bar\phi,\partial_\mu A_\nu)d^4x\\
\mathcal{L}&=\mathcal{L}_0(\phi,\bar\phi,D_\mu\phi,\overline{D_\mu\phi})+\mathcal{L}_\text{Maxwell}(\partial_\mu A_\nu)\\
&=-\overline{D_\mu\phi}D^\mu\phi-U(|\phi|^2)
-\frac{1}{4g^2}F_{\mu\nu}F^{\mu\nu}\end{align*}$$where $A_\mu$ is a real gauge field and $$\Huge\begin{align*}
D_\mu\phi&=(\partial_\mu-iA_\mu)\phi\\
F_{\mu\nu}&=\partial_\mu A_\nu-\partial_\nu A_\mu
\end{align*}$$are invariant under $G=U(1)$ gauge transformations:$$\Huge\begin{align*}
\phi(x)&\rightarrow e^{i\alpha(x)}\phi(x)\\
A_\mu(x)&\rightarrow A_\mu(x)+\partial_\mu\alpha(x)
\end{align*}$$Note that:
> To linear order in $A_\mu$:$$\Huge \mathcal{L}=\mathcal{L}_0+j^\mu A_\mu+\dots$$That is, the scalar field is coupled to the gauge field $A_\mu$ and not to the field strength $F_{\mu\nu}$. $A_\mu$ couples directly to the conserved current $j^\mu$ of the theory with $U(1)$ global symmetry. This is known as minimal coupling. Note that sometimes we rescale the gauge field $A_\mu\rightarrow gA_\mu$ so that we can control the strength of the coupling between $j^\mu$ and the gauge field $A_\mu$ with the group element $g$.
> The group of gauge transformations$$\Huge \mathcal{G}=\mathcal{U}(1)=\left\{\begin{align*}
g:\Re^{1,3}&\rightarrow G=U(1)\\
x^\mu&\rightarrow g(x)=e^{i\alpha(x)}
\end{align*}\right\}$$is infinite dimensional, since it associated independent $g(x)$ for the fields at different points $x^\mu$ and there are infinitely many points in spacetime. 
> A gauge symmetry relates physically equivalent configurations, which are to be identified. The identification of field configurations which differ by a gauge transformation leads to non-trivial topological properties of gauge fields. These ensure the existence of [[Topological lumps|topological solitons]] and instantons.
> Under a $U(1)$ gauge transformation$$\Huge\begin{align*}
D_\mu\phi&\rightarrow e^{i\alpha}D_\mu\phi\\
F_{\mu\nu}&\rightarrow F_{\mu\nu}
\end{align*}$$, we say that $D_\mu\phi$ is gauge covariant as it transforms in a representation of $G$ for all $x$. The field strength $F_{\mu\nu}$ is gauge invariant.
> We think of the covariant derivative $D_\mu=\partial_\mu-iA_\mu$ as a differential operator. Requiring that under a $U(1)$ gauge transformation$$\Huge D_\mu\rightarrow e^{i\alpha}D_\mu e^{-i\alpha},\,\,D_\mu\phi\rightarrow e^{i\alpha}D_\mu\phi$$implies the gauge transformation of the field:$$\Huge A_\mu\rightarrow A_\mu+\partial_\mu\alpha$$
> A gauge field $A_\mu$ is only defined locally, in a patch where we take Poincare's lemma to apply. This means that for two patches $U^{(1)},U^{(2)}$ with nontrivial overlap $U^{(1)}\cap U^{(2)}\neq\emptyset$, the gauge fields $A^{(1)}_\mu,A^{(2)}_\mu$ defined in the two patches are related by a gauge transformation$$\Huge A^{(1)}_\mu=A^{(2)}_\mu+\partial_\mu\alpha^{(12)}$$on the overlap. The transformation parameter $\alpha^{(12)}$ is called a transition function. This local definition of the gauge field is responsible for most of the topological and geometric properties of gauge theories.

# Gauge redundancy and gauge fixing:

We start from the EOM for the theory of scalar electrodynamics, described by the action with Lagrangian density$$\Huge\mathcal{L}=-|D_\mu\phi|^2-V(\bar\phi,\phi)-\frac{1}{4g^2}F_{\mu\nu}^2$$where $F_{\mu\nu}^2=F_{\mu\nu}F^{\mu\nu}$ and the scalar potentials take form $V(\bar\phi,\phi)=U(|\phi|^2)$ to ensure gauge invariance. The Euler-Lagrange equations are then:$$\Huge\begin{align*}
D_\mu D^\mu\phi&=\frac{\partial V}{\partial \phi}=U'(|\phi|^2)\phi\\
\partial_\nu F^{\mu\nu}&=g^2J^\mu
\end{align*}$$ We consider the transformation properties under a $U(1)$ gauge transformation so that the first equation transforms as$$\Huge D_\mu D^\mu\phi\rightarrow e^{i\alpha}D_\mu D^\mu\phi$$, a gauge covariant. The second equation transforms as a gauge invariant.

Therefore a field configuration $(\phi,A_\mu)$ solves the EOM, then any gauge transformed field configuration also solves the EOM. That is, the EOM only determines $(\phi,A_\mu)$ up to a gauge transformation.

Given some initial data $(\phi^{(0)},A_\mu^{(0)})$ specifying the field configuration at an initial time $t_0$, we cannot uniquely determine the field configuration $(\phi,A_\mu)$ at a later time $t>t_0$. This makes sense as $\phi'=e^{i\alpha}\phi,A_\mu'=A_\mu+\partial_\mu\alpha$ is as a good solution to the EOM as $(\phi,A_\mu)$, and will obey the same initial condition, provided that the gauge parameter $\alpha$ obeys $\alpha(t_0,\underline{x})=0$ and $\partial_\mu\alpha(t_0,\underline{x})=0$ at the initial time $t_0$.

We would like the EOM to define a well-posed initial value problem that uniquely determines physically observable fields at later times. This is not the case if we consider field configurations that differ by gauge transformations as physically equivalent. In this case the IVP is well posed and we therefore identify field configurations related by a gauge transformation:$$\Huge (\phi,A_\mu)\sim(\phi'=e^{i\alpha}\phi,A_\mu'=A_\mu+\partial_\mu\alpha)$$Physically observable quantities must then by gauge invariant, such as for example the field strength $F_{\mu\nu}$, the magnitude of the scalar field  $|\phi|^2$, or the conserved current $J_\mu$.

Considering the field space $\mathcal{F}=\{\phi(x),A_\mu(x)\}$ is foliated by gauge orbits traced by the action of the gauge group:$$\Huge \mathcal{G}\cdot(\phi(x),A_\mu(x))=\{(e^{i\alpha(x)}\phi(x),A_\mu(x)+\partial_\mu\alpha(x)):\alpha(x)\sim\alpha(x)+2\pi\}$$That is, a gauge orbit consists of all of the field configurations related by a gauge transformation. Therefore we have the correspondence:$$\Huge \text{Physical configuration}\leftrightarrow\text{ Gauge orbit}$$![[Abelian gauge theories 2026-02-26 14.53.09.excalidraw]]We see that the space of all field configurations decomposes into the disjoint union of gauge orbits, each representing a physical configuration. A complete gauge fixing selects a single representative for each orbit.

Instead of working with the redundant description of a field space $\mathcal{F}$ subject to the gauge symmetry $\mathcal{G}$, it is useful to fix a gauge. Any representative works, however we need to ensure that the gauge fixing cuts each orbit once and only once. If that is not the case, gauge symmetry is left over and we call the gauge fixing partial. We study a few standard partial gauge fixings:
> The Lorentz gauge is defined by imposing the constraint$$\Huge\partial_\mu A^\mu=0$$on the gauge field $4$-vector $A_\mu$. This is always achieved, as a representative $A_\mu$ that does not obey the above can always be redefined as $A_\mu'=A_\mu+\partial_\mu\alpha$ in the same gauge orbit that obeys this:$$\Huge 0=\partial_\mu A'^\mu=\partial_\mu A^\mu+\partial_\mu\partial^\mu\alpha$$Which is solved by picking some $\alpha$ to be a solution of the inhomogeneous equation$$\Huge \partial_\mu\partial^\mu\alpha=-\partial_\mu A^\mu$$, which always exists. This constraint is clearly Lorentz invariant, however this only fixes the gauge partially. This is because we are free to perform gauge transformations with parameters $\alpha$ such that $\partial_\mu\partial^\mu\alpha=0$ and we remain in the Lorentz gauge.
> The Coulomb gauge is defined by imposing the constraint$$\Huge \underline{\nabla}\cdot\underline{A}=0$$on the vector potential $\underline{A}$, the spatial part of the $4$-vector $A_\mu$. This is always possible by similar reasoning as above. This is clearly not Lorentz invariant, so gauge fixing spoils the manifest relativistic symmetry of the formalism. Another drawback is that the gauge is only partially fixed as in the Lorentz gauge, however acting only on the spatial indices. Note that the Coulomb gauge has a temporal component $A_0$ determined by the charge density $\rho=J^0$ in electrostatics, we can set $\rho=0$ for "pure electromagnetism" and get $A_0=0$.

# $U(1)$ Wilson line and Wilson loop:

Recalling that if $\phi$ is a charged scalar, then its partial derivative is not gauge covariant. We therefore introduced the covariant derivative $D_\mu\phi=(\partial_\mu-iA_\mu)\phi$, which indeed transforms covariantly as a field of charge $1$ under the gauge transformation. 

To understand why this makes the scalar transform covariantly, let us look at the total differential of $\phi(x)$$$\Huge d\phi(x)=\lim_{\epsilon\to 0}\frac{\phi(x+\epsilon dx)-\phi(x)}{\epsilon}=\partial_\mu\phi(x)dx^\mu$$, where we introduce the infinitesimal parameter $\epsilon$. The final expression write the total differential of $\phi(x)$ as the $4$-vector $\partial_\mu\phi(x)$ contracted with the differential increment $dx^\mu$. The reason why this does not transform covariantly is that the two terms we subtract in the limit have different transformation properties$$\Huge\begin{align*}
\phi(x+\epsilon dx)&\rightarrow e^{i\alpha(x+\epsilon dx)}\phi(x+\epsilon dx)\\
\phi(x)&\rightarrow e^{i\alpha(x)}\phi(x)
\end{align*}$$as $\alpha(x+\epsilon dx)\neq\alpha(x)$. We fix this problem by introducing the Wilson line. This is the mathematical notion of parallel transport.

Let $C$ be an open curve from $x_1$ to $x_2$$$\Huge C:I=[\tau_1,\tau_2]\rightarrow\Re^{1,3},\,\,\tau\rightarrow x^{\mu}(\tau)$$with $x(\tau_1)=x_1,x(\tau_2)x_2$ at the endpoints. The Wilson line along the path $C$ is defined to be$$\large W_C(x_2,x_2)=\exp\left(i\int_{x_1,C}^{x_2}A_\mu(x)dx^\mu\right)=\exp\left(i\int_{\tau_1}^{\tau_2}A_\mu(x(\tau))\dot x^\mu(\tau)d\tau\right)$$where the first integral is the [[Line integrals#Line integrals of vector fields|line integral]] from $x_1$ to $x_2$ along $C$, and the second is the expression in the parametrisation $x^\mu(\tau)$. If $C$ is a closed loop $(x_1=x_2)$ then we define$$\Huge W_C=\exp\left(i\oint_CA_\mu(x)dx^\mu\right)$$as the Wilson loop (of charge $1$) along the curve $C$. From our insight in multivariable calculus, we know that this does not depend on the end points $x_1,x_2$ and only on the curve $C$.

Under a $U(1)$ gauge transformation we claim that the Wilson line transforms as$$\Huge W_C(x_2,x_1)\rightarrow e^{i\alpha(x_2)}W_C(x_2,x_1)e^{-i\alpha(x_1)}$$, proof:$$\Huge\begin{align*}
W_C(x_2,x_1)&=\exp\left(i\int_{x_1,C}^{x_2}A_\mu dx^\mu\right)\\
&\rightarrow\exp\left(i\int_{x_1,C}^{x_2}(A_\mu+\partial_\mu\alpha)dx^\mu\right)\\
&=\exp\left(i\int_{x_1,C}^{x_2}A_\mu dx^{\mu}\right)\exp\left(i\int_{x_1,C}^{x_2}\partial_\mu\alpha dx^\mu\right)\\
&=W_C(x_2,x_1)\exp(i(\alpha(x_2)-\alpha(x_1)))\\
&=e^{i\alpha(x_2)}W_C(x_2,x_1)e^{-i\alpha(x_1)}
\end{align*}$$Where we use the fact that $\partial_\mu\alpha dx^\mu=d\alpha(x)$ is an exact differential, so its integral along $C$ only depends on boundary terms. A consequence of this is that the $U(1)$ Wilson loop is gauge-invariant.

Remarks:
> In QM, the Wilson line $W_C(x_2,x_1)$ is the phase picked up by the [[Wave function#Phases|wave function]] of a charged point particle adiabatically moving from $x_1$ to $x_2$ along $C$ in the presence of a gauge field.
> The Wilson loop is gauge invariant and therefore physically observable. We can interpret it as the above, and is associated with the Aharonov-Bohm effect in QM. This is an unexpected effect arising from the wave function directly coupling to the gauge potential $A_\mu$ rather than the physical fields.

If the loop $C$ is the boundary of some surface $\Sigma$, then by [[Integral theorems#Stokes' theorem|Stokes' theorem]] we find$$\large\begin{align*}
\oint_C A_\mu(x)dx^\mu&=\frac{1}{2}\int_\Sigma F_{\mu\nu}(x)dx^\mu dx^\nu\\
&=\frac{1}{2}\int_{x^{-1}(\Sigma)}F_{\mu\nu}(x(\sigma))\left(\frac{\partial x^\mu(\sigma)}{\partial \sigma^1}\frac{\partial x^\nu(\sigma)}{\partial \sigma^2}-\frac{\partial x^\nu(\sigma)}{\partial \sigma^1}\frac{\partial x^\mu(\sigma)}{\partial \sigma^2}\right)d\sigma^1d\sigma^2
\end{align*}$$where $x^\mu(\sigma)=x^\mu(\sigma^1,\sigma^2)$ is a parametrisation of the surface $\Sigma$. This is a higher-dimensional analogue of Stokes' theorem$$\Huge \oint_C\underline{A}\cdot d\underline{l}=\int_\Sigma(\underline{\nabla}\times\underline{A})\cdot\underline{\hat{n}}d^2\sigma=\int_\Sigma\underline{B}\cdot\underline{\hat{n}}d^2\sigma$$, our version tells us that the field strength $F_{\mu\nu}$ encodes the value of infinitesimal Wilson loops. If the loop $C$ is not contractible to a point, we might have that $A_\mu\neq0$ and so$$\Huge\oint_C A_\mu dx^\mu\neq0$$even if $F_{\mu\nu}=0$ everywhere in a region probed by a quantum particle. 

#  The Dirac monopole:

We investigate if we can have a magnetic field localised near a point in $\Re^3$. This configuration is known as a magnetic monopole, classically forbidden by Maxwell's equations$$\Huge\begin{align*}
\partial_\nu F^{\mu\nu}&=J^\mu\\
\partial_\nu\tilde F^{\mu\nu}&=0
\end{align*}$$where $\tilde F^{\mu\nu}=\frac{1}{2}\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}$ is the dual field strength obtained from the original under the replacement $(\underline{E},\underline{B})\rightarrow(\underline{B},-\underline{E})$. Notice the absence of a corresponding magnetic current $4$-vector $\tilde J^\mu$ in the second equation. This absence allows us to write field strength in terms of a gauge field. For static field configurations we have$$\Huge\underline{B}=\underline{\nabla}\times\underline{A}\implies\underline{\nabla}\cdot\underline{B}=0$$with no magnetic charge density $\tilde\rho$ to source the magnetic field $\underline{B}$. Therefore point-like electric sources are allowed, however point-like magnetic sources are forbidden.

Using the classical Maxwell equation $\underline{\nabla}\cdot\underline{E}=\rho$, we can place a point charge of magnitude $q$ at the origin, $\underline{\nabla}\cdot\underline{E}=2\pi q\delta(\underline{x})$. This is the classic electric monopole and one can integrate to find:$$\Huge\frac{1}{2\pi}\int_{\partial V}\underline{E}\cdot d\underline{S}=q$$What this means is that the field lines of the electric field lines always start and end at charges. One can do the same for the magnetic field equation to find that magnetic field lines are always closed.

Dirac looked for the equivalent of a magnetic monopole writing $\underline{B}=\underline{\nabla}\times\underline{A}$ and aiming to get a similar integral:$$\Huge\frac{1}{2\pi}\int_{\partial V}\underline{B}\cdot d\underline{S}=m\neq0$$This is not admitted under the classic interpretation of the Maxwell equations, as writing $\underline{B}=\underline{\nabla}\times\underline{A}$ directly implies $\underline{\nabla}\cdot\underline{B}=0$, which disallows the existence of the magnetic monopole. The way to remedy this is to observe that we only define the scalar field $\underline{A}$ locally.

By removing the origin, we can demand $\underline{\nabla}\cdot\underline{B}=0$ everywhere in $\Re^3\setminus\{0\}$ while still having non-vanishing magnetic flux through any two-sphere surrounding the monopole, measured by the magnetic charge$$\Huge m=\frac{1}{2\pi}\int_{S^2}\underline{B}\cdot d^2\underline{\sigma}$$where $d^2\underline{\sigma}$ is the infinitesimal area element of $S^2$.

Working on $\Re^3$ and using Gauss' theorem we can rewrite $\underline{\nabla}\cdot\underline{B}$ on $\Re^3\setminus\{0\}$ as$$\Huge \underline{\nabla}\cdot\underline{B}=2\pi m\delta(\underline{x}),\,\,\underline{x}\in\Re^3$$, however it is preferable to work in $\Re^3\setminus\{0\}$ so we can use gauge fields.

In polar coordinates we have the identities$$\Huge\underline{\nabla}\frac{1}{r}=-\frac{\underline{x}}{r^3},\,\,\Delta\frac{1}{r}=-4\pi\delta(\underline{x})$$where $r=|\underline{x}|$. We can then solve the $\Re^3$ definition of the magnetic field with:$$\Huge\underline{B}=\frac{m}{2}\frac{\underline{x}}{r^3}=\frac{m}{2r^2}\hat{\underline{x}}$$We cannot write a smooth vector potential $\underline{A}$ defined everywhere in $\Re^3$ such that $\underline{B}=\underline{\nabla}\times\underline{A}$ agrees with the delta function definition of $\underline{B}$ as we would have $\underline{\nabla}\cdot(\underline{\nabla}\times\underline{A})=0$. We can try define $\underline{A}$ on $\Re^3\setminus\{0\}$ such that $\underline{B}=\underline{\nabla}\times\underline{A}$ obeys $\underline{\nabla}\cdot\underline{B}=0$ however this too fails. Consider a vector potential $\underline{A}^+$ given by:$$\Huge A_x^+=-\frac{m}{2}\frac{y}{r(r+z)},\,\,A_y^+=\frac{m}{2}\frac{x}{r(r+z)},\,\,A_z^+=0$$The corresponding magnetic field agrees with the one defined above, however this only holds where the field is defined which is $\Re^3$ minus the origin and the negative $z$ axis. This area that is ill defined is known as a Dirac string. Defining a similar vector potential$$\Huge A_x^-=\frac{m}{2}\frac{y}{r(r-z)},\,\,A_y^-=-\frac{m}{2}\frac{x}{r(r-z)},\,\,A_z^-=0$$, we can try to patch the two together in areas that will remove the Dirac string.

Using polar coordinates, we can split $\Re^3$ into patches:$$\Huge\begin{align*}
u_+&=\left\{(r,\theta,\varphi):0\leq\theta<\frac{\pi}{2}+\epsilon\right\}\\
u_-&=\left\{(r,\theta,\varphi):\frac{\pi}{2}-\epsilon\leq\theta<\pi\right\}\\
u_+\cup u_-&=\Re^3\setminus\{0\}
\end{align*}$$Notice that our previous findings for $\underline{A}$ are valid in $u_+$, so we define $\underline{A}^+$ as this vector potential on the $u_+$ patch. We can define a similar potential that covers the $u_-$ patch as well. On the intersection, we expect:$$\Huge\underline{A}^+-\underline{A}^-=d\alpha=\frac{\partial \alpha}{\partial x}dx+\dots+\frac{\partial \alpha}{\partial z}dz$$That is, $\underline{A}^+$ and $\underline{A}^-$ are related by a Gauge redundancy. Writing $\underline{A}^\pm$ in its differential form and using spherical coordinates, we find:$$\Huge\begin{align*}
A^\pm&=A^\pm_xdx+A^\pm_ydy+A^\pm_zdz\\
&=\frac{m}{2}(\pm1-\cos\theta)d\varphi\\
\implies \underline{A}^+-\underline{A}^-&=ig\,dg^{-1}\\
&=ie^{im\varphi}e^{-im\varphi}(-im)d\varphi\\
&=m\,d\varphi
\end{align*}$$Where we have written the difference between vector potentials in terms of the group elements $g\in U(1)$ that define the Gauge transformation between $\underline{A}^+$ and $\underline{A}^-$. As we have a $U(1)$ symmetry, we must have that $m\in\mathbb{Z}$.

Note that the magnetic monopole cannot be physical, as if one integrates the total energy of the system over $\Re^3$, we get divergence (infinite energy). We can check our result directly by computing the integral we used to define our monopole and splitting it over $u_\pm$.