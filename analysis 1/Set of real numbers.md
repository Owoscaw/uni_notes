
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
> Monotony of multiplication ($OIV$): if $a<b$