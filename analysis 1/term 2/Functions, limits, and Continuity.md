
## Open-ness? and interior points:

A subset $X\subset\Re$ is called open if for each $c\in X$ there exists in an open interval $(c-\delta,c+\delta)\subset X$ with $\delta>0$. This $\delta$ usually depends on $c$ and is not unique, if $\delta>0$ works, then every $\delta^\prime$ with $0<\delta^\prime<\delta$ also works. For example, any open interval $(a,b)$ is open since for $c\in(a,b)$ then choose $\delta=\min(c-a,b-c)$. $\emptyset$ is also open, since $\nexists c\in\emptyset$. Any closed interval $[a,b]$ is not open, $\delta$ can be found for any point except $a$ or $b$, at these points $(a-\delta,a+\delta)\not\subset[a,b]$.

A point $c\in X$ is called an interior point if there exists an open interval $(c-\delta,c+\delta)\subset X$ with $\delta>0$.

For a convergent [[Sequences#Limit of a sequence|sequence]] $(x_n)_{n\in\mathbb N}$ in the closed interval $[a,b]$, then the limit lies in $[a,b]$. This has a corollary where if the sequence is instead in the open interval $(a,b)$ then the limit lies in the closed interval $[a,b]$ also.

A subset $X\subset\Re$ define $\overline X$ be the set of all limits of convergent sequences in $X$. We call $\overline X$ the closure of $X$. $X\subset\Re$ is closed if $X=\overline X$, we always get that $X\subset\overline X$. For the closed interval $(a,b)$, then $\overline{(a,b)}\subset[a,b]$ by the above corolarry. Define a sequence $(x_n)_{n\in\mathbb N}\in(a,b)$ such that $\lim_{n\to\infty}x_n=a$. We then say $x_n=a+\frac{1}{n}$ such that for any $\delta>0$, we have $\frac{1}{n}<\delta$