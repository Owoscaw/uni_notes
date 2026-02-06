
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

# Reflectionless potentials:

Let us return to the initial field configurations $u(x,0)=a\text{sech}^2(x)$ that we tried for KdV previously. We saw interesting field evolutions when $a=n(n+1)$ for a positive integer $n$. It is natural to wonder if this behaviour is apparent in the scattering problem. 

The relevant potential is:$$\Huge V(x)=-a\text{ sech}^2(x)$$The relevant time independent Schrodinger equation to solve is$$\Huge-\psi''(x)-a\text{ sech}^2(x)\psi(x)=k^2\psi(x)$$, where we look for bounded solutions. Substituting in $y=\tanh(x)$ so that $$\Huge \frac{d}{dx}=\text{sech}^2(x)\frac{d}{dy}=(1-y^2)\frac{d}{dy}$$makes the equation:$$\Huge \frac{d}{dy}\left((1-y^2)\frac{d\psi}{dy}\right)+\left(\frac{k^2}{1-y^2}+a\right)\psi=0$$Putting $k^2=-m^2,a=n(n+1)$ gives us the associated Legendre equation:$$\Huge \frac{d}{dy}\left((1-y^2)\frac{d\psi}{dy}\right)+\left(n(n+1)-\frac{m^2}{1-y^2}\right)\psi=0$$This is a well studied equation, and has solutions known in terms of special functions:
> If $n\in\mathbb{Z}_{\geq0}$ and $m=0$, then this becomes the Legendre equation and has a bounded solution for $y\in[-1,1]$$$\Huge \psi=P_n(y)=\frac{1}{n!2^n}\frac{d^n}{dy^n}(y^2-1)^n$$, the $n$th Legendre polynomial of the first kind. In general, $P_j(-y)=(-1)^jP_j(y)$ and $P_j(1)=1$. Since $y=\pm1$ corresponds to the asymptotics $x=\pm\infty$, this means we have bounded solutions to the Schrodinger equation. Note that these however are not bound states as $\psi\not\rightarrow0$ at $x\to\pm\infty$.
> If $n\in\mathbb{Z}_{\geq0}$, bounded solutions only exist for $m=\{0,\dots,n\}$. These are given by$$\Huge P^m_n(y)=(-1)^m(1-y^2)^{m/2}\frac{d^m}{dy^m}P_n(y)$$, the associated Legendre polynomials of the first kind. 
> Even when $m,n$ are not integers, solutions can be written explicitly using certain special functions. We have that$$\Huge P_n^m(y)=\frac{1}{\Gamma(1-m)}\left(\frac{1+y}{1-y}\right)^{m/2}\,_2F_1\left(-n,n+1;1-m;\frac{1-y}{2}\right)$$solves the Schrodinger equation and reduces to the above equation for $n\in\mathbb{Z}_{\geq0}$ and $m\in\{0,\dots,n\}$. Here, $$\Huge\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}dt$$is Euler's Gamma function, and $_2F_1$ is the hypergeometric function. This has Taylor expansion$$\Huge _2F_1(a,b;c;z)=\frac{\Gamma(c)}{\Gamma(a)\Gamma(b)}\sum_{k=0}^\infty\frac{\Gamma(k+1)\Gamma(k+b)}{\Gamma(k+c)}\frac{z^k}{k!}$$for $|z|<1$, and is defined by analytic continuation elsewhere.
> Therefore, up to normalisation, a bounded solution to the relevant Schrodinger equation is$$\Huge \psi(x)=P^m_n(y=\tanh(x))$$with:$$\Huge m=ik,\,\,n=\frac{\sqrt{1+4a}}{2}-\frac{1}{2}$$

Note that we chose roots that give scattering solutions with particles incident from the left. Observe also that $n$ is real if $a\geq-1/4$ and $n\geq0$ if $a\geq0$. Let us now analyse the spectrum of solutions:
> $k^2>0$, the continuous spectrum:
> > As $x\to+\infty$, we have that $y=\tanh(x)\to1^-$ and so$$\Huge _2F_1\left(\dots;\frac{1-y}{2}\right)\to\,_2F_1(\dots;0)=1;\,\,\frac{1+y}{1-y}\approx e^{2x}$$, giving the asymptotic behaviour$$\Huge \psi\approx\frac{1}{\Gamma(1-ik)}e^{ikx}$$as $x\to+\infty$.
> > As $x\to-\infty$, we have that $y=\tanh(x)\to-1^+$ and so:$$\frac{1}{\Gamma(1-m)}\,_2F_1\left(-n,n+1;1-m;\frac{1-y}{2}\right)\approx\frac{\Gamma(-m)}{\Gamma(1-m+n)\Gamma(-m-n)}+\frac{\Gamma(m)}{\Gamma(-n)\Gamma(n+1)}e^{-2mx}$$This asymptotic is proven using the properties of the hypergeometric function. Therefore$$\Huge\psi\approx\frac{\Gamma(-ik)}{\Gamma(1-ik+n)\Gamma(-ik-n)}e^{ikx}+\frac{\Gamma(ik)}{\Gamma(-n)\Gamma(n+1)}e^{-ikx}$$as $x\to-\infty$
>>Normalising this scattering solution so that the coefficient of $e^{ikx}$ at $-\infty$ is $1$, we can read off the values of $R(k)$ and $T(k)$:$$\Huge\begin{align*}
R(k)&=\frac{\Gamma(ik)\Gamma(1-ik+n)\Gamma(-ik-n)}{\Gamma(-ik)\Gamma(1+n)\Gamma(-n)}\\
&=-\frac{\sin(\pi n)}{\pi}\frac{\Gamma(ik)\Gamma(1-ik+n)\Gamma(-ik-n)}{\Gamma(-ik)}\\
T(k)&=\frac{\Gamma(1-ik+n)\Gamma(-ik-n)}{\Gamma(1-ik)\Gamma(-ik)}
\end{align*}$$Note that the $\sin(\pi n)$ factor in $R(k)$ means that it vanishes for all $k$ if $n$ is an integer. The corresponding potentials$$\Huge V(x)=-n(n+1)\text{sech}^2(x)$$with $n\in\mathbb{Z}_{\geq0}$ are called reflectionless. That is, no particles are reflected for any value of $k$. 
>$k^2<0$, the discrete spectrum. To find this spectrum, we set $k=i\mu$ with $\mu>0$, and divide the scattering solution through by $T(i\mu)$ to find a possible eigenfunction:$$\Huge \psi(x)\approx\begin{cases}\frac{1}{T(i\mu)}e^{-\mu x}+\frac{R(i\mu)}{T(i\mu)}e^{\mu x} & x\to-\infty \\
e^{i\mu x} & x\to+\infty\end{cases}$$This is automatically bounded as $x\to+\infty$ and will be bounded at $x\to-\infty$ if and only if $\mu\geq0$ is such that $1/T(i\mu)=0$. This requires:$$\Huge\frac{1}{T(i\mu)}=\frac{\Gamma(1+\mu)\Gamma(\mu)}{\Gamma(1+\mu+n)\Gamma(\mu-n)}=0$$Given that $\mu$ must be a positive real number and that $\gamma(z)$ has no zeros, there are two options:
> >$1+\mu+n=-j$ with $j\in\mathbb{Z}_{\geq0}$
> >$\mu-n=-h$ with $h\in\mathbb{Z}_{\geq0}$. 
> If $n\notin\Re$ then there are no real solutions for $\mu$. If $n\in\Re$ then we can take $n\geq-1/2$ WLOG since the first statement is equivalent to the second whenever $n\mapsto-1-n$.
> Then the first statement never holds, while solutions for positive $\mu$ do exists for the second statement, provided $n\geq0$:$$\Huge \mu=n,n-1,\dots ,n-\lfloor n\rfloor$$Therefore the total number of bound states is $\lceil n\rceil$.

## Summary:
For our potential $V(x)=-a\text{ sech}^2(x)=-n(n+1)\text{sech}^2(x)$, we have:![[Scattering theory 2026-02-06 20.19.15.excalidraw]]
