# Initial value problems:

So far, we saw a range of methods to construct particular solutions to [[Basic properties of Solitons#Soliton properties|integrable PDEs]]. We now aim to find general solutions to these PDEs. To elaborate, we want to solve the following Initial Value Problem (IVP):

Given a wave equation and initial data at an initial time $t=0$, find $u(x,t)$ at all later times $t>0$.

For there to be a unique solution, the initial data must be sufficient:
> For first order (in time) PDEs, we must specify $u(x,0)$
> For second order PDEs, we must specify $u(x,0),u_t(x,0)$

Given this information, it is not possible to construct $u(x,t)$ for $t>0$ analytically unless the initial condition happens to be a snapshot of one of the special solutions we saw previously:
> $u(x,0)=2\text{sech}^2(x)$ is a snapshot of a one-soliton at $t=0$, so we assume $u(x,t)=2\text{sech}^2(x-4t)$, which describes a single soliton moving to the right with velocity $v=4$.
> $u(x,0)=2.001\text{sech}^2(x)$ describes $2$ right-moving solitons and some noise that disperses to the left.
> $u(x,0)=6\text{sech}^2(x)$ describes a pure $2$-soliton solution.

Inverse scattering will allow us to understand these different situations and give us a more complete understanding on what is formed given some initial data. We must first look at a simpler setting, linear wave equations.

# Linear IVPs:

For a linear wave equation, the general solution is just a linear transformation of the initial data. Take for example:
> The heat equation, $u_t=u_{xx}$ for $x\in\Re,t>0$. Given initial data $u(x,0)=u_0(x)$, the general solution becomes:$$\Huge u(x,t)=\int_\Re\frac{1}{\sqrt{4\pi t}}e^{-(x-x')^2/(4t)}u_0(x')dx'$$which is simply a linear transformation of $u_0(x)$ (and is also a [[Green's method#General greens' function|Green's function]] solution).
> The Klein-Gordon equation, $u_{tt}-u_{xx}+m^2u=0$ for $x\in\Re,t>0$. This is second order in time, so we specify $u(x,0)=\alpha(x),u_t(x,0)=\beta(x)$. It turns out that this is a well-posed IVP and can be solved using a [[Fourier transform]] wrt $x$. Given $u(x,t)$, we set:$$\Huge\begin{align*}
\tilde u(k,t)&=\int_\Re u(x,t)e^{-ikx}dx\\
u(x,t)&=\frac{1}{2\pi}\int_\Re\tilde u(k,t)e^{ikx}dk
\end{align*}$$where the first equation defines the Fourier transform $\tilde u$ of $u$ wrt $x$, and the second acts as the inverse FT. We then work with $\tilde u(k,t)$ instead of $u$ as the wave equation becomes:$$\Huge\tilde u_{tt}+(k^2+m^2)\tilde u=0$$which is actually an ODE in $t$ for given $k$. The general solution of which is:$$\Huge\begin{align*}
\tilde u(k,t)&=A(k)e^{i\omega t}+B(k)e^{-i\omega t}\\
\omega&=\omega (k)=\sqrt{k^2+m^2}
\end{align*}$$The integration constants $A,B$ are found by matching initial data at $t=0$:$$\Huge\begin{align*}
\tilde\alpha(k)&=\tilde u(k,0)=A(k)+B(k)\\
\tilde\beta(k)&=\tilde u_t(k,0)=i\omega(A(k)-B(k))
\end{align*}$$Solving for $A,B$ gives us our FT field $\tilde u(k,t)$:$$\Huge\begin{align*}
\tilde u(k,t)&=\frac{1}{2}\left(\tilde\alpha(k)+\frac{\tilde\beta(k)}{i\omega}\right)e^{i\omega t}+\frac{1}{2}\left(\tilde\alpha(k)-\frac{\tilde\beta(k)}{i\omega}\right)e^{-i\omega t}\\
&=\tilde\alpha(k)\cos(\omega t)+\frac{1}{\omega}\tilde\beta(k)\sin(\omega t)
\end{align*}$$and we finally get our solution by applying the inverse FT:$$\large\begin{align*}
u(x,t)&=\frac{1}{2\pi}\int_\Re\left(\tilde\alpha(k)\cos(\omega t)+\frac{1}{\omega}\tilde\beta(k)\sin(\omega t)\right)e^{ikx}dk\\
&=\frac{1}{2\pi}\iint_{\Re^2}\left(u(x',0)\cos(\omega t)+\frac{1}{\omega}u_t(x',0)\sin(\omega t)\right)e^{ik(x-x')}dk\,dx'
\end{align*}$$with $\omega=\omega(k)=\sqrt{k^2+m^2}$. Again this is a linear function of the initial data $u(x,0)$ and $u_t(x,0)$.

The key feature from this is that the Fourier transformed data $\tilde u(k,t)$ for each value of $k$ evolves separately and in a simple way according to the Fourier transformed wave equation:![[Inverse scattering method 2026-01-15 19.44.04.excalidraw]]