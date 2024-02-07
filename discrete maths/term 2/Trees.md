
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

![[Prufer trees example]]So we have a bijection between Prufer codes and labelled trees. Then the number of Prufer codes of size $n$ is equal to the number of labelled trees of size $n$:![[Trees .excalidraw]]