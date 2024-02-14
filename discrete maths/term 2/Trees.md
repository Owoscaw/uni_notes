
A tree is a [[Eulerian Graphs#Connectedness|connected]] acyclic graph, that is a connected graph with no cycles present. A forest is any acyclic graph, note that every connected component of a forest is itself a tree. A leaf of a graph is a vertex of degree one. We try drawing all trees of $n$ vertices:![[size n trees]]

| n               | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
| Number of Trees | 1   | 1   | 1   | 2   | 3   | 6   | 11  |


# Counting trees:

A labelled tree on $n$ vertices is a tree where every vertex on the tree is assigned a unique integer from $1,\dots,n$, labelled trees for $n=2,3,4$:![[labelled trees]]$n=5$ was calculated by finding the number of ways to label the 3 types of trees with $5$ vertices seen above.

## Trees to sequences:
Given a tree $T$ with vertices labelled $1,2,\dots,n$ for $n\geq3$, construct a sequence of labels by repeatedly cutting of leaves as follows:
> Find the leaf $l$ with smallest label, it will be connected to a unique vertex $p$ which we record.
> Delete the vertex $l$ and it's incident edge $l_p$ from $T$.
> If there is more than one edge left, repeat.

This will compute a sequence $\mathcal P(T)=(p_1,p_2,\dots,p_{n-2})$ called the Prufer code of the tree. This is a sequence of $n-2$ elements with repetitions allowed:![[Prufer code examples]]Notice that the leaves of $T$ are the vertices that don't occur in $\mathcal P(T)$, more generally if the label $i$ appears $m_i$ times in $\mathcal P(T)$, then vertex $i$ has degree $d_T(i)=m_i+1$. This is because a vertex that is not a leaf will appear the amount of times equal to the number of leaves it has, this is equivalent to $m_i$, then it must connect to the rest of the tree so its total degree becomes $m_i+1$:
> Only star trees will have a Prufer code with only one value
> Only trees where two vertices have leaves will have a Prufer code with exactly two values
> A path will have Prufer code with all distinct values

## Sequences to trees:
Given a sequence $P=(p_1,p_2,\dots,p_{n-2})$ of elements $L=\{1,\dots,n\}$, construct a tree as follows:
> Find the least number $l\in L$ not in $P$ and create an edge between $l$ and the first element in $P$
> Remove $l$ from $L$ and the first element in $P$
> If $P$ is not empty then repeat, if it is empty then $L$ only has two numbers left, create an edge between these two vertices

![[Prufer trees example]]

# Cayley's formula:

So we have a bijection between Prufer codes and labelled trees. Then the number of Prufer codes of length $n-2$ is equal to the number of labelled trees of size $n$. There are $n-2$ positions to fill for any Prufer code, and $n$ choices for each position, so the total number of possible Prufer codes, and therefore the total number of labelled trees of size $n$ is given by:$$\Huge \text{There are }n^{n-2}\text{ distinct labelled trees with }n\text{ vertices}$$This is convincing, however not rigorous as there are two doubts:
> How do we know that the sequences to trees algorithm indeed produces a tree?
> How can we be sure that the two algorithms are truly inverses to each other

We (try) prove this using linear algebra:![[Cayley proof]]
# MSTs:

A weighted graph is a graph where each edge $e$ has an associated non-negative number $w(e)$, the weight of $e$. A useful way of encoding this information for a simple graph is with a weight matrix:![[wieghted graph]]Where $\infty$ is used to represent the lack of an edge. A spanning tree is a subgraph that is a tree, which uses the same vertex set as the original graph. A minimum spanning tree is a spanning tree of minimum total edge length, this obviously has many real world applications. We try to minimise $w(T)$, the weight of all spanning trees $T\subset G$.

For a graph to have a spanning tree, there must be a way to connect every edge to a tree, so it is obvious to require that a graph must be connected to have a spanning tree. Suppose that a connected graph contains a cycle, then it is not a tree. Any edge from this cycle can be removed without disconnecting the graph, since there exists a path around the other direction of the cycle. Repeat this for every cycle in a graph to show that there exists a spanning tree for every connected graph. Note if the graph never contained any cycles then it was already its own spanning tree.

# Prim's algorithm:

Suppose a connected graph $G$ has $n$ vertices and select a vertex. This itself is a tree composed of a single vertex and no edges, call this $T_1$:
> Suppose a tree $T_k$ with $k<n$ has been constructed
> Find a least weight edge connecting $T_k$ to a new vertex in $G$, add this new edge and vertex to construct $T_{k+1}$
> Repeat until all vertices in $G$ are included in $T_k$

This process must create a spanning tree since an edge will be added to the tree only if one of the vertices was not already in the tree, so it is impossible to create a cycle as this algorithm will not add an edge between two vertices already in the tree. Since this algorithm only terminates when all vertices in $G$ are in the tree, it must be spanning.

Suppose that the output tree $T$ is not minimal, and $T'$ be a minimal spanning tree. That is $w(T)>w(T')$, therefore there must exist some edge $e$ in $T$ that is not in $T'$. This is because $T$ either has more edges than $T'$ or the algorithm chose a larger edge to use in $T$, as these are the only ways to satisfy $w(T)>w(T')$. Let $V$ be the set of vertices used in the algorithm before adding $e$. There must be an edge $f$ in $T'$ that connects a vertex in $V$ to a vertex not in $V$, let $T''=T'-f+e$, the graph obtained by replacing $f$ with $e$ in $T'$. $T''$ is also a minimum spanning tree since no vertices are removed and $w(e)\leq w(f)$ since $T'$ is an MST. Then $w(T'')=w(T')-w(f)+w(e)\leq w(T')$, so $w(T'')=w(T')$ and both are minimum spanning trees. We have $T'$ is minimal $\implies$ $T''$ is minimal. Repeating this until $V$ contains every vertex in $G$ shows that eventually, $w(T)\leq\dots\leq w(T'')\leq w(T')$, therefore $T$ is a minimum spanning tree.

# Kruskal's algorithm:

Given a connected graph $G$, construct a sequence of subgraphs by repeating the following:
> Add in the least weight edge that does not cause a cycle

This will eventually produce a spanning tree, since this algorithm preserves acyclicity and only terminates when it cannot add another edge without creating a cycle. This must mean that the graph is connected. We have that Kruskal's algorithm produces a connected graph that preserves acyclicity, so it must produce a tree. This tree must be spanning since the original graph $G$ was connected, so there are always enough edges to add that will not cause a cycle.

Suppose that the tree produced from Kruskal's algorithm, $T$, is not optimal, whereas $T'$ is. In order for this to be true, we require $w(T)> w(T')$. Since both are spanning, there must be an edge $e$ in $T$ that is not in $T'$ that causes the above inequality to hold. Consider the set of edges at stage $k$ in the algorithm, $E_k$. If we say $E=\{e_1,e_2,\dots,e_k\}$, then it is true that $w(e_1)\leq w(e_2)\leq\dots\leq w(e_k)$ since the only minimal acyclicity preserving edges are considered. It is also true that $w(E_k)\leq w(T)$, with equality when $k$ is the final stage of the algorithm. Since $e$ was not added by the algorithm, it is also true that $w(e)>w(e_k)$ for any stage $k$.