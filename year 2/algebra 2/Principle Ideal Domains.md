Recall for a commutative ring $R=\mathbb{Z}$ or $F[x]$ with $F$ a [[Rings, subrings, and fields#Fields|field]]:$$\Huge (a,b)=(\gcd(a,b))$$An [[Integral domains, units, and polynomial rings|integral domain]] in which all [[Ideals]] are principle is called principle ideal domain (PID). We propose that $\mathbb{Z}$ and $F[x]$ are PIDs. Let $R$ be either $\mathbb{Z}$ or $F[x]$ and define:$$\Huge d:R\setminus\{0\}\mapsto\mathbb{N},\,\,d(a)=\begin{cases}|a|&R=\mathbb{Z}\\\deg a&R=F[x]\end{cases}$$Let $I$ be an ideal in $R$. If $I=\{0\}=0$ then $I$ is principle. So assume $I\neq0$ and let $m\in I$ with $m\neq0$ such that $d(m)$ is minimal for all elements in $I$. That is for any $b\in I$, $d(b)\geq d(m)$. We then aim to show that $I=(m)$, which is principle. Let $a\in I$, then dividing by $m$ we see that $a=q\cdot m+r$ with $d(r)<d(m)$. If $r\neq0$ this contradicts the minimality of $m$ since $r=a-qm\in I$, therefore we must have $r=0$. This implies that $a=qm\implies a\in(m)\implies I=(m)$ is a principle ideal. Therefore all ideals in $\mathbb{Z}$ and $F[x]$ are principle, making them PIDs.

We propose that being a PID implies being a [[Factorisation in rings#Unique factorisation domains|UFD]]. The proof is omitted.

We can directly show $\mathbb{Z}[\sqrt{-5}]$ is not a PID. The ideal $(3,1+\sqrt{-5})\in\mathbb{Z}[\sqrt{-5}]$ is not principle, so assume that it is of the form $(a)$, then we have:$$\Huge 3=ax_1,\,\,1+\sqrt{-5}=ax_2$$For some $x_1,x_2\in\mathbb{Z}[\sqrt{-5}]$. After applying the Norm map, we see that $N(a)$ divides both $N(3)=9$ and $N(1+\sqrt{-5})=6$, therefore $N(a)=1$ or $3$, as these are the common factors of $9$ and $3$. There is no element with norm of $3$, so we have that $N(a)=1\implies a=\pm1$ is a unit, implying that $(a)=\mathbb{Z}[\sqrt{-5}]$ however $(3,1+\sqrt{-5})\neq\mathbb{Z}[\sqrt{-5}]$. If that were the case we should be able to write:$$\Huge 1=(x+y\sqrt{-5})3+(z+w\sqrt{-5})=(3x+z-5w)+(3y+z+w)\sqrt{-5}$$Since $1\in\mathbb{Z}[\sqrt{-5}]$ for some $x,y,z,w\in\mathbb{Z}$. This implies $3x+z-5w=1$ and $3y+z+w=0$. The last equation implies $\overline{3y+z+w}=\bar z+\bar w=\bar 0$, however the second implies $\overline{3x+z-5w}=\bar z+\bar w=\bar 1$, which is a contradiction. Therefore the ideal above is not the whole ring and we have that $\mathbb{Z}[\sqrt{-5}]$ is indeed not a PID. Note that $\mathbb{Z}[i]$ and $\mathbb{Z}[\sqrt{\pm2}]$ are both PIDs.

Let $R$ be a PID and $a,b\in R$. Then $d=\gcd(a,b)$ exists and $(d)=(a,b)$. Let $d\in R$ satisfy the claim, then $a=dm$ and $b=dn$ for some $m,n\in R$. Suppose there exists some $e\in R$ such that $a=em'$ and $b=en'$ for some $m',n'\in R$. Then:$$\Huge (d)=(a,b)\subseteq(e)$$Therefore $\exists k\in R:d=ek\implies e|d$, so $d$ is a $\gcd$ of $a$ and $b$.

# Fields as quotients:

Let $R$ be a commutative ring and $I\subseteq R$ an ideal of $R$. We have seen that $R/I$ is a field if and only if $I$ is a maximal ideal, allowing us to prove the following:

Let $R$ be a PID and $a\in R$ an irreducible element. Then the principal ideal $(a)$ is a maximal ideal. Suppose that some ideal $I$ contains $(a)$, then $I=(t)$ for some $t\in R$ and so $a=tm$ for some $m\in R$. Then either $t$ or $m$ is a unit. If $t$ is the unit, $(t)=(1)=R$ and if $m$ is the unit, $(t)=(a)$. That is either $I=R$ or $I=(a)$, so by definition $(a)$ is maximal.

The above lemma suggests that for a PID $R$ and irreducible element $(a)$ we have that $R/(a)$ is a field. Previously we have seen that $\Re[x]/(x^2+1)\cong\mathbb{C}$ and $\mathbb{Q}[x]/(x^2-2)\cong\mathbb{Q}[\sqrt{2}]$. We can generalise this result as follows, extending the definition of a [[Real vector spaces|vector field]] $V$ to be defined on any field $F$ instead of $\Re$. Now we can prove:

Let $F$ be a field and $f(x)\in F[x]$ be an irreducible polynomial, then $F[x]/(f(x))$ is a field. Moreover, it is a vector space with a basis $B=\{1,\bar x,\bar x^2,\dots,\bar x^{n-1}\}$ where $n=\deg f$. That is to say, any element in $F[x]/(f(x))$ can be uniquely written as:$$\Huge a_0+a_1\bar x+\dots+a_{n-1}\bar x^{n-1}$$With each $a_i\in F$. To prove this, observe that $f(x)$ is irreducible and $F[x]$ is a PID, making the quotient $F[x]/(f(x))$ a field automatically. Moreover the quotient is a vector space over $F$ since it is an abelian group with scalar multiplication given by $\alpha\cdot(\overline{g(x)})=\overline{\alpha g(x)}$ for $\alpha\in F$ and $g(x)\in F[x]$. The set $B$ spans $F[x]/(f(x))$ by the following:$$\Huge g(x)=q(x)f(x)+r(x)$$For any $g(x)\in F[x]$ with $\deg g>n$ where $\deg r<n$. Therefore we can say $\overline{g(x)}=\overline{r(x)}$. Since this span contains any polynomial in $\bar x$ of degree at most $n-1$ it will contain $\overline{r(x)}$ and hence $\overline{g(x)}$, therefore the basis spans the quotient. The set $B$ is linearly independent if:$$\Huge \sum_{i=0}^{n-1}a_i\bar x^i=\bar 0$$For some $a_i\in F$. Since $\sum_{i=0}^{n-1}a_ix^i\in(f(x))$ we have that $f(x)$ divides the sum, implying that $\deg f\leq n-1$, a contradiction unless each $a_i=0$, making $B$ indeed a basis.

Take for example the quotient $\mathbb{Q}[x]/(x^3-2)$. We ask if this is a field. As a vector space over $\mathbb{Q}$ has a basis $\{1,\bar x,\bar x^2\}$ and hence has dimension $3$ over $\mathbb{Q}$, so the quotient is indeed a field.

Also $(\mathbb{Z}/2)[x]/(x^2+x+1)$ has basis $\{1,\bar x\}$ and so is of dimension $2$ over $\mathbb{Z}/2$. That is, it has four elements represented as $\{\bar 0,\bar 1,\bar x,\overline{1+x}\}$, usually denoted as $\mathbb{F}_4$. This is not $\mathbb{Z}/4$ since it is not an integral domain $(\bar 2\bar 2=\bar 4=\bar 0)$.

# Finite fields:

For any given prime $p\in\mathbb{Z}$ and $n\in\mathbb{N}$ there exists an irreducible polynomial $f(x)\in(\mathbb{Z}/p)[x]$ of degree $n$. Therefore we construct the field $(\mathbb{Z}/p)[x]/(f(x))$. This field will therefore have $p^n$ elements and any two such fields will be isomorphic, so we can denote the unique field (up to isomorphisms) with $p^n$ elements as $\mathbb{F}_{p^n}$.

Note that $\mathbb{F}_p$ is $\mathbb{Z}/p$ for prime $p$ but $\mathbb{F}_{p^n}$ is not $\mathbb{Z}/p^n$ for $n>1$ as this is not a field for $n>1$ since $\bar p^{n-1}\bar p=\bar p^n=\bar 0$ however $\bar p^{n-1}\neq\bar 0$ so we have a zero divisor that is not itself $\bar 0$, so $\mathbb{Z}/p^n$ fails to be an integral domain.

For example, we can construct $\mathbb{F}_{27}$ as $\mathbb{F}_{3^3}$. To do this, we must find an irreducible polynomial in $(\mathbb{Z}/3)[x]$ of degree $3$. Such a polynomial is given by $f(x)=x^3+x^2+x+\bar 2\in(\mathbb{Z}/3)[x]$. Note that this is indeed irreducible as it is of degree $3$ and has no roots in $\mathbb{Z}/3$ (one can check by finding $f(\bar 0),f(\bar 1),f(\bar 3)$). So by the above theorem we have:$$\Huge \mathbb{F}_{27}\cong(\mathbb{Z}/3)[x]/(f(x))$$Every element in this field can be written as $\overline{a_0+a_1x+a_2x^2}$ with each $a_i\in\mathbb{Z}/3$. Noting that $\overline{x^3+x^2+x+2}=\bar 0$ we can multiply two such elements:$$\Huge\begin{align}
(\bar 2x^2-\bar x+\bar 2)(\bar x^2+\bar x+\bar 1)&=\overline{ 2x^4}+\bar x^3+\bar x+\bar 2\\
&=\overline{2x^4}-(\bar x^2+\bar x+\bar 2)+\bar x+\bar 2\\
&=\overline{2x^4}-\bar x^2\\
&=\overline{2x}(-\bar x^2-\bar x-\bar 2)-\bar x^2\\
&=\bar x^3+\overline{2x}\\
&=-\bar x^2-\bar x-\bar 2+\overline{2x}\\
&=\overline{2x^2}+\bar x+\bar 1\in\mathbb{F}_{27}
\end{align}$$

# The Chinese Remainder Theorem:

