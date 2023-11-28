
# Taylor's theorem:

Taylor's theorem states that if a $f(x)$ has $n+1$ continuous [[Derivative as a limit#Differentiability|derivatives]] in an open interval $I$, containing the point $x=a$, then $\forall x$ in that interval:$$\Huge f(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n(x)$$
Where:$$\Huge R_n(x)=\frac{1}{n!}\int_a^x(x-t)^nf^{(n+1)}(t)dt$$
$R_n$ is known as the remainder. Proof:
![[taylor series proof]]

# Taylor polynomials:

The combination $P_n(x)=f(x)-R_n(x)$ is a polynomial in $x$ of degree $n$, called the $n$th order tayl