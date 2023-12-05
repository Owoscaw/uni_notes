Consider a function $f(x)$ with period $2L$ given on the interval $(-L,L)$. The functions $\cos(\frac{n\pi x}{L})$ and $\sin(\frac{n\pi x}{L})$ are also periodic with $2L$, for any $n\in\mathbb N$. Constant functions are trivially periodic, so a sum of a constant function and functions of form defined above will also be periodic with $2L$. So we can express $f(x)$ as:$$\Huge f(x)=\frac{a_0}{2}+\sum_{n=1}^\infty a_n\cos{\frac{n\pi x}{L}}+b_n\sin{\frac{n\pi x}{L}}$$
Where $a_0, a_n, b_n$ are the Fourier coefficients of $f(x)$. If this sum converges, it is called the Fourier series of $f(x)$. In general, an infinite number of coefficients may be non-zero, which need to be determined from $f(x)$. For positive integers $m,n$:
>$\displaystyle{\int_{-L}^L\cos{\frac{n\pi x}{L}}dx}=0$
>$\displaystyle{\int_{-L}^L\sin{\frac{n\pi x}{L}}dx}=0$
>$\displaystyle{\int_{-L}^L\cos{\frac{m\pi x}{L}}dx}=0$
>$\displaystyle{\frac{1}{L}\int_{-L}^L\cos{\frac{m\pi x}{L}}\cos{\frac{n\pi x}{L}}dx=\begin{cases}0&\text{if}&m\neq n\\1&\text{if}&m=n\end{cases}}$
>$\displaystyle$