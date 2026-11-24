
We have studied [[Ensembles and Kinetic theory#Microstates, Macrostates, and Ensembles|ensembles]] as probability densities, we now wish to associate a given density $\rho$ with a macrostate $M$. We do this with a few different ensembles:
> We define the Microcanonical ensemble$$\huge M=(E,V,N)$$, characterised by energy $E$, volume $V$, and # of particles $N$.
> We define the Canonical ensemble$$\huge M=(T,V,N)$$, where $T$ is temperature.
> We define the Grand canonical ensemble$$\huge M=(T,V,\mu)$$, where $\mu$ is the chemical potential.

For now we focus on the first, the Microcanonical ensemble.

# Microcanonical ensemble:

This is most appropriate for an isolated system with fixed energy, volume, and # of particles. As we have fixed energy, all accessible microstates will have:$$\huge H(q,p)=E\text{ conserved}$$We saw [[Ensembles and Kinetic theory#Classical Hamiltonian mechanics|phase space]] $\mathcal{P}$ was $6N$ dimensional (in $\Re^3$), and so the above defines a $6N-1$ dimensional hypersurface. All microstates on this hypersurface are equally probable, so we require$$\Large \rho_{E,V,N}=\frac{1}{\mathcal{N}(E,V,N)}\delta(H(q,p)-E)$$, where $\mathcal{N}$ can be thought of as the # of microstates. $\rho$ is still a probability density, and so normalisation imposes:$$\Large \int d\mu\rho=1\iff\mathcal{N}(E,V,N)=\int_\mathcal{P}d\mu\,\delta(H(q,p)-E)$$Note $\mathcal{N}$ is manifestly dimensional, so a more apt description is the "area" of the hypersurface in $\mathcal{P}$. Defining$$\Large u(E)=\int_\mathcal{P}d\mu\,\theta(E-H(q,p))$$, where $\theta$ is the Heaviside step function, we see that:$$\Large \frac{d\theta(x)}{dx}=\delta(x)\implies \mathcal{N}(E)=\frac{d u(E)}{dE}$$

We can also define the Microcanonical ensemble using infinitesimal energy ranges by$$\Large \rho_{[E,E+dE]}(q,p)=\frac{\theta(E+dE-H(q,p))-\theta(E-H(q,p))}{\mathcal{N}([E,E+dE])}$$, where the denominator calculated the volume of phase space where $E<H<E+dE$ and the numerator evaluated to $1$ if $E<H<E+dE$ and $0$ otherwise. Taking the limit $dE\to0$:$$\Large\lim_{dE\to0}\rho_{[E,E+dE]}=\frac{\frac{d}{dE}\theta(E-H(q,p))dE}{\frac{d}{dE}u(E)dE}=\frac{\delta(E-H(q,p))}{\mathcal{N}(E)}$$