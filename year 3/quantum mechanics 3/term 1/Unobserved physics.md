
# Young's Slits:

Young's double slit experiment is the go-to example when explaining quantum mechanics in layman's terms, the setup is as follows:![[yet another double slit experiment]]
For the particle source, we can find the probability distribution at the screen by calling $P_1(x)$ the distribution when one of the slits is blocked, and $P_2(x)$ the distribution when the other slit is blocked. The total distribution of particles at the screen is then $P=1/2(P_1+P_2)$. Note that for physical particles, we can add detectors (i.e. a sheet of paper with bullets passing through) without changing the distribution at the screen. This is the notion of completeness.

For the electron/photon source, experiments show an interference pattern only seen with waves:
![[Double_slit_experiment.webm]]
Plotting the intensity of the waves at the screen can be done by calling the amplitude of oscillation $\psi(x)$, making the intensity $P=|\psi|^2$. This is a measure of the energy transmitted by the wave. Performing the same procedure for particles, we can find the intensity of waves emanating from each slit by writing $P_1=|\psi_1|^2,P_2=|\psi_2|^2$. Now as amplitudes add, not intensities, when considering waves, we find that $\psi=1/\sqrt{2}(\psi_1+\psi_2)$, making the final intensity $P_\text{wave}(x)=1/2|\psi_1(x)+\psi_2(x)|^2$, exactly the pattern in the diagram. Note that when measuring electrons using a Geiger counter, we get the same interference pattern as any physical particle would make, suggesting the nature of the electrons differs based on observation.

This leads to the conclusion that electrons travel as waves when not observed, despite them being observed as particles.

# The Delayed-Choice Quantum Eraser:

Consider a laser firing photons at a double slit setup with a nonlinear crystal (SPDC) as the screen. This produces entangled signal/idler photons. The signal then travels to the screen, using beam splitters the idler is routed either along which-path arms to $A,B$ (no recombination) or along paths where beams are recombined to get detected at $C,D$:![[Unobserved physics 2025-10-18 16.11.14.excalidraw]]Here, the crystal performs spontaneous parametric down-conversion (SPDC). The result of this is that each incident photon is converted into a pair of lower energy photons (signal and idler). The signal photon travels toward a detection screen, and the idler photon is routed by mirrors and beam splitters to one of four detectors ($A,B,C,D$) located very far away. If it lands in detector $C,D$ then the photons are recombined and information about the original slit is erased. However if the photons land in $A,B$, the idler photon may travel a much longer path. The final beam splitter can be inserted after the signal photon has already been detected. In any case, the coincidence counts respect:
> Interference is observed only when idler information is erased
> Interference is always present in the joint two photon state, but is only visible when the data is sorted according to idler outcomes. If we take the interference pattern from $C$ (signal photons) and add it to $D$ (signal photons), we get the same pattern at $A$

We can therefore conclude that for electrons, the slit that they pass through is meaningless in the sense that an observed wave pattern means that the information of which slit the electron passed through has been lost and cannot be recovered.
# Discrete bound energy spectra:

Recall the definition of the [[Schrodinger's equation#Hamiltonian operator|Hamiltonian operator]] $H=p^2/2m+U(x)$ for some potential $U$. The [[Hamiltonian Formalism]] dictates $\dot p=-\frac{\partial H}{\partial x},\dot x=\frac{\partial H}{\partial p}$, we then have $\dot x=p/m,p=\dot xm$. Taking the time derivative of the second expression we see $m\ddot x=-\frac{\partial U}{\partial x}$, Newton's law. For any potential, we can prove the conservation law $\frac{d H}{dt}=0$:$$\Huge\begin{align}
\frac{d H}{dt}&=\frac{\partial H}{\partial t}+\frac{d x}{dt}\frac{\partial H}{\partial x}+\frac{d p}{dt}\frac{\partial H}{\partial p}\\
&=0+\frac{\partial H}{\partial p}\frac{\partial H}{\partial x}-\frac{\partial H}{\partial p}\frac{\partial H}{\partial x}=0
\end{align}$$This can also be proven using a [[Hamiltonian Formalism#Poisson bracket|Poisson bracket]]:$$\Huge\begin{align}
\frac{d A}{dt}&=\frac{\partial A}{\partial t}+\frac{d x}{dt}\frac{\partial A}{\partial x}+\frac{d p}{dt}\frac{\partial A}{\partial p}\\
&=\frac{\partial A}{\partial t}+\{A,H\}\\
\implies\frac{d H}{dt}&=\frac{\partial H}{\partial t}+\{H,H\}=0
\end{align}$$This is not the case in Quantum Mechanics, energy can only take discrete values, not any continuous value. Two variables are canonical conjugate if their Poisson bracket is $1$, in QM we have $\{x,p\}=1$ as our canonical conjugate variables.

Making a measurement of $x=x_0$ collapses the wave function and causes an infinite probability spike at $x=x_0$, that is $\psi(x)=\delta(x-x_0)$. Then we see that the [[Fourier transform]] of the wave function $\psi$ takes form:$$\Huge \tilde\psi(p)=\frac{1}{2L}\int_{-L}^{L}e^{ipx_0/\hbar}\delta(x-x_0)dx=\frac{1}{2L}$$if $x_0=0$. We see that the function $\psi(x)$ settles into energy eigenstates, which are stable. Any trapped state ends up like this, arranged by energy (principal quantum number).