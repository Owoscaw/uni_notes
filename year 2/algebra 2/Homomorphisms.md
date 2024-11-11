
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
A ring homomorphism $f:R\mapsto S$ is [[Functions, Domain and Range#Injectivity|injective]] if and only if 