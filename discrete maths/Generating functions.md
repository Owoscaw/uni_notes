Generating functions encode combinatorial information in an analytical form. For example, the binomial theorem encodes counting information:$$\Huge {n\choose0},{n\choose1},\dots,{n\choose n}\mapsto(1+x)^n$$

Let $a_0,a_1,a_2,\dots$ be a sequence of numbers. The ordinary generating function for the sequence is the formal sum:$$\Huge f(x)=\sum_{k=0}^\infty a_kx^k$$
Since this is discrete mathematics, we do not care if this series converges and can manipulate it however we need to, this is why it is called a formal sum.

Example:![[7 into 4 example]]
Now to generalise this, consider the amount of solutions to the equation:$$\Huge e_1+e_2+\dots+e_n=k$$
Where $e_i\in\{0,1\}$ and $n,k\in\mathbb{N}_0$. Note that each $e_i$ corresponds to $(x^0+x^1)$, then we take:$$\Huge f(x)=(1+x)\cdot(1+x)\dots(1+x)=(1+x)^n=\sum_{k=0}^n{n\choose k}x^k$$
Each $x^k$ corresponds to a choice of $x^{e_1}$ from the first bracket, $x^{e_2}$ from the second, and so forth such that the total power is $e_1+\dots+e_n=k$. So the coefficient of $x^k$ is the number of solutions to the original equation. This is given by $n$ choose $k$.

For an integer $n\geq0$:$$\Huge \sum_{k=0}^nx^k=\frac{1-x^{n+1}}{1-x},\,\,\,\sum_{k=0}^\infty x^k=\frac{1}{1-x}$$$$\Huge \sum_{k=0}^\infty {n+k-1\choose k}x^k=\frac{1}{(1-x)^n}$$
The first formulae come from writing the sum as $\sum_{k=0}^\infty x^k=1+x\sum_{k=0}^\infty x^k$, then solving for the sum. The second comes from the [[Arrangements and Combinations with repetitions#Extended binomial coefficients|extended binomial coefficients]]. If $f(x)=\sum_{k=0}^\infty a_kx^k$ and $g(x)=\sum_{k=0}^\infty b_kx^k$ are generating functions of two sequences, then:$$\Huge f(x)g(x)=\sum_{k=0}^\infty c_kx^k$$
These can be used to simplify generating functions into a more compact form, where coefficients of powers can be found easier.

# [[Recurrence relations]] and generating functions:

Generating functions are often used to solve recurrence relations. The generating function for $(a_n)$ can be written as $\sum_{n=0}^\infty a_nx^n$. $a_n$ is substituted for the given recurrence formula. For example, if the first $N$ initial conditions are given, then the recurrence relation can be given by:$$\Huge f(x)=a_0+a_1x+\dots+a_Nx^N+\sum_{n=N}^\infty a_nx^n$$
Assume the relation $a_n=b_0a_{n-1}+b_1a_{n-2}+\dots+b_ka_{n-k}$ is given, then the sum becomes:$$\large \sum_{n=N}^\infty a_nx^n=\sum_{n=N}^\infty (b_0a_{n-1}+\dots+b_ka_{n-k})x_n=b_0\sum_{n=N}^\infty a_{n-1}x^n+\dots+b_k\sum_{n=N}^\infty a_{n-k}x^n$$
The powers and indexes of each term can be made equal by factoring powers of $x$ the sum to make it in the form:$$\Huge \sum_{n=N}^\infty a_nx^n=b_1x\sum_{n=N}^\infty a_{n-1}x^{n-1}+\dots+b_kx^k\sum_{n=N}^\infty a_{n-k}x^{n-k}$$
This sum can be further manipulated to make each summand $a_nx^n$:$$\Huge \sum_{n=N}^\infty a_nx^n=b_1x\sum_{n=N-1}^\infty a_nx^n+\dots+b_kx^k\sum_{n=N-k}^\infty a_nx^n$$
If $k=N$, then the last term is in the appropriate form of $f(x)$, if not then further manipulation needs to occur to make each sum in the correct form:$$\Huge \sum_{n=N-i}^\infty a_nx^n=\sum_{n=0}^\infty a_nx^n -\sum_{n=0}^{N-i-1}a_nx^n=f(x)-\sum_{n=0}^{N-i-1}a_nx^n$$
Finally substituting this back into the original relation gives:$$\Huge f(x)=a_0+\dots+a_Nx^N+\left(b_1x\sum_{n=N-1}^\infty a_nx^n+\dots+b_kx^k\sum_{n=N-k}^\infty a_nx^n\right)$$$$\large f(x)=a_0+\dots+a_Nx^N+\left(b_1xf(x)-b_1x\sum_{n=0}^{N-2}a_nx^n+\dots+b_kx^kf(x)-b_kx^k\sum_{n=0}^{N-k-1}a_nx^n\right)$$$$\Huge f(x)=a_0+\dots+a_Nx^N+(b_1x+\dots+b_kx^k)f(x)-\sum_{n=1}^kb_kx^k\sum_{m=1}^{N-n-1}a_mx^m$$
Rearranging to solve $f(x)$ gives:$$\Huge f(x)(1-b_1x-\dots-b_kx^k)=a_0+\dots+a_Nx^N-\sum_{n=1}^kb_kx^k\sum_{n=m}^{N-n-1}a_mx^m$$$$\Huge f(x)=\frac{\sum_{n=0}^Na_nx^n-\sum_{n=1}^kb_kx^k\sum_{m=1}^{N-n-1}a_mx^m}{1-\sum_{n=1}^kb_kx^k}$$
This expands to a generating function, that can be used to solve the recurrence relation.