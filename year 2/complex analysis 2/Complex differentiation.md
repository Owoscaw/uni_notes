
To visualise functions $f:\mathbb{C}\mapsto \mathbb{C}$, $4$ dimensions are required. Two dimensions represent the input $z$, and two represent the output $f(z)$. Such functions are therefore visualised by observing where they take certain domains in $\mathbb{C}$.

 Consider the function $f(z)$ and $g(z)=\arg z$ and the images of $\mathbb{D}=\{z\in \mathbb{C}:|z|<1\}$ under $f$ and $g$:![[visualising complex maps]]
 Consider $f(z)=z^n$ with $n\in \mathbb{N}$. If $z=re^{i\theta}$ we see that $f(z)=re^{in\theta}$. Notice that a section of a circle with radius $r$ and $\theta_0\leq\theta\leq\theta_1$ is mapped to a section of a circle with radius $r^n$ with angle $n\theta_0\leq \theta\leq n\theta_1$. In general, a segment of angular size $\eta$ in a circle of radius $r$ is mapped to a segment of angular size $n\eta\mod 2\pi$ in a circle of radius $r^n$. In the case where angular width is greater than or equal to $\frac{2\pi}{n}$, a full circle (or more) is produced. Therefore $f(z)$ is not injective when $\eta>\frac{2\pi}{n}$. Restricting the domain of this function to:$$\Huge S_{n,k}=\left\{z\in \mathbb{C}:-\pi+\frac{2\pi k}{n}<\arg z\leq-\pi+\frac{2\pi(k+1)}{n}\right\}$$Makes the map [[Injective functions|injective]], as each $S_{n,k}$ will be mapped to a full circle. Notice that $z^n$ takes a segment of a ray of angle $\theta$ to a segment of a ray of angle $n\theta$. Therefore we say that:
 > The map $z^n$ injectively takes an angular segment of length $\frac{2\pi}{n}$ which is open at one end and closed at the other from a circle of radius $r$ to the entire circle of radius $r^n$.
 > The map $z^n$ injectively takes a ray of angle $\theta$ to a ray of angle $n\theta\mod2\pi$, also the map $z^n$ injectively takes the wedge bounded by rays of angles $\theta_1,\theta_2$ to the wedge bounded by $n\theta_1\mod2\pi,n\theta_2\mod2\pi$.
 > We can define $n$ different $n$-th roots which are inverses to the map $z^n$, written in the form:$$\Huge z^{\frac{1}{n}}=|z|^{\frac{1}{n}}e^{i\left(\frac{\arg z+2\pi k}{n}\right)}$$

## Exponential and trig functions:
Define the complex exponential function $\exp:\mathbb{C}\mapsto\mathbb{C}$:$$\Huge \exp(z)=e^x(\cos y+i\sin y),\,\,z=x+iy$$For $x,y\in\Re$. We have the following properties:
> $e^z\neq0$ for all $z\in \mathbb{C}$
> $e^{z_1+z_2}=e^{z_1}e^{z_2}$
> $e^z=1$ if and only if $z=2\pi ik$ for some $k\in \mathbb{Z}$
> $e^{-z}=\frac{1}{e^z}$
> $|e^z|=e^{\Re(z)}$

The proofs for which are trivial