
A metric space is a set $X$ together with a function $d:X\times X\mapsto\Re_{\geq0}$ such that for all $x,y,z\in X$:
>Positivity: $d(x,y)=0\iff x=y$
>Symmetry: $d(x,y)=d(y,x)$
>Triangle inequality: $d(x,y)\leq d(x,z)+d(z,y)$

$X$ is the set with elements that we want to find the distance of, and $d(x,y)$ is the distance between points $x$ and $y$. The function $d$ is called a metric, a metric space is often denoted as $(X,d)$. Examples of metrics:
> On $\Re$ or $\mathbb{C}$, $d(x,y)=|x-y|$, where $|x|$ is the modulus, or absolute value of $x$
> On $\Re^n$ or $\mathbb{C}^n$, $d_{EUC}((x_1,\dots,x_n),(y_1,\dots,y_n))=\sqrt{\sum_{i=1}^n|x_i-y_i|^2}$
> A metric on $\mathbb{C}$ can be defined by using the [[The complex plane and Riemann Sphere#The Riemann Sphere|stereographic projection]]. This is known as the Riemannian metric:$$\Huge d_{\text{Chordal}}(z,\omega)=d_{EUC}(P^{-1}(z),P^{-1}(\omega))$$This metric also works on $\hat{\mathbb{C}}$.
> The discrete metric on a set $X$ is defined as $d(x,y)=\begin{cases}0&x=y\\1&x\neq y\end{cases}$

Most of these examples were on vector spaces and said metric is derived from a notion of length. We call this notion of length a norm. Given any real or complex vector space, $V$, a function $||\cdot||:V\mapsto\Re_{\geq0}$ is a norm if it satisfies for all $v,w\in V$:
>$||v||\geq0$ and $||v||=0\iff v=0$
>$||\lambda v||=|\lambda|\cdot||v||$ for $\lambda\in\mathbb{C}$
>$||v+w||\leq||v||+||w||$

A vector space combined with a norm is called a normed vector space. Any norm induces a metric given by:$$\Huge d(v,w):=||v-w||$$

# Taxicab norm:

The $l_p$ norm, with $1\leq p<\infty$ on $\Re^n$ or $\mathbb{C}^n$ is given by:$$\Huge || \underline x||_p=\left(\sum_{i=0}^n|x_i|^p\right)^{\frac{1}{p}}$$Note that $d_{EUC}=l_2$. This norm comes from the dot product on $\Re^n$. In general if $X$ has an inner product, then $||v||=\sqrt{\left<v,v\right>}$ is a norm. Note that when $p\neq 2$, the norm does not come from an inner product.

When $p=1$ on $\Re^2$, we have that $||(x,y)||_l=|x|+|y|$. Consider the limiting case, the $l_{\infty}$ or "sup norm", on $\Re^n$:$$\Huge ||\underline x||_{\infty}=\max_{i=1,\dots,n}|x_i|$$

Let $X$ be the space of continuous functions on a given closed interval $[a,b]$. Since $X$ is a vector space, we can take the sup norm on $X$:$$\Huge ||f||_{\infty}=\sup_{x\in[a,b]}|f(x)|=_{\text{extreme value theorem}}\max_{x\in[a,b]}|f(x)|$$

# Open and closed sets:

Recall that a subset $X\subseteq\Re$ is open if for any $c\in X$ there exists $\epsilon>0$ such that:$$\Huge (c-\epsilon,c+\epsilon)\subseteq X$$Note also:$$\Huge (c-\epsilon,c+\epsilon)=\{x\in\Re:|x-c|<\epsilon\}$$This is called a ball of radius $\epsilon$ centred at $c$. This motivates the following definition. Let $(X,d)$ be a metric space, $x\in X$, and let $r>0$ be a real number. Then:
> The open ball $B_r(x)$ of radius $r$ centred at $x$ is:$$\Huge B_r(x):=\{y\in X:d(x,y)<r\}$$The closed ball $\overline{B_r(x)}$ of radius $r$ centred at $x$ is:$$\Huge \overline{B_r(x)}:=\{y\in X:d(x,y)\leq r\}$$

Let $(X,d)$ be a metric space. Then we define the following:
> A subset $U\subseteq X$ is open if for every point $x\in U$ there exists $\epsilon>0$ such that $B_\epsilon(x)\subset U$
> A subset $U\subseteq X$ is closed if its complement $U^C:=X\setminus U$ is open

Note that some sets are both open and closed.

We now prove that an open ball is indeed open. Let $y\in B_r(x)$, that is $d(x,y)<r$. Consider $\epsilon=\frac{1}{2}(r-d(x,y))>0$. We claim that $B_\epsilon(y)\subseteq B_r(x)$. Note that if $z\in B_\epsilon(y)$, then $d(x,z)\leq d(x,y)+d(y,z)<d(x,y)+\epsilon=d(x,y)+\frac{1}{2}(r-d(x,y))=\frac{1}{2}(r+d(x,y))<\frac{r+r}{2}=r$. This comes from the triangle inequality inherent to the metric space. So we have for $z\in B_\epsilon(y)$, $d(x,z)<r$, since $y\in B_r(x)$, we then have that the ball $B_r(x)$ must be open.`

Note that $[0,1)$ is not open, since there is no open interval around $0$ that is contained withing $[0,1)$. This interval is not a closed set either since the same argument exists for its complement. This is a set that is neither open nor closed with respect to the metric space $(\Re,|\cdot|)$. However using the metric space $(X,|\cdot|)$ with $X=[0,\infty)$, this set is indeed open. The notion of being open or closed is relative to the metric space.

Let $(X,d)$ be a metric space, then:
> $\bigcup_{i\in I}U_i$ is open for any collection of open sets $U_i$. Let $x\in\bigcup_{i\in I}U_i$, then $\exists i_0:x\in U_{i_0}$. Therefore $U_{i_0}$ is open, so there exists some $\epsilon>0$ such that $B_\epsilon(x)\subseteq U_{i_0}\implies B_\epsilon(x)\subseteq\bigcup_{i\in I}U_i$. Since $x$ was an arbitrary point, and this open ball is completely contained within the union, said union is also open.
> $\bigcap_{i\in I}U_i$ is open for any finite collection of open sets $U_i$. Let $x\in\bigcap_{i\in I}U_i$, so for any $i\in\{1,\dots n\}$, we have that $x\in U_i$. Since each $U_i$ is open, there exists $\epsilon_i>0$ such that $B_{\epsilon_i}(x)\subseteq U_i$. Let $\epsilon=\min_{i=1,\dots,n}\epsilon_i$, then $B_\epsilon(x)\subseteq B_{\epsilon_i}(x)\subseteq U_i$ for all $i$. Therefore $B_\epsilon(x)\subseteq\bigcap_{i=1}^nU_i$, and since the chosen $x$ was arbitrary, the finite intersection is open. 

This has a corollary for finite unions of closed sets and arbitrary intersections of closed sets both being closed. this comes from De Morgan's law:$$\Huge \left(\bigcup_{i\in I}U_i\right)^C=\bigcap_{i\in I}U_i^C,\,\,\left(\bigcap_{i\in I}U_i\right)^C=\bigcup_{i\in I}U_i^C$$
Note that infinite intersections of open sets are not necessarily open since $\bigcap_{n=1}^\infty(\frac{-1}{n},\frac{1}{n})=\{0\}$, which is not open the metric space $(\Re,|\cdot|)$. Similarly, $\bigcup_{n=2}^\infty[\frac{1}{n},1-\frac{1}{n}]=(0,1)$. This shows that an infinite union of closed sets is not necessarily closed.

# Interiors, closure, and boundaries:

Let $A$ be a subset of a metric space $(X,d)$:
> The interior, $A^0$, of $A$ is defined by $A^0:=\{x\in A:\text{there exists an open set }U\subseteq A\text{ such that }x\in U\}$
> The closure, $\overline A$, of $A$ is defined as the complement of the interior of the complement:$$\Huge \overline A:=\left(\left(A^C\right)^0\right)^C:\{x\in X:U\cap A\neq\emptyset\text{ for every open set }U\text{ with }x\in U\}$$
> The boundary, $\partial A$, of $A$ is defined as the closure without the interior:$$\Huge \partial A:=\overline A\setminus A^0=\left(A^0\right)^C\cap\left(\left(A^C\right)^0\right)^C=\left(A^0\cup\left(A^C\right)^0\right)^C$$

Note that $A^0$ is always open, $\overline A$ is always closed, and $\partial A$ is always closed. Note that in $\Re$, with $A=\{x\}$, we have $A^0=\emptyset,\overline A=\{x\},\partial A=\{x\}$.

Properties of a set $A$ in a metric space $(X,d)$:
> $A$ is open $\iff\partial A\cap A=\emptyset\iff A=A^0$, moreover:$$\Huge A^0=\bigcup_{U\subseteq A}U\,\,\text{for open } U$$
> $A$ is closed $\iff\partial A\subseteq A\iff A=\overline A$, moreover:$$\Huge \overline A=\bigcap_{A\subseteq F}F\text{ for closed }F$$
> $\partial A=\{x\in X:\text{for all open sets }U\text{ containing }x\text{, there exists }y,z\in U\text{ with }y\in A\text{ and }z\in A^C\}$ 

This is to say $A^0$ is the largest open set that is inside $A$, and $\overline A$ is the smallest closed set that contains $A$

# Convergence and Continuity:

We say a [[Sequences#Limit of a sequence|sequence]] $(x_n)_{n\in\mathbb{N}}$ in a metric space $(X,d)$ converges to $x\in X$ if we have:$$\Huge \lim_{n\to\infty}d(x_n,x)=0$$That is, if for every $\epsilon>0$ there exists $N\in \mathbb{N}$ such that $d(x_n,x)<\epsilon$ for every $n>N$. We write $x_n\to x$ as $n\to\infty$, or $\lim_{n\to\infty}x_n=x$.


## Proving complex numbers converge:
We propose that a sequence of complex numbers $(z_n)$ converges in $(\mathbb{C},|\cdot|)$ if and only if the sequences $(\Re(z_n))$ and $(\Im(z_n))$ converge in $(\Re,|\cdot|)$. This follows from the fact that $\forall z\in \mathbb{C}$:$$\Huge \max{(|\Re(z)|,|\Im(z)|)}\leq|z|\leq|\Re(z)|+|\Im(z)|$$Assume $z_n=x_n+iy_n$ converges to $z=x+iy$:$$\Huge 0\leq|x_n-x|=|\Re(z_n-z)|\leq|z_n-z|$$By our assumption, the RHS and LHS both converge to $0$, so by the sandwich theorem we have that $|\Re(z_n-z)|$ converges to $0$. So we have $x_n\to x$ and $y_n\to y$ as $n\to\infty$. That is $\lim_{n\to\infty}z_n=z\implies\Re(z_n)\to\Re(z)$ and $\Im(z_n)\to\Im(z)$. Conversely, assume $x_n\to x$ and $y_n\to y$ and aim to show $z_n=x_n+iy_n\to x+iy$:$$\Huge 0\leq|z_n-z|\leq|x_n-x|+|y_n-y|$$Both the LHS and RHS tend to $0$, so by the gentle squeeze theorem, we get that $z_n\to z$ as $n\to\infty$ and we have the statement as required.

## Convergence on the chordal metric:
Consider the sequence $(ik)_{k\in \mathbb{N}}$ in $\hat{\mathbb{C}}$ and show that it converges to $\infty\in\hat{\mathbb{C}}$ with the chordal metric:$$\Huge d(ik,\infty)=||P^{-1}(ik)-P^{-1}(\infty)||_2=\left|\left|\left(0,\frac{2k}{1+k^2},\frac{k^2-1}{1+k^2}\right)-\left(0,0,1\right)\right|\right|_2$$Where $||\cdot||_2$ represents the euclidian metric. Now:$$\Huge d(ik,\infty)=\left|\left|\left(0,\frac{2k}{1+k^2},-\frac{2}{1+k^2}\right)\right|\right|_2=\frac{2}{1+k^2}||(0,k,-1)||_2=\frac{2}{\sqrt{1+k^2}}$$This clearly tends to $0$ as $k\to\infty$, so we have that $ik\to\infty$ as $k\to\infty$

## Limit uniqueness:
Let $(X,d)$ be a metric space, then:
> A sequence can have at most one limit
> We have that $\lim_{n\to\infty}x_n=x$ if and only if for any open $U$ with $x\in U$ there exists $n\in N$ such that for $n>N$ we have $x_n\in U$. Hence the notion of a limit can be stated in terms only of its open sets.

Proof:
>Assume $x_n\to x$ and $x_n\to y$. Then for all $n\in \mathbb{N}$ we have:$$\Huge 0\leq d(x,y)\leq d(x,x_n)+d(y,x_n)$$Both sides of the inequality converge to $0$ as $n\to\infty$, so by the gentle sandwich theorem we have that $d(x,y)=0$. Therefore $\lim_{n\to\infty}d(x,y)=d(x,y)=0\implies x=y$. Therefore we have proven the first statement.
> Assume $x_n\to x$ as $n\to\infty$, this means that for any $\epsilon>0$ there exists $N\in \mathbb{N}$ such that $\forall n>N$ we have $x_n\in B_\epsilon(x)$. Let $U$ be an open set such that $x\in U$. Since $U$ is open, there exists $\epsilon>0$ such that $B_\epsilon(x)\subseteq U$. Then by definition, there exists $N\in \mathbb{N}$ such that $\forall n>N$ we have that $x_n\in B_\epsilon(x)\subseteq U$. Conversely, assume that for any $U$ open such that $x\in U$, there exists $N\in \mathbb{N}$ such that $\forall n>N$ we have that $x_n\in U$. Given $\epsilon>0$ find $N\in \mathbb{N}$ such that $\forall n>N$ we have that $x_n\in B_\epsilon(x)$

## Closure criteria
Let $(X,d)$ be a metric space. Then $A$ is a closed set if and only if for any sequence $(x_n)_{n\in \mathbb{N}}$ in $A$ that converges to an element $x\in X$ we have that $x\in A$.

# Continuity:

A map between two metric spaces $f:(X_1,d_1)\mapsto(X_2,d_2)$ is called continuous at $x_0\in X_1$ if for all $\epsilon>0$ there exists such $\delta>0$ such that for all $x\in X_1$ with $d_1(x,x_0)<\delta$ we have $d_2(f(x),f(x_0))<\epsilon$. We call a function continuous on $X_1$ if it is continuous at every point $x_0\in X_1$. That is to say a function is continuous at $x_0$ if for any $\epsilon>0\,\,\exists \delta>0$ such that $f(x)\in B_\epsilon^{(d_2)}(f(x))$ when $x\in B_\delta^{(d_1)}(x_0)$

A function $f:X\mapsto Y$ between two metric spaces is continuous at $x\in X$ if and only if:$$\Huge \lim_{n\to\infty}f(x_n)=f(x)$$For every sequence $(x_n)_{n\in \mathbb{N}}$ in $X$ such that $\lim_{n\to\infty}x_n=x$. These are the same definitions as proved [[Continuity#Continuity through sequences|here]], however they have been extended to use any metric space. Therefore we get similar consequences. For functions $f:X\mapsto Y,g:X\mapsto Y$ that are continuous, we have the following:
> Products, sums, and quotients of continuous functions on the same metric space are continuous. That is $f+g,f\cdot g,f/g$ are all continuous given a suitable definition of $+,\cdot,/$.
> Compositions of functions are continuous. That is for $h:Y\mapsto Z$, we have that $h\circ f:X\mapsto Z$ is continuous.

The proofs for these follow the same as the metric space $(\Re,||_{EUC})$, which were previously proven so have been omitted. Examples:
> $f:X\mapsto X$ defined as $f(x)=x$ is continuous. The proof is immediate by taking $\delta=\epsilon$
> Constant functions are continuous, proven by taking any $\delta>0$
> The following functions from $\mathbb{C}$ to $\mathbb{C}$ are continuous:
> > $z\mapsto\Re(z)$
> > $z\mapsto\Im(z)$
> > $z\mapsto\overline z$
> > $z\mapsto|z|$
> Note that $\arg(z)$ is not continuous on $\mathbb{C}$ regardless of the choice of $\theta$ interval. Let $z_n=e^{i(\frac{1}{n}-\pi)}$, then $\arg(z_n)=\frac{1}{n}-\pi\to-\pi$ as $n\to\infty$. However $\lim_{n\to\infty}z_n=e^{-i \pi}=-1$ and $\arg(-1)=\pi$, so $\arg(z_n)\nrightarrow\arg(z_0)$ where $z_n\to z_0$, so this function cannot be continuous.

For any function $f:X_1\mapsto X_2$ and any set $U\subseteq X_2$, the preimage of $U$ under $f$ is defined as:$$\Huge f^{-1}(U):=\{x\in X_1:f(x)\in U\}$$For metric spaces $X_1,X_2$ and $f:X_1\mapsto X_2$ a given map, the following are equivalent:
>$f$ is continuous
>$f^{-1}(U)$ is open in $X_1$ for every open set $U\subseteq X_2$
>$f^{-1}(F)$ is closed in $X_1$ for every closed set $F\subseteq X_2$

Assume $f$ is continuous and let $U\subseteq X_2$ be a given open set. For every element in $f^{-1}(U)$, there must exist an open ball centred at that point such that the ball is completely contained within the set in order for $f^{-1}(U)$ to be an open set. Let $x\in f^{-1}(U)\implies f(x)\in U$. $U$ is open, so there must exist $\epsilon>0$ such that a ball of radius $\epsilon$ around the point $f(x)$ is completely contained within $U$, that is $B_\epsilon(f(x))\subseteq U$. Since $f$ is continuous at $x$, there exist $\delta>0$ such that if $y\in B_\delta(x)$ then $f(y)\in B_\epsilon(f(x))$. This implies $B_\delta(x)\subseteq f^{-1}(B_\epsilon(f(x)))\subseteq f^{-1}(U)$, therefore $f^{-1}(U)$ is open as $x$ was arbitrary. So we have that $f$ being continuous implies that $f^{-1}(U)$ is open. 

Conversely, assume $f^{-1}(U)$ is open for all open sets $U$. Given $\epsilon>0$ and some $x\in X$, then $B_\epsilon(f(x))$ is open. This implies $f^{-1}(B_\epsilon(f(x)))$ is also open. As $x\in f^{-1}(B_\epsilon(f(x)))$ and $f^{-1}(B_\epsilon(f(x)))$ was open, then there exists a $\delta>0$ such that $B_\delta(x)\subseteq f^{-1}(B_\epsilon(f(x)))$. That is to say $f(y)\in B_\epsilon(f(x))$ when $y\in B_\delta(x)$, so we have that $f$ is continuous at arbitrary $x$, making $f$ continuous. Therefore $f^{-1}(U)\implies f$ is continuous.

The criterion for closed sets follows from the above, completing the tautology. For any $y\in X_2$ we immediately get that $f^{-1}(\{y\})$ is closed, since any singleton set is closed.

Take for example $U=\{(x,y)\in\Re^2:(x^2+y^2)\sin^3(\sqrt{x^2+7})>2\}$. The function $f(x,y)=(x^2+y^2)\sin^3(\sqrt{x^2+7})$ is continuous since is is only composition and addition of other continuous functions. We have $U=\{(x,y)\in\Re^2:f(x,y)>2\}=f^{-1}(2,\infty)$. This is the pre image of an open set on a continuous function, so we automatically get that this set is also open by the above.

# Properties of the pre-image:
> $f^{-1}(A\cup B)=f^{-1}(A)\cup f^{-1}(B)$
> $f^{-1}(A\cap B)=f^{-1}(A)\cap f^{-1}(B)$
> $f^{-1}(A\setminus B)=f^{-1}(A)\setminus f^{-1}(B)$
> $f^{-1}(A^C)=f^{-1}(Y\setminus A)=f^{-1}(Y)\setminus f^{-1}(A)=X\setminus f^{-1}(A)=(f^{-1}(A))^C$

# Sequential compactness:

A non-empty subset $K$ of a metric space $X$ is called sequentially compact if for any sequence $(x_n)_{n\in\mathbb{N}}$ in $K$ there exists a convergent [[Sequences#The Bolzano-Weierstrass Theorem|subsequence]] $(x_{n_k})_{k\in \mathbb{N}}$ with a limit in $K$. $(0,1)$ is not compact in $(\Re,|\cdot|)$, the sequence $a_n=1-\frac{1}{n}$ does not have a converging subsequence in $(0,1)$

A set $F\subseteq X$ is closed if and only if every sequence in $F$ which converges in $X$ has its limit as a point in $F$. That is to say if $(x_n)_{n\in \mathbb{N}}$ is in $F$ and $\lim_{n\to\infty}x_n=x$ for some $x\in X$, then $x\in F$. This implies a connection between being closed and sequential compactness. We get the corollaries:
> Sequentially compact sets are closed
> Any closed subset of a sequentially compact set is sequentially compact

This relies on the [[Sequences#The Bolzano-Weierstrass Theorem|Bolzano-Weierstrass Theorem]], that is if $(x_n)_{n\in \mathbb{N}}$ is a convergent sequence in a metric space $X$, then any subsequence of it converges to the same limit. $\lim_{n\to\infty}x_n=x$ by definition when $d(x,x_n)\to0$ as $n\to\infty$. Let $(x_{n_j})_{j\in \mathbb{N}}$ be a subsequence of $(x_n)$, then $(d(x_{n_j},x))_j$ is a subsequence of $(d(x_n,x))_{n\in \mathbb{N}}$. From the Bolzano-Weierstrass theorem, we know that $d(x_n,x)\to0$ implies that $d(x_{n_j},x)\to 0$ as $n,j\to\infty$. Thus $x_n\to x$ and $x_{n_j}\to x$ as $n,j\to\infty$.

Let $K$ be sequentially compact. To show that it is closed, it is enough to show that if $(x_n)_{n\in \mathbb{N}}$ is a sequence in $K$ that converges to some $x\in X$, then $x\in K$. Let $(x_n)_{n\in \mathbb{N}}\subseteq K$ such that $x_n\to x$ as $n\to\infty$. Since $K$ is compact there exists $(x_{n_j})_{j\in \mathbb{N}}$ such that $x_{n_j}\to k$ as $j\to\infty$ where $k\in K$. However $x_{n_j}\to x$ as $j\to\infty$ since $x_n\to x$ as $n\to\infty$. Therefore we say that $x=k\in K$ and have proven that a sequentially compact set is closed.

Note that closedness is not enough to be sequentially compact. For instance with $\Re$ with $|\cdot|$ is not sequentially compact

## Boundedness:
A subset $A\subseteq X$ of a metric space $X$ is said to be bounded if there exists $R>0$ and $x\in X$ such that $A\subseteq B_R(x)$. In the space $\mathbb{C}$, $A$ is bounded if and only if:$$\Huge \exists R>0:A\subseteq\{z\in \mathbb{C}:|z|<R\}\subseteq B_R(0)$$So we ask what is the link between boundedness and sequentially compactness.

Let $K\subseteq X$ be a sequentially compact subset of a metric $X$. Then $K$ is bounded.

So we ask if being bounded and closed is enough to guarantee sequential compactness. In most metric spaces, this is not true. In $\Re^n$ and $\mathbb{C}^n$, these two criteria are enough to guarantee sequential compactness, known as the Heine-Borel theorem:

## Heine-Borel:
A subset $K$ of $\Re^n$ or $\mathbb{C}^n$ is sequentially compact with respect to the standard metric if and only if it is closed and bounded.

Any sequentially compact set in any metric space is automatically bounded and closed, we show the converse for $\Re^2$ or $\mathbb{C}$. The general case follows by induction. Assume $K$ is bounded and closed. Let $(z_n)_{n\in \mathbb{N}}$ be a sequence in $K$. Writing $z_n=x_n+iy_n$ with $x_n,y_n\in \Re$ we see that:$$\Huge \max(|x_n|,|y_n|)\leq|z_n|\implies(x_n)_{n\in \mathbb{N}},(y_n)_{n\in \mathbb{N}}\text{ are bounded}$$By 