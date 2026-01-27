
Our aim in this note is to analyse the possible solutions to the [[Inverse scattering method#The KdV-Schrodinger connection|eigenvalue problem]] $L\psi=\lambda\psi$, that is$$\Huge \left(\frac{d^2}{dx^2}+u(x)\right)\psi(x)=\lambda\psi(x)$$with $\psi(x)$ bounded for all $x$. Note that this slightly relaxes the requirement $\int_\Re|\psi|^2dx<\infty$, i.e. $\psi\in L^2(\Re)$. Note that the KdV time $t$ appears only as a parameter in $u(x,t)$ and stays fixed. The operator $L$ in the eigenvalue problem should then be viewed as a second order ordinary differential operator in $x$.

# Physical interpretation:

The equation$$\Huge i\frac{\partial }{\partial \tau}\Psi(x,\tau)=\left(-\frac{\partial^2}{\partial x^2}+V(x)\right)\Psi(x,\tau)$$is known as the time-dependent Schrodinger equation. This describes a particle of mass $1/2$ moving on a line in a potential $V(x)$ in quantum mechanics. The wavefunction $\Psi$ describes where the particle may be, $|\Psi(x,\tau)|^2dx$ is the probability to find the particle in $[x,x+dx]$ at time $\tau$.

To solve this, we separate variables$$\Huge \Psi(x,\tau)=\psi(x)\phi(\tau)$$to find that$$\Huge i\frac{\dot\phi}{\phi}=\frac{-\psi''+V\psi}{\psi}=\text{constant}=k^2$$Now we solve this for $\phi$ to get$$\Huge \dot\phi=-ik^2\phi\implies\phi(\tau)=e^{-ik^2\tau}$$while $\psi(x)$ solves the time independent Schrodinger equation$$\Huge \left(-\frac{d^2}{dx^2}+V(x)\right)\psi(x)=k^2\psi(x)$$which is the same as our differential operator with $u=-V,\lambda=-k^2$. In quantum mechanics, this equation describes a particle with energy $E=k^2=-\lambda$ moving in the potential $V(x)=-u(x)$.

With our connection to KdV in mind, we will consider potentials that tend to $0$ as $x\to\pm\infty$. In classical mechanics, a particle with total energy $E=T+V$ is localised, and bounces off the potential at the "turning points" $x_*$ where $V(x_*)=E$. In quantum mechanics, there is a nonzero chance to find the particle anywhere, and the particle can "tunnel" through potential barriers which are impenetrable in classical mechanics.

The scattering data will be encoded in the asymptotics of $\psi(x)$ as $x\to\pm\infty$. Since $V(x)\to0$ as $x\to\pm\infty$, the equation reduces to (in these regions)$$\Huge -\frac{d^2}{dx^2}\psi=k^2\psi$$which has two independent plane wave solutions $e^{\pm ikx}$. Therefore the general solution with eigenvalue $E=k^2$ has asymptotics$$\Huge\begin{align*}
\psi(x)&\approx A(k)e^{ikx}+B(k)e^{-ikx},\,\,x\to-\infty\\
\psi(x)&\approx C(k)e^{ikx}+D(k)e^{-ikx},\,\,x\to+\infty
\end{align*}$$and, restoring $\tau$-dependence$$\Huge\begin{align*}
\Psi(x,\tau)&\approx A(k)e^{ikx-ik^2\tau}+B(k)e^{-ikx-ik^2\tau},\,\,x\to-\infty\\
\Psi(x,\tau)&\approx C(k)e^{ikx-ik^2\tau}+D(k)e^{-ikx-ik^2\tau},\,\,x\to+\infty
\end{align*}$$showing that for real $k>0$, the $A,C$ terms correspond to right-moving waves, while the $B,D$ terms correspond to left-moving waves. Taking $k>0$ WLOG, our solution will be bounded for any $A,B,C,D$ if $E=k^2>0$.

We will see that solving the time independent Schrodinger equation in the region where $V(x)\neq0$ interpolates between the two asymptotic regions and imposes two relations on $A,B,C,D$ leaving two undetermined coefficients. To fix these remaining coefficients, for $k^2>0$ we impose$$\Huge A(k)=1,\,\,D(k)=0$$and write$$\Huge\begin{align*}
B(k)&=R(k)\text{ (reflection coefficient)}\\
C(k)&=T(k)\text{ (transmission coefficient)}
\end{align*}$$so that the resulting scattering solution has asymptotics$$\Huge\begin{align*}
\psi(x)&\approx e^{ikx}+R(k)e^{-ikx},&x\to-\infty\\
\psi(x)&\approx T(k)e^{ikx}&x\to+\infty
\end{align*}$$and represents a unit flux of incoming particles from the left, partially reflected from the potential and partially transmitted through it. It can be shown that$$\Huge |R(k)|^2+|T(k)|^2=1$$meaning that a particle is either reflected or transmitted with probability $1$.

## The Wronskian:
The above result is proven using a tool known as the Wronskian. For two functions $f,g$ their Wronskian is the function$$\Huge W[f,g](x)=f'(x)g(x)-f(x)g'(x)$$which has the properties:
> If $f,g$ are linearly dependent then $W[f,g]=0$ identically.
> The converse, $W[f,g]=0$ implies linear dependence is more tricky, however is easily proven if:
> > $W[f,g](x)=0$ on some interval
> > either function is nonzero on that interval
> then $f,g$ are linearly dependent on that interval

Returning to our equation$$\Huge \left(-\frac{d^2}{dx^2}+V(x)\right)\psi(x)=E\psi(x)=k^2\psi(x)$$So far we have considered $k^2=E>0$. For $k^2<0$ we let $k=i\mu$ with $\mu>0$ real, so $E=-\mu^2$. Then the asymptotics of the general solution become$$\Huge\begin{align*}
\psi(x)&\approx a(\mu)e^{-\mu x}+b(\mu)e^{\mu x},&x\to-\infty\\
\psi(x)&\approx c(\mu)e^{-\mu x}+d(\mu)e^{\mu x},&x\to+\infty
\end{align*}$$and it follows that$$\Huge \psi\text{ bounded}\iff a(\mu)=d(\mu)=0$$In such cases, $\psi$ is not only bounded, but it also tends to zero exponentially fast at $\pm\infty$ and therefore satisfies $\int_\Re|\psi|^2dx<\infty$.

Note that there might be no values for $\mu$ where this happens, but if it does then $\psi$ is called a bound state solution. Given a potential $V(x)$ tending to zero at $\pm\infty$, bound state solutions only exist for a finite set of $\mu$ values:$$\Huge \{\mu_k\}_{k=1}^N=\{\mu_1,\mu_2,\dots,\mu_N\},\,\,\mu_1<\mu_2<\dots<\mu_N$$
## Summary:
Bounded solutions to $$\Huge \left(-\frac{d^2}{dx^2}+V(x)\right)\psi(x)=E\psi(x)=k^2\psi(x)$$come in two flavors:
> $E=k^2=-\lambda\in(0,+\infty)$, the continuous spectrum leading to scattering solutions which are bounded, and have oscillatory asymptotics.
> $E=-\mu^2=-\lambda\in\{-\mu_1^2,\dots,-\mu_N^2\}$, the discrete spectrum leading to bound state solutions which are square integrable, and have damped asymptotics.

# Examples:

## Zero potential: $V(x)=0$:
We must solve $-\frac{d^2}{dx^2}\psi=k^2\psi$ for all $x\in\Re$. There are two cases to consider:
> $k^2>0$: The general solution, valid for all $x$, is$$\Huge\psi(x)=Ae^{ikx}+Be^{-ikx}$$which describes a left or right moving wave upon restoring $\tau$-dependence. This gives hounded solutions for all real $k$. Comparing with the general asymptotics, we see $C(k)=A(k)$ and $D(k)=B(k)$. Imposing the conditions $A(k)=0,D(k)=0$ we get teh scattering solution$$\Huge\psi(x)=e^{ikx}$$from which it follows$$\Huge R(k)=0,\,\,T(k)=1$$which makes sense. This describes a particle incident from the left being transmitted through to the right with probability $1$, as one would expect for zero potential.
> $k^2=-\mu^2<0$: The general solution becomes$$\Huge \psi(x)=ae^{-\mu x}+be^{\mu x}$$which is only bounded when $a=b=0$, so there are no bound state solutions.

For $u=0$, the problem $L(u)\psi=\lambda\psi$ has a scattering solution for all real $\lambda<0$ and no solutions for $\lambda>0$.

## Delta function potential: $V(x)=a\delta(x)$:
Here, $a$ is a real constant and $\delta(x)$ is the Dirac delta function. Recall that $\delta(x)$ can be viewed as the limit of a sequence of unit-area functions that become increasingly concentrated at the origin so that for any continuous test function $f(x)$ we have$$\Huge \int_\Re\delta(x)f(x)dx=f(0)$$We seek a single solution $\psi(x)$ solving the equation in both regions before and after the delta spike, and is also consistent with the potential at $x=0$.
> $k^2>0$: In both regions, $V(x)=0$ and so $\psi$ satisfies our above example. Here, the solutions are$$\Huge\psi(x)=\begin{cases}A(k)e^{ikx}+B(k)e^{-ikx}&x<0 \\
C(k)e^{ikx}+D(k)e^{-ikx}&x>0\end{cases}$$However we must match the two parts of the solution at $x=0$, which will determine the relationship between $A,B,C,D$. 
> To find these conditions, we integrate the time-independent Schrodinger equation$$\Huge -\psi''(x)+a\delta(x)\psi(x)=k^2\psi(x)$$in an infinitesimal neighbourhood $[-\epsilon,+\epsilon]$ of $x=0$:$$\Huge\begin{align*}
\int_{-\epsilon}^\epsilon-\psi''(x)+a\delta(x)\psi(x)\,dx&=k^2\int_{-\epsilon}^\epsilon\psi(x)\,dx\\
\implies[-\psi'(x)]_{-\epsilon}^\epsilon+a\psi(0)&=k^2\int_{-\epsilon}^\epsilon\psi(x)\,dx
\end{align*}$$
> Provided that $\psi$ is bounded, the RHS of this equation tends to $0$ as $\epsilon\to0$. Taking this limit implies that$$\Huge[\psi'(x)]_{0^-}^{0^+}=a\psi(0)$$Here, we implicitly assume that $\psi(x)$ is continuous at $x=0$. It is not hard to relax this assumption to deduce a modified version of our condition that can be used to deduce if $\psi(x)$ is continuous$$\Huge [\psi(x)]_{0^-}^{0^+}=0$$
> Applying our matching conditions, we have$$\Huge\begin{align*}
A+B&=C+D\\
ik(C-D)-ik(A-B)&=a(A+B)=a(C+D)
\end{align*}$$which in turn implies$$\Huge\begin{align*}
A+B&=C+D\\
A-B&=\left(1-\frac{a}{ik}\right)C-\left(1-\frac{a}{ik}\right)D
\end{align*}$$Adding and subtracting gives$$\Huge\begin{align*}
A&=\left(1-\frac{a}{2ik}\right)C-\frac{a}{2ik}D\\
B&=\frac{a}{ik}C+\left(1+\frac{a}{2ik}\right)D
\end{align*}$$
> Substituting this into our general solution gives a solution with two undetermined constants as expected. To get the scattering solution, we set $D=0$ and divide through so that $A=1$:$$\Huge\psi(x)=\begin{cases}e^{ikx}+\frac{a}{2ik-a}e^{-ikx}&x<0 \\
\frac{2ik}{2ik-a}e^{ikx}&x>0\end{cases}$$from which we read the reflection and transmission coefficients:$$\Huge R(k)=\frac{a}{2ik-a},\,\,T(k)=\frac{2ik}{2ik-a}$$
> $k^2=-\mu^2<0$: Setting $k=i\mu$ in our general solution and our relationships between $A,B,C,D$ with $\mu>0$ we obtain$$\Huge\psi(x)=\begin{cases}A(i\mu)e^{-\mu x}+B(i\mu)e^{\mu x}&x<0 \\
C(i\mu)e^{-\mu x}+D(i\mu)e^{\mu x} & x>0\end{cases}$$Given that we chose $\mu>0$, this is bounded as $x\to\pm\infty$ if and only if$$\Huge A(i\mu)=D(i\mu)=0$$which fixes our relation$$\Huge\begin{align*}
0&=\left(1+\frac{a}{2\mu}\right)C\\
B&=-\frac{a}{\mu}C
\end{align*}$$which gives two further options:
> > $A=B=C=D=0$, which is trivial.
> > $\mu=-\frac{a}{2}$ with $B=C$. Given that we took $\mu>0$, this option means that there is a bounded solution with $k^2<0$ only for $a<0$. The bound state solution is then$$\Huge\psi(x)=e^{\frac{a}{2}|x|},\,\,k^2=-\frac{a^2}{4}$$
> Note that we can obtain bound state solutions by an alternative method. First, we observe $D(k)=0$ is a requirement for the general solution to be bounded. Hence we can directly substitute $k=i\mu$ directly into our scattering solution$$\Huge\psi(x)=\begin{cases}e^{-\mu x}+\frac{a}{-2\mu-a}e^{\mu x}&x<0 \\
\frac{-2\mu}{-2\mu-a}e^{-\mu x}&x>0\end{cases}$$which looks unbounded due to the $e^{-\mu x}$ term. The trick is to divide through by $T(i\mu)=\frac{2\mu}{2\mu+a}$, which gives$$\Huge\psi(x)=\begin{cases}\frac{2\mu+a}{2\mu}e^{-\mu x}-\frac{a}{2\mu}e^{\mu x}&x<0 \\
e^{-\mu x}&x>0\end{cases}$$which is bounded as $x\to-\infty$ if and only if $\mu=-\frac{a}{2}$, in which we can recover our bound state solution we just found.

## Summary:
For $V(x)=-u(x)=a\delta(x)$, the eigenvalue problem $L(u)\psi=\lambda\psi$ has a scattering solution for all real $\lambda<0$, and either no solutions for $\lambda>0$ if $a\geq0$ or one solution for $\lambda>0$ if $a<0$.
> For all $k^2>0$, a scattering solution$$\Huge\psi(x)=\begin{cases}e^{ikx}+R(k)e^{-ikx}&x<0 \\
T(k)e^{ikx}&x>0\end{cases}$$exists with reflection and transmission coefficients$$\Huge R(k)=\frac{a}{2ik-a},\,\,T(k)=\frac{2ik}{2ik-a}$$
> For isolated $k^2=-\mu^2<0$, a bound state solution$$\Huge\psi(x)=\begin{cases}\frac{R(i\mu)}{T(i\mu)}e^{\mu x}&x<0 \\
e^{-\mu x}&x>0\end{cases}$$exists if $\mu=-a/2$ such that$$\Huge \frac{1}{T(i\mu)}=0$$

For potentials $V(x)$ that tend to zero as $x\to\pm\infty$, bound state solutions can be obtained from scattering solutions by:
> Dividing through by $T(k)$
> Setting $k=i\mu$, a pole of $T(k)$ on the positive imaginary axis

These conditions determine the discrete spectrum of $-\frac{d^2}{dx^2}+V(x)$.