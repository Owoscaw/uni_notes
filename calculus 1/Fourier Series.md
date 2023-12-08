Consider a function $f(x)$ with period $2L$ given on the interval $(-L,L)$. The functions $\cos(\frac{n\pi x}{L})$ and $\sin(\frac{n\pi x}{L})$ are also periodic with $2L$, for any $n\in\mathbb N$. Constant functions are trivially periodic, so a sum of a constant function and functions of form defined above will also be periodic with $2L$. So we can express $f(x)$ as:$$\Huge f(x)=\frac{a_0}{2}+\sum_{n=1}^\infty a_n\cos{\frac{n\pi x}{L}}+b_n\sin{\frac{n\pi x}{L}}$$
Where $a_0, a_n, b_n$ are the Fourier coefficients of $f(x)$. If this sum converges, it is called the Fourier series of $f(x)$. In general, an infinite number of coefficients may be non-zero, which need to be determined from $f(x)$. For positive integers $m,n$:
>$\displaystyle{\int_{-L}^L\cos{\frac{n\pi x}{L}}dx}=0$
>$\displaystyle{\int_{-L}^L\sin{\frac{n\pi x}{L}}dx}=0$
>$\displaystyle{\int_{-L}^L\cos{\frac{m\pi x}{L}}\sin{\frac{n\pi x}{L}}dx}=0$
>$\displaystyle{\frac{1}{L}\int_{-L}^L\cos{\frac{m\pi x}{L}}\cos{\frac{n\pi x}{L}}dx=\begin{cases}0&\text{if}&m\neq n\\1&\text{if}&m=n\end{cases}}$
>$\displaystyle{\frac{1}{L}\int_{-L}^L\sin{\frac{m\pi x}{L}}\sin{\frac{n\pi x}{L}}dx=\begin{cases}0&\text{if}&m\neq n\\1&\text{if}&m=n\end{cases}}$

It is convenient to write the RHS of the last two results as the [[Matrix definition#Special matrices|Kronecker delta]] function, defined as:$$\Huge \delta_{mn}=\begin{cases}0&\text{if}&m\neq n\\1&\text{if}&m=n\end{cases}$$The proof for the first result comes from the fact that $\sin$ is $0$ at integer multiples of $\pi$. The second and third result are integrals of odd functions over a symmetric interval, so it is obvious that they integrate to $0$. Recall that $\cos{(x\pm y)}=\cos x\cos y\mp\sin x\sin y$, so $\cos{(x+y)}+\cos{(x-y)}=2\cos x\cos y$. Then the fourth result can be written as:$$\small \frac{1}{2L}\int_{-L}^L\cos{\frac{(m+n)\pi x}{L}+\cos{\frac{(m-n)\pi x}{L}}}dx=\frac{1}{2L}\left[\frac{L}{(m+n)\pi}\sin\frac{(m+n)\pi x}{L}+\frac{L}{(m-n)\pi}\sin{\frac{(m-n)\pi x}{L}}\right]_{-L}^L$$This is assuming that $m\neq n$, as we are dividing by $m-n$. This will result in $0$ as $\sin$ is $0$ at integer multiples of $\pi$. Note if $m=n$, there is a $\cos^2$ term in the integrand, resulting in a $\sin$ term and $x$ term in the resulting integral. This finally gives $\frac{L}{2L}-\left(\frac{(-L)}{2L}\right)=1$. The proof for the fifth result is similar.

We say that the set $\left\{1,\cos{\frac{n\pi x}{L}}, \sin{\frac{n\pi x}{L}}\right\}$ form an orthogonal set on $[-L,L]$ because if $\phi,\psi$ are $2$ different function from that set, then we have:$$\Huge \frac{1}{L}\int_{-L}^L\phi(x)\psi(x)dx=0$$These identities can be used to determine the Fourier coefficients. By integrating $f(x)$:$$\large \frac{1}{L}\int_{-L}^Lf(x)dx=\frac{1}{L}\int_{-L}^L\frac{a_0}{2}+\sum_{n=1}^\infty a_n\cos\frac{n\pi x}{L}+b_n\sin{\frac{n\pi x}{L}}dx=\frac{1}{L}\cdot\frac{2a_0 L}{2}=a_0$$Since by the above results, the terms in the summand will integrate to $0$. Then when we let $m>0$:$$\large\frac{1}{L}\int_{-L}^Lf(x)\cos{\frac{m\pi x}{L}}dx=\frac{1}{L}\int_{-L}^L\left(\frac{a_0}{2}+\sum_{n=1}^\infty a_n\cos{\frac{n\pi x}{L}+b_n\sin{\frac{n\pi x}{L}}}\right)\cos{\frac{m\pi x}{L}}$$Using above results, this integral is equal to the following:$$\Huge \sum_{n=1}^\infty a_n\delta_{mn}=a_m$$Therefore we have an expression for the $n$th Fourier coefficient:$$\Huge a_n=\frac{1}{2}\int_{-L}^Lf(x)\cos{\frac{n\pi x}{L}}dx$$
Similarly, consider:1L∫−LLf(x)sin⁡mπxLdx=1L∫−LL(a02+∑n=1∞ancos⁡nπxL+bnsin⁡nπxL)sin⁡mπxL=∑n=1∞bnδmn=bmTherefore we get the other coefficient with:bn=1L∫−LLf(x)sin⁡nπxL

For example, consider $f(x)=|x|$ for $-1<x<1$ with $f(x+2)=f(x)$:
![[sawtooth signal example]]Here, every $b_n$ was $0$. This happens when $f(x)$ is even on $(-L,L)$. In this case, the Fourier series only consists of cosine terms, so the series is called a cosine series. Similarly, if $f(x)$ is an odd function on $(-L,L)$ then the Fourier series only consists of sine terms, so the series is called a sine series.

# Partial sum:

To show that the Fourier series approaches $f(x)$, we define the partial sum as:Sm(x)=a02+∑n=1mancos⁡nπxL+bnsin⁡nπxL
As more terms are included in the partial sum, the Fourier series becomes an increasingly accurate approximation to $f(x)$ on $(-L,L)$. However at jump discontinuity points, the Fourier series converges to the midpoint of the jump. This leads to Dirichlet's theorem:

# Dirichlet's Theorem:

Let $f(x)$ be a periodic function with period $2L$ such that on the interval $(-L,L)$ it has a finite number of [[EVT, MVT, boundedness and monotonicity#Extreme value theorem|extreme values]], a finite number of [[Limits and Continuity#Classification of discontinuities|jump discontinuities]] and $|f(x)|$ is integrable on $(-L,L)$, then it's Fourier series converges for all values of $x$ where $f(x)$ is continuous and if $x=a$ is a jump discontinuity then it converges to:$$\Huge \frac{1}{2}\lim_{x\to a^-}f(x)+\frac{1}{2}\lim_{x\to a^+}f(x)$$That is, it converges to the midpoint of the jump.

# Parseval's Theorem:

If $f(x)$ is a function of period $2L$ with Fourier coefficients $a_n,b_n$ then:$$\Huge \frac{1}{2L}\int_{-L}^Lf(x)^2dx=\frac{a_0^2}{4}+\frac{1}{2}\sum_{n=1}^\infty(a_n^2+b_n^2)$$
Proven as follows:
![[Parsevals theorem proof]]

This can be used to find the value of certain infinite sums, for example:![[Parsevals example]]
# Half-range Fourier series:

If a function is defined on only $(0,L)$, a different Fourier series can be found that still converges to $f(x)$ on $(0,L)$. We can obtain $f$'s '