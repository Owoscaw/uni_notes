
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

Let $f$ be meromorphic on a domain $D$ with a zero or pole of order $k>0$ at $a\in D$. Then the function $\frac{f'(z)}{f(z)}$ has a simple pole at $a$ and:$$\Huge \text{Res}_{z=a}\left(\frac{f'}{f}\right)=\begin{cases}k&\text{if }f\text{ has a zero at }z=a\\-k&\text{if }f\text{ has a pole at }z=a\end{cases}$$To prove this, assume $f$ has a zero of order $k>0$ at $a$. Then we can write:$$\Huge f(z)=(z-a)^kg(z),\,\,g(a)\neq0$$by definition of the [[Holomorphic functions#Order of a zero|order of a zero]]. Therefore:$$\Huge \frac{f'(z)}{f(z)}=\frac{k(z-a)^{k-1}g(z)+(z-a)^kg'(z)}{(z-a)^kg(z)}=\frac{k}{z-a}+\frac{g'(z)}{g(z)}$$Note that since $g(z)$ is holomorphic and $g(a)\neq0$ we have that $\frac{g'(z)}{g(z)}$ is also holomorphic at $z=a$. This means that $g$ can be written as a power series and that $f$ can be written as a Laurent series with $\frac{k}{z-a}$ as the principle part and $\frac{g'(z)}{g(z)}$ as the analytic part. Clearly $f$ therefore has a pole of order $1$ at $z=a$ and by definition, $c_{-1}=k$ and we have $\text{Res}_{z=a}(f'/f)=k$ as required.

Now assume that $f$ has a pole of order $k>0$ at $a$. Then we can write:$$\Huge f(z)=\frac{g(z)}{(z-a)^k}$$for some holomorphic $g$ such that $g(a)\neq0$. In this case:$$\Huge \frac{f'(z)}{f(z)}=\frac{-kg(z)/(z-a)^{k+1}+g'(z)/(z-a)^k}{g(z)/(z-a)^k}=-\frac{k}{z-a}+\frac{g'(z)}{g(z)}$$Now by the same argument we have that $c_{-1}=k$ and $\text{Res}_{z=a}(f'/f)=-k$, completing the proof.

Take for example $f(z)=e^z/z$, which has no zeros and a pole of order $1$ at $z=0$. Here we have:$$\Huge f'(z)=\frac{e^z}{z}-\frac{e^z}{z^2},\,\,\frac{f'(z)}{f(z)}=\frac{(z-1)e^z/z^2}{e^z/z}=\frac{z-1}{z}=-\frac{1}{z}+1$$which clearly has a pole of order $1$ at $z=0$ and $\text{Res}_{z=0}(f'/f)=-1$

Note that if $f$ is meromorphic then $f'/f$ is meromorphic and the poles of $h=f'/f$ are at either:
> the zeros or poles of $f$ 
> the poles of $f'$:
> > Assume $z=a$ is a "new pole" (doesn't come from a  pole of $f$). This means that $f$ does not have a pole at $a$ and is therefore holomorphic at $a$. Now $f$ can be written as a power series and we write $f'(z)=\sum_{n=1}^\infty nc_n(z-a)^{n-1}$ which is just a power series and cannot have a pole. This is a contradiction, so $z=a$ cannot be a "new pole". Therefore, poles of $f$ must also be poles of $f'$, and all poles must come from the zeros or poles of $f$ (and are all therefore simple).

## Argument Principle:
Now we can state and prove the Argument Principle. Let $\gamma$ be a simple closed contour, positively oriented, and suppose $f$ is meromorphic on and inside the contour ($\gamma\cup D_\gamma^\text{int}$) with no zeros or poles on $\gamma$. Now we define $z_f$ as the number of zeros $f$ has in $D_\gamma^\text{int}$ and $p_f$ as the number of poles in $D_\gamma^\text{int}$ (counted with multiplicities!). Then we have:$$\Huge \frac{1}{2\pi i}\int_\gamma\frac{f'(z)}{f(z)}dz=z_f-p_f$$Proven as follows: By Cauchy's residue theorem:$$\Huge\begin{align}
\frac{1}{2\pi i}\int_\gamma\frac{f'(z)}{f(z)}dz&=\sum_{j=1}^n\text{Res}_{z=a_j}\left(\frac{f'}{f}\right)\\
&=\sum_{j=1}^m\text{Res}_{z=b_j}\left(\frac{f'}{f}\right)+\sum_{j=1}^k\text{Res}_{z=c_j}\left(\frac{f'}{f}\right)\\
&=\sum\text{orders of zeros}+\sum\text{orders of poles}\\
&=z_f-p_f
\end{align}$$where $b_j$ are the zeros of $f$ and $c_j$ are the poles of $f$ and we get equality from the third to fourth line by the lemma proven above.

Take for example $f(z)=\frac{(z-3)^3(z-1)^7z^3}{(z-i)^4(z+4)^5(z-3i)^7}$ and $\gamma(\theta)=\frac{7}{2}e^{i\theta}$ for $\theta\in[0,2\pi]$. Then:$$\Huge \frac{1}{2\pi i}\int_\gamma\frac{f'(z)}{g(z)}dz=(3+7+3)-(4+7)=13-11=2$$
We now see where the name "argument principle" comes from. Imagine any $\gamma,f$ that satisfy the conditions for the principle:![[arg princ]]Clearly, $0\notin\Gamma_f$ so we ask how many times $\Gamma_f$ winds around $0$:$$\Huge\begin{align}
I(\Gamma_f;0)&=\frac{1}{2\pi i}\int_{\Gamma_f}\frac{1}{z}dz\\
&=\frac{1}{2\pi i}\int_a^b\frac{1}{\Gamma_f(t)}\Gamma_f'(t)dt\\
&=\frac{1}{2\pi i}\int_a^b\frac{1}{f(\gamma(t))}(f'(\gamma(t))\gamma'(t))dt\\
&=\frac{1}{2\pi i}\int_a^b\frac{f'(\gamma(t))}{f(\gamma(t))}\gamma'(t)dt\\
&=\frac{1}{2\pi i}\int_\gamma\frac{f'(z)}{f(z)}dz=z_f-p_f
\end{align}$$So we see that the winding number of $\Gamma_f$ around $0$ is simply equal to the number of zeros inside $\gamma$ minus the number of poles inside $\gamma$.

## Rouche's theorem:
Let $\gamma$ be a simple closed contour, and let $f,g$ be holomorphic functions on $D_\gamma^\text{int}\cup\gamma$. Suppose that:$$\Huge |f(z)-g(z)|<|g(z)|,\,\,\forall z\in\gamma$$Then $f(z)$ and $g(z)$ have the same number of zeros (counting multiplicities!) inside $\gamma$. Note that if we write $\Gamma_f=f\circ\gamma$ and $\Gamma_g=g\circ\gamma$, then the above statement is equivalent to:$$\Huge |\Gamma_f(t)-\Gamma_g(t)|<|\Gamma_g(t)-0|,\,\,\forall t\in[a,b]$$
![[rouches]]
This is proven as follows:

Since both $f,g$ are holomorphic on $D_\gamma^\text{int}$, they have no poles on $\gamma$ and we set $h(z)=\frac{f(z)}{g(z)}$. Observe that $h$ has no poles on $\gamma$ as the poles have to be zeros of $g$, and $g$ has no zeros on $\gamma$. If $g(z_0)=0$ for some $z_0\in\gamma$, then we have that $|f(z_0)|<0$, which is a contradiction. Similarly $h$ has no zeros on $\gamma$ as these would be the zeros of $f$ on $\gamma$, however $f$ has no zeros on $\gamma$. If $f(z_0)=0$ then we have that $|g(z_0)|<|g(z_0)|$, a contradiction. So we have that both $f,g$ have no zeros and no poles on $\gamma$. Since $h$ is the quotient of two holomorphic functions, and any poles of $h$ must be isolated ([[Holomorphic functions#Principle of isolated zeros (PIZ)|PIZ]] on $g$) and so we must have that $h$ is meromorphic on $D_\gamma^\text{int}\cup\gamma$. Now we can apply the Argument Principle on all $f,g,h$. Notice that:$$\Huge\begin{align}
\frac{1}{2\pi i}\int_\gamma\frac{h'(z)}{h(z)}dz&=\frac{1}{2\pi i}\int_\gamma\frac{\frac{f'(z)}{g(z)}-\frac{f(z)g'(z)}{g^2(z)}}{\frac{f(z)}{g(z)}}dz\\
&=\frac{1}{2\pi i}\left(\int_\gamma\frac{f'(z)}{f(z)}dz-\int_\gamma\frac{g'(z)}{g(z)}dz\right)
\end{align}$$So applying the Argument Principle to $f,g$:$$\Huge \frac{1}{2\pi i}\int_\gamma\frac{f'(z)}{f(z)}dz=z_f,\,\,\frac{1}{2\pi i}\int_\gamma\frac{g'(z)}{g(z)}dz=z_g$$And therefore:$$\Huge \frac{1}{2\pi i}\int_\gamma\frac{h'(z)}{h(z)}dz=I(\Gamma_h;0)$$with $\Gamma_h=g\circ\gamma$. When we establish that $I(\Gamma_h;0)=0$ we will have that $z_f-z_g=0$, that is $z_f=z_g$ $f,g$ have the same number of zeros. Now note that $|f(z)-g(z)|<|g(z)|$ for all $z\in\gamma$ implies:$$\large |h(z)-1|=\left|\frac{f(z)}{g(z)}-\frac{g(z)}{g(z)}\right|=\frac{1}{|g(z)|}|f(z)-g(z)|<\frac{|g(z)|}{|g(z)|}=1,\,\,\forall z\in\gamma$$That is, $\Gamma_h\subset B_1(1)$. Finally since $0\notin B_1(1)$ and $B_1(1)$ is starlike, it follows that $I(\Gamma_h;0)=0$, and we prove the theorem as required.

Take for example $p(z)=z^4+6z+\pi$. We know that this has $4$ roots in $\mathbb{C}$ and that $g(z)=z^4$ has $4$ roots in $|z|=r$ for any $r>0$. Then on $|z|=r$:$$\Huge\begin{align}
|g(z)|&=|z^4|=|z|^4=r^4\\
|f(z)-g(z)|&=|6z+\pi|\leq6|z|+\pi=6r+\pi
\end{align}$$Taking $r=2$ we have $|g(z)|=16$ and $|f(z)-g(z)|=12+\pi<16$. So by Rouche's theorem, $f$ has $4$ roots within $|z|=2$. We can determine how many of these roots are within $|z|=1$ by taking $g(z)=6z$. $g$ has one roots inside $|z|=1$:$$\Huge\begin{align}
|g(z)|&=6|z|=6\\
|f(z)-g(z)|&=|z^4+\pi|\leq1+\pi<6
\end{align}$$therefore $f$ has one root inside $|z|=1$ by Rouche's theorem.

Also consider $f(z)=\cos(\pi z)-\alpha z^m$ for $\alpha>e^\pi$ and $m\in\mathbb{N}$. We can show that this function has $m$ zeros in the unit disc by setting $g(z)=-\alpha z^m$ and considering the contour $\gamma:|z|=1$. Then for all $z\in\gamma$ we have $|g(z)|=\alpha>e^\pi$ and:$$\Huge |f(z)-g(z)|=|\cos(\pi z)|=\left|\frac{e^{i\pi z}+e^{-i\pi z}}{2}\right|\leq\frac{|e^{i\pi z}|+|e^{-i\pi z}|}{2}$$Now since $z\in\gamma$ we can write $z=x+iy$ and we have that $x\in[-1,1],y\in[-1,1]$ and:$$\Huge |e^{i\pi z}|=|e^{i\pi(x+iy)}|=e^{-\pi y}\leq e^\pi$$with the same result for $|e^{-i\pi z}|$. Therefore for all $z\in\gamma$ we have:$$\Huge |f(z)-g(z)|\leq e^\pi<\alpha=|g(z)|$$Therefore by Rouche's theorem $f$ and $g$ have the same number of zeros inside the unit disc. Clearly $g=\alpha z^m$ has the zero $z=0$ with multiplicity $m$, therefore $f$ has $m$ zeros inside the unit disc.

# Open mapping theorem:

Let $D$ be a domain and $f$ holomorphic on $D$. If $U\subset D$ is open then $f(U)$ is open.

Note that if we assume $f$ is not constant on $D$, then it must be non constant on $U$. To show that $f(U)$ is open, we will show that for every $b\in f(U)$ there exists some $\delta>0$ such that $B_\delta(b)\subset f(U)$. Note that there exists some $a\in U$ such that $b=f(a)$. To show open-ness we must show that for all $\tilde b\in B_\delta(b)$ there exists $\tilde a\in U$ such that $f(\tilde a)=\tilde b$. The proof therefore has two parts, finding a suitable $\delta$ and constructing $\tilde a$ such that $f(\tilde a)=\tilde b$:

## Part 1:
Let $g(z)=f(z)-b$ so that $g(a)=f(a)-b=0$. Now the [[Holomorphic functions#Principle of isolated zeros (PIZ)|PIZ]] applies and there exists some $\epsilon>0$ such that $g(z)\neq0$ for all $z\in B_\epsilon(a)\setminus\{a\}$. Now define $\gamma(t)=a+\frac{\epsilon}{2}e^{it}$ for $t\in[0,2\pi]$ and note that $g\neq0$ on $\gamma$ so therefore $1/g$ is holomorphic on $\gamma$. By the [[Metric spaces#Extreme Value Theorem|EVT]], $1/g$ is bounded above on $\gamma$ and so $g$ is bounded below on $\gamma$. Now write:$$\Huge |g(z)|\geq \delta>0,\,\,\forall z\in \gamma$$
## Part 2:
Given $\tilde b\in B_\delta(b)$ notice $\forall z\in\gamma$ we have:$$\Huge |g(z)|\geq\delta>|\tilde b-b|=|g(z)-(\tilde b-b)-g(z)|>0$$by definition. This fits the conditions for Rouche's theorem to apply with $h(z)=g(z)-(\tilde b-b)$ and therefore $g,h$ have the same number of zeros inside $\gamma$. By construction $g$ has at least one zero, and so $h$ has at least one zero. Therefore $\exists\tilde a\in\gamma\subset U$ such that $h(\tilde a)=0$ however:$$\Huge\begin{align}
h(\tilde a)&=g(\tilde a)-(\tilde b-b)\\
&=f(\tilde a)-b-\tilde b+b\\
&=f(\tilde a)-\tilde b=0
\end{align}$$which implies $f(\tilde a)=\tilde b$ as required.