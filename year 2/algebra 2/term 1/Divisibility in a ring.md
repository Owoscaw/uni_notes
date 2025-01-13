
Let $R$ be a [[Rings, subrings, and fields|commutative ring]]. Let $a,b\in R$. We say that $a$ divides $b$ in $R$ and write $a|b$ if there exists $r\in R$ such that $b=r\cdot a$. An element $d\in R$ is called a greatest common divisor of $a$ and $b$ if the following hold:
> $d|a$ and $d|b$
> If $e\in R$ divides both $a,b$, then $e|d$

Note that according to the definition above, both $-1$ and $1$ are a $\gcd(2,3)$ with $R=\mathbb{Z}$, however since $\mathbb{Z}$ has an ordering, we can define the greatest common divisor as $1$. We must also define:$$\Huge \gcd(0,0):=0$$Note that $\gcd(a,b)$ does not exist for every $a,b$ in every ring $R$.

Let $R$ be $\mathbb{Z}$ or $F[x]$ with $F$ a field. Then:
> Given $a,b\in R$, a $\gcd(a,b)$ always exists
> If $a,b\neq0$, then $\gcd(a,b)$ can be computed using the Euclidean Algorithm
> If $d$ is a $\gcd(a,b)$ then there exists $x,y\in R$

## Euclidean algorithm:
Set $r_{-1}(x):=a\in F[x]$ and $r_0(x):=b\in F[x]$. We start with the pair $(r_{-1}(x),r_0(x))$ and obtain the decomposition $r_{-1}(x)=q_1r_0(x)+r_1(x)$ with $q_1(x),r_1(x)\in F[x]$ where $\deg(r_1)<\deg(r_0)$. If $r_0(x)=0$ then $r_0(x)$ already divides $r_{-1}(x)$. Otherwise we then iterate this process with the pair $(r_0(x),r_1(x))$. That is:
$$\large
\begin{align}
r_{-1}(x) &= q_1(x)r_0(x)+r_1(x),&0\leq\deg(r_1)<\deg(r_0),\\r_0(x) &= q_2(x)r_1(x)+r_2(x),& 0\leq\deg(r_2)<\deg(r_1),\\\vdots\\ r_{i-2}(x) &=q_i(x)r_{i-1}(x)+r_i(x),& 0\leq\deg(r_i)<\deg(r_{i-1}),\\\vdots\\r_{n-2}(x)&=q_{n}(x)r_{n-1}(x)+r_n(x),&0\leq\deg(r_n)<\deg(r_{n-1}),\\ r_{n-1}(x)&=q_{n+1}(x)r_n(x)+0
\end{align}
$$Note that this process would terminate after finitely many steps, as the degree is a positive integer (or $-\infty$ for the zero polynomial) so if $\deg(r_0)=n\geq0$ there are at most $n+1$ steps before the remainder becomes zero. Now $r_n(x)$ is a common divisor of both $r_{-1}(x)$ and $r_0(x)$. We can also substitute remainders in to write:$$\Huge r_n(x)=h(x)r_{n-2}(x)+g(x)r_{n-3}(x)$$For some $g,h\in F[x]$. Going "up the ladder" by substituting $r_{n-2}$ and $r_{n-3}$ successively until we are only left with $r_{-1}(x)$ and $r_0(x)$. In such case we write:$$\Huge r_n(x)=A(x)r_{-1}(x)+B(x)r_0(x)$$For some $A,B\in F[x]$.
 

Let $R$ be an [[Integral domains, units, and polynomial rings|integral domain]], let $a,b\in R$ and assume $d=\gcd(a,b)$ exists. Then $u\cdot d$ is a $\gcd(a,b)$ for every $u\in R^X$. Moreover if $d$ and $d'$ are $\gcd(a,b)$ then $d=u\cdot d'$ for some $u\in R^X$. 

To prove the first statement, assume $d\cdot u$ has the same properties of $d$. That is $d|a\implies\exists m\in R$ such that $a=d\cdot m\implies a=d\cdot u\cdot u^{-1}\cdot m=(d\cdot u)\cdot(u^{-1}\cdot m)\implies d\cdot u|a$. Similarly, one can show that $d\cdot u|b$ by the same argument. To show that if $e|a,e|b$ then $e|u\cdot d$ we observe $e|a\implies e|d$ since $d$ is a $\gcd(a,b)\implies  d=k\cdot e$ for some $k\in R\implies d\cdot u=k\cdot u\cdot e\implies e|d\cdot u$. Similarly $e|b\implies e|d\cdot u$ by the same argument. So we have that if $d=\gcd(a,b)$ and $u$ is a unit in $R$, then $d\cdot u$ is also a $\gcd(a,b)$.

To prove the second statement, we observe both $d,d'$ are $\gcd(a,b)$. From the properties of the $\gcd$ we have that $d|d'$ and $d'|d$, that is $d'=d\cdot v$ and $d=d'\cdot u$ for $u,v\in R$. Combining these statements gives $d=(d\cdot v)\cdot u\implies d(1-u\cdot v)=0$. Now since $R$ was assumed to be an integral domain, there exist no zero divisors other than $0$. This allows us to conclude that either $d=0$ or $(1-u\cdot v)=0$. $d=0\implies d'=0$. $1-u\cdot v=0\implies u\cdot v=1\implies u,v\in R^X$ are units. So either both $d=d'=0$ or $d$ and $d'$ differ by a unit.

# Monicicity:

A polynomial in $F[x]$ with $F$ a field is called monic if its leading coefficient is $1$.

Note that for $p(x)=a_mx^m+a_{m-1}x^{m-1}+\dots+a_0$ with $a_m\neq0$, $q(x)=a^{-1}_m(a_mx^m+\dots+a_0)=x^m+\dots$, then:$$r\Huge q(x)=a^{-1}_mp(x)\text{ is monic}$$If $p(x)=\gcd(f,g)$, then so is $q(x)$.

Assume $p_1(x),p_2(x)$ are monic polynomials in $F[x]$ such that $p_1(x)=u\cdot p_2(x)$ for $u\in F^X$. By comparing leading terms, we observe that $u=1\implies p_1(x)=p_2(x)$. Therefore if $f,g\in F[x]$, then the monic $\gcd(f,g)$ is unique