
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
\implies V^\lambda[\nabla_\mu,\nabla_\nu]\omega_\lambda&=- R^{\lambda}{}_{\rho\mu\nu}V^\rho\omega_\lambda=_{\rho\leftrightarrow\lambda'}- R^{\lambda}{}_{\lambda'\mu\nu}V^{\lambda'}\omega_\lambda,\,\,\forall V^\lambda\\
\implies [\nabla_\mu,\nabla_\nu]\omega_\lambda&=- R^{\rho}{}_{\lambda\mu\nu}\omega_\rho
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

These differ from [[The metric tensor and Causality#Locally inertial coordinates|locally inertial coordinates]] in the sense that they fix higher-order coordinate freedom by requiring geodesics through $p$ to (initially) be straight lines $x^\mu(\lambda)=V^\mu\lambda$. That is, every geodesic through $p$ has zero coordinate acceleration along it's parametrisation, whereas locally inertial coordinates only guarantee this at the point $p$ itself.

## Properties of the Riemann tensor:

### Algebraic symmetries:
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


### Differential symmetries (Bianchi identity):
In addition to the algebraic symmetries we found above, the Riemann tensor also satisfies a differential symmetry known as the Bianchi identity. Consider the covariant derivative of the Riemann tensor in locally inertial coordinates (dropping the hat bc its a pain to type), using our expression above:$$\Large\begin{aligned}
\nabla_\lambda R_{\rho\sigma\mu\nu}&=\partial_\lambda R_{\rho\sigma\mu\nu}\\
&=\frac{1}{2}\partial_\lambda(\partial_\mu\partial_\sigma g_{\rho\nu}-\partial_\mu\partial_\rho g_{\nu\sigma}-\partial_\nu\partial_\sigma g_{\rho\mu}+\partial_\nu\partial_\rho g_{\mu\sigma})
\end{aligned}$$Note we are taking the derivative of an expression derived at a point, however we neglect all terms proportional to $\partial_\sigma g_{\mu\nu}$ anyway so it's fine (trust bro). Now consider the sum of cyclic permutations over the first three indices:$$\Large\begin{aligned}
\underline{\nabla}_\lambda R_{\rho\sigma\mu\nu}+\underline{\nabla}_\rho R_{\sigma\lambda\mu\nu}+\underline{\nabla}_\sigma R_{\lambda\rho\mu\nu}&=\frac{1}{2}(\partial_\lambda\partial_\mu\partial_\sigma g_{\rho\nu}-\dots\\
&+\partial_\sigma\partial_\nu\partial_\lambda g_{\mu\rho})\\
&=0
\end{aligned}$$Antisymmetry in the first two indices then lets us write this identity as:$$\Huge \underline{\nabla}_{[\lambda}R_{\rho\sigma]\mu\nu}=0$$This is known as the Bianchi identity, and for a general connection will involve more terms to do with the Torsion tensor. One can think of this as a generalisation of the [[Lie Groups and Algebras#Lie algebras|Jacobi identity]] for curved spacetimes.

# Ricci, Weyl, and Eienstien tensors:

It is useful to decompose a tensor into a sum of different parts that are each easier to handle and have physical interpretations. The way to do this without breaking coordinate-invariance is to use contractions and noting symmetric/antisymmetric parts:
> For example, consider a general $[0,2]$ tensor $X_{\mu\nu}$ which we can decompose into symmetric and antisymmetric parts:$$\Large X_{\mu\nu}=X_{(\mu\nu)}+X_{[\mu\nu]}$$
> The symmetric part can further be decomposed into its trace $X=g^{\mu\nu}X_{(\mu\nu)}$ and its trace-free part $\hat X_{\mu\nu}=X_{(\mu\nu)}-\frac{1}{n}Xg_{\mu\nu}$ so that:$$\Large\begin{aligned}
X_{\mu\nu}&=\frac{1}{n}Xg_{\mu\nu}+\hat X_{\mu\nu}+X_{[\mu\nu]}\\
&=\text{trace }+\text{ trace-free }+\text{antisymmetric}
\end{aligned}$$
> Under coordinate transformations, these objects rotate onto themselves and not each other. They define invariant subspaces of the $[0,2]$ tensors. For higher-order/mixed tensors, this decomposition may not be as nice.


## Ricci tensor:
Doing this decomposition on the Riemann tensor, our first step is to take a contraction over the third index to define the Ricci tensor:$$\huge R_{\mu\nu}= R^{\lambda}{}_{\mu\lambda\nu}$$Note that a curvature tensor formed from a non-Christoffel connection would have a number of independent contractions to take, all contractions on the Riemann tensor either vanish or relate to the above. As a consequence of the Riemann tensor symmetries, the Ricci tensor will be symmetric automatically. The trace of the Ricci tensor is known as the Ricci scalar:$$\Large R=R^\mu_\mu=g^{\mu\nu}R_{\mu\nu}$$
## Weyl tensor:
The Ricci tensor and scalar contain all information about the traces of the Riemann tensor, leaving the trace-free parts. We capture these with the Weyl tensor, essentially the Riemann tensor with all contractions removed:$$\Large\begin{aligned}
C_{\rho\sigma\mu\nu}&=R_{\rho\sigma\mu\nu}-\frac{2}{n-2}(g_{\rho[\mu}R_{\nu]\sigma}-g_{\sigma[\mu}R_{\nu]\rho})\\
&+\frac{2}{(n-1)(n-2)}g_{\rho[\mu}g_{\nu]\sigma}R
\end{aligned}$$The above expression is designed so that all contractions of $C_{\rho\sigma\mu\nu}$ vanish, while retaining the algebraic symmetries of the Riemann tensor. Note in $\Re^3$, this vanishes identically.

The Weyl tensor is invariant under conformal transformations, that is if one computes $C^{\rho}{}_{\sigma\mu\nu}$ for some metric $g_{\mu\nu}$ and then for $\omega^2(x)g_{\mu\nu}$, one would get the same answer. For this reason, it is often known as the conformal tensor.

## Einstein tensor:
A useful form of the Bianchi identity comes from twice contracting the sum of cyclic covariant derivatives:$$\Large\begin{aligned}
0&=g^{\nu\sigma}g^{\mu\lambda}(\underline{\nabla}_\lambda R_{\rho\sigma\mu\nu}+\underline{\nabla}_\rho R_{\sigma\lambda\mu\nu}+\underline{\nabla}_\sigma R_{\lambda\rho\mu\nu})\\
&=\underline{\nabla}^\mu R_{\rho\mu}-\underline{\nabla}_\rho R+\underline{\nabla}^\nu R_{\rho\nu}\\
\implies\underline{\nabla}^\mu R_{\rho\mu}&=\frac{1}{2}\underline{\nabla}_\rho R
\end{aligned}$$Then, defining the Einstein tensor$$\huge G_{\mu\nu}=R_{\mu\nu}-\frac{1}{2}Rg_{\mu\nu}$$, we can write the double-contracted Bianchi identity as:$$\huge \underline{\nabla}^\mu G_{\mu\nu}=0$$One can think of the Einstein tensor as a trace-reversed version of the Ricci tensor.

# Symmetries and killing vectors:

A manifold $M$ has a symmetry if the geometry is invariant under certain transformations mapping $M$ onto itself, that is if the metric is the same from one point to another. Metric symmetries are called isometries, we know many for Minkowski space:
> Translations $x^\mu\to x^\mu+a^\mu$
> Lorentz transformations $x^\mu\to\Lambda^\mu_\nu x^\nu$

Metric invariance is made apparent by noting that metric coefficients are independent of individual coordinate functions $x^\mu$. Whenever $\partial_\sigma g_{\mu\nu}=0$ for some fixed $\sigma$, there will be a symmetry under translations along $x^\sigma:$$$\Large \partial_\sigma g_{\mu\nu}=0\implies x^\sigma\to x^\sigma+a^\sigma \text{ is a symmetry}$$Isometries of this form have immediate consequences for the motion of test particles described by the geodesic equation. Recall we can write the geodesic equation in terms of four-momentum $p^\mu=mU^\mu$, by metric compatibility we can lower an index:$$\Large\begin{aligned}
p^\lambda\underline{\nabla}_\lambda p^\mu&=0\\
\implies p^\lambda\underline{\nabla}_\lambda p_\mu&=0\\
\implies p^\lambda\partial_\lambda p_\mu-\Gamma^\sigma_{\lambda\mu}p^\lambda p_\sigma&=0
\end{aligned}$$The first term shows how momentum components change along a path$$\Large p^\lambda\partial_\lambda p_\mu=m \frac{dx^\lambda}{d\tau}\partial_\lambda p_\mu=m \frac{dp_\mu}{d\tau}$$, while the second term is$$\large\begin{aligned}
\Gamma^\sigma_{\lambda\mu}p^\lambda p_\sigma&=\frac{1}{2}g^{\sigma\nu}(\partial_\lambda g_{\mu\nu}+\partial_\mu g_{\nu\lambda}-\partial_\nu g_{\lambda\mu})p^\lambda p_\sigma\\
&=\frac{1}{2}(\partial_\lambda g_{\mu\nu}+\partial_\mu g_{\nu\lambda}-\partial_\nu g_{\lambda\mu})p^\lambda p^\nu\\
&=\frac{1}{2}(\partial_\mu g_{\nu\lambda})p^\lambda p^\nu
\end{aligned}$$, where we used the symmetry of $p^\lambda p^\nu$ to go from second to third line. Without making any assumptions about the symmetry, we have arrive at this form of the geodesic equation:$$\Large m \frac{dp_\mu}{d\tau}=\frac{1}{2}(\partial_\mu g_{\nu\lambda})p^\lambda p^\nu$$Therefore, we find this isometry implies the momentum component $p_\sigma$ is conserved under the motion:$$\Large \partial_\sigma g_{\mu\nu}=0\implies \frac{dp_\sigma}{d\tau}=0$$This will hold along any geodesic. Conserved quantities derived from isometries are very useful in studying the motion of test particles.

## Killing vectors:
We can generalise this procedure in a manifestly covariant form. If $x^\sigma$ is a coordinate of which $g_{\mu\nu}$ is independent of, let us consider the vector:$$\Large K=\partial_\sigma,\,\,K^\mu=(\partial_\sigma)^\mu=\delta^\mu_\sigma$$We say that the vector $K^\mu$ generates the isometry, meaning the geometry-invariant transformation is expressed infinitesimally as motion in the direction of $K^\mu$. In this notation, we can write the quantity $p_\sigma$ as:$$\Large p_\sigma=K^\nu p_\nu=K_\nu p^\nu$$The constancy of this quantity along the path is equivalent to vanishing directional derivative along the geodesic:$$\Large\begin{aligned}
\frac{dp_\sigma}{d\tau}=0&\leftrightarrow p^\mu\underline{\nabla}_\mu(K_\nu p^\nu)=0\\
p^\mu\underline{\nabla}_\mu (K_\nu p^\nu)&=p^\mu K_\nu\underline{\nabla}_\mu p^\nu +p^\mu p^\nu\underline{\nabla}_\mu K_\nu\\
&=p^\mu p^\nu\underline{\nabla}_\mu K_\nu\\
&=p^\mu p^\nu\underline{\nabla}_{(\mu}K_{\nu)}
\end{aligned}$$Where we invoked the geodesic equation. We also used the automatic symmetry for $p^\mu p^\nu$, so only the symmetric part of $\underline{\nabla}_\mu K^\nu$ can contribute. Therefore we conclude that any vector $K_\mu$ satisfying $\underline{\nabla}_{(\mu}K_{\nu)}=0$ implies $K_\nu p^\nu$ is conserved along a geodesic trajectory:$$\Large \underline{\nabla}_{(\mu}K_{\nu)}=0\implies p^\mu\underline{\nabla}_\mu(K_\nu p^\nu)=0$$This is known as Killing's equation, and vector fields that satisfy it are known as Killing vectors. Every Killing vector implies the existence of conserved quantities associated with geodesic motion. We can generalise the logic we used for additional indices; a Killing tensor is a symmetric $l$-index tensor $K_{\nu_1\dots\nu_l}$ that satisfies the generalisation of Killing's equation. We will also get conserved quantities by contracting with $l$ copies of momentum:$$\Large \underline{\nabla}_{(\mu}K_{\nu_1\dots\nu_l)}=0\implies p^\mu\underline{\nabla}_\mu(K_{\nu_1\dots\nu_l}p^{\nu_1}\dots p^{\nu_l})=0$$A simple example of a Killing tensor is the metric itself, and symmetrised tensor products of Killing vectors.

Derivatives of Killing vectors can be related to the Riemann tensor by$$\Large\underline{\nabla}_\mu\underline{\nabla}_\sigma K^\rho= R^{\rho}{}_{\sigma\mu\nu}K^\nu$$, contracting this yields:$$\Large \underline{\nabla}_\mu\underline{\nabla}_\sigma K^\mu=R_{\sigma\nu}K^\nu$$Together with the Bianchi identity and Killing's equation, we have that the directional derivatives of the Ricci scalar along a Killing vector field will vanish:$$\huge K^\lambda\underline{\nabla}_\lambda R=0$$
## Energy:
The existence of a timelike Killing vector allows us to define a conserved energy for the entire spacetime. Given a Killing vector $K_\nu$ and conserved energy-momentum tensor $T_{\mu\nu}$, we can construct a current $J^\mu_T=K_\nu T^{\mu\nu}$ that is automatically conserved:$$\Large\begin{aligned}
\underline{\nabla}_\mu J^\mu_T&=(\underline{\nabla}_\mu K_\nu)T^{\mu\nu}+K_\nu(\underline{\nabla}_\mu T^{\mu\nu})\\
&=0
\end{aligned}$$Where the first term vanishes by Killing's equation. If $K_\nu$ is timelike, we can integrate over a spacelike hypersurface $\Sigma$ to define total energy$$\Large E_T=\int_\Sigma J^\mu_T n_\mu\sqrt{\gamma}d^3x$$, where $\gamma$ is the induced metric on $\Sigma$, and $n_\mu$ is the normal vector to $\Sigma$. This integral will be the same over any spacelike hypersurface, and is therefore conserved.