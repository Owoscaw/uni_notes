Let $a,b\in\Re$ with $a<b$ and $f:[a,b]\mapsto\Re$ be a [[Continuity|continuous]] function. If $f(a)<f(b)$ and $d\in[f(a),f(b)]$ then there exists $c\in[a,b]$ with $f(c)=d$. Similarly, if $f(a)>f(b)$ and $d\in[f(b),f(a)]$ then there exists $c\in[a,b]$ with $f(c)=d$. Proof:![[IVT proof]]
If $f:X\mapsto\Re$ is continuous and $X$ is an interval and for $a,b\in X$ with $a<b$, then restrict $f$ to a function acting on the interval $[a,b]$, then the IVT shows that all values between $f(a)$ and $f(b)$ are attained. So the image of $f$ becomes itself an interval. That is to say for an interval $I$, $f:I\mapsto\Re$, then the image under $f$, $f(I)$ is also an interval. 

# Extreme value theorem:

Let $a,b\in\Re$ with $a<b$ and $f:[a,b]\mapsto\Re$ be a continuous function. Then by the above corollary we have that $f([a,b])=[c,d]$ for some $c,d\in\Re$ with $c\leq d$. In particular, $\exists u,v\in[a,b]$ with $f(u)=c,f(v)=d$. So every continuous function on a closed interval attains its minimum and maximum, and the continuous image of a closed interval is a closed interval:![[EVT proof]]
# Uniform continuity:

The definition of continuity for a function $f:X\mapsto\Re$ is such that for all $c\in X$ and all $\epsilon>0$ there exists $\delta>0$ such that for all $x\in X$ we have that $|f(x)-f(c)|<\epsilon$ whenever $|x-c|<\delta$. Now delta