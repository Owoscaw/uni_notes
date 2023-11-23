Generating functions encode combinatorial information in an analytical form. For example, the binomial theorem encodes counting information:$$\Huge {n\choose0},{n\choose1},\dots,{n\choose n}\mapsto(1+x)^n$$

Let $a_0,a_1,a_2,\dots$ be a sequence of numbers. The ordinary generating function for the sequence is the formal sum:$$\Huge f(x)=\sum_{k=0}^\infty a_kx^k$$
Since this is discrete mathematics, we do not care if this series converges and can manipulate it however we need to, this is why it is called a formal sum.

Example:![[7 into 4 example]]
Now to generalise this, consider the amount of solutions to the equation:$$\Huge e_1+e_2+\dots+e_n=k$$
Where $e_i\in\{0,1\}$ and $n,k\in\mathbb{N}_0$. Note that each $e_i$ corresponds to $(x^0+x^1)$, then we take:$$\Huge f(x)=(1+x)\cdot(1+x)\dots(1+x)=(1+x)^n=\sum_{k=0}^n{n\choose k}x^k$$
Each $x^k$ corresponds to a choice of $x^{e_1}$ from the first bracket, $x^{e_2}$ from the second, and so forth such that the total power is $e_1+\dots+e_n=k$. So the coefficient of $x^k$ is the number of solutions to the original equation. This is given by $n$ choose $k$.

For an integer $n\geq0$:$$\Huge \sum_{k=0}^nx^k=\frac{1-x^{n+1}}{1-x},\,\,\,\sum_{k=0}^\infty x^k=\frac{1}{1-x}$$$$\Huge \sum_{k=0}^\infty {n+k-1\choose k}x^k=\frac{1}{(x+1)^n}$$
The first formulae come from writing the sum as $\sum_{k=0}^\infty x^k=1+x\sum_{k=0}^\infty x^k$, then solving for the sum. The second comes from the [[Arrangements and Combinations with repetitions#Extended binomial coefficients|extended binomial coefficients]]. If $f(x)=\sum_{k=0}^\infty a_kx^k$ and $g(x)=\sum_{k=0}^\infty b_kx^k$ are generating functions of two sequences, then:$$\Huge \sum_{k=0}^\infty c_kx^k$$

Considering the number of solutions 