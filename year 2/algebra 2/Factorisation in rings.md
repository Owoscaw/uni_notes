
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

A non-constant polynomial $f(x)=a_0+a_1x+\dots+a_nx^n$ in $\mathbb{Z}[x]$ is irreducible in $\mathbb{Z}[x]$ if and only if it is irreducible in $\mathbb{Q}[x]$ and $\gcd(a_0,a_1,\dots,a_n)=1$.

Assume $f(x)$ irreducible in $\mathbb{Q}[x]$ and $\gcd(a_0,\dots,a_n)=1$. Assume $f(x)=g(x)h(x)$ for $g,h\in \mathbb{Z}[x]$. By the assumption, we have either $\deg(g)=0$ or $\deg(h)=0$. Otherwise there would be a factorization in $\mathbb{Q}[x]$. Without loss of generality assume $\deg(g)=0,g(x)=a$ for some $a\in \mathbb{Z}$. Since $\gcd(a_0,\dots,a_n)=1$ we have that $a=\pm1$. Therefore $g(x)\in \mathbb{Z}[x]^X$, making $f(x)$ irreducible in $\mathbb{Z}[x]$. The other direction of implication is omitted.

Let $f(x)=a_0+\dots+a_nx^n\in \mathbb{Z}[x]$ and $\gcd(a_0,\dots,a_n)=1$. Then $f(x)$ is irreducible in $\mathbb{Q}[x]$ if and only if $f(x)$ is irreducible in $\mathbb{Z}[x]$. This comes directly from the above lemma.

Let $f(x)=x^n+\dots+a_0\in \mathbb{Z}[x]$ be a monic polynomial. If $f(x)$ factors in $\mathbb{Q}[x]$ then it factors in $\mathbb{Z}[x]$ to monic polynomials. Since $f(x)$ is monic, we have that $\gcd(a_0,\dots,1)=1$. By Gauss' lemma we have that $f(x)$ factors in $\mathbb{Z}[x]$ with $f(x)=g(x)h(x)=(b_mx^m+\dots+b_0)(c_lx^l+\dots+c_0)$ with $b_i,c_j\in \mathbb{Z}$. We have $b_mx^m\times c_lx^l=x^n$, so $b_mc_l=1$. Since these are integer coefficients, we must have $b_m=c_l=\pm1$. Then $f(x)=(-g(x))(-h(x))$ with $g,h$ monic.

# Eisenstein's criterion:

Let $f(x)=a_0+\dots+a_nx^n\in \mathbb{Z}[x]$ and $p\in \mathbb{Z}$ such that $p|a_0,\dots,p|a_{n-1},p\not{|}a_n$ and $p^2\not{|}a_0$ then $f(x)$ is irreducible in $\mathbb{Q}[x]$.

Let $d=\gcd(a_0,\dots,a_n)$ and set $b_i=\frac{a_i}{d}$ for $i=0,\dots,n$. We then define:$$\Huge F(x)=\frac{1}{d}f(x)=b_0+\dots+b_nx^n$$We now have $\gcd(b_0,\dots,b_n)=1$. Since $p\not{|}a_n$ we have $p\not{|}d$ so we get the same conditions on $F(x)$ as we did on $f(x)$, that is $p|b_0,\dots,p|b_{n-1},p\not{|}b_n$ and $p^2\not{|}b_0$. Note that $\frac{1}{d}\in \mathbb{Q}[x]^X$, so $f(x)$ irreducible in $\mathbb{Q}[x]$ if and only if $F(x)$ irreducible in $\mathbb{Q}[x]$.

Assume $F(x)$ is not irreducible in $\mathbb{Q}[x]$. By Gauss' lemma $F(x)$ is therefore not reducible in $\mathbb{Z}[x]$, that is $F(x)=g(x)h(x)=(\alpha_0+\dots+\alpha_mx^m)(\beta_0+\dots+\beta_kx^k)$ with $\alpha_i,\beta_j\in \mathbb{Z}$. Note $\deg(g),\deg(h)\geq1$ since if one function were constant, it would be a common factor of $F$. Take a reduction $\mod p$:$$\Huge \bar F(x)=\bar g(x)\bar h(x)\in\left(\frac{\mathbb{Z}}{p}\right)[x]$$Since $p$ divides every coefficient in $F(x)$ except for the leading term, we have:$$\Huge \bar F(x)=\bar b_nx^n$$Note $\deg(\bar g)=\deg(g)$ and $\deg(\bar h)=\deg(h)$ since $\bar\alpha_m\bar\beta_k=\bar b_n\neq\bar0$. This implies  $\bar\alpha_m,\bar\beta_k\neq0$. Moreover $\bar\alpha_0\bar\beta_0=\bar b_0=\bar 0\implies p|\alpha_0\beta_0$, so $p$ divides either $\alpha_0$ or $\beta_0$. Without loss of generality assume $p|\alpha_0$. It is enough to show that $p|\beta_0$ since in this case, $p^2$ will divide $\alpha_0\beta_0$. Assuming that $p|\alpha_0$ but $p\not{|}\beta_0$ we have that $b_1=\alpha_0\beta_1+\alpha_1\beta_0$, which implies $\alpha_1\beta_0=b_1-\alpha_0\beta_1$. Since $p|b_1$ and $p|\alpha_0$ we have that $p|\alpha_1\beta_0$, and since $p\not{|}\beta_0$ we have that $p|\alpha_1$. One can show that this holds for every coefficient in $\bar g(x)$ up to $\alpha_{m-1}$. So we have:$$\Huge \bar g(x)=\bar\alpha_mx^m,\,\,\bar g(x)\bar h(x)=\bar\alpha_m\bar\beta_0x^m+\dots=\bar F(x)=\bar b_nx^n$$Which implies $\bar \alpha_m\bar \beta_0=\bar 0\implies \bar \beta_0=\bar 0\implies p|\beta_0$, a contradiction. Therefore the assumption that $F(x)$ is not irreducible in $\mathbb{Q}[x]$ is false, that is $F(x)$ is irreducible in $\mathbb{Q}[x]$. Since we had the same conditions on $F(x)$ as $f(x)$, we can conclude that $f(x)$ is irreducible in $\mathbb{Q}[x]$.

# Unique factorization:

Let $F$ be a [[Rings, subrings, and fields#Fields|field]], $f(x)\in F[x]$ with $\deg(f)\geq1$. Then $f(x)$ can be factorized uniquely into a product of irreducible polynomials, up to the order of factors and units. That is to say:$$\Huge x^2-1=(x+1)(x-1)=(x-1)(x+1)=\frac{1}{2}(x+1)2(x-1)$$Are the same factorisation. To prove this, we must first show that a factorisation exists, and then prove such factorisation is unique. We do this by induction on $\deg(f)$:

Base case, $\deg(f)=1$. It is trivial that all degree $1$ polynomials over a field are irreducible. Assume we have a factorisation into irreducible elements for all $f(x)\in F[x]$ with $\deg(f)<n$ for some $n\in \mathbb{N}$. Now let $\deg(f)=n$, if $f(x)$ is irreducible then we are done. However if $f(x)$ is not irreducible, then $f(x)=g(x)h(x)$ for some $g,h\in F[x]$ such that $1\leq\deg(g)<n$ and $1\leq\deg(h)<n$. By the assumption, $g,h$ have factorisations into irreducible elements, therefore $f(x)=g(x)h(x)$ has a factorisation into irreducible elements. Therefore a factorisation into irreducible elements exists for every $f(x)\in F[x]$. We now show that such a factorisation is unique.

We claim that if $p(x)\in F[x]$ is irreducible and divides $a(x)b(x)$ for some $a,b\in F[x]$ then $p(x)$ divides either $a(x)$ or $b(x)$. If $p(x)\not{|}a(x)$ then $\text{Monic}\gcd(p(x),a(x))=1$ and by the properties of $\gcd$ we have that there exists $A,B\in F[x]$ such that:$$\Huge A(x)p(x)+B(x)a(x)=1$$Hence $A(x)p(x)b(x)+B(x)a(x)b(x)=b(x)$. However since $p(x)|B(x)a(x)b(x)$ by assumption, and clearly $p(x)|A(x)p(x)b(x)$ we have $p(x)|b(x)$. The proof for $p(x)|a(x)$ is analogous, so we have the claim.

Now we can prove uniqueness of the factorisation. Suppose that $f(x)=p_1p_2\dots p_m=q_1q_2\dots q_n$ where each $p,q$ are irreducible polynomials in $F[x]$. Then $p_1$ divides $q_1q_2\dots q_n$ so by the above claim $p_1|q_i$ for some $i$, that is to say $q_i=u_1p_1$ for some $u_1\in F[x]$. However since $p_1,q_i$ are irreducible we have that $u_1$ must be a unit, therefore:$$\Huge p_1p_2\dots p_m=q_1\dots q_i\dots q_n=q_1\dots q_{i-1}u_1p_1q_{i+1}\dots q_n$$Which implies $p_2\dots p_m=q_1\dots q_{i-1}u_1q_{i+1}\dots q_n$. This argument can be repeated until all factors cancel out and we see that $m=n$ and each $q_i=p_ju_j$ for some $p_j$ and some unit $u_j$, thus the two factorisations are the same up to re ordering and multiplication by units. So we have the proof as required.

## Prime definition:
Let $R$ be a commutative ring. An element $x\in R$ is called prime if the following hold:
> $x$ is non zero and not a unit
> If $x|ab$ for $a,b\in R$ then $x|a$ or $x|b$

Note that in $\mathbb{Z}$, an element $p$ is prime if and only if it is irreducible. Similarly, in $F[x]$ with $F$ a field a polynomial $f(x)$ is irreducible if and only if it is prime. 

Let $R$ be an [[Integral domains, units, and polynomial rings#Polynomials over a field|integral domain]] and $x\in R$ a prime element. Then $x$ is irreducible. Assume we have a factorisation $x=ab$ with $a,b\in R$. We must show that either $a$ or $b$ is a unit. By definition it is known that $x$ divides either $a$ or $b$, so without loss of generality assume $x|a$. Therefore there exists some $r\in R$ such that $a=rx$, but then $x=ab=rxb\implies x(1-rb)=1$. Since $R$ is an integral domain and $x\neq 0$ we get that $rb=1$, that is $b$ is a unit. The proof is analogous for $x|b$.

# Unique factorisation domains