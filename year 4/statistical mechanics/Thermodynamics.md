

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
> Clausius: No process is possible whose only effect is to transfer heat from a colder to a hotter body. That is, there is no such thing as an ideal fridge.

Note that these statements are logically equivalent, one could use a perfect engine to build a perfect fridge:![[Thermodynamics 2026-10-15 10.52.35.excalidraw]]The dashed blue box shows how the work done on a fridge by an ideal engine makes the system equivalent to an ideal fridge. Similarly, the existence of an ideal fridge implies the existence of an ideal engine.

## Carnot cycle:
It might appear that reversible cycles seem to convert heat to work fine via $0=W+Q$, however the cycle must necessarily dump heat out. 

Consider a reversible engine operating between heat reservoirs with fixed temperatures $\theta_H>\theta_C$. Two paths of the process are isothermal, and the other two are adiabatic:![[Thermodynamics 2026-10-15 11.46.17.excalidraw]]
The cycle is as follows:
> $AB$: Isothermal expansion $\theta_H$, during which the system has fixed temperature, but heat $Q_H$ is absorbed at a fixed temperature. That is, we have heated the system.
> $BC$: Adiabatic expansion, the system exchanges no heat this time so $\dbar Q=0$ - however the system still expands, causing a drop in temperature $\theta_H\to\theta_C$.
> $CD$: Isothermal compression $\theta_C$, $Q_C$ is dumped into the cold reservoir at a fixed temperature.
> $DA$: Adiabatic compression, causing a rise in temperature $\theta_C\to\theta_H$.

Now at the end of the cycle, we see that the first law of thermodynamics dictates:$$\Huge W=Q_H-Q_C$$We can now define the efficiency of an engine by:$$\Huge\eta=\frac{W}{Q_H}=1-\frac{Q_C}{Q_H}$$If this is $1$, all energy is used as work (an ideal engine!). Kelvin's law then dictates $\eta<1$, the engine always dumps some $Q_C>0$ into its surroundings that is not used as work. Note that $\eta$ is invariant under the following operations$$\Large\begin{aligned}
(Q_H,Q_C)&\to(-Q_H,-Q_C)&\text{reversal}\\
(Q_H,Q_C)&\to(\lambda Q_H,\lambda Q_C)&\text{run }\lambda\text{ cycles}
\end{aligned}$$, so efficiency can be thought of as a property of the engine itself.

## Carnot's theorem:
We can now prove Carnot's theorem, which states; Of all engines running between two heat reservoirs, reversible engines have the highest efficiency. 

To prove this, consider a non-reversible engine called Merlin $(Q_H',Q_C')$, coupled to a reversible engine called Carnot $(Q_H,Q_C)$ running in reverse. That is, the work output $W$ of Merlin drives Carnot in reverse. The two engines take energy $\Delta E'=Q_H'-Q_H$ from the hot reservoir and dump it into the cold reservoir $Q_C'-Q_C=Q_H'-Q_H$. Clausius' statement of the second law then dictates $Q_H'-Q_H\geq0\implies Q_H'\geq Q_H$ as a perfect fridge cannot exist. We can rearrange out statement about $\Delta E$ to say$$\Huge Q_C'-Q_H'=Q_C-Q_H$$and so we compute the efficiency of Merlin:$$\Large\begin{aligned}
\eta_\text{Merlin}&=1-\frac{Q_C'}{Q_H'}\\
&=\frac{Q_C-Q_H}{Q_H'}\\
&\leq\frac{Q_C-Q_H}{Q_H}=\eta_\text{Carnot}
\end{aligned}$$Hence proving Carnot's theorem.

### Corollary:
All reversible engines have the same efficiency, dependent only on the temperatures of the reservoirs $\theta_H,\theta_C$. This is clear to see if one imagines that a Merlin engine were indeed reversible, in which case we would find $\eta_\text{Merlin}\geq\eta_\text{Carnot}$ as we could just reverse the direction of each engine. This would force $\eta_\text{Carnot}=\eta_\text{Merlin}=\eta_\text{rev}$, and so this argument applies to ALL reversible engines. Since the engines are characterised only by the temperatures of the reservoirs, we have:$$\Huge\eta_\text{rev}=\eta(\theta_H,\theta_C)$$

## Thermodynamic temperature scale:
We now have the tools to define our true temperature, the thermodynamic temperature scale. Consider running several Carnot cycles between a few different temperatures, say from $\theta_1\to\theta_2$ and $\theta_2\to\theta_3$. Using our newfound knowledge of efficiency, we can write:$$\Large\frac{Q_2}{Q_1}=1-\eta(\theta_1,\theta_2),\,\,\frac{Q_3}{Q_2}=1-\eta(\theta_2,\theta_3)$$Now consider the composition of these engines, which forms an engine between $\theta_1$ and $\theta_3$:$$\Large\frac{Q_3}{Q_1}=1-\eta(\theta_1,\theta_3)$$We multiply the first two expressions to find$$\Large\begin{aligned}
(1-\eta(\theta_1,\theta_2))(1-\eta(\theta_2,\theta_3))&=1-\eta(\theta_1,\theta_3)\\
\implies1-\eta(\theta_H,\theta_C)&=\frac{f(\theta_C)}{f(\theta_H)}
\end{aligned}$$, since the LHS contains functions of $\theta_2$ but the RHS does not - implying that it must cancel out somehow (note we also relabeled $\theta_1,\theta_3\to\theta_H,\theta_C$). We now define the thermodynamic temperature $T$ by$$\Huge T=cf(\theta)$$where $f(\theta)$ is the function defined above, and $c$ is a constant fixed so that $T=273.15\text{K}$ at the triple point of ice-water-steam (what the fuck). We then have a nice relation between the efficiency of a reversible engine operating between two temperatures:$$\Large\eta(T_H,T_C)=1-\frac{T_C}{T_H}\equiv1-\frac{Q_C}{Q_H}$$
This is rather profound, we have defined a quantitative measure of efficiency from a set of axioms and some pretty drawings. To revel in our joy, let us consider the example of an car engine:
> Petrol burns at $1000\text{K}$ and room temperature is $300\text{K}$, so the efficiency of a Carnot engine between the two is$$\Large\eta_\text{car}\approx1-0.3=0.7$$
> This is an upper bound on efficiency, unless one could make the fuel burn hotter.

## Carnot cycle for an Ideal gas:
An ideal gas has the equation of state $pV=cT$, and $E(T,V)=E(T)$ is dependent only on temperature. Now consider a Carnot cycle as we have above:
> Along the isotherm $AB$, $T=T_H\implies dT=0$ and therefore:$$\huge dE=\frac{dE}{dT}dT=0$$Our first law then dictates:$$\huge\begin{aligned}
dE&=\dbar Q+\dbar W\\
&=\dbar Q-pdV=0\\
\implies\dbar Q&=pdV
\end{aligned}$$Allowing us to write:$$\Large\begin{aligned}
Q_H&=\int_A^B\dbar Q\\
&=\int_A^Bp\,dV\\
&=\int_A^B\frac{cT}{V}dV\\
&=cT_H\int_A^B\frac{dV}{V}=cT_H\ln\left(\frac{V_B}{V_A}\right)
\end{aligned}$$We get a similar result for the $CD$ isotherm:$$\huge Q_C=cT_C\ln\left(\frac{V_C}{V_D}\right)$$Note that we should have a leading minus sign here, as this is the heat leaving the system. However since we drew a nice diagram with arrows above, it is clear that this is the heat exiting the system and we continue with this convention throughout.
> Along the adiabat $BC$, we have $\dbar Q=0$ and so we get $dE=\dbar W=-p\,dV$ from the first law. Now by the chain rule:$$\huge\begin{aligned}
dE&=\frac{dE}{dT}dT=-p\,dV\\
&=-\frac{cT}{V}dV\\
\implies \frac{dV}{V}&=-\frac{1}{cT}\frac{dE}{dT}dT\equiv df(T)\\
_\text{where }\,f(T)&=-\frac{1}{c}\int_{T_0}^T\frac{1}{T'}\frac{dE(T')}{dT'}dT'
\end{aligned}$$Along our adiabatic path, we can write:$$\huge\begin{aligned}
\int_B^C\frac{dV}{V}&=\int_B^Cdf(T)=f(T_C)-f(T_B)\\
\implies\ln\left(\frac{V_C}{V_B}\right)&=f(T_C)-f(T_H)
\end{aligned}$$We again get a similar result for the other adiabat:$$\huge \ln\left(\frac{V_A}{V_D}\right)=f(T_H)-f(T_C)$$Note that this differs from the above by only a minus sign, giving us the result:$$\huge\begin{aligned}
\ln\left(\frac{V_A}{V_D}\right)&=-\ln\left(\frac{V_C}{V_B}\right)\\
\implies\frac{V_D}{V_A}&=\frac{V_C}{V_B}\\
\implies\frac{V_C}{V_D}&=\frac{V_B}{V_A}
\end{aligned}$$
> We can now compute the efficiency of this Carnot cycle, as we have expressions for both $Q_C,Q_H$:$$\huge\begin{aligned}
\eta&=1-\frac{Q_C}{Q_H}\\
&=1-\frac{cT_C\ln\left(\frac{V_C}{V_D}\right)}{cT_H\ln\left(\frac{V_B}{V_A}\right)}\\
&=1-\frac{T_C}{T_H}
\end{aligned}$$This is exactly the thermodynamic temperature, we have:$$\Huge T_\text{thermodynamic}=T_\text{ideal gas}$$

# 

We now switch conventions so that outgoing heat is negative, $Q_2=-Q_C<0$, and incoming heat is positive $Q_1=Q_H>0$. This makes our definition of Carnot efficiency:$$\huge \eta_\text{Carnot}=1+\frac{Q_2}{Q_1}=1-\frac{T_2}{T_1}$$