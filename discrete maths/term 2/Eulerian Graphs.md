
# Connectedness: 

A [[Graph definitions#Standard Graphs|graph]] $G$ is connected if given any two vertices $u,v$, there is a [[Graph definitions#Path|path]] in $G$ from $u$ to $v$.

A connected component of $G=(V,E)$ is a [[Graph definitions#Subgraphs|subgraph]] $G_1=(V_1,E_1)$ such that the following are true:
> $G_1$ is connected.
> For every edge $e=uv\in E$ where $u,v\in V_1$, then $e\in E_1$.
> For any $u\in V_1$ and $w\in V\setminus V_1$ then there is no path in $G$ from $u$ to $w$

# Euler's Theorem:

An Euler circuit in a graph $G$ is a circuit in $G$ which uses each edge in $G$ exactly once. A graph that contains an Eul