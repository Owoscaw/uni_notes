
Let $R$ be a [[Rings, subrings, and fields|commutative ring]]. Let $a,b\in R$. We say that $a$ divides $b$ in $R$ and write $a|b$ if there exists $r\in R$ such that $b=r\cdot a$. An element $d\in R$ is called a greatest common divisor of $a$ and $b$ if the following hold:
> $d|a$ and $d|b$
> If $e\in R$ divides both $a,b$, then $e|d$

Note that according to the definition above, both $-1$ and $1$ are a $\gcd(2,3)$ with $R=\mathbb{Z}$, however since $\mathbb{Z}$ has an ordering, we can define the greatest common divisor as $1$. We must also define:$$\Huge \gcd(0,0):=0$$Note that $\gcd(a,b)$ does not exist for every $a,b$ in every ring $R$.

Let $R$ be $\mathbb{Z}$ or $F[x]$ with $F$ a field. Then:
> Given $a,b\in R$, a $\gcd(a,b)$ always exists
> If $a,b\neq0$, then $\gcd(a,b)$ can be computed using the Euclidean Algorithm
> If $d$ is a $\gcd(a,b)$ then there exists $x,y\in R$

Let $R$ be an [[Integral domains, units, and polynomial rings|integral domain]], let $a,b\in R$ and assume $d=\gcd(a,b)$ exists. Then $u\cdot d$ is a $\gcd(a,b)$ for every $u\in R^X$. Moreover if $d$ and $d'$ are $\gcd(a,b)$ then $d=u\cdot d'$ for some $u\in R^X$. 

To prove the first statement, assume $d\cdot u$ has the same properties of $d$. That is $d|a\implies\exists m\in R$ such that $a=d\cdot m\implies a=d\cdot u\cdot u^{-1}\cdot m=(d\cdot u)\cdot(u^{-1}\cdot m)\implies d\cdot u|a$. Similarly, one can show that $d\cdot u|b$ by the same argument. To show that if $e|a,e|b$ then $e|u\cdot d$ we observe $e|a\implies e|d$ since $d$ is a $\gcd(a,b)\implies  d=k\cdot e$ for some $k\in R\implies d\cdot u=k\cdot u\cdot e\implies e|d\cdot u$. Similarly $e|b\implies e|d\cdot u$ by the same argument. So we have that if $d=\gcd(a,b)$ and $u$ is a unit in $R$, then $d\cdot u$ is also a $\gcd(a,b)$.

To prove the second statement, we observe both $d,d'$ are $\gcd(a,b)$. From the properties of the $\gcd$ we have that $d|d'$ and $d'|d$, that is $d'=d\cdot v$ and $d=d'\cdot u$ for $u,v\in R$. Combining these statements gives $d=(d\cdot v)\cdot u\implies d(1-u\cdot v)=0$. Now since $R$ was assumed to be an integral domain, there exist no zero divisors other than $0$. This allows us to conclude that either $d=0$ or $(1-u\cdot v)=0$. $d=0\implies d'=0$. $1-u\cdot v=0\implies u\cdot v=1\implies u,v\in R^X$ are units. So either both $d=d'=0$ or $d$ and $d'$ differ by a unit.

## Monic:
A polynomial in $F[x]$ with $F$ a field is called monic if its leading coef