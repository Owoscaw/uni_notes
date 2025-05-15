
# Meromorphicity:

Let $D$ be a domain. We call a function $F$ meromorphic on $D$ if it is [[Complex differentiation#Holomorphicity|holomorphic]] on $D\setminus S$, where $S$ is a set of point at which $f$ has a [[Holomorphic functions on punctured domains#Poles|pole]] and $S$ contains no [[Holomorphic functions#Isolated points and Identity theorem|non-isolated]] point.

# Residue theorem:

Let $\gamma$ be a [[General form of Cauchy's theorem and CIF#Jordan curve theorem|simply connected contour]] and suppose $f$ is meromorphic on $D_\gamma^{\text{int}}\cup\gamma$ with no poles on $\gamma$. Then:$$\Huge \int_\gamma f(z)dz=2\pi i\sum_{j=1}^m\text{Res}_{z=a_j}(f)$$where $a_1,\dots,a_m$ are the poles of $f$ in $D_\gamma^{\text{int}}$. 

Let $f$ have [[Holomorphic functions on punctured domains#Laurent series|Laurent series]] about $z=a$ given by $\sum_{n=-k}^\infty c_n(z-a)^k$. Then the residue of $f$ at $z=a$ is:$$\Huge \text{Res}_{z=a}(f)=c_{-1}$$
For example, we saw the function $f(z)=\frac{e^z-1}{z^2}=\sum_{m=-1}^\infty\frac{1}{(m+2)!}z^m$ has a single pole of order $1$ at $z=0$. So the residue of $f$ at $z=0$ will be equal to the coefficient corresponding to the $z^{-1}$ term in the Laurent series, that is:$$\Huge \text{Res}_{z=0}\left(\frac{e^z-1}{z^2}\right)=\frac{1}{((-1)+2)!}=1$$so by CRT:$$\Huge \int_{|z|=2}f(z)dz=2\pi i\text{ Res}_{z=0}(f)=2\pi i$$
We saw that $\tan z/z$ has poles at $z=n\pi+\pi/2$ and zeros at $z=n\pi$ for $n\neq0$. Then we can calculate:$$\Huge \int_{|z|=\pi}\frac{\tan z}{z}dz=2\pi i(\text{Res}_{z=-\pi/2}(f)+\text{Res}_{z=\pi/2}(f))$$This is doable, but who wants to calculate the Laurent series for this? We aim to determine a way of finding residues easily:
> If $f,g$ have poles at $z=a$ with $A,B\in\mathbb{C}$, then:$$\Huge \text{Res}_{z=a}(Af+Bg)=A\text{Res}_{z=a}(f)+B\text{Res}_{z=a}(g)$$Proven trivially.
> If $f$ has a pole of order $1$ at $z=a$ (simple pole) then:$$\Huge\text{Res}_{z=a}(f)=\lim_{z\to a}(z-a)f(z)$$which is the limit that characterises a [[Holomorphic functions on punctured domains#Removable singularities|removable singularity]]. To prove this, assume a pole of order $1$, which means we can write $f$ as $\sum_{n=-1}^\infty c_n(z-a)^n$ and write:$$\Huge\begin{align}
\lim_{z\to a}(z-a)f(z)&=\lim_{z\to a}\sum_{n=-1}^\infty c_n(z-a)^{n+1}\\
&=\lim_{z\to a}\sum_{m=0}^\infty c_{m-1}(z-a)^m\\
&=c_{0-1}=c_{-1}=\text{Res}_{z=a}(f)
\end{align}$$
> If $f(z)=g(z)/h(z)$ with $g,h$ holomorphic at $z=a$ and $h$ has a zero of order $1$ at $z=a$ then:$$\Huge \text{Res}_{z=a}(f)=\frac{g(a)}{h'(a)}$$Which comes from the fact that $f$ has a pole of order one at $z=a$ by definition. Now let $h(z)=\sum_{n=1}^\infty d_n(z-a)^n$ with $d_1\neq0$, then $h'(z)=\sum_{n=1}^\infty nd_n(z-a)^{n-1}$ and $\lim_{z\to a}\frac{h(z)}{z-a}=\lim_{z\to a}\sum_{n=1}^\infty d_n(z-a)^{n-1}$. Note that both of these expressions evaluate to $d_1\neq0$ at $z=a$. Applying the second rule, we have:$$\Huge \text{Res}_{z=a}(f)=\lim_{z\to a}(z-a)f(z)=\lim_{z\to a}\frac{g(z)}{h(z)/(z-a)}=\frac{g(a)}{d_1}=\frac{g(a)}{h'(a)}$$
> Suppose $f(z)=\frac{g(z)}{(z-a)^k}$ where $g$ is holomorphic at $z=a$, then:$$\Huge \text{Res}_{z=a}(f)=\frac{g^{(k-1)}(a)}{(k-1)!}$$Proven trivially.

For example, let $f(z)=\frac{1}{z^2-9}=\frac{1}{(z-3)(z+3)}$. This has order one poles at $z=\pm 3$, so we apply rule 2:$$\Huge \text{Res}_{z=3}(f)=\lim_{z\to 3}(z-3)f(z)=\lim_{z\to 3}\frac{1}{z+3}=1/6$$

# Proof of Cauchy's Residue theorem:

Let $S=\{a_1,\dots,a_m\}$ be the set of poles of $f$ inside $\gamma$. So $f$ is holomorphic on $D\setminus S$. We write:$$\Huge f_j(z)=\sum_{n=-k_j}^{-1}c_{n,j}(z-a_j)^n$$for the principle part of the Laurent series of $f$ around each $z=a_j$. This extends to a holomorphic function on $\mathbb{C}\setminus\{a_j\}$ so it makes sense to define $\int_\gamma f_j(z)dz$ as:$$\Huge\begin{align}
\int_\gamma f_j(z)dz&=\int_\gamma\sum_{n=-k_j}^{-1}c_{n,j}(z-a_j)^ndz\\
&=\sum_{n=-k_j}^{-1}c_{n,j}\int_\gamma(z-a_j)^ndz\\
&=c_{-1,j}(2\pi i)=2\pi i\text{Res}_{z=a_j}(f)
\end{align}$$where all terms in the sum other than $n=-1$ are zero by [[General form of Cauchy's theorem and CIF#General forms of Cauchy's theorem and CIF|Cauchy's theorem]], and the only surviving term is given by $2\pi i c_{-1,j}$, by Cauchy's integral formula. This is equivalent to the residue of $f$ about $z=a_j$, expressed in the final line. We define $g:D_\gamma^{\text{int}}\cup\gamma\setminus S\rightarrow\mathbb{C}$ by:$$\Huge g=f-\sum_{j=1}^mf_j$$Then at $z=a_i$ we have $g=P-\sum_{j=1,j\neq i}^mf_j$ where $P$ is some power series. Both parts are holomorphic at $z=a_i$, so $g$ is extended to a holomorphic function at $z=a_i$. Now we apply Cauchy's theorem:$$\Huge\begin{align}
0=\int_\gamma g(z)dz&=\int_\gamma\left(f(z)-\sum_{j=1}^mf_j(z)\right)dz\\
\implies\int_\gamma f(z)dz&=\sum_{j=1}^m\int_\gamma f_j(z)dz\\
&=2\pi i\sum_{j=1}^m\text{Res}_{z=a_j}(f)
\end{align}$$Concluding the proof.

# Real series calculation:

We now have the tools required to take any integral on the complex plane. We consider two scenarios, one where $f$ has no poles on $\Re$ and one where $f$ has a pole at $z=0$ (for example):![[year 2/complex analysis 2/term 2/drawings/integration]]
For the pole-less function we have two methods:
> $$\Huge \int_{-R}^Rf(x)dx=\int_{L_R}f(z)dz=\int_{\gamma_R}fdz-\int_{C_r}fdz$$
> $$\large \int_{-R}^Rg(x)\sin(x)dx=\Im\left(\int_{L_R}g(z)e^{-z}dz\right)=\Im\left(\int_{\gamma_R}g(z)e^{iz}dz-\int_{C_R}g(z)e^{iz}dz\right)$$

And for the pole-full function:$$\large\begin{align}
\int_\epsilon^{R}g(x)\sin(x)dx&=\frac{1}{2i}\left(\int_{L_1}g(z)e^{iz}dz+\int_{L_2}g(z)e^{iz}dz\right)\\
&=\frac{1}{2i}\left(\int_{\gamma_R}g(z)e^{iz}dz-\int_{C_R}g(z)e^{iz}dz+\int_{C_\epsilon}g(z)e^{iz}dz\right)
\end{align}$$
## Squares lemma:
For $N\geq0$ let $S_N$ be the square in $\mathbb{C}$ with vertices $(1+i)(N+1/2),(-1+i)(N+1/2),(-1-i)(N+1/2),(1-i)(N+1/2)$, then there exist real constants $C,D>0$ independent of $N$ such that:$$\Huge |\cot(\pi z)|=\frac{|\cos(\pi z)|}{|\sin(\pi z)|}\leq C,\,\,|\csc(\pi z)|=\frac{1}{|\sin(\pi z)|}\leq D$$![[square lemma]]On the vertical sides we have $z=\pm(N+1/2)+iy$ with $|y|\leq N+1/2$ so we have:$$ |\csc(\pi z)|=\frac{1}{|\sin(\pi(\pm(N+1/2)+iy)|}=\frac{1}{|\sin(\pm\pi(N+1/2)+i\pi y)|}=\frac{1}{|\cos(i\pi y)|}=\frac{1}{\cosh(\pi y)}\leq1$$as $\cosh(y)\geq1$ on the reals. Similarly we have:$$ |\cot(\pi z)|=\frac{|\cos(\pm\pi(N+1/2)+i\pi y)|}{|\sin(\pm\pi(N+1/2)+i\pi y)|}=\frac{|\pm\sin(i\pi y)|}{|\pm\cos(i\pi y)|}=\frac{|e^{-\pi y}-e^{\pi y}|}{|e^{-\pi y}+e^{\pi y}|}=\frac{|1-e^{-2\pi y}|}{|1+e^{-2\pi y}|}\leq 1$$Now on the horizontal sides we have $z=x+iy$ with $|y|\geq1/2$ so:$$\Huge |\csc(\pi z)|=\frac{1}{1/2|e^{i\pi z}-e^{-i\pi z}|}$$now notice that $|e^{i\pi z}|=|e^{i\pi x}e^{-\pi y}|=e^{\pi y}$ so by the reverse triangle inequality:$$\Huge|\csc(\pi z)|\leq\frac{1}{1/2||e^{i\pi(x+iy)}|-|e^{i\pi(x+iy)}||}=\frac{1}{1/2|e^{-\pi y}-e^{\pi y}|}$$This upper bound becomes $\frac{1}{1/2(e^{\pi y}-e^{i\pi y})}$ for $y\geq0$ and $\frac{1}{1/2(e^{-\pi y}-e^{\pi y})}$ if $y\leq 0$ so the upper bound can be written as $\frac{1}{\sinh(\pi|y|)}$. Now we have $|y|\geq1/2$ and as $\sinh$ is an increasing function we have:$$\Huge |\csc(\pi z)|\leq\frac{1}{\sinh(\pi|y|)}\leq\frac{1}{\sinh(\pi/2)}$$for the horizontal sides. Similarly:$$\large \begin{align}
\cot(\pi z)&=\frac{\cos(\pi z)}{\sin(\pi z)}=\cos(\pi z)\csc(\pi z)\\
|\cos(\pi z)|&=\frac{1}{2}|e^{i\pi z}+e^{-i\pi z}|\leq\frac{1}{2}(|e^{i\pi z}|+|e^{-i\pi z}|)=\frac{1}{2}(e^{-\pi y}+e^{\pi y})=\cosh(\pi y)\\
|\cot(\pi z)|&=|\cos(\pi z)||\csc(\pi z)|\leq\frac{\cosh(\pi|y|)}{\sinh(\pi|y|)}=\coth(\pi|y|)\leq\coth(\pi/2)
\end{align}$$So we have the result as required.

## Basel problem:
Now we can solve the classical problem:$$\Huge \sum_{n=1}^\infty\frac{1}{n^2}=\frac{\pi^2}{6}$$Euler solved this (of course) ages ago, however we offer a modern proof using complex analysis. To do this, we will calculate $\int_{S_N}f(z)dz$ with $f(z)=\frac{\cot(\pi z)}{z^2}$ and take $S_N$ to be the path described in the above squares lemma.

The singularities of $f(z)=\frac{\cot(\pi z)}{z^2}=\frac{\cos(\pi z)}{z^2\sin(\pi z)}$ occur precisely at the zeros of the denominator. For $z^2$ these occur at $z=0$ and $\sin(\pi z)$ they occur at $z=n$. The numerator is never zero at these points, so all poles are simple apart from $z=0$ as this is clearly a zero of the denominator of order $3$ so must be a pole of $f$ of order $3$. We must therefore find the residue of these poles:$$\Huge \text{Res}_{z=n}(f)=\frac{\cos(\pi z)/z^2}{\frac{d}{dz}(\sin(\pi z))}\vert_{z=n}=\frac{\cos(\pi n)/n^2}{\pi\cos(\pi n)}=\frac{1}{\pi n^2}$$We cannot use this method for $z=0$ as $f$ has a pole of order $3$ here. Because of this, the principal part of $f$'s Laurent series must have form $c_{-3}z^{-3}+c_{-2}z^{-2}+c_{-1}z^{-1}$ for some $c\in\mathbb{C}$ with $c_{-3}\neq0$. Now we write $g(z)=z^3f(z)$ and notice that $g$ is simply a power series (no principal part) and so must extend to a holomorphic function at $z=0$ (this is a removable singularity of $g$). Then clearly $c_{-3}$ is the value of $g$ at $z=0$, that is $c_{-3}=g(0)$. Moreover $c_{-2}=g'(0)$ and:$$\Huge \text{Res}_{z=0}(f)=c_{-1}=\frac{g''(0)}{2}$$To find this, we simply verify that the Taylor series of $\sin(\pi z)$ on $\mathbb{C}$ is given by:$$\Huge \sin(\pi z)=\sum_{n=0}^\infty\frac{(-1)^n}{(2n+1)!}(\pi z)^{2n+1}=\sum_{n=0}^\infty\frac{(-1)^n\pi^{2n+1}}{(2n+1)!}z^{2n+1}$$and hence:$$\Huge \begin{align}
z^3f(z)&=\frac{z\cos(\pi z)}{\sin(\pi z)}\\
&=\frac{\cos(\pi z)}{\sum_{n=0}^\infty\frac{(-1)^n\pi^{2n+1}}{(2n+1)!}z^{2n}}\\
&=\frac{\cos(\pi z)}{\pi+\sum_{n=1}^\infty\frac{(-1)^n\pi^{2n+1}}{(2n+1)!}z^{2n}}\\
&=\frac{\cos(\pi z)}{\pi+h(z)}
\end{align}$$where $h(z)=\sum_{n=1}^\infty a_nz^n$ is a holomorphic power series converging on $\mathbb{C}$ with:$$\Huge h(0)=a_0=0,\,\,h'(0)=a_1=0,\,\,h''(0)=2a_2=-2\frac{\pi^3}{6}=-\frac{\pi^3}{3}$$Now:$$\Huge g'(z)=\frac{d}{dz}(z^3f(z))=\frac{-\pi\sin(\pi z)}{\pi+h(z)}+\frac{-h'(z)\cos(\pi z)}{(\pi+h(z))^2}$$so we have:$$\large g''(0)=\frac{-\pi^2\cos(0)}{\pi+h(0)}+\frac{-h''(0)\cos(0)}{(\pi+h(0))^2}=-\pi+\frac{\pi^3/3}{\pi^2}=-\pi+\pi/3=-\frac{2\pi}{3}$$Therefore $\text{Res}_{z=0}(f)=c_{-1}=g''(0)/2=-\pi/3$. Now we can return to the integral, for sufficiently large $N$, the poles lying inside $S_N$ are precisely $z=0$ and $z=n\neq0$ for $-N\leq n\leq N$. Therefore by Cauchy's residue theorem:$$\Huge \frac{1}{2\pi i}\int_{S_N}f(z)dz=-\frac{\pi}{3}+\frac{1}{\pi}\sum_{n_{n\neq0}=-N}^N\frac{1}{n^2}=-\frac{\pi}{3}+\frac{2}{\pi}\sum_{n=1}^N\frac{1}{n^2}$$The length of $S_N$ is $4(2N+1)=8N+4$. Now for $z\in S_N$ and sufficiently large $N$ we meet the requirements for the Squares lemma and there exists $C>0$ independent of $N$ such that:$$\large \sup_{z\in S_N}|f(z)|=\sup_{z\in S_N}\left|\frac{\cot(\pi z)}{z^2}\right|\leq C\sup_{z\in S_N}\frac{1}{|z|^2}=\frac{C}{(N+1/2)^2}=\frac{C}{N^2+N+1/4}$$Then by the estimation lemma we have:$$\Huge \left|\int_{S_N}f(z)dz\right|=\left|\int_{S_N}\frac{\cot(\pi z)}{z^2}dz\right|\leq\frac{C(8N+4)}{N^2+N+1/4}=\frac{C(8+4/N)}{N+1+1/4N}$$this clearly tends to $0$ as $N\to\infty$. Moreover we know that $\sum_{n=1}^N\frac{1}{n^2}$ converges thus by letting $N\to\infty$:$$\Huge \sum_{n=1}^\infty\frac{1}{n^2}=\frac{\pi}{2}\lim_{N\to \infty}\left(\frac{1}{2\pi i}\int_{S_N}f(z)dz+\frac{\pi}{3}\right)=\frac{\pi}{2}\cdot\frac{\pi}{3}=\frac{\pi^2}{6}$$as required.

# Argument principle and Rouche's theorem:

