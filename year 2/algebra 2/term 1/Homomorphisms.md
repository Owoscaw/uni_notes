
Let $R,S$ be two [[Rings, subrings, and fields|rings]]. A map $f:R\mapsto S$ is called a ring homomorphism if:
> $f(1)=1$, that is the identity for $R$ maps to the identity for $S$
> $f(a+b)=f(a)+f(b)$ for all $a,b\in R$
> $f(a\cdot b)=f(a)f(b)$ for all $a,b\in R$

We then get the following consequences:
> $f(0)=f(0+0)=f(0)+f(0)\implies f(0)-f(0)=f(0)+f(0)-f(0)\implies f(0)=0$
> $0=f(0)=f(a-a)=f(a+(-a))=f(a)+f(-a)\implies -f(a)=f(-a)$

We check that $f:\mathbb{Z}\mapsto(\mathbb{Z}/n)$ is a homomorphism. We have $1\mapsto\bar 1$, $\overline{a+b}=\bar a+\bar b$, and $\overline{a\cdot b}=\bar a\cdot\bar b$ so this map is indeed a homomorphism.

We define the Kernel and Image of a map to be:$$\Huge \ker(f)=\{a\in R:f(a)=0\},\,\,\text{Im}(f)=\{f(a):a\in R\}$$
We claim that $S=\left\{\begin{pmatrix}a&-b\\ b&a\end{pmatrix}:a,b\in\Re\right\}\subseteq M_2(\Re)$ is a subring of $M_2(\Re)$. For this, we require $0,I\in S$, closure under addition, and closure under multiplication. $0\in S$ with $a=b=0$, and $I\in S$ with $a=1$, $b=0$. So we check closure under multiplication:$$\Huge\begin{align}
\begin{pmatrix}a&-b\\b&a\end{pmatrix}\begin{pmatrix}c&-d\\d&c\end{pmatrix}=\begin{pmatrix}ac-bd&-(ad+bc)\\ad+bc&ac-bd\end{pmatrix}\in S
\end{align}$$So we have closure under multiplication. It is trivial to show closure under addition. So we have that $S\subseteq M_2(\Re)$ is indeed a subring. We define the map:$$\Huge\begin{align}
f:\mathbb{C}&\mapsto S\\
a+bi&\mapsto \begin{pmatrix}a&-b\\b&a\end{pmatrix}
\end{align}$$And claim that such a map is a homomorphism. We see that $f(1)=I$, so the identity maps to the identity. We also have:$$\Huge\begin{align}
f((a+bi)+(c+di))&=f((a+c)+(b+d)i)\\
&=\begin{pmatrix}a-c&-(b+d)\\b+d&a+c\end{pmatrix}\\
&=\begin{pmatrix}a&-b\\b&a\end{pmatrix}+\begin{pmatrix}c&-d\\d&c\end{pmatrix}\\
&=f(a+bi)+f(c+di)
\end{align}$$That is, the map is additive. Also:$$\Huge\begin{align}
f((a+bi)(c+di))&=f((ac-bd)+(ad+bc)i)\\
&=\begin{pmatrix}ac-bd&-(ad+bc)\\ad+bc&ac-bd\end{pmatrix}\\
&=\begin{pmatrix}a&-b\\b&a\end{pmatrix}\begin{pmatrix}c&-d\\d&c\end{pmatrix}\\
&=f(a+bi)f(c+di)
\end{align}$$So the map is multiplicative. Therefore we conclude that the map is a homomorphism.

# Isomorphism:

We say that two rings $R$ and $S$ are isomorphic if there exists a [[Functions, Domain and Range#Bijectivity|bijective]] ring-homomorphism $f:R\mapsto S$ between $R$ and $S$. If such a map $f$ exists, we write:$$\Huge R\cong S$$
A ring homomorphism $f:R\mapsto S$ is [[Functions, Domain and Range#Injectivity|injective]] if and only if $\ker(f)=\{0\}$. To prove this, recall injectivity implies $f(x)=f(y)\implies x=y$. Assume $f$ is injective and let $x\in\ker(f)$, that is $f(x)=0\implies f(x)=f(0)\implies x=0$, therefore $\ker(f)=\{0\}$. Assume $\ker(f)=\{0\}$ and consider $x,y\in R$ with $f(x)=f(y)$, this implies $f(x)-f(y)=0=f(x)+f(-y)=f(x-y)=0\implies x-y\in\ker(f)\implies x-y=0\implies x=y$, so we have injectivity and the proof is complete.

Note that $f:\mathbb{C}\mapsto S$ with $S$ as above we can see that $f(a+bi)=0\implies \begin{pmatrix}a&-b\\b&a\end{pmatrix}=\begin{pmatrix}0&0\\0&0\end{pmatrix}\implies a=b=0$, so $\ker(f)=\{0\}$, one can also show that $f$ is surjective and conclude that $\mathbb{C}\cong S$.

# Ring products:

Let $R$ and $S$ be rings. We define the product of $R$ and $S$ as:$$\Huge R\times S=\{(r,s):r\in R,s\in S\}$$We then have:
> $(r_1,s_1)+(r_2,s_2)=(r_1+r_2,s_1+s_2)$
> $(r_1,s_1)\cdot(r_2,s_2)=(r_1\cdot r_2,s_1\cdot s_2)$

These satisfy the properties required to be a ring with the identity for $R\times S$ as $(1_R,1_S)$. We then define two ring homomorphisms:$$\Huge\begin{align}
P_1:R\times S\mapsto R,\,\,(r,s)\mapsto r\\
P_2:R\times S\mapsto S,\,\,(r,s)\mapsto s
\end{align}$$
Note $\ker P_1=\{(r,s)\in R\times S:P_1(r,s)=0\}$ and $\ker P_2=\{(r,s)\in R\times S:P_2(r,s)=0\}$, here $P_1$ is invariant for any $s\in S$ and $P_2$ is invariant for any $r\in R$, therefore $\ker P_1=\{(0,s):s\in S\},\ker P_2=\{(r,0):r\in R\}$.
