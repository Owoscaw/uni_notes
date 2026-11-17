
# Classical Hamiltonian mechanics:

Consider a single particle in $\Re^3$, the state of the particle is described by two coordinates $(q_\alpha(t),p_\alpha(t))\in\mathcal{P}$ where $\mathcal{P}$ is phase space. The Hamiltonian $H$ is defined as a function on phase space, typically taking form:$$\Large H(q,p)=\frac{p^2}{2m}+U(q)=\frac{1}{2m}\sum_{\alpha=1}^3p_\alpha p_\alpha+U(q)$$Hamilton's equations then dictate the time evolution of the Hamiltonian:$$\Large \dot q_\alpha=\frac{\partial H}{\partial p_\alpha},\,\,\dot p_\alpha=-\frac{\partial H}{\partial q_\alpha}$$Note the time-reversal symmetry here, $t\to-t\implies p\to-p,q\to-q$. Let us generalise this to many particles:
> Let $N$ denote the number of particles and introduce the index $i=(\alpha,I)$ where $\alpha=1,\dots,3$ and $I=1,\dots,N$. $i$ runs over $3N$ values in this case.
> Hamilton's equations therefore have the same form but with $\alpha\leftrightarrow i$. The form of the Hamiltonian in vector notation is therefore$$\Large H=\sum_{I=1}^N\frac{\underline{p}_I^2}{2m}+\sum_{I=1}^NU(\underline{q}_I)+\sum_{1\leq I<J\leq N}V(\underline{q}_I-\underline{q}_J)$$, where the last term describes interaction between particles.

Consider an observable $\mathcal{O}(q_i,p_i,t)$ and consider it's time evolution. In general, we find this using the multivariable chain rule:$$\Large\begin{aligned} \frac{d\mathcal{O}}{dt}&=\frac{\partial \mathcal{O}}{\partial t}+\sum_{i=1}^s\left(\frac{\partial \mathcal{O}}{\partial q_i}\dot q_i+\frac{\partial \mathcal{O}}{\partial p_i}\dot p_i\right)\\
&=\frac{\partial \mathcal{O}}{\partial t}+\sum_{i=1}^s\left(\frac{\partial \mathcal{O}}{\partial q_i}\frac{\partial H}{\partial p_i}-\frac{\partial \mathcal{O}}{\partial p_i}\frac{\partial H}{\partial q_i}\right)\\
&=\frac{\partial \mathcal{O}}{\partial t}+\{\mathcal{O},H\}
\end{aligned}$$Where $\{\cdot,\cdot\}$ is the [[Hamiltonian Formalism#Poisson bracket|Poisson bracket]]. For a conserved quantity, we can directly find the time evolution of $\mathcal{O}$:$$\Large \frac{d\mathcal{O}}{dt}=0\implies\frac{\partial \mathcal{O}}{\partial t}=-\{\mathcal{O},H\}=\{H,\mathcal{O}\}$$Note $H$ is a conserved quantity (if $\frac{\partial H}{\partial t}=0$) trivially, $\{H,H\}=-\{H,H\}=0$. We call this conserved quantity the energy of the system.

As an example, let us consider the SHO:
> The SHO has Hamiltonian$$\Large H=\frac{p^2}{2m}+\frac{1}{2}m\omega^2q^2=K(p)+U(q)$$, and so we get the Hamilton's equations:$$\Large\begin{aligned}
\dot q&=\frac{\partial H}{\partial p}=\frac{p}{m}\\
\dot p&=-\frac{\partial H}{\partial q}=-m\omega^2q
\end{aligned}$$
> We also compute the Poisson bracket $\{K(p),U(q)\}$:$$\Large\begin{aligned}
\{K,U\}&=\frac{\partial K}{\partial q}\frac{\partial U}{\partial p}-\frac{\partial K}{\partial p}\frac{\partial U}{\partial q}\\
&=0-\frac{p}{m}(m\omega^2q)=-p\omega^2q
\end{aligned}$$

# Microstates, Macrostates, and Ensembles:

Consider $N$ particles of gas in a box. The microstate $\mu$ is given by the complete classification of the phase space $\mathcal{P}$:$$\Large\mu(t)=(q_i(t),p_i(t))_{i=1}^s\in\mathcal{P}$$This makes the phase space $2s$ dimensional, and contains a lot of information when considering a large number of particles. The macrostate $M$ is classified by [[Thermodynamics#Definitions|state variables]], for example $M=(T,V,N)$. Therefore the map $\mu\to M$ will be many to one. The notion of an ensemble is to consider all possible microstates for a given macrostate and average over them.

A statistical ensemble is a collection of $\mathcal{N}$ copies of a physical system, each in a different microstate that realises the same macrostate. Hamilton's equations then dictate the path each different point in the ensemble will follow, the ensemble evolves "like a swarm of bees". Note as $\mathcal{N}\to\infty$, the discrete set of points looks like a continuous fluid. This prompts the definition of a volume element on $\mathcal{P}$ by$$\huge d\mu=\prod_i dq_idp_i$$, leading us to the definition of phase space density:$$\Large \rho(q,p,t)d\mu=\lim_{\mathcal{N}\to\infty}\frac{d\mathcal{N(q,p,t)}}{\mathcal{N}}$$Where $d\mathcal{N}(q,p,t)$ is the number of phase space points in a small volume $d\mu$.![[Ensembles and Kinetic theory 2026-11-17 17.42.28.excalidraw]]
Now consider the integral:$$\Large\begin{aligned}
\int_\mathcal{P}d\mu\,\rho&=\int_\mathcal{P}\left(\frac{d\mathcal{N}(q,p,t)}{\mathcal{N}}\right)\\
&=\frac{1}{\mathcal{N}}\int_\mathcal{P}d\mathcal{N}(q,p,t)=1\\
d\mathcal{N}(q,p,t)\geq0&\implies\rho(q,p,t)\geq0
\end{aligned}$$We have that $\rho$ is always positive and integrates to $1$, making $\rho$ a [[Elements of Probability#Definitions/Axioms|probability distribution]]! 

Given an observable $\mathcal{O}$, we can construct the ensemble average:$$\Large\langle\mathcal{O}(t)\rangle=\int_\mathcal{P}d\mu\,\rho(q,p,t)\mathcal{O}(q,p,t)$$Note if $\mathcal{O}=\mathcal{O}(q,p)$ is not explicitly dependent on time, $\langle\mathcal{O}\rangle$ will pick up time dependence from $\rho(q,p,t)$.