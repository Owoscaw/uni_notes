
In classical mechanics, we introduced the Lagrangian and Hamiltonian $L,H$. Once quantised, the Lagrangian will lead to the path integral quantisation and the Hamiltonian will lead to the canonical quantisation. For now, we focus on the latter. 

## Equal-time commutation relations:

Classically, we defined the [[Hamiltonian Formalism#Poisson bracket|Poisson bracket]] structure. When we quantise, each canonical coordinate and momentum gets promoted to operators and we can go one of two ways:
> Schrodinger's formulation defined states $|\psi(t)\rangle\in\mathcal{H}$ for a [[Hilbert space]] $\mathcal{H}$. We then had the commutator relations:$$\huge\begin{aligned}
[\hat{\underline{q}_a},\hat{\underline{q}_b}]&=[\hat p_a,\hat p_b]=0\\
[\hat q_a,\hat p_b]&=i\delta_{ab}\hat{\mathbb{I}}
\end{aligned}$$
> In Heisenberg's formulation, we treat each operator as time-evolving instead of the state itself. Note we have the exact same relations as above, however with time dependence on each operator.

When we replace $q_a(t)$ with our [[SR and Noether's theorem#Classical field theory|field]] $\phi(t,\underline{x})$ and $p_a(t)$ with our canonical momentum $\pi(t,\underline{x})$, we will arrive at the canonical equal time commutation relations. The first two are trivial:$$\Large[\hat\phi(t,\underline{x}),\hat\phi(t,\underline{y})]=[\hat\pi(t,\underline{x}),\hat \pi(t,\underline{y})]=0$$Note the last relation takes a slightly different form:$$\huge[\hat\phi(t,\underline{x}),\hat\pi(t,\underline{y})]=i\delta(\underline{x}-\underline{y})\hat{\mathbb{I}}$$We aim to construct a QFT satisfying these relations, as well as the eigenvalues/eigenstates of our equivalent of the Hamiltonian operator. 

## Free massive scalar theory:
Consider a free massive scalar field, with Hamiltonian density:$$\Large H=\frac{1}{2}\int\pi^2+\underline{\nabla}\phi\cdot\underline{\nabla}\phi+m^2\phi^2\,d^3x$$Recall this had equation of motions given by the Klein-Gordon equation:$$\Large(\partial_\mu\partial^\mu-m^2)\phi(t,\underline{x})=(-\partial_t^2+\underline{\nabla}^2-m^2)\phi(t,\underline{x})=0$$Since K-G is invariant under spatial translations, we take a [[Fourier transform]] across each spatial coordinate:$$\Large\begin{aligned}
\phi(t,\underline{x})&=\frac{1}{(2\pi)^3}\int e^{i\underline{k}\cdot\underline{x}}\tilde\phi(t,\underline{k})d^3k\\
\tilde\phi(t,\underline{x})&=\int e^{-i\underline{k}\cdot\underline{x}}\phi(t,\underline{x})d^3x\\
_\text{FT KG}\implies(\partial_t^3+|\underline{k}|^2+m^2)\tilde\phi(t,\underline{k})&=0
\end{aligned}$$This is just the EOM for a simple harmonic oscillator, i.e:$$\Large\omega_\underline{k}=\sqrt{|\underline{k}|^2+m^2}\implies(\partial_t^2+\omega_\underline{k}^2)\tilde\phi(t,\underline{k})=0$$That is, each Fourier mode of $\phi(t,\underline{x})$ is a SHO which we know how to [[Quantum S.H.O.|quantise]].