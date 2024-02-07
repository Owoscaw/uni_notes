
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

This will compute a sequence $\mathcal P(T)=(p_1,p_2,\dots,p_{n-2})$ called the Prufer code of the tree. This is a sequence of $n-2$ elements with repetitions allowed:![[Trees .excalidraw]]