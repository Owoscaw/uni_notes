
We have studied [[Ensembles and Kinetic theory#Microstates, Macrostates, and Ensembles|ensembles]] as probability densities, we now wish to associate a given density $\rho$ with a macrostate $M$. We do this with a few different ensembles:
> We define the Microcanonical ensemble$$\huge M=(E,V,N)$$, characterised by energy $E$, volume $V$, and # of particles $N$.
> We define the Canonical ensemble$$\huge M=(T,V,N)$$, where $T$ is temperature.
> We define the Grand canonical ensemble$$\huge M=(T,V,\mu)$$, where $\mu$ is the chemical potential.

For now we focus on the first, the Microcanonical ensemble.

# Microcanonical ensemble:

This is most appropriate for an isolated system with fixed energy, volume, and # of particles. As we have fixed energy, all accessible microstates will have:$$\huge H(q,p)=E\text{ conserved}$$We saw [[Ensembles and Kinetic theory#Classical Hamiltonian mechanics|phase space]] $\mathcal{P}$ was $6N$ dimensional (in $\Re^3$), and so the above defines a $6N-1$ dimensional hypersurface. All microstates on this hypersurface are equally probable, so we require$$\Large \rho_{E,V,N}=\frac{1}{\mathcal{N}(E,V,N)}\delta(H(q,p)-E)$$, where $\mathcal{N}$ can be thought of as the # of microstates. $\rho$ is still a probability density, and so normalisation imposes:$$\Large \int d\mu\rho=1\iff\mathcal{N}(E,V,N)=\int_\mathcal{P}d\mu\,\delta(H(q,p)-E)$$Note $\mathcal{N}$ is manifestly dimensional, so a more apt description is the "area" of the hypersurface in $\mathcal{P}$. Defining$$\Large u(E)=\int_\mathcal{P}d\mu\,\theta(E-H(q,p))$$, where $\theta$ is the Heaviside step function, we see that:$$\Large \frac{d\theta(x)}{dx}=\delta(x)\implies \mathcal{N}(E)=\frac{d u(E)}{dE}$$

We can also define the Microcanonical ensemble using infinitesimal energy ranges by$$\Large \rho_{[E,E+dE]}(q,p)=\frac{\theta(E+dE-H(q,p))-\theta(E-H(q,p))}{\mathcal{N}([E,E+dE])}$$, where the denominator calculated the volume of phase space where $E<H<E+dE$ and the numerator evaluated to $1$ if $E<H<E+dE$ and $0$ otherwise. Taking the limit $dE\to0$:$$\Large\lim_{dE\to0}\rho_{[E,E+dE]}=\frac{\frac{d}{dE}\theta(E-H(q,p))dE}{\frac{d}{dE}u(E)dE}=\frac{\delta(E-H(q,p))}{\mathcal{N}(E)}$$

## Statistical entropy:
Boltzmann claims we have a more intuitive definition of [[Thermodynamics#Entropy and the arrow of time|entropy]] at the $\mu$-state level$$\Large S(E,V,N)=k_B\log(\Omega(E,V,N))$$, where $\Omega$ is the # of accessible $\mu$-states on the $H=E$ hypersurface. This is related to $\mathcal{N}(E,V,N)$ by:$$\Large \Omega(E,V,N)=\frac{\mathcal{N}(E,V,N)}{\mathcal{N}_0}$$Here, $\mathcal{N}_0$ is the area per microstate along the hypersurface. Generally, $\Omega$ grows with $N$ (# of particles). The constant $k_B$ in our new entropy definition is known as Boltzmann's constant, which has units $\text{JK}^{-1}$ (energy). We mentioned the correlation between lack of information and entropy, which we gain new insight on via our $\mu$-state understanding. Larger entropy is associated with less certainty about the $\mu$-state we are in. Note $\mathcal{N}_0$ here is necessitated by$$\Large \mathcal{N}=\int_\mathcal{P}d\mu\,\delta(H-E)=\int_\mathcal{P}\prod_I(dq_idp_i)\delta(H-E)\sim\text{pos}^{3N}\text{mom}^{3N}$$, a dimension full quantity. Re-scaling $\mathcal{N}_0$ has the overall effect of shifting entropy $S$ by a constant. This $\mathcal{N}_0$ appears as we are trying to use classical physics to describe an inherently quantum world, in which there is no such notion as phase space (due to the uncertainty principle). We do not need $\mathcal{N}_0$ in a quantum description, as states allowed by $E=H$ will be discrete and we find a discrete "PDF" for the microcanonical ensemble:$$\Large p_n=\frac{1}{\Omega(E)}\delta_{E,E_N}$$
## Second and zeroth laws of thermodynamics:
We proceed by ignoring $\mathcal{N}_0$, i.e. working in a quantum statistical mechanics formalism. Consider two isolated sub-systems with Hamiltonians $H_1,H_2$ and initial energy $E_1^0,E_2^0$. We can then find the total # of accessible microstates to simply be:$$\Large \Omega(E_1^0,E_2^0)=\Omega(E_1^0)\Omega(E_2^0)$$We can then find the combined initial entropy of the system:$$\Large\begin{aligned}
S_0=S(E_1^0,E_2^0)&=k_B\log(\Omega(E_1^0)\Omega(E_2^0))\\
&=S_1(E_1^0)+S_2(E_2^0)
\end{aligned}$$Now we allow these systems to exchange energy while:
> holding total energy fixed:$$\Large E=E_1+E_2=E_1^0+E_2^0$$
> holding the Hamiltonian fixed:$$\Large H=H_1+H_2+\epsilon H_\text{int}$$Noting the presence of our [[Interacting QFT#Interaction|interaction]] Hamiltonian, which we typically neglect as contributions from it are negligible.

Before this exchange, we had constraints $H_1=E_1^0,H_2=E_2^0$ and so we localised to a $\text{codim-}2$ hypersurface in phase space. After, we had but one constraint $H=H_1+H_2=E=E_1^0+E_2^0$ and so we are now localised to a $\text{codim-}1$ hypersurface. We now have many more $\mu$-states accessible to us, and so entropy must have increased. This is the second law of thermodynamics at the $\mu$-scopic scale.

More quantitatively, we can write$$\Large\begin{aligned}
\Omega(E)&=\sum_{E_1}\Omega_1(E_1)\Omega_2(E-E_1)\\
&\sim\int dE_1\Omega_1(E_1)\Omega_2(E-E_1)\\
&\sim\int dE_1\exp\left(\frac{1}{k_B}(S_1(E_1)+S_2(E-E_1))\right)\\
_{\text{using }\int\text{ of large }\exp}\exp\left(\frac{S(E)}{k_B}\right)&\approx\exp\left(\frac{1}{k_B}(S_1(E_*)+S_2(E-E_*))\right)\\
&\approx\exp\left(\frac{S_\text{max}}{k_B}\right)
\end{aligned}$$, where we borrowed some knowledge about [[Elements of Probability#Mathematical interlude - Integrals of large exponentials|integrals of large exponentials]]. We know that $E_*$ maximises $S(E_1,E-E_1)$ and so we proceed:$$\Large\begin{aligned}
\frac{\partial }{\partial E_1}(S_1(E_1)+S_2(E-E_1))\vert_{E_1=E_*}&=0\\
\implies S_\text{max}\geq S_0=S(E_1^0,E_2^0)&=S_1(E_1^0)+S_2(E-E_1^0)
\end{aligned}$$That is, $E_1\to E_*$ reaches a new equilbrium after we allow the systems to exchange energy. We have been provided with a $\mu$-scopic definition of equilibrium, the place where entropy is maximised. Computing the partial derivatives in the first line$$\Large\begin{aligned}
\implies S_1'(E_*)&=S_2'(E-E_*)\\
_\text{recalling}\frac{1}{T}&=\left(\frac{\partial S}{\partial E}\right)_{V,N}\\
\implies S_1'(E_*)=\frac{1}{T_1}&=\frac{1}{T_2}=S'_2(E-E_*)\\
\implies T_1&=T_2
\end{aligned}$$, we have arrived at the zeroth law!