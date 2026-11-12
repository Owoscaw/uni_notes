
# Definitions/Axioms:

A random variable $X$ takes values in $\mathcal{S}$, the set of possible outcomes. This set can be either discrete or continuous. Consider a single random variable, with $X\in\Re=\mathcal{S}$. We then define the probability density by$$\huge\text{Prob}(X\in[x,x+dx])=p(x)dx$$, where $p(x)$ full characterises the distribution. $p$ should always be positive and integral normalised $\int_\Re p(x)=1$:
> We can then define probability an expectation values:$$\Large\begin{aligned}
\text{prob}(X\in[a,b])&=\int_a^bp(x)dx\\
\langle F(X)\rangle&=\int p(x)F(x)dx
\end{aligned}$$$F(X)$ is therefore also a random variable, with its own measure:$$\Large\text{prob}(F(X)\in[f,f+df])=p_F(f)df$$We can calculate this measure from the underlying PDF for $x$. Consider the solutions $x_i$ to $F(x_i)=f$:$$\Large p_F(f)df=\sum_Ip(x_i)dx\implies p_F(f)=\sum_i p(x_i)\left|\frac{dx}{dF}\right|_{x=x_i}$$Note the derivative terms in the sum are just the Jacobians associated with a change of variable $x\to f$. 
> We can also define the $n$-th moment of a random variable $x$ as the expectation of $x^n$:$$\Large m_n=\langle x^n\rangle=\int p(x)x^ndx$$
> The characteristic function $\tilde p(k)$ is also defined through the expectation value$$\Large \tilde p(k)=\langle e^{-ikx}\rangle=\int p(x)e^{-ikx}dx$$and can be thought of as the Fourier transform of $p(x)$. Notably, we can easily invert the Fourier transform to recover the original distribution from the characteristic function:$$\Large p(x)=\frac{1}{2\pi}\int\tilde p(k)e^{ikx}dk$$Writing the exponential in summation form, we see that the characteristic function can be expanded to provide moments:$$\Large\tilde p(k)=\int p(x)\sum_{n=0}^\infty\frac{(-ik)^n}{n!}x^ndx=\sum_{n=0}^\infty\frac{(-ik)^n}{n!}\langle x^n\rangle$$
> Cumulant generating functions are defined as the logarithm of characteristic functions. These functions generate cumulants $\langle x^n\rangle_c$ when expanded in powers of $k$. We define cumulants through the following:$$\Large\log\tilde p(k)=\sum_{n=1}^\infty\frac{(-ik)^n}{n!}\langle x^n\rangle_c$$These contain a lot of useful information about the distribution. The information from moments is actually the same as those in cumulants. Explicitly taking the logarithm$$\Large
\log\tilde p(k)=\log\left(\sum_{n=0}^\infty\frac{(-ik)^n}{n!}\langle x^n\rangle\right)$$, one can use the expansion for $\log(1+\epsilon)$ and equation terms to find:$$\Large\begin{aligned}
\langle x\rangle_c&=\langle x\rangle&\text{mean}\\
\langle x^2\rangle_c&=\langle x^2\rangle-\langle x\rangle^2&\text{variance }\sigma^2\\
\langle x^3\rangle_c&=\langle x^3\rangle-3\langle x^2\rangle\langle x\rangle+2\langle x\rangle^3&\text{skewness}
\end{aligned}$$

# Notable distributions:

## Gaussian:
The normal, or Gaussian, distribution for a single continuous variable $x$ is defined as:$$\Large p(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\lambda)^2}{2\sigma^2}\right)$$This is the bell curve, with mean $\lambda$ and width $\sigma$. More precisely, let us calculate the characteristic function:$$\Large\begin{aligned}
\tilde p(k)&=\int\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-ikx-\frac{(x-\lambda)^2}{2\sigma^2}\right)dx\\
_\text{completing the square}&=\int\frac{1}{\sigma\sqrt{2\pi}}\exp\left(\frac{(x-\lambda-ik\sigma^2)^2}{2\sigma^2}-\frac{\sigma^2k^2}{2}-ik\lambda\right)dx\\
_{\text{shift in }x\text{, normalise}}&=\exp\left(-\frac{k^2\sigma^2}{2}-ik\lambda\right)
\end{aligned}$$Let us also compute the cumulants:$$\Large\begin{aligned}
\log\tilde p(k)&=-ik\langle x\rangle_c-\frac{k^2}{2}\langle x^2\rangle_c+\dots\\
&=-ik\lambda-\frac{k^2}{2}\sigma^2\\
\implies\langle x\rangle_c&=\lambda\,\,\text{ mean}\\
\implies  \langle x^2\rangle_c&=\sigma^2\,\,\text{ variance}\\
\implies  \langle x^n\rangle_c&=0\,\,\text{ for }n>2
\end{aligned}$$Note that higher order moments do not vanish for the Gaussian distribution. For $X_i$ independent randomly distributed variables each with mean $\mu$ and variance $\sigma^2$, the [[Inference#The central limit theorem|Central Limit theorem]] dictates:$$\huge \sum_{i=1}^N X_i\to_{N\to\infty}\sim N(\mu,\sigma^2)$$
## Binomial:
Consider a random variable with two discrete outcomes, $S=\{A,B\},P(X=A)=p,P(X=B)=1-p$. Over $N$ trials, we ask what the probability of getting $N_A$ of outcome $A$:$$\Large\begin{aligned}
N_A&\in\{0,\dots, N\}\\
\implies p_N(N_A) &= {N\choose N_A}p^{N_A}(1-p)^{N-N_A}
\end{aligned}$$Note that this is not technically a PDF, as the outcomes are discrete. To show this is properly normalised:$$\Large\begin{aligned}
\sum_{N_A=0}^Np_N(N_A)&=\sum_{N_A=0}^N{N\choose N_A}p^{N_A}(1-p)^{N-N_A}\\
&=(p+(1-p))^N\\
&=1^N=1
\end{aligned}$$Now let us compute the characteristic function. Due to the discreteness of this distribution, we write:$$\Large\begin{aligned}
\tilde p_N(k)&=\langle e^{-ikN_A}\rangle\\
&=\sum_{N_A=0}^Np_N(N_A)e^{-ikN_A}\\
&=\sum_{N_A=0}^N{N\choose N_A}(1-p)^{1-N_A}(pe^{-ik})^{N_A}\\
&=(pe^{-ik}+1-p)^N
\end{aligned}$$Continuing to write the cumulants:$$\Large\begin{aligned}
\log\tilde p(k)&=N\log(pe^{-ik}+1-p)\\
&=N\log\tilde p_1(k)\\
\implies  \langle x^m\rangle_c\text{ for }N&=N  \langle x^m\rangle_c\text{ for }1
\end{aligned}$$Therefore let us proceed by finding cumulants for $N=1$:$$\Large\begin{aligned}
 \langle x^m\rangle&=p\cdot 1^m+(1-p)\cdot 0^m\\
&=p\\
\implies  \langle x\rangle_c&=\langle x\rangle =p\\
\implies  \langle x^2\rangle_c&=\langle x^2\rangle-\langle x\rangle^2=p-p^2\\
&=p(1-p)\\
\implies_{\text{for }N} \langle x\rangle_c&=Np\\
 \langle x^2\rangle_c&=Np(1-p)
\end{aligned}$$
# Many random variables:

We want to build probability distributions over all particles in a gas, i.e. for $N$ random variables. Consider an $N$ dimensional space of outcomes$$\Large \mathcal{S}_\underline{x}=\{\underline{x}=(x_1,\dots,x_N)\in\Re^N\}$$where we define a joint probability density $p(\underline{x})$, defined as$$\Large\text{prob}(X_i\in[x_i,x_i+dx_i]\forall i\in1,\dots,N)=p(\underline{x})d^Nx$$where $d^Nx=\prod_{i=1}^N dx_i$. The joint probability density is normalised by construction. There are two ways to look at specific subsets of variables:
> We introduce the unconditional probability density, the probability for a set of random variables $(X_1,\dots,X_m)$ regardless of the value of the other variables $(X_{m+1},\dots,X_N)$:$$\Large p(x_1,\dots,x_m)=\int\prod_{i=m+1}^Ndx_ip(x_1,\dots,x_N)$$
> The other way to do this is the conditional probability density. This is the probability density for a subset of random variables $(X_1,\dots,X_m)$ given the value of the other other variables $(X_{m+1},\dots,X_N)$. This must be properly normalised, one can check the appropriate normalisation factor is the unconditional probability density for the variables held fixed:$$\Large p(x_1,\dots,x_m|x_{m+1},\dots,x_N)=\frac{p(x_1,\dots,x_m,x_{m+1},\dots,x_N)}{p(x_{m+1},\dots,x_N)}$$

Note if all variables are independent, the joint probability density reduces into a produce of single-variable densities:$$\huge p(\underline{x})=\prod_{i=1}^Np_i(x_i)$$We can also define the joint characteristic function, which is now a multidimensional Fourier transform:$$\Large\tilde p(\underline{k})=\langle e^{-i\sum_ik_iX_i}\rangle=\langle e^{-i\underline{k}\cdot\underline{X}}\rangle$$We can find cumulants by looking at the expansion of the logarithm of this for each equation. To strip these powers out, we can take $k$ derivatives:
> We therefore define the joint moments as:$$\Large\langle X_1^{n_1}\dots X_N^{n_N}\rangle=\left(i\frac{\partial }{\partial k_1}\right)^{n_1}\dots\left(i\frac{\partial }{\partial k_N}\right)^{n_N}\tilde p(\underline{k})|_{\underline{k}=0}$$As well as the joint cumulants:$$\Large\langle X_1^{n_1}\dots X_N^{n_N}\rangle_c=\left(i\frac{\partial }{\partial k_1}\right)^{n_1}\dots\left(i\frac{\partial }{\partial k_N}\right)^{n_N}\log\tilde p(\underline{k})|_{\underline{k}=0}$$

It is straightforward to see that if two random variables $X_1,X_2$ are independent, their mixed cumulant will vanish:$$\huge\langle X_1,X_2\rangle_c=0$$
# The random walk:

Consider a particle at $x=0$ that takes a series of steps, each with length $a$ either left or right with probability $1/2$. We ask what the probability distribution is for the walker's net displacement after $N$ steps. Say the displacement at each step is given by a random variable $s_i$ with PDF $w(s_i)$, which will be the same at each step. The distribution above is therefore:$$\Large w(s)=\frac{1}{2}\delta(s-a)+\frac{1}{2}\delta(s+a)$$We wish to calculate the net displacement$$\huge X=\sum_{i=1}^Ns_i$$, which we do in two different ways:

## Exact solution:
Let us write the joint PDF for $X$ and $s_i$ for each $i$:$$\Large p(X,s_1,\dots,s_N)=\delta\left(X-\sum_{i=1}^Ns_i\right)\prod_{i=1}^Nw(s_i)$$To show this is correct, let us compute the unconditional PDF for the $\{s_i\}$, which we obtain by integrating over $X$:$$\Large\int dXp(X,s_1,\dots,s_N)=\prod_{i=1}^Nw(s_i)$$This is exactly what we expect, the joint PDF of a collection of independent random variables is the product of the individual PDFs. We introduce the delta function to force $X$ to take the value we want. We are interested in the unconditional PDF for the random variable $X$, which we find by integrating over the individual steps $s_i$:$$\Large\begin{aligned}
p(X)&=\int\prod_{i=1}^N(ds_i\,w(s_i))\delta\left(X-\sum_{i=1}^Ns_i\right)\\
\implies\tilde p(k)&=\int dX\,e^{-ikX}\int\prod_{i=1}^N(ds_i\,w(s_i))\delta\left(X-\sum_{i=1}^Ns_i\right)\\
&=\int\prod_{i=1}^N(ds_i\,w(s_i))e^{ik \sum_{i=1}^Ns_i}\\
&=\prod_{i=1}^N\int ds_i\,w(s_i)e^{ik\sum_{i=1}^Ns_i}\\
&=\left(\int ds_i\,w(s_i)
e^{ik\sum_{i=1}^Ns_i}\right)^N\end{aligned}$$Where we used the delta function definition to integrate over $X$, note this is just $N$ copies of the integral for $\tilde w(s_i)$:$$\Large\implies\tilde p(k)=\tilde w(k)^M\,\,p(X)=\int\frac{dk}{2\pi}e^{ikX}\tilde w(k)^N$$This gives us a procedure to answer the question, simply raise the characteristic function to the $N$th power and inverse Fourier transform:$$\Large\begin{aligned}
\tilde w(k)&=\int_{-\infty}^\infty dx\,e^{-ikx}\left(\frac{1}{2}\delta\left(x-a\right)+\frac{1}{2}\delta(x+a)\right)\\
&=\frac{1}{2}(e^{ika}+e^{-ika})=\cos(ka)\\
\implies p(x)&=\int\frac{dk}{2\pi}e^{ikx}\tilde p(k)\\
&=\left(\frac{1}{2}\right)^N\int\frac{dk}{2\pi}e^{ikx}(e^{ika}+e^{-ika})^N\\
&=\left(\frac{1}{2}\right)^N\int\frac{dk}{2\pi}e^{ikx}\sum_{j=0}^N{ N\choose j}e^{ijka}e^{-i(N-j)ka}\\
_{\text{using exp }\delta\text{ func defn}}&=\frac{1}{2^N}\sum_{j=0}^N{N\choose j}\delta(x-(2j-N)a)
\end{aligned}$$Noting that the $\delta$ function is only nonzero when $x$ is an integer multiple of $a$.

## Diffusion solution:
Suppose $N$ steps occur in time $T$, where each step takes $\Delta T=T/N$. We rewrite the step length $a$as $a=\Delta X$. We denote the probability distribution at time $T$, location $X$ by $p(T,X)$. Initially, $p(T=0,X)=\delta(X)$. Therefore:$$\Large p(T+\Delta T,X)=\frac{1}{2}(p(T,X+\Delta X)+p(T,X-\Delta X))$$Defining $D=\frac{\Delta X^2}{2\Delta T}$ and subtracting $P(T,X)$ from the above:$$\frac{1}{\Delta T}(p(T+\Delta T,X)-p(T,X))=\frac{D}{\Delta X}\left(\frac{p(T,X+\Delta X)-p(T,X)}{\Delta X}-\frac{p(T,X)-p(T,X-\Delta X)}{\Delta X}\right)$$Taking the limit $\Delta T,\Delta X\to0$, $D$ is held finite and nonzero, we notice that the LHS is simply the partial time derivative of $p$ and that the RHS is the difference of the first space derivative of $p$ over $\Delta x$, the second space derivative:$$\Large \frac{\partial p(T,X)}{\partial T}=D\frac{\partial^2}{\partial X^2}p(T,X)$$This is the diffusion equation, and $D$ is known as the diffusion constant. We have recovered a macroscopic equation from the microscopic steps in the random walk. This easily generalises to higher dimensions by replacing $\frac{\partial^2}{\partial X^2}\to\underline{\nabla}^2$.

Our initial condition $p(0,X)=\delta(X)$ admits a Gaussian ansatz$$\Large p(T,X)=\frac{1}{\sqrt{2\pi}\sigma(T)}\exp\left(-\frac{X^2}{2\sigma(T)^2}\right)$$with mean $0$ and variance $\sigma(T)^2$. We assume all time dependence is contained in the variance. Using this in the diffusion equation gives$$\Large\begin{aligned}
0&=\left(\frac{\partial }{\partial T}-D\frac{\partial^2}{\partial X^2}\right)p(T,X)\\
&=\frac{\exp(-\frac{X^2}{2\sigma(T)^2})}{\sqrt{2\pi}\sigma(T)^5}(X^2-\sigma(T)^2)(\sigma(T)\sigma'(T)-D)
\end{aligned}$$, where the rightmost term must equal zero for this to hold for all $X,T$:$$\Large\begin{aligned}
\implies \sigma(T)\sigma'(T)&=D\\
\iff\sigma(T)^2&=2D(T-T_0)
\end{aligned}$$Where $T_0$ is an integration constant we set to $0$ from our initial condition. We see that variance increases linearly with time:![[Elements of Probability 2026-11-10 17.46.33.excalidraw]]Note we could've guessed this solution through the central limit theorem on our exact binomial solution above.

### Mathematical interlude - Integrals of large exponentials:
Given an integral $$\Large I=\int_{-\infty}^\infty dx\,e^{N\phi(x)}$$, consider the large $N$ limit. This integral converges if $\phi(x)\to-\infty$ as $x\to\pm\infty$, however if $\phi$ is suitably continuous it will have a maximum $\phi(x_\text{max})$. Taylor expanding around this point:$$\Large \phi(x)=\phi(x_\text{max})+\frac{1}{2}\phi''(x_\text{max})(x-x_\text{max})+\dots$$Note the vanishing $\phi'$ term as we are evaluating at a maximum. Changing variables via $x=x_\text{max}+N^{-1/2}y$ we write$$\Large N\phi(x)\approx N\phi(x_\text{max})+\frac{1}{2}\phi''(x_\text{max})y^2+\mathcal{O}(N^{-})$$, so in the large $N$ limit other terms are suppressed. This makes the integral:$$\Large I=N^{-1/2}\int dy\,\exp(N\phi(x_\text{max})-\frac{1}{2}\phi''(x_\text{max})y^2+\dots)$$This is just a standard Gaussian integral (to leading order in $1/N$), which we calculate:$$\Large I=\sqrt{\frac{2\pi}{N|\phi''(x_\text{max})|}}e^{N\phi(x_\text{max})}+\mathcal{O}(N^{-1})$$This is very useful in the large $N$ limit, as these integrals are often tricky to do. There are two possible corrections we could have made to this result:
> Taylor series terms of form $1/N$, coming from fluctuations about $x_\text{max}$.
> Other terms of form $e^{N\phi(x'_\text{max})}$ coming from lower local minima. Note these are exponentially suppressed compared to the terms mentioned above.

Our work here nicely generalises to multidimensional and complex integrals, and is core to much of QFT.

## Stirling's formula:
We can apply this technique to derive Stirling's formula, a useful approximation to the factorial for large values of the argument:$$\Large\ln N!=N\ln N-N+\frac{1}{2}\ln(2\pi N)+\mathcal{O}(N^{-1})\,\,N\to\infty$$We do this by considering the factorial in integral form:
> Consider the more general integral$$\Large\begin{aligned}
I(\alpha)&=\int_0^\infty dx\,x^Ne^{-\alpha x}\\
&=\left(-\frac{d}{d\alpha}\right)^N\int_0^\infty dx\,e^{-\alpha x}\\
&=\left(-\frac{d}{d\alpha}\right)^N\left(\frac{1}{\alpha}\right)=\frac{N!}{\alpha^{N+!}}
\end{aligned}$$which we evaluate at $\alpha=1$ to find:$$\huge N!=\int_0^\infty dx\,x^Ne^{-x}$$

Now to extract Stirling's formula, we write the integral as:$$\Large\begin{aligned}
N!&=\int_0^\infty dx\,\exp\left(N\left(\log x-\frac{x}{N}\right)\right)\\
&=\int dx\,\exp(Nf(x))\\
f(x)&=\log x-\frac{x}{N}\\
f'(x)&=\frac{1}{x}-\frac{1}{N},\,\,f''(x)=-\frac{1}{x^2}
\end{aligned}$$From this we see that $f(x)$ is maximised at $x=N$, so let us Taylor expand the terms in the exponential to rewrite the integrand as:$$\Large\begin{aligned}
N!&=\int dx\exp\left(Nf(N)+\frac{1}{2}Nf''(N)(x-N)^2+\dots\right)\\
&=\exp(N\log N-N)\int dx\,\exp\left(-\frac{1}{2N}(x-N)^2+\dots\right)
\end{aligned}$$This now looks like a Gaussian with $\sigma^2=N$ so let us perform our usual method to find:$$\huge N!=N^Ne^{-N}\sqrt{2\pi N}+\dots$$This is exactly Stirling's formula. Note we were slightly naughty in not justifying that subleading terms were in fact subleading.

## Approximating binomial with a Gaussian:
Now let us apply our integral tricks to show that the binomial distribution to show that it appears as a Gaussian in the appropriate limit. To do this, recall the exact answer for the random walk:$$\Large p_n=\frac{1}{2^N}\frac{N!}{n!(N-n)!}$$Where $n$ is the total steps to the right. To make the symmetry more obvious, define $n=\frac{N}{2}+\frac{m}{2}$ so that $m$ measures total displacement from the origin. Then we have:$$\Large p=\frac{1}{2^N}\frac{N!}{\left(\frac{N}{2}+\frac{m}{2}\right)!\left(\frac{N}{2}-\frac{m}{2}\right)!}$$Now consider Stirling's approximation, working in the limit $N\to\infty$ with $m$ held finite. We work to first nontrivial order in $\frac{m}{N}$ to find:$$\Large\begin{aligned} p&\approx\frac{1}{2^N\sqrt{2\pi}}\frac{N^N\sqrt N}{\left(\frac{N}{2}+\frac{m}{2}\right)^{\frac{N}{2}+\frac{1}{2}}\left(\frac{N}{2}-\frac{m}{2}\right)^{\frac{N}{2}+\frac{1}{2}}}\left(\frac{\frac{N}{2}-\frac{m}{2}}{\frac{N}{2}+\frac{m}{2}}\right)^{\frac{m}{2}}\\
&\approx\frac{1}{2^N\sqrt{2\pi}}\frac{N^N\sqrt{N}}{\left(\frac{N}{2}\right)^{N+1}\left(1+\frac{m}{N}\right)^{\frac{N}{2}+\frac{1}{2}}\left(1-\frac{m}{N}\right)^{\frac{N}{2}+\frac{1}{2}}}\left(\frac{1-\frac{m}{N}}{1+\frac{m}{N}}\right)^{\frac{m}{2}}\\
&\approx\frac{2}{\sqrt{2\pi N}}\left(1-\frac{m^2}{N^2}\right)^{-\frac{N}{2}-\frac{1}{2}}\left(1+\frac{2m}{N}\right)^{-\frac{m}{2}}
\end{aligned}$$Where we used the Taylor expansion $\left(\frac{1+\epsilon}{1-\epsilon}\right)\approx1+2\epsilon+\mathcal{O}(\epsilon^2)$. The next approximations become easier if we take the logarithm if this:$$\begin{aligned}\log p\approx\log\frac{2}{\sqrt{2\pi}}&-\frac{1}{2}\log N-\frac{1}{2}\log\left(1-\frac{m^2}{N^2}\right)\\
&-\frac{N}{2}\log\left(1-\frac{m^2}{N^2}\right)-\frac{m}{2}\log\left(1+\frac{2m}{N}\right)\end{aligned}$$We expand the logarithms to first order ($\log(1+\epsilon)\approx\epsilon$):$$\Large\log p\approx\log\frac{2}{\sqrt{2\pi}}-\frac{1}{2}\log N+\frac{m^2}{2N^2}+\frac{m^2}{2N}-\frac{m^2}{N}$$Now we drop terms of order $N^{-2}$ as well as the $\log N$ term to find:$$\Large\begin{aligned}\log p&\approx\log\frac{2}{\sqrt{2\pi N}}-\frac{m^2}{2N}\\
\implies p&\approx\frac{2}{\sqrt{2\pi N}}\exp\left(-\frac{m^2}{2N}\right)
\end{aligned}$$Fucking hell. We have shown analytically that the binomial distribution looks like a Gaussian if the number of steps is large and we do not go too far from the origin. 