
Many potentials in real life are not simple, so it is important to have approximate methods for finding the [[QM systems for general potentials|energy spectrum/wave function]]. 

# Constant potential:

We use the trivial constant potential and "build" on it to gain insight into less trivial potentials:![[The WKB approximation 2026-02-20 23.17.39.excalidraw]]The wave function for this is:$$\Huge\Psi_{\pm}=A_{\pm}e^{\pm ikx},\,\,k=\sqrt{2m(E-V)}$$So the wave function is oscillatory with wavelength $\lambda=2\pi/k$. 

Taking $E<V$ we will get exponential decay in either direction the particle can go. The associated wavefunction is then:$$\Huge\Psi_\pm(x)=B_\pm e^{\pm\kappa x},\,\,\kappa=\sqrt{2m(V-E)}$$The particle essentially becomes localised in $[-1/\kappa,1/\kappa]$.

# "Slow" potentials:

We assume $E>V(x)$ for all $x$ and that $V(x)$ varies in space slowly in comparison with $\lambda$. That is, $V(x)$ varies in such a way that it remains almost constant over a region containing multiple wavelengths. Here we expect that $\Psi$ is similar to the first case, however with amplitude $A$ and wavelength $\lambda$ functions of $x$ that are slowly varying.

Assuming $E<V(x)$ with slowly varying $V$ compared to $1/\kappa$, we see that $\Psi$ will have the same form as the constant case however with $A,\kappa$ slowly varying functions of $x$.

Let us make this intuition more quantitative:
> $E>V(x)$, the Schrodinger equation becomes:$$\Huge\begin{align*}
-\frac{1}{2m}\frac{d^2\Psi}{dx^2}+(V(x)-E)\Psi(x)=0\\
\iff \frac{d\Psi}{dx^2}&=-2m(E-V(x))\Psi\\
&=p^2(x)\Psi
\end{align*}$$
>We assume the form of $\Psi$ to be:$$\Huge\begin{align*}
\Psi(x)&=A(x)e^{ip(x)}\\
\implies A''(x)+2iA'(x)p'(x)+iA(x)p''(x)&=A(x)(p'(x))^2\\
&=-p^2(x)A(x)
\end{align*}$$Looking at the real part of this equation we find$$\Huge A''-(p')^2A=-p^2A\implies A''(x)=A(x)((p')^2-p^2)$$and for the imaginary part:$$\Huge\begin{align*}
2A'p'+Ap''&=0\\
\implies(A^2p)'&=\\
\implies A^2p'&=\eta^2=\text{constant}\\
\implies A(x)&=\frac{\eta}{\sqrt{|p'(x)|}}
\end{align*}$$
>The real equation cannot be solved in general, but if we assume $A''/A<<((p')^2-p^2)$ we can approximate$$\Huge\begin{align*}
(p'(x))^2&=p^2(x)\\
\implies p'&=\frac{dp}{dx}=\pm p(x)\\
\implies p(x)&=\pm\int_\alpha^xp(y)dy
\end{align*}$$for some constant $\alpha$. This constant is arbitrary, so we choose $\alpha=0$ for simplicity.
> The wave function then becomes$$\Huge\Psi_{I,\pm}(x)\approx\frac{\eta_\pm}{\sqrt{p(x)}}e^{\pm i\int_0^xp(y)dy},\,\,p(x)=\sqrt{2m(E-V(x))}$$, and general solutions are given by linear combinations of $\Psi_{I,+},\Psi_{I,-}$.

Note that:
> If $V=\text{constant}$ we recover the plane wave solution $e^{\pm ip(x-\alpha)}$
> $|\psi_{I,\pm}|^2=\frac{\eta^2}{p(x)}$, the probability to find a particle in $x\pm dx$ is inverse proportional to its velocity.

Let us look at the "bump" square well potential:
>![[The WKB approximation 2026-02-20 23.43.24.excalidraw]]In regions $I,III$ we simply have $\Psi_I=\Psi_{III}=0$ as there is infinite potential.
>In region $II$ we assume $E>V(x)$ and that $f(x)$ is slowly varying. Therefore our wave function is simply a linear combination of the wave function we derived above:$$\Huge\begin{align*}
\Psi(x)&=\frac{1}{\sqrt{p(x)}}(\eta_+e^{ip(x)}+\eta_-e^{-ip(x)})\\
&=\frac{1}{\sqrt{p(x)}}(\eta_1\cos(p(x))+\eta_2\sin(p(x)))
\end{align*}$$
> We now impose the boundary conditions:$$\Huge\begin{align*}
\Psi_{II}(0)=\Psi_{I}(0)&=0\implies\eta_1=0\\
\Psi_{II}(a)=\Psi_{III}(0)&=0\implies\sin(p(a))=0\\
\implies p(a)\int_0^ap(y)dy&=n\pi
\end{align*}$$Hence we see that energy is quantised, as$$\Huge\begin{align*}
\int_0^ap(x)dx&=\int_0^a\sqrt{2m(E-V(x))}dx\\
&=F_n(E)=n\pi\\
\implies E&=E(n)
\end{align*}$$, so we recover the generality of [[QM systems for general potentials#Bounded propagation|bounded propagation]] giving quantised energy.
> Looking at the case where $E<V(x)$ in region $II$, we follow a similar analysis to find:$$\Huge\Psi_{II,\pm}(x)\approx\frac{\xi_\pm}{\sqrt{q(x)}}e^{\pm\int_0^xq(y)dy},\,\,q(y)=\sqrt{2m(V(x)-E)}$$

Let us look at a particle scattering off of a "bumpy step" potential:
> ![[The WKB approximation 2026-02-20 23.53.57.excalidraw]]
> For $x<0$ we have $E>V=0$ and so we have$$\Huge\Psi_I(x)=Ae^{ikx}+Be^{-ikx},\,\,k=\sqrt{2mE}$$, representing the incoming and reflected wave.
> For $x>a$ we have the same situation:$$\Huge \Psi_{III}(x)=Qe^{ikx}$$
> For $0\leq x\leq a$ we use the WKB approximation and write:$$\Huge \Psi_{II}(x)\approx\frac{\xi_1}{\sqrt{q(x)}}e^{\int_0^xq(y)dy}+\frac{\xi_2}{\sqrt{q(x)}}e^{-\int_0^xq(y)dy}$$That is, we get a superposition of an exponentially increasing and exponentially decreasing terms. Note that if $a\to\infty$ we would set $\xi_1=0$ as the exponentially decreasing term would dominate. The important term is therefore the decreasing term. We would expect the qualitative shape:![[The WKB approximation 2026-02-27 02.08.06.excalidraw]]
> We can find the transmission coefficient $T=|Q|^2/|A|^2$, showing how much of the incoming wave is transmitted through the potential. We can find:$$\Huge\begin{align*}
T&=\frac{|\Psi_\text{WKB}(a)|^2}{|\Psi_\text{WKB}(0)|^2}\sim e^{-2\int_0^a q(y)dy}\\
\implies T&\sim e^{-2\gamma},\,\,\gamma=\int_0^aq(y)dy
\end{align*}$$This is essentially the same method for finding the transmission coefficient, measuring the probability of finding the particle at the start and the end of potential and taking their ratio. This gives the probability for a particle to tunnel through the potential barrier.

# Sloped potentials:

We have so far been considering "vertical" walls in our potentials between regions. Here, $V(x)$ jumps at some number of points $x_1^*,x_2^*,\dots$ to define the regions in which we approximate. 
![[The WKB approximation 2026-02-28 23.39.05.excalidraw]]
In each region, we can write the approximate WKB wave function:$$\Huge \begin{align*}
\Psi_{\text{WKB I}}(x)&=\frac{\eta_1}{\sqrt{p(x)}}\sin\left(\int_0^x p(y)dy\right)+\frac{\eta_2}{\sqrt{p(x)}}\cos\left(\int_0^xp(y)dy\right)\\
\Psi_{\text{WBK II}}(x)&=\frac{\xi_+}{\sqrt{q(x)}}e^{\int_0^xq(y)dy}+\frac{\xi_-}{\sqrt{q(x)}}e^{-\int_0^xq(y)dy}\\
\Psi_{\text{WBK III}}(x)&\sim\Psi_\text{WBK II}(x)\\
p(x)&=\sqrt{2m(E-V(x))}=iq(y)=i\sqrt{2m(V(x)-E)}
\end{align*}$$
At the jump points $x=x_1^*,x_2^*$ we see that the momentum becomes:
> $x=x_1^*$ we approach from the left and so:$$\Huge p(x=x_1^*-\epsilon)=\sqrt{2m(V_1^{-}-E)}\neq0$$
> $x=x_2^*$ we approach from the right and so:$$\Huge q(x=x_2^*+\epsilon)=\sqrt{2m(V_2^{+}-E)}\neq0$$

We have valid momentum for all $x$ and so $\Psi$ should be well defined for this scenario. However if we allow for sloped walls in this smooth $V(x)$ we see:![[The WKB approximation 2026-02-28 23.45.58.excalidraw]]Here, momentum for both turning points becomes zero. This means that $\Psi$ is not well defined as $\Psi\sim1/\sqrt{q(x)},1/\sqrt{p(x)}$ will tend to infinity at these points. These points are where the particle becomes classically forbidden. 

The idea to fix this is to "zoom out" the problematic region around $x=x^*$ and approximate with a linear potential:$$\Huge V(x^*+\epsilon)=V(x^*)+V'(x^*)\epsilon+\mathcal{O}(\epsilon^2)$$We keep these terms and solve the Schrodinger equation with this linear potential. Solutions in this case are known as the Airy functions $A_i(x),B_i(x)$, two solutions that exhibit the behaviour:![[The WKB approximation 2026-02-28 23.57.03.excalidraw]]We use these functions to connect $\Psi_\text{WKB I}$ to $\Psi_\text{WKB II}$:![[The WKB approximation 2026-03-01 00.01.40.excalidraw]]Hence we have the unfixed constants $\eta_1,\eta_2,A_i,B_i,\xi_-$ and only four gluing conditions from the continuity of $\Psi,\Psi'$ at $x_1^*\pm\epsilon$. All but one constant is fixed, which we introduce to define our improved WKB approximation at the left turning point, moving inwards:$$\Huge\Psi_\text{WKBI}^\text{(L)}(x)=\begin{cases}\frac{a}{\sqrt{q(x)}}\exp(-\int_x^{x_1^*}q(y)dy) & x<<x_1^* \\
\sqrt{\frac{4\pi}{\alpha}}aA_i(\alpha x) & x\approx x_1^* \\
\frac{2a}{\sqrt{p(x)}}\sin(\int_{x_1^*}^xp(y)dy+\pi/4) & x>>x_1^*\end{cases}$$Where $\alpha=(2mV'(x_1^*))^{1/3}$ and $\Psi$ is smooth with one unfixed constant $a$. A similar solution can be written for the other turning point.

Let us look at a potential with one infinite barrier and a sloped wall:![[The WKB approximation 2026-03-03 21.22.46.excalidraw]]
> Here we define the potential:$$\Huge V(x)=\begin{cases}0 & x<0 \\
f(x) & x>0\end{cases}$$
> We have a right-sloped wall so we will use our improved WKB approximation, particularly the sine integral term $x<<x_2^*$. The boundary condition $\Psi(0)=0$ implies:$$\Huge\begin{align*}
\frac{2a}{\sqrt{p(0)}}\sin\left(\int_0^{x_2^*}p\left(y\right)dy+\frac{\pi}{4}\right)&=0\\
\implies\int_0^{x_2^*}p(y)dy*=(n-1/4)\pi\hbar
\end{align*}$$This is the energy quantisation condition.
> Let us consider $f(x)=\frac{1}{2}m^2\omega^2x^2$ in our quantisation condition:$$\Huge\begin{align*}
p(x)&=\sqrt{2m\left(E-\frac{1}{2}m^2\omega^2x^2\right)}\\
&=m\omega\sqrt{x_2^{*2}-x^2}\\
\implies\int_0^{x_2^*}p(y)dy&=m\omega\int_0^{x_2^*}\sqrt{x_2^{*2}-x^2}dy\\
&=\frac{\pi}{4}m\omega^2x_2^{*2}\\
&=\frac{\pi E}{2\omega}=(n-1/4)\pi\hbar\\
\implies E_n&=(2n-1/2)\hbar\omega
\end{align*}$$
> We can rewrite $\hat n=2n$ and then shift $\tilde n=\hat n-1$ to write:$$\Huge E_{\tilde n}=(\tilde n+1/2)\hbar\omega$$This is exactly the result for the [[Quantum S.H.O.#Excited states|SHO]] with the odd states $\tilde n=1,3,5,\dots$.

# Summary:

We have explored the following situations for our potentials:
> Infinite vertical walls at $x=0,a$ showed us energy was quantised and it followed that:$$\Huge \Psi_\text{WKB}(0)=\Psi_\text{WKB}(a)=0\implies\int_0^ap(y)dy=n\pi\hbar$$
> Finite vertical walls at $x=x_1^*,x_2^*$ gave us a similar formula:$$\Huge \int_{x_1^*}^{x_2^*}p(y)dy=n\pi\hbar$$
> One sloped, one infinite wall motivated us to improve our approximation and led us to another quantisation condition:$$\Huge\int_0^{x_1^*}p(y)dy=(n-1/4)\pi\hbar$$
> For two sloped walls, we would need to use the left and the right wall formulas:$$\Huge\begin{align*}
\Psi_\text{WKBI}^\text{L}(x)&=\frac{2b}{\sqrt{p(x)}}\sin\left(\int_{x_1^*}^xp\left(y\right)dy+\frac{\pi}{4}\right)\\
\Psi_\text{WKBI}^\text{R}(x)&=\frac{2a}{\sqrt{p(x)}}\sin\left(\int_x^{x_2^*}p\left(y\right)dy+\frac{\pi}{4}\right)
\end{align*}$$These describe the wave function of an arbitrary point between the two turning points $x_1*,x_2^*$. Since they describe the same particle, they must agree. Requiring that they match leads to the quantisation condition:$$\Huge\int_{x_1^*}^{x_2^*}p(y)dy=(n-1/2)\pi\hbar$$

All of the energy quantisation formulae we found pretty much differ by constants, however since our approximation is only really valid for $E>>\hbar$ then our formulae are only really valid for $n>>1$. In practice, we can ignore the constant difference and just use our first formula.