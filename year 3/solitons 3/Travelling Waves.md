
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

The sine-Gordon equation is defined:$$\Huge u_{xx}-u_{tt}=\sin(u)$$Again we aim to find a travelling wave solution:$$\Huge f''-v^2f''=\sin(f)\implies(1-v^2)f''=\sin(f)$$Introducing $\gamma=\frac{1}{\sqrt{1-v^2}}$:$$\Huge f''=\gamma^2\sin(f)\implies_{\times f'}f''f'=\gamma^2\sin(f)f'$$we now notice that each side of the equation is simply a derivative:$$\Huge \implies(f')^2=A-2\gamma^2\cos(f)\implies f'=\pm\sqrt{A-2\gamma^2\cos(f)}$$Now we must impose boundary conditions. We require $f',f''\to0$ as $x\to\pm\infty$, which implies that we need $\sin(f)\to0$, that is $f\to n\pi$ as $x\to\pm\infty$. In fact we impose $f(\pm\infty)=2\pi n$. We must therefore have that the terms in the root tend to $0$. This imposes $A=2\gamma^2$, making our equation:$$\Huge f'=\pm\sqrt{2}\gamma\sqrt{1-\cos(f)}$$Dividing by the root and integrating wrt $f$:$$\Huge \int\frac{df}{\sqrt{1-\cos(f)}}=\pm\sqrt2\gamma(x-vt)$$The LHS integral becomes:$$\Huge \sqrt 2\log\left(\tan\left(\frac{f}{4}\right)\right)+\text{constant}=\pm\sqrt{2}\gamma(x-vt)$$Rearranging for $f$ gives:$$\Huge u(x,t)=f(x-vt)=4\arctan(e^{\pm\gamma(x-x_0-vt)})$$which is sometimes called the Kink (+) or the anti-Kink (-). At a fixed $t$, we can graph the Kink and anti-Kink:![[Travelling Waves 2025-10-26 08.21.09.excalidraw]]
Note that choosing a different branch of $\arctan$ shifts the solution by a multiple of $2\pi$. We get the following properties of this solution:
> The velocity of the Kink/anti-Kink can be:$$\Huge\begin{cases}v>0&\text{right-moving} \\
v=0&\text{static} \\
v<0&\text{left-moving}\end{cases}$$
>For a real solution, we require $\gamma^2\geq0\implies|v|\leq1=c$
>The Kink/anti-Kink is a localised lump centered at $x_0+vt$ with:$$\Huge\text{width}\sim\frac{1}{\gamma}=\sqrt{1-v^2}$$

So we see that faster Kinks\anti-Kinks are narrower, a phenomenon known as Lorentz contraction.

# Mechanical model for the sine-Gordon equation:

Consider a chain of infinitely many identical pendulums hanging from a wire that can be twisted. Each identical pendulum consists of a massless rod of length $L$ with a mass $M$ at the end. The pivot of the $n$th pendulum is at position $na$ along the line for $n\in\mathbb{Z}$ and $a$ the separation, and the configuration of the $n$th pendulum at time $t$ is encoded by $\theta_n(t)$:![[Travelling Waves 2025-10-26 08.29.36.excalidraw]]
The pendulums are subject to a gravitational force as well as a twisting force from neighboring pendulums. The equations of motion for this physical system are a coupled system of infinitely many ODEs indexed by $n$ of form:$$\large ML^2\ddot\theta_n(t)=-MgL\sin\theta_n(t)+\frac{k}{a}(\theta_{n+1}(t)-\theta_n(t))+\frac{k}{a}(\theta_{n-1}(t)-\theta_n(t))$$where the first term represents the net gravitational force, while the second and third terms represent the twisting forces exerted by neighboring pendulums. Here, $g$ is the gravitational constant and $k$ is an elastic constant that parametrises the strength of the twisting force.

We take the continuum limit of this infinite dimensional discrete system, in which the separation between pendulums becomes infinitesimally small, and the average mass density is kept fixed:$$\Huge a\to0,\,\,m=M/a=\text{constant}$$In this limit, the position $x=na$ of the $n$th pendulum effectively becomes a continuous variable, replacing the discrete index $n\in\mathbb{Z}$. Identifying $\theta_n(t)=\theta(x=na,t)$, the collection $\{\theta_n(t)\}_{n\in\mathbb{Z}}$ of angular coordinates is replaced by a single limit function $\theta(x,t)$ of two continuous variables $x,t$. By the definition of the derivative as a limit we have that:$$\Huge\begin{align*}
\frac{\theta_{n+1}(t)-\theta_n(t)}{a}&\rightarrow\theta'(x,t)\\
\frac{1}{a}\left(\frac{\theta_{n+1}(t)-\theta_n(t)}{a}-\frac{\theta_n(t)-\theta_{n-1}(t)}{a}\right)&\rightarrow\theta''(x,t)
\end{align*}$$
Dividing the equations by $ML^2=amL^2$ and taking the continuum limit gives the single equation of motion:$$\Huge\ddot\theta=-\frac{g}{L}\sin\theta+\frac{k}{mL^2}\theta''$$for the field $\theta(x,t)$. We can rescale $x,t$ to get rid of the constants, making the equation:$$\Huge \ddot\theta-\theta''=-\sin\theta$$which is exactly the sine-Gordon equation. We can use this mechanical model to gain some intuition about the configurations of the sine-Gordon field:
> The lowest energy state of the system is a configuration with all pendulums pointing downwards:$$\Huge \theta(x,t)=0\mod2\pi$$which is a configuration of stable equilibrium.
> By a continuous perturbation of the vacuum, we can obtain configurations that represent a "small wave" that satisfies the same BCs of the vacuum, $\theta\to0$ as $x\to\pm\infty$.
> There are configurations in which the chain of pendulums twist around the line. Say that they twist once in the direction of decreasing angles, so that $\theta$ decreases by $2\pi$ from $x\to-\infty$ to $x\to+\infty$. This describes a Kink or anti-Kink:![[Travelling Waves 2025-10-26 08.46.42.excalidraw]]
> The limiting values of the sine-Gordon field $\theta$ as $x\to\pm\infty$ are fixed. Changing them would require twisting infinitely many pendulums by a full $2\pi$, costing energy. If:$$\Huge\theta(+\infty,t)-\theta(-\infty,t)=2m\pi,\,\,m\neq0,\,\,m\in\mathbb{N}$$then the configuration of the system cannot be deformed continuously to the vacuum where all pendulums point downwards. That is, the Kink/anti-Kink cannot disperse into the vacuum.

