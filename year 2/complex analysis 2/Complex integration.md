
Given the notion of [[Complex differentiation]], it is natural to look for a notion of the opposite. On $\Re$, there was only one path from $a$ to $b$. In $\mathbb{C}$ there are infinitely many paths between two points.

Consider a continuous function $f:[a,b]\mapsto\mathbb{C}$ where $[a,b]\subset\Re$:$$\Huge \int_a^bf(t)dt=\int _a^b\Re(f(t))+i\Im(f(t))dt=\int_a^b\Re(f(t))dt+i\int_a^b\Im(f(t))dt$$Take $f(t)=t+it$ on $[0,1]$ as example:$$\Huge \int_0^1(t+it)dt=\int_0^1tdt+i\int_0^1tdt=\frac{1+i}{2}$$Writing $f_1=u_1+iv_1$ and $f_2=u_2+iv_2$, one can show that:
>$$\Huge\int_a^bf_1(t)+f_2(t)dt=\int_a^bf_1(t)dt+\int_a^bf_2(t)dt$$
>$$\Huge \int_a^bcf(t)dt=c\int_a^bf(t)dt$$

These can be proven by using the definition of the integral and linearity on $\Re$. 