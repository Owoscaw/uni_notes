Consider the integers, $\mathbb{Z}=\{0,\pm1,\pm2,...\}$. Addition, subtraction, and multiplication between any two integers always result in another integer. Consider the natural numbers, $\mathbb{N}=\{1,2,3,\dots\}$, addition and multiplication between any two natural numbers result in another natural number, however this does not hold for subtraction. Consider the rational numbers, $\mathbb{Q}=\{\frac{a}{b}:a,b\in\mathbb{Z},b\neq0\}$, all elementary operations on two numbers in this set result in another rational number.

This motivates the definition of a ring. A ring is a set of mathematical objects where addition, subtraction, and multiplication is possible between any two elements in the set, where the result is another element in the set. We see that $\mathbb{Z}$ and $\mathbb{Q}$ are both rings. If division is possible while remaining in the set, we call this a field. Therefore all fields are rings but not all rings are fields.

# Binary operations:

Let $R$ be a set, and write $R\times R=\{(a,b):a,b\in R\}$. Addition on $R$ is a map, $+:R\times R\mapsto R$ and $(a,b)\mapsto a+b$. Multiplication on $R$ is also a map, $\cdot:R\times R\mapsto R$ and $(a,b)\mapsto a\cdot b=ab$.

We can then define a ring. A ring $R$ is a set together with two binary operations, usually written as $+,\cdot$, such that:
> $+$ makes $R$ an [[Groups#Axioms|abelian]] group
> There exists an element $1\in R$ such that $1\cdot r=r\cdot r=r$ for all $r\in R$
> For every $x,y,z\in R$ we have that $(x\cdot y)\cdot z=x\cdot(y\cdot z)$
> For every $x,y,z\in R$ we have that $x\cdot(y+z)=x\cdot y+x\cdot z$ and $(y+z)\cdot x=y\cdot x+y\cdot z$
