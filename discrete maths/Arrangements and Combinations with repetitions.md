
# Arrangements with repetitions:

Given a list of $n$ objects of $r$ different types, in which objects of type $i$ occur $n_i$ times ($n_1+n_2+\dots+n_r=n$), the number of [[Arrangements and Permutations#Arrangements|arrangements]] of the list is:
$$\Huge P(n,n_1,n_2,\dots,n_r)=\frac{n!}{n_1!n_2!\dots n_r!}$$

# Combinations with repetitions:

A [[Combinations|combination]] from a set of objects is an unordered selection of elements in that set. We will consider combinations with repetitions. The number of $k$ combinations from a set of $n$ objects where objects can be chosen more than once is found by considering the following problem:

How many $k$ combinations with repetitions from $n$ objects are there in which each object is chosen at least once in the combination. This question only has a non-zero answer if $k\geq n$, as each element of $n$ needs to be used at least once:
![[combinations with repetitions]]
So the number of $k$ combinations with repetitions taken from a set with $n$ objects, where there is at least one of each element from the set in each combination is given by:$$\Huge {n-1\choose k-1}$$
To change a problem of the first type into the second type, one of each object from $n$ can be added to the combination, then taken away at the end. So the answer to the first question is given by:$$\Huge {k+n-1\choose n-1}={k+n-1\choose k}$$

# Extended binomial coefficients:

For integers $n,k$ with $0\leq k\leq n$, ${n \choose k}$ is the coefficient of $x^k$ in $(1+x)^n$. The definition can be extended to the reals, defining ${\alpha \choose k}$ to be the coefficient of $x^k$ in $(a+x)^\alpha$ as a power series around $x=0$, that is:$$\Huge (1+x)^\alpha=\sum_{k=0}^\infty {\alpha \choose k}x^k$$
Maclaurin's theorem dictates that for $\alpha\in\Re$ and integer $k\geq 0$:$$\Huge {\alpha \choose k}=\frac{\alpha(\alpha-1)\dots(\alpha-k+1)}{k!}$$
This is equivalent to "$\alpha$ choose $k$" if $\alpha$ is an integer. If $\alpha$ is a positive integer less than $k$, then the numerator will contain a zero, so the expression is 0 and $(1+x)^\alpha$ is a finite expansion. If $\alpha$ is not an integer then the numerator will not contain a zero, so $(1+x)^\alpha$ is an infinite expansion. Note that:
$$\Huge {-n\choose k}=\$$