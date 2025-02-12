# Winding numbers and simply connected sets:

Assume we have a curve $\gamma:[a,b]\rightarrow\mathbb{C}$ of the form:$$\Huge \gamma(t)=\omega+r(t)e^{i\theta(t)}$$where $\omega\in\mathbb{C}$ and $r,\theta:[a,b]\rightarrow\mathbb{C}$ are piecewise $C^1$ continuous functions with $r(t)>0$ for all $t\in[a,b]$. We define:$$\Huge I(\gamma,\omega)=\frac{\theta(b)-\theta(a)}{2\pi}$$called the winding number of the curve $\gamma$ around $\omega$. Note that $\omega\notin\gamma$ since $r(t)>0$.

If a curve $\gamma$ of this form is closed, then $I(\gamma,\omega)\in\mathbb{Z}$. Since $\gamma$ is closed, we have $\gamma(a)=\gamma(b)\implies r(a)e^{i\theta(a)}=r(b)e^{i\theta(b)}\implies r(a)=r(b)$ and that $e^{i\theta(a)}=e^{i\theta(b)}$, therefore $\theta(b)-\theta(a)\in2\pi\mathbb{Z}\implies I(\gamma,\omega)\in\mathbb{Z}$ as required.

Let $\gamma:[a,b]\rightarrow\mathbb{C}$ be a [[Complex integration#Contours|contour]] and $\omega\in\mathbb{C}$ with $\omega\notin\gamma$. Then there exists $r,\theta:[a,b]\rightarrow\Re$ piecewise $C^1$ continuous and $r(t)>0$ such that:$$\Huge \gamma(t)=\omega+r(t)e^{i\theta(t)}$$

Let $\gamma:[a,b]\rightarrow\mathbb{C}$ be a closed contour and $\omega\notin\gamma$, then:$$\Huge I(\gamma,\omega)=\frac{1}{2\pi i}\int_\gamma\frac{1}{z-\omega}dz$$To prove this, we write $\gamma(t)=\omega+r(t)e^{i\theta(t)}$ and observe:$$\Huge\begin{align}
\int_\gamma\frac{1}{z-\omega}dz&=\int_a^b\frac{\gamma'(t)}{\gamma(t)-\omega}dt\\
&=\int_a^b\frac{r'(t)}{r(t)}+i\theta'(t)dt\\
&=[\ln(r(t))+i\theta(t)]_a^b\\
&=i(\theta(b)-\theta(a))=2\pi iI(\gamma,\omega)
\end{align}$$As required.

Let $D$ be a [[Cauchy's theorem#Starlike domains|starlike domain]]. If $\gamma$ is a closed contour in $D$ and $\omega\notin D$, then $I(\gamma,\omega)=0$. The function $f(z)=\frac{1}{z-\omega}$ is [[Complex differentiation#Holomorphicity|holomorphic]] on $D$ since $\omega\notin D$ and since $\gamma$ is closed on this domain, by Cauchy's theorem we have:$$\Huge I(\gamma,\omega)=\frac{1}{2\pi i}\int_\gamma\frac{1}{z-\omega}dz=0$$

Let $U\subset\mathbb{C}$ be an open set:
> A closed contour $\gamma\in U$ is called homologous to zero in $U$ if $I(\gamma,\omega)=0\,\forall\omega\notin U$.
> The open set $U$ is called simply connected if every closed contour in $U$ is homologous to zero in $U$.

## Cycles:
A cycle $\Gamma$ on an open set $U$ is a finite collection of contours $\gamma_1,\gamma_2,\dots,\gamma_n$. We write $\Gamma=\gamma_1+\gamma_2+\dots+\gamma_n$. We say that a point $\omega\in\mathbb{C}$ does not lie in $\Gamma$ if $\omega\notin\gamma_i$ for all $i=1,2,\dots,n$. For such a point we define the winding number of the cycle:$$\Huge I(\Gamma,\omega)=\sum_{i=1}^nI(\gamma_i,\omega)$$moreover we define:$$\Huge \int_\Gamma f(z)dz=\sum_{i=1}^n\int_{\gamma_i}f(z)dz$$We say that the cycle $\Gamma$ is homologous to zero in $U$ if for every $\omega\notin U$ we have $I(\Gamma,\omega)=0$.

Consider the annulus $A=\{z\in\mathbb{C}:r<|z-a|<R\}$ for some $a\in\mathbb{C}$ and $0\leq r<R\leq\infty$. Let $\gamma_1(t)=a+\rho_1e^{-2\pi it}$ and $\gamma_2(t)=a+\rho_2e^{2\pi it}$ for $t\in[0,1]$ and $r<\rho_1<\rho_2<R$. Then the cycle $\Gamma=\gamma_1+\gamma_2$ is homologous to zero in $A$.

# General forms of Cauchy's theorem and CIF:

Let $f:D\rightarrow\mathbb{C}$ be holomorphic on a domain. Then for any cycle that is homologous to zero in $D$ and any $\omega\notin\Gamma$ we have:
>The general form of Cauchy's theorem:$$\Huge \int_\Gamma f(z)dz=0$$
>The general form of CIF:$$\Huge \int_\Gamma\frac{f(z)}{z-\omega}dz=2\pi iI(\Gamma,\omega)f(\omega)$$

Given a simply connected domain, we have $\int_\gamma f(z)dz=0$ for all closed $\gamma$. The proof is trivial.

We say that a closed curve $\gamma:[a,b]\rightarrow\mathbb{C}$ is simple if $\gamma(a)=\gamma(b)$ and if $\gamma(t_1)=\gamma(t_2)$ for $t_1<t_2$ then $t_1=a,t_2=b$.

## Jordan curve theorem:
Suppose $\gamma$ is a simple closed contour. Then $\mathbb{C}\setminus\gamma$ can be expressed as a disjoint union of two domains, exactly one of which is bounded. We call the bounded domain the interior, $D_\gamma^{\text{int}}$, and the other the exterior, $D_\gamma^{\text{ext}}$. We say that $f$ is holomorphic on $D_\gamma^{\text{int}}\cup\gamma$ if there exists a domain $D_\gamma^{\text{int}}\cup\gamma\subset D$ on which $f$ is holomorphic.

Given a simple closed contour, we can give $\gamma$ an orientation such that:$$\Huge I(\gamma,\omega)=\begin{cases}1&\omega\in D_\gamma^{\text{int}}\\0&\omega\in D_\gamma^{\text{ext}}\end{cases}$$
## Cauchy's theorem for simple closed contours
Let $\gamma$ be a simple closed contour and let $f$ be holomorphic on $D_\gamma^{\text{int}}\cup\gamma$. Then for any $\omega\in D_\gamma^{\text{int}}$:$$\Huge \int_\gamma f(z)dz=0$$and:$$\Huge \int_\gamma\frac{f(z)}{z-\omega}dz=2\pi if(\omega)$$for some $\omega\in D_\gamma^{\text{int}}$.