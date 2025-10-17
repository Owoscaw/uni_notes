
# Balls:

Let $(X,d)$ be a [[Metric spaces|metric space]], $r>0$ and $x\in X$. Then we define the open ball:$$\Huge B(x;r)=\{y\in X:d(x,y)<r\}$$This is the open ball of radius $r$ around $x$. Furthermore we define the closed ball of radius $r$ around $x$:$$\Huge D(x;r)=\{y\in X:d(x,y)\leq r\}$$

Take the metric on $\Re^n$ for $p\in[1,\infty)$ defined by:$$\Huge d_p(x,y)=\left(\sum_{i=1}^n|x_i-y_i|^p\right)^\frac{1}{p}$$The open and closed balls $B(0;1)$ and $D(0;1)$ are both defined on this metric, and can easily be visualised in $\Re,\Re^2,\Re^3$. These are generalised to the open and closed hyperspheres in $n$ dimensions.

# Open and closed sets:

We use the open ball to define a much wider class of sets. Let $X$ be a metric space. A subset $U\subset X$ is called open if for every $x\in U$ there exists $\epsilon>0$ such that $B(x;\epsilon)\subset U$. A subset $A\subset X$ is called close if $X\setminus A$ is open.

Intuitively, an open set does not contain is boundary, while a closed set does. We consider a set that only contains a portion of its boundary, it is neither open nor closed. Similarly, "clopen" sets exist.

Let $\Re$ have the Euclidean metric. Then:
> Any single point $\{x\}\in\Re$ is not open
> Any single point $\{x\}\in\Re$ is closed

To prove the first statement, for any $\epsilon>0$ consider $y=x+\frac{\epsilon}{2}$. Then $y\in B(x;\epsilon)$ but $y\notin\{x\}$, so $\{x\}$ cannot be an open set. To prove the second, consider any $y\in\Re\setminus\{x\}$. Let $\epsilon=|x-y|>0$ (since by definition, $x\neq y$). Then $x\notin B(y;\epsilon)$ so $y\in B(y;\epsilon)\subseteq\Re\setminus\{x\}$, therefore $\Re\setminus\{x\}$ is open. This makes the set $\{x\}$ closed. More generally, this is true for any single point in $\Re^n$ using the Euclidean metric. Note that this also holds for $d_p$ and $d_\infty$.

Suppose that $X$ is a metric space and $x\in N\subseteq X$. We then call $N$ a neighbourhood of $x$ if there exists an open set $V\subseteq X$ with $x\in V\subseteq N$. Using the definition of balls we write: For $x$ in a metric space $X$, $N\subseteq X$ is a neighbourhood of $x$ if and only if there is some $\epsilon>0$ such that $x\in B(x;\epsilon)\subseteq N$. Moreover a set $U\subseteq X$ is open if and only if $U$ is a neighbourhood of each $x\in U$

A neighbourhood $N$ of a point $x$ can therefore be open, closed, neither, or both. $N$ only has to include "wiggle room" for $x$.

We now prove that open balls are open and closed balls are closed:
> Let $B(x;r)$ be an open ball with $x\in X$ and $r>0$ and suppose $y\in B(x;r)$. We aim to find an open ball around $y$ with $B(x;r)$, so let $s=d(x,y)$. We then know that $s<r$ so we set $\epsilon=r-s>0$. Now we claim that $B(y;\epsilon)\subset B(x;r)$. To show this, consider $z\in B(y;\epsilon)$. Then we have that:$$\Huge\begin{align}d(z,x)&\leq d(z,y)+d(y,x)\\&<\epsilon+s\\&=(r-s)+s=r\end{align}$$So $z\in B(y;\epsilon)$ and we have that $y\in B(y;\epsilon)\subset B(x;r)$ as required.
> Now let $D(x;r)$ be a closed ball. To show that it is a closed set, we must show that $X\setminus D(x;r)$ is open. If $X\setminus D(x;r)=\emptyset$ then the proof is trivial. So assume this is not true, then we have some $y\in X\setminus D(x;r)$ with $s=d(x,y)>r$. Then we set $\epsilon=s-r>0$ and claim that $B(y;\epsilon)\subset X\setminus D(x;r)$. Let $z\in B(y;\epsilon)$, then:$$\Huge\begin{align}d(z,x)&\geq d(x,y)-d(y,z)\\&>s-\epsilon\\&=s-(s-r)=r\end{align}$$So $z\notin D(x;r)$ and we have that $y\in B(y;\epsilon)\subset X\setminus D(x;r)$ as required. Therefore $X\setminus D(x;r)$ is open, making $D(x;r)$ closed.

Let $X$ be a metric space:
> $X$ and $\emptyset$ are both open and closed
> An arbitrary union of open sets is open
> A finite intersection of open sets is open
> A finite union of closed sets is closed
> An arbitrary intersection of closed sets is closed

Proofs:
> For $x\in X$ we have $x\in B(x;1)\subseteq X$. Also since there is no $x$ in $\emptyset$, both are therefore open. Notice $X\setminus X=\emptyset$ and $X\setminus\emptyset=X$, so both have open complements and are therefore closed.
> Let $U_i\subset X$ be open for all $i\in I$. Then if $x\in \bigcup_{i\in I}U_i$ we have $x\in U_{i_0}$ for some $i_0\in I$. Therefore we have some $\epsilon>0$ such that $a\in B(x;\epsilon)\subseteq U_{i_0}\subseteq\bigcup_{i\in I}U_i$. Hence $\bigcup_{i\in I}U_i$ is open.
> Let $U_i\subset X$ be open for $1,\dots,n$. Then if $x\in\bigcap_{i=1}^nU_i$ we have $x\in U_i$ for $i=1,\dots,n$. Therefore for each $i$ there is some $\epsilon_i>0$ such that $x\in B(x;\epsilon_i)\subseteq U_i$. Let $\epsilon=\min\{\epsilon_1,\dots,\epsilon_n\}>0$. Then for $i=1,\dots,n$ we have $x\in B(x;\epsilon)\subseteq B(x;\epsilon_i)\subseteq U_i$. Hence $x\in B(x;\epsilon)\subseteq\bigcap_{i=1}^nU_i$ as required.
> Let $V_i\subset X$ be closed for $i=1,\dots,n$. Then by definition $X\setminus V_i\subseteq X$ is open for $i=1,\dots,n$ so by the above proof we know that $X\setminus(\bigcup_{i=1}^nV_i)=\bigcap_{i=1}^n(X\setminus V_i)$ is open, so $\bigcup_{i=1}^nV_i$ is closed as required.
> This proof is similar the the above.

# Continuity:

Let $(X,d)$ be a metric space. A sequence in $X$ is a function $a:\mathbb{N}\rightarrow X$, we write $(a_n)$ for the sequence where $a_n=a(n)$. Let $a\in X$, then the sequence $(a_n)_{n\in\mathbb{N}}$ converges to $a$ if for all $\epsilon>0$ there exists $n_0\in\mathbb{N}$ with $d(a,a_n)<\epsilon$ for all $n\geq n_0$. We write:$$\Huge \lim_{n\to\infty}a_n=a,\,\,a_n\to a$$
Suppose that $(X,d_X)$ and $(Y,d_Y)$ are metric spaces, $a\in X$, and $f:X\rightarrow Y$ is a function. Then the following are equivalent:
> For all $\epsilon>0$ there exists $\delta>0$ such that:$$\Huge d_X(a,x)<\delta\implies d_Y(f(a),f(x))<\epsilon$$
> For any sequence $(a_n)$ with $a_n\to^{d_X}a$ we have $f(a_n)\to^{d_Y}f(a)$
> For all open $U\subseteq Y$ with $f(a)\in U$ we have that $f^{-1}(U)$ is a neighbourhood of $a$

We prove the implications one after another.

Assume the first statement holds and we have a sequence $(a_n)\in X$ such that $a_n\to^{d_X}a$. We then aim to show that $f(a_n)\to^{d_Y}f(a)$, that is for all $\epsilon>0$ there is some $n_0\in\mathbb{N}$ such that for $n\geq n_0$ we have $d_Y(f(a_n),f(a))<\epsilon$. So let $\epsilon>0$ be given, then the firsts statement implies that some $\delta>0$ exists that satisfies $d_X(a_n,a)<\delta$ then $d_Y(f(a_n),f(a))<\epsilon$. But also since $a_n\to^{d_X}a$ there exists some $n_0\in\mathbb{N}$ such that for all $n\geq n_0$ we have $d_X(a_n,a)<\delta$. Therefore for $n\geq n_0$ we have $d_Y(f(a_n),f(a))<\epsilon$ as required.

Assume that the third statement does not hold. Then there exists some open $U$ with $f(a)\in U\subseteq X$ such that $f^{-1}(U)$ is not a neighbourhood of $a$. This means that for such $U$, there is no open set $V$ with $a\in V\subseteq f^{-1}(U)$. For all $n$, let $a_n\in B_X(a;1/n)\setminus\,f^{-1}(U)$. Since $d_X(a_n,a)<1/n$, this sequence converges to $a$. Also since $U$ is open there must exist some $\epsilon>0$ such that $B_Y(f(a),\epsilon)\subseteq U$. Hence since $f(a_n)\notin U$ we must have $d_Y(f(a_n),f(a))\geq\epsilon$ for all $n$, a contradiction. Therefore the second sequence implies the third.

Assume the third statement holds and let $\epsilon>0$. Then $B_Y(f(a);\epsilon)$ is open, so we have $f^{-1}(B_Y(f(a);\epsilon))$ is a neighbourhood of $a$. Then for some $\delta>0$ we have $a\in B_X(a;\delta)\subseteq f^{-1}(B_Y(f(a);\epsilon))$. This means that if $d_X(a,x)<\delta$ so $x\in B_X(a;\delta)$ then $x\in f^{-1}(B_Y(f(a);\epsilon))$. So $f(x)\in B_Y(f(a);\epsilon)$ and $d_Y(f(a),f(x))<\epsilon$ as required.

If a function $f$ as above satisfies the first statement, we call $f$ continuous at a point $a\in X$. If $f:X\rightarrow Y$ is continuous at all points $a\in X$ we call $f$ continuous.

A function $f:X\rightarrow Y$ is continuous if and only if $f^{-1}(U)$ is open for all open $U\subseteq Y$. To prove this, consider any open set $U\subseteq Y$. Since $f$ is continuous, for any $a\in f^{-1}(U)\subseteq X$ we have that $f^{-1}(U)$ is a neighbourhood of $a$. It follows that there is some $\epsilon>0$ such that $a\in B_X(a;\epsilon)\subseteq f^{-1}(U)$, which means that $f^{-1}(U)$ is open as required. This proves the forward implication. To prove the converse, consider any point $a\in X$ and any open set $U$ with $f(a)\in U\subseteq Y$, that is $a\in f^{-1}(U)$. Our assumption that $f^{-1}(U)$ is open means that there exists some $\epsilon>0$ such that $a\in B_X(a;\epsilon)\subseteq f^{-1}(U)$, satisfying the third statement. This means that $f$ is indeed continuous.