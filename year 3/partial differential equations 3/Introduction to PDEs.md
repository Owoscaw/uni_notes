
PDEs are equations that describe the change of a given quantity that depends on several variables. 

# The vibration of a string:

PDEs are often approximations or models of real world phenomena. As a first example, we look at the vibrational behavior (displacement from equilibrium over time) while neglecting effects due to gravity. Consider an infinitesimal segment of the string:
![[wave equation derivation]]
As we are considering an infinitesimal string segment, $\Delta x$ is considered an infinitesimal change in $x$. Here, $u(x,t)$ is the displacement of the string, $T(x,t)$ is the tension, and $\theta(x,t)$ is the angle made between the tension in the string and the horizontal line passing through $(x,u(x,t))$. Then we have:$$\Huge \tan(\theta(x,t))=\frac{\partial u}{\partial x}(x,t)$$
We assume that the vibration is only in the direction of the vertical axis and that all functions involved are differentially continuous.

Using Newton's second law we see that:$$\Huge T(x,t)\cos(\theta(x,t))=T(x+\Delta x,t)\cos(\theta(x+\Delta x,t))$$as the horizontal forces must cancel out. Note that as $\Delta x$ is infinitesimal, we can use a first order [[Taylor series|Taylor approximation]] to write:$$\Huge T(x+\Delta x,t)\cos(\theta(x+\Delta x,t))\approx T(x,t)\cos(\theta(x,t))$$
Now looking at vertical movement we see that:$$\Large\begin{align}
\text{mass}\times\text{acceleration}&=\text{Force}\\
&=T(x+\Delta x,t)\sin(\theta(x+\Delta x,t))\\
&\,\,\,\,-T(x,t)\sin(\theta(x,t))
\end{align}$$
Here, acceleration is approximately $\frac{\partial^2 u}{\partial^2 t}(x,t)$. To deal with the mass, we assume the string has a mass density function $\rho(x)$:$$\Huge \begin{align}\text{mass}&\approx\rho(x)\times\text{string length}\\
&\approx\rho(x)\sqrt{(\Delta x)^2+(\Delta u)^2}\\
&\approx\rho(x)\Delta x\sqrt{1+\left(\frac{\Delta u}{\Delta x}\right)^2}\\
&\approx\rho(x)\Delta x\sqrt{1+\left(\frac{\partial u}{\partial x}(x,t)\right)^2}
\end{align}$$
Again as we are considering an infinitesimal string segment, we can assume that $|\theta(x,t)|$ and $|\theta(x+\Delta x,t)|$ are also infinitesimal. In such case, we can use the small angle approximation:$$\Huge \sin(\theta(x,t))\approx\theta(x,t)\approx \tan(\theta(x,t))=\frac{\partial u}{\partial x}(x,t)$$Using this approximation:$$\Huge\begin{align} \text{mass}&\approx\rho(x)\Delta x\frac{\partial^2u}{\partial t^2}(x,t)\\
&\approx T(x,t)(\sin(\theta(x+\Delta x,t))-\sin(\theta(x,t)))\\
&\approx T(x,t)\left(\frac{\partial u}{\partial x}\left(x+\Delta x,t\right)-\frac{\partial u}{\partial x}(x,t)\right)\\
&\approx T(x,t)\frac{\partial^2u}{\partial x^2}(x,t)\Delta x
\end{align}$$That is to say, in the limiting case:$$\Huge \frac{\partial^2u}{\partial t^2}(x,t)=\frac{T(x,t)}{\rho(x)}\frac{\partial^2u}{\partial x^2}(x,t)$$This is known as the wave equation. Usually, we ignore where the PDE came from, and will only focus on the analysis of the PDE. This involves proving solutions exist, how many solutions exist and when, and finding unique solutions.

# Prerequisite information:

A set $U\subseteq\Re^n$ is open if for all $\underline x\in U,\exists\epsilon>0:B_\epsilon(\underline x)\subset U$ where $B_r(\underline x)=\{\underline y\in\Re^n:|\underline y-\underline x|<r\}$. A set $V\subseteq\Re^n$ is closed if its complement $\Re^n\setminus V$ is open.

A set $V\subseteq\Re^n$ is closed if and only if for every convergent sequence $(\underline x_n)\in V$ with $\underline x_n\to\underline x\in\Re^n$ we have that $\underline x\in V$. That is, the limit of every convergent sequence in $V$ belongs to $V$.

Let $\Omega\subseteq\Re^n$. A point $\underline x\in\Re^n$ is a limit point of $\Omega$ if $\forall\epsilon>0$ the open ball $B_\epsilon(\underline x)$ contains a point of $\Omega$ that is not $\underline x$. That is, $\Omega\cap(B_\epsilon(\underline x)\setminus\{\underline x\})\neq\emptyset$. The closure of $\Omega$ is then the set $\Omega$ together with its limit points. 

The boundary of $\Omega,\partial\Omega$ is then defined as $\partial\Omega=\bar\Omega\cap\overline{(\Re^n\setminus\Omega)}$.

PDEs are often defined on open and bounded sets with smooth boundary, that is the boundary can be locally parametrised by a continuously differentiable function.

Properties of the closure and boundary:
> The closure of a set is closed
> A set is closed if and only if it equals its closure (contains all its limit points)
> The closure of a set is the smallest closed set containing the set