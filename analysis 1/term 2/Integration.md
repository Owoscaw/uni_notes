
# Regulated integral

Let $f$ be a [[Regulated functions#Step functions|step function]] on $[a,b]$ associated to a partition $a=x_0<x_1<\dots<x_{N-1}<x_N=b$ and let $x_k^*\in(x_k,x_{k+1})$, on which $f$ is constant. Then the integral $I(f)$ of $f$ is defined by:$$\Huge I(f)=I(f,a,b)=\sum_{k=0}^{N-1}f(x_k^*)(x_{k+1}-x_k)$$Note that if $a=y_0<y_1<\dots<y_{M-1}<y_M=b$ is another partition, then:$$\Huge I(f)=\sum_{k=0}^{M-1}f(y_k^*)(y_{k+1}-y_k)$$
Let a [[Regulated functions#Continuous functions are regulated|regulated function]] on $[a,b]$, say that $f$ is the uniform limit of the step functions $f_n$, $n\in \mathbb{N}$, then we define:$$\Huge I(f)=\lim_{n\to \infty}I(f_n)$$However we require that this sequence $I(f_n)$ converges, and that this limit should not depend on the sequence of step functions. Let $f$ be a regulated function on $[a,b]$ and $(f_n)_{n\in \mathbb{N}}$ a sequence of step function with $f_n\to f$ uniformly. Then the sequence $(I(f_n))_{n\in \mathbb{N}}$ converges. To prove this, for $\epsilon>0$ take $N\in \mathbb{N}$ such that $|f(x)-f_n(x)|<\frac{\epsilon}{2(b-a)}$ for all $x\in[a,b]$ and all $n\geq N$. Let $n,m\geq N$, we require $|I(f_n)-I(f_m)|<\epsilon$ since this means $(I(f_n))$ form a cauchy sequence. Now let $a=x_0<x_1<\dots<x_{M-1}<x_M=b$ be a common refinement of $f_n$ and $f_m$:$$\big |I(f_n)-I(f_m)|=\left|\sum_{k=0}^{M-1}f_n(x_k^*)(x_{k+1}-x_k)-f_m(x_k^*)(x_{k+1}-x_k)\right|=|\sum_{k=0}^{M-1}(f_n(x_k^*)-f_m(x_k^*))(x_{k+1}-x_k)|$$$$\implies\small |\sum_{k=0}^{M-1}(f_n(x_k^*)-f(x_k^*)+f(x_k^*)-f_m(x_k^*)(x_{k+1}-x_k)|<\sum_{k=0}^{M-1}(|f_n(x_k^*)-f(x_k^*)|+|f_m(x_k^*)-f(x_k^*)|)(x_{k+1}-x_k)$$$$\Huge\implies|I(f_n)-I(f_m)|<\sum_{k=0}^{M-1}\frac{\epsilon}{b-a}(x_{k+1}-x_k)=\epsilon$$So we have these sequences are cauchy sequences, and the sequence $(I(f_n))_{n\in \mathbb{N}}$ converges.

Let $f$ be a regulated function on $[a,b]$ and let $(f_n),(g_n)$ be sequences of step functions converging uniformly to $f$, then:$$\Huge \lim_{n\to \infty}I(f_n)=\lim_{n\to \infty}I(g_n)$$To prove this, pick a common refinement for each $f_n,g_n$ and let $\epsilon>0$. Pick $N\in \mathbb{N}$ such that $|f(x)-f_n(x)|<\frac{\epsilon}{2(b-a)}$ for all $n\geq N$, then:$$ |I(f_n)-I(g_n)|=\left|\sum_{k=0}^{M-1}f_n(x_k^*)(x_{k+1}-x_k)-g_n(x_k^*)(x_{k+1}-x_k)\right|=\left|\sum_{k=0}^{M-1}(f_n(x_k^*)-g_n(x_k^*))(x_{k+1}-x_k)\right|$$$$\Huge \implies|I(f_n)-I(g_n)|=\left|\sum_{k=0}^{M-1}(f_n(x_k^*)-f(x_k^*)+f(x_k^*)-g_n(x_k^*))(x_{k+1}-x_k)\right|$$$$\implies |I(f_n)-I(g_n)|\leq\sum_{k=0}^{M-1}(|f_n(x_k^*)-f(x_k^*)|+|f(x_k^*)-g_n(x_k^*)|)(x_{k+1}-x_k)<\frac{\epsilon}{b-a}\sum_{k=0}^{M-1}(x_{k+1}-x_k)=\epsilon$$So we get that $f,g$ are cauchy sequences and therefore share the same limit, as require. For a regulated function, we write:$$\Huge I(f)=I(f,a,b)=\int_a^bf(x)dx$$
## Properties:
Let $f$ and $g$ be regulated functions on $[a,g]$ then:
> Linearity, for $c\in\Re$:$$\Huge\int_a^bcf(x)dx=c\int_a^bf(x)dx,\,\,\int_a^bf(x)+g(x)dx=\int_a^bf(x)dx+\int_a^bg(x)dx$$If $f(x)\leq g(x)$ for all $x\in[a,b]$, then:$$\Huge \int_a^bf(x)dx\leq\int_a^bg(x)dx$$Furthermore, set $m=\inf\{f(x)|x\in[a,b]\}, M=\sup\{f(x):x\in[a,b]\}$, then:$$\Huge m(b-a)\leq\int_a^bf(x)dx\leq M(b-a)$$Finally:$$\Huge \left|\int_a^bf(x)dx\right|\leq\int_a^b|f(x)|dx$$

To prove linearity, let $(f_n)$ be a sequence of step function converging uniformly to $f$, similarly for $(g_n)\to f$ and assume $f_n,g_n$ are defined on the same partition. Then $cf_n\to cf$ uniformly, and $\lim_{n\to \infty}I(cf_n)=I(cf)$. Then we get $I(cf_n)=\sum_{k=0}^{N-1}cf_n(x_k^*)(x_{k+1}-x_k)=cI(f_n)$, hence $\lim_{n\to \infty}I(cf_n)=\lim_{n\to \infty}cI(f_n)=c\lim_{n\to \infty}I(f_n)=cI(f)$.

Since $m,M$ are well defined, $f$ is bounded on $[a,b]$ and we have $m\leq f(x)\leq M$ for all $x\in[a,b]$. Therefore we get:$$\Huge m(b-a)=\int_a^bmdx\leq\int_a^bf(x)dx\leq\int_a^bMdx=M(b-a)$$
$|f(x)|\geq f(x)$ and $|f(x)|\geq-f(x)$ implies that $\int_a^b|f(x)|dx\geq\int_a^bf(x)dx$ and $\int_a^b|f(x)|dx\geq-\int_a^bf(x)$, which implies the statement as required.

Let $f(x)$ be a continuous function on $[a,b]$ such that $f(x)\geq0$ for all $x\in[a,b]$ and $f(c)>0$ for some $c\in[a,b]$, then:$$\Huge \int_a^bf(x)dx>0$$Since by continuity there exists a non-trivial interval $[\alpha,\beta]$ containing $c$ such that $f(x)\geq \frac{C}{2}$ where $C=f(c)>0$. Choose $\epsilon=\frac{C}{2}>0$, now there exists $\delta>0$ such that $|f(x)-C|<\frac{C}{2}$ for all $x:|x-c|<\delta$. Now $\int_a^bf(x)dx=\int_a^\alpha f(x)dx+\int_\alpha^\beta f(x)dx+\int_\beta^bf(x)dx\geq0+\frac{C}{2}(\beta-\alpha)+0>0$, as required.
## Additivity:
For any $c\in(a,b)$, $f$ is also regulated on $[a,c],[c,b]$ and we have:$$\Huge \int_a^bf(x)dx=\int_a^cf(x)dx+\int_c^bf(x)dx$$Since $f_n\to f$ converges uniformly on $[a,b]$, it still converges uniformly on smaller intervals, like $[a,c]$ and $[c,b]$. When $f_n$ is restricted to these intervals, it remains a step function. We assume $c$ to be a part of the partition for each $f_n$, then $I(f_n,a,b)=I(f_n,a,c)+I(f_n,c,b)$.

# MVT for integrals:

Let $f$ be a continuous function on $[a,b]$, then there exists $c\in[a,b]$ such that:$$\Huge \int_a^bf(x)dx=f(c)(b-a)$$Let $C=\frac{1}{b-a}\int_a^bf(x)dx$ and $m=\inf\{f(x):x\in[a,b]\},M=\sup\{f(x):x\in[a,b]\}$. We then have $m\leq C\leq M$. Since $f$ is continuous, there exists $x\in[a,b]$ and $y\in[a,b]$ with $f(x)=m$ and $f(y)=M$. By the intermediate value theorem, there exists $c\in[x,y]:f(c)=C$. Multiplying this equation by $b-a$ gives the result as required.

# Fundamental theorem of Calculus:

Consider the function $F(x)=\int_a^xf(t)dt$ where $f:[a,b]\mapsto\Re$ is a regulated function. We propose that $F:[a,b]\mapsto\Re$ is Lipschitz continuous with constant $M=\sup\{|f(x)|:x\in[a,b]\}$. Let $x,y\in[a,b]$ with $x>y$, then:$$\large |F(x)-F(y)|=\left|\int_a^xf(t)dt-\int_z^yf(t)dt\right|=\left|\int_y^xf(t)dt\right|\leq\int_y^x|f(t)|dt\leq M|x-y|$$
Let $f$ be continuous on $[a,b]$, then $F(x)=\int_a^xf(t)dt$ defines a differentiable function, that is $F:[a,b]\mapsto\Re$ and $F'(x)=f(x)$ for all $x\in[a,b]$. Let $c\in[a,b]$, we then need to show:$$\Huge\lim_{x\to c}\frac{F(x)-F(c)}{x-c}=f(c)$$For $x\neq c$, we have:$$ \frac{F(x)-F(c)}{x-c}=\frac{1}{x-c}\int_a^xf(t)dt-\frac{1}{x-c}\int_a^cf(t)dt=\frac{1}{x-c}\int_c^xf(t)dt=\frac{f(\xi_x)(x-c)}{x-c}=f(\xi_x)$$By the mean value theorem for integrals, where $\xi_x\in[x,c]$, so:$$\Huge\lim_{x\to c}\frac{F(x)-F(c)}{x-c}=\lim_{x\to c}f(\xi_x)=f(\lim_{x\to c}\xi_c)=f(c)$$By continuity of $f$, we get the result as required. Another way to formulate the fundamental theorem of calculus is as follows: Let $f(x)$ be continuous on $[a,b]$ and $f(x)=F'(x)$ for some function $F:[a,b]\mapsto\Re$, then:$$\Huge F(x)=F(a)+\int_a^xf(t)dt$$Define $G(x)=F(x)-\int_a^xf(t)dt$, then by the FOTC, $G'(x)=f(a)-f(x)=0$. Then by MVT, $G$ is constant:$$\Huge G(x)=F(x)-\int_a^xf(t)dt=G(a)=F(a)-\int_a^af(t)dt=F(a)=c$$
This gives the following results:
> If $f:[a,b]\mapsto\Re$ is continuous, then there exists an antiderivative ($F:[a,b]\mapsto\Re:F'=f$)
> If $f:[a,b]\mapsto\Re$ is continuous with antiderivative $F:[a,b]\mapsto\Re$, then:$$\Huge \int_a^bf(x)dx=F(b)-F(a)=F(x)|^b_a$$

# Substitution:

Let $f$ be a continuous function on a closed interval $I$ and $g:[a,b]\mapsto I$ continuously differentiable. Then:$$\Huge \int_a^bf(g(x))g'(x)dx=\int_{g(a)}^{g(b)}f(t)dt$$Let $F$ be an antiderivative of $f$ on $I$. Then $F\circ g$ is an antiderivative of $f\circ g\times g'$ by the chain rule:$$\Huge \int_c^bf(g(x))g'(x)dx=F(g(b))-F(g(a))=\int_{g(a)}^{g(b)}f(x)dx$$as required.

# Integration by Parts:

Let $f,g$ be continuous functions on $[a,b]$ with $g$ continuous differentiable. Let $F$ be an antiderivative of $f$ on $[a,b]$, then:$$\Huge \int_a^bf(x)g(x)dx=[F(x)g(x)]_a^b-\int_a^bF(x)g'(x)dx$$Since, letting $G(x)=F(x)g(x)$, we have $G'(x)=F'(x)g(x)+F(x)g'(x)$. So:$$\Huge G(b)-G(a)=\int_a^bf(x)g(x)dx+\int_a^bF(x)g'(x)dx$$Which rearranges to give the result as required, using linearity of the integral.

# Functions via integrals:

We can define functions using the integral as follows:$$\Huge F(x)=\int_a^xf(t)dt$$As an example define:$$\Huge L(x)=\int_1^x\frac{dt}{t}$$Then we obviously get:
> $L(0)=1$
> $L$ is differentiable with $L'(x)=\frac{1}{x}$
> For all $x,y>0$ we have $L(xy)=L(x)+L(y)$, and $L(\frac{1}{x})=-L(x)$
> $L$ is strictly monotonically increasing
> $\frac{x}{x+1}\leq L(x+1)\leq x$ for all $x>-1$
> $L(2)>\frac{1}{2}$ and $L(2^n)>\frac{n}{2}$
> $\lim_{x\to \infty}L(x)=\infty$ and $\lim_{x\to 0^+}L(x)=-\infty$

The fifth property implies the sixth by setting $x=1$ in the inequality. The fourth and the sixth properties imply the first half of the seventh, while the third property implies the second half. To prove the third:$$\large L(xy)=\int_1^{xy}\frac{dt}{t}=\int_{\frac{1}{x}}^y\frac{ds}{s}=\int_{\frac{1}{x}}^1\frac{ds}{s}+\int_1^y\frac{ds}{s}=\int_1^x\frac{du}{u}+L(y)=L(x)+L(y)$$Where $s=\frac{t}{x}$ and $u=xs$. Using $L(1)=0$ and taking $y=\frac{1}{x}$ we get $L(\frac{1}{x})=-L(x)$, proving the third property. Let $g(x)=x-L(x+1)$, then $g'(x)=1-\frac{1}{1+x}\geq0$, which implies the LHS of the inequality for property five. Let $h(x)=L(x+1)-\frac{x}{x+1}$, then $h'(x)=\frac{1}{x+1}-\frac{x+1-x}{(x+1)^2}=\frac{1}{x+1}(1-\frac{1}{1+x})\geq0$, which implies the RHS. Since $L$ is monotonically increasing on $(0,\infty)$ with $\lim_{x\to \infty}L(x)=\infty$ and $\lim_{x\to0^+}L(x)=-\infty$ and $L$ is continuous, there exists an inverse function for $L$ defined as $E:\Re\mapsto(0,\infty)$. From this we can define Euler's number as the unique number $e>0$ with $L(e)=1$.

# Uniform convergence and Integration:

Let $I=[a,b]$ and $(f_n)$ be a sequence of regulated function on $I$ with $f_n\to f$ uniformly. Then:
> The limit function $f$ is regulated
> $$\Huge \int_a^bf(x)dx=\lim_{n\to \infty}\int_a^bf_n(x)dx$$

To prove the first statement, let $\epsilon>0$. Since $f_n\to f$ uniformly, there exists $N\in \mathbb{N}$ such that for all $n\geq N$ we have $|f(x)-f_n(x)|<\epsilon$ for all $x\in [a,b]$. There exists a step function $g_n:[a,b]\mapsto\Re$ such that $|g_n(x)-f_n(x)|<\epsilon$ for all $x\in[a,b]$. Now $|f(x)-g_n(x)|\leq|f(x)-f_n(x)|+|f_n(x)-g_n(x)|<2 \epsilon$ for all $x\in[a,b]$, that is $|f(x)-g_n(x)|<2\epsilon$. So we have that $f$ is indeed regulated.

To prove the second statement, look at:$$\Huge\left|\int_a^bf(x)dx-\int_a^bf_n(x)dx\right|\leq\int_a^b|f(x)-f_n(x)|dx<\int_a^b \epsilon \,dx=(b-a)\epsilon$$For all $n\geq N$. Therefore we get that $\int_a^b f_n(x)dx$ converges to $\int_a^bf(x)dx$, showing the result as required. Note that the pointwise limit of regulated functions may not be regulated. Take for example:$$\Huge f_n(x)=\begin{cases}1&\text{if }x\in\left[0,\frac{2}{(2n+1)\pi}\right]\\\sin\left(\frac{1}{x}\right)&\text{if }x\in\left[\frac{2}{(2n+1)\pi},1\right]\end{cases}$$Each $f_n$ is continuous, so each are regulated. Then the pointwise limit function becomes:$$\Huge f(x)=\begin{cases}1&\text{if }x=0\\\sin\left(\frac{1}{x}\right)&\text{if }x\in(0,1]\end{cases}$$
# Examples:
$$\Huge f(x)=\sum_{k=0}^\infty\frac{1}{2^k}\cos(15^k\pi x)$$This is continuous as it is just a sum of continuous functions, so we look at the integral:$$\small \int_0^\frac{1}{2}f(x)dx=\sum_{k=0}^\infty\int_0^\frac{1}{2}\frac{1}{2^k}\cos(15^k\pi x)dx=\sum_{k=0}^\infty\frac{1}{2^k}\frac{1}{15^k\pi}[\sin(15^k \pi x)]_0^{\frac{1}{2}}=\sum_{k=0}^\infty\frac{1}{30^k\pi}\sin\left(\frac{15^k\pi}{2}\right)=\frac{1}{\pi}\sum_{k=0}^\infty\left(\frac{-1}{30}\right)^k$$Now this is just a geometric series. We were allowed to swap the sum and the integral because of the continuity of the function:$$\Huge \int_0^\frac{1}{2}f(x)dx=\frac{1}{\pi}\frac{1}{1+\frac{1}{30}}=\frac{30}{31\pi}$$

# Improper Integrals:

Let $f$ be a continuous function on an interval $[a,b)$. We then define the improper integral by:$$\Huge \int_a^bf(x)dx=\lim_{c\to b^-}\int_a^cf(x)dx$$We call the integral convergent or divergent depending on whether this limit exists. If $f$ is continuous on $(a,b]$ we have a similar definition:$$\Huge \int_a^bf(x)dx=\lim_{c\to a^+}\int_c^bf(x)dx$$Then for continuity on $(a,b)$ pick $c\in(a,b)$ and consider:$$\Huge \int_a^bf(x)dx=\int_a^cf(x)dx+\int_c^bf(x)dx$$