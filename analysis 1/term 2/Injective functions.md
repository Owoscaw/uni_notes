
A function $f:X\mapsto\Re$ is said to be strictly increasing if $\forall x,y\in X$ with $x<y$, then $f(x)<f(y)$. A strictly decreasing function can be defined similarly. Strictly increasing or decreasing functions are always injective.

Let $f:I\mapsto\Re$ be continuous and injective with $I$ as an interval. Then $f$ is either strictly increasing or decreasing. To prove this, assume that $f:I\mapsto\Re$ is neither increasing or decreasing. Then there must exist $a,b,c\in I$ with $a<b<c$ such that $f(a)<f(b)>f(c)$ or $f(a)>f(b)<f(c)$. The proofs for each of these cases are very similar, so focus on $f(a)<f(b)>f(c)$. Assume also $f(a)<f(c)$. Then $f(c)\in[f(a),f(b)]$ by the [[IVT and EVT|IVT]] there is $d\in[a,b]$ such that $f(d)=f(c)$ with $d<c$, contradicting injectivity.

For $f:X\mapsto\Re$, an injective function, there exists an inverse function $f^{-1}:f(X)\mapsto\Re$ given by $f^{-1}(y)=x$ where $x\in X$ is the unique element with $f(x)=y$. For all $x\in X,\,\,y\in f(X)$ we have that $f(f^{-1}(y))=y$ and $f^{-1}(f(x))=x$.

Let $f:I\mapsto\Re$ be a continuous injective function. Let $J=f(I)$ be the image. Then $f^{-1}:J\mapsto\Re$ is also continuous. To prove this, let $d\in J$ where $d=f(c)$ for $c\in I$. Given $\epsilon>0$ we required $\delta>0$ such that $|f^{-1}(d)-f^{}|$