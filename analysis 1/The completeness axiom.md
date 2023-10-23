
Let $X\subset \Re$. We say $X$ is bounded above if there exists $C\in\Re$ with $x\leq C$ for all $x\in X$. Here, $C$ is an upper bound for $X$, note that $C+1$ is also an upper bound for $X$. $X$ is bounded below is there exists a set $c\in\Re$ with $x\geq c$ for all $x\in X$. Here, $c$ is a lower bound for $X$. The set $X$ is bounded if it is both bounded above and below.

For example, take $X=\mathbb{N}$. $1$ is a lower bound for $\mathbb{N}$ as $1\leq n$ for all $n\in\mathbb{N}$. An upper bound for $\mathbb{N}$ would be a number $C$ such that $n\leq C$ for all $n\in \mathbb{N}$. The existence of such $C$ cannot be ruled out.

Let $X\subset\Re$, an element $M\in X$ is called the maximum of $X$ if $x\leq M$ for all $x\in X$. If such $M$ exists, then we write $M=\text{max}\,X$. Similarly, an element $m\in X$ is called the minimum of $X$ if $x\geq m$ for all $x\in X$. If such $m$ exists, then we write $m=\text{min}\,X$.

Let $X\subset\Re$ be bounded from above. A number $C\in\Re$ is called the supremum ($sup\,X$) of $X$, or least upper bound if:
> $C$ is an upper bound of $X$.
> Whenever $B\in\Re$ is an upper bound of $X$, then $C\leq B$.

Similarly, a number $c\in\Re$ is called the infimum ($inf\,X$) of $X$, or greatest lower bound if:
> $c$ is a lower bound of $X$.
> Whenever $b\in\Re$ is a lower bound of $X$, then $c\geq b$.

If $X$ has a maximum, then this maximum must be the supremum of $X$. Let $X$ be a set and $M\in X$ be the maximum of $X$, then $sup\,X=M$. By definition, $M$ is an upper bound. If $B\in\Re$ is another upper bound of $X$, then we require $M\leq B$. This is the case as $B\geq x,\,\forall x\in X$.

Example:
![[infimum example]]

# The axiom:

Every non-empty subset of $\Re$ which is bounded above has a supremum. 

Let $a,b\in\Re$ with $b>0$, then there exists a natural number $n$ with $nb>a$. Assume that this is not the case, then $X=\{nb\in\Re:n\in\mathbb{N}\}$ is bounded above. By the completeness axiom, $sup\,X=C\in\Re$ exists. So $nb\leq C$. Also $C-b<C$, so $C-b$ must not be an upper bound of $X$. So $\exists n\in\mathbb{N}$ such that $nb>C-b\iff(n+1)b>C$. Note that $(n+1)\in\mathbb{N}$, so $(n+1)b\in X$, so $C$ cannot be an upper bound. Here, assuming the opposite of this axiom leads to a contradiction so it must then be true.

Taking $b=1$, this says for any real number $a$, there is a natural number $n\in\mathbb{N}$ with $n>a$. Therefore the natural numbers cannot be bounded above. Therefore, using the example above:![[infimum resolved]]
Another example:![[The completeness axiom .excalidraw]]This relies on the following:

