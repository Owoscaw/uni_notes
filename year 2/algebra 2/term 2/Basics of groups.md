
The idea of groups is to analyse the intuitive notion of symmetries. Here are some examples:![[reflections]]Here, each shape after the last gains more symmetries. Note that the circle has infinite symmetry along any axis of reflection and rotation about the center. A composition of symmetries is again a symmetry. Note that the action of performing no action (corresponding to a symmetry composed with its inverse) is also a symmetry.

We can now define the group. A group is a pair $(G,\circ)$ where $G$ is a set and $\circ$ is a [[Rings, subrings, and fields#Binary operations|binary operation]] on $G$ with the following properties:
> Associativity: $(a\circ b)\circ c=a\circ(b\circ c)\,\forall a,b,c\in G$
> Existence of the identity: $g\circ e=e\circ g=g\,\forall g\in G$
> Existence of the inverse: $\forall g\in G\exists h\in G$ such that $g\circ h=h\circ g=e$

Furthermore, an abelian group also satisfies $g\circ h=h\circ g$ for all $g,h\in G$. For example, $(\Re,+)$ forms an abelian group with $0\in\Re$ as the identity element, and the inverse of $a\in\Re$ is $-a$. Taking the [[Integral domains, units, and polynomial rings#Units|units]] of $\Re$, that is $\Re^X=\Re\setminus\{0\}$ we cannot use addition as the binary operator, so we use multiplication. We claim that $(\Re^X,\times)$ is an abelian group.  