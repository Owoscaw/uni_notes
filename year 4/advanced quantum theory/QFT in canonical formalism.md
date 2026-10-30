
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
\end{aligned}$$This is just the EOM for a simple harmonic oscillator, i.e:$$\Large\omega_\underline{k}=\sqrt{|\underline{k}|^2+m^2}\implies(\partial_t^2+\omega_\underline{k}^2)\tilde\phi(t,\underline{k})=0$$That is, each Fourier mode of $\phi(t,\underline{x})$ is a SHO which we know how to [[Quantum S.H.O.|quantise]]. The most general solution is therefore:$$\Large\tilde\Phi(t,\underline{k})=\frac{1}{\sqrt{2\omega_\underline{k}}}(a_\underline{k}e^{-i\omega_\underline{k}t}+b^*_{-\underline{k}}e^{i\omega_\underline{k}t})$$Returning to position space, we can write the solution as:$$\Large\begin{aligned}\Phi(t,\underline{x})&=\frac{1}{(2\pi)^3\sqrt{2\omega_\underline{k}}}\int e^{i\underline{k}\cdot\underline{x}}(a_\underline{k}e^{-i\omega_\underline{k}t}+b^*_{-\underline{k}}e^{i\omega_\underline{k}t})d^3k\\
&=\frac{1}{(2\pi)^3\sqrt{2\omega_\underline{k}}}\int a_\underline{k}e^{i(\underline{k}\cdot\underline{x}-\omega_\underline{k}t)}+b^*_\underline{k}e^{i(\omega_\underline{k}t-\underline{k}\cdot\underline{x})}d^3k
\end{aligned}$$Writing $k^\mu=(\omega_\underline{k},\underline{k}),x^\mu=(t,\underline{x})$ our solution becomes:$$\Large\Phi(t,\underline x)=\frac{1}{(2\pi)^3\sqrt{2\omega_\underline{k}}}\int a_\underline{k}e^{ik_\mu x^\mu}+b^*_\underline{k}e^{-ik_\mu x^\mu}d^3k$$Note we can recover the real scalar field by demanding $b_\underline{k}=a_\underline{k}$. We are now ready to apply the canonical quantisation, promoting $\Phi,\pi$ to operators:$$\Large\begin{aligned}
\hat\Phi(t,\underline{x})&=\frac{1}{(2\pi)^3\sqrt{2\omega_\underline{k}}}\int\hat a_\underline{k}e^{ik_\mu x^\mu}+\hat b^\dagger_\underline{k}e^{-ik_\mu x^\mu}d^3k\\
\hat\Phi(t,\underline{x})^\dagger&=\frac{1}{(2\pi)^3\sqrt{2\omega_\underline{k}}}\int\hat a_\underline{k}^\dagger e^{-ik_\mu x^\mu}+\hat b_\underline{k}e^{ik_\mu x^\mu}d^3k\\
\pi&=\frac{\partial \mathcal{L}}{\partial (\partial_t\Phi)}=\partial_t\Phi^*\\
\implies\hat\pi(t,\underline{x})&=\partial_t\hat\Phi(t,\underline{x})^\dagger\\
&=-i\sqrt{\frac{\omega_\underline{k}}{2}}\int\hat b_\underline{k}e^{ik_\mu x^\mu}-\hat a_\underline{k}^\dagger e^{-ik_\mu x^\mu}\frac{d^3k}{(2\pi)^3}\\
\hat\pi(t,\underline{x})^\dagger&=-i\sqrt{\frac{\omega_\underline{k}}{2}}\int\hat a_\underline{k}e^{ik_\mu x^\mu}-\hat b_\underline{k}^\dagger e^{-ik_\mu x^\mu}\frac{d^3k}{(2\pi)^3}
\end{aligned}$$We can think of each of these as a "sum over infinitely many SHOs". What remains to do is:
> Impose equal time canonical commutation relations between $\hat\Phi,\hat\pi$
> Find commutation relations for our constants 
> Use creation/annihilation operators to construct spectrum

## Equal time commutation relations:
Applying the equal time commutation relations on our operators shows:$$\Large\begin{aligned}
[\hat\Phi(t,\underline{x}),\hat \pi(t,\underline{y})]&=[\hat\Phi(t,\underline{x})^\dagger,\hat\pi(t,\underline{y})^\dagger]\\
&=i\delta(\underline{x}-\underline{y})
\end{aligned}$$All other commutators are trivially zero. Using the identity$$\Large\int e^{i\underline{p}\cdot\underline{x}}d^3x=(2\pi)^3\delta(\underline{p})$$, we proceed to isolate the $k'$th Fourier mode:$$\Large\begin{aligned}
\int e^{i\underline{k'}\cdot\underline{x}}\hat\Phi(t,\underline{x})d^3x&=\frac{1}{\sqrt{2\omega_\underline{k}}}\iint(\hat a_\underline{k}e^{-i\omega_\underline{k}t+i\underline{k}\cdot\underline{x}}+\hat b_\underline{k}^\dagger e^{i\omega_kt-i\underline{k}\cdot\underline{x}})e^{i\underline{k}'\cdot\underline{x}}\frac{d^3k}{(2\pi)^3}d^3x\\
&=\int\frac{d^3k}{(2\pi)^2}\frac{1}{\sqrt{2\omega_\underline{k}}}\left(\hat a_\underline{k}e^{-i\omega_kt}\int d^3x(e^{i(\underline{k}+\underline{k}')\cdot\underline{x}})\\
+\hat b_\underline{k}^\dagger e^{i\omega_\underline{k}t}\int d^3x(e^{i(\underline{k}'-\underline{k})\cdot\underline{x}})\right)\\
&=\frac{1}{\sqrt{2\omega_\underline{k}}}(\hat a_{-\underline{k}'}e^{-i\omega_\underline{k'}t}+\hat b_\underline{k'}^\dagger e^{i\omega_\underline{k'}t})
\end{aligned}$$Similarly, we can find an expression for $\hat\pi$ and therefore $\hat a_\underline{k},\hat b_\underline{k}^\dagger$:$$\Large\begin{aligned}
\int e^{i\underline{k}'\cdot\underline{x}}\hat\pi^\dagger(t,\underline{x})d^3x&=-i\sqrt{\frac{\omega_\underline{k}}{2}}(\hat a_{-\underline{k}'}e^{-i\omega_\underline{k'}t}-\hat b_\underline{k'}^\dagger e^{i\omega_\underline{k'}t})\\
\hat a_\underline{k}&=\int d^3x\,e^{-ik_\mu x^\mu}\left(\sqrt{\frac{\omega_\underline{k}}{2}}\hat\Phi\left(t,\underline{x}\right)+\frac{i}{\sqrt{2\omega_\underline{k}}}\hat\pi^\dagger(t,\underline{x})\right)\\
\hat b_\underline{k}^\dagger&=\int d^3x\,e^{ik_\mu x^\mu}\left(\sqrt{\frac{\omega_\underline{k}}{2}}\hat\Phi(t,\underline{x})^\dagger-\frac{i}{\sqrt{2\omega_\underline{k}}}\hat\pi(t,\underline{x})\right)
\end{aligned}$$We can then proceed to calculate our commutation relations for $a,b$, with our delta function identity and commutator between $\hat\Phi,\hat\pi$ in mind:$$\huge
[\hat a_\underline{k},\hat a_{\underline{k}'}^\dagger]=(2\pi)^3\delta(\underline{k}-\underline{k}')$$