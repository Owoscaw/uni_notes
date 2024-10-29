
For $n\in \mathbb{Z}$ we can write any $n$ as a product of prime numbers:$$\Huge n=\pm p_1^{e_1}p_2^{e_2}\dots p_m^{e_m}$$For $e_1,\dots,e_m\in \mathbb{Z}$ and prime numbers $p_1,\dots,p_m$. We look for a similar notion in the [[Integral domains, units, and polynomial rings#Polynomials over a field|polynomials over a field]]. 

# Irreducibility:

Let $R$ be a [[Rings, subrings, and fields|commutative ring]], an element $0\neq r\in R$ is called irreducible if:
> $r\notin R^X$
> If $r=a\cdot b$ for $a,b\in R$ then either $a$ or $b$ is a unit.

Where $R^X$ represents the [[Integral domains, units, and polynomial rings#Units|units]] of $R$. Take for example $R=F[x]$ with $F$ a [[Rings, subrings, and fields#Fields|field]]. A non-zero polynomial in $F[x]$ is an irreducible polynomial if it is not a constant polynomial and cannot be written as a product of two non constant polynomials.

Take $x^2+1$ for example. We ask if this is an irreducible polynomial in $\Re[x]$. It is not possible to write $x^2+1=(ax+b)(cx+d)$ for $a,b,c,d\in\Re$ as this polynomial has complex roots. It is irreducible in $\Re[x]$. So we look at $x^2+1\in\mathbb{C}[x]$. We see that $x^2+1=(x+i)(x-i)$, making the polynomial reducible in $\mathbb{C}[x]$

For $f\in F[x]$, if $\deg f=1$ and $f(x)=ax+b$ with $a\neq0$ then $f(x)$ is irreducible. 

For $\deg f=2,3$ $f(x)$ is irreducible if and only if there is no root of $f(x)$ in $F$, that is there exists no $a\in F:f(a)=0$. To prove this, let $a\in F$ be such that $f(a)=0$. By the division algorithm, $f(x)=q(x)(x-a)+r(x)$ with $\deg r<1$, that is $r(x)$ is a constant. Moreover $f(a)=0\implies r(a)=0$, hence $r(x)=0$ and $f(x)=q(x)$, making $f(x)$ irreducible. Conversely, assume $f(x)$ is not irreducible. Then it must have at least one root in $F$. To show that such $a\in F$ exists, we write $f(x)=g(x)h(x)$ with $\deg g,\deg h\geq1$. When written like this, either $\deg g$ or $\deg h$ must be $1$. So without loss of generality assume $\deg g=1$, that is $g(x)=bx+c$ with $b\neq0$. Take $a=-b\cdot c^{-1}$ with $b,c\in F$. Therefore $g(a)=0$, and $f(a)=g(a)h(a)=0$. Therefore $a$ is a root of $f$, and by contradiction we get that $f$ being irreducible means that it has no roots. So we have the proof as required.

Note that if $f(x)\in F[x]$ and there exists $a\in F$ such that $f(a)=0$, then $f(x)$ is not irreducible. The proof for this come from the forward implication in the proof above.