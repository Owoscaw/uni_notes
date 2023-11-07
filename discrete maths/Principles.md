
# The inclusion-exclusion principle:

The size of the repeated union between [[Set theory definitions#Union|sets]] $A_1,A_2,\dots,A_n$ is trivial if they are pairwise disjoint, that is $A_i\cap A_j=\emptyset$ for any $i\neq j,\,1\leq i,j\leq n$:
$$\Huge \left|\bigcup_{i=1}^nA_i\right|=\sum_{i=1}^n|A_i|$$
However if they are not pairwise disjoint, it gets more complicated. A typical $k-$fold intersection for $1\leq k\leq n$ of a selection of this sets can be written as:$$\Huge A_{i1}\cap A_{i2}\dots\cap A_{ik}$$
Where $1\leq i_1<i_2<\dots<i_k\leq n$. Now let:$$\Huge S_k=\sum_{i_1<i_2<\dots<i_k}|A_{i1}\cap A_{i2}\cap\dots\cap A_{ik}|$$
Here, $S_k$ is the sum of the sizes of all possible $k-$fold intersections, that is $S_k$ is the sum of the sizes of all possible ways of taking the intersection between $k$ sets, from a total of $n$ sets. Now for a positive integer $n$ and finite sets $A_1,\dots,A_n$:$$\Huge |A_1\cup\dots\cup A_n|=S_1-S_2+S_3+\dots+(-1)^{n+1}S_n=\sum_{k=1}^n(-1)^{k+1}S_k$$$$\Huge\left|\bigcup_{i=1}^nA_i\right|=\sum_{k=1}^n(-1)^{k+1}S_k$$
Example:
![[inclusion exclusion example]]

## Derangements:

A [[Arrangements and Permutations#Permutations|permutation]] is called a derangement if no elements end up in the required position, that is for every $k$, the number $k$ is not in the $k$th place. Let $A_i$ be the permutations where $i$ is in the correct position. $|A_i|=(n-1)!$, since after placing $i$ in position $i$, there are a following $n-1$ numbers to be arranged in any order. $A_i\cap A_j,i\neq j$ consists of permutations on $n$ with both $i$ and $j$ in fixed positions. $|A_i\cap A_j|=(n-2)!$, as two position have been fixed. In general:$$\Huge \left|\bigcap_{i=1}^kA_i\right|=(n-k)!$$
As $k$ positions have been fixed, allowing for a further $(n-k)!$ choices. There are ${n\choose k}$ ways of selecting $i_1<i_2<\dots<i_k$, so:
$$\Huge S_k=\sum_{i_1<i_2<\dots<i_k}\left|\bigcap_{i=1}^kA_i\right|={n\choose k}(n-k)!=\frac{n!}{k!}$$
Then the inclusion-exclusion formula dictates that the number of non-derangements are:$$\Huge\left|\bigcup_{i=1}^nA_n\right|=\sum_{k=1}^n(-1)^{k+1}\frac{n!}{k!}$$
So the number of derangements of $1,2,\dots,n$ is given by:
$$\Huge d(n)=n!-\Huge\left|\bigcup_{i=1}^nA_n\right|=n!\sum_{k=1}^n(-1)^{k+1}\frac{n!}{k!}=n!\left(1+\sum_{k=1}^n(-1)^{k}\frac{1}{k!}\right)$$$$\Huge \implies d(n)=n!\sum_{k=0}^n(-1)^{k}\frac{1}{k!}=\sum_{k=0}^n(-1)^{k}\frac{n!}{k!}$$
Note that the proportion of derangements to the total number of arrangements is given by:$$\Huge \frac{d(n)}{n!}=\sum_{k=0}^n(-1)^k\frac{1}{k!}$$
This is equivalent to the series expansion of $e^{-1}$:$$\Huge \lim_{n\to\infty}\frac{d(n)}{n!}=\frac{1}{e}$$


# Mathematical induction:

[[Proof techniques#Mathematical induction|Mathematical induction]] provides a method to determine the truth of a sequence of statements, each associated with a non-negative integer. The general form is as follows:
> Suppose each integer $n\geq n_0$ has an associated statement $P(n)$.
> Show $P(n_0)$ is true
> For any $n\geq n_0$, $P(n)\implies P(n+1)$

Assuming $P(n_0)$ is true, and that $P(n)\implies P(n+1)$, then $P(n_0+1)$ is true, so is $P(n_0+2)$. This chain continues for any $n\geq n_0$