
Non-abelian gauge theories are the language of the standard model of particle physics and establish fundamental connections between maths and physics.

We focus on compact [[Lie Groups and Algebras#Lie groups|Lie groups]] and choose to write group elements $g$ in terms of Lie algebra elements as$$\Huge g=\exp(i\alpha^at_a)$$for real numbers $\alpha_a$. That is, we write a basis of the Lie algebra as $it_a$. In such a basis the structure constants are related to the generators $t_a$ by$$\Huge [t_a,t_b]=if_{ab}^ct_c$$for $a,b,c=1,\dots,\dim\pmb g$. We can always assume that $r(g)$ is unitary for any compact Lie group. For simplicity, we write the representation of $t_a$ associated with a representation $r$ of the Lie group $t_a^{(r)}$.

# Fields:

We introduce the tools we will use to formulate actions that are invariant under non-abelian gauge transformations:
> Charged fields, denoted as $\phi$, transforming in a representation $r$ of the gauge group $G$
> The covariant derivative $D_\mu\phi$
> The gauge field $A_\mu$, present in the definition of the covariant derivative
> The field strength $F_{\mu\nu}$ of the gauge field

Let us first assume the gauge group $G$ is a classical group whose elements are matrices, and that the charged field $\phi$ transforms in the fundamental representation. This means that the gauge transformation of the charged field $\phi$ is$$\Huge\phi\rightarrow g\phi=e^{i\alpha^at_a}\phi$$where $\phi$ is a column vector. In this case, the Lie algebra generators $t_a$ are matrices and the group element $g$ is also a matrix acting on $\phi$. Recall that both the field $\phi=\phi(x)$ and the group element $g=g(x)$ and so the gauge parameter $\alpha=\alpha(x)$ also depends on space-time.

Given the charged field $\phi$, the covariant derivative is$$\Huge D_\mu\phi=\partial_\mu\phi-iA_\mu\phi$$where the gauge field $A_\mu$ is now a matrix, which turns out to be an element of the Lie algebra to ensure the consistency of its transformation:$$\Huge A_\mu=A_\mu^at_a$$We require that under the non-abelian gauge transformation above, the covariant derivative transforms in the same way as $\phi$:$$\Huge D_\mu\phi\rightarrow gD_\mu\phi$$We can view the covariant derivative as a matrix-valued differential operator$$\Huge D_\mu=\mathbb{1}\partial_\mu-iA_\mu$$which reads component-wise as:$$\Huge (D_\mu)^j_k=\delta^j_k\partial_\mu-i(A_\mu)^j_k$$We require the gauge transformation:$$\Huge\begin{align*}
D_\mu&\rightarrow gD_\mu g^{-1}\\
&\rightarrow g(\partial_\mu-iA'_\mu)g^{-1}\\
&=g(\partial_\mu g^{-1})+gg^{-1}\partial_\mu-igA_\mu g^{-1}
\end{align*}$$Note that $g,A_\mu$ are matrices and so they do not commute.

Comparing initial and final results, we have the following gauge transformation for $A_\mu$:$$\Huge\begin{align*}
A_\mu\rightarrow A_\mu'&=gA_\mu g^{-1}+ig(\partial_\mu g^{-1})\\
&=gA_\mu g^{-1}-i(\partial_\mu g)g^{-1}
\end{align*}$$Note that we used the identity:$$\Huge 0=(\partial_\mu\mathbb{1})=(\partial_\mu(gg^{-1}))=(\partial_\mu g)g^{-1}+g(\partial_\mu g^{-1})$$Remarks:
> The first term in the gauge transformation of $A_\mu$ is the adjoint action of the Lie group $G$ on a lie algebra element. This is why $A_\mu$ belongs to the lie algebra $\pmb g$.
> The second term is a correction term to the adjoint action, involving a derivative. This is also an element in the Lie algebra in the following sense. Consider the path $g(t_0+t)g^{-1}(t_0)$ which passes through the identity for $t=0$. The associated Lie algebra element is then:$$\Huge\begin{align*} \frac{\partial }{\partial t}g(t_0+t)g^{-1}(t_0)|_{t=0}&=\left(\frac{\partial }{\partial t_0}g(t_0+t)\right)g^{-1}(t_0)|_{t=0}\\
&=\left(\frac{\partial }{\partial t_0}g(t_0)\right)g^{-1}(t_0)\end{align*}$$Therefore for any path $g(t)$ we have that $(\partial_tg(t))g^{-1}(t)\in\pmb g$ for all $t$. For $g(x)$ we get paths by setting $t=x^\mu$ for some $\mu$ while keeping all other components of $x$ fixed. Hence:$$\Huge (\partial_\mu g(x))g^{-1}(x)\in\pmb g$$

Finally, analogous to $G=U(1)$, we define the field strength:$$\Huge F_{\mu\nu}=i[D_\mu,D_\nu]$$We view both sides of this as differential operators that are matrix valued. It turns out that $F_{\mu\nu}$ is a multiplicative operator. By construction, the field strength transforms as:$$\Huge F_{\mu\nu}\rightarrow gF_{\mu\nu}g^{-1}$$The proof of which is simple:$$\Huge\begin{align*}
F_{\mu\nu}=i[D_\mu,D_\nu]\rightarrow F_{\mu\nu}'&=i[gD_\mu g^{-1},gD_\nu g^{-1}]\\
&=g[D_\mu,D_\nu]g^{-1}\\
&=gF_{\mu\nu}g^{-1}
\end{align*}$$If we calculate the commutator, one can show that we can write the field strength as:$$\Huge F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu-i[A_\mu,A_\nu]$$Proof:$$\Huge\begin{align*}
-iF_{\mu\nu}&=[D_\mu,D_\nu]=[\mathbb{1}\partial_\mu-iA_\mu,\mathbb{1}\partial_\nu-iA_\nu]\\
&=[\mathbb{1}\partial_\mu,\mathbb{1}\partial_\nu]-i[\mathbb{1}\partial_\mu,A_\nu]-i[A_\mu,\mathbb{1}\partial_\nu]-[A_\mu,A_\nu]\\
&=0-i(\partial_\mu A_\nu)+i(\partial_\nu A_\mu)-[A_\mu,A_\nu]\\
&=-i(\partial_\mu A_\nu-\partial_\nu A_\mu-i[A_\mu,A_\nu])
\end{align*}$$
The finite gauge transformations of $D_\mu$ and $F_{\mu\nu}$ is by the adjoint action of the Lie group on the Lie algebra. That is, $D_\mu$ and $F_{\mu\nu}$ transform in the adjoint representation of $G$. By considering infinitesimal gauge transformations $$\Huge g=e^{i\alpha^at_a}=e^{i\alpha}=1+i\alpha+\mathcal{O}(\alpha^2)$$one can show that the infinitesimal gauge variations of the fields are$$\Huge\begin{align*}
\delta_\alpha\phi&=i\alpha\phi\\
\delta_\alpha A_\mu&=i[\alpha,A_\mu]+\partial_\mu\alpha\\
\delta_\alpha F_{\mu\nu}&=i[\alpha,F_{\mu\nu}]
\end{align*}$$where $\phi\rightarrow\phi+\delta_\alpha\phi+\mathcal{O}(\alpha^2)$. Remarks:
> Field strength $F_{\mu\nu}$ transforms in the adjoint representation of $\pmb g$ under infinitesimal gauge transformations.
> The gauge field $A_\mu$ does not transform in the adjoint representation, as the first term in its variation suggests.
> $D_\mu$ transforms in the adjoint representation.

What we have discussed generalises to arbitrary Lie groups $G$ and charged fields $\phi$ transforming in an $r$-dimensional representation $\pmb r$. Now $\phi$ is a column vector with $r$ components, and we simply replace the group element $g$ with the appropriate $r\times r$ matrix representation:$$\Huge r(g)=\exp(i\alpha^at_a^{(r)})$$
For example$$\Huge D_\mu\phi=\partial_\mu\phi-iA_\mu\phi=(\mathbb{1}_r\partial_\mu-iA_\mu^at_a^{(r)})\phi$$and$$\Huge\begin{align*}
F_{\mu\nu}\phi&=i[D_\mu,D_\nu]\phi\\
&=(\partial_\mu A_\nu-\partial_\nu A_\mu-i[A_\mu,A_\nu])\phi\\
&=(\partial_\mu A_\nu^a-\partial_\nu A_\mu^a+f_{bc}^aA_\mu^bA_\nu^c)t_a^{(r)}\phi\\
\end{align*}$$where we understand that if $\phi$ transforms in $\pmb r$ then:$$\Huge\begin{align*}
A_\mu\phi&=A_\mu^at_a^{(r)}\phi\\
F_{\mu\nu}\phi&=F_{\mu\nu}^at_a^{(r)}\phi
\end{align*}$$

# Actions and equations of motion:

Let us consider a gauge invariant action for the Lie algebra valued non-abelian gauge field $A_\mu=A_\mu^at_a$. Since the field strength $F_{\mu\nu}=F_{\mu\nu}^at_a$ transforms as$$\Huge F_{\mu\nu}\rightarrow gF_{\mu\nu}g^{-1}$$under a gauge transformation, it immediately follows that $\text{tr}(F_{\mu\nu}F^{\mu\nu})$ is gauge invariant and can therefore be used in our Lagrangian density:$$\Huge\begin{align*}
\text{tr}(F_{\mu\nu}F^{\mu\nu})&\rightarrow\text{tr}(gF_{\mu\nu}g^{-1}gF^{\mu\nu}g^{-1})\\
&=\text{tr}(g^{-1}gF_{\mu\nu}g^{-1}gF^{\mu\nu})=\text{tr}(F_{\mu\nu}F^{\mu\nu})
\end{align*}$$Where we used the cyclic property of the trace. We can now define the Yang-Mills action$$\Huge\begin{align*}
S_\text{YM}[A]&=\int\mathcal{L}_\text{YM}d^4x\\
\mathcal{L}_\text{YM}&=-\frac{1}{2g^2_\text{YM}}\text{tr}(F_{\mu\nu}F^{\mu\nu})
\end{align*}$$where we are working with normalisation such that:$$\Huge \text{tr}(t_at_b)=\frac{1}{2}\delta_{ab}$$Note that the constant $g_\text{YM}$ is known as the Yang-Mills coupling constant and controls the strength of the interactions.

It turns out we can introduce a second gauge invariant term known as the theta term$$\Huge\begin{align*}
S_\theta[A]&=\int\mathcal{L}_\theta d^4x\\
\mathcal{L}_\theta&=\frac{\theta}{16\pi^2}\text{tr}(F_{\mu\nu}\tilde F^{\mu\nu})
\end{align*}$$where $\theta$ is known as the theta angle and$$\Huge \tilde F^{\mu\nu}=\frac{1}{2}\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}$$is the dual field strength. 

To summarise, the most general gauge invariant action (up to two derivatives) that contains appropriate kinetic and interaction terms for a non-abelian gauge field $A_\mu$ is:$$\Huge\begin{align*}
S_\text{gauge}[A]&=S_\text{YM}[A]+S_\theta[A]\\
\mathcal{L}_\text{gauge}&=\mathcal{L}_\text{YM}+\mathcal{L}_\theta\\
&=-\frac{1}{2g_\text{YM}^2}\text{tr}(F_{\mu\nu}F^{\mu\nu})+\frac{\theta}{16\pi^2}\text{tr}(F_{\mu\nu}\tilde F^{\mu\nu})
\end{align*}$$If we introduce charged fields $\phi$ transforming in a representation $\pmb r$, then we can write another gauge invariant action for them using covariant derivatives. Taking $G=SU(N)$ we have$$\Huge\begin{align*}
S_\text{matter}[\phi,\phi^\dagger,A]&=\int\mathcal{L}_\text{matter}d^4x\\
\mathcal{L}_\text{matter}&=-(D_\mu\phi)^\dagger D^\mu\phi-V(\phi,\phi^\dagger)
\end{align*}$$where we require $V$ to be gauge invariant. This generalises to other classical groups $G$ by using an appropriate inner product for the kinetic term.

# The Standard Model:

The Standard Model of elementary particle physics is a gauge theory with gauge group:$$\Huge G_\text{SM}=U(1)_h\times SU(2)\times SU(3)$$The reason why field theories have relevance in particle physics is that quanta of fields are simply quantum particles. We can associate (ish) a type of particle with every field.

A gauge theory implies the existence of gauge fields which generalise electric and magnetic fields, so we think of them as a mediating force. We think of $U(1)\times SU(2)$ as the gauge groups of the electromagnetic and weak forces. The $SU(3)$ factor gives rise to the strong force, which binds quarks together in Baryons.

All we need to do to define this theory is to state the gauge symmetry and which charged matter fields we have and in which representations of $G_\text{SM}$ they transform in. Writing down the most general Lagrangian gives the Standard Model Lagrangian up to fixing free parameters. We discuss the "classical" version which neglects neutrino masses, which has $19$ free parameters.

The charged particles are $q_{Li},u_{Ri},d_{Ri},l_{Li},e_{Ri}$ for $i=1,2,3$, which are all left/right handed [[The Lorentz Group#Spinors of the Lorentz group|Weyl fermions]]. The label $i$ is called the generation, a single complex scalar $H$. These transform in the following representations:

|          | $q_{Li}$ | $u_{Ri}$ | $d_{Ri}$ | $l_{Ri}$ | $e_{Ri}$ | $H$ |
| -------- | -------- | -------- | -------- | -------- | -------- | --- |
| $U(1)_h$ | $1/3$    | $4/3$    | $-2/3$   | $-1$     | $-2$     | $1$ |
| $SU(2)$  | $2$      |          |          | $2$      |          | $2$ |
| $SU(3)$  | $3$      | $3$      | $3$      |          |          |     |
Here we have given the $U(1)$ charge to each fermion and the $2$ or $3$ indicates that they transform in the defining representation of $SU(2)$ or $SU(3)$. Blank spaces indicate no transformation. For example $l_{Li}$ has two components and $q_{Li}$ has six components as it transforms in both $SU(2)$ and $SU(3)$.

$q_{Li}=(u_{Li},d_{li}), u_{Ri}, d_{Ri}$ describe the six quarks; $i=1$ corresponds to up/down, $i=2$ corresponds to strange/charm, $i=3$ corresponds to top/bottom. $l_{Li}=(e_{Li},\nu_{Li}),e_{Ri}$ describe the leptons; $i=1$ corresponds to the electron/electron-neutrino, $i=2$ corresponds to the muon/muon-neutrino, $i=3$ corresponds to the tau/tau-neutrino. We notice several things about their interactions:
> $SU(2)$ only interacts with left-handed Weyl spinors, not right-handed. This is the origin of parity violation in nature, demonstrated in $\beta$ decay.
> Only quarks interact with the strong force.
> $U(1)$ charges are not all integers, however we use an appropriate rescaling of the generator of $U(1)$ to remedy this.

We can now write down the kinetic terms for all gauge fields and charged particles as usual. The covariant derivative of $q_{Li}$ is for example$$\Huge D_\mu q_{Li}=\left(\partial_\mu-i\frac{1}{3}(A_h)_\mu-iW_\mu-ig_\mu\right)q_{Li}$$where $(A_h)_\mu$ is the gauge field of $U(1)$, $W_\mu$ is the gauge field of $SU(2)$, and $g_\mu$ is the gauge field of $SU(3)$.

For $H$ we can write down a potential term in the Lagrangian:$$\Huge V(H)=-m|H|^2+\lambda|H|^4$$Note that $H$ is actually two complex fields as it transforms in the $2$ of $SU(2)$ and so $|H|^2=H_i\bar H_i$. It turns out that the RHS physics emerges for $m,\lambda>0$ and so the vacua of $H$ are described by:$$\Huge |H|^2=m/\lambda$$The set of options to solve this equation is gauge-invariant, however any given choice is not invariant under all elements in $U(1)_h\times SU(2)$. This is known as spontaneous symmetry breaking, the action is invariant under a symmetry but the vacuum is not.

