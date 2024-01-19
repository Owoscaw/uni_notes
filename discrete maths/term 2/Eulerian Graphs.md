	
# Connectedness: 

A [[Graph definitions#Standard Graphs|graph]] $G$ is connected if given any two vertices $u,v$, there is a [[Graph definitions#Path|path]] in $G$ from $u$ to $v$.

A connected component of $G=(V,E)$ is a [[Graph definitions#Subgraphs|subgraph]] $G_1=(V_1,E_1)$ such that the following are true:
> $G_1$ is connected.
> For every edge $e=uv\in E$ where $u,v\in V_1$, then $e\in E_1$.
> For any $u\in V_1$ and $w\in V\setminus V_1$ then there is no path in $G$ from $u$ to $w$

# Euler's Theorem:

An Euler circuit in a graph $G$ is a circuit in $G$ which uses each edge in $G$ exactly once. A graph that contains an Eulerian circuit is known as an Eulerian graph. Euler's theorem states that for a finite connected graph $G=(V,E)$ with $|V|>1$ then $G$ has an Euler circuit if and only if the degree of all vertices in $G$ is even. It is trivial to prove the $\implies$ direction, so we focus on $\Longleftarrow$:

First we need a lemma. If a graph, $G=(V,E)$, is finite and connected with $|V|>1$ and all vertices of even degree, then $G$ is a finite union of edge-disjoint cycles. That is there exist cycles $C_1,C_2,\dots,C_n$ such that the union of vertices in these cycles is equal to $V$ and the union of edges equal to $E$. Since $G$ is connected, it has no isolated vertices. Therefore all vertices have degree of at least $2$, and there must exist a cycle $C_1$ in $G$. A new graph is formed by removing all edges in $C_1$. Every vertex in $C_1$ will have their degree decreased by $2$ as a result, so remove any now isolated vertices from $G$. This remaining graph will have vertices with even degree all greater than $2$. Therefore we can now repeat this process on the new graph. All degrees will eventually decrease to $0$ under this process, so every vertex belongs to a cycle and can therefore be decomposed into a union of disjoint cycles as required.

Now we can prove $\Longleftarrow$. Assuming $G$ is a finite, connected graph with vertices that are all of even degree. Then by the above lemma, $G$ is a finite union of $n$ disjoint cycles. We show by induction that these can be combined into a single Euler circuit:![[Eulerian Graphs .excalidraw]]