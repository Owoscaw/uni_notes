
# The Riemann curvature tensor:

We are now prepared to discuss curvature in a meaningful way, quantified by the Riemann curvature tensor which is derived from the connection. The notion of curvature comes from how we differ from the "flat" metric. These "flat" metrics have a number of properties that we take as manifestations of "flatness":
> [[year 4/Project/Geodesics#Parallel transport|Parallel transportation]] around closed loops leaves a vector unchanged.
> [[Covariant derivative|Covariant derivatives]] of tensors commute.
> Initially, parallel geodesics remain parallel.

The Riemann tensor arises when we study these properties in more general contexts. We saw that parallel transport around a closed loop on curved space introduces some transformation on the vector, which will be dependent on the total curvature enclosed by the loop:![[Geodesics 2026-11-17 13.52.27.excalidraw]]

Therefore we look for a measure of local curvature at each point, and we will find it in the form of the Riemann curvature tensor. We can make a guess at the form already, knowing that the action of the tensor will contract with $A^\mu,B^\nu$ and that parallel transport introduces a linear transformation. We therefore expect the change $\delta V^\rho$ experienced by the vector when parallel transported around the loop to look like$$\Large \delta V^\rho= R^{\rho}{}_{\sigma\mu\nu}V^\sigma A^\mu B^\nu$$, where $R^{\rho}{}_{\sigma\mu\nu}$ is a $[1,3]$ tensor known as the Riemann tensor. Note it is antisymmetric in the last two indices:$$\Large  R^{\rho}{}_{\sigma\mu\nu}=-R^{\rho}{}_{\sigma\nu\mu}$$
Our knowledge of parallel transport allows us to perform the manipulations necessary to write the curvature tensor in terms of connection coefficients, however there is a much nicer way to do this:
> Consider the commutator of two covariant derivatives, $[\nabla_\mu,\nabla_\nu]$. Since the covariant derivative measures how much the tensor changes relative to parallel transport, the commutator measures the difference between parallel transporting the tensor first one way, and then the other (see [[Geodesics 2026-11-10 15.22.10.excalidraw|my lovely illustration]]).
> The computation is as follows:$$\begin{aligned}\Large[\nabla_\mu,\nabla_\nu]V^\rho&= \nabla_\mu\nabla_\nu V^\rho-\nabla_\nu\nabla_\mu V^\rho\\
&=\partial_\mu(\nabla_\nu V^\rho)-\Gamma^\lambda_{\mu\nu}\nabla_\lambda V^\rho+\Gamma^\rho_{\mu\sigma}\nabla_\nu V^\sigma-(\mu\leftrightarrow\nu)\\
&=\partial_\mu\partial_\nu V^\rho+(\partial_\mu\Gamma^\sigma_{\nu\sigma})V^\sigma+\Gamma^\rho_{\nu\sigma}\partial_\mu V^\sigma-\Gamma^\lambda_{\mu\nu}\partial_\lambda V^\rho\\
&-\Gamma^\lambda_{\mu\nu}\Gamma^\rho_{\lambda\sigma}V^\sigma+\Gamma^\rho_{\mu\sigma}\partial_\nu V^\sigma+\Gamma^\rho_{\mu\sigma}\Gamma^\sigma_{\nu\lambda}V^\lambda -(\mu\leftrightarrow\nu)\\
&=(\partial_\mu\Gamma^\rho_{\nu\sigma}-\partial_\nu\Gamma^\rho_{\mu\sigma}+\Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma}-\Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma})V^\sigma-2\Gamma^\lambda_{[\mu\nu]}\nabla_\lambda V^\rho
\end{aligned}$$Note in the last step we relabeled dummy indices and eliminated some terms that cancel when antisymmetrised. 
> Recognising that the antisymmetrised connection coefficients in the last term are simply half the [[Covariant derivative|torsion tensor]] and that the LHS is manifestly tensorial, the bracketed terms must also be a tensor:$$\Large\begin{aligned}
[\nabla_\mu,\nabla_\nu]V^\rho&= R^{\rho}{}_{\sigma\mu\nu}V^\sigma- T^{\lambda}{}_{\mu\nu}\nabla_\lambda V^\rho\\
&=\text{tensor }+\text{ scalar}\\
\implies  R^{\rho}{}_{\sigma\mu\nu}&=\partial_\mu\Gamma^\rho_{\nu\sigma}-\partial_\nu\Gamma^\rho_{\mu\sigma}+\Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma}-\Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}
\end{aligned}$$
> Note it remains to show this is the same tensor we derived previously.
> It is notable that the action of a (seemingly) differential operator $[\nabla_\mu,\nabla_\nu]$ gave us a simple multiplicative transformation. The Riemann tensor measures the part of the commutator that is proportional to the vector field, and the torsion tensor measures the part proportional to the covariant derivative of the vector field.
> This is true for any connection, no matter if it is metric compatible or torsion free.

As an example, let us calculate the Riemann tensor on the two-sphere:
> Recall our calculation for the Christoffel connection on $S^2$:$$\Large\Gamma^\theta_{\phi\phi}=-\sin\theta\cos\theta,\,\,\Gamma^\phi_{\theta\phi}=\cot\theta,\,\,\text{other connections }0$$
> Therefore the only non-zero components are $R^{\lambda}{}_{\rho\theta\phi}$:$$\Large\begin{aligned}
 R^{\theta}{}_{\theta\theta\phi}&=\partial_\theta\Gamma^\theta_{\phi\theta}-\partial_\phi\Gamma^\theta_{\theta\theta}+\Gamma^\theta_{\theta\sigma}\Gamma^\sigma_{\phi\theta}-\Gamma^\theta_{\phi\sigma}\Gamma^\sigma_{\theta\theta}=0\\
 R^{\theta}{}_{\phi\theta\phi}&=\partial_\theta\Gamma^\theta_{\phi\phi}-\partial_\phi\Gamma^\theta_{\theta\phi}+\Gamma^\theta_{\theta\sigma}\Gamma^\sigma_{\phi\phi}-\Gamma^\theta_{\phi\sigma}\Gamma^\sigma_{\theta\phi}\\_{\sigma\leftrightarrow\phi \text{ in last term}}
&=\partial_\theta(-\sin\theta\cos\theta)-\Gamma^\theta_{\phi\phi}\Gamma^\phi_{\theta\phi}\\
&=-(\cos^2\theta-\sin^2\theta)-(\sin\theta\cos\theta)\cot\theta=\sin^2\theta\\
 R^{\phi}{}_{\theta\theta\phi}&=\partial_\theta\Gamma^\phi_{\phi\theta}-\partial_\phi\Gamma^\phi_{\theta\theta}+\Gamma^\phi_{\theta\sigma}\Gamma^\sigma_{\phi\theta}-\Gamma^\phi_{\phi\sigma}\Gamma^\sigma_{\theta\theta}\\
&=\partial_\theta(\cot\theta)+\Gamma^\phi_{\theta\phi}\Gamma^\phi_{\phi\theta}\\
&=-\frac{1}{\sin^2\theta}+\cot^2\theta=\frac{\cos^2\theta-1}{\sin^2\theta}=-1\\
 R^{\phi}{}_{\phi\theta\phi}&=\partial_\theta\Gamma^\phi_{\phi\phi}-\partial_\phi\Gamma^\phi_{\theta\phi}+\Gamma^\phi_{\theta\sigma}\Gamma^\sigma_{\phi\phi}-\Gamma^\phi_{\phi\sigma}\Gamma^\sigma_{\theta\phi}\\
&=-\partial_\phi(\cot\theta)+\Gamma^\phi_{\theta\theta}\Gamma^\theta_{\phi\phi}+\Gamma^\phi_{\theta\phi}\Gamma^{\phi}_{\phi\phi}=0
\end{aligned}$$

Both the torsion and Riemann tensors have elegant expressions in terms of the vector field commutator. Thinking of the torsion as a map from two vector fields to a third, we have$$\Large\begin{aligned}
T(X,Y)&=\nabla_XY-\nabla_YX-[X,Y]\\
R(X,Y)Z&=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z
\end{aligned}$$, using similar logic for the Riemann tensor. Note $\nabla_X$ refers to the covariant derivative along the vector field $X$. Note that we can find the commutator of covariant derivatives on other tensors using the Riemann tensor. To see this, consider this commutator acting on a scalar $V^\lambda\omega_\lambda$:$$\large\begin{aligned}
[\nabla_\mu,\nabla_\nu](V^\lambda\omega_\lambda)&=\nabla_\mu\nabla_\nu(V^\lambda\omega_\lambda)-\nabla_\nu\nabla_\mu(V^\lambda\omega_\lambda)=0\\
&=\nabla_\mu((\nabla_\nu V^\lambda)\omega_\lambda+V^\lambda(\nabla_\nu\omega_\lambda))-(\mu\leftrightarrow\nu)\\
&=(\nabla_\mu\nabla_\nu V^\lambda)\omega_\lambda+\nabla_\nu V^\lambda\nabla_\mu\omega_\lambda+\nabla_\mu V^\lambda\nabla_\nu\omega_\lambda+V^\lambda\nabla_\mu\nabla_\nu\omega_\lambda-(\mu\leftrightarrow\nu)\\
_{\text{cancelling terms 2,3}}&=([\nabla_\mu,\nabla_\nu]V^\lambda)\omega_\lambda+V^\lambda([\nabla_\mu,\nabla_\nu]\omega_\lambda)\\
&= R^{\lambda}{}_{\rho\mu\nu}V^\rho\omega_\lambda+V^\lambda[\nabla_\mu,\nabla_\nu]\omega_\lambda\\

\end{aligned}$$

Having defined the curvature tensor, we can finally formalise our notion of locally flat spaces:
> If a coordinate system exists in which the components of the metric are constant, the Riemann tensor will vanish:
> > If we are in some coordinate system where $\partial_\sigma g_{\mu\nu}=0$ everywhere, then $\Gamma^\rho_{\mu\nu}=0$ and $\partial_\sigma\Gamma^\rho_{\mu\nu}=0$.
> > This forces $R^{\rho}{}_{\sigma\mu\nu}=0$, as it is constructed from these connection coefficients. 
> > The Riemann tensor equation is tensorial, it is true in all coordinate systems. Therefore it is a necessary condition that it is possible to find coordinates in which components of $g_{\mu\nu}$ are constant everywhere.
> If the Riemann tensor vanishes, we can always construct a coordinate system in which the metric components are constant:
> > This is harder to prove, so let us start by proving this for the one-form $\omega=\omega_\mu dx^\mu$ defined at a point $p$.
> > For any path $x^\mu(\lambda)$ that runs through $p$, we can construct a unique one-form field along the path by demanding $\omega_\mu$ be parallel transported:$$\Large \frac{dx^\mu}{d\lambda}\nabla_\mu\omega_\nu=0$$If we did this for distinct paths starting at $p$ and passing through some other point $q$, the value of $\omega_\mu$ at $q$ would depend on the path. However, if the Riemann tensor is everywhere vanishing, the parallel-transport will be path independent and we can define our unique one-form field on the whole manifold. 
> > Therefore this equation must be true for arbitrary $\frac{dx^\mu}{d\lambda}$, which is only true if $\omega_\mu$ is covariantly constant:$$\huge\nabla_\mu\omega_\nu=0$$This only holds for vanishing curvature, this has no solutions for an arbitrary manifold.
> > We can take the antisymmetric part of the above and notice that it is just the [[SR, Manifolds, and Field theory summary#Exterior derivatives|exterior derivative]]:$$\Large\nabla_{[\mu}\omega_{\nu]}=\partial_{[\mu}\omega_{\nu]}=0\implies d\omega=0$$That is, $\omega$ is closed. Since we have restricted our topology, it is also exact and will admit a scalar function $\alpha$ such that:$$\Large\omega_\mu=\partial_\mu\alpha$$
> > Since the one-form $\omega$ was generic, we can repeat this procedure with a set of one-forms $\hat\theta^{(a)},a\in\{1,\dots,n\}$ on an $n$-dimensional manifold. We can choose such one-forms to comprise a normalised dual space basis $T_p^*$ such that the metric components wrt this basis are those of canonical form, that is:$$\Large ds^2(p)=\eta_{ab}\hat\theta^{(a)}\otimes\hat\theta^{(b)}$$Where we are using $\eta_{ab}$ in a general sense as a diagonal matrix with either $\pm1$ as the entries.
> > Let us parallel transport the entire set of basis forms over the whole manifold. Vanishing Riemann tensor ensures this process is path independent. 
> > Since the metric is automatically parallel-transported wrt a metric-compatible connection, the metric components are unchanged, i.e. the above holds for all $p$ in the manifold.
> > We have specified a set of one-form fields which everywhere define a basis in which metric components are constant, as required.

In the last step of this proof, we never used any notion of curvature to find our basis. What if we demand this is a coordinate basis (only possible on vanishing curvature)? We know all $\hat\theta^{(a)}$ are exact forms, so there must exist a set of functions $y^a$ such that the one-form fields are their gradients ($\hat\theta^{(a)}=dy^a$). These $n$ functions are exactly the coordinates we are looking form. Over the whole manifold, the metric takes form:$$\huge ds^2=\eta_{ab}dy^ady^b$$
## Geodesic deviation:
To gain a physical intuition for the significance of the Riemann tensor, we investigate geodesic deviation - the failure of initially parallel geodesics to remain parallel. Consider a one-parameter family of geodesics $\gamma_u(t)$ so that $x^\mu(t,u)$. Therefore, $V^\mu=\partial_t x^\mu$ is tangent to the geodesics and $U^\mu=\partial_u x^\mu$ is the geodesic deviation vector (pointing from one geodesic to another).

We now propose the lemma:$$\Large V^\mu\nabla_\mu U^\nu-U^\mu\nabla_\mu V^\nu=0$$Proof:
> We can directly compute:$$\Large\begin{aligned}
V^\mu\nabla_\mu U^\nu-U^\mu\nabla_\mu V^\nu&=V\partial_\mu U^\nu-U^\mu\partial_\mu V^\nu\\
&=\frac{\partial^2x^\nu}{\partial t\partial u}-\frac{\partial^2 x^\nu}{\partial u\partial t}=0
\end{aligned}$$
> Relative acceleration between geodesics is therefore:$$\Large\begin{aligned}
A^\nu&=V^\mu\nabla_\mu(V^\lambda\nabla_\lambda U^\nu)\\
_\text{using lemma}&=V^\mu\nabla_\mu(U^\lambda\nabla_\lambda U^\nu)\\
_\text{using geodesic eqn}&=V^\mu\nabla_\mu(U^\lambda\nabla_\lambda V^\nu)-U^\mu\nabla_\mu(V^\lambda\nabla_\lambda V^\nu)\\
&=(V^\mu\nabla_\mu U^\lambda-U^\mu\nabla_\mu V^\lambda)(\nabla_\lambda V^\nu)+V^\mu U^\lambda[\nabla_\mu,\nabla_\lambda]V^\nu\\
&=V^\mu U^\lambda  R^{\nu}{}_{\rho\mu\lambda}V^\rho
\end{aligned}$$

The equation$$\Large A^\nu= R^{\nu}{}_{\rho\mu\lambda}V^\rho V^\mu U^\lambda$$is known as the geodesic deviation equation and describes the failure of parallel lines to remain parallel. $A^\mu=0$ for all geodesics if and only if the Riemann tensor vanishes, the components of this tensor measure the strength of "tidal" forces induced by the manifold on a family of geodesic observers.

## Riemann normal coordinates:
Riemann normal coordinates are the closest coordinate system such that the metric looks flat over any open region on the manifold. A manifold equipped with a metric should locally behave like Minkowski space. That is, we should expect the metric is exactly the Minkowski metric at some point $p$ i.e. there should exist some coordinate system in which $g_{\mu\nu}(p)=\eta_{\mu\nu}$. One can show this using a similar counting argument presented in the next section.

Coordinates such that $g_{\mu\nu}=\eta_{\mu\nu}$ and $\partial_\lambda g_{\mu\nu}=0$ at a point are called Riemann normal coordinates, very useful for studying general properties of metrics and curvature. Let us explicitly calculate the Riemann tensor in such coordinate systems:
> $\partial_\lambda g_{\mu\nu}=0$ at $p$ implies $\Gamma^\mu_{\nu\rho}$ at $p$, so the general expression for the Riemann tensor reduces to:$$\Large  R^{\lambda}{}_{\rho\mu\nu}=\partial_\mu\Gamma^\lambda_{\nu\rho}-\partial_\nu\Gamma^\lambda_{\mu\rho}$$
> Now using our expression for the Christoffel symbols in terms of the metric, $\Gamma^\lambda_{\nu\rho}=\frac{1}{2}g^{\lambda\sigma}(\partial_\mu g_{\rho\sigma}+\partial_\rho g_{\nu\sigma}-\partial_\sigma g_{\nu\rho})$, we have:$$\Large\begin{aligned}
 R^{\lambda}{}_{\rho\mu\nu}&=\frac{1}{2}g^{\lambda\sigma}(\partial_\mu\partial_\nu g_{\rho\sigma}+\partial_\mu\partial_\rho g_{\nu\sigma}-\partial_\mu\partial_\sigma g_{\nu\rho}\\
&-\partial_\nu\partial_\mu g_{\rho\sigma}-\partial_\nu\partial_\mu g_{\mu\sigma}+\partial_\nu\partial_\sigma g_{\mu\rho})\\
&=\frac{1}{2}g^{\lambda\sigma}(\partial_\mu\partial_\rho g_{\nu\beta}+\partial_\nu\partial_\beta g_{\mu\rho}-\partial_\mu\partial_\beta g_{\nu\rho}-\partial_\nu\partial_\rho g_{\mu\beta})
\end{aligned}$$

## Properties of the Riemann tensor:

## Algebraic symmetries:
The Riemann tensor naively has $n^4$ independent components in $n$-dimensional space, however the antisymmetry restriction on the last two indices forces $n(n-1)/2$ values on said indices. Therefore we have $n^3(n-1)/2$ independent components. Considering the Christoffel connection, other symmetries reduce the independent components further:
> To derive these additional symmetries, examine the Riemann tensor with all lower indices:$$\Large R_{\rho\sigma\mu\nu}=g_{\rho\lambda} R^{\lambda}{}_{\sigma\mu\nu}$$
> Furthermore, consider the components of this tensor in locally inertial coordinates $x^{\hat\mu}$ established at a point $p$. In this setup, the Christoffel symbols vanish, similar to the calculation above (although their derivatives will not):$$\Large\begin{aligned}
R_{\hat\rho\hat\sigma\hat\mu\hat\nu}(p)&=g_{\hat\rho\hat\lambda}(\partial_{\hat\mu}\Gamma^{\hat\lambda}_{\hat\nu\hat\sigma}-\partial_{\hat\nu}\Gamma^{\hat\lambda}_{\hat\mu\hat\sigma})\\
&=\frac{1}{2}g_{\hat\rho\hat\lambda}g^{\hat\lambda\hat\tau}(\partial_{\hat\mu}\partial_{\hat\nu}g_{\hat\sigma\hat\tau}+\partial_{\hat\mu}\partial_{\hat\sigma}g_{\hat\tau\hat\nu}-\partial_{\hat\mu}\partial_{\hat\tau}g_{\hat\nu\hat\sigma}\\
&-\partial_{\hat\nu}\partial_{\hat\mu}g_{\hat\sigma\hat\tau}-\partial_{\hat\nu}\partial_{\hat\sigma}g_{\hat\tau\hat\mu}+\partial_{\hat\nu}\partial_{\hat\tau}g_{\hat\mu\hat\sigma})\\
&=\frac{1}{2}(\partial_{\hat\mu}\partial_{\hat\sigma}g_{\hat\rho\hat\nu}-\partial_{\hat\mu}\partial_{\hat\rho}g_{\hat\nu\hat\sigma}-\partial_{\hat\nu}\partial_{\hat\sigma}g_{\hat\rho\hat\mu}+\partial_{\hat\nu}\partial_{\hat\rho}g_{\hat\mu\hat\sigma})
\end{aligned}$$
> This expression highlights three symmetries about our modified Riemann tensor: it is antisymmetric in the first two indices, the last two indices, and is invariant under interchange $(\rho\sigma\leftrightarrow\mu\nu)$:$$\Large\begin{aligned}
R_{\rho\sigma\mu\nu}&=-R_{\sigma\rho\mu\nu}\\
&=-R_{\rho\sigma\nu\mu}\\
&=R_{\mu\nu\rho\sigma}\\
\implies R_{\rho\sigma\mu\nu}+R_{\rho\mu\nu\sigma}+R_{\rho\nu\sigma\mu}&=0\\
\implies R_{\rho[\sigma\mu\nu]}&=0
\end{aligned}$$
> We derived this in a designated coordinate system, however all of our equations are tensorial and therefore hold in any coordinate system.

Given these symmetries, how many independent components are we left with? We can think of our modified tensor as a symmetric matrix $R_{[\rho\sigma][\mu\nu]}$, where we think of $\rho\sigma$ and $\mu\nu$ as individual indices. A symmetric $m\times m$ matrix has $m(m+1)/2$ independent components, while an antisymmetric $n\times n$ matrix has $n(n-1)/2$ independent components and so we have$$\Large \frac{1}{2}\left(\frac{1}{2}n(n-1)\right)\left(\frac{1}{2}n(n-1)+1\right)=\frac{1}{8}(n^4-2n^3+3n^2-2n)$$independent components. It remains to impose the last symmetry we derived above, however one can show that imposing this is equivalent to imposing total antisymmetry:$$\huge R_{[\rho\sigma\mu\nu]}=0$$A totally antisymmetric $4$-index tensor has $n(n-1)(n-2)(n-3)/4!$ independent components, so imposing the above reduces our number of independent components by this amount. Computing the remaining independent components and doing some lovely factorising, we are left with$$\huge\frac{1}{12}n^2(n^2-1)$$independent components.


## Differential symmetries (Bianchi identity):
In addition to the algebraic symmetries we found above, the Riemann tensor also satisfies a differential symmetry known as the Bianchi identity. Consider the covariant derivative of the Riemann tensor in locally inertial coordinates (dropping the hat bc its a pain to type), using our expression above:$$\Large\begin{aligned}
\nabla_\lambda R_{\rho\sigma\mu\nu}&=\partial_\lambda R_{\rho\sigma\mu\nu}\\
&=\frac{1}{2}\partial_\lambda(\partial_\mu\partial_\sigma g_{\rho\nu}-\partial_\mu\partial_\rho g_{\nu\sigma}-\partial_\nu\partial_\sigma g_{\rho\mu}+\partial_\nu\partial_\rho g_{\mu\sigma})
\end{aligned}$$Note we are taking the derivative of an expression derived at a point, however we neglect all terms proportional to $\partial_\sigma g_{\mu\nu}$ anyway so it's fine (trust bro). Now consider the sum of cyclic permutations over the first three indices:$$\Large\begin{aligned}

\end{aligned}$$