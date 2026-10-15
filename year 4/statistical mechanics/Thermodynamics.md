

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

Let us assume we have the state variable relations for this system:$$\Huge
\begin{aligned}
\text{MTE}\implies V_B&=g_{AB}(p_A,V_A;p_B)\\
&=g_{BC}(p_C,V_C;p_B)\\
\implies g_{AB}&=g_{BC}
\end{aligned}$$Now our $0$th law implies MTE between $A,C$ so we have another relation:$$\Huge F_{AC}(p_A,V_A;p_C,V_C)=0$$This came from our understanding of MTE, so we expect the relation $g_{AB}=g_{BC}$ to imply the above. Note that the above is independent of $p_B$, so we can drop the $p_B$ dependence. Two systems in MTE are characterised by a function $\theta(p,V)$ which is equal in MTE. We call this function the Empirical temperature:$$\Huge \text{MTE}\implies \theta_A(p_A,V_A)=\theta_C(p_C,V_C)$$Remarks:
>Note that this definition is not unique, and $\tilde\theta(\theta)$ is also an "Empirical temperature". Consider an ideal gas. By default we have $T=\frac{pV}{c}$, which is of form:$$\Huge \theta=\theta(p,V)=\frac{pV}{c}$$This is called our "Equation of state". 
>If we set $\theta(p,V)=\theta_0$, we trace out lines in the $p,V$ plane which we call "isotherms".

# Energy, heat, and the 1st Law:

We define the work as the transfer of energy due to forces exerted:$$\Huge W=\int\underline{F}\cdot d\underline{x}$$The only way to change the amount of energy in a system is through either work done or heat. We can now define the $1$st Law of Thermodynamics:
> The amount of work needed to change an otherwise isolated system from one state to another is independent of how the work is performed

This implies the existence of some quantity we call energy, $E=E(p,V)$. Our first law can then be written as$$\Huge\implies\Delta E=E(p_2,V_2)-E(p_1,V_1)=W$$for an adiabatic process.

Considering diathermal processes, we also give the definition$$\Huge \Delta E=W+Q$$where $Q$ is heat. Note that while $E$ is a function of state variables, $W,Q$ are not properties of the system and are instead modes of energy transfer.

## Quasi-static processes:
A quasi-static process is one where a system remains in equilibrium throughout. That is, we change a system slowly enough so that equilibrium is re-achieved after every infinitesimal time step.

We can also write a new $1$st law for these QSP:$$\Huge dE=\dbar Q+\dbar W$$Since $E(p,V)$ is a function of state variables, we can write $dE$ using the chain rule:$$\Huge dE=\frac{\partial E}{\partial p}\vert_Vdp+\frac{\partial E}{\partial V}\vert_pdV,\,\,\oint_CdE=0$$Where $C$ is a closed loop in the $p,V$ plane. Note that $\dbar Q,\dbar W$ are not exact differentials, and so we cannot do the above with them. On the contrary, $dE$ is an exact differential and therefore has the property:$$\Huge\int_{\gamma_1}dE=\Delta E=\int_{\gamma_2}dE$$Where $\gamma_1,\gamma_2$ are paths in the $p,V$ plane. This is notably not true for inexact differentials. 

Consider what happens when we change the volume by an infinitesimal amount $dV$:![[Thermodynamics 2026-10-13 17.13.45.excalidraw]]Looking at the work integral:$$\Large\begin{aligned}
W&=\int\underline{F}\cdot d\underline{x}\\
&=\int\frac{\underline{F}}{A}\cdot(Ad\underline{x})\\
&=-\int p\,dV\\
\implies\dbar w&=-p\,dV
\end{aligned}$$Compression of the volume implies $dV<0$ and therefore $\dbar W>0\implies dE>0$, energy increases. For expansion of the volume, $dV>0$ which leads to $dE<0$.

## Heat capacities:
Heat capacity measures how the energy of system responds to a change in temperature:
> For a fixed volume, we can define heat capacity:$$\Large C_V=\frac{\dbar Q}{dt}\vert_V=\frac{dE+p\,dV}{dt}\vert_V=\frac{\partial E}{\partial t}\vert_V$$
> For a fixed pressure, we can provide an alternative definition:$$\Large C_p=\frac{\dbar Q}{dt}\vert_p=\frac{dE+p\,dV}{dt}\vert_p=\frac{\partial E}{\partial t}\vert_p+p\frac{\partial V}{\partial t}\vert_p$$

# Generalised displacements:

The general expression for change in work done for a system is written as$$\Huge\dbar W=\sum_iy_idx_i$$, where $y_i$ are the generalised forces and $dx_i$ are the generalised displacements. Note that generalised displacements are called extensive (scale with system size), while generalised forces are called intensive (do not scale with system size). Here we list some common generalised displacements and forces:

| generalised               | displacement         | force                      |
| ------------------------- | -------------------- | -------------------------- |
| Gas                       | $V$                  | $-p$                       |
| Wire                      | $L$ (length)         | $T$ (tension)              |
| Magnet                    | $M$ (magnetisation)  | $H$ (magnetic field)       |
| Conserved particle number | $N$ (# of particles) | $\mu$ (chemical potential) |
We can therefore write a more general version of the $1$st law of thermodynamics:$$\Huge dE=\sum_iy_idx_i+\dbar Q$$We look to write $\dbar Q$ as an exact differential in the form $\dbar Q=\alpha\,d\sigma$. Considering two isolated systems $A,B$ separated by a diathermal wall, we call the systems in mechanical equilibrium if $p_A=p_B$ and thermal equilibrium if $\theta_A=\theta_B$. It is therefore natural to set $\alpha$ to be the empirical temperature $\theta$:$$\Huge \implies\dbar Q=\theta\,d\sigma$$However, what does $d\sigma$ represent?...

# 2nd law and the Arrow of Time:

## Engines and reversible cycles:
Reversible processes are a subset of quasi-static processes, but have the additional property that they can be ran both forward and backward in time. For such processes, friction is absent and heat comes exclusively from temperature differences. In the $p,V$ plane, consider a closed path (cycle) $C$. Reversible processes have the property that $C$ can be traversed in either direction. We must also have:$$\Huge\Delta E=0\implies W=-Q$$
When $Q>0$, we are traversing the direction where $W<0$. That is, the system converts heat into work - we call this an engine.

Consider traversing $C$ in the other direction, so we have $Q<0,W>0$. Here, work is converted to heat - we call this a fridge.

## 2nd Law of Thermodynamics:
We have two versions of this law:
> Kelvin: No process is possible whose only effect is to extract heat from a hot reservoir and convert it entirely to work. That is, there is no such thing as an ideal engine. In a physical engine with $Q_H$ being inputted, an amount of heat $Q_C>0$ is dissipated and the work converted comes to $W=Q_H-Q_C$.