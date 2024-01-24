
# Bipartite:

Given a [[Graph definitions|graph]] $G(V,E)$, where there exists subsets $V_1,V_2\subset V$ such that $V_1\cup V_2=V$ and $V_1\cap V_2=\emptyset$ and every edge is of form $uv$ where $u\in V_1,v\in V_2$, that is every edge connects a node in $V_1$ to a node in $V_2$, then $G$ is said to be bipartite.

If a bipartite graph is simple and if for the partition $V_1,V_2$ is such that $u\in V_1,v\in V_2\implies uv\in E$ then $G$ is the complete bipartite graph where $|V_1|=m,|V_2|=n$ and $G$ is denoted as $K_{m,n}$. This graph has $mn$ edges.

# Planarity:

A graph is planar if it can be drawn with no edges crossing. Such a drawing is a planar representation of $G$.
