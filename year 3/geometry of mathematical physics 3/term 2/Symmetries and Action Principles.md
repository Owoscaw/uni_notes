
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


# Actions for Field Theories:

Let us now consider field theories, we now deal with functions $\phi(t,\underline{x})$ dependent on $\underline{x}$ as well as time. Consequently, equations of motion for $\phi(t,\underline{x})$ will have to involve derivatives wrt components of $\underline{x}$ as well. 

An action for a field theory with a field $\phi$ is written in terms of a Lagrangian density $\mathcal{L}$ as$$\Huge S[\phi,\partial_t\phi,\partial_i\phi]=\int\mathcal{L}(\phi,\partial_t\phi,\partial_i\phi)d^4x$$We now vary$$\Huge\begin{align*}
\phi&\rightarrow\phi+\delta\phi\\
\partial_t\phi&\rightarrow\partial_t\phi+\delta\partial_t\phi=\partial_t\phi+\partial_t\delta\phi\\
\partial_i\phi&\rightarrow\partial_t\phi+\delta\partial_i\phi=\partial_i\phi+\partial_i\delta\phi
\end{align*}$$Now we set the limits of the integral to that of a box, $t\in[t_a,t_b],x_i\in[a_i,b_i]$. The variational principal then dictates $\delta S=0$. Expanding $\delta S$ to linear order in the variation of $\phi$ gives$$\Huge\begin{align*}
0&=\delta S=\int\left(\frac{\partial }{\partial \phi}\mathcal{L}\right)\delta\phi+\left(\frac{\partial }{\partial (\partial_t\phi)}\mathcal{L}\right)\delta\partial_t\phi+\left(\frac{\partial }{\partial (\partial_i\phi)}\mathcal{L}\right)\delta\partial_i\phi\,d^4x\\
&=\int\left(\frac{\partial }{\partial \phi}\mathcal{L}\right)\delta\phi+\left(\frac{\partial }{\partial (\partial_t\phi)}\mathcal{L}\right)\partial_t\delta\phi+\left(\frac{\partial }{\partial (\partial_i\phi)}\mathcal{L}\right)\partial_i\delta\phi\,d^4x
\end{align*}$$
Similarly to how we treated systems of finitely many degrees of freedom, we now integrate the terms that involve derivatives of $\delta\phi$ by parts to get something proportional to $\delta\phi$. This gives$$\Huge0=\int\left(\left(\frac{\partial }{\partial \phi}\mathcal{L}\right)-\partial_t\left(\frac{\partial }{\partial (\partial_t\phi)}\mathcal{L}\right)-\partial_i\left(\frac{\partial }{\partial (\partial_i\phi)}\mathcal{L}\right)\right)\delta\phi\,d^4x+B$$where $B$ are the boundary terms$$\Huge\begin{align*}
B&=\int\left[\left(\frac{\partial }{\partial (\partial_t\phi)}\mathcal{L}\right)\delta\phi\right]_{t=t_a}^{t=t_b}d^3x\\
&+\int\left[\left(\frac{\partial }{\partial(\partial_3\phi)}\mathcal{L}\right)\right]_{x_3=a_3}^{x_3=b_3}dt\,dx_1\,dx_2\\
&+\int\left[\left(\frac{\partial }{\partial(\partial_2\phi)}\mathcal{L}\right)\right]_{x_2=a_2}^{x_2=b_2}dt\,dx_1\,dx_3\\
&+\int\left[\left(\frac{\partial }{\partial(\partial_1\phi)}\mathcal{L}\right)\right]_{x_1=a_1}^{x_1=b_1}dt\,dx_2\,dx_3
\end{align*}$$
We now assume that the field vanishes when approaching infinity, and send the volume of the box to infinity. This causes the boundary terms to vanish. As $\delta\phi$ was arbitrary, we conclude that the Euler-Lagrange equations for a field theory are$$\Huge\left(\frac{\partial }{\partial \phi}\mathcal{L}\right)-\partial_t\left(\frac{\partial }{\partial (\partial_t\phi)}\mathcal{L}\right)-\sum_i\partial_i\left(\frac{\partial }{\partial (\partial_i\phi)}\mathcal{L}\right)=0$$
Note that if the action $S$ depends on several fields and their derivatives, we get a Euler-Lagrange equation as above for every field. 

## Examples:
Let us consider the theory of a real scalar field $\phi$ with action$$\Huge S=\int-(\partial_t\phi)^2+(\partial_i\phi)^2+m^2\phi^2\,dt\,d^3x$$then our equation of motion for $\phi$ is$$\Huge (\partial_t^2-\underline{\nabla}^2+m^2)\phi=0$$
We can also use complex fields to write actions. Consider the theory of a complex scalar field $\phi$ with action$$\Huge S=\int-|\partial_t\phi|^2+|\partial_i\phi|^2+m^2|\phi|^2\,dt\,d^3x$$then the equation of motion is then the same as above. This is because if we treat the real and imaginary parts of $\phi$ as different fields, this is equivalent to treating $\phi,\bar\phi$ as independent fields. Then each $\phi,\bar\phi$ has the same equation of motion given above.

Consider a complex scalar field $\psi$ with action$$\Huge S=\int-|\underline{\nabla}\psi|^2+\frac{i}{2}(\bar\psi\partial_t\psi-\psi\partial_t\psi)\,dt\,d^3x$$, the equations of motion for $\bar\psi$ are then$$\Huge\begin{align*}
0&=-\partial_i\left(\frac{\partial }{\partial (\partial_i\bar\psi)}\mathcal{L}\right)-\partial_t\left(\frac{\partial }{\partial (\partial_t\bar\psi)}\mathcal{L}\right)+\left(\frac{\partial }{\partial \bar\psi}\mathcal{L}\right)\\
&=\underline{\nabla}\cdot\underline{\nabla}\psi+\frac{i}{2}\partial_t\psi+\frac{i}{2}\partial_t\psi\\
&=\Delta\psi+i\partial_t\psi
\end{align*}$$which is nothing but the [[Time evolution of QM states#Schrodinger equation motivation|Schrodinger equation]] for a free particle with $m=1/2$ and $\hbar=1$. Similarly for $\psi$ we find$$\Huge \Delta\bar\psi-i\partial_t\bar\psi=0$$
Consider an action of the form$$\Huge S=\int\mathcal{L}(\phi_I,\partial_\mu\phi_I)dt\,d^3x$$, then we have the E-L equations:$$\Huge\delta S=0\implies\frac{\partial \mathcal{L}}{\partial \phi_I}-\partial_\mu\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi)}=0$$

# Noether's theorem:

For a Lie group $G$ and representation $r$, a linear map acting on fields $\phi_I$$$\Huge\begin{align*}\phi_I\rightarrow\phi_I'&=(r(g)\underline{\phi})_I\\
\partial_\mu\phi_I\rightarrow\partial_\mu\phi_I'&=\partial_\mu(r(g)\underline{\phi})_I=(r(g)\partial_\mu\underline{\phi})_I\end{align*}$$is called a symmetry of $\mathcal{L}$ if:$$\Huge\mathcal{L}(\phi_I,\partial_\mu\phi_I)=\mathcal{L}(\phi_I',\partial_\mu\phi_I')$$
Considering infinitesimal transformations, we see the field transforms as:$$\Huge\phi_I\rightarrow\phi_I'=\phi_I+\delta_\gamma\phi_I=((\mathbb{1}+\rho(\gamma))\underline{\phi})_I$$
We can now state Noether's theorem. Let $G$ be a Lie group of symmetries of $\mathcal{L}$ acting in a representation $r$. Then: $$\Huge\partial_\mu j^\mu=0,\,\,j^\mu=(\rho(\gamma)\underline{\phi})_I\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi_I)}$$Where $j^\mu$ is known as a conserved current.

To prove this, we use the fact that the Lagrangian shouldn't vary:
> Consider:$$\Huge0=\delta_\gamma\mathcal{L}=\frac{\partial \mathcal{L}}{\partial \phi_I}\delta_\gamma\phi_I+\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi_I)}\delta_\gamma\partial_\mu\phi_I$$
> Now we notice that the first term appears in the associated equations of motion for $\mathcal{L}$:$$\Huge\implies\begin{align*}
0&=\partial_\mu\left(\frac{\partial \mathcal{L}}{\partial (\partial\mu\phi_I)}\right)\delta_\gamma\phi_I+\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi_I)}\partial_\mu\delta_\gamma\phi_I\\
&=\partial_\mu\left(\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi_I)}\delta_\gamma\phi_I\right)\\
&=\partial_\mu\left((\rho(\gamma)\underline{\phi})_I\frac{\partial \mathcal{L}}{\partial (\partial_\mu\phi_I)}\right)=\partial_\mu j^\mu
\end{align*}$$Completing the proof.


To see the physical interpretation of this theorem, we turn away from relativistic notation and integrate a conserved current over some volume $V\subset\Re^3$$$\Huge\int_V\partial_\mu j^\mu\,d^3x=\frac{\partial }{\partial t}\int_Vj^0\,d^3x+\int_V\partial_i j^i\,d^3x=0$$, where we have taken the time derivative out of the first term. Then this becomes$$\Huge\frac{\partial }{\partial t}\int_V j^0\,d^3x+\int_{\partial V}j^i\,dA^i=0$$, where $dA^i$ represents the surface element. 

Assuming our fields tend to $0$ at spatial infinity, the current $j^\mu$ must also tend to $0$ as the volume is expanded to all of $\Re^3$:$$\Huge\frac{\partial }{\partial t}\int_{\Re^3}j^0\,d^3x=0$$That is, the total charge of the system does not change with time.