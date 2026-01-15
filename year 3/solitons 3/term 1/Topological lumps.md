
A topological lump is a localised field configuration that cannot dissipate or disperse into the vacuum by virtue of a topological conservation law. A topological conservation law is the time-conservation of a topological charge.
# The [[Travelling Waves#The sine-Gordon equation|sine-Gordon kink]] as a topological lump:

Recall the sine-Gordon equation for the field $u$:$$\Huge u_{tt}-u_{xx}+\sin u=0$$We saw that the sine-Gordon kink cannot disperse or dissipate into the vacuum. Using the mechanical model and taking $a\to0$ we can see that the kinetic, $T$, and potential, $V$, energies become:$$\Huge\begin{align*}
T&=\int_{-\infty}^\infty\frac{1}{2}u_{t}^2dx\\
V&=\int_{-\infty}^\infty\frac{1}{2}u_x^2+(1-\cos u)dx
\end{align*}$$where the first term in the potential integral is due to twisting, and the second is due to gravity. We can use this result do deduce the boundary conditions that follow from requiring all field configurations to have finite total energy $E=T+V$. Since total energy is simply the integral over the real line:$$\Huge E=\int_\Re\frac{1}{2}(u_t^2+u_x^2)+(1-\cos u)dx$$For this integral to be finite, we require:$$\Huge u_t,\,\,u_x,\,\,1-\cos u\to_{x\to\pm\infty}0,\,\,\forall t$$Since $1-\cos u=0\iff$ $u$ is an integer multiple of $2\pi$, we require:$$\Huge u(-\infty,t)=2\pi n_-,\,\,u(\infty,t)=2\pi n_+$$for integers $n_-,n_+$. Remarks:
> The individual values of $n_\pm$ do not matter, since $u$ is defined modulo $2\pi$. A shift of $u\rightarrow u+2\pi k$ has no physical meaning other than shifts $n_\pm\to n_\pm +k$. However, the difference $n_+-n_-$ does matter, and is invariant under this ambiguity:$$\Huge\frac{1}{2\pi}(u(\infty,t)-u(-\infty,t))=n_+-n_-=\text{no. of kinks}$$
> The integer $n_+-n_-$ is topological, in the sense that it does not change under continuous changes of $u$. In particular, it cannot change under time evolution as $u$ is a continuous function of $t$. It is therefore a constant of motion/conserved charge. We call this a topological charge due to the fact this arises from a topological property. Solutions with the same topological charge are said to belong to the same topological sector.
> Dispersion and dissipation occur by time evolution. Since the vacuum has $n_+-n_-=0$, any configuration with nonzero values for this cannot disperse/dissipate into the vacuum.

# The Bogomol'nyi bound:

Among the kink solutions to the sine-Gordon equation, there was a static kink with no velocity. We ask if its precise "shape" is stable under small perturbations. An equivalent condition would be to see if the solution minimises energy amongst all configurations with the same topological charge. This is because any perturbation near an energy minimum would increase energy, which is conserved under time evolution.

Therefore, we seek a lower bound for $E=T+V$ in the topological sector of the kink, which has a charge $n_+-n_-=1$. The energy is an integral of non-negative quantities so we automatically get $E\geq0$, but we can do better:$$\Huge\begin{align*}
E=T+V&=\int_{-\infty}^\infty\frac{1}{2}u_t^2+\frac{1}{2}u_x^2+(1-\cos u)dx\\
&\geq_{u_t^2\geq0}\int_{-\infty}^\infty\frac{1}{2}u_x^2+(1-\cos u)dx\\
&=\int_{-\infty}^\infty\frac{1}{2}u_x^2+2\sin^2\frac{u}{2}dx\\
&=\int_{-\infty}^\infty\frac{1}{2}\left(u_x\pm2\sin\frac{u}{2}\right)^2\mp2\sin\frac{u}{2}\cdot u_xdx\\
&=\int_{-\infty}^\infty\frac{1}{2}\left(u_x\pm2\sin\frac{u}{2}\right)^2dx\pm4\left[\cos\frac{u}{2}\right]_{-\infty}^\infty
\end{align*}$$where we used the "Bogomol'nyi trick" to replace the sum of squares by the square of a sum with a correction term that is in fact a total $x$-derivative. If $u$ satisfies the boundary conditions associated with $1$-kink ($u(-\infty,t)=0,\,\,u(\infty,t)=2\pi$) then we can evaluate the boundary term:$$\Huge 4\left[\cos\frac{u}{2}\right]_{-\infty}^\infty=4(-1-1)=-8$$Now choosing the negative branch of the bound:$$\Huge E\geq\int_{-\infty}^\infty\frac{1}{2}\left(u_x-2\sin\frac{u}{2}\right)^2dx+8\geq8$$This is an example of a Bogomol'nyi bound. This is saturated ($E=8$) if and only if the field configuration is static ($u_t=0$) and satisfies the Bogomol'nyi equation:$$\Huge u_x=2\sin\frac{u}{2}$$Therefore we can find the least energy field configuration in the $1$-kink topological sector by looking for solutions $u$ of the Bogomol'nyi equation:$$\Huge u_x=2\sin\frac{u}{2}\implies\int dx=\int\frac{du}{2\sin\frac{u}{2}}=\log\left(\tan\frac{u}{4}\right)$$which has general solution:$$\Huge u(x)=4\arctan(e^{x-x_0})$$This is nothing but the static kink, a special case of a [[Travelling Waves#Mechanical model for the sine-Gordon equation|travelling wave solution]] of the sine-Gordon equation with $v=0$. Note that topology in principle allows the kink to disperse into other solutions with the same charge, however the dispersing waves would carry some energy away. Since the static kink has the least energy in the $n_+-n_-=1$ sector, it cannot lose energy and is therefore stable. This notion of stability originating from minimising energy in a topological sector is known as topological stability.

The Bogomol'nyi equation gives a shortcut to compute the energy density $\varepsilon$ of the static kink ($E=\int_\Re\varepsilon dx$):$$\Huge \varepsilon=\frac{1}{2}u_t^2+\frac{1}{2}u_x^2+2\sin^2\frac{u}{2}=u_x^2=4\text{ sech}^2(x-x_0)$$where we used the fact that $u_t=0$ and $u_x=2\sin\frac{u}{2}$. This shows that energy density of the kink is localised near $x_0$.

There are two ways for a lump to be "long-lived":
> Integrability implies infinitely many conservation laws, leading to "true" integrable solitons
> Topological conservation laws lead to topological lumps

Note that these are not mutually exclusive, the sine-Gordon lump is an example of a topological lump as well as a true soliton
  