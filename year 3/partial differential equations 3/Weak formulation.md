
We saw that in "simple" settings, we can find [[year 3/partial differential equations 3/Conservation laws#Breakdown of classical solutions|classical solutions to conservation laws]] up to some critical time. We would like to extend our solutions past this critical time and get some notion of a solution in $\Re\times(0,\infty)$. One issue with this is the derivatives blowing up at critical time, so we try to find a way to circumvent them. 

To do this, we can try to recast the PDE in an integral form and move the derivatives to some other function. Such functions must belong to a well behaved class in order to retain PDE information. 

Let $X\subseteq\Re^n$ and let $\varphi:X\rightarrow\Re$. The support of $\varphi$, denoted by $\text{supp}(\varphi)$, is the set defined by:$$\Huge \text{supp}(\varphi)=\overline{\{\underline{x}\in X:\varphi(\underline{x})\neq0\}}$$We say that a function $\varphi$ has compact support if this set if compact. In a sense, this function captures all of the points on which $\varphi\neq0$. Let $X\subseteq\Re^n$ and let $k\in\mathbb{N}\cup\{0\}\cup\{\infty\}$. The set $C_c^k(X)$ is defined as the set of all compactly supported functions that belong to $C^k(X)$.

For any $\epsilon>0$ we define the standard mollifier as:$$\Huge \varphi_\epsilon(x)=\begin{cases}\exp(-\frac{1}{1-(x/\epsilon)^2})&|x|<\epsilon \\
0&|x|\geq\epsilon\end{cases}$$Then $\varphi_\epsilon\in C_c^\infty(\Re)$ for all $\epsilon>0$ and $\text{supp}(\varphi_\epsilon)=[-\epsilon,\epsilon]$.