
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

A permutations is an arrangement of length $|S|$, where each element in a finite set $S$ is used exactly once.