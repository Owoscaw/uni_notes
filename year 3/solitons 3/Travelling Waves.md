
# The [[Basic properties of Solitons#The KdV equation|KdV]] soliton:

Recall the KdV equation:$$\Huge u_t+6uu_x+u_{xxx}=0$$on $x\in\Re$ with boundary conditions $u,u_x,u_{xxx}\to0$ as $|x|\to\infty$. We define travelling waves as PDE solutions of the form $u(x,t)=f(x-vt)$, substituting a travelling wave solution into the KdV equation yields:$$\Huge -vf'+6ff'+f'''=0$$Boundary conditions on $u$ imply $f,f',f'''\to0$ as $x-vt\to\pm\infty$. Notice that the above is simply the derivative:$$\Huge\begin{align*}
(-vf+3f^2+f'')'&=0\\
\implies-vf+3f^2+f''&=\text{constant}
\end{align*}$$However boundary conditions force this constant to be $0$, that is:$$\Huge -vf+3f^2+f''=0$$we have now reduced the PDE into an ODE. We can then solve:$$\Huge\begin{align*}
\implies-vff'+3f^2f'+f''f'=0\\
\implies-\frac{1}{2}vf^2+f^3+\frac{1}{2}(f')^2=0
\end{align*}$$where we have noticed that this is a derivative of the bottom line, and that boundary conditions again imply the constant on the second line to be $0$. We have now reduced to a nonlinear first order ODE:$$\Huge (f')^2=f^2(v-2f)\implies f'=\pm f\sqrt{v-2f}$$which is separable:$$\Huge\begin{align*}
\implies\int\frac{df}{f\sqrt{v-2f}}&=\pm(x-vt)\\
f=\frac{1}{2}v\text{ sech}^2\theta\implies\int\frac{df}{f\sqrt{v-2f}}&=-\frac{2}{\sqrt{v}}\int d\theta\\
&=-\frac{2\theta}{\sqrt v}\\
\implies\theta&=\pm\frac{\sqrt v}{2}(x-x_0-vt)
\end{align*}$$where $x_0$ is the integration constant. On the first line, there is a slight abuse of notation, as the $\pm(x-vt)$ comes from the fact that we are actually performing the integral:$$\Huge \int\frac{df}{f\sqrt{v-2v}}=\pm\int df(x-vt)=\pm(x-vt)$$ Substituting our expression for $f$ back in gives:$$\Huge u(x,t)=f(x-vt)=\frac{v}{2}\text{ sech}^2\left(\frac{\sqrt v}{2}(x-x_0-vt)\right)$$Note that we could have chosen different boundary conditions such that when we were reducing our ODE, each constant derivative would not be forced to $0$. In such case, the solutions describe the KdV equation defined on a circle.

# The sine-Gordon equation:

The sine-Gordon equation is defined:$$\Huge u_{xx}-u_{tt}=\sin(u)$$Again we aim to find a travelling wave solution:$$\Huge f''-v^2f''=\sin(f)\implies(1-v^2)f''=\sin(f)$$Introducing $\gamma=\frac{1}{\sqrt{1-v^2}}$:$$\Huge f''=\gamma^2\sin(f)\implies_{\times f'}f''f'=\gamma^2\sin(f)f'$$we now notice that each side of the equation is simply a derivative:$$\Huge \implies(f')^2=A-2\gamma^2\cos(f)\implies f'=\pm\sqrt{A-2\gamma^2\cos(f)}$$Now we must impose boundary conditions. We require $f',f''\to0$ as $x\to\pm\infty$, which implies that we need $\sin(f)\to0$, that is $f\to n\pi$ as $x\to\pm\infty$. In fact we impose $f(\pm\infty)=2\pi n$. We must therefore have that the terms in the root tend to $0$. This imposes $A=2\gamma^2$, making our equation:$$\Huge f'=\pm\sqrt{2}\gamma\sqrt{1-\cos(f)}$$Dividing by the root and integrating wrt $f$:$$\Huge \int\frac{df}{\sqrt{1-\cos(f)}}=\pm\sqrt2\gamma(x-vt)$$The LHS integral becomes:$$\Huge \sqrt 2\log\left(\tan\left(\frac{f}{4}\right)\right)+\text{constant}=\pm\sqrt{2}\gamma(x-vt)$$Rearranging for $f$ gives:$$\Huge u(x,t)=f(x-vt)=4\arctan(e^{\pm\gamma(x-x_0-vt)})$$