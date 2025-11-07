# Early principles:

There are four initially guiding principles:
> Quantum states in Hilbert space:
> > The first principle states that the quantum state of a system is represented by a vector in a [[QM linear algebra#Hilbert space|complex Hilbert space]]:
> > >A quantum state $|\psi\rangle$ is a vector in a complex Hilbert space $\mathcal{H}$.
> > >The Hilbert space is equipped with an [[Inner product spaces|inner product]] $\langle \phi|\psi\rangle$ which allows us to calculate probability and expectation values.
> > >The state vector $|\psi\rangle$ contains all information about the quantum system.
> > >Any linear combination of allowed states is also an allowed state.
> Observables as Hermitian operators:
> > Physical observables are represented by Hermitian operators acting on the Hilbert space:
> > > An observable $A$ is represented by a Hermitian operator $\hat A$.
> > > Hermitian operators have real eigenvalues, corresponding to possible measurement outcomes.
> > > The eigenvectors of $\hat A$ form a complete orthonormal basis for the Hilbert space.
> > > The expectation value of an observable in a state $|\psi\rangle$ is given by $\langle A\rangle=\langle \psi|\hat A |\psi\rangle$.
> Measurement and probability:
> > Measurement of an observable yields one of its eigenvalues, with a probability determined by the projection of the state onto the corresponding eigenspace:
> > > For an observable $\hat A$ with eigenvalues $a_i$ and corresponding eigenvectors $|a_i\rangle$, the probability of measuring $a_i$ is:$$\Huge P(a_i)=|\langle a_i|\psi\rangle|^2=\langle \psi|\hat P_{a_i}|\psi\rangle$$where $\hat P_{a_i}=|a_i\rangle \langle a_i|$ is the projection operator onto the eigenspace of $a_i$. This is often referred to as the Born rule.
> > > The measurement process causes the wavefunction to collapse into the measured eigenstate.
> State normalisation after measurement:
> > After measurement, the state of the system collapses to the eigenstate corresponding to the measured eigenvalue, and this new state must be normalised:
> > > If outcome $a_i$ is measured, the state immediately after measurement is:$$\Huge |\psi'\rangle=\frac{\hat P_{a_i}|\psi\rangle}{\sqrt{\langle \psi|\hat P_{a_i}|\psi\rangle}}$$
> > > This ensures that the new state $|\psi'\rangle$ is normalised.
> > > Subsequent measurements of the same observable will yield the same result with certainty.

# Expectation values:

We can also derive the formula for the expectation value of an operator:$$\Huge\langle\hat O\rangle=\sum_{i=1}^mw_iP(w_i)=\sum_{i=1}^mw_i\langle \psi|\hat P_{w_i}|\psi\rangle=\langle \psi|\sum_{i=1}^mw_i\hat P_{w_i}|\psi\rangle=\langle \psi|\hat O\|\psi\rangle$$This has the exact same interpretation as the classical expectation formula as classical probability. More generally:$$\Huge \langle\hat f(\hat O)\rangle=\langle \psi|\hat f\hat O |\psi\rangle$$It is important to note that measurements cannot completely fix a quantum mechanical state.

Take for example the quantum coin, $|\psi\rangle=a |H\rangle+b |T\rangle$. Suppose we make a lot of measurements and find the probabilities of heads and tails are $h,t$ respectively. Then:$$\Huge\begin{align*}

\end{align*}$$