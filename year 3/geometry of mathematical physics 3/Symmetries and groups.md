
Defining systems using an action $S$ provokes the definition of a symmetry.

Let $g$ be an invertible map:$$\Huge g:\begin{align}
q_i&\rightarrow g(q_i)\\
\dot q_i&\rightarrow g(\dot q_i)
\end{align}$$such that $S[g(q_i),g(\dot q_i)]=S[q_i,\dot q_i]$. In this case, $g$ is called a symmetry of the action $S$. This must hold for all generalised coordinates $q_i,\dot q_i$. For any given action $S$, we can ask about the set $G$ of all of its symmetries. The above definition has two immediate consequences:
> The identity map $g=\underline 1$ is a trivial symmetry
> For any two symmetries $g,g'$ we can form a composed symmetry:$$\Huge S[g(g'(q_i)),g(g'(\dot q_i))]=S[g'(q_i),g'(\dot q_i)]=S[q_i,\dot q_i]$$Note that it does not matter in which order $g,g'$ are applied.

These properties of $G$ exactly define a [[Basics of groups|group]], with the composition $\circ$ acting as the composition of maps and the identity map $e$ acting as $g=\underline 1$. We automatically get the first two properties of a group from these facts. Associativity comes from the fact that map compositions are intrinsically associative. The final property comes from the fact that we defined all symmetric maps to be invertible.

Note that this notion of symmetries is not entirely accurate in quantum mechanics as the only requirement for a symmetry is that it leaves the action invariant. When considering quantum system, this leads to the discovery that a group is not formed from all symmetries. This is an active area of research.

Symmetries imply conservation laws through [[Symmetries, Noether's theorem, and conservation laws#Noether's theorem|Noether's theorem]]. The Standard Model of particle physics has an important symmetry that implies baryon number must be conserved, which implies protons cannot decay into any lighter particles. Without such restriction, protons could decay into positrons, which immediately fucks us up.

We now discuss the properties of groups, and how they can act.

Take for example $U(1)$, the group of complex numbers of unit modulus under multiplication. For $\varphi\in[0,2\pi]$ we can write any group element as $g=e^{i\varphi}$. It is not true that this group is isomorphic to $[0,2\pi]$ as $\varphi=0$ and $\varphi=2\pi$ correspond to the same group element.