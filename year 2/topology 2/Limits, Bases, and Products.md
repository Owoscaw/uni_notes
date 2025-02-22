
# Limit points, interiors, and closures:

Let $X$ be a [[Topological spaces#Topologies|topological space]] and $x\in X,A\subseteq X$:
> A neighbourhood of $x$ is a set $N\subseteq X$ with open subset $U$ such that $x\in U\subseteq N$
> A point $x\in X$ is called a limit point of $A$ if every neighbourhood $N$ of $x$ satisfies:$$\Huge (N\setminus\{x\})\cap A\neq\emptyset$$

Note that a point in $A$ may or may not be a limit point of $A$, and a limit point of $A$ may or may not be in $A$. If $x$ is a limit point of $A$, then however small a neighbourhood around $x$, it must include some other point of $A$.

The point $x$ is not a limit point of $A$ if and only if there is some neighbourhood $N$ of $x$ with:$$\Huge A\cap N=\begin{cases}\{x\}&x\in A \\
\emptyset&x\notin A\end{cases}$$
Take for example $X=\Re$. Then $0\in X,(-1,1),(-2,3],$ and $[-4,5]$ are all neighbourhoods of $0$, in each case we take the open set $U=(-1,1)$.

If $U\subseteq X$ is open, then $U$ is a neighbourhood of every $x\in U$.

Let $A=\{1/n\in\Re:n\in\mathbb{Z}\setminus\{0\}\}$. Then $A$ has exactly one limit point $0$ and $0\notin A$. To check that no other point note that for given $x\neq0$, if $x\notin A$ we can find a small enough interval $(x-\epsilon,x+\epsilon)$ so that no other point of $A$ is in the interval. Each case shows that $x$ is not a limit point.

We can now define the interior and the closure of a set. First note that if for $A,B$ we have $A\subseteq B$ we can say that $A$ is smaller than $B$ or $B$ is larger than $A$. Let $X$ be a topological space with $A\subseteq X$. The interior of $A$, $A^\circ$ is the largest open set contained in $A$.  The closure of $A$, $\bar A$ is the smallest closed set containing $A$. Formally:$$\Huge A^\circ=\bigcup_{\text{open }U\subseteq A}U,\,\,\bar A=\bigcap_{\text{closed }A\subseteq C}C$$A subset $A\subseteq X$ is called dense if $\bar A=X$.

We then have the following results:
> $\overline{(X\setminus A)}=X\setminus A^\circ$
> $\bar A=X\setminus(A\setminus A^\circ)$ or $X\setminus\bar A=(X\setminus A)^\circ$, the complement of the closure of a set if the interior of its complement

To prove the first result, we know $\overline{(X\setminus A)}$ is closed and contains $X\setminus A$. Therefore its complement is an open set and lies within $X\setminus(X\setminus A)=A$. Also, $\overline{(X\setminus A)}$ is the smallest possible such closed set, so its complement must be the largest possible such open set, that is $A^\circ$. Replacing $A$ by $X\setminus A$ then gives the second result.

For example, let $\mathbb{Q}\subseteq\Re$ with the standard topology. Then $\mathbb{Q}^\circ=\emptyset$ and $\overline{\mathbb{Q}}=\Re$. To prove this, note that any non-empty subset of $\Re$ contains the open interval $(a-\epsilon,a+\epsilon)$ around each point $a\in\Re$. That is, any non-empty subset of $\Re$ contains both rational and irrational numbers. The interior of $\mathbb{Q}$ must then be an open set within $\mathbb{Q}$, which is only satisfied by $\emptyset$. The interior of $\Re\setminus\mathbb{Q}$ must then be an open set within $\Re\setminus\mathbb{Q}$ and must therefore be empty. Then by the above $\overline{\mathbb{Q}}=\Re\setminus(\Re\setminus\mathbb{Q})^\circ=\Re\setminus\emptyset=\Re$, therefore $\mathbb{Q}$ is dense in $\Re$.

Let $A\subseteq X$. Then $\bar A=A\cup\{\text{limit points of }A\}$. We prove this by showing two inclusions:
> We show that the RHS subsets the LHS by showing that $x\notin\text{RHS}\implies x\notin\text{LHS}$. Let $x\notin\bar A$, then $U=X\setminus\bar A$ is a neighbourhood of $x$. Note that $U\cap A\subseteq U\cap\bar A=\emptyset$, so $x$ is not a limit point of $A$. Clearly $x\notin A\subseteq\bar A$ so $x\notin\text{RHS}$, we have $A\cup\{\text{limit points of }A\}\subseteq\bar A$.
> We show the other subset in the same manner. Let $x\notin A\cup\{\text{limit points of }A\}$. Then $x$ has a neighbourhood $N$ with $N\cap A=\emptyset$. By definition this contains an open subset $U$ such that $x\in U\subseteq N$. Therefore $U\cap A\subseteq N\cap A=\emptyset$ and $X\setminus U$ is a closed set containing $A$. Recall that $\bar A$ is the intersection of all such closed sets, so $\bar A\subseteq X\setminus U$. Since $x\notin X\setminus U$ it follows that $x\notin\bar A$.

We extend this notion to functions. Let $f:X\rightarrow Y$ be a function between topological spaces. Then the following are equivalent:
> $f$ is continuous
> $f(\bar A)\subseteq\overline{f(A)}$ for every subset $A\subseteq X$
> $\overline{f^{-1}(V)}\subseteq f^{-1}(\bar V)$ for every subset $V\subseteq Y$

The latter two statements say that a larger set may be found by taking the closure in $Y$ rather than in $X$. Proofs:
>Continuity implies the second statement since $\overline{f(A)}$ is a closed set in $Y$ then $f^{-1}(\overline{f(A)})$ but also:$$\Huge A\subseteq f^{-1}(f(A))\subseteq f^{-1}(\overline{f(A)})$$As it is a closed set containing $A$, we have $\bar A\subseteq f^{-1}(\overline{f(A)})$. Then applying $f$ to both sides gives:$$\Huge f(\bar A)\subseteq f(f^{-1}(\overline{f(A)}))\subseteq\overline{f(A)}$$So we have that $f$ is continuous implies the second statement.
>For any $V\subseteq Y$ we have $f^{-1}(V)\subseteq X$. The second statement implies:$$\Huge f(\overline{f^{-1}(V)})\subseteq\overline{f(f^{-1}(V))}\subseteq\bar V$$Now we apply $f^{-1}$ to both sides to give:$$\Huge \overline{f^{-1}(V)}\subseteq f^{-1}(f(\overline{f^{-1}(V)}))\subseteq f^{-1}(\bar V)$$as required.
>Let $C\subseteq Y$ be closed, then $\bar C=C$ and we have:$$\Huge f^{-1}(C)\subseteq\overline{f^{-1}(C)}\subseteq f^{-1}(\bar C)=f^{-1}(C)$$which shows that $f^{-1}(C)$ is closed as required.

## The Dirichlet prime number theorem:
For coprime integers $a$ and $d$ the set $a+d\mathbb{Z}$ includes infinitely many primes.

In $\mathbb{Z}$ with Furstenberg's topology let $A=\{2,3,5,7,\dots\}$, the set of all primes. We ask what is the closure $\bar A$. We only need to find any limit points of $A$ in $\mathbb{Z}\setminus A$. We start with $0\notin A$, which is in the open set $10\mathbb{Z}$. This contains no primes, so $0$ cannot be a limit point of $A$. Now consider all $a\in A$, then $a\notin\{-1,0,1\}$, then $a$ is in the open set $a+10a\mathbb{Z}=\{\dots,-9a,a,11a,21a,\dots\}$. No element of this set is prime, so $a$ is not a limit point of $A$.

Let $M$ be a metric space with $A\subseteq M$:
> If $x$ is a limit point of $A$, there exists a sequence $(x_n)$ in $A$ such that $\lim x_n=x$
> If $x\in M\setminus A$ and there is a sequence $(x_n)$ in $A$ with $\lim x_n=x$ then $x$ is a limit point of $A$

Proofs:
> The open balls $B(x;1/n)$ are neighbourhoods of $x$. So if $x$ is a limit point of $A$ then by definition each $B(x;1/n)$ contains a point $x_n\in A$ with $x_n\neq x$. But then $d(x_n,x)<1/n\to0$ and $n\to\infty$ and hence $x_n\to x$.
> Let $x\in M\setminus A$ and let sequence $(x_n)$ have $x_n\in A$ and $\lim x_n=x$. Let $N$ be a neighbourhood of $x$. Then for some $\epsilon>0$ we have $B(x;\epsilon)\subseteq N$. Since $x_n\to x$ for some large enough $n_\epsilon$ we have $d(x_{n_\epsilon},x)<\epsilon$. Hence $x_{n_\epsilon}\in B(x,\epsilon)\cap A\subseteq N\cap A$. This shows that $x$ is a limit point of $A$.

# Bases:

In a vector space, a [[Bases and dimensions in RN|basis]] is a set of vectors from which all other vectors can be defined as a linear combination. We extend this notion to topologies. That is, a topological basis is a smaller collection of open sets from which the whole topology can be made, however we replace the notion of a linear combination with a union of those in the basis.

Let $X$ be a topological space. A basis $\mathcal{B}$ for the topology of $X$ is a collection of open sets such that every open set $U$ is the union of elements in $\mathcal{B}$. Note that this means if $p\in U$ is open, there is some $B\in\mathcal{B}$ such that $p\in B\subseteq U$.

Take for example a metric space $M$. The collection $\mathcal{B}=\{B(x;r):x\in M,r>0\}$ is a basis for the topology of $M$. This is because for an open set $U$, we know that for any $p\in U$ there exists some $r_p>0$ such that $p\in B(p;r_p)\subseteq U$. But then:$$\Huge U=\bigcup_{p\in U}\{p\}\subseteq\bigcup_{p\in U}B(p;r_p)\subseteq U$$So $U$ is the union as required.

Let $U$ be open in $\Re^n$ with the standard topology. Then for any $p\in\Re^n$ there is some $r>0$ such that $p\in B(p;r)\subseteq U$. Now we must find a set in $\mathcal{B}$ which contains $p$ and is inside $B(p;r)$. Choose $m\in\mathbb{Z}$ large enough such that $1/m<r/2$ and then since $\mathbb{Q}$ is dense in $\Re$ we can find a $q\in\mathbb{Q}^n\cap B(p;1/m)$. Then we must have $p\in B(q;1/m)$. We also claim that $B(q;1/m)\subseteq\,B(p;r)$ if $x\in B(q;1/m)$, then:$$\Huge d(x,p)\leq d(x,q)+d(q,p)<1/m+1/m<r$$by definition. We can find such $m_p,q_p$ for each $p\in U$, then as above we have:$$\Huge U=\bigcup_{p\in U}\{p\}\subseteq\bigcup_{p\in U}B(q_p;1/m_p)\subseteq\,U$$
Let $f:(X,\tau_X)\rightarrow(Y,\tau_Y)$ be a function between topological spaces with $\mathcal{B}$ a basis for $\tau_Y$. Then $f$ is continuous if and only if $f^{-1}(B)$ is in $\tau_X$ for every $B\in\mathcal{B}$. This is proven by the definition of continuity, since $\mathcal{B}\subseteq\tau_Y$. For the other direction of implication notice for any set $U\in\tau_Y$ let $(B)_{i\in I}$ be a family of sets in $\mathcal{B}$ such that $U=\bigcup_{i\in I}B_i$. Then:$$\Huge f^{-1}(U)=f\left(\bigcup_{i\in I}B_i\right)=\bigcup_{i\in I}f^{-1}(B_i)$$by assumption each $f^{-1}(B_i)\in\tau_X$ so their union must also be in $\tau_X$, as required.

Let $X$ be a set and $\mathcal{B}$ a collection of subsets of $X$ such that:
> For each $p\in X$ there is a $B\in\mathcal{B}$ with $p\in B$
> If $p\in B_1\cap B_2$ where $B_1,B_2\in\mathcal{B}$ then there is a $B_3\in\mathcal{B}$ with $p\in B_3\subseteq B_1\cap B_2$

Then there is a unique topology $\tau_{\mathcal{B}}$ on $X$ of which $\mathcal{B}$ is a basis. The conditions on $\mathcal{B}$ make sense, as the first enables $B\in\mathcal{B}$ to function as "elbow-room" sets in the topology and the second is needed for the finite intersections property of the topology to hold.

To prove this, assume $\mathcal{B}$ is a basis for some topology $\tau$. Since $\mathcal{B}\subseteq\tau$, for any family $(B_i)_{i\in I}$ in $\mathcal{B}$ we have $\bigcup_{i\in I}B_i\in\tau$. So if we define $\tau_{\mathcal{B}}=\{\bigcup_{i\in I}B_i:B_i\in\mathcal{B}\}$ for some indexing set $I$ then certainly $\tau_{\mathcal{B}}\subseteq\tau$. Also $\mathcal{B}$ is a basis for $\tau$, so every element $U$ of $\tau$ is a union of elements of $\mathcal{B}$, that is $U\in\tau_{\mathcal{B}}$. So $\tau\subseteq\tau_{\mathcal{B}}$ and we have $\tau=\tau_{\mathcal{B}}$. This proves uniqueness, we move on to show existence. Take:$$\Huge \tau_{\mathcal{B}}=\left\{\bigcup_{i\in I}B_i:B_i\in\mathcal{B}\right\}$$for some indexing set $I$. We check this satisfies the definition of a topology. First we take $I=\emptyset$ gives $\emptyset\in\tau_{\mathcal{B}}$. Also we have for each $p\in X$ there is a $B_p$ with $p\in B_p\subseteq X$  so:$$\Huge X=\bigcup_{p\in X}\{x\}\subseteq\bigcup_{p\in X}B_p\subseteq X$$It is clear that arbitrary unions of sets in $\tau_{\mathcal{B}}$ will be in $\tau_{\mathcal{B}}$ but we still need to check intersections. Suppose that $U,V\in\tau_{\mathcal{B}}$. Then there exist index sets $I,J$ such that $U=\bigcup_{i\in I}B_i,V=\bigcup_{j\in J}B_j$ so by distributivity:$$\Huge U\cap V=\left(\bigcup_{i\in I}B_i\right)\cap\left(\bigcup_{j\in J}B_j\right)=\bigcup_{(i,j)\in I\times J}(B_i\cap B_j)$$Then for each $p\in B_i\cap B_j$ there is some $B_p\in\mathcal{B}$ such that $p\in B_p\subseteq B_i\cap B_j$. Then:$$\Huge B_i\cap B_j=\bigcup_{p\in B_i\cap B_j}\{p\}\subseteq\bigcup_{p\in B_i\cap B_j}B_p\subseteq B_i\cap B_j$$Each small intersection is in fact a union so we can take a union:$$\Huge U\cap V=\bigcup_{(i,j)\in I\times J}\left(\bigcup_{p\in B_i\cap B_j}B_p\right)\in\tau_{\mathcal{B}}$$
# Product topologies:

We extend the notion of the cartesian product to general topologies. Let $X,Y$ be topological spaces. The product topology is then given by:$$\Huge \mathcal{B}_{X\times Y}=\{U\times V:U\in\tau_X,V\in\tau_Y\}$$
We must check that this is able to be a basis for a topology, that is it satisfies [[Topological spaces#Topologies|these]] conditions:
> Since $X,Y$ are both open, we know that any $(x,y)\in X\times Y\in\mathcal{B}_{X\times Y}$
> Suppose $(x,y)\in(U_1\times V_1)\cap(U_2\times V_2)$. We then need to find a single set $U_3\times V_3$ in the basis $\mathcal{B}_{X\times Y}$ such that $(x,y)\in U_3\times V_3\subseteq(U_1\times V_1)\cap(U_2\times V_2)$. Notice that:$$\Huge\begin{align}
(x,y)\in(U_1\times V_1)\cap(U_2\times V_2)&\iff x\in U_1,x\in U_2,y\in V_1,y\in V_2\\
&\iff(x,y)\in(U_1\cap U_2)\times(V_1\cap V_2)
\end{align}$$that is, $(U_1\times V_1)\cap(U_2\times V_2)=(U_1\cap U_2)\times(V_1\cap V_2)$. So we set $U_3=U_1\cap U_2$ and $V_3=V_1\cap V_2$ which we know are both open in $X,Y$ respectively by the finite intersection property for the topologies on $X,Y$ and so their product is in $\mathcal{B}_{X\times Y}$ as required.

Take for example $X=\Re,Y=\Re$, then $X\times Y=\Re^2$ and the product topology agrees with the standard topology. Let $X=S^1=Y$. Then $T^2=S^1\times S^1$ is called the torus. We also form the $n$-torus inductively for $n\geq3$ by defining:$$\Huge T^n=S^1\times T^{n-1}$$

If $X$ is a set and $\tau,\tau'$ are topologies on $X$, we say that $\tau$ is smaller than $\tau'$ if and only if $\tau\subseteq\tau'$.

To understand product spaces, it can be useful to map them back to their original "factor" spaces. Let $X,Y$ be topological spaces, we define the projection maps:$$\Huge \pi_X:X\times Y\rightarrow X,\,\pi_X(x,y)=x\text{ and }\pi_Y:X\times Y\rightarrow Y,\,\pi_X(x,y)=y$$
Then if $X\times Y$ is the given product topology:
> Projection maps $\pi_X,\pi_Y$ are continuous
> Projection maps $\pi_X,\pi_Y$ map open sets to open sets
> The product topology is the smallest topology for which both projections are continuous