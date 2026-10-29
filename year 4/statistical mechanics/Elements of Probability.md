
# Definitions/Axioms:

A random variable $X$ takes values in $\mathcal{S}$, the set of possible outcomes. This set can be either discrete or continuous. Consider a single random variable, with $X\in\Re=\mathcal{S}$. We then define the probability density by$$\huge\text{Prob}(X\in[x,x+dx])=p(x)dx$$, where $p(x)$ full characterises the distribution. $p$ should always be positive and integral normalised $\int_\Re p(x)=1$. We can then define probability an expectation values:$$\Large\begin{aligned}
\text{prob}(X\in[a,b])&=\int_a^bp(x)dx\\
\langle F(X)\rangle&=\int p(x)F(x)dx
\end{aligned}$$$F(X)$ is therefore also a random variable, with its own measure:$$\Large\text{prob}(F(X)\in[f,f+df])=p_F(f)df$$We can calculate this measure from the underlying PDF for $x$. Consider the solutions $x_i$ to $F(x_i)=f$:$$\Large p_F(f)df=\sum_Ip(x_i)dx\implies p_F(f)=\sum_i p(x_i)\left|\frac{dx}{dF}\right|_{x=x_i}$$Note the derivative terms in the sum are just the Jacobians associated with a change of variable $x\to f$.