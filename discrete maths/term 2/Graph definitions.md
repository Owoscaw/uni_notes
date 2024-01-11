Informally, a graph consists of a set of vertices, joined by edges. A finite undirected graph is a triple $(V,E,\Phi)$ where $V$ and $E$ are finite sets and $\Phi:E\mapsto V$. $\Phi$ is the incidence function. An edge $e$ is incident to a vertex $v\in V$ if $v\in\Phi(e)$. The two vertices on the edge are the endpoints of the edge. For example, the edge $ab$ is defined as $\Phi(ab)=\{a,b\}$. When the map $\Phi$ is [[Functions, Domain and Range#Injectivity|injective]], the associated graph is called simple. Simple graphs can still be defined by the pair $(E,V)$ where $E\subset V$ and the incidence function is replaced instead by the adjacency relation.

Two vertices, $u,v\in V$ are said to be adjacent in the graph $G=(E,V)$ if $\{u,v\}\in E$. The graph $G=(E,V,\Phi)$ with $V=\{v_1,\dots,v_n\}$ and $E=\{e_1,\dots,e_m\}$ using the incidence [[Matrix definition|matrix]] $(B(i,j), i\leq n, j\leq m)$ where:$$\Huge B(i,j)=\begin{cases}1&\text{if }v_i\in\Phi(e_j)\\0&\text{otherwise}\end{cases}$$Similarly, simple graphs can be represented using the adjacency matrix $(A(i,j),i,j\leq n)$ where:$$\Huge A(i,j)=\begin{cases}1&\text{if }v_iv_j\in E\\0&\text{otherwise}\end{cases}$$

Given a graph $G=(E,V,\Phi)$, the degree of a vertex $v\in V$ denoted by $d_G(v)$ counts the number of times that a vertex is an endpoint to an edge:$$\Huge d_G(v)=\sum_{e\in E}1\{v\in\Phi(e)\}=\sum_{e\in E}B(v,e)$$If a vertex has degree $1$, then it is known as a leaf.

# Standard Graphs:

## Null:
The null graph $G=(V,E)$ on $m$ vertices is denoted as $N_m$ has $|V|=m$ but $|E|=0$, not very interesting.

## Complete:
The complete graph on $m$ vertices is denoted as $K_m=(V_m,E_m)$. If $|V_m|=m$, then $|E_m|={m\choose 2}$. Every vertex is connected to every other vertex.

## Cycle:
The cycle graph on $m$ vertices is denoted as $C_m$. Given $|V|=m$, the cycle graph is constructed by the following: $V=\{v_1,\dots,v_m\}$, $E=\{v_1v_2,v_2v_3,\dots,v_{m-1}v_m,v_mv_1\}$.

## N-cube:
The $n$-cube is denoted as $Q_n$ and has vertices defined by $V=\{x:\{1,2,\dots,n\}\mapsto\{0,1\}\}=\{(x_i,i\in\{1,2,\dots,n\}):x_i\in\{0,1\}\}$ and $E_n=\{uv:\sum_{i=1}^n|u_i-v_i|=1\}$. Here $|V|=2\times2\times\dots\times2$ for a total of $n$ times, since each $x_i$ can be $0$ or $1$. So we have that $|V|=2^n$ and $|E|=n2^{n-1}$.

# Handshaking:

For any graph $G=(V,E)$, we have that: $$\Huge \sum_{v\in V}d_G(v)=2|E|$$ Using the $n$-cube as an example, for each $v\in V$, $d_{Q_n}(v)=n$, so summing gives $\sum_{v\in V}n=\sum_{i=1}^nn=n+n+\dots+n$ for a total of $2^n$ times. This makes the sum equal to $n2^n=2|E|$, so finally $|E|=n2^{n-1}$

# Isomorphism:

Given two simple graphs, $G_1=(V_1,E_1)$ and $G_2=(V_2,E_2)$, are isomorphic when there is a map $\psi:V_1\mapsto V_2$ such that $\psi$ is [[Functions, Domain and Range#Bijectivity|bijective]] (one to one) and $\{u,v\}\in E_1=\{\psi(u),\psi(v)\}\in E_2$. That is, $\psi$ is bijective and preserves adjacency of vertices. The following graphs are isomorphic:![[isomorphic graphs example]]
# Complements:

For a graph $G=(V,E)$, the complement of $G$ is the graph $\overline G=(V,F)$ where $E\cup F=\mathbb V$