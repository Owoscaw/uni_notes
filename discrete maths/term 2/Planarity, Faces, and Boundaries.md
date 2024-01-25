
# Bipartite:

Given a [[Graph definitions|graph]] $G(V,E)$, where there exists subsets $V_1,V_2\subset V$ such that $V_1\cup V_2=V$ and $V_1\cap V_2=\emptyset$ and every edge is of form $uv$ where $u\in V_1,v\in V_2$, that is every edge connects a node in $V_1$ to a node in $V_2$, then $G$ is said to be bipartite.

If a bipartite graph is simple and if for the partition $V_1,V_2$ is such that $u\in V_1,v\in V_2\implies uv\in E$ then $G$ is the complete bipartite graph where $|V_1|=m,|V_2|=n$ and $G$ is denoted as $K_{m,n}$. This graph has $mn$ edges.

# Planarity:

A graph is planar if it can be drawn with no edges crossing. Such a drawing is a planar representation of $G$.

# Faces and Boundaries:

A planar representation of a graph $G$ divides the plane into a set of faces $F$. The boundary of a face $f$, denoted by $B(f)$ is the set of edges that contain the face. The length of $B(f)$ is the smallest length of closed [[Graph definitions#Walk|walks]] in $G$ that cover $B(f)$ denoted as $b(f)$. For a disconnected graph, $b(f)$ is defined as the smallest sum of closed walks in $G$ that cover $B(f)$:![[faces example]]In the plane, every edge has two sides but both can be bound by the same face (i.e. $f_4$ binds $de$ and $ed$). Note that for every finite planar graph, there is one infinite face (i.e. $f_4$).

Similar to the [[Graph definitions#Handshaking|handshaking lemma]], for any planar representation of a graph $G=(V,E)$ we have:$$\Huge \sum_{f\in F}b(f)=2|E|$$This is because each edge contributes $2$ to the sum of boundary lengths (one for each side). We say that an edge $e\in E$ is a bridge in $G$ if removing $e$ from $G$ increases the number of connected components.

We propose that for any edge $e\in E$ for a graph $G=(V,E)$, then $e$ is a bridge if and only if it is not a member of a cycle in $G$. Let $e$ join vertices $u,v\in V$ and compare with $G'=(V,E\setminus\{e\})$ formed by removing $e$ from $G$. Then if our proposition is true we claim that $u$ and $v$ lie in different connected components of $G'$:

If $e$ is a bridge then there are two vertices $w_1,w_2$ which are in the same connected component in $G$, but different components in $G'$. Therefore there exists a path from $w_1$ to $w_2$ in $G$, but no such path in $G'$. This is the same as saying any path from $w_1$ to $w_2$ in $G$ passes through $e$. Also in $G'$ there must be a path from either $u$ or $v$ to $w_1$ and a path from the other to $w_2$. Since $w_1,w_2$ will be in different connected components of $G'$, so must the endpoints of $e$ ($u,v$).

Suppose $e$ is not a bridge, then there is a path from $u$ to $v$ in $G'$. Adding back $e$ will create a cycle in $G$. Conversely suppose that $e$ is part of a cycle in $G$, then there is a path from $u$ to $v$ in $G'$ (by going around the cycle). Then $e$ must not be a bridge.

# Jordan curve theorem:

A simple closed curve in the plane divides it into two regions, one outside and one inside. This has a corollary where in a planar representation of a graph, an edge $e$ has both sides on the same face if and only if $e$ is a bridge.

