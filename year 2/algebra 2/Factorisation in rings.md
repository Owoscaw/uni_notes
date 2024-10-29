
For $n\in \mathbb{Z}$ we can write any $n$ as a product of prime numbers:$$\Huge n=\pm p_1^{e_1}p_2^{e_2}\dots p_m^{e_m}$$For $e_1,\dots,e_m\in \mathbb{Z}$ and prime numbers $p_1,\dots,p_m$. We look for a similar notion in the [[Integral domains, units, and polynomial rings#Polynomials over a field|polynomials over a field]]. 

Let $R$ be a [[Rings, subrings, and fields|commutative ring]], an element $0\neq r\in R$ is called irreducible if:
> $r\notin R^X$
> If $r=a\cdot b$ for $a,b\in R$ then either $a$ or $b$ is a unit.

Where $R^X$ represents the [[Integral domains, units, and polynomial rings#Units|units]] of $R$. Take for example $R=F[x]$ with $F$ a [[Rings, subrings, and fields#Fields|field]]. A non-zero polynomial in $F[x]$ is an irreducible polynomial if it is not a constant polynomial and cannot be written as a product of two non constant polynomials.

Take $x^2+1$ for example. We ask if this is an irreducible polynomial in $\Re[x]$. It is not possible to write $x^2+1=(ax+b)(cx+d)$ for $a,b,c,d\in\Re$ as this polynomial has complex roots. It is irreducible in $\Re[x]$. So we look at $x^2+1\in\mathbb{C}[x]$. We see that $x^2+1=(x+i)(x-i)$, making the polynomial reducible in $\mathbb{C}[x]$