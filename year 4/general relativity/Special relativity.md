
Because the speed of light falls out of [[Abelian gauge theories#Maxwell equation and actions|Maxwell's equations]], it is universal across all reference frames. Universality of the laws of physics seems to require the universality of the speed of light.

# Lorentz transformations:

We consider an observer in a coordinate system $(x,t)$ and label events on this plane by their coordinates as well:![[Special relativity 2026-10-07 12.11.23.excalidraw]]We are interested in the coordinate transformation relating $(t',\underline{x}')$ to $(t,\underline{x})$ for a given event. This is called a Galilean transformation:$$\Huge\begin{align*}
\underline{x}'&=\underline{x}-vt\\
t'&=t
\end{align*}$$This is not compatible with the universality of the speed of light, as this leads to the velocity addition rule:$$\Huge \frac{d\underline{x}'}{dt}=\frac{d\underline{x}}{dt}-\underline{v}$$Let us therefore consider a new transformation, under the following assumptions:
> Transformation is linear
> Other coordinates unaffected
> $x=vt$ should map to $x'=0$, which implies $x'=\gamma(v)(x-vt)$
> $x'=-vt'$ should map to $x=0$, which implies $x=\gamma(v)(x+vt)$

Now let us impose the universality of lightspeed by requiring $x=ct$ maps to $x'=ct'$:$$\Huge\begin{align*}
ct'=x'&=\gamma(x-vt)\\
&=\gamma(c-v)t\\
ct=x&=\gamma(x'+vt')\\
&=\gamma(c+v)t'\\
\implies c^2t&=\gamma(c+v)ct'\\
&=\gamma(c+v)\gamma(c-v)t\\
&=\gamma^2(c^2-v^2)t\\
\implies\gamma(v)&=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}}
\end{align*}$$Solving $x=\gamma(x'+vt')$ for $t'$ we find:$$\Huge\begin{align*}
t'&=-\frac{x'}{v}+\frac{x}{v\gamma}\\
&=-\frac{\gamma(x-vt)}{v}+\frac{x}{v\gamma}\\
&=\gamma\left(t-\frac{v}{c^2}x\right)
\end{align*}$$This lets us define the Lorentz transformation:$$\Huge x'=\gamma(x-vt),\,\,t'=\gamma\left(t-\frac{v}{c^2}x\right),\,\,\gamma=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}}$$

The expression for $t'$ is distinctly profound and leads to the Relativity of Simultaneity:  Events at the same time in one coordinate system do not necessarily occur at the same time in other coordinate systems. Note that the separation between events is invariant under coordinate transforms, implying the invariance of the spacetime interval.$$\Huge \Delta s^2=-c^2\Delta t^2+\Delta x^2$$is invariant. Let us check that this is indeed true:$$\large\begin{align*}
\implies\Delta t'&=\gamma\left(\Delta t-\frac{v}{c^2}\Delta x\right)\\
\implies\Delta x'&=\gamma(\Delta x-v\Delta t)\\
\implies -c^2(\Delta t')^2+(\Delta x')^2&=\gamma^2\left(-\left(-c\Delta t-\frac{v}{c^2}\right)+(\Delta x-v\Delta t)^2\right)\\
&=\gamma^2\left(-c^2\Delta t^2\left(1-\frac{v^2}{c^2}\right)+\Delta x^2\left(1-\frac{v^2}{c^2}\right)\right)\\
&=-c^2\Delta t^2+\Delta x^2
\end{align*}$$

This spacetime interval is a coordinate-independent property of the events involved. We take this to be fundamental and define Lorentz transformations to be the linear transformations leaving $\Delta s^2$ invariant. Note that this need not be positive:![[Special relativity 2026-10-07 12.54.49.excalidraw]]