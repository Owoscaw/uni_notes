An action of a [[Basics of groups|group]] on a non-empty set $X$ is a [[Relating, identifying, and distinguishing groups|homomorphism]]:$$\Huge \varphi:G\rightarrow S_X$$That is, for each $g\in G$ we choose a [[Families of groups#Permutation groups|permutation]] $\varphi(g)$ of the set $X$ such that:$$\Huge \varphi(g)\circ\varphi(g)=\varphi(gh)\,\,\forall g,h\in G$$We say that the group $G$ acts on $X$. Note that $\varphi$ need not be injective or surjective.

For example take $G=(\mathbb{Z},+)$ acting on $\Re$. In this case we say:$$\Huge\begin{align}
\psi:\mathbb{Z}&\rightarrow S_\Re\\
n&\mapsto L_n\\
L_n:\Re&\rightarrow\Re\\
x&\mapsto n+x
\end{align}$$We must check if this is indeed a group action ($\psi$ is a group homomorphism). Let $m,n\in\mathbb{Z}$, we must confirm that $\psi(m)\circ\psi(n)=\psi(m+n)$:$$\Huge\begin{align}
(\psi(m)\circ\psi(n))(x)&=\psi(m)(\psi(n)(x))\\
&=\psi(m)(L_n(x))\\
&=\psi(m)(n+x)\\
&=L_m(n+x)\\
&=m+(n+x)=m+n+x\\
\psi(m+n)(x)&=L_{m+n}(x)=m+n+x
\end{align}$$So we see that this is indeed a group homomorphism, and this homomorphism is indeed a group action. We can also check another group action:$$\Huge\begin{align}
\varphi:\mathbb{Z}&\rightarrow S_\Re\\
n&\mapsto M_n\\
M_n:\Re&\rightarrow\Re\\
x&\mapsto(-1)^nx
\end{align}$$This can be verified in the same manner, and it can be shown that this is indeed a group action.

Let $X$ be the vertices of a cube, that is $X=\{v_1,\dots,v_8\}$, and consider the rotations by $\pi/2$ around an axis such that it goes through the face with $1,2,3,4$. Then we have the maps:$$\Huge\begin{align}
\mathbb{Z}\ni1&\mapsto(1\,2\,3\,4)(5\,6\,7\,8)\in S_8\\
2&\mapsto(1\,3)(2\,4)(5\,7)(6\,8)\in S_8\\
3&\mapsto(1\,4\,3\,2)(5\,8\,7\,6)\in S_8\\
4&\mapsto 0\
\end{align}$$These maps defined by $\varphi$ then satisfy $\ker(\varphi)=4\mathbb{Z}$ and $\text{im}(\varphi)=\langle (1\,2\,3\,4)(5\,6\,7\,8)\rangle<S_8$ (this is a [[Families of groups#Cyclic groups|cyclic group]]). Then the [[Relating, identifying, and distinguishing groups#First Isomorphism Theorem for groups|FIT]] states:$$\Huge \mathbb{Z}/4\mathbb{Z}\cong\text{im}(\varphi)$$Which makes sense, as along this axis the vertices with different of exactly $4$ are coupled.

# Orbits and stabilisers:

Let $\varphi:G\rightarrow S_X$ be a group action. Then for any $x\in X$ define:
> $G(x):=\{\varphi(g)(x):g\in G\}$, the orbit of $x$ inside of $X$
> $G_x:=\{g\in G:\varphi(g)(x)=x\}$, the stabiliser of $x$ in $G$

We propose that for any $x\in X$, the stabiliser subgroup $G_x$ is a subgroup of $G$. $G_x$ is non empty, so there exists some $\varphi(e)\in S_X$ that fixes every element in $X$, including $x\in X$, that implies $\varphi(e)\in G_X$. $G_x$ is closed under compositions: let $g,h\in G_X$, then $\varphi(g)(x)=x$ and $\varphi(h)(x)=x$. Now since $\varphi$ is a group action, $\varphi(gh)(x)=\varphi(g)\circ\varphi(h)(x)=\varphi(g)(x)=x$. $G_X$ is closed under inverses: Let $g\in G_X$, then $\varphi(g^{-1})(x)=\varphi(g^{-1})(\varphi(g)(x))=\varphi(g^{-1}g)(x)=\varphi(e)(x)=x$. Therefore we have the proof as required.

Take $G=\mathbb{Z}$ acting on $\Re$ with $n\in\mathbb{Z}\mapsto L_n\in S_\Re$. Given $x\in\Re$ we aim to find its orbit under $G$:$$\Huge\begin{align}
G(x)&=\{\psi(g)(x):g\in G\}\\
&=\{\psi(n)(x):n\in\mathbb{Z}\}\\
&=\{n+x:n\in\mathbb{Z}\}
\end{align}$$This is $x$ together with all of its integer shifts. We now aim to find the stabiliser of $x$ in $G$:$$\Huge\begin{align}
G_x&=\{n\in\mathbb{Z}:n+x=x\}\\
&=\{0\}
\end{align}$$Consider a different homomorphism now, defined as $\varphi:\mathbb{Z}\rightarrow\Re$ with $n\mapsto M_n$ ($M_n(x)=(-1)^nx$):$$\Huge\begin{align}
G(x)&=\{M_n(x):n\in\mathbb{Z}\}\\
&=\{(-1)^nx:n\in\mathbb{Z}\}\\
&=\{x,-x\}\\
G_x&=\{n\in\mathbb{Z}:M_n(x)=x\}\\
&=\{n\in\mathbb{Z}:(-1)^nx=x\}\\
&=\{2m:m\in\mathbb{Z}\}=2\mathbb{Z}
\end{align}$$For $x\neq0$. Note that if $x=0$ we have that $G(x)=\{0\}$ and $G_x=\mathbb{Z}$.

We introduce the notation $\varphi(g)(x)=g(x)$ and $\varphi(g)(\varphi(h)(x))=g(h(x))$, allowing us to define orbits and stabilisers as:$$\Huge\begin{align}
G(x)&=\{g(x):g\in G\}\\
G_x&=\{g\in G:g(x)=x\}
\end{align}$$
# Orbit partitions:

Let $G$ act on a set $X$ and $\varphi:G\rightarrow S_X$ be an action. Then the distinct orbits $G(x)$ for $x\in X$ partition the set $X$, that is:
> Each orbit is a non-empty subset of $X$
> The union of all orbits is the set itself, $X$
> Orbits are either disjoint or identical

Proven as follows:
1. The identity permutation $\varphi(e)$ maps $x$ to $\varphi(e)(x)=e(x)=x\in G(x)$, so $G(x)\neq\emptyset$.
2. Observe $\bigcup_{x\in X}G(x)\supset\bigcup_{x\in X}\{x\}=X$. One can show that the subset is an identity, so we have $X=\bigcup_{x\in X}G(x)$, as required.
3. Suppose $z\in G(x)\cap G(y)$. Then $z\in G(x)\implies z=\varphi(g_1)(x)$ for some $g_1\in G$ and $z\in G(y)\implies z=\varphi(g_2)(y)$ for some $g_2\in G$. Note that $\varphi(g_1)$ is a bijection of $X$ and therefore has an inverse given by $\varphi(g_1^{-1})$, which means that $\varphi(g_1^{-1})(z)=\varphi(g_1^{-1})\varphi(g_1)(x)=\varphi(g_1^{-1}g_1)(x)=\varphi(e)(x)=x$. Now we can simply substitute the definition for $z$ in to get $x=\varphi(g_1^{-1})(z)=\varphi(g_1^{-1})(\varphi(g_2)(y))=\varphi(g_1^{-1}g_2)(y)\in G(y)$. That is, every element in $G(x)$ also lies in $G(y)$. One can write for $w\in G(x)$ the following: $w=\varphi(g_3)(x)\implies w=\varphi(g_3)(\varphi(g_1^{-1}g_2)(y))=\varphi(g_3g_1^{-1}g_2)(y)\in G(y)$ to show that $G(x)=G(y)$ by symmetry.

# Group action upon itself:

Suppose that $G$ acts on $X=G$, that it $G$ acts on itself. We saw this in the proof of [[Relating, identifying, and distinguishing groups#Cayley's Theorem|Cayley's Theorem]] that with $g\in G$ acting through $L_g$ defined as $L_g(h)=gh$, equivalent to $g(h)=gh$. The orbit of $x\in X$ under $G$ is then:$$\Huge G(x)=\{gx:g\in G\}=G$$The stabiliser of $x\in X$ is then:$$\Huge G_x=\{g\in G:gx=x\}=\{e\}$$
Another such action would be conjugation:$$\Huge\begin{align}
\varphi:G&\rightarrow S_G\\
g&\mapsto\varphi(g)
\end{align}$$with $\varphi(g)(h)=ghg^{-1}$. In shorthand this is written as $g(h)=ghg^{-1}$. We claim that this is indeed a group homomorphism, and therefore defines a group action on $G$:$$\Huge\begin{align}
\varphi(gg')(h)&=(gg')h(gg')^{-1}\\
&=g(g'hg'^{-1})g^{-1}\\
&=\varphi(g)(g'hg'^{-1})=\varphi(g)\varphi(g')(h)
\end{align}$$for all $h\in G$. So we see that this is indeed a group action and $\varphi$ is a homomorphism.

# Conjugacy classes as orbits:

The conjugacy class of an element $g\in G$ is defined as:$$\Huge \text{ccl}_G(g)=\{hgh^{-1}:h\in G\}$$That is, the set of all elements in $G$ that are conjugate to $g$. The orbit under conjugation of $g\in G$ is simply the conjugacy class of $g$.

Let $S_3$ act on itself by conjugation, we then ask what are the orbits and stabilisers of the following:

| Conjucacy class | $\{e\}$ | $\{(1\,2),(2\,3),(3\,1)\}$                                                                          | $\{(1\,2\,3),(3\,2\,1)\}$                                                     |
| --------------- | ------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Stabiliser      | $G$     | $G_{(1\,2)}=\langle (1\,2)\rangle, G_{(2\,3)}=\langle(2\,3)\rangle,G_{(3\,1)}=\langle(3\,1)\rangle$ | $G_{(1\,2\,3)}=\langle(1\,2\,3)\rangle,G_{(3\,2\,1)}=\langle(3\,2\,1)\rangle$ |

Let $D_5$ be the $5$th dihedral group act on itself by conjugacy. Again we ask its orbits and stabilisers. Recall:$$\Huge\begin{align}
D_5&=\langle r,s:r^5=e,s^2=e,srs^{-1}=r^{-1}\rangle\\
&=\{r^is^j:0\leq i\leq 4,0\leq j\leq 1\}
\end{align}$$Then we have two cases for a conjugacy class, $r_i$ and $r^is$:$$\Huge\begin{align}
\text{ccl}_{D_5}(r^i)&=\{r^k(r^i)(r^k)^{-1}:0\leq k\leq 4\}\\
&\,\,\,\,\cup\{r^ks(r^i)(r^ks)^{-1}:0\leq k\leq 4\}\\
&=\{r^{k+i-k}:0\leq k\leq 4\}\\
&\,\,\,\,\cup\{r^kr^{-i}ss^{-1}r^{-k}:0\leq k\leq 4\}\\
&=\{r^i\}\cup\{r^{-i}\}=\{r^i,r^{-i}\}\\
\text{ccl}_{D_5}(r^is)&=\{r^k(r^is)r^{-k}:0\leq k\leq 4\}\\
&\,\,\,\,\cup\{r^ks(r^is)(r^ks)^{-1}:0\leq k\leq 4\}\\
&=\{r^{k+i+k}s:0\leq k\leq 4\}\\
&\,\,\,\,\cup\{r^kr^{k-i}s:0\leq k\leq 4\}\\
&=\{r^js:0\leq j\leq 4\}
\end{align}$$Note that the conjugacy class of $r^is$ is independent of $i$.