
To construct the set of real numbers, many axioms need to be defined.

# Addition axioms:

The existence of the function $+:\Re\times\Re\mapsto\Re$ is assumed, which allows the addition of two real numbers:
$$\Huge +:\Re\times\Re\mapsto\Re:(a,b)\mapsto(a+b)$$
$$\Huge +(a,b)=a+b$$
The following axioms are satisfied by this definition of the + function:
>Commutativity ($AI$):$$\Huge a+b=b+a,\,\forall a,b\in\Re$$
>Associativity ($AII$):$$\Huge (a+b)+c=a+(b+c),\,\forall a,b,c\in\Re$$
>Existence of zero ($AIII$):$$\Huge 0+a=a,\,\forall a\in\Re$$
>Existence of the negative ($AIV$): For every $a\in\Re$, there is a unique $(-a)\in\Re$ such that $a+(-a)=0$. That is to say, $(-a)$ is the negative of $a$. Also, $-(-a)=a$.

# Multiplication axioms:

The existence of the function $\cdot:\Re\times\Re\mapsto\Re$ is assumed, which allows for the multiplication of two real numbers:
$$\Huge \cdot:\Re\times\Re\mapsto\Re:(a,b)\mapsto ab$$
$$\Huge \cdot(a,b)=a\cdot b=ab,\,\forall a,b\in\Re$$
Multiplication satisfies the following axioms:
> Commutativity ($MI$):$$\Huge ab=ab,\,\forall a,b\in\Re$$
> Associativity ($MII$):$$\Huge a(bc)=(ab)c,\,\forall a,b,c\in\Re$$
> Existence of 1 ($MIII$): There exists a number in $\Re$ such that $1\neq 0$ and $1\cdot a=a,\,\forall a\in\Re$
> Existence of the inverse ($MIV$): There exists for all $a\in\Re\setminus\{0\}$ a unique $a^{-1}\in\Re$ such that $a\cdot a^{-1}=1$

# Distributivity axiom:

This axiom combines addition and multiplication definitions:
$$\Huge a(b+c)=(ab)+(ac),\,\forall a,b,c\in\Re$$

# Order axioms:

The existence of an order $<$ is assumed, such that for every $a,b\in\Re$, the statement $a<b$ is either true or false:
$$\Huge <:\Re\times\Re\mapsto\{True, False\}$$
$$\Huge <(a,b)\mapsto a<b$$
The order satisfies the following axioms:
> Trichotomy ($OI$): either $a<b$, $a=b$, or $a>b$ are true
> Transitivity ($OII$): if $a<b$ and $b<c$, then $a<c$
> Monotony of addition ($OIII$): if $a<b$, then $a+c<b+c$
> Monotony of multiplication ($OIV$): if $a<b$ and $c>0$, then $a\cdot c<b\cdot c$

$a>b$ is the same statement as $b<a$, and $a\leq b$ is written for ($a<b$ and $a=b$)

# Consequences of axioms:

Let $a,b,c,d\in\Re$:
> If $a\neq 0$, then $a^2>0$. Proof: 
> Particularly if $a=1$ then $1\cdot 1>0$ and $1\cdot 1=1$, so $1>0$. Given $a>0$, $a^2>0$ by the monotony of multiplication ($OIV$). If $a<0$, $0<-a$ by monotony of addition ($OIII$), therefore $(-a)^2>0$ by the previous case. Note that $(-a)^2=a^2$, clearly $1^2=1$ ($MIII$), so $1>0$.
> 
> If $a<b$ and $c<d$, then $a+c<b+d$. Proof:
> $a<b$, so $a+c<b+c$ by monotony of addition ($OIII$). $c<d$, so $c+b<d+b$ by monotony of addition ($OIII$). Transitivity ($OII$) then dictates that $a+c<b+d$.
> 
> If $0<a<b$ and $0<c<d$, then $a\cdot  c<b\cdot d$. Proof:
> $a<b$ and $c>0$ so $a\cdot c<b\cdot c$ by monotony of multiplication ($OIV$), $c<d$ and $b>0$ so $c\cdot b<d\cdot b$ by monotony of multiplication ($OIV$). Transitivity ($OII$) then dictates that $a\cdot c<b\cdot d$.
> 
> If $a<b$ and $c<0$, then $c\cdot b<c\cdot a$. Proof:
> $c<0$, so $-c>0$, then we have $-ca<-cb$ by monotony of multiplication ($OIV$). Therefore $-ca + ca + cb<-cb + ca + cb$ by monotony of addition ($OIII$). By the existence of the negative ($AIV$), $ca-ca=0$ and $cb-ab=0$, so we have $cb<ca$ which is equivalent to $c\cdot b<c\cdot a$ as required.
> 
> If $0<a<b$, then $0<b^{-1}<a^{-1}$. Proof:
> Note that $b^{-1}\neq 0$ and $a^{-1}\neq 0$ by existence of the inverse ($MIV$). Also $b^{-1}=(b^{-1})^2\cdot b$. $b^{-1}>0$ using monotony of multiplication ($OIV$) and the first proof. This also implies that $(ab)^{-1}>0$, so $a^{-1}b^{-1}>0$. Multiplying the inequality $a<b$ (as defined) with $a^{-1}b^{-1}$ (allowed because it is greater than zero) gives $0<b^{-1}<a^{-1}$ as required.