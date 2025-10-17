
# Bounds, suprema, and infima:

Let $X\subset \Re$. We say $X$ is bounded above if there exists $C\in\Re$ with $x\leq C$ for all $x\in X$. Here, $C$ is an upper bound for $X$, note that $C+1$ is also an upper bound for $X$. $X$ is bounded below is there exists a set $c\in\Re$ with $x\geq c$ for all $x\in X$. Here, $c$ is a lower bound for $X$. The set $X$ is bounded if it is both bounded above and below.

For example, take $X=\mathbb{N}$. $1$ is a lower bound for $\mathbb{N}$ as $1\leq n$ for all $n\in\mathbb{N}$. An upper bound for $\mathbb{N}$ would be a number $C$ such that $n\leq C$ for all $n\in \mathbb{N}$. The existence of such $C$ cannot be ruled out.

Let $X\subset\Re$, an element $M\in X$ is called the maximum of $X$ if $x\leq M$ for all $x\in X$. If such $M$ exists, then we write $M=\text{max}\,X$. Similarly, an element $m\in X$ is called the minimum of $X$ if $x\geq m$ for all $x\in X$. If such $m$ exists, then we write $m=\text{min}\,X$.

Let $X\subset\Re$ be bounded from above. A number $C\in\Re$ is called the supremum ($sup\,X$) of $X$, or least upper bound if:
> $C$ is an upper bound of $X$.
> Whenever $B\in\Re$ is an upper bound of $X$, then $C\leq B$.

Similarly, a number $c\in\Re$ is called the infimum ($inf\,X$) of $X$, or greatest lower bound if:
> $c$ is a lower bound of $X$.
> Whenever $b\in\Re$ is a lower bound of $X$, then $c\geq b$.

If $X$ has a maximum, then this maximum must be the supremum of $X$. Let $X$ be a set and $M\in X$ be the maximum of $X$, then $sup\,X=M$. By definition, $M$ is an upper bound. If $B\in\Re$ is another upper bound of $X$, then we require $M\leq B$. This is the case as $B\geq x,\,\forall x\in X$.

Let $X\subset \Re$ and $f:X\mapsto\Re$. If $f(x)$ is bounded above, we denote $sup(f)$ as the supremum of $f(x)$. Similarly if $f(x)$ is bounded below, we denote $inf(f)$ as the infimum of $f(x)$

Example:
![[infimum example]]

# The axiom:

Every non-empty subset of $\Re$ which is bounded above has a supremum. 

Let $a,b\in\Re$ with $b>0$, then there exists a natural number $n$ with $nb>a$. Assume that this is not the case, then $X=\{nb\in\Re:n\in\mathbb{N}\}$ is bounded above. By the completeness axiom, $sup\,X=C\in\Re$ exists. So $nb\leq C$. Also $C-b<C$, so $C-b$ must not be an upper bound of $X$. So $\exists n\in\mathbb{N}$ such that $nb>C-b\iff(n+1)b>C$. Note that $(n+1)\in\mathbb{N}$, so $(n+1)b\in X$, so $C$ cannot be an upper bound. Here, assuming the opposite of this axiom leads to a contradiction so it must then be true.

Taking $b=1$, this says for any real number $a$, there is a natural number $n\in\mathbb{N}$ with $n>a$. Therefore the natural numbers cannot be bounded above. Therefore, using the example above:![[infimum resolved]]
## Roots:

Let $a\geq 0$ and $p\in\mathbb{N}$, there exists exactly one $x\geq 0$ with $x^p=a$. This unique $x$ is called the $p$th root of $a$, denoted as $^p\sqrt{a}$. This gives a function:$$\Huge ^p\sqrt{\cdot}:[0,\infty)\mapsto[0,\infty)$$
If $p$ is odd, this function definition can be extended to:
$$\Huge ^p\sqrt{a}=-^p\sqrt{-a}$$
This is proven as follows:
If $a=0$, use $x=0$, so we assume $a>0$. If $0<x<y$, then $x^p<y^p$, which gives at most one $x$ with $x^p=a$. Consider the set $A=\{x\in\Re:x^p<a\}$. If $x\in A$, then:
$$\Huge x^p<a<1+pa\leq(1+a)^p$$
By the [[Proof techniques#Bernoulli inequality|Bernoulli inequality]]. We also get $x<1+a$ from looking at $x^p<(1+a)^p$ and taking the $p$th root, so $1+a$ is an upper bound for the set $A$. By the completeness axiom, $\zeta=sup\,A$ exists, as it is bounded above and is non empty ($0\in A$). We require $\zeta^p=a$, so we will show $\zeta^p>a$ and $\zeta^p<a$, as in $\zeta^p\neq a$, leads to a contradiction:
> Assuming $\zeta^p<a$, by the Bernoulli inequality, we have:$$\Huge \left(\zeta+\frac{1}{n}\right)^p\leq\zeta^p+\frac{\alpha}{n},\,\text{where}:$$$$\Huge \alpha={p\choose1}\zeta^{p-1}+{p\choose 2}\zeta^{p-2}+\dots+{p\choose p-1}\zeta+1>0$$
> By the theorem of Archimedes, there exits $n$ so large such that:$$\Huge \frac{\alpha}{n}<a-\zeta^p$$
> So we have:$$\Huge \left(\zeta+\frac{1}{n}\right)^p\leq\zeta^p+\frac{\alpha}{n}<a,\,\text{so}:$$$$\Huge \left(\zeta+\frac{1}{n}\right)^p<a,\,\text{so}\,\,\,\zeta+\frac{1}{n}\in A$$
> This contradicts the assumption that $\zeta$ is an upper bound of $A$, as it is a member of the set. So now assume $\zeta^p>a$, then it is given $\zeta\notin A$:
> $$\Huge \left(\zeta-\frac{1}{n}\right)^p=\zeta^p\left(1-\frac{1}{\zeta n}\right)\geq\zeta^p\left(1-\frac{p}{\zeta n}\right)=\zeta^p-\frac{p\zeta^{p-1}}{n}$$
> By the Bernoulli inequality. Now by the theorem of Archimedes, there is $n\in\mathbb{N}$ with:$$\Huge 0<\frac{p\zeta^{p-1}}{n}<\zeta^p-a\iff-\zeta^p<\frac{p\zeta^{p-1}}{n}-\zeta^p<-a$$
> Multiplying by $-1$, flipping the inequality:
> $$\Huge \zeta^p>\zeta^p-\frac{p\zeta^{p-1}}{n}>a$$
> Combining this with the above inequalities gives:$$\Huge \left(\zeta-\frac{1}{n}\right)^p\geq\zeta^p-\frac{p\zeta^{p-1}}{n}>a$$
> This means that $\zeta -\frac{1}{n}$ is an upper bound for $A$, which is contradictory to the assumption that $\zeta=sup\,A$, as the supremum must be included in the set. Therefore there is only one value for $\zeta^p$ that satisfies $\zeta=sup\,A$, which is $\zeta^p=a$.
> 

Now we can define powers with rational exponents. Let $a>0$ and $r=\frac{p}{q}$, with $p,q\in\mathbb{N}$. We then define:$$\Huge a^r=^q\sqrt{a^p},\,\,\text{and}\,\,a^{-r}=\frac{1}{^q\sqrt{a^p}}$$
Then we must set $a^0=1$.

