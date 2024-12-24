There are several generalisations of the [[year 1/analysis 1/term 2/Integration#Fundamental theorem of Calculus|fundamental theorem of calculus]] that apply to vector calculus. One of which is the fundamental theorem of [[Line integrals|line integrals]]:

# Fundamental theorem of line integrals:

If $f:\Re^n\mapsto\Re$ is a $C^1$ scalar field and $C$ is an oriented curve with parametrisation $\underline x(t)$ for $t\in[t_0,t_1]$:$$\Huge \int_C\underline{\nabla}f\cdot\hat{\underline t}dl=f(\underline x(t_1))-f(\underline x(t_2))$$We prove this for $n=3$:$$\Huge\begin{align} \int_C\underline{\nabla}f\cdot\hat{\underline t}dl&=\int_{t_0}^{t_1}\underline{\nabla}f\cdot\frac{d \underline x}{dt}dt\\
&=\int_{t_0}^{t_1}\left(\frac{\partial f}{\partial x}\frac{d x}{dt}+\frac{\partial f}{\partial y}\frac{d y}{dt}+\frac{\partial f}{\partial z}\frac{d z}{dt}\right)dt\\
&=\int_{t_0}^{t_1}\frac{d f}{dt}dt\\
&=f(t_1)-f(t_0)=f(\underline x(t_1))-f(\underline x(t_0))
\end{align}$$Where we have used the chain rule to make the integrand a total derivative.

A vector field $f:\Re^n\mapsto\Re^n$ is called conservative if it can be written as $\underline f=\underline{\nabla}g$ for some $C^1$ scalar field $g:\Re^n\mapsto\Re$. Such a scalar field is called a scalar potential of $\underline f$. Take for example:![[scalar potential example]]Note that $\underline f=\underline{\nabla}g$ only defines $g$ up to a constant, hence the presence of the constant in the scalar potential $g(x,y)$.

## Path independence:
A vector field is conservative if and only if it has path independent line integrals between any pair of points:![[path independence proof]]Here we have used the [[year 1/analysis 1/term 2/Integration#MVT for integrals|MVT]] for integrals. The proof is analogous for other components of $g$.

# Divergence theorem:

If $\underline f:\Re^3\mapsto\Re^3$ is a $C^1$ vector field and $S$ is a closed surface with outwards normal $\underline{\hat{n}}$, bounding a region $V$, then:$$\Huge \oint_S\underline f\cdot\underline{\hat{n}}\,dS=\int_V(\underline{\nabla}\cdot\underline f)dV$$This generalises to $V\subset\Re^n$ with boundary $S$ on $n-1$ dimension hypersurface. For $n=1$ we have $V=[a,b],S=\{a,b\}$, $\underline f=f(x)\underline e_1$, $\underline{\nabla}\cdot\underline f=f'(x)$, and $\underline{\hat{n}}=\begin{cases}-\underline e_1&x=a\\-\underline e_1&x=b\end{cases}$. Then this reduces to $f(b)-f(a)$, the fundamental theorem of calculus. The proof of this theorem involves subdividing $V$ into a disjoint union of smaller domains $V_i$ for $i\in\{1,\dots,m\}$ where each boundary $S_i$ have unit normal $\underline{\hat{n}}_i$:![[divergence proof theorem]]

Then each interior segment of $S_i$ is shared by a neighboring subdomain $V_j$, with equal and opposite $\underline{\hat{n}}_j$. So we write:$$\Huge\begin{align} 
\oint_S\underline f\cdot\underline{\hat{n}}\,dS&=\sum_{i=1}^m\oint_{S_i}\underline f\cdot\underline{\hat{n}}_idS\\
&=\sum_{i=1}^m\left(\frac{1}{|V_i|}\oint_{S_i}\underline f\cdot\underline{\hat{n}}_idS\right)|V_i|\\
&=\lim_{m\to\infty}\sum_{i=1}^m\left(\frac{1}{|V_i|}\oint_{S_i}\underline f\cdot\underline{\hat{n}}_idS\right)|V_i|\\
&=\int_V(\underline{\nabla}\cdot\underline f)dV
\end{align}$$For this to work, we require $\underline f\in C^1$. This theorem applies even when $S$ is not connected, i.e. two concentric spheres. Suppose that $S$ is the boundary of $V$ and can be written as $S=S_0\cup S_1$, then:$$\Huge \oint_{S_0}\underline f\cdot\underline{\hat{n}}_0\,dS+\oint_{S_1}\underline f\cdot\underline{\hat{n}}_1\,dS=\int_V(\underline{\nabla}\cdot\underline f)dV$$This theorem plays a large role in converting between differentiation and integration when considering conservation laws.

# Stokes' theorem:

If $\underline f:\Re^3\mapsto\Re^3$ is a $C^1$ vector field and $C$ is an oriented closed curve bounding a surface $S$, then:$$\Huge \oint_C\underline f\cdot\hat{\underline t}\,dl=\int_S(\underline{\nabla}\times\underline f)dS$$Where $\underline{\hat{n}}$ is chosen such that $\hat{\underline t}\times\underline{\hat{n}}$ on $C$ is outward:![[stokes]]
The surface $S$ is sometimes called a capping surface of $C$. Stokes' theorem dictates that the flux is the same through every possible surface, $S$, sharing the boundary $C$.

Example:![[stokes' example]]
## Proof:
To prove Stokes' theorem we must show the following lemmas.

Let $C$ be a curve in the plane with unit normal $\underline{\hat{n}}$ with diameter $d(C)$, closed area $|A|$, and containing the point $\underline x$. Then for any vector field $\underline f:\Re^3\mapsto\Re^3$:$$\Huge \underline{\hat{n}}\cdot(\underline{\nabla}\times\underline f)\vert_{\underline x}=\lim_{d(C)\to 0}\frac{1}{|A|}\oint_C\underline f\cdot\hat{\underline t}\,dl$$Where $C$ is oriented such that $\hat{\underline t}=\underline{\hat{n}}\times\underline{\hat{n}}_C$:![[pill lemma]]To prove this, we can "extrude" $C$ by a small distance $h$ in the $\underline{\hat{n}}$ direction to form a surface with normal $\underline{\hat{n}}_S$:![[pill lemma 2]]Then by definition of curl:$$\Huge\begin{align}
\underline{\hat{n}}\cdot(\underline{\nabla}\times f)\vert_{\underline x}&=\underline{\hat{n}}\cdot\left(\lim_{d(S)\to0}\frac{1}{|V|}\oint_S\underline{\hat{n}}_S\times\underline f\,dS\right)\\
&=\lim_{d(S)\to0}\frac{1}{|V|}\oint_S\underline{\hat{n}}\cdot(\underline{\hat{n}}_S\times\underline f)dS\\
&=\lim_{|A|,h\to0}\frac{1}{h|A|}\oint_S\underline f\cdot(\underline{\hat{n}}\times\underline{\hat{n}}_S)dS\\
&=\lim_{|A|,h\to0}\frac{1}{h|A|}\oint_{\tilde S}\underline f\cdot(\underline{\hat{n}}\times\underline{\hat{n}}_C)d\tilde S
\end{align}$$Now we parametrise $\tilde S$ by $\tilde{\underline x}(t,v)=\underline x_C(t)+v\underline{\hat{n}}$ for $v\in[0,h]$ and $t\in[t_0,t_1]$. We must now calculate the Jacobian:$$\Huge \left|\frac{\partial \underline{\tilde x}}{\partial t}\times\frac{\partial \underline{\tilde x}}{\partial v}\right|=\left|\frac{d \underline x_C}{dt}\times\underline{\hat{n}}\right|=\left|\frac{d \underline x_C}{dt}\right||\underline{\hat{n}}|=\left|\frac{d \underline x_C}{dt}\right|$$So we get the following:$$\Huge\begin{align}
\int_{\tilde S}\underline f\cdot(\underline{\hat{n}}\times\underline{\hat{n}}_C)d\tilde S&=\int_{t_0}^{t_1}\int_0^h\underline f\cdot(\underline{\hat{n}}\times\underline{\hat{n}}_C)\left|\frac{d \underline x_C}{dt}\right|dv\,dt\\
&=\int_{t_0}^{t_1}(\underline{\hat{n}}\times\underline{\hat{n}}_C)\cdot\left(\int_0^h\underline f\,dv\right)\left|\frac{d \underline x_C}{dt}\right|dt\\
&=h\int_{t_0}^{t_1}(\underline{\hat{n}}\times\underline{\hat{n}}_C)\cdot\underline f(t,v_*(t))\left|\frac{d \underline x_C}{dt}\right|dt
\end{align}$$When taking the limit as $h\to0$ we have that $v_*(t)\to0$ for all $t$, so we get:$$\large \underline{\hat{n}}\cdot(\underline{\nabla}\times\underline f)\vert_{\underline x}=\lim_{|A|\to0}\frac{1}{|A|}\int_{t_0}^{t_1}(\underline{\hat{n}}\times\underline{\hat{n}}_C)\cdot \underline f(t,0)\left|\frac{d \underline x_C}{dt}\right|dt=\lim_{|A|\to 0}\frac{1}{|A|}\oint_C\underline f\cdot\underline{\hat t}\,dl$$As required. This proof used the [[year 1/analysis 1/term 2/Integration#MVT for integrals|MVT]] for integrals and the fact that $\underline{\hat t}$ is tangent to the curve $C$. We can now prove Stokes' theorem. First we subdivide $S$ into a disjoint union of small regions $S_i$ for $i\in\{1,\dots,m\}$ whose bounding curve have unit tangent vectors $\underline{\hat t}_i$:![[stokes proof]]We see that each interior boundary segment is shared by four neighboring regions with equal and opposite tangents except for along the boundary. So we write:$$\Huge\begin{align}
\oint_C\underline f\cdot\underline{\hat{t}}\,dl&=\sum_{i=1}^n \oint_{S_i}\underline f\cdot \underline{\hat{t}}_idl\\
&=\sum_{i=1}^n\left(\frac{1}{|A_i|}\oint_{S_i}\underline f\cdot\underline{\hat{t}}_idl\right)|A_i|\\
&=\lim_{m\to\infty}\sum_{i=1}^m\left(\frac{1}{|A_i|}\oint_{S_i}\underline f\cdot\underline{\hat{t}}_idl\right)|A_i|=\int_S(\underline{\nabla}\times\underline f)\cdot\underline{\hat{n}}\,dS
\end{align}$$Where we used the lemma on the last line. So we have Stokes' theorem as required. Note that there is a much more general form of Stokes' theorem in differential calculus written as:$$\Huge \int_\Omega d\omega=\int_{\partial \Omega}\omega$$Where $\Omega$ is a manifold, $\partial\Omega$ is its boundary, $d$ is the exterior derivative, and $\omega$ is the differential form. Divergence theorem and Stokes' theorem are special cases of  this formula.


## Green's theorem:
If $\underline f:\Re^2\mapsto\Re^2$ is a $C^1$ vector field and $C$ is a closed curve in the plane oriented anti-clockwise, then:$$\Huge \oint_C\underline f\cdot\hat{\underline t}\,dl=\int_A\left(\frac{\partial f_2}{\partial x}-\frac{\partial f_1}{\partial y}\right)dx\,dy$$Where $A$ is the area enclosed by $C$. This is a direct corollary of Stokes' theorem.


If $\underline f:\Re^3\mapsto\Re^3$ is a $C^1$ vector field with $\underline{\nabla}\times\underline f=\underline 0$ throughout some simply-connected region $V\subset\Re^3$ then $\underline f$ is conservative in $V$. A domain is simply connected if any curve can be shrunk to a point in the domain.

To prove this, recall that $\underline f=\underline{\nabla}g$ if and only if $\underline f$ has path independent line integrals. Consider two arbitrary curves $C_1,C_2$ between two arbitrary points $\underline x_a,\underline x_b\in V$. Define the closed curve $C=C_1-C_2$. Since $V$ is simply connected, there exists a capping surface $S\subset V$ for $C$. Stokes' theorem implies that $\oint_C\underline f\cdot\hat{\underline t}\,dl=0$, which implies $\int_{C_1}\underline f\cdot\hat{\underline t}\,dl=\int_{C_2}\underline f\cdot\hat{\underline t}\,dl$, that is path independence holds, implying that $\underline f$ is conservative.