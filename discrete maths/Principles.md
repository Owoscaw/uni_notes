
# The inclusion-exclusion principle:

The size of the repeated union between [[Set theory definitions#Union|sets]] $A_1,A_2,\dots,A_n$ is trivial if they are pairwise disjoint, that is $A_i\cap A_j=\emptyset$ for any $i\neq j,\,1\leq i,j\leq n$:
$$\Huge \left|\bigcup_{i=1}^nA_i\right|=\sum_{i=1}^n|A_i|$$
However if they are not pairwise disjoint, it gets more complicated. A typical $k-$fold intersection for $1\leq k\leq n$ of a selection of this sets can be written as:$$\Huge A_{i1}\cap A_{i2}\dots\cap A_{ik}$$
Where $1\leq i_1<i_2<\dots<i_k\leq n$. Now let:$$\Huge S_k=\sum_{i_1<i_2<\dots<i_k}|A_{i1}\cap A_{i2}\cap\dots\cap A_{ik}|$$
Here, $S_k$ is the sum of the sizes of all possible $k-$fold intersections, that is $S_k$ is the sum of the sizes of all possible ways of taking the intersection between $k$ sets, from a total of $n$ sets. Now for a positive integer $n$ and finite sets $A_1,\dots,A_n$:$$\Huge |A_1\cup\dots\cup A_n|=S_1-S_2+S_3+\dots+(-1)^{n+1}S_n=\sum_{k=1}^n(-1)^{k+1}S_k$$$$\Huge\left|\bigcup_{i=1}^nA_i\right|=\sum_{k=1}^n(-1)^{k+1}S_k$$
Example:
![[inclusion exclusion example]]

## Derangements:

A [[Arrangements and Permutations#Permutations|permutation]] is called a derangement if no elements end up in the required position