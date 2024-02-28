
# Step functions:

A function on a closed interval $[a,b]$ is called a step function if there exists a partition:$$\Huge a=x_0<x_1<\dots<x_{N-1}<x_N=b$$of $[a,b]$ such that $f$ is constant on each subinterval $(x_k,x_{k+1})$ for $k=0,\dots,N-1$. Note each $f(x_k)$ is arbitrary in value. We then immediately get the following properties:
> Let $f,g$ be two step functions on $[a,b]$ and $c\in\Re$, then $cf$ and $f+g$ are also step functions. Therefore step functions form a vector space
> The product $fg(x)=f(x)g(x)$ is also a step function
> The absolute value $|f|(x)=|f(x)|$ is also a step function

Let $f$ be a function on a closed interval $[a,b]$. $f$ is a regulated function if there exists a sequence of step functions $f_n$ converging [[Sequences of functions, uniform convergence, and Limit theorems#Uniform convergence preserves continuity|uniformly]] to $f$. That is for all $\epsilon>0$ there exists $N\in \mathbb{N}:|f_n(x)-f(x)|<\epsilon$ for all $x\in[a,b]$ and $n\geq N$.

Let $f$ be a function on a compact interval $[a,b]$. Then $f$ is regulated if and only if for all $\epsilon>0$ there exists a step function $g$ on $[a,b]$ such that $|f(x)-g(x)|<\epsilon$ for all $x\in[a,b]$. Assume that $f$ is regulated, then there is a sequence $(g_n)_{n\in \mathbb{N}}$ of step functions converging uniformly to $f$. Given $\epsilon>0$ then there is $N$ that satisfies the definition for a regulated function, taking $g=g_n$. So we get the forwards implication. For $n\in \mathbb{N}$ take $\epsilon=\frac{1}{n}$, and take $g_n=g$ where $g$ satisfies $|f(x)-g(x)|<\epsilon$. Given $\epsilon>0$ take $N$ with $\frac{1}{N}<\epsilon$. Then for $n\geq N$ we have $\frac{1}{n}\leq \frac{1}{N}<\epsilon$ and we get the statement as required.

Let $f$ be a continuous function on $[a,b]$. Then $f$ is regulated. Since $f$ is continuous on $[a,b]$, it is uniformly continuous on the same interval. For all $\epsilon>0$ there exists $\delta>0$ such that for all $x,y\in[a,b]$ we have that $|x-y|<\delta\implies|f(x)-f(y)|<\epsilon$. So take $\epsilon>0$ and use $\delta>0$ from uniform continuity and let $a=x_0<x_1,\dots<x_{N-1}<x_N=b$ be a partition of $[a,b]$