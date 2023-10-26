
# Reliability networks:

A reliability network is a diagram of nodes and arcs. Each node represents a component of a multi component system. Each node is either working or not. The entire system works if it is possible to traverse the system while only passing through working nodes. Probability has applications here, with each node having a related [[Probability definition|probability]] if it is working or not.

Suppose that the $i$th component functions with a probability $p_i,i\in\{1,2,\dots,k\}$ and different components are independent. The probability that a system overall works is equivalent to $p_1p_2\dots p_k$. This function is denoted as $r(p_1,p_2,\dots,p_k)$, known as the reliability function. This is determined by the layout of the probability network.

Consider $W_i$ to be the event that component $i$ works, and $S$ to be the event that the entire system works. $S$ needs to be represented in terms of $W_i$ for $\mathbb{P}(S)$ to be calculated. For a system with components in series:
$$\Huge S=\bigcap_{i=1}^kW_k$$
![[series reliability]]
For components in parallel:$$\Huge S=\bigcup_{i=1}^kW_k$$![[parallel reliability]]
# Genetics:

Inherited characteristics are determined by genes, the mechanisms governing inheritance are random, so the laws of probability are often used. Genotypes of siblings are dependant if not conditional on the genotypes of parents:
![[Applications of probability .excalidraw]]