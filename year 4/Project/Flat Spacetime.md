
# Special relativity recap:

Before we introduce [[Manifolds and tensors|manifolds]], we describe spacetime in the context of special relativity as a four dimensional set whose elements are labelled by $3$ spatial and $1$ temporal dimension. We call points in spacetime events, and a particle's path is written as a parametrised $1$D set of events - called the worldline. Note we will use$$\Huge\eta_{\mu\nu}=\begin{pmatrix}-1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}$$as our [[Special relativity#Relativistic notation|Minkowski metric]], allowing us to write the [[Special relativity#Lorentz transformations|invariant interval]] as:$$\Huge (\Delta s)^2=\eta_{\mu\nu}\Delta x^\mu\Delta x^\nu$$For timelike particles, this interval will clearly be negative which prompts the definition of proper time:$$\Huge (\Delta\tau)^2=-(\Delta s)^2$$This has a crucial feature:
> The proper time between two events measures the time elapsed as seen by an observer moving on a straight path between the events.

For general trajectories, proper time will differ from coordinate time. Not all of these trajectories can be made from straight line segments, so we introduce the infinitesimal interval (line element)$$\Huge ds^2=\eta_{\mu\nu}dx^\mu dx^\nu$$for infinitesimal coordinate displacements $dx^\mu$. Writing out trajectories as a [[Special relativity#Free motion|parameterised path]] $x^\mu(\lambda)$, we notice we can take the square root of the above and integrate along our path to find:$$\Large\Delta s=\int\sqrt{\eta_{\mu\nu}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda}}d\lambda,\,\,\Delta\tau=\int\sqrt{-\eta_{\mu\nu}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda}}d\lambda$$The second definition is for timelike paths, where the terms under the root would otherwise be negative. 

## Poincare group:
Writing our [[Special relativity#Relativistic notation|Lorentz transformations]] as matrices $\Lambda$, we can get the condition on $\Lambda$ that leaves our interval invariant:$$\Large\begin{aligned}
(\Delta s)^2&=(\Delta x)^T\eta(\Delta x)\,\,\text{(in matrix notation)}\\
&=(\Delta x')^T\eta(\Delta x')\\
&=(\Lambda\Delta x)^T\eta(\Lambda\Delta x)\\
&=\Delta x\Lambda^T\eta\Lambda\Delta x\\
\implies\eta&=\Lambda^T\eta\Lambda
\end{aligned}$$The set of these matrices forms the Lorentz transformation group. We further demand $\det\Lambda=1$ and $\Lambda^0_0\geq1$ to define the proper orthochronous Lorentz group $SO(1,3)^+$. The set of translations and this group forms a $10$-parameter non-abelian group called the Poincare group.

# Vectors:
To each point $p$ in spacetime, we associate the set of all possible located at that point. That is, we define the tangent space $T_p$ at $p$. Note this behaves as a real vector space, so we are nice and linear. 

Consider at each tangent space we set of four basis vectors $\hat{\underline{e}}_\mu$ with $\mu=0,1,2,3$ as usual. Any abstract vector $A$ can then be written as a linear combination:$$\Huge A=A^\mu\hat{\underline{e}}_\mu$$The coefficients $A^\mu$ here are simply the components of the vector $A$. 