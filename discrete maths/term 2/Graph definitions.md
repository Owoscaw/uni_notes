Informally, a graph consists of a set of vertices, joined by edges. A finite undirected graph is a triple $(V,E,\Phi)$ where $V$ and $E$ are finite sets and $\Phi:E\mapsto V$. $\Phi$ is the incidence function. An edge $e$ is incident to a vertex $v\in V$ if $v\in\Phi(e)$. The two vertices on the edge are the endpoints of the edge. For example, the edge $ab$ is defined as $\Phi(ab)=\{a,b\}$. When the map $\Phi$ is [[Functions, Domain and Range#Injectivity|injective]], the associated graph is called simple. Simple graphs can still be defined by the pair $(E,V)$ where $E\subset V$ and the incidence function is replaced instead by the adjacency relation.

Two vertices, $u,v\in V$ are said to be adjacent in the graph $G=(E,V)$ if $\{u,v\}\in E$. The graph $G=(E,V,\Phi)$ with $V=\{v_1,\dots,v_n\}$ and $E=\{e_1,\dots,e_m\}$ using the incidence [[Matrix definition|matrix]] $(B(i,j), i\leq n, j\leq m)$ where:$$\Huge B(i,j)=\begin{cases}1&\text{if }v_i\in\Phi(e_j)\\0&\text{otherwise}\end{cases}$$Similarly, simple graphs can be represented using the adjacency matrix $(A(i,j),i,j\leq n)$ where:$$\Huge A(i,j)=\begin{cases}1&\text{if }v_iv_j\in E\\0&\text{otherwise}\end{cases}$$

Given a graph $G=(E,V,\Phi)$, the degree of a vertex $v\in V$ denoted by $d_G(v)$ counts the number of times that a vertex is an endpoint to an edge:$$\Huge d_G(v)=\sum_{e\in E}1\{v\in\Phi(e)\}=\sum_{e\in E}B(v,e)$$If a vertex has degree $1$, then it is known as a leaf.

# Standard Graphs:

The null graph $G=(V,E)$ on $m$ vertices is denoted as $N_m$ has $|V|=m$ but $|E|=0$, not very interesting.

The complete graph on $m$ vertices is denoted as $K_m=(V_m,E_m)$. If $|V_m|=m$, then $|E_m|={m\choose 2}$. Every vertex is connected to every other vertex.

The cycle graph on $m$ vertices is denoted as $C_m$