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

Let $R$ be a PID and $a,b\in R$ be two coprime elements (that is, no irreducible element divides both $a$ and $b$). Then $(a,b)=(1)$ and thus $ax+by=1$ for some $x,y\in R$. In particular, any $\gcd(a,b)$ is a unit. 

To prove this, observe that since $R$ is a PID, we have that $(a,b)=(r)$ for some $r\in R$. Therefore $r$ divides both $a$ and $b$, so must be a unit (as $a,b$ are coprime). Now since $r$ is a unit we have $(r)=R=(1)$. We can now state the Chinese Remainder Theorem (CRT):

Let $R$ be a PID. If $a_1,\dots,a_k\in R$ are pairwise coprime elements, then the map given by:$$\Huge\begin{align}
\varphi:R/(a_1\dots a_k)&\rightarrow\,R/(a_1)\times\dots\times R/(a_k)\\
r+(a_1\dots a_k)&\mapsto(r+(a_1),\dots,r+(a_k))
\end{align}$$Is an isomorphism.

To prove this, let $\psi:R\rightarrow R/(a_1)\times\dots\times R/(a_k)$ be a map given by $\psi(r)=(\bar r,\dots,\bar r)$. Note that this is trivially a homomorphism. We prove that this is surjective and $\ker(\psi)=(a_1a_1\dots a_k)$, then by the [[Ideals#First Isomorphism Theorem|FIT]] we have the theorem as required:

We first show that $\psi$ is surjective. For each $i=1,\dots,k$ the elements $a_i$ and each $a_1\dots a_{i-1}a_{i+1}\dots a_k$ are coprime (otherwise there would exist some $p\in R$ that divides both terms, contradicting the assumption that each element $a_n$ are pairwise coprime). Therefore by the above lemma there exists $x_i,y_i\in R$ such that:$$\Huge a_ix_i+(a_1\dots a_{i-1}a_{i+1}\dots a_k)y_i=1$$Now set $e_i=1-a_ix_i$, then we have that if $i=j$ then $e_i=1\mod(a_j)$ and $e_i=0\mod(a_j)$ otherwise. For any element $(r_1+(a_1),\dots,r_k+(a_K))\in R/(a_1)\times\dots\times R/(a_k)$ we have that:$$\Huge \psi\left(\sum_{i=1}^kr_ie_i\right)=(r_1+(a_1),\dots,r_k+(a_k))$$, so $\varphi$ is indeed surjective. We now show injectivity:$$\Huge\begin{align}
\ker\psi&=\{r:r\in(a_i),i=1,\dots,k\}\\
&=\{r:a_i|r,i=1,\dots,k\}\\
&=\{r:a_1\dots a_k|r\}\\
&=(a_1\dots a_k)
\end{align}$$Where we have used the fact that each $a_i$ are coprime and $R$ is a UFD. So we have the CRT as required.

Take for example $F[x]$ with $F$ a field. If $f(x)\in F[x]$ is a product of two coprime factors $g(x),h(x)$, then the CRT states that the map:$$\Huge\begin{align}
F[x]/(f(x))&\rightarrow F[x]/(g(x))\times F[x]/(h(x))\\
p(x)+(f(x))&\mapsto(p(x)+(g(x)),p(x)+(h(x)))=(\bar p(x),\bar p(x))
\end{align}$$Is an isomorphism. 

We can also use the CRT to understand the structure of $\mathbb{Z}[i]/(13)$. We use the fact that $\mathbb{Z}[i]$ is a PID, and that $13=(3+2i)(3-2i)$. Firstly we must prove that $3+2i$ and $3-2i$ are coprime. Suppose $x=a+bi|3+2i$ and $3-2i$, we then apply the norm map to get $N(a+bi)=a^2+b^2|N(3+2i)=N(3-2i)=13$. Therefore we have that $N(x)=1$ or $13$, since $13$ is prime. However $N(x)=13$ implies that $x=w(3+2i)$ or $x=w(3-2i)$ with $w\in\mathbb{Z}[i]^X=\{1,-1,i,-i\}$. However since $(3+2i)/(3-2i)=(3+2i)^2/13\notin\mathbb{Z}[i]$, implying that if $a+bi|3+2i$ and $a+bi|3-2i$ then $N(a+bi)=1$, and thus $a+bi\in\mathbb{Z}[i]^X$, so we have that $3+2i$ and $3-2i$ are indeed coprime and we can apply the CRT to state:$$\Huge \mathbb{Z}[i]/(13)\cong\mathbb{Z}[i]/(3+2i)\times\mathbb{Z}[i]/(3-2i)$$Note that one can also prove that $3\pm2i$ are irreducible, making $(3\pm2i)$ maximal ideals, and the rings $\mathbb{Z}[i]/(3+2i),\mathbb{Z}[i]/(3-2i)$ are fields.