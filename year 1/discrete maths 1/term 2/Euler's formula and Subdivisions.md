Let $G=(V,E,\phi)$ be a [[Planarity, Faces, and Boundaries#Planarity|planar graph]] with [[Planarity, Faces, and Boundaries#Faces and Boundaries|face]] set $F$ and $k$ connected components. Then Euler states:$$\Huge |V|-|E|+|F|=k+1$$This is proven by induction on $|E|$. Take our base case to be $|E|=0$. Then every vertice is a connected component, so $|V|=k$. Then the formula becomes $|V|-|E|+|F|=k-0+1=k+1$, which is true. This is because there will only be one face, the unbounded one.

Assume Euler's formula is true for any planar graph with $k$ connected components and $|E|=k$. Remove any edge $e\in E$ to form the graph $G_0$. Now, $G_0$ has $|V|$ vertices, $|E|-1$ edges, $k_0$ connected components, and $|F_0|$ faces. Using the induction hypothesis:$$\Huge |V|-(|E|-1)+|F_0|=k_0+1$$Consider the two cases:
>$e$ was a bridge. Removing $e$ increased the amount of connecting components by $1$, $k_0=k+1$, and will not change the number of faces $|F|=|F_0|$, so we get:$$\Huge |V|-(|E|-1)+|F|=k+1+1\implies|V|-|E|+|F|+1=k+1$$This simplifies to show that the formula holds when removing $e$.
>$e$ was not a bridge. Removing $e$ does not disconnect $G$, so $k_0=k$ and by the [[Planarity, Faces, and Boundaries#Jordan curve theorem|Jordan curve theorem]], $e$ divided a face into two so removing $e$ will decrease the amount of faces in $G_0$ by $1$. That is $|F_0|=|F|-1$, so the formula becomes:$$\Huge |V|-(|E|-1)+(|F|-1)=k+1\implies|V|-|E|+|F|+1-1=k+1$$Which again simplifies to prove the formula.

# Simple planar graphs have few edges:

If $G=(V,E)$ is a simple planar graph with $|V|\geq 3$ then:$$\Huge |E|\leq3|V|-6$$This is proven by considering that if $G$ has at least $2$ edges, then $b(f)\geq 3$ for every face. This becomes:$$\Huge 2|E|=\sum_{f\in F}b(f)\geq\sum_{f\in F}3=3|F|$$If $G$ has one or fewer edges then we already get the inequality for free. Now use this bound with Euler's formula:$$\Huge |V|-|E|+\frac{2|E|}{3}\geq k+1\geq 2$$Which simplifies to prove the inequality.

# Girth:

We define the girth, $g$, of a graph $G=(V,E)$ to be the length of the shortest cycle in $G$. We then propose that if $G$ is simple and planar with nonzero girth then:$$\Huge |E|\leq\frac{g}{g-2}(|V|-2)$$To prove this, start with the planar handshaking lemma. Note that for every face, $b(f)\geq g$ by definition:$$\Huge 2|E|=\sum_{f\in F}b(f)\geq\sum_{f\in F}g=g|F|$$Again using Euler's formula:$$\Huge |V|-|E|+\frac{2|E|}{g}\geq k+1\geq 2$$Which simplifies to prove the inequality.

# Subdivisions:

A subdivision of a graph $G$ is obtained by subdividing the edges of $G$. To subdivide an edge $e=uv$:
> Add a new vertex $w$ to $G$
> Add edges $uw, vw$
> Remove $e$

New edges can further be subdivided. Note that subdivision does not change the planarity of a graph. To undo subdivision, you can remove any vertices of degree $2$ by joining the edges this vertex connects with a new edge.

## Kuratowski's Theorem:
A graph $G$ is planar if and only if $G$ contains no subdivisions of $K_5$ or $K_{3,3}$ as a subgraph. This is proven in chapter $11$ of Frank Harary's "Graph Theory".

Every finite simple graph has a vertex of degree $\leq 5$. This is obviously true for $|V|\leq 6$ (see above inequalities), for $|V|>6$. Assume every vertex has degree $\geq 6$, then by handshaking we get $2|E|\geq 6|V|\implies|E|\geq 3|V|$, which does not satisfy the above inequalities so $G$ cannot be planar.

# Platonic graphs:

A platonic graph is finite, simple, planar, connected, and has all vertices with the same degree $\geq3$, and has all faces with the same boundary length $\geq3$.

There are only $5$ platonic graphs. We prove this as follows:![[platonic solids proof]]