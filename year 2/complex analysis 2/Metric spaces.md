
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

We propose that a sequence of complex numbers $(z_n)$ converges in $(\mathbb{C},|\cdot|)$ if and only if the sequences $(\Re(z_n))$ and $(\Im(z_n))$ converge in $(\Re,|\cdot|)$. This follows from the fact that $\forall z\in \mathbb{C}$:$$\Huge \max{(|\Re(z)|,|\Im(z)|)}\leq|z|\leq|\Re(z)|+|\Im(z)|$$