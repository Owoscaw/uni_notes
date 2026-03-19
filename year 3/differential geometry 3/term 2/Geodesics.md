
Geodesics are the generalisation of straight lines in Euclidean space. The fundamental properties of straight lines are:
> Straight lines represent the shortest path between two points
> Travelling along straight lines at a constant speed results in no force (no acceleration)

Instead of using a geometric description of straight lines, we use the physical description to generalise straight lines to geodesics on surfaces.
# Geodesics as ODE solutions:

Let $S\subset\Re^3$ be a [[Surfaces in R3#Regular points/values|regular surface]]. A regular curve $\underline{\alpha}:I\rightarrow S$ is called a geodesic if $\underline{\alpha}''$ is normal to $S$. That is:$$\Huge \underline{\alpha}''\perp T_{\underline{\alpha}(t)}S\,\,\forall t\in I$$
An immediate consequence of this definition is that for a geodesic $\underline{\alpha}$ of $S$, we must have $||\underline{\alpha}'||$ is constant. That is, $\underline{\alpha}$ is proportional to a unit speed curve. Proof:
> Let $f(t)=||\underline{\alpha}'(t)||^2=\underline{\alpha}'(t)\cdot\underline{\alpha}'(t)$, the proof is then immediate:$$\Huge\begin{align*}
f'(t)&=\underline{\alpha}''(t)\cdot\underline{\alpha}'(t)+\underline{\alpha}'(t)\cdot\underline{\alpha}''(t)\\
&=2\underline{\alpha}''(t)\cdot\underline{\alpha}'(t)=0
\end{align*}$$This is because $\underline{\alpha}''(t)$ is normal to $S$, while $\underline{\alpha}'(t)\in T_{\underline{\alpha}(t)}S$, so they are orthogonal to one another. Since $f'(t)=0$, $f(t)$ is constant, as required.

Let us consider great circles on a sphere:
> Let $$\Huge S^2(r)=\{\underline{x}\in\Re^3:||\underline{x}||^2=r^2\}$$be the round sphere of radius $r$. A great circle is the intersection of $S^2(r)$ with a plane through the origin. That is, they are circles on $S^2(r)$ with the same center and radius.
> Let $P$ be a plane through the origin, $X_1,X_2$ an orthonormal basis of $P$. Then $P\cap S^2(r)$ is defined by the curve$$\Huge\underline{\alpha}(t)=r\cos tX_1+r\sin tX_2$$, which has derivatives:$$\Huge\begin{align*}
\underline{\alpha}'(t)&=-r\sin tX_1+r\cos tX_2\\
\underline{\alpha}''(t)&=-r\cos tX_1-r\sin tX_2\\
&=-\underline{\alpha}(t)
\end{align*}$$
> This is orthogonal to the tangent plane of $S^2(r)$ and so must be a geodesic.

Let us consider geodesics on a cylinder:
> We define the cylinder as $$\Huge S=\{\underline{x}:x^2+y^2=1\}$$and consider the curve$$\Huge\underline{\alpha}(t)=(\cos(at+b),\sin(at+b),ct+d)$$with $a,b,c,d\in\Re$ and $a,c\neq0$. The trace of this curve is generally a subset that spirals up or down along the cylinder.
> We verify that $\underline{\alpha}$ is a geodesic, we have:$$\Huge\begin{align*}
\underline{\alpha}'(t)&=(-a\sin(at+b),a\cos(at+b),c)\\
\underline{\alpha}''(t)&=(-a^2\cos(at+b),-a^2\sin(at+b),0)
\end{align*}$$
> Noting that the inward unit normal of $S$ is given by $(-x,-y,0)$ and it is clear that $\underline{\alpha}''$ is parallel to the unit normal of $S$ at $\underline{\alpha}(t)$. It can be shown that all geodesics on $S$ have this form.
> In the case of $c=0$ we obtain a parallel of $S$ and in the case of $a=0$ we obtain a meridian of $S$.

We now provide an alternative definition of geodesics that implies geodesics are intrinsic objects of surfaces. Let $S$ be a surface and $\underline{\alpha}:I\rightarrow S$ be a regular curve. Then the following are equivalent:
> $\underline{\alpha}$ is a geodesic
> $\underline{\alpha}$ is constant speed and its geodesic curvature $\kappa_g$ vanishes identically

Since $||\underline{\alpha}'||$ and $\kappa_g$ are intrinsic quantities, geodesics are also intrinsic to the surface:
> Let us assume $\underline{\alpha}$ is a geodesic, then $\underline{\alpha}$ is constant speed trivially and:$$\Huge \begin{align*}
\kappa_g&=\frac{1}{||\underline{\alpha}'||^3}(\underline{\alpha}'\times\underline{\alpha}'')\cdot(\underline{N}\circ\underline{\alpha})\\
&=\frac{1}{||\underline{\alpha}||^3}(\underline{\alpha}\times0)\cdot(\underline{N}\circ\underline{\alpha})=0
\end{align*}$$This prove the first equivalence direction.
> We now assume $\underline{\alpha}$ is constant speed and has vanishing geodesic curvature. Since $\underline{\alpha}$ is regular, $\underline{\alpha}'$ and $\underline{\alpha}'\times\underline{N}(\underline{\alpha})$ span the [[Tangent planes#The tangent plane|tangent plane]] $T_\underline{\alpha}S$. Therefore it is only required to show $\underline{\alpha}''$ is perpendicular to both $\underline{\alpha}'$ and $\underline{\alpha}'\times(\underline{N}\circ\underline{\alpha})$ as this would force $\underline{\alpha}''$ to be normal to $S$.
> Constant $\underline{\alpha}'$ implies $\underline{\alpha}'\cdot\underline{\alpha}'$ is constant and so $\underline{\alpha}''\perp\underline{\alpha}'$. Since $\kappa_g=0$ we have:$$\Huge \kappa_g=\underline{\alpha}'\times\underline{\alpha}''\cdot(\underline{N}\circ\underline{\alpha})=0$$
> A basic property of the spat product is$$\Huge (\underline{x}\times\underline{y})\cdot\underline{z}=\begin{vmatrix}\underline{x} \\ \underline{y} \\ \underline{z}\end{vmatrix}$$and so we can write the vanishing curvature condition as$$\Huge\begin{vmatrix}\underline{\alpha}' \\ \underline{\alpha}'' \\ \underline{N}\circ\underline{\alpha}\end{vmatrix}=0$$where we consider $\underline{\alpha}',\underline{\alpha}'',\underline{N}\circ\underline{\alpha}$ as row vectors. Interchanging rows, we can write this as$$\Huge 0=\begin{vmatrix}\underline{\alpha}' \\ \underline{N}\circ\underline{\alpha} \\ \underline{\alpha}''\end{vmatrix}=(\underline{\alpha}'\times(\underline{N}\circ\underline{\alpha}))\cdot\underline{\alpha}''$$, showing that $\underline{\alpha}''$ is normal to $S$ and therefore a geodesic.

We now provide a description of geodesics using a nonlinear system of second order ODEs. Let $\underline{x}:U\rightarrow S$ be a local parametrisation of a surface $S$ and $E,F,G:U\rightarrow\Re$ be the corresponding coefficients of the first fundamental form. Then $\underline{\alpha}:I\rightarrow\underline{x}(U)\subset S$ with $\underline{\alpha}(t)=\underline{x}(u(t),v(t))$ is a geodesic if and only if the following system of ODEs is satisfied:$$\Huge\begin{align*}
u''E+v''F&=-\frac{1}{2}(u')^2E_u-u'v' E_v-(v')^2\left(F_v-\frac{1}{2}G_u\right)\\
v''G+u''F&=-\frac{1}{2}(v')^2G_v-u'v'G_u-(u')^2\left(F_u-\frac{1}{2}E_v\right)
\end{align*}$$To prove this:
> Notice that the tangent space $T_{\underline{\alpha}(t)}S$ is spanned by $\underline{x}_u(u(t),v(t))$ and $\underline{x}_v(u(t),v(t))$. The curve $\underline{\alpha}$ is a geodesic if and only if:$$\Huge \underline{\alpha}''\cdot\underline{x}_u=\underline{\alpha}''\cdot\underline{x}_v=0$$
> Starting with the form $\underline{\alpha}'=u'\underline{x}_u+v'\underline{x}_v$ we differentiate further:$$\Huge\underline{\alpha}''=u''\underline{x}_u+(u')^2\underline{x}_{uu}+u'v'\underline{x}_{uv}+v''\underline{x}_v+u'v'\underline{x}_{vu}+(v')^2\underline{x}_{vv}$$
> Taking the inner product with $\underline{x}_u$ then gives$$\large\underline{\alpha}''\cdot\underline{x}_u=u''E+v''F+(u')^2\frac{1}{2}E_u+2u'v'\frac{1}{2}E_v+(v')^2(F_v-\frac{1}{2}G_u)=0$$, which rearranges to the differential equation required. The same can be done with $\underline{x}_v$ to get the other equation.

# Fundamental properties of geodesics:

The fact that geodesics are intrinsic to a surface has the following immediate consequence, true for all intrinsic objects. Let $\underline{\alpha}:I\rightarrow S_1$ be a geodesic in a surface $S_1$ and let $f:S_1\rightarrow S_2$ be a local isometry between two surfaces. Then the image curve $\underline{\beta}=f\circ\underline{\alpha}:I\rightarrow S_2$ is also a geodesic in $S_2$.

We saw that we can write geodesics as solutions to a system of two second order differential equations. The theory of ODEs tells us that these equations should be locally uniquely determined by their initial conditions. Let $S$ be a surface, $\underline{p}\in S$ and $\underline{v}\in T_\underline{p}S$ be a non-zero tangent vector at $\underline{p}$. Then there exists $c>0$ and a unique geodesic $\underline{\alpha}:[-c,c]\rightarrow S$ such that $\underline{\alpha}(0)=\underline{p}$ and $\underline{\alpha}'(0)=\underline{v}$. That is, any non-zero tangent vector $\underline{v}$ gives rise to a unique geodesic passing through its footpoint in this particular direction with the same speed and length as $\underline{v}$.

Let us consider some examples:
> Consider the Euclidean plane $\Re^2$ as a surface and the identity as a global parametrisation leading to $E=G=1$ and $F=0$. The equations for geodesics $\underline{\alpha}(t)=(u(t),v(t))$ then simplify to$$\Huge u''=0,\,\,v''=0$$, that is $u(t)=u_0+at,v(t)=v_0+bt$ for any point $\underline{p}=(u_0,v_0)\in\Re^2$ and any tangent vector $\underline{v}=(a,b)\in T_\underline{p}\Re^2$. That is to say that all geodesics in $\Re^2$ are of the form $\alpha(t)=\underline{p}+t\underline{v}$.
> There is a local isometry between $\Re^2$ and the cylinder $S=\{\underline{x}\in\Re^3:x^2+y^2=1\}$ given by:$$\Huge f:\Re^2\rightarrow S,\,\,f(u,v)=(\cos u,\sin u,v)$$Since geodesics on $S$ are just the images of the above straight Euclidean lines, we can write them as:
> > Lines $t\to(\cos u_0,\sin u_0,t)$ with $u_0\in[0,2\pi)$ constant. 
> > Circles $t\to(\cos t,\sin t,v_0)$ with $v_0\in\Re$ constant.
> > Helices $t\to(\cos t,\sin t,v_0+ct)$ with $v_0\in\Re,c\neq0$ constants.

Let us investigate another property of straight lines, as curves of minimal length between any two points. First let us recall how a connected surfaces is promoted to a metric space with a distance function $d_S:S\times S\to[0,\infty)$. It can be shown that the following definition leads to a distance function$$\Huge d_S(\underline{p},\underline{q})=\inf\{L(\underline{\alpha})\}$$where the infimum is taken over all $\underline{\alpha}:[0,1]\to S$ continuous and piecewise smooth with $\underline{\alpha}(0)=\underline{p}$ and $\underline{\alpha}(1)=\underline{q}$. It is easy to show that $d_S(\underline{p},\underline{q})=d_S(\underline{q},\underline{p})$ and that the triangle inequality$$\Huge d_S(\underline{p}_1,\underline{p}_3)\leq d_S(\underline{p}_1,\underline{p}_2)+d_S(\underline{p}_2,\underline{p}_3)$$holds. It is more work to show that if $\underline{p}\neq\underline{q}$ then $d_S(\underline{p},\underline{q})>0$. This is a consequence of the Gauss Lemma. We now mention (without proof) facts about geodesics in connection to this distance function:
> Minimising curves are geodesics: If $\underline{\alpha}:[a,b]\to S$ is a curve satisfying$$\Huge d_S(\underline{\alpha}(a),\underline{\alpha}(b))=L(\underline{\alpha})$$then $\underline{\alpha}$ is, up to constant speed reparametrisation, a geodesic. Such geodesics are called minimal geodesics. For a pair of points $\underline{p},\underline{q}$ there may be many curves $\underline{\alpha}:[a,b]\to S$ with different traces connecting $\underline{p}=\underline{\alpha}(a)$ and $\underline{q}=\underline{\alpha}(b)$ that satisfy this. For examples, all great semicircles connecting opposing poles satisfy this property.
> Not every geodesic is minimising: A geodesic is not necessarily globally the shortest curve between its end-points.
> Geodesics are always locally minimising: Let $\underline{\alpha}:[a,b]\to S$ be a geodesic and $\underline{p}=\underline{\alpha}(t_0)$. Then there exists a positive constant $c>0$ such that for any $\underline{q}=\underline{\alpha}(t_1)$ with $|t_1-t_0|\leq c$$$\Huge d_S(\underline{\alpha}(t_0),\underline{\alpha}(t_1))=L(\underline{\alpha}|_I)$$where $I=[t_0,t_1]\subset[a,b]$ if $t_0<t_1$ and $I=[t_1,t_0]\subset[a,b]$ otherwise.

The connection between minimising curves on a connected surface and geodesics is more subtle than in the simple case of the Euclidean plane, however it still holds that minimising curves are geodesics.

Let us consider Geodesics on the hyperbolic plane:
> Let $\mathbb{H}^2=\{z=u+iv\in\mathbb{C}:v>0\}$ be the upper half plane model of the hyperbolic plane with:$$\Huge E(u,v)=G(u,v)=\frac{1}{v^2},\,\,F(u,v)=0$$
> We know that geodesics $\underline{\alpha}(t)=(u(t),v(t))$ are solutions of differential equations, which simplify to:$$\Huge\begin{align*}
u''E(u,v)&=-u'v'E_v(u,v)\\
v''G(u,v)&=-\frac{1}{2}(v')^2G_v(u,v)+\frac{1}{2}(u')^2E_v(u,v)
\end{align*}$$Since $E_v(u,v)=G_v(u,v)=-\frac{2}{v^3}$ we write these equations as:$$\Huge u''=\frac{2u'v'}{v},\,\,v''=\frac{(v')^2-(u')^2}{v}$$
> Assuming $u$ is constant, the first equation is trivially satisfied and the second simplifies to$$\Huge v''v-(v')^2=0\implies_{v>0}\left(\frac{v'}{v}\right)'=\frac{v''v-(v')^2}{v^2}=0$$, that is $v'/v$ is constant. Taking $v'/v=C$ leads to (if $C\neq0$) $v(t)=Ae^{Ct}$ for $A>0$. A unit speed geodesic is therefore$$\Huge \underline{\alpha}(t)=(u(t),v(t))=(0,e^t)$$since $\underline{\alpha}'(t)=(0,e^t)\in T_{\underline{\alpha}(t)}\mathbb{H}^2$ and:$$\Huge \underline{I}_{\underline{\alpha}(t)}(\underline{\alpha}'(t))=\frac{\underline{\alpha}'(t)\cdot\underline{\alpha}'(t)}{v(t)^2}=\frac{e^{2t}}{e^{2t}}=1$$
> Since [[Mobius transform#Finding Mobius transforms|Mobius transformations]] are isometries of $\mathbb{H}^2$, curves $\underline{\beta}=f_A\circ\underline{\alpha}:\Re\to\mathbb{H}^2$ ,with $f_A$ the Mobius transform, are also geodesics in $\mathbb{H}^2$.

# Clairaut's Theorem:

We now explore geodesics on surfaces of revolution. Let $S\subset\Re^3$ be a surface of revolution with local parametrisation$$\Huge \underline{x}(u,v)=(f(v)\cos u,f(v)\sin u,g(v))$$for $(u,v)\in(0,2\pi)\times[a,b]$ and $\underline{\alpha}(t)=\underline{x}(u(t),v(t))$. If we assume $f(v)>0$ for all $v\in[a,b]$ then we deduce $E(u,v)=E(v)=f(v)^2,F(u,v)=0,G(u,v)=G(v)=(f'(v))^2+(g'(v))^2$ and the geodesic defining differential equations take form:$$\Huge\begin{align*}
u''E+u'v'E_v&=0\\
v''G+\frac{1}{2}(v')^2G_v-\frac{1}{2}(u')^2E_v&=0
\end{align*}$$The first equation is rewritten as $(u'E)'=0$, implying $c=u'E$ and therefore$$\Huge u'=\frac{c}{f(v)^2}$$for some constant $c\in\Re$. Assuming the generating curve has unit speed, we have $G=1$ and the second equation simplifies to:$$\Huge v''=(u')^2f(v)f'(v)=\frac{c^2f'(v)}{f(v)^3}$$Consequently, surfaces of revolution with an arc length parametrised generating curve, a curve $\underline{\alpha}(t)=\underline{x}(u(t),v(t))$ is a geodesic if and only if the two equations above are satisfied.

From this we draw the following conclusion. Let $S\subset\Re^3$ be a regular surface of revolution with unit speed generating curve $v\to(f(v),0,g(v))$ with $f>0$ and parametrisation:$$\Huge \underline{x}(u,v)=(f(v)\cos u,f(v)\sin u,g(v))$$Then all meridians $\underline{\alpha}(t)=\underline{x}(u_0,t)$ are geodesics and parallels $\underline{\beta}(t)=\underline{x}(t,v_0)$ are geodesics if and only if $f'(v_0)=1$. Proof:
> Let us first verify the meridians. In this case we have $u(t)=u_0$ and $v(t)=t$, implying that $u'=0$ and therefore the first equation holds with $c=0$. We also have $v''=0$ and so the other equation is automatically satisfied.
> Now considering the parallels, given by $\underline{\beta}(t)=\underline{x}(t,v_0)$. Here we have $u(t)=t,v(t)=v_0$ implying that $u'=1$, so the first equation is satisfied with $c=f(v)^2>0$. Consequently, the second equation simplifies to the condition:$$\Huge v''=\frac{c^2f'(v)}{f(v)^3}=f(v)f'(v)$$However $v(t)=v_0$ implies $v''=0$ and since $f>0$ this equation is satisfied if and only if $0=f'(v(t))=f'(v_0)$, proving the second part of the proposition.

This is illustrated in the following render:![[Pasted image 20260319164003.png|355]]Where black curves are geodesics, while the red one is not.

We can now present Clairaut's theorem: Let $S\subset\Re^3$ be a surface of revolution and let $\underline{\alpha}:I\to S$ be a geodesic. Let $d:I\to(0,\infty)$ be the distance of $\underline{\alpha}$ from the $z$-axis and $\theta:I\to\Re$ be the angle at which $\underline{\alpha}$ intersects the corresponding parallel. Then we have:$$\Huge d(t)\cos(\theta(t))=\text{constant}$$The proof of which is omitted.

Let us apply this theorem to a Torus of revolution:
> A torus of revolution $S\subset\Re^3$ is given as follows. Let $C$ be a circle of radius $r>0$ in the $(x,z)$-coordinate plane around $(R,0,0)$. That is$$\Huge C=\{(R+r\cos v,0,r\sin v):v\in[0,2\pi)\}$$, we then obtain $S$ by rotating $C$ around the $z$-axis:$$\Huge S=\{((R+r\cos v)\cos u,(R+r\cos v)\sin u,r\sin v):u,v\in[0,2\pi)\}$$
> We know that there must exists a unique geodesic $\underline{\alpha}$ starting at $(R+r,0,0)\in S$ in a specific direction at an angle $\theta_0$ to the corresponding parallel, given by $x^2+y^2=(R+r)^2,z=0$. In the case of the Torus, such a geodesic exists globally as a map $\underline{\alpha}:\Re\to S$$$\Huge \underline{\alpha}(t)=((R+r\cos v(t))\cos u(t),(R+r\cos v(t))\sin u(t),r\sin v(t))$$with suitable function $u,v:\Re\to\Re$.
> Let $d,\theta$ be the corresponding functions introduced above. Then we have $d(0)=R+r$ and $\underline{\alpha}(0)=\theta_0$ and we can conclude that for all $t\in\Re$:$$\Huge\begin{align*}
d(t)\cos(\theta(t))&=(R+r\cos v(t))\cos\theta(t)\\
&=d(0)\theta(0)=(R+r)\cos\theta_0
\end{align*}$$
> In particular we must have $d(t)\geq(R+r)\cos\theta_0$ for all $t\in\Re$ since $\cos\theta(t)\leq1$. Consequently, a geodesic starting at $(R+r,0,0)$ with a small angle $|\theta_0|$ to the corresponding parallel is trapped in a certain neighbourhood of this parallel, that is, in the intersection of $S$ with all points of distance at least $(R+r)\cos\theta_0$ to the vertical $z$-axis.

