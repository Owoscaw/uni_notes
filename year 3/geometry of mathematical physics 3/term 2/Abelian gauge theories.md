
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