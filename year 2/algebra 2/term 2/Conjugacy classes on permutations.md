
# Cycle shapes:

Let $x\in$[[Families of groups#Permutation groups|$S_n$]], $x\neq e$, be written as the product of disjoint cycles:$$\Huge x=(a_1\,a_2\,\dots\,a_{k_1})(b_1\,b_2\,\dots\,b_{k_2})\dots(t_1\,t_2\,\dots\,t_{k_r})$$where $r\geq1$ and $2\leq k_1\leq k_2\leq\dots\leq k_r$ with $n\geq k_1+\dots+k_r$. We then say that $x$ has cycle shape $[k_1,k_2,\dots,k_r]$.

Let $(i_1\,i_2\,\dots\,i_k)$ be a $k$-cycle in $S_n$. Then for any $g\in S_n$ we can write the action of $g$ on $x$ by conjugation as:$$\Huge gxg^{-1}=(g(i_1)\,g(i_2)\,\dots\,g(i_k))$$where $g$ is viewed as a permutation from the RHS. For example, the action of $g=(1\,2\,3\,5\,4)$ on $x=(2\,5\,4)$ by conjugation is $(g(2)\,g(5)\,g(4))=(3\,4\,1)$.

We prove this by considering two cases. Let $T=\{i_1,i_2,\dots,i_k\}$. Now if $j\in T$ then $j=i_r$ for some $1\leq r\leq k$ and we observe:$$\Huge gxg^{-1}(g(i_r))=gx(g^{-1}g(i_r))=g(x(i_r))=g(i_{r+1})$$which is the behavior expected by the cycle associated with this action. If $j\notin T$ then $gxg^{-1}$ leaves $g(j)$ fixed by definition:$$\Huge gxg^{-1}(g(j))=gx(g^{-1}g(j))=g(x(j))=g(j)$$As required.

# Conjugacy classes:

For $x\in S_n$, the [[Group actions#Conjugacy classes as orbits|conjugacy class]] $\text{ccl}_{S_n}(x)$ consists of all permutations which have the same cycle shape as $x$.

To prove this, notice that for $x\neq e$ in $S_n$ has form:$$\Huge x=(a_1\,\dots\,a_{k_1})(b_1\,\dots\,b_{k_2})\dots(t_1\,\dots\,t_{k_r})$$which by definition has cycle shape $[k_1,k_2,\dots,k_r]$. Then we take conjugacy by $g$:$$\large\begin{align}
gxg^{-1}&=g(a_1\,a_2\,\dots\,a_{k_1})(b_1\,b_2\,\dots\,b_{k_2})\dots(t_1\,t_2\,\dots\,t_{k_r})g^{-1}\\
&=g(a_1\,a_2\,\dots\,a_{k_1})g^{-1}g(b_1\,b_2\,\dots\,b_{k_2})g^{-1}g\dots g(t_1\,t_2\,\dots\,t_{k_r})g^{-1}\\
&=(g(a_1)\,g(a_2)\,\dots\,g(a_{k_1}))(g(b_1)\,g(b_2)\,\dots\,g(b_{k_2}))\dots(g(t_1)\,g(t_2)\,\dots\,g(t_{k_r}))
\end{align}$$which has the same cycle shape as $x$. This shows that two elements in the same conjugacy class have the same cycle shape, we now show the converse. Suppose that $x$ and $y$ have the same cycle shape as described above. We then claim that there is a bijection of $\{1,\dots,n\}$ that sends $a_1\mapsto a_1',a_2\mapsto a_2',\dots,b_1\mapsto b_1',\dots,t_1\mapsto t_1'$, elements of $x$ to $y$. The result then comes from noticing such bijection satisfies $gxg^{-1}=y$.

Take for example $S_n$ for:
> $n=4$. Conjugacy classes then consists of $1$-cycles (identity), $2$-cycles, $3$-cycles, $4$-cycles, and $[2,2]$-cycles. That is, the cycle shapes are $[1],[2],[3],[4],[2,2]$.
> $n=5$. Conjugacy classes then have all the previous cycle shapes in addition to the cycles of shape $[5]$ and $[2,3]$.
> $n=6$. Conjugacy classes then have all the previous cycle shapes in addition to the cycles of shape $[6],[2,4],[3,3],[2,2,2]$.

Note that this follows the pattern of listing all non-decreasing partitions of $n$.

In order to determine the size of a conjugacy class in $S_n$ we need the following:
>We claim that for an $m$-cycle $x=(a_1\,\dots\,a_m)\in S_n$ we get:$$\Huge |\text{ccl}_{S_n}(x)|=\frac{n(n-1)\dots(n-m+1)}{m}$$
>If $x\in S_n$ is a cycle of shape $[m_1,\dots,m_r]$ with $m_1<m_2<\dots<m_r$ with mutually different $m_i$ then the number of elements for that cycle shape is given by:$$\large\begin{align}
\gamma(n;m_1,\dots,m_r)&=\frac{n(n-1)\dots(n-m_1+1)}{m_1}\times\\
&\frac{(n-m_1)(n-m_1-1)\dots(n-m_1-m_2+1)}{m_2}\times\dots\times\\
&\frac{(n-\sum_{i=1}^{r-1}m_i)(n-\sum_{i=1}^{r-1}m_i-1)\dots(n-\sum_{i=1}^rm_i+1)}{m_r}
\end{align}$$
>If $x\in S_n$ is of general cycle shape $[m_1,\dots,m_1,m_2,\dots,m_2,\dots,m_r,\dots m_r]$ where each $m_i$ is repeated $s_i$ times and $m_1<m_2<\dots<m_r$ then the number of elements for that cycle shape is given by:$$\Huge \gamma(n;m_1,\dots,m_1,m_2,\dots,m_2,\dots,m_r,\dots,m_r)$$

Let $x\in A_n$ with $n\geq 2$, then:
> If $x$ commutes with some odd permutation, then:$$\Huge\text{ccl}_{A_n}(x)=\text{ccl}_{S_n}(x)$$
> If $x$ does not commute with any odd permutation then:$$\Huge \text{ccl}_{S_n}(x)=\text{ccl}_{A_n}(x)\cup\text{ccl}_{A_n}((1\,2)x(1\,2))$$that is, the conjugacy class in $S_n$ splits into two conjugacy classes in $A_n$ of equal size with representatives $x$ and $(1\,2)x(1\,2)$.

Prove as follows:
1. Assume $x$ commutes with some $g\in S_n$ with $g$ odd, then $gxg^{-1}=x$. We need to show that for any $y\in\text{ccl}_{S_n}(x)$ we have that $y\in\text{ccl}_{A_n}(x)$. Such $y$ has form $y=hxh^{-1}$ for some $h\in S_n$. Now either $h$ or $hg$ is an even permutation and hence in $A_n$, both of which conjugate $x$ into $y$:$$\Huge (hg)x(hg)^{-1}=hgxg^{-1}h^{-1}=hxh^{-1}=y$$Similar for $h$, proving the first statement.
2. Assume that $x$ does not commute with any odd permutation in $S_n$. Then the stabiliser of $x$ in $S_n$ is the same as the stabiliser of $x$ in $A_n$, that is $(S_n)_x=\{g\in S_n:gxg^{-1}=x\}$. By assumption this is equal to the set of even $g$ such that $gxg^{-1}=x$, equivalent to the stabiliser of $x$ in $A_n$. Then the orbit-stabiliser theorem gives that:$$\Huge |\text{ccl}_{A_n}(x)|=\frac{|A_n|}{|(A_n)_x|}=\frac{1}{2}\frac{|S_n|}{|(S_n)_x|}=\frac{1}{2}|\text{ccl}_{S_n}(x)|$$as required.

Let $H$ be a subgroup of $G$, then we have that $H$ is normal in $G$ if and only if $H$ is a union of conjugacy classes of $G$.