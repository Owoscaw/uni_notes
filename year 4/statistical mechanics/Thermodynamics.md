

Thermodynamics is a phenomenological theory that describes relationships among observable properties of macroscopic systems in equilibrium. This is an experimentally motivated, observation based theory that does not try to describe fundamental truth. We have a set of axioms, known as the Laws of Thermodynamics.

# Definitions:
> Isolated system: A system unaffected by external influences, which we denote with double lines (called adiabatic walls, e.g. perfectly insulating thermos).
> Non-isolated system: A system affected by external influences, which we denote with single lines (called diathermal walls, e.g. Durham uni free thermos). We say such a system is in "thermal contact" with its environment.
> Equilibrium: A state in which no further macroscopic change is observable.
> State variables: Macroscopic quantities that specify the state of a system, we postulate that these specify equilibrium states.

The prototypical example used throughout these notes is the isolated system of gas in a box, which has state variables pressure $p$ and volume $V$.

# Mutual thermal equilibrium:

Consider two isolated systems $A,B$  with state variables $(p_A^i,V_A^i),(p_B^i,V_B^i)$. Now consider what happens if we put these systems in thermal contact with each other. We say that the combined system will relax to a state of mutual thermal equilibrium. 

When this is reached, we will have new state variables $(p_A^f,V_A^f),(p_B^f,V_B^f)$ that are not the same as before. Mutual thermal equilibrium implies some relation$$\Huge F_{AB}(p_A^f,V_A^f;p_B^f,V_b^f)=0$$, which can be inverted if it is sufficiently well behaved. Or equivalently we could have a relation like:$$\Huge V_B^f=g_{AB}(p_A^f,V_A^f;p_B^f)$$
As an example, consider three systems $A,B,C$ where:
>$A,B$  as well as $B,C$ share a diathermal wall
>$A,C$ share an adiabatic wall

We ask if $A,C$ will reach mutual thermal equilibrium. This is the "0th" Law of Thermodynamics: If $A,B$ are each in equilibrium with $C$, then they are in equilibrium with each other. That is to say, mutual thermal equilibrium is transitive.

Let us assume we have the state variable relations for this system:$$\Huge\begin{align*}
\text{MTE}\implies V_B&=g_{AB}(p_A,V_A;p_B)\\
&=g_{BC}(p_C,V_C;p_B)\\
\implies g_{AB}&=g_{BC}
\end{align*}$$Now our $0$th law implies MTE between $A,C$ so we have another relation:$$\Huge F_{AC}(p_A,V_A;p_C,V_C)=0$$This came from our understanding of MTE, so we expect the relation $g_{AB}=g_{BC}$ to imply the above. Note that the above is independent of $p_B$, so we can drop the $p_B$ dependence. Two systems in MTE are characterised by a function $\theta(p,V)$ which is equal in MTE. We call this function the Empirical temperature:$$\Huge \text{MTE}\implies \theta_A(p_A,V_A)=\theta_C(p_C,V_C)$$Remarks:
>Note that this definition is not unique, and $\tilde\theta(\theta)$ is also an "Empirical temperature". Consider an ideal gas. By default we have $T=\frac{pV}{c}$, which is of form:$$\Huge \theta=\theta(p,V)=\frac{pV}{c}$$This is called our "Equation of state". 
>If we set $\theta(p,V)=\theta_0$, we trace out lines in the $p,V$ plane which we call "isotherms".

# Energy, heat, and the 1st Law:

We define the work as the transfer of energy due to forces exerted:$$\Huge W=\int\underline{F}\cdot d\underline{x}$$The only way to change the amount of energy in a system is through either work done or heat. We can now define the $1$st Law of Thermodynamics:
> The amount of work needed to change an otherwise isolated system from one state to another is independent of how the work is performed

This implies the existence of some quantity we call energy, $E=E(p,V)$. Our first law can then be written as$$\Huge\implies\Delta E=E(p_2,V_2)-E(p_1,V_1)=W$$for an adiabatic process.

Considering diathermal processes, we also give the definition$$\Huge \Delta E=W+Q$$where $Q$ is heat. Note that while $E$ is a function of state variables, $W,Q$ are not properties of the system and are instead modes of energy transfer.

## Quasi-static processes:
A quasi-static process is one where a system remains in equilibrium throughout. That is, we change a system slowly enough so that equilibrium is re-achieved after every infinitesimal time step.

We can also write a new $1$st law for these QSP:$$\Huge dE=\dbar Q+\dbar W$$Since $E(p,V)$ is a function of state variables, we can write $dE$ using the chain rule:$$\Huge dE=\frac{\partial E}{\partial p}\vert_Vdp+\frac{\partial E}{\partial V}\vert_pdV,\,\,\oint_CdE=0$$Where $C$ is a closed loop in the $p,V$ plane. Note that $\dbar Q,\dbar W$ are not exact differentials, and so we cannot do the above with them.