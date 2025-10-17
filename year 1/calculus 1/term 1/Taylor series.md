
# Taylor's theorem:

Taylor's theorem states that if a $f(x)$ has $n+1$ continuous [[Derivative as a limit#Differentiability|derivatives]] in an open interval $I$, containing the point $x=a$, then $\forall x$ in that interval:$$\Huge f(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n(x)$$
Where:$$\Huge R_n(x)=\frac{1}{n!}\int_a^x(x-t)^nf^{(n+1)}(t)dt$$
$R_n$ is known as the remainder. Proof:
![[taylor series proof]]

# Taylor polynomials:

The combination $P_n(x)=f(x)-R_n(x)$ is a polynomial in $x$ of degree $n$, called the $n$th order Taylor polynomial of $f(x)$ at the point $x=a$:$$\Huge P_n(x)=f(a)+f'(a)(x-a)+\frac{f''(a)}{2}(x-a)^2+\dots+\frac{f^{(n)}(a)}{n!}(x-a)^n$$
If $x=a$ is omitted, assume $x=0$. This is called the Maclaurin series. The Taylor polynomial is an approximation to $f(x)$, which tends to be a good approximation for $x$ sufficiently close to $a$. As $n$ increases, the quality of the approximation also increases. The remainder function $R_n$ gives an exact expression for the remainder in the approximation.

If $f(x)$ is infinitely differentiable (smooth) on an open interval $I$ that contains $x=a$, as well as for all $x\in I,\,\lim_{n\to\infty}R_n(x)=0$, then we can say that the Taylor series about $x=a$ is given by:$$\Huge f(x)=\sum_{n=0}^\infty\frac{f^{(n)}(a)}{k!}(x-a)^n$$
The $n$th order Taylor polynomial is obtained by taking the first $n+1$ terms of the Taylor series, including zero terms.

# Lagrange form of the remainder:

There exists a more convenient expression for the remainder function from Taylor's theorem. This is called the Lagrange form of the remainder, given by:$$\Huge R_n(x)=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}\,\,\text{for some}\,\,c\in(a,x)$$
The proof of this requires the following lemma: Let $h(t)$ be a differentiable function $n+1$ times on the interval $[a,x]$ with $h^{(k)}(a)=0$ for $0\leq k\leq n$ and $h(x)=0$. Then $\exists c\in(a,x):h^{(n+1)}(c)=0$.

[[EVT, MVT, boundedness and monotonicity#Rolle's Theorem|Rolle's theorem]] can be used since $h(a)=h(x)=0$, so $\exists c_1\in(a,x)$ such that $h'(c_1)=0$. Now we can use the theorem again, because we have $h'(a)=h'(c_1)=0$, so $\exists c_1\in(a,c_1)$ such that $h''(c_2)=0$. This can be applied a total of $n$ times, so we finally get that $h^{(n)}(a)=h^{(n)}(c_n)=0$ so $\exists c_{n+1}\in(a,c_n)$ such that $h^{(n+1)}(c_{n+1})=0$. We claim that $c_{n+1}=c$, the original constant used in the Lagrange form of the remainder.

Using a similar argument to the [[EVT, MVT, boundedness and monotonicity#Mean Value Theorem|mean value theorem]], we state:$$\Huge h(t)=(f(t)-P_n(t))(x-a)^{n+1}-(f(x)-P_n(x))(t-a)^{n+1}$$
We have $h(x)=0$. Since $P_n(t)=\sum_{k=0}^n\frac{f^{(k)}(0)}{k!}(t-a)^k$, then $P_n(a)=f(a)+0+0+\dots$. Similarly, $P_n'(a)=f'(a)$ and more generally since $\frac{d^k}{dt^k}(t-a)^n$ evaluated at $t=a$ will always equal $0$, also $\frac{d^n}{dt^n}(t-a)^n$ evaluated at $t=a$ will equal $n!$, then $P_n^{(k)}(a)=f^{(k)}(a)$ for $0\leq k\leq n$. Therefore, $h^{(k)}(a)=0$. Now we can apply the lemma defined above, that is $\exists c\in(a,x):h^{(n+1)}(c)=0$. Note that $P_n^{(n+1)}(t)=0$, since this function is degree $n$, whereas $n+1$ derivatives are being taken. Also, $\frac{d^{n+1}}{dt^{n+1}}(t-a)^{n+1}=(n+1)!$:$$\Huge 0=h^{(n+1)}(c)=f^{(n+1)}(c)(x-a)^{n+1}-(f(x)-P_n(x))(n+1)!$$
Rearranging, we get:$$\Huge f(x)=P_n(x)+\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$As required.

The Lagrange form of the remained is useful for putting an upper bound on the error of a Taylor polynomial approximation to a function. Suppose that:$$\Huge |f^{(n+1)}(t)|\leq M\,\,\forall t\in[a,x],\,\,\text{then:}$$$$\Huge |R_n(x)|=\left|\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}\right|\leq\frac{M|x-a|^{n+1}}{(n+1)!}$$The significance of the absolute value signs indicates the absolute error of the function. This provides a bound on the error.

# Calculating limits using Taylor series:

Let $n\in\mathbb N_0$, we say that $f(x)=o(x^n)$ if $\lim_{x\to0}\frac{f(x)}{x^n}=0$. In particular, for any constant $\alpha\neq0$, $\alpha x^m=o(x^n)\iff m>n$.

If we know that a Taylor series is valid on a given interval, then it may be useful in calculating certain limits. For example, the two most important trigonometric limits can be calculated in this way:
$$ \lim_{x\to 0}\frac{\sin x}{x}=\lim_{x\to0}\frac{x-\frac{x^3}{3!}+o(x^4)}{x}=\lim_{x\to0}\left(1-\frac{x^2}{3!}+o(x^3)\right)=\lim_{x\to0}(1+o(x))=1+\lim_{x\to0}o(x)=1$$$$\large \lim_{x\to0}\frac{1-\cos x}{x}=\lim_{x\to0}\frac{1-1+\frac{x^2}{2!}+o(x^3)}{x}=\lim_{x\to0}\left(\frac{x}{2!}+o(x^2)\right)=\lim_{x\to0}o(x)=0$$