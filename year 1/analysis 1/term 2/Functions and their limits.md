
## Open-ness? and interior points:

A subset $X\subset\Re$ is called open if for each $c\in X$ there exists in an open interval $(c-\delta,c+\delta)\subset X$ with $\delta>0$. This $\delta$ usually depends on $c$ and is not unique, if $\delta>0$ works, then every $\delta^\prime$ with $0<\delta^\prime<\delta$ also works. For example, any open interval $(a,b)$ is open since for $c\in(a,b)$ then choose $\delta=\min(c-a,b-c)$. $\emptyset$ is also open, since $\nexists c\in\emptyset$. Any closed interval $[a,b]$ is not open, $\delta$ can be found for any point except $a$ or $b$, at these points $(a-\delta,a+\delta)\not\subset[a,b]$.

A point $c\in X$ is called an interior point if there exists an open interval $(c-\delta,c+\delta)\subset X$ with $\delta>0$.

For a convergent [[Sequences#Limit of a sequence|sequence]] $(x_n)_{n\in\mathbb N}$ in the closed interval $[a,b]$, then the limit lies in $[a,b]$. This has a corollary where if the sequence is instead in the open interval $(a,b)$ then the limit lies in the closed interval $[a,b]$ also.

A subset $X\subset\Re$ define $\overline X$ be the set of all limits of convergent sequences in $X$. We call $\overline X$ the closure of $X$. $X\subset\Re$ is closed if $X=\overline X$, we always get that $X\subset\overline X$. For the closed interval $(a,b)$, then $\overline{(a,b)}\subset[a,b]$ by the above corolarry. Define a sequence $(x_n)_{n\in\mathbb N}\in(a,b)$ such that $\lim_{n\to\infty}x_n=a$. We then say $x_n=a+\frac{1}{n}$ such that for any $\delta>0$, we have $\frac{1}{n}<\delta$. So the point $a$ is included in the closure of $(a,b)$, giving the result as follows by the above theorems:$$\Huge \overline{(a,b)}=[a,b],\,\,\overline{[a,b]}=[a,b]$$
Note that sets can be both open and closed, for example [[Definition of the reals|$\Re$]] is both open and closed. Similarly, $\emptyset$ is both open and closed by triviality. Sets can also be neither open nor closed, for example $[a,b)$ since openness fails at $a$, and closedness fails at $b$. This is because $\overline{[a,b)}=[a,b]\neq[a,b)$. For a sequence $(x_n)_{n\in\mathbb N}\in[a,b]$, the sequence has a convergent subsequence with the limit in $[a,b]$. The proof comes from looking at the [[Sequences#The Bolzano-Weierstrass Theorem|Bolzano-Weierstrass theorem]].

# Limits of functions:

Let $f:X\mapsto\Re$ be a [[Functions, Domain and Range|function]] and assume $X\subset\Re$ contains an open interval $(a,b)$ with the possible exception of $c\in(a,b)$. We say that:$$\Huge \lim_{x\to c}f(x)=L$$For some $L\in\Re$ if for all $\epsilon>0$ there exists a $\delta>0$ such that $|f(x)-L|<\epsilon$ for all $x\in(a,b)\setminus\{c\}$ with $|x-c|<\delta$. Note that if $c\in X$ then $L$ can be $f(c)$, but not necessarily:![[limit of a function]]
Let $f:X\mapsto\Re$ be a function and assume $X\subset\Re$ contains an open interval $(a,b)$ again with the possible exception of $c\in(a,b)$. Then $\lim_{x\to c}f(x)=L\iff$ for all sequences $(x_n)-{n\in\mathbb N}\in X\setminus\{c\}$ with $\lim_{n\to\infty}x_n=c$, we have:$$\Huge\lim_{x\to c}f(x)=L\iff\lim_{n\to\infty}f(x_n)=L$$Proven as follows:![[sequence limit proof]]
# Sided limits:

Let $f:(a,b)\mapsto\Re$ be a function. The right sided limit is then defined as: $$\large \lim_{x\to a^+}f(x)=L\iff\forall\epsilon>0,\,\,\exists\delta>0:|f(x)-L|<\epsilon\,\forall x\in(a,b)\,\,\text{with}\,\,|x-a|<\delta$$The left sided limit is defined similarly. The right and left sided limits for $c\in(a,b)$ can be defined by restricting the domain to $(a,c)$ or $(c,b)$.

# Infinite limits:

Let $f:X\mapsto\Re$ be a function such that $X$ contains an interval $(a,\infty)$. Then we define:$$\Huge \lim_{x\to\infty}f(x)=L\iff\forall\epsilon>0,\,\exists K>a:|f(x)-L|<\epsilon\,\,\forall x>K$$Similarly, if $X$ contains an interval $(-\infty, b)$, define:$$\Huge \lim_{x\to-\infty}f(x)=L\iff\forall\epsilon>0,\,\exists K<b:|f(x)-L|<\epsilon\,\forall x<K$$
# COLT:

Let $f,g:X\mapsto\Re$ be two functions with limits $\lim_{x\to c}f(x)=L_1$ and $\lim_{x\to c}g(x)=L_2$:
> For any $\alpha,\beta\in\Re$, $\lim_{x\to c}(\alpha f(x)+\beta g(x))=\alpha L_1+\beta L_2$
> $\lim_{x\to c}f(x)g(x)=L_1L_2$
> $\lim_{x\to c}\frac{f(x)}{g(x)}=\frac{L_1}{L_2}$, assuming $L_2\neq0$

The following are proven using [[Sequences#Calculus of limits theorem ( Limits and Continuity Consequences of continuity COLT )|COLT]] and the above theorems regarding a sequence within an interval.

# Squeezing theorem:

Let $X\subset\Re$, $c\in X$, and $f,g,h:X\mapsto\Re$ with $f(x)\leq g(x)\leq h(x)$ for all $x\in X$. Assume that:$$\Huge \lim_{x\to c}f(x)=L=\lim_{x\to c}h(x)\implies\lim_{x\to c}g(x)=L$$
