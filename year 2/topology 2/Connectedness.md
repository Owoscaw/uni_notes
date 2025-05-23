
Let $A$ and $B$ be subsets of $X$. We call $A$ and $B$ complementary subsets of $X$ if $A\cup B=X$ and $A\cup B=\emptyset$. A separation of a [[Topological spaces#Topologies|topological space]] $X$ is a pair of complementary subsets of $X$ which are both open and non-empty. Take for example the following, which are complementary subsets of $\Re$:
> $A=(-\infty,3), B=[3,\infty)$
> $A=\bigcap_{k\in\mathbb{Z}}[2k,2k+1],B=\bigcap_{k\in\mathbb{Z}}(2k+1,2k)$
> $A=\Re,B=\emptyset$

However none of these are separations, as the first two have a non-open set and the last has an empty set.

A topological space $X$ is called connected if there is no separation in $X$:
> $\mathbb{Q}$ is not connected as $L=\mathbb{Q}\cap(-\infty,\sqrt{2}),M=\mathbb{Q}\cap(\sqrt{2},\infty)$ are both open in $\mathbb{Q}$ and non-empty. Since $L\cup M=\mathbb{Q}$ and $L\cap M=\emptyset$, $L$ and $M$ form a separation of $\mathbb{Q}$ and so it is not connected.
> $\Re$ is connected. We show this by contradiction, so assume that $U,V$ form a separation of $\Re$. Now let $x\in U,y\in V$ and assume $x<y$ WLOG. We define:$$\Huge A=\{a\in[x,\infty):[x,a]\subseteq U\}$$We see that both $x\in A$ and $a\in A$ implies $a<y$, so $y$ is an upper bound for this set. Therefore $A$ has a supremum that we label $s=\sup A$. We consider the two possibilities $s\in U$ or $s\in V$:
> > If $s\in U$ then as $U$ is open there exists some $\epsilon>0$ such that $(s-\epsilon,s+\epsilon)\subseteq U$. $s-\epsilon$ is by definition not an upper bound so there must exist some $a>s-\epsilon$ that belongs to $A$. That is, $[x,a]\subseteq U$. Also $(s-\epsilon,s+\epsilon/2]\subseteq(s-\epsilon,s+\epsilon)\subseteq U$, the union $[x,s+\epsilon/2]\subseteq U$ and therefore $s+\epsilon/2\in A$ and $s$ cannot be an upper bound for $A$.
> > If $s\in V$ then as $V$ is open there exists some $\epsilon>0$ such that $(s-\epsilon,s+\epsilon)\subseteq V=X\setminus U$. Therefore for $b\in(s-\epsilon,s+\epsilon),b\notin U$ which means that $[x,b]\not\subseteq U$ and $b\notin A$. Therefore $s-\epsilon$ is the upper bound for $A$ and $s$ is not the supremum.
> Both cases lead to a contradiction, so $\Re$ is connected.


If $h:X\rightarrow Y$ is continuous and $X$ is connected then $h(X)\subseteq Y$ is also connected, that is to say continuity preserves connectedness. We prove this by contradiction, so assume $h(X)$ has a separation $U,V$. We claim that $h^{-1}(U),h^{-1}(V)$ then form a separation of $X$. We have that $U\cup V=h(X)$ so we can apply $h^{-1}$ to both sides to get $h^{-1}(U)\cup h^{-1}(V)=h^{-1}(h(X))=X$. We have that $U\cap V=\emptyset$, so $h^{-1}(U)\cap h^{-1}(V)=h^{-1}(\emptyset)=\emptyset$. We must now show that $h^{-1}(U),h^{-1}(V)$ are open in $X$. Since $h(X)$ has the subspace topology from $Y$, $U$ and $V$ being open in $h(X)$ is equivalent to $U=U'\cap h(X)$ and $V=V'\cap h(X)$ for some open $U',V'$ that are open in $Y$. Then:$$\Huge\begin{align}
h^{-1}(U)&=h^{-1}(U'\cap h(X))=h^{-1}(U')\\
h^{-1}(V)&=h^{-1}(V'\cap h(X))=h^{-1}(V')
	\end{align}$$And since $h$ is continuous, both of these sets are open in $X$. This forms the separation on $X$, which is a contradiction. Therefore there must not be a separation in $h(X)$.

This has a corollary that states for a homeomorphism $h:X\rightarrow Y$ with $X$ connected, $Y$ is connected. This is simply an application of the above with $h(X)=Y$.

If $X$ is a topological space then we call a subset $A\subseteq X$ clopen if it is both closed and open.

Let $X$ be a topological space, then the following form a tautology:
> $X$ is connected
> The only clopen subsets of $X$ are $\emptyset, X$
> There is no continuous surjective function from $X$ to a discrete space with more than one point

Proofs:
1. The first and second statements are equivalent as if there is a clopen subset $A\subseteq X$ with $A\neq\emptyset,X$ then $A$ and $X\setminus A$ form a separation. Also if $U,V$ is a separation of $X$ then $U,V$ are both clopen and non-empty. Therefore the first and second statements are equivalent.
2. The first and third statements are equivalent as for connected $X$ and continuous, surjective $f:X\rightarrow Y$ where $Y$ has at least two elements and the discrete topology it is trivial that $Y$ is not connected, however by continuity preserves connectedness $Y$ is connected. This is a contradiction, so no such $f$ exists. 
3. Suppose there exists a separation $U,V$. Let $Y$ be the set $\{0,1\}$ with the discrete topology and define:$$\Huge f(x)=\begin{cases}0&x\in U\\1&x\in V\end{cases}$$then $f$ is surjective and continuous, so the first and third statements are equivalent.

Take for example:
>$GL_n(\Re)$ is not connected as the function $\det:GL_n(\Re)\rightarrow\Re\setminus\{0\}$ is continuous and surjective so by the above we must have that if $GL_n(\Re)$ is connected, so is $\Re\setminus\{0\}$. However this has a separation, $(-\infty,0),(0,\infty)$ and therefore $GL_n(\Re)$ is not connected.
>$(0,1)$ is connected as it is homeomorphic to $\Re$ and $\Re$ is connected, since homeomorphism preserves connectedness this set is also connected.

# Components and path-connectedness:

Let $X$ be a topological subspace, $Z\subseteq X$ be connected, and $Y\subseteq X$ with $Z\subseteq Y\subseteq\bar Z$. Then $Y$ is connected, in particular the closure of a connected set is connected. Proof:
> Let $A,A'$ be complementary open sets of $Y$. Since $Y$ has the induced topology from $X$, there are open sets $U,U'$ in $X$ such that $A=U\cap Y$ and $A'=U'\cap Y$. Now $Z\subseteq Y$ so we have:$$\Huge\begin{align}
Z=Y\cap Z&=(A\cup A')\cap Z\\
&=(A\cap Z)\cup(A'\cap Z)\\
&=((U\cap Y)\cap Z)\cup((U'\cap Y)\cap Z)\\
&=(U\cap(Y\cap Z))\cup(U'\cap(U\cap Z))\\
&=(U\cap Z)\cup(U'\cap Z)
\end{align}$$However since $Z\subseteq Y$ we must have:$$\Huge (U\cap Z)\cup(U'\cap Z)\subseteq (U\cap Y)\cup(U'\cap Y)=A\cap A'=\emptyset$$So we have that $U\cap Z$ and $U'\cap Z$ are complementary open subsets of $Z$. Since $Z$ is connected, it has no separation and these subsets must be trivial. WLOG we assume $U\cap Z=Z$ and $U'\cap Z=\emptyset$. It follows that $Z\subseteq X\setminus U'$, which is closed, and $Y\subseteq \bar Z\subseteq X\setminus U'$. Therefore $A'=Y\cap U'=\emptyset$ and $A=Y\cap U=Y$. Therefore $Y$ has no separation and is therefore connected.

Let $\mathcal{A}=\{A_i:i\in I\}$ be a collection of subsets of $X$ such that $\bigcup_{i\in I}A_i=X$. Assume each $A_i$ is connected and for each $i,j\in I$ we have $A_i\cap A_j=\emptyset$. Then $X$ is connected. Proof:
 > Let $U,V$ be complementary open sets for $X$. If we fix some $i_0\in I$ then $U\cap A_{i_0}$ and $V\cap A_{i_0}$ are complementary open sets for $A_{i_0}$. Since this is connected, we assume WLOG that $U\cap A_{i_0}=A_{i_0}$ and $V\cap A_{i_0}=\emptyset$. Similarly for any $i\in I$ we have that $U\cap A_i$ and $V\cap A_i$ must be trivial. Note that $(U\cap A_i)\cap A_{i_0}=(U\cap A_{i_0})\cap A_i=A_{i_0}\cap A_i\neq\emptyset$ and hence $U\cap A_i\neq\emptyset$ so we must have $U\cap A_i=A_i$. We now know that every $A_i\subseteq U$, so $X=\bigcup_{i\in I}A_i\subseteq U\subseteq X$. We can therefore conclude that $X=U,V=\emptyset$ and therefore $X$ is connected.
 
If $X$ and $Y$ are connected, then [[Limits, Bases, and Products#Product topologies|$X\times Y$]] is connected. Proof:
> Choose any $p\in X,q\in Y$. Then $\{p\}\times Y\cong Y$ and $X\times\{q\}\cong X$. So both $\{p\}\times Y$ and $X\times\{q\}$ are connected and since they intersect at $(p,q)$ their union $(\{p\}\times Y)\cup(X\times\{q\})$ is connected. Now fix $p$ but let $q$ vary over $Y$ which gives the whole product space:$$\Huge \bigcup_{q\in Y}(\{p\}\times Y)\cup(X\times \{q\})=X\times Y$$Which is a union of connected sets in which every pair intersects in $\{p\}\times Y$, so the whole product topology is also connected.

Take the following as examples:
> $\Re^n$ is connected as $\Re$ is connected, and $\Re^n$ is simply a repeated product of $\Re$
> $B^n=\{x\in\Re^n:d_2(0,x)<1\}$ is connected, as this set is homeomorphic to $\Re^n$
> $D^n=\{x\in\Re^n:d_2(0,x)\leq1\}$ is connected, as $D^n=\overline{B^n}$ and the closure of a connected set is also connected
> $S^n=\{x\in\Re^{n+1}:d_2(0,x)=1\}$ is connected for $n\geq1$. To prove this, we write the set as the union $S^n=U^n\cup L^n$ where $U^n=S^n\cap\{x\in\Re^{n+1}:x_1\geq0\}$ and $L^n=S^n\cap\{x\in\Re^{n+1}:x_1\leq0\}$. We then claim that both $U^n,L^n$ are homeomorphic to $D^n$. The obvious homeomorphism to use is:$$\Huge\begin{align}
h&:U^n\rightarrow D^n\\
h(x_1,x_2,\dots,x_{n+1})&=(x_2,\dots,x_{n+1})\\
h^{-1}&:D^n\rightarrow U^n\\
h^{-1}(x_2,\dots,x_{n+1})&=(\sqrt{1-x_2^2-\dots-x_{n+1}^2},x_2,\dots,x_{n+1})
\end{align}$$with the negative square root for $L^n$. Since $D^n$ is connected and this is a homeomorphism, both $U^n,L^n$ are connected and:$$\Huge U^n\cap L^n=\{(0,x_2,\dots,x_{n+1}:x_2^2+\dots+x_{n+1}^2=1\}\neq\emptyset$$So as $S^n$ is the union of two connected sets with non-empty intersection, $S^n$ itself is connected.

A component of a topological space $X$ is a maximal connected subset of $X$. We then have:
> Each point $p$ of $X$ is in a unique component
> If $C_1,C_2$ are different components, then $C_1\cap C_2=\emptyset$
> $X$ is the union of its components
> Each component is closed in $X$

Proofs:
1. We first show that each $p\in X$ is in some component. Let:$$\Huge C_p\{x\in X:\exists\text{ connected subset }U_x\text{ with }x,p\in U_x\}$$It is trivial that $p\in C_p$. Also if $y\in U_x$ then $y\in C_p$ so every $U_x$ is a subset of $C_p$:$$\Huge C_p=\bigcup_{x\in C_p}\{x\}\subseteq\bigcup_{x\in C_p}U_x\subseteq C_p$$So all of these are equal. All $U_x$ intersect in $p$, so we have a union of pairwise intersecting connected sets, which must also be connected. By construction $U_x$ is maximal so is a component containing $p$, as required.
2. Let $C_1$ and $C_2$ be two different components of $X$ and suppose $C_1\cap C_2\neq\emptyset$. Then each $p\in C_1\cup C_2$ is an element of two distinct components, contradicting the first statement.
3. If each point $p$ is in component $C_p$ then:$$\Huge X=\bigcup_{p\in X}\{p\}\subseteq\bigcup_{p\in X}C_p\subseteq X$$
4. If a component $C$ is connected, so is its closure $\bar C$. Therefore if $C$ is maximally connected by definition, we must have $C=\bar C$.

Examples:
> If $X$ is connected, $X$ itself is the only component
> If $X$ is discrete, each point is a component and any discrete space with more than one component is not connected, while singleton sets are connected

## Paths:
A path in a topological space $X$ is a continuous function $\gamma:[0,1]\rightarrow X$. In this case we say that $\gamma$ is a path from $\gamma(0)$ to $\gamma(1)$. A topological space is called oath connected if for any two points $p,q\in X$, there is a path from $p$ to $q$.

A path connected space is connected. Fix some $p\in X$ and then for each $q\in X$ let $\gamma_q:[0,1]\rightarrow X$ be a path from $p$ to $q$. As an interval, $[0,1]$ is connected so as $\gamma_q$ is continuous each $\gamma_q([0,1])$ is also connected. Since any of the two paths intersect in $p$, the union of all paths is connected:$$\Huge X=\bigcup_{q\in X}\{q\}=\bigcup_{q\in X}\{\gamma_1(1)\}\subseteq\bigcup_{q\in X}\gamma_q([0,1])\subseteq X$$So all are equal and $X$ is connected. 

However not all connected sets are path connected, take for example:$$\Huge Z=\left\{\left(x,\sin\left(\frac{1}{x}\right)\right)\in\Re^2:0<x\leq1\right\}$$Then the closure $\bar Z$ is connected but not path connected. First we note that $Z$ itself is path connected as a path in $Z$ from $(x_1,\sin(1/x_1))$ to $(x_2,\sin(1/x_2))$ is $\gamma:[0,1]\rightarrow Z$ with:$$\Huge \gamma(t)=\left(x_1+(x_2-x_1)t,\sin\left(\frac{1}{x_1+(x_2-x_1)t}\right)\right)$$Therefore $Z$ is path connected and therefore connected. Since the closure of a connected set is connected, we have that $\bar Z$ is also connected. It is clear that any point $(0,y)$ with $-1\leq y\leq 1$ is a [[Limits, Bases, and Products#Limit points, interiors, and closures|limit point]] of $Z$. Suppose that $\bar Z$ is path connected, then there is a path $\gamma:[0,1]\rightarrow\bar Z$ from $(0,0)$ to $(1,\sin(1))$. We can project this path onto th $x$-axis using [[Limits, Bases, and Products#Product topologies|$\pi_x$]] so then $\pi_x\circ \gamma:[0,1]\rightarrow[0,1]$. Since $\pi_x\circ\gamma(0)=0$ , $\pi_x\circ\gamma(1)=1$, and $\pi_x\circ\gamma$ is continuous, the IVT states that there is some $t_1\in[0,1]$ such that:$$\Huge \pi_x\circ\gamma(t_1)=\frac{2}{\pi},\,\,\gamma(t_1)=\left(\frac{2}{\pi},\sin(\frac{\pi}{2})\right)=\left(\frac{2}{\pi},1\right)$$Then applying the IVT again there is some $t_2\in[0,t_1]$ such that:$$\Huge \pi_x\circ\gamma(t_2)=\frac{2}{2\pi},\,\,\gamma(t_2)=\left(\frac{2}{2\pi},\sin(\frac{2\pi}{2})\right)=\left(\frac{2}{2\pi},0\right)$$And once more to state that there is some $t_3\in[0,t_2]$ such that:$$\Huge \pi_x\circ\gamma(t_3)=\frac{2}{3\pi},\,\,\gamma(t_3)=\left(\frac{2}{3\pi},\sin\left(\frac{3\pi}{2}\right)\right)=\left(\frac{2}{3\pi},-1\right)$$Continuing in this manner gives a sequence $t_n\in[0,1]$ with $t_1>t_2>\dots>t_n>\dots$ for which each $\pi_x\circ\gamma(t_n)=\frac{2}{n\pi}$. This is a sequence decreasing and bounded below by $0$ so must converge. Let such limit be $t^*=\lim_{n\to\infty}(t_n)$. Now think about projecting onto the $y$-axis. The composition $\pi_y\circ\gamma$ is also continuous so we must have $\lim_{n\to\infty}\pi_y\circ\gamma(t_n)=\pi_y\circ\gamma(t^*)$, however we have chosen $t_n$ such that:$$\Huge \pi_y\circ\gamma(t_n)=\sin\left(\frac{1}{\frac{2}{n\pi}}\right)=\sin\left(\frac{n\pi}{2}\right)$$which is an oscillating function and does not converge, leading to contradiction. Therefore $\bar Z$ is not path connected.