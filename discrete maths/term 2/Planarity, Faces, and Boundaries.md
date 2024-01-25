
# Bipartite:

Given a [[Graph definitions|graph]] $G(V,E)$, where there exists subsets $V_1,V_2\subset V$ such that $V_1\cup V_2=V$ and $V_1\cap V_2=\emptyset$ and every edge is of form $uv$ where $u\in V_1,v\in V_2$, that is every edge connects a node in $V_1$ to a node in $V_2$, then $G$ is said to be bipartite.

If a bipartite graph is simple and if for the partition $V_1,V_2$ is such that $u\in V_1,v\in V_2\implies uv\in E$ then $G$ is the complete bipartite graph where $|V_1|=m,|V_2|=n$ and $G$ is denoted as $K_{m,n}$. This graph has $mn$ edges.

# Planarity:

A graph is planar if it can be drawn with no edges crossing. Such a drawing is a planar representation of $G$.

# Faces and Boundaries:

A planar representation of a graph $G$ divides the plane into a set of faces $F$. The boundary of a face $f$, denoted by $B(f)$ is the set of edges that contain the face. The length of $B(f)$ is the smallest length of closed [[Graph definitions#Walk|walks]] in $G$ that cover $B(f)$ denoted as $b(f)$. For a disconnected graph, $b(f)$ is defined as the smallest sum of closed walks in $G$ that cover $B(f)$:![[faces example]]In the plane, every edge has two sides but both can be bound by the same face (i.e. $f_4$ binds $de$ and $ed$). Note that for every finite planar graph, there is one infinite face (i.e. $f_4$).

10.2