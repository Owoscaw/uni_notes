
# Vector calculus and Dirac delta:

The study of electromagnetism requires some knowledge from vector calculus. We recall some of the main results in [[Index notation|index notation]] and assume that all functions considered have continuous second order partial derivatives, so that they commute.

We prove the following results for any function $f$ and vector field $\underline A$:
1. $$\Huge \underline{\nabla}\cdot(\underline{\nabla}\times\underline A)=0$$where $\underline{\nabla}\cdot$ represents the [[Differential operators#Differentiating vector fields|divergence]] and $\underline{\nabla}\times$ represents the curl of the vector field $\underline A$:$$ \underline{\nabla}\cdot(\underline{\nabla}\times\underline A)=\partial_i\epsilon_{ijk}\partial_jA_k=\epsilon_{ijk}\partial_i\partial_jA_k=-\epsilon_{jik}\partial_j\partial_iA_k=-\epsilon_{ijk}\partial_i\partial_jA_k=-\underline{\nabla}\cdot(\underline{\nabla}\times\underline A)$$Hence $\underline{\nabla}\cdot(\underline{\nabla}\times\underline A)=0$ as required. We have used the antisymmetry of [[Index notation#Vector products|$\epsilon_{ijk}$]] with a relabeling from $i,j\to j,i$.

2. $$\Huge \underline{\nabla}\times\underline{\nabla}f=0$$That is, the curl of the gradient of $f$ is zero:$$\Huge (\underline{\nabla}\times\underline{\nabla}f)_i=\epsilon_{ijk}\partial_j\partial_jf=-\epsilon_{ikj}\partial_k\partial_jf=-\epsilon_{ijk}\partial_j\partial_kf=-(\underline{\nabla}\times\underline{\nabla}f)_i$$Hence $\underline{\nabla}\times\underline{\nabla} f=0$ as required.
3. $$\Huge \underline{\nabla}\times(\underline{\nabla}\times\underline A)=\underline{\nabla}(\underline{\nabla}\cdot\underline A)-\nabla^2\underline A$$where $\nabla^2$ is the Laplacian. This is proven as follows:$$\Huge\begin{align}
(\underline{\nabla}\times(\underline{\nabla}\times\underline A))_i&=\epsilon_{ijk}\partial_j\epsilon_{kpq}\partial_pA_q\\
&=\epsilon_{kij}\epsilon_{kpq}\partial_j\partial_pA_q\\
&=(\delta_{ip}\delta_{jq}-\delta_{iq}\delta_{jp})\partial_j\partial_pA_q\\
&=\partial_i\partial_jA_j-\partial_j\partial_jA_i\\
&=\partial_i(\underline{\nabla}\cdot \underline A)-\nabla^2A_i\\
&=(\underline{\nabla}(\underline{\nabla}\cdot\underline A)-\nabla^2\underline A)_i
\end{align}$$
Note that the [[Integral theorems#Divergence theorem|divergence theorem]] applies to a region $V$ of space which has a boundary given by a closed surface $S$. We denote this as $\partial V=S$ and write:$$\Huge \int_V\underline{\nabla}\cdot\underline A\,dV=\int_S\underline A\cdot\underline{dS}$$It follows that [[Integral theorems#Stokes' theorem|Stoke's theorem]] also applies to a surface $S$ with boundary given by the closed curve $C$, which we denote as $\partial S=C$:$$\Huge \int_S(\underline{\nabla}\times\underline A)\cdot\underline{dS}=\oint_C\underline A\cdot\underline{dr}$$with the notation $\underline r=(x,y,z)=(x_1,x_2,x_3)=\underline x$.

Considering a single spatial dimension we define the function:$$\Huge h(x)=\begin{cases}1/\epsilon&|x|\leq\epsilon/2\\0&|x|>\epsilon/2\end{cases}$$for some positive constant $\epsilon$. Then it is clear that the integral:$$\Huge \int_{-\infty}^\infty h(x)dx=1$$and is independent of $\epsilon$. The Dirac delta function is then obtained from taking $\lim_{\epsilon\to0}h(x)$:$$\Huge \lim_{\epsilon\to0}h(x)=\delta(x)=\begin{cases}\infty&x=0\\0&x\neq0\end{cases}$$with:$$\Huge \int_{-\infty}^\infty\delta(x)dx=\lim_{\epsilon\to0}\int_{-\infty}^\infty h(x)dx=\lim_{\epsilon\to0}1=1$$It is useful to show that:$$\Huge \int_{-\infty}^\infty f(x)\delta(x)dx=\int_{-\infty}^\infty f(0)\delta(x)dx=f(0)\int_{-\infty}^\infty\delta(x)dx=f(0)$$
We can also shift the argument of the Dirac delta function by any constant $x_0$ to get:$$\Huge\begin{align}
\int_a^b\delta(x-x_0)dx&=\begin{cases}1&x_0\in(a,b)\\0&x_0\notin[a,b]\end{cases}\\
\int_a^bf(x)\delta(x-x_0)&=\begin{cases}f(x_0)&x_0\in(a,b)\\0&x_0\notin[a,b]\end{cases}
\end{align}$$
This function generalises to three-dimensional space with the following definitions:$$\Huge\begin{align}
\delta(\underline r-\underline r_0)&=\begin{cases}\infty&\underline r=\underline r_0\\0&\underline r\neq\underline r_0\end{cases}\\
\int_Vf(\underline r)\delta(\underline r-\underline r_0)dx&=\begin{cases}f(\underline r_0)&\underline r_0\in V\\0&\underline r_0\in V\end{cases}
\end{align}$$

# Charges, currents, and fields:

Electric charge $q$ is a real number associated with a particle that specifies how it interacts with the force of electromagnetism. If $q=0$ the particle is unaffected by the electromagnetic force, otherwise we call the particle charged. Such charge can be positive or negative.

We can extend the notion of charge of a point particle to the charge density $\rho(\underline x)$ defined so that the amount of charge in the region $\delta V$ containing $\underline x$ is $\rho(\underline x)\delta V$. The total charge $Q$ in a region $V$ is therefore given by:$$\Huge Q=\int_V\rho\,dV$$
A point particle with charge $q$ and position $\underline X$ in space corresponds to charge density $\rho=q\delta(\underline x-\underline X)$. The presence of the Dirac delta function represents the fact that all charge is contained in the point $\underline X$.

Charge can flow from one place to another, described by electric current density $\underline J(\underline x)$ defined by the property that for any surface $S$, the integral:$$\Huge I=\int_S\underline J\cdot dS$$gives the charge per unit time passing through $S$. $I$ is called the electric current with SI unit Ampere (amp). If a small volume moving with velocity $\underline v$ has a charge density $\rho$ then the current density is given by $\underline J=\underline v\rho$.

Total electric charge is conserved, so can only move around and cannot be created or destroyed. If we consider a region $V$ then we must have that charge $Q$ in the region can only change if charge moves in or out of the region:$$\Huge \frac{d Q}{dt}=\int_V\frac{\partial \rho}{\partial t}dV=-\int_S\underline J\cdot dS=-\int_V\underline{\nabla}\cdot\underline J\,dV$$where $S$ is the surface that is the boundary of $V$. Note the negative sign is present as $dS$ points outward normal to the surface, so measured the flow of charge out of $V$. We therefore have that:$$\Huge \int_V\left(\frac{\partial \rho}{\partial t}+\underline{\nabla}\cdot\underline J\right)dV=0$$for any region $V$. Taking $V$ to be an infinitesimal region around a point $\underline x$, we conclude that the integrand must vanish at such point. This gives the continuity equation:$$\Huge \frac{\partial \rho}{\partial t}+\underline{\nabla}\cdot\underline J=0$$
Electric and magnetic fields, denoted as $\underline E$ and $\underline B$, are three dimensional vectors that are defined at every point in space and at any time. We call the Lorentz force on a particle the sum:$$\Huge \underline F=q(\underline E+\underline v\times\underline B)$$for some particle travelling at velocity $\underline v$. We can take this as the definition of the electric and magnetic fields.

# Maxwell's equations:
$$\Huge\begin{align}
(1)&&\underline{\nabla}\cdot\underline E&=\rho/\epsilon_0\\
(2)&&\underline{\nabla}\cdot\underline B&=0\\
(3)&&\underline{\nabla}\times\underline E&=-\frac{\partial \underline B}{\partial t}\\
(4)&&\underline{\nabla}\times\underline B&=\mu_0\left(\underline J+\epsilon_0\frac{\partial \underline E}{\partial t}\right)
\end{align}$$The two constants $\epsilon_0,\mu_0$ are known as the permittivity and permeability of free space, or electric and magnetic constants. These constants quantify the strength of electric and magnetic interactions. Note that for some fucking reason:$$\Huge c=\frac{1}{\sqrt{\epsilon_0\mu_0}}$$
In the absence of charges or currents we consider the source-free versions of Maxwells equations ($\rho=\underline J=0$):$$\Huge\begin{align}
(1)&&\underline{\nabla}\cdot\underline E&=0\\
(2)&&\underline{\nabla}\cdot\underline B&=0\\
(3)&&\underline{\nabla}\times\underline E&=-\frac{\partial \underline B}{\partial t}\\
(4)&&\underline{\nabla}\times\underline B&=\mu_0\epsilon_0\frac{\partial \underline E}{\partial t}
\end{align}$$We can take the curl of $(3)$ which gives:$$\Huge \underline{\nabla}\times(\underline{\nabla}\times\underline E)=-\frac{\partial }{\partial t}(\underline{\nabla}\times\underline B)$$applying $(4)$ gives:$$\Huge \underline{\nabla}\times(\underline{\nabla}\times\underline E)=\underline{\nabla}(\underline{\nabla}\cdot\underline E)-\nabla^2\underline E=-\mu_0\epsilon_0\frac{\partial^2\underline E}{\partial t^2}$$the first term vanishes due to $(1)$ so we get:$$\Huge \frac{1}{c^2}\frac{\partial^2\underline E}{\partial t^2}-\nabla^2\underline E=0$$which is precisely the wave equation with wave speed $c=1/\sqrt{\epsilon_0\mu_0}$. A similar calculation shows the same for magnetic fields:$$\Huge \frac{1}{c^2}\frac{\partial^2\underline B}{\partial t^2}-\nabla^2\underline B=0$$This all shows that light is indeed an electromagnetic wave, unifying the topics of electricity, magnetism, and optics.

