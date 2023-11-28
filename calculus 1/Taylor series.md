
# Taylor's theorem:

Taylor's theorem states that if a $f(x)$ has $n+1$ continuous [[Derivative as a limit#Differentiability|derivatives]] in an open interval $I$, containing the point $x=a$, then $\forall x$ in that interval:$$\Huge f(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n(x)$$
Where:$$\Huge R_n(x)=\frac{1}{n!}\int_a^x(x-t)^nf^{(n+1)}(t)dt$$
$R_n$ is known as the remainder. Proof:
![[taylor series proof]]

# Taylor polynomials:

The combination $P_n(x)=f(x)-R_n(x)$ is a polynomial in $x$ of degree $n$, called the $n$th order Taylor polynomial of $f(x)$ at the point $x=a$:$$\Huge P_n(x)=f(a)+f'(a)(x-a)+\frac{f''(a)}{2}(x-a)^2+\dots+\frac{f^{(n)}(a)}{n!}(x-a)^n$$
If $x=a$ is omitted, assume $x=0$. This is called the Maclaurin series. The Taylor polynomial is an approximation to $f(x)$, which tends to be a good approximation for $x$ sufficiently close to $a$. As $n$ increases, the quality of the approximation also increases. The remainder function $R_n$ gives an exact expression for the remainder in the approximation.