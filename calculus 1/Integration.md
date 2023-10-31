## Indefinite and definite integrals:

### Indefinite:

A function $F(x)$ is called an indefinite integral or anti[[Derivative as a limit|derivative]] of a function $f(x)$ in the interval $(a,b)$ if $F(x)$ is differentiable on that interval with $F^\prime(x)=f(x)$, then we write $F(x)=\int f(x)dx$. If $F(x)$ is an indefinite integral, then so is $F(x)+c$ for any constant $c$, as this will satisfy $F^\prime(x)=f(x)$. If $F_1(x)$ and $F_2(x)$ are both indefinite integrals of $f(x)$, then $F_1(x)-F_2(x)=c$, for any constant $c$.

A function $f(x)$ is integrable in $(a,b)$ if it has an indefinite integral $F(x$) in $(a,b)$ that is [[Limits and Continuity#Continuity|continuous]] in $[a,b]$.

### Definite:

A definite integral of $f(x)$ gives the signed area under the curve of the graph of $f(x)$:
![[Integration .excalidraw]]
This area is defined as the limit of a Riemann sum, by splitting the area into rectangles:
![[Integration _0.excalidraw]]
If $f(x)$ is continuous and the rectangles are small, the method of summing rectangular areas can become a good approximation. The error can be reduced to zero by taking the limit of the size of the rectangles to zero. This limit exists if it is independent of how the rectangles are constructed to form the approximation.

A subdivision, $S$, of a closed interval $[a,b]$ is a [[Probability definition#Partitions|partition]] into a finite number of sub-intervals, the following would be a subdivision of $[a,b]$:
$$\Huge [x_0,x_1],[x_1,x_2],\dots,[x_{n-1},x_n]$$
Here, $a=x_0<x_1<x_2<\dots<x_{n-1}<x_n=b$. The norm of a subdivision, $|S|$, is the maximum of the sub-interval lengths, $|a-x_1|,|x_1-x_2|,\dots,|x_{n-1}-b|$. The numbers $z_1,z_2,\dots,z_n$ form a set of sample points from $S$ if $z_j\in[x_{j-1},x_j]$ for $j=1,\dots,n$. Now this can be used to define a Reimann sum:

Suppose that $f(x)$