
If we imagine the force due to gravity on a mass $m$ as a conservative vector valued field over space $\underline{f}:\Re^2\rightarrow\Re^2$, we can then define the gravitational potential $g:\Re^2\rightarrow\Re$ as:$$\Huge\underline{f}=-\underline{\nabla}g$$
Let us consider a few examples:
> Let $M$ be a body of mass $M$ centered at the origin. The force due to gravity on a mass $m$ is then$$\Huge \underline{f}(r)=-\frac{GMm}{r^2}\underline{e}_r$$, where $r$ is a scalar representing the distance between the centers of mass $M,m$:$$\Huge r=||\underline{x}_M-\underline{x}_m||_{\Re^2}$$To find $g$, we assume it depends only on $r$ in the polar representation of $\Re^2$ with $(x,y)=(r\cos\theta,r\sin\theta)$ and write:$$\Huge\begin{align*}
-\frac{\partial g}{\partial r}&=\underline{f}_r=-\frac{GMm}{r^2}\\
-\frac{\partial g}{\partial \theta}&=\underline{f}_\theta=0\\
\implies g(r)&=GMm\int r^{-2}dr\\
&=-\frac{GMm}{r}+C\\
\implies V(r)&=\frac{g(r)}{m}=-\frac{GM}{r}
\end{align*}$$Because of the nature of scalar potentials, we set $C=0$ and proceed. 
> We aim to graph the equipotential lines due to a potential involving two bodies of mass $M_1,M_2$ respectively. We assume that mass $M_1$ is centered at $\underline{x}_{M_1}$ and that $M_2$ is centered at $\underline{x}_{M_2}$. Defining$$\Huge\begin{align*}
r_1(x,y)&=||\underline{x}_{M_1}-\underline{x}_m||_{\Re^2}\\
r_2(x,y)&=||\underline{x}_{M_2}-\underline{x}_m||_{\Re^2}
\end{align*}$$we can write the combined potential as:$$\Huge V_T(x,y)=-G\left(\frac{M_1}{r_1\left(x,y\right)}+\frac{M_2}{r_2(x,y)}\right)$$Equipotential curves are then found by setting $V_T(x,y)=C$ constant.

# Finding Lagrange points:

Lagrange points occur when the force due to gravity vanishes identically. We take $m=1$ in our calculations as this will just cancel later:$$\Huge\begin{align*}
\implies \underline{\nabla}g=\underline{\nabla} V_T&=0\\
\implies\underline{\nabla}\left(\frac{M_1}{r_1\left(x,y\right)}+\frac{M_2}{r_2(x,y)}\right)&=0\\
\implies\left(\underline{e}_r\frac{\partial }{\partial r}+\underline{e}_\theta\frac{1}{r}\frac{\partial }{\partial \theta}\right)\left(\frac{M_1}{r_1\left(x,y\right)}+\frac{M_2}{r_2(x,y)}\right)&=0\\
\end{align*}$$For the Earth-Sun system, we take $M_1$ to be the mass of the sun, $M_2$ to be the mass of the Earth, $\underline{x}_{M_1}=\underline{0}$ and $\underline{x}_{M_2}=(r^*,\theta^*)$:$$\Huge\begin{align*}
\left(\underline{e}_r\frac{\partial }{\partial r}+\underline{e}_\theta\frac{1}{r}\frac{\partial }{\partial \theta}\right)\left(\frac{M_1}{r}+\frac{M_2}{(r^2-2rr^*\cos(\theta-\theta^*)+{r^*}^2)^{1/2}}\right)&=0
\end{align*}$$Since this must be identically zero, let us look at the angular and radial components separately:$$\Huge\begin{align*}
\frac{1}{r}\frac{\partial }{\partial \theta}\left(\frac{M_1}{r}+\frac{M_2}{(r^2-2rr^*\cos(\theta-\theta^*)+{r^*}^2)^{1/2}}\right)&=0\\
\implies\frac{1}{r}\left(-\frac{1}{2}\frac{M_2(2rr^*\sin(\theta-\theta^*))}{(r^2-2rr^*\cos(\theta-\theta^*)+{r^*}^2)^{3/2}}\right)&=0\\
\implies\frac{M_2r^*\sin(\theta-\theta^*)}{(r^2-2rr^*\cos(\theta-\theta^*)+{r^*}^2)^{3/2}}&=0\\
\implies\theta-\theta^*&=n\pi\\
\frac{\partial }{\partial r}\left(\frac{M_1}{r}+\frac{M_2}{(r^2-2rr^*\cos(\theta-\theta^*)+{r^*}^2)^{1/2}}\right)&=0\\
\implies-\frac{M_1}{r^2}-\frac{1}{2}\frac{M_2(2r-2r^*\cos(\theta-\theta^*))}{(r^2-2rr^*\cos(\theta-\theta^*)+{r^*}^2)}&=0\\
\implies M_1(r^2-2rr^*\cos(n\pi)+{r^*}^2)^{3/2}+M_2r^2(r-{r^*}\cos(n\pi))&=0
\end{align*}$$It can be shown that the left hand bracketed term reduces to $(r-r^*\cos(n\pi))^3$, so we have:$$\Huge
\implies(r-r^*\cos(n\pi))((\sqrt{M_1}(r-r^*\cos(n\pi))^2+(\sqrt{M_2}r)^2))=0$$So we therefore get $3$ solutions for $r$ from this equation:$$\Huge r=r^*\cos(n\pi),\,\,\frac{r^*\cos(n\pi)}{1\pm\sqrt{\frac{M_2}{M_1}}}$$