A [[Rings, subrings, and fields|ring]] $R$ which is commutative has at least two elements, and does not have any [[Rings, subrings, and fields#Fields|zero divisors]] other than $0$. This ring is then called an integral domain.

Let $R$ be an integral domain. Then the ring $R[x]_n=\{a_0+a_1x+\dots+a_nx^n:a_i\in R\}$ is also an integral domain. Let $f(x)\in R[x]_n,g(x)\in R[x]_m$, with $m\geq n$ then we have:$$\Huge f(x)+g(x)=(a_0+b_0)+(a_1+b_1)x+\dots+(a_n+b_n)x^n+\dots+b_mx^m$$$$\Huge f(x)g(x)=c_0+c_1x+\dots+c_nx^{m+n}$$Where:$$\Huge c_k=\sum_{j=0}^ka_kb_{k-j}$$So we have that $R[x]$ is a commutative ring.


# Units:

Let $R$ be a ring. An element $a\in R$ is called a unit in $R$ if there exists $b\in R$ such that $a\cdot b=b\cdot a=1$ and $b$ is unique. We can then write $b=a^{-1}$ as the multiplicative inverse of $a$. The set of units in $R$ is denoted as $R^X$. Note that for any $R$ we have $1\in R$ since $1\cdot 1=1$.

We claim that $(R^X,\cdot)$ is a group. $R^X$ is closed with respect to multiplication since for $a,c\in R^X$ then $a\cdot c\in R$. This is because $(a\cdot c)\cdot(c^{-1}\cdot a^{-1})=a\cdot(c\cdot c^{-1})\cdot a^{-1}=a\cdot 1\cdot a^{-1}=a\cdot a^{-1}=1$. For every $a\in R^X$, we have that $a^{-1}\in R^X$. Associativity comes from associativity of multiplication on $R$.

## Examples:
>If $F$ is a [[Rings, subrings, and fields#Fields|field]], every non-zero element of $F$ has a multiplicative inverse. Therefore:$$\Huge F^X=F\setminus\{0\}$$Consider the units of $\mathbb{Z}$. In order for $a,b\in \mathbb{Z}$ to satisfy $a\cdot b=1$ we must have $a=b=1$ or $a=b=-1$. Therefore we conclude:$$\Huge \mathbb{Z}^X=\{\pm 1\}$$Consider a field $F$ and define $R=F[x]$. To find the units of $R$ we need $f(x),g(x)\in F[x]$ to satisfy $f(x)\cdot g(x)=1$. This implies $\deg(f)=\deg(g)=0$ so we must have $f(x)=a_0$ and $g(x)=b_0$ such that $a_0\cdot b_0=1$ and $a_0,b_0\in F$. Therefore we can say:$$\Huge R^X=F^X$$Consider $R=M_n(\Re)$, we require a multiplicative inverse so the answer is trivial:$$\Huge R^X=\{A\in M_n()\}$$