## Indefinite and definite integrals:

### Indefinite:

A function $F(x)$ is called an indefinite integral or anti[[Derivative as a limit|derivative]] of a function $f(x)$ in the interval $(a,b)$ if $F(x)$ is differentiable on that interval with $F^\prime(x)=f(x)$, then we write $F(x)=\int f(x)dx$. If $F(x)$ is an indefinite integral, then so is $F(x)+c$ for any constant $c$, as this will satisfy $F^\prime(x)=f(x)$. If $F_1(x)$ and $F_2(x)$ are both indefinite integrals of $f(x)$, then $F_1(x)-F_2(x)=c$, for any constant $c$.

A function $f(x)$ is integrable in $(a,b)$ if it has an indefinite integral $F(x$) in $(a,b)$ that is [[Limits and Continuity#Continuity|continuous]] in $[a,b]$.

### Definite:

A definite integral of $f(x)$ gives the signed area under the curve of the graph of $f(x)$:
![[signed area]]
This area is defined as the limit of a Riemann sum, by splitting the area into rectangles. If $f(x)$ is continuous and the rectangles are small, the method of summing rectangular areas can become a good approximation. The error can be reduced to zero by taking the limit of the size of the rectangles to zero. This limit exists if it is independent of how the rectangles are constructed to form the approximation.

A subdivision, $S$, of a closed interval $[a,b]$ is a [[Probability definition#Partitions|partition]] into a finite number of sub-intervals, the following would be a subdivision of $[a,b]$:
$$\Huge [x_0,x_1],[x_1,x_2],\dots,[x_{n-1},x_n]$$
Here, $a=x_0<x_1<x_2<\dots<x_{n-1}<x_n=b$. The norm of a subdivision, $|S|$, is the maximum of the sub-interval lengths, $|a-x_1|,|x_1-x_2|,\dots,|x_{n-1}-b|$. The numbers $z_1,z_2,\dots,z_n$ form a set of sample points from $S$ if $z_j\in[x_{j-1},x_j]$ for $j=1,\dots,n$. Now this can be used to define a Reimann sum:

Suppose that $f(x)$ is defined for $x\in[a,b]$. The Reimann sum is:
$$\Huge \mathcal{R}=\sum_{j=1}^n(x_j-x_{j-1})f(z_j)$$
![[Reimann sum example]]
The definite integral is then given in terms of a Reimann sum by taking the limit as $|S|$ tends to zero. This limit exists if it is independent of the subdivision and set of sample points. Let $f(x)$ be defined $\forall\,x\in[a,b]$, the definite integral of $f(x)$ from $a$ to $b$ is then defined as:
$$\Huge \int_a^bf(x)dx=\lim_{|S|\to0}\mathcal{R}$$
It can be shown that this limit exists if $f(x)$ is continuous in $[a,b]$. The above is defined for $a<b$, however can be generalised by defining $\int_b^af(x)dx=-\int_a^bf(x)dx$. This implies $\int_a^af(x)dx=0$. The definite integral satisfies the following properties. Let $f,g$ be integrable in $(a,b)$:
>Linearity of integrals. For $\lambda,\mu\in\Re$, $(\lambda f+\mu g)(x)$ is also integrable in $(a,b)$ with:$$\Huge \int_a^b(\lambda f+\mu g)(x)dx=\lambda\int_a^bf(x)dx+\mu\int_a^bf(x)dx$$
>If $c\in[a,b]$, then:$$\Huge \int_a^bf(x)dx=\int_a^cf(x)dx+\int_c^bf(x)dx$$
>If $f(x)\geq g(x)\,\forall x\in(a,b)$, then:$$\Huge\int_a^bf(x)dx\geq\int_a^bg(x)dx$$
>If $m\leq f(x)\leq M,\,\forall x\in[a,b]$, then:$$\Huge m(b-a)\leq\int_a^bf(x)dx\leq M(b-a)$$

# Fundamental theorem of calculus:

The following theorem (FTOC) connects definite and indefinite integrals. Let $f(x)$ be continuous on $[a,b]$, then:$$\Huge F(x)=\int_a^xf(t)dt$$
This is defined for all $x\in[a,b]$. The theorem states that $F(x)$ is continuous on $[a,b]$, differentiable on $(a,b)$ and is an indefinite integral of $f(x)$ on $(a,b)$:$$\Huge F^{\prime}(x)=\frac{d}{dx}F(x)=\frac{d}{dx}\int_a^xf(t)dt=f(x),\,\forall x\in(a,b)$$
Furthermore, if $\tilde{F}(x)$ is any indefinite integral of $f(x)$ on $(a,b)$, then:$$\Huge \int_a^bf(t)dt=\tilde{F}(b)-\tilde{F}(a)=\left[\tilde{F}(x)\right]_a^b$$ For $a\leq x<x+h<b$, we have:$$\large F(x+h)-F(x)=\int_a^{x+h}f(t)dt-\int_a^xf(t)dt=\int_x^af(t)dt+\int_a^{x+h}f(t)dt$$
Using properties of the integral, this can be written as one integral:$$\Huge \implies F(x+h)-F(x)=\int_x^{x+h}f(t)dt$$
Let $m(h)$ and $M(h)$ denote the minimum and maximum values of $f(x)$ on $[x,x+h]$ respectively. These minimum and maximum must exist by the [[EVT, MVT, boundedness and monotonicity#Extreme value theorem|extreme value theorem]]. Then by another property of the integral:
$$\Huge m(h)\times h\leq\int_x^{x+h}f(t)dt\leq M(h)\times h$$
The two bounds can be thought of as bounding boxes for the area under the curve of the graph of $f(t)$ between $x$ and $x+h$. So we have:
$$\Huge m(h)\leq\frac{\int_x^{x+h}f(t)dt}{h}\leq M(h)\implies m(h)\leq\frac{F(x+h)-F(x)}{h}\leq M(h)$$
Since $f(x)$ is continuous on $[x,x+h]$, then we have:$$\Huge \lim_{h\to0^+}m(h)=\lim_{h\to0^+}M(h)=f(x)$$
By the pinching theorem, we have:
$$\Huge \lim_{h\to0^+}\frac{F(x+h)-F(x)}{h}=F^{\prime}(x)=f(x)$$
There is a similar argument for $\lim_{h\to0^-}$. Putting both of these limits together, we have:$$\Huge F^\prime(x)=\lim_{h\to 0}\frac{F(x+h)-F(x)}{h}=f(x)$$
This shows that $F(x)$ is an indefinite integral of $f(x)$. If $\tilde{F}(x)$ is any indefinite integral of $f(x)$ on $(a,b)$, then $\tilde{F}(x)=F(x)+c$ for some constant $c$, so we get:$$\large \tilde{F}(b)-\tilde{F}(a)=(F(b)+c)-(F(a)+c)=F(b)-F(a)+c-c=F(b)-F(a)$$$$\Huge \tilde{F}(b)-\tilde{F}(a)=F(b)-F(a)=\int_a^bf(t)dt-\int_a^af(t)dt=\int_a^bf(t)dt$$
This theorem also for differentiating a definite integral with respect to it's limits, using:$$\Huge F^\prime(x)=\frac{d}{dx}\int_a^xf(t)dt=f(x)$$
For example:$$\Huge \frac{d}{dx}\int_0^x\frac{1}{1+sin^2t}dt=\frac{1}{1+sin^2x}\times\frac{d}{dx}(x)=\frac{1}{1+sin^2x}$$
$$\Huge \frac{d}{dx}\int_0^{g(x)}f(t)dt=f(g(x))g^\prime(x)$$

# Integration by recurrence relations:

A common way to find integrals related by recurrence relations is when integrating by parts, using the [[Leibniz and Chain rules|Leibniz rule]]:
$$\Huge (f(x)g(x))^\prime=f^\prime(x)g(x)+f(x)g^\prime(x)$$
Integrating over an interval $[a,b]$ and using FOTC:$$\Huge \int_a^b(f(x)g(x))^\prime dx=\int_a^bf^\prime(x)g(x)+f(x)g^\prime(x)dx$$
Rewriting:$$\Huge \int_a^bf^\prime(x)g(x)dx=\left[\left(f(x)g(x)\right)\right]_a^b-\int_a^bf(x)g^\prime(x)dx$$
Which is the integration by parts formula. Consider the following:$$\Huge I_n=\int_0^1x^ne^xdx,\,\forall n\in\mathbb{N}_0$$
Then:$$\Huge I_{n+1}=\int_0^1x^{n+1}e^xdx,\,\text{using integration by parts:}$$$$\large I_{n+1}=\left[x^{n+1}e^x\right]_0^1-\int_0^1(n+1)x^ne^xdx=e-(n+1)\int_0^1x^ne^xdx$$$$\Huge I_{n+1}=e-(n+1)I_n$$
Calculating $n=0$ traditionally allows for any further cases of $n$ to be found, without having to perform a complex sequence of integration by parts. Another way recurrence relations can be found in integrals is through trigonometric identities:
![[recurrence integral example]]
This relation only relates every other term, whereas the previous relation related every term to the next.

# Event and odd integrals:

If $f_{odd}(x)$ is an integrable odd function on $[-a,a]$, then:$$\Huge \int_{-a}^af_{odd}(x)dx=0$$
$$\large \int_{-a}^af_{odd}(x)dx=\int_0^af_{odd}(x)dx+\int_{-a}^0f_{odd}(x)dx=\int_0^af_{odd}(x)dx-\int_a^0f_{odd}(-x)dx$$
$$\large \int_{-a}^af_{odd}(x)dx=\int_0^af_{odd}(x)dx+\int_0^af_{odd}(-x)dx=\int_0^af_{odd}(x)dx-\int_0^af_{odd}(x)dx=0$$
Similarly, if $f_{even}(x)$ is an integrable even function on $[-a,a]$, then:$$\Huge \int_{-a}^af_{even}(x)dx=2\int_0^af_{even}(x)dx$$
The proof is similar to that of the odd integral. This has a corollary when $f(x)$ is decomposed into an odd and even function:
$$\Huge \int_{-a}^af(x)dx=\int_{-a}^af_{even}(x)dx+\int_{-a}^af_{odd}(x)dx=2\int_0^af_{even}(x)dx$$