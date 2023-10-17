
# Arrangements:

An arrangement is a finite sequence of items in which the order of the items is important. The length of the arrangement is the number of elements contained within in. Repeated elements are allowed in an arrangement. 

## Standard problem 1:

The amount of lists of length $k$ that can be made from a set $S$, where $|S|=n$ is a standard problem. Each arrangement corresponds to a $k$-tuple in the cartesian product $S^k$. $|S^k|$ is a standard result, equivalent to $n^k$:
$$\Huge |S^k|=|S|^k=(n)^k=n^k$$

## Standard problem 2:

The amount of lists of length $k$ that can be make from a set $S$, where $|S|=n$ where repetitions are not allowed is another standard problem. Given $n\geq k$, there are $n$ choices for the first item, $n-1$ for the second, and $n-k+1$ for the last, so there are $n(n+2)\dots(n-k+1)$ arrangements:
$$\Huge n\times(n+1)\times\dots\times(n-k+1)=(n)_k=\frac{n!}{(n-k)!}$$

Both standard problems 1 and 2 make use of the [[Counting principles#Multiplication principle|multiplication principle]].


# Permutations:

A permutation is an arrangement of length $|S|$, where each element in a finite set $S$ is used exactly once. If $|S|=n$, the number of permutations of $S$ is given by using standard problem 2, where $n=k$, as we are using every element from $S$:
$$\Huge \frac{n!}{(n-n)!}=\frac{n!}{0!}=n!$$

This concept is generalised for $r>0$, an $r$-permutation on the set $S$ is an arrangement of $r$ distinct elements from $S$. $P(n,r)$ is written to represent the number of $r$-permutations on a set of size $n$. We have:$$\Huge P(n,r)=n\times(n-1)\times(n-r+1)=\frac{n!}{(n-r)!}=(n)_r$$
$P(n,r)=0$ for any $r>n$, as there are no permutations on $S$ of size $r$ as there are less than $r$ elements in $S$.