
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

Let $f(x)=a_0+a_1x+\dots+a_nx^n\in\mathbb{Z}[x]$ and $\deg f\geq1$. If $f\left(\frac{p}{q}\right)=0$ with $p,q\in\mathbb{Z}$ and $\gcd(p,q)=1$, then $p|a_0$ and $q|a_n$. To prove this, observe $0=f\left(\frac{p}{q}\right)=a_0+a_q\left(\frac{p}{q}\right)+a_2\left(\frac{p}{q}\right)^2+\dots+a_n\left(\frac{p}{q}\right)^n$. Rearranging for $q^n$ gives $-a_0q^n=a_1pq^{n-1}+a^2p^2q^{n-2}+\dots+a_np^n=p(a_1q^{n-1}+\dots+a_np^{n-1})$. We see that the right hand bracketed term is the sum and product of a series of integers, so must be an integer itself. Therefore we say $p|-a_0q^n\implies p|a_0$ since $\gcd(p,q)=1$. Similarly, we have $-a_n\left(\frac{p}{q}\right)^n=a_0+a_1\left(\frac{p}{q}\right)+\dots+a_{n-1}\left(\frac{p}{q}\right)^{n-1}\implies-a_np^n=a_0q^n+a_1pq^{n-1}+\dots+a_{n-1}p^{n-1}q=q(a_0q^{n-1}+\dots+a_{n-1}p^{n-1})$, and by the same argument we conclude $q|-a_np^n\implies q|a_n$, giving the proof as required. This is useful for finding rational roots of any polynomial, and can therefore be used to find irreducible elements in a ring.

Note that $2x+2$ is irreducible in $\mathbb{Q}[x]$, however is not irreducible in $\mathbb{Z}[x]$ since $2\notin\mathbb{Z}[x]^X$.

# Gauss' Lemma:

A non-constant polynomial $f(x)=a_0+a_1x+\dots+a_nx^n$ in $\mathbb{Z}[x]$ is irreducible in $\mathbb{Z}[x]$ if and only if it is irreducible in $\mathbb{Q}[x]$ and $\gcd(a_0,a_1,\dots,a_n)=1$