
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

We now prove that open balls are open and closed balls are closed