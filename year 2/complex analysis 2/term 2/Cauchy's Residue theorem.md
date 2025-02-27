
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