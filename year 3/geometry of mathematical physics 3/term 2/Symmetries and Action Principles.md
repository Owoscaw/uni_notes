
# Finite degrees of freedom:

Recall the [[Calculus of variations#Action principle|action principle]] for systems with finitely many degrees of freedom. Given the action$$\Huge S[q_i,\dot q_i]=\int L(q_i,\dot q_i)dt$$, the paths $q(t)$ described by this system are those of stationary action. Let us consider paths from $q(t_0)$ to $q(t_1)$. Stationary points are found by varying:$$\Huge\begin{align*}
q_i(t)&\rightarrow q_i(t)+\delta q_i(t)\\
\dot q_i(t)&\rightarrow q_i(t)+\frac{d}{dt}\delta q_i(t)=q_i(t)+\delta\dot q_i(t)
\end{align*}$$where $\delta q(t)$ is an arbitrary smooth function such that $\delta q_i(t_0)=\delta q_i(t_1)=0$. We then set$$\Huge \delta S=S[q_i+\delta q_i,\dot q_i+\delta\dot q_i]-S[q_i,\dot q_i]=0$$to find the condition on $L$:$$\Huge\begin{align*}
\delta S&=\int\frac{\partial }{\partial q_i}L(q_i,\dot q_i)\delta q_i+\frac{\partial }{\partial \dot q_i}L(q_i,\dot q_i)\delta\dot q_i\,dt\\
&=\int\frac{\partial }{\partial q_i}L(q_i,\dot q_i)\delta q_i-\frac{d}{dt}\left(\frac{\partial }{\partial \dot q_i}L(q_i,\dot q_i)\right)\delta q_i\,dt\\
&=\int\left(\frac{\partial }{\partial q_i}L\left(q_i,\dot q_i\right)-\frac{d}{dt}\frac{\partial }{\partial \dot q_i}L(q_i,\dot q_i)\right)\delta q_i\,dt
\end{align*}$$where we use IBP in the second line. The boundary term was discarded as $\delta q_i$ vanishes there.

As $\delta q_i(t)$ is an arbitrary smooth function, we hence see that paths described by the system must obey the Euler-Lagrange equation$$\Huge\frac{\partial }{\partial q_i}L(q_i,\dot q_i)-\frac{d}{dt}\frac{\partial }{\partial \dot q_i}L(q_i,\dot q_i)=0$$Note that adding a term $\frac{d}{dt}F(q,\dot q)$ to $L$ will not change the equations of motion. 

An invertible transformation of the generalised coordinates$$\Huge q_i\rightarrow q_i'=f(q_i),\,\,\dot q_i\rightarrow\dot q_i'=\dot f(q_i)$$is called a symmetry of $L$ if:$$\Huge L'=L(q_i',\dot q_i')=L(q_i,\dot q_i)+\frac{d}{dt}F(q_i,\dot q_i)$$If the symmetries of $L$ contain a [[Lie Groups and Algebras#Lie groups|Lie group]] $G$, then elements of the Lie algebra $\pmb g$ of $G$ are called infinitesimal transformations.

We restrict ourselves to linear group actions, meaning that $q_i$ transform in the representation $r$ of $G$ with$$\Huge \begin{align*}
\pmb q&\rightarrow\pmb q'=r(g)\pmb q\\
\dot{\pmb q}&\rightarrow\dot{\pmb q}'=r(g)\dot{\pmb q}
\end{align*}$$and the infinitesimal transformations act as the associated Lie algebra representation $\rho$$$\Huge\begin{align*}
\pmb q&\rightarrow\pmb q'=(1+\rho(\gamma))\pmb q\\
\dot{\pmb q}&\rightarrow\dot{\pmb q}'=(1+\rho(\gamma))\dot{\pmb q}
\end{align*}$$for every $\gamma\in\pmb g$.

## Noether's theorem
Let $G$ be a Lie group of symmetries of $L$ acting linearly on the generalised coordinates in a representation $r$. Then$$\Huge Q(\gamma)=\frac{\partial L}{\partial \dot q_i}(\rho(\gamma)\pmb q)_i-F(q,\dot q,\gamma)$$is a conserved quantity for each $\gamma\in\pmb g$. Here, $\rho$ is the Lie algebra representation associated with the group representation $r$. This is proven in the same manner as [[Symmetries, Noether's theorem, and conservation laws#Noether's theorem|first year]].

As the Lie algebra $\pmb g$ and its representation $\rho(\gamma)$ are vector spaces, we have for $a,b\in\Re$ that$$\Huge a\rho(\gamma)+b\rho(\gamma')\in\rho(\pmb g)$$and$$\Huge Q(a\gamma)+Q(b\gamma')=Q(a\gamma+b\gamma')$$
Consider the example:
> Consider a particle in $n$ dimensions in a spherically symmetric potential. Then$$\Huge S=\int\frac{m}{2}|\dot{\underline{q}}|^2-V(|\underline{q}|^2)\,dt$$
> The Lagrangian is invariant under rotations in $O(n)$ which act in the defining representation on $\pmb q$. Hence$$\Huge Q(\gamma)=m\dot{\underline{q}}\gamma\underline{q}$$is conserved for any element $\gamma$ of the Lie algebra of $O(n)$, equivalent to the Lie algebra of $SO(n)$.
> Recalling the form of the matrices in the Lie algebra of $SO(3)$ we can write$$\Huge\gamma=\sum_i\alpha_i l_i$$for $\alpha_i\in\Re$ and matrices $l_i$ with components $(l_i)_{jk}=\epsilon_{ijk}$. This gives the conserved quantity$$\Huge Q=\lambda_iL_i$$for any choice of $\lambda_i\in\Re$ and $\underline{L}=\underline{x}\times\underline{p}$. Hence each component of the angular momentum $\underline{L}$ is conserved. Note that the appearance of $\epsilon_{ijk}$ in the vector cross product is now seen to be due to the form of the matrices in the Lie algebra of $SO(3)$.

