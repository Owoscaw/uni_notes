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