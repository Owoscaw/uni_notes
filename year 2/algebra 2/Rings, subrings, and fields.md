Consider the integers, $\mathbb{Z}=\{0,\pm1,\pm2,...\}$. Addition, subtraction, and multiplication between any two integers always result in another integer. Consider the natural numbers, $\mathbb{N}=\{1,2,3,\dots\}$, addition and multiplication between any two natural numbers result in another natural number, however this does not hold for subtraction. Consider the rational numbers, $\mathbb{Q}=\{\frac{a}{b}:a,b\in\mathbb{Z},b\neq0\}$, all elementary operations on two numbers in this set result in another rational number.

This motivates the definition of a ring. A ring is a set of mathematical objects where addition, subtraction, and multiplication is possible between any two elements in the set, where the result is another element in the set. We see that $\mathbb{Z}$ and $\mathbb{Q}$ are both rings. If division is possible while remaining in the set, we call this a field. Therefore all fields are rings but not all rings are fields.

# Binary operations:

Let $R$ be a set, and write $R\times R=\{(a,b):a,b\in R\}$. Addition on $R$ is a map, $+:R\times R\mapsto R$ and $(a,b)\mapsto a+b$. Multiplication on $R$ is also a map, $\cdot:R\times R\mapsto R$ and $(a,b)\mapsto a\cdot b=ab$.

We can then define a ring. A ring $R$ is a set together with two binary operations, usually written as $+,\cdot$, such that:
> $+$ makes $R$ an [[Groups#Axioms|abelian]] group
> There exists an element $1\in R$ such that $1\cdot r=r\cdot r=r$ for all $r\in R$
> For every $x,y,z\in R$ we have that $(x\cdot y)\cdot z=x\cdot(y\cdot z)$
> For every $x,y,z\in R$ we have that $x\cdot(y+z)=x\cdot y+x\cdot z$ and $(y+z)\cdot x=y\cdot x+y\cdot z$

Note that if $x\cdot y=y\cdot x$ for every $x,y\in R$, the ring is called commutative. For example $\mathbb{Z}$ is a commutative ring with regular addition and multiplication, however $M_n(\mathbb{Q})$ is not a commutative ring for $n>1$. 

Let $V$ be a complex [[Vector space definitions|vector space]] of dimension $n$. We define:$$\Huge End(V)=\{f:V\mapsto V:\text{f is a linear map}\}$$ To make this a ring, we need to define $+,\cdot$. Let $f,g\in End(V)$. Consider a definition for $(f+g)(v)$:$$\Huge (f+g)(v):=f(v)+g(v)\,\,\forall v\in V$$And consider the following definition for $\cdot$:$$\Huge (f\circ g)(v):=f(g(v))\,\forall v\in V$$These can be proven to be linear maps by observing $f(0)$, addition, and scalar multiplication. Therefore we say that $(End(V),+,\circ)$ is a ring.

# Equivalence relation on a set:

A binary relation on the set $S$ is a subset of $S\times S$. We write $a\sim b$ if $(a,b)\in B$. This binary relation is called an equivalence relation on $S$ if:
> $a\sim a$ (reflexivity)
> $a\sim b\iff b\sim a$ (symettry)
> If $a\sim b$ and $b\sim c$ then $a\sim c$ (transitivity)

The equivalence class of $a\in S$ under $\sim$, denoted by $[a]$ is defined as:$$\Huge [a]=\{x\in S:x\sim a\}$$x 