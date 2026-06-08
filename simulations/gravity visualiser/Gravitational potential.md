
If we imagine the force due to gravity on a mass $m$ as a conservative vector valued field over space $\underline{f}:\Re^2\rightarrow\Re^2$, we can then define the gravitational potential $g:\Re^2\rightarrow\Re$ as:$$\Huge\underline{f}=-\underline{\nabla}g$$
Let us consider a few examples:
> Let $M$ be a body of mass $M$ centered at the origin. The force due to gravity on a mass $m$ is then$$\Huge \underline{f}(r)=\frac{GMm}{r^2}\underline{e}_r$$, where $r$ is a scalar representing the distance between the centers of mass $M,m$:$$\Huge r=||\underline{x}_M-\underline{x}_m||_{\Re^2}$$To find $g$, we assume it depends only on $r$ in the polar representation of $\Re^2$ with $(x,y)=(r\cos\theta,r\sin\theta)$ and write:$$\Huge\begin{align*}
-\frac{\partial g}{\partial r}&=\underline{f}_r=-\frac{GMm}{r^2}\\
-\frac{\partial g}{\partial \theta}&=\underline{f}_\theta=0\\
\implies g(r)&=GMm\int r^{-2}dr\\
&=-\frac{GMm}{r}+C
\end{align*}$$Because of the nature of scalar potentials, we set $C=0$ and proceed.