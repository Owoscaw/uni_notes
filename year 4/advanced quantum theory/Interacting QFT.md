
Now we have [[QFT in canonical formalism|quantised a free massive complex scalar field]], we will look at QFTs with interactions. We will mostly look at interacting theories of real scalar fields, whose action is:$$\Large S[\phi]=\int d^4x\left(-\frac{1}{2}\partial_\mu\phi\partial^\mu\phi-\frac{m^2}{2}\phi^2\right)$$After quantising, we find the Fourier expansion:$$\Large\phi(t,\underline{x})=\int\frac{d^3k}{(2\pi)^3}\frac{1}{\sqrt{2\omega_\underline{k}}}(a_\underline{k}e^{-i\omega_\underline{k}t+i\underline{k}\cdot\underline{x}}+a_\underline{k}^\dagger e^{i\omega_\underline{k}t-i\underline{k}\cdot \underline{x}})$$Note that particles in the real scalar theory are their own antiparticles, so no $b$-type operators. These operators satisfy the usual [[QFT in canonical formalism#Equal-time commutation relations|commutation relations]]$$\Large [a_\underline{k},a_\underline{k'}^\dagger]=(2\pi)^3\delta^{(3)}(\underline{k}-\underline{k'})$$, and the [[QFT in canonical formalism#Normal ordering|normal ordered]] Hamiltonian takes form:$$\Large :H_0:=\int\frac{d^3k}{(2\pi)^3}\omega_\underline{k}a_\underline{k}^\dagger a_\underline{k}\equiv H_0$$We can construct our Fock space by introducing the vacuum state annihilated by $a_\underline{k}$ and introducing particle/multiparticle states by acting with $a_\underline{k}^\dagger$. These are eigenstates of the Hamiltonian, and will have eigenvalues given by:$$\Large [H_0,a_\underline{k}]=-\omega_\underline{k}a_\underline{k},\,\,[H_0,a_\underline{k}^\dagger]=\omega_\underline{k}a_\underline{k}^\dagger$$

The simplest example of an interacting QFT is $\phi^4$ theory, with action:$$\Large S[\phi]=\int d^4x\left(-\frac{1}{2}\partial_\mu\phi\partial^\mu\phi-\frac{m^2}{2}\phi^2-\frac{\lambda}{4!}\phi^4\right)$$This additional quartic term forces the action to no longer be quadratic in $\phi$, allowing particles to interact with one another. $\lambda$ is known as the coupling constant, and is varied to control the strength of the interaction. We assume it is small and expand in powers of $\lambda$. At leading order, we just recover the action for a free massive scalar field. We then try to solve the interacting theory order by order in $\lambda$, known as [[Perturbation theory|perturbation theory]]. 

More generally, we consider theories like$$\Large S[\phi]=\int d^4x\left(-\frac{1}{2}\partial_\mu\phi\partial^\mu\phi-\frac{m^2}{2}\phi^2+\sum_{n\geq3}\frac{\lambda_n}{n!}\phi^n\right)$$with coupling constants $\lambda_n$. Since we set $\hbar=c=1$ a while ago, we measure time length and mass by a single mass scale. We denote the mass dimension of a quantity by square brackets, and we have $[\text{mass}]=-[\text{time}]=-[\text{length}]=1$ so that $[\hbar]=[c]=0$. The action should have the same units as $\hbar$, i.e. vanishing mass dimension $[S]=0$:
> $x$ is a spacetime point so $[x]=-1\implies[d^4x]=-4$ and $[\partial_\mu]=1$. In order for each term in the action to result in mass dimension $0$, we must have:$$\Large [\phi]=1,\,\,[m]=1,\,\,[\lambda_n]=4-n$$

Since the couplings carry mass dimension, we need them to be small wrt another object with the same mass dimension. Considering a process at some energy scale $E$, the dimensionless quantity we want is:$$\huge \lambda_nE^{n-4}$$For $n<4$, this quantity is small at high energies and large at low energies. We call such couplings $\lambda_{\{1,2,3\}}$ relevant, as they dictate low energy behaviour. In relativistic theory we have $E\geq m$, so we can make the combination small by taking $\lambda_{\{1,2,3\}}<<m$. For $n=4$, the combination does not depend on energy scale, we say the coupling is marginal and take $\lambda_4<<1$. Typically, high energy interactions are unavoidable in QFT so irrelevant operators lead to non-renormalisable theories.

# Interaction:

We start studying interactions by splitting the Hamiltonian of $\phi^4$ theory into a free and interacting part:$$\Large\begin{aligned}
H&=\int d^3x\left(\frac{1}{2}\pi^2+\frac{1}{2}\underline{\nabla}\phi\cdot\underline{\nabla}\phi+\frac{1}{2}m^2\phi^2+\frac{\lambda}{4!}\phi^4\right)\\
&=\int d^3x\left(\frac{1}{2}\pi^2+\frac{1}{2}\underline{\nabla}\phi\cdot\underline{\nabla}\phi+\frac{1}{2}m^2\phi^2\right)+\frac{\lambda}{4!}\int d^3x\phi^4\\
&=H_0+H_\text{int}
\end{aligned}$$If we know some operator at a reference time $t_0$, the Heisenberg picture allows us to find the time evolution of the operator:$$\Large\mathcal{O}_H(t)=e^{iH(t-t_0)}\mathcal{O}_H(t_0)e^{-iH(t-t_0)}=e^{iH(t-t_0)}\mathcal{O}_S e^{-iH(t-t_0)}$$Where we take the Schrodinger picture operator to be the Heisenberg picture operator evaluated at $t_0$, denoting each by $\mathcal{O}_S,\mathcal{O}_H(t)$ respectively. Note this implies $H_H=H_S$ and so we drop the subscript. Similarly, states evolve as:$$\Large |\psi_S(t)\rangle=e^{-iH(t-t_0)}|\psi_S(t_0)\rangle=e^{-iH(t-t_0)}|\psi_H\rangle$$
These forms of time evolution require exponentiation of the Hamiltonian, which is difficult due to the interaction terms. We do know how to exponentiate $H_0$, which we used to find the Fourier expansion form of the free theory previously. Therefore we define $\mathcal{O}_I(t)$ to be the operator time-evolved using only the Schrodinger picture free Hamiltonian $H_{0S}$:$$\Large \mathcal{O}_I(t)=e^{iH_{0S}(t-t_0)}\mathcal{O}_Se^{-iH_{0S}(t-t_0)}$$This defines our interaction picture, hence the subscript $I$. We can now relate the Heisenberg picture operator to the interaction picture operator by:$$\Large\begin{aligned}
\mathcal{O}_I(t)&=e^{iH_{0S}(t-t_0)}e^{-iH(t-t_0)}\mathcal{O}_H(t)e^{iH(t-t_0)}e^{-iH_{0S}(t-t_0)}\\
\implies |\psi_I(t)\rangle&=e^{iH_{0S}(t-t_0)}|\psi_S(t)\rangle\\
&=e^{iH_{0S}(t-t_0)}e^{-iH(t-t_0)}|\psi_H\rangle
\end{aligned}$$This picture we defined is a hybrid of the Heisenberg and Schrodinger pictures, with operators evolving by $H_0$ and states evolving by $H_\text{int}$.

We can now construct our interaction picture field, an operator in the interacting QFT. Parametrising the field and it's conjugate momentum as$$\Large\begin{aligned}
\phi_S(\underline{x})&=\int\frac{d^3k}{(2\pi)^3}\frac{1}{\sqrt{2\omega_\underline{k}}}(a_\underline{k}e^{-i\omega_\underline{k}t_0+i\underline{k}\cdot\underline{x}}+a_\underline{k}^\dagger e^{i\omega_\underline{k}t_0-i\underline{k}\cdot\underline{x}})\\
\pi_S(\underline{x})&=-i\int\frac{d^3k}{(2\pi)^3}\sqrt{\frac{\omega_\underline{k}}{2}}(a_\underline{k}e^{-i\omega_\underline{k}t_0-i\underline{k}\cdot\underline{x}}+a_\underline{k}^\dagger e^{i\omega_\underline{k}t_0-i\underline{k}\cdot\underline{x}})
\end{aligned}$$, we find we can write the free Schrodinger Hamiltonian as:$$\Large H_{0S}=\int\frac{d^3k}{(2\pi)^3}\omega_\underline{k}a_\underline{k}^\dagger a_\underline{k}$$

Time dependence of the field and free Hamiltonian take a complex form in the Heisenberg picture, however in our interaction picture, they take a simpler form:
> Starting from the canonical commutation relations$$\Large\begin{aligned}
[\phi(\underline{x}),\phi(\underline{y})]=[\pi(\underline{x}),\pi(\underline{y})]&=0,\,\,[\phi(\underline{x}),\pi(\underline{y})]=i\delta^{(3)}(\underline{x}-\underline{y})\\
\implies[a_\underline{k},a_\underline{k'}^\dagger]=(2\pi)^3\delta^{(3)}(\underline{k}-\underline{k}')&,\,\,[H_{0S},a_\underline{k}^\dagger]=\omega_\underline{k}a_\underline{k}^\dagger,\,\,[H_{0S},a_\underline{k}]=-\omega_\underline{k}a_\underline{k}
\end{aligned}$$, with remaining commutators vanishing. 
> Therefore, the interaction picture field in our interacting theory is given by$$\Large\phi_I(t,\underline{x})=\int\frac{d^3k}{(2\pi)^3}\frac{1}{\sqrt{2\omega_\underline{k}}}(a_\underline{k}e^{-\omega_\underline{k}t+i\underline{k}\cdot\underline{x}}+a_\underline{k}^\dagger e^{i\omega_\underline{k}t-i\underline{k}\cdot\underline{x}})$$, the same form as the Heisenberg picture.

Here, we have evolved the field only with the free Hamiltonian which we have studied extensively. It remains to relate the Heisenberg picture to the interaction picture, which we do as follows:$$\Large\begin{aligned}
\mathcal{O}_H(t)&=e^{iH(t-t_0)}\mathcal{O}_H(t_0)e^{-iH(t-t_0)}\\
&=e^{iH(t-t_0)}e^{-iH_{0S}(t-t_0)}\mathcal{O}_H(t_0)e^{iH_{0S}(t-t_0)}e^{-iH(t-t_0)}\\
&=U^\dagger(t,t_0)\mathcal{O}_I(t)U(t,t_0)
\end{aligned}$$Where we have used the time evolution operator, defined next.
## Time evolution operator:
The relation between the Heisenberg and interaction pictures suggest that it will be useful to define the time evolution operator$$\Large U(t,t_0)=e^{iH_{0S}(t-t_0)}e^{-iH(t-t_0)}$$such that:$$\Large\mathcal{O}_I(t)=U(t,t_0)\mathcal{O}_H(t)U^\dagger(t,t_0),\,\,|\psi_I(t)\rangle=U(t,t_0)|\psi_H\rangle$$This can be thought of as the full Hamiltonian evolution minus the free theory Hamiltonian evolution. Note:$$\Large\begin{aligned}
i\frac{\partial }{\partial t}U(t,t_0)&=e^{iH_{0S}(t-t_0)}(-H_{0S}+H)e^{-iH(t-t_0)}\\
&=e^{iH_{0S}(t-t_0)}H_{\text{int }S}e^{-iH_{0S}(t-t_0)}U(t,t_0)\\
&=H_{\text{int }I}(t)U(t,t_0)\\
_\text{where }H_{\text{int }I}(t)&=e^{iH_{0S}(t-t_0)}H_{\text{int }S}e^{-iH_{0S}(t-t_0)}
\end{aligned}$$This is a differential equation of the form:$$\Large\begin{aligned}
i \frac{d}{dt}F(t)&=\alpha(t)F(t)\\
F(t)&=A\exp\left(-i\int_{t_0}^t \alpha(T')dT'\right)
\end{aligned}$$We would naively assume that we can solve this with$$\Large \tilde U(t,t_0)=\exp\left(-i\int_{t_0}^tH_I(t')dt'\right)$$subject to $\tilde U(t_0,t_0)=\mathbb{1}$, however it turns out that the correct solution is given by Dyson's formula, $$\Large U(t,t_0)= T\exp\left(-i\int_{t_0}^tH_I(t')dt'\right)$$, where $T$ is the [[Propagators and Causality#Feynman propagator|time ordering]] operator. Now we can expand the exponential of our operator to write:$$\Large\begin{aligned}
U(t,t_0)&=T\left(\mathbb{1}-i\int_{t_0}^tH_I\left(t'\right)dt'-\frac{1}{2}\int_{t_0}^tdt_1H_I(t_1)\int_{t_0}^tdt_2H_I(t_2)\right)+\mathcal{O}(\lambda^3)\\
&=\mathbb{1}-i\int_{t_0}^tH_I(t')dt'-\frac{1}{2}T\left(\int_{t_0}^tdt_1H_I(t_1)\int_{t_0}^tdt_2H_I(t_2)\right)+\mathcal{O}(\lambda^3)
\end{aligned}$$Note that the first two terms were already time-ordered trivially, so we only need to look at the second-order term:$$\begin{aligned}
T\left(\int_{t_0}^tdt_1H_I(t_1)\int_{t_0}^tdt_2H_I(t_2)\right)&=T\left(\int_{t_0}^tdt_1\int_{t_0}^{t_1}dt_2 H_I(t_1)H_I\left(t_2\right)+\int_{t_0}^tdt_1\int_{t_1}^tdt_2H_I(t_1)H_I(t_2)\right)\\
&=\int_{t_0}^tdt_1\int_{t_0}^{t_1}dt_2H_I(t_1)H_I(t_2)+\int_{t_0}^tdt_1\int_{t_1}^tdt_2H_I(t_2)H_I(t_1)
\end{aligned}$$Here, we used the notion of time ordering to split the integrals so that we integrate earlier times first, and later times second:![[Interacting QFT 2026-11-20 17.26.57.excalidraw]]

We can generalise this to:$$\Large\begin{aligned}
U(t_2,t_1)&=\begin{cases}T\exp(-i\int_{t_1}^{t_2}dt'H_I(t')) & t_2>t_1\\
T\exp(i\int_{t_2}^{t_1}dt'H_I(t')) & t_1>t_2 \end{cases}\\
&=e^{iH_{0S}(t_2-t_0)}e^{-iH(t_2-t_1)}e^{-iH_{0S}(t_1-t_0)}
\end{aligned}$$This makes it clear what we are doing:
> First, we evolve according to the free Hamiltonian from time $t_0$ to $t_1$.
> Next, we evolve according to the full Hamiltonian from time $t_1$ to $t_2$.
> Lastly, we "undo" the time evolution from the free Hamiltonian from time $t_0$ to $t_2$.

It is intuitive to see that this will leave behind the time evolution associated with the full Hamiltonian between times $t_1,t_2$. Note in general, one would systematically compute the form of $U$according to a Feynman diagram. Our operator in this form has the following properties:
> $U(t_1,t_1)=\mathbb{1}$
> $U(t_1,t_2)U(t_2,t_3)=U(t_1,t_3)$, composition
> $(U(t_1,t_2))^\dagger=U(t_2,t_1)=U(t_1,t_2)^{-1}$, unitarity

## Vacuum state:
It remains to relate the ground state $|0\rangle$ of the free Hamiltonian in the Schrodinger picture $H_{0S}$ to $|\Omega\rangle$, the vacuum associated with the full theory. Let us consider the time evolution of $|0\rangle$: