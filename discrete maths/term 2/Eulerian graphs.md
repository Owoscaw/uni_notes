
## Walk:
Given a [[Graph definitions#Standard Graphs|graph]] $G=(V,E,\phi)$, a walk in $G$ is a sequence of vertices $v_1,v_2,\dots,v_k\in V$ together with edges $e_1,e_2,\dots,e_{k-1}\in E$ such that $\phi(e_i)=\{v_i,v_{i+1}\}$ for all $1\leq i\leq k-1$. This can sometimes be written as $\gamma=v_1e_1v_2e_2\dots v_{k=1}e_{k-1}v_k$. The length of this walk will be the number of edges it contains, $k-1$. A walk is closed if $v_1=v_k$. Neither edges nor vertices are required to be distinct.

## Trail:
A trail is a walk with no edges repeated, and a circuit is a closed trail ($v_1=v_k$ with $k\geq 2$).

## Path:
A path is a trail such that all vertices are distinct, and a cycle is a closed path.

## Hamiltonian cycle:
A Hamilt