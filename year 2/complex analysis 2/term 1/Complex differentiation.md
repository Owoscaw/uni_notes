
To visualise functions $f:\mathbb{C}\mapsto \mathbb{C}$, $4$ dimensions are required. Two dimensions represent the input $z$, and two represent the output $f(z)$. Such functions are therefore visualised by observing where they take certain domains in $\mathbb{C}$.

 Consider the function $f(z)$ and $g(z)=\arg z$ and the images of $\mathbb{D}=\{z\in \mathbb{C}:|z|<1\}$ under $f$ and $g$:![[visualising complex maps]]
 Consider $f(z)=z^n$ with $n\in \mathbb{N}$. If $z=re^{i\theta}$ we see that $f(z)=re^{in\theta}$. Notice that a section of a circle with radius $r$ and $\theta_0\leq\theta\leq\theta_1$ is mapped to a section of a circle with radius $r^n$ with angle $n\theta_0\leq \theta\leq n\theta_1$. In general, a segment of angular size $\eta$ in a circle of radius $r$ is mapped to a segment of angular size $n\eta\mod 2\pi$ in a circle of radius $r^n$. In the case where angular width is greater than or equal to $\frac{2\pi}{n}$, a full circle (or more) is produced. Therefore $f(z)$ is not injective when $\eta>\frac{2\pi}{n}$. Restricting the domain of this function to:$$\Huge S_{n,k}=\left\{z\in \mathbb{C}:-\pi+\frac{2\pi k}{n}<\arg z\leq-\pi+\frac{2\pi(k+1)}{n}\right\}$$Makes the map [[Injective functions|injective]], as each $S_{n,k}$ will be mapped to a full circle. Notice that $z^n$ takes a segment of a ray of angle $\theta$ to a segment of a ray of angle $n\theta$. Therefore we say that:
 > The map $z^n$ injectively takes an angular segment of length $\frac{2\pi}{n}$ which is open at one end and closed at the other from a circle of radius $r$ to the entire circle of radius $r^n$.
 > The map $z^n$ injectively takes a ray of angle $\theta$ to a ray of angle $n\theta\mod2\pi$, also the map $z^n$ injectively takes the wedge bounded by rays of angles $\theta_1,\theta_2$ to the wedge bounded by $n\theta_1\mod2\pi,n\theta_2\mod2\pi$.
 > We can define $n$ different $n$-th roots which are inverses to the map $z^n$, written in the form:$$\Huge z^{\frac{1}{n}}=|z|^{\frac{1}{n}}e^{i\left(\frac{\arg z+2\pi k}{n}\right)}$$

# Exponential and trig functions:

Define the complex exponential function $\exp:\mathbb{C}\mapsto\mathbb{C}$:$$\Huge \exp(z)=e^x(\cos y+i\sin y),\,\,z=x+iy$$For $x,y\in\Re$. We have the following properties:
> $e^z\neq0$ for all $z\in \mathbb{C}$
> $e^{z_1+z_2}=e^{z_1}e^{z_2}$
> $e^z=1$ if and only if $z=2\pi ik$ for some $k\in \mathbb{Z}$
> $e^{-z}=\frac{1}{e^z}$
> $|e^z|=e^{\Re(z)}$

The proofs for which are trivial other than the third statement. $z=2\pi ik\implies e^x=e^0=1$ and we have $e^z=e^x(\cos y+i\sin y)$ with $y=2\pi k$. Now $\cos(2\pi k)=1$ and $\sin(2\pi k)=0$, leaving $e^z=1\times(1+0)=1$. Note that this function is $2\pi i$ periodic, $\exp(z+2\pi i k)=\exp(z)$ for $k\in \mathbb{Z}$. Because $e^z=e^xe^{iy}$, we see that a segment of the line $x=c$ goes to a segment on the circle $|e^z|=r=e^c$. If such segment is of length $\geq 2\pi$, this maps to the full circle.

A line segment from $z=a$ to $z=a+ib$ under the map $e^z$ becomes a portion of the circle given by $r=e^a$ from $\theta=0$ to $\theta=\max{2\pi, b}$. A line segment from $z=-a+ib$ to $z=a+ib$ becomes a ray of angle $\theta=b$ (without the origin) from $e^{-a}$ to $e^a$. More formally:
> The map $e^z$ injectively takes a segment of length $2\pi$ which is open at one end and close at the other from the line $x=c$ to the entire circle of radius $e^c$. If the above segment is closed, or its size is larger than $2\pi$ the image is no longer injective.
> The map $e^z$ injectively takes the line $y=c$ to the ray of angle $c\mod2\pi$ without the origin.
> The map $e^z$ injectively takes the set $\{z\in\mathbb{C}:\theta<\Im(z)\leq\theta+2\pi\}$ to $\mathbb{C}^*=\mathbb{C}\setminus\{0\}$

Now, being familiar with the map $e^z$ we define the following complex trig functions:$$\Huge \sin(z):=\frac{1}{2i}(e^{iz}-e^{-iz}),\,\,\cos(z):=\frac{1}{2}(e^{iz}+e^{-iz})$$$$\Huge \sinh(z):=\frac{1}{2}(e^z-e^{-z}),\,\,\cosh(z):=\frac{1}{2}(e^z+e^{-z})$$Then, for $z=x+iy$, we get the following formulae associated with these definitions:
> $\sin(z)=\sin(x)\cosh(y)+i\cos(x)\sinh(y)$
> $\cos(z)=\cos(x)\cosh(y)-i\sin(x)\sinh(y)$
> $\sinh(z)=-i\sin(iz)=\sinh(x)\cos(y)+i\cosh(x)\sin(y)$
> $\cosh(z)=\cos(iz)=\cosh(x)\cos(y)+i\sinh(x)\sin(y)$
> $\sin^2(z)+\cos^2(z)=1$
> $\cosh^2(z)-\sinh^2(z)=1$

Note that $\sin(z),\cos(z)$ are not bounded as they involve real terms of $\cosh,\sinh$. We get the following lemma from these definitions:
> The map $\sin(z)$ injectively takes a segment of length $2\pi$ which is open at one end and closed at the other from the line $y=c$ to an ellipse when $c\neq0$. 
> The map $\sin(z)$ injectively takes the line $x=c$ to a one sided hyperbola when $c\neq\pi k$ and $c\neq \frac{\pi}{2}+\pi k$ for some $k\in \mathbb{N}$

While $e^z$ is not injective, we observe that a restricted domain can make the map injective with image $\mathbb{C}^*$. This prompts the definition of an inverse. For every $w\in\mathbb{C}^*$ the equation $e^z=w$ has a solution $z$. Furthermore if we write $w=|w|e^{i\varphi}$ with $\varphi=\arg(w)$. Then all solutions $z$ are given by:$$\Huge z=\log|w|+i(\varphi+2\pi k)$$For some $k\in \mathbb{Z}$. To prove this, write $z=x+iy$ and $w=|w|e^{i\varphi}$. Then we get the following:$$\Huge e^z=w\iff e^xe^{iy}=|w|e^{i\varphi}\iff e^x=|w|,\,\,y=\varphi+2\pi k$$Which gives the solution $z=x+iy$ as required. Fixing $k$ and considering $\mathbb{C}^*$ we propose that:$$\Huge g(w)=\log|w|+i(\arg w+2\pi k)$$Is a continuous inverse to $e^z$. Consider $w_n=e^{i(-\pi+\frac{1}{n})}$ then $w_n\to e^{i\pi}\neq e^{-i\pi}$, so this $g(w)$ is not a continuous inverse of $e^z$. In order to define a continuous inverse we must prevent the angle from jumping every $2\pi$. To do this, we remove the ray:$$\Huge R_\theta=\{re^{i\theta}:0\leq r<\theta\}$$For any two real numbers $\theta_1<\theta_2$ with $\theta_2-\theta_1=2\pi$. Let $\arg$ be the choice of argument function with values in $(\theta_1,\theta_2]$. Then the function:$$\Huge \log(z):=\log|z|+i\arg(z)$$Is called a branch of logarithm. There is a jump discontinuity along the ray $R_{\theta_1}=R_{\theta_2}$, called the branch cut. Choosing $\arg(z)=\text{Arg}(z)\in(-\pi,\pi]$ , then we obtain a branch of logarithm called the principle branch of log. We write this as $\text{Log}$ for such principle branch, given by:$$\Huge \text{Log}:=\log|z|+i\text{Arg}(z)$$The principle branch of logarithm has a jump discontinuity along the ray given by $\Re_{\leq0}$. So all possible branches of $z^{\frac{1}{n}}$ are:$$\Huge z^{\frac{1}{n}}=|z|^{\frac{1}{n}}\exp\left(i\frac{\text{Arg}(z)}{n}+\frac{2\pi k}{n}\right)$$Take $(1-i)^{\frac{1}{2}}$ as example, using the principle branch of the logarithm:$$\Huge (1-i)^{\frac{1}{2}}=e^{\frac{1}{2}\text{Log}(1-i)}=e^{\frac{1}{2}(\log|1-i|+i\text{Arg}(1-i))}=e^{\frac{1}{2}(\log(\sqrt{2})+i\frac{\pi}{4})}$$

Functions of the form:$$\Huge f(z)=\frac{az+b}{cz+d}$$With $a,d,b,c\in\mathbb{C}$ and $ad-bc\neq 0$.

# Complex differentiability:

A function $f:U\mapsto\mathbb{C}$ defined on an open set $U$ in $\mathbb{C}$ is called complex differentiable at $z_0\in U$ if:$$\Huge \lim_{z\to z_0}\frac{f(z)-f(z_0)}{z-z_0}$$Exists. If so, we call this the derivative of $f$ at $z_0$. Another form of this limit is:$$\Huge f'(z_0)=\lim_{h\to 0}\frac{f(z_0+h)-f(z_0)}{h}$$Note that this is actually a limit of two variables, since $z=x+iy$ for $x,y\in\Re$. Much like real valued functions, if $f$ is complex differentiable at $z_0$, it is continuous at $z_0$. We had the notion of left and right limits in real valued functions. Now there are limits from every direction at once, since there exists limits for $\pm\Re$ and $\pm\Im$ axis, it also makes sense to take a limit along an angle.

Take for example $f(z)=\overline z$. We ask where this is differentiable. Given $z_0\in\mathbb{C}$:$$\large \lim_{h\to 0}\frac{f(z_0+h)-f(z_0)}{h}=\lim_{h\to 0}\frac{\overline{z_0+h}-\overline z_0}{h}=\lim_{h\to0}\frac{\overline h}{h}=\lim_{h\to0}\frac{|h|e^{-i\text{Arg}(h)}}{|h|e^{i\text{Arg}(h)}}=\lim_{h\to0}e^{-2i\text{Arg}(h)}$$This limit does not exist, since different paths to zero give different values of the limit. Therefore we can say that $\bar z$ is not differentiable at any point. 

Note that all the same notions for [[Differentiable Functions#Differentiable results|differentiable]] functions exist, that is the product, sum, quotient, and composition of two differentiable functions are also differentiable. These are all proved in a similar way to their real valued equivalents.

# Cauchy-Riemann equations:

We can write any complex valued function as:$$\Huge f(z)=f(x+iy)=u(x,y)+iv(x,y)$$Where $u,v$ are functions from $U\subseteq\mathbb{C}$ to $\Re$. We aim to connect complex differentiation of $f$ to real differentiation of $u,v$. This prompts the following proposition, the Cauchy Riemann equations:

Let $f=u+iv$ be complex differentiable at $z_0=x_0+iy_0$. Then the real partial derivatives $u_x,u_y,v_x,v_y$ exist at $(x_0,y_0)$ and satisfy:$$\Huge u_x(x_0,y_0)=v_y(x_0,y_0),\,\,u_y(x_0,y_0)=-v_x(x_0,y_0)$$Furthermore, the derivative of $f$ at $z_0$:$$\Huge f'(z_0)=u_x(z_0)+iv_x(z_0)=v_y(z_0)-iu_y(z_0)$$This theorem gives a condition when $f$ is not complex differentiable, when the equations do not hold. One can show that $f$ is complex differentiable if and only if $u,v$ are real differentiable at $(x_0,y_0)$ and the equations hold.

Let $f=u+iv$ be defined on an open subset $U$ of $\mathbb{C}$. Assume the partial derivatives of $u,v$ wrt to $x,y$ exist, are continuous, and satisfy the Cauchy-Riemann equations at $z_0\in U$. Then $f$ is complex differentiable at $z_0$. The proof is as follows:![[C-R proof]]

Take $f(z)=e^z=e^xe^{iy}$ for example. Here, $u(x,y)=e^x\cos(y),\,\,v(x,y)=e^x\sin(y)$ with $u,v\in C^1$. We then check the C-R equations:$$\ u_x(x,y)=e^x\cos(y),\,\,u_y(x,y)=-e^x\sin(y),\,\,v_y(x,y)=e^x\cos(y),\,\,v_x(x,y)=e^x\sin(y)$$So these equations are satisfied. Moreover we can find its derivative:$$\Huge f'(z)=u_x(x,y)+iv_x(x,y)=e^x\cos(y)+ie^x\sin(y)=e^xe^{iy}=e^z$$So we have that the derivative of $f(z)=e^z$ is $f'(z)=e^z$.

## Holomorphicity:
A function $f:U\mapsto\mathbb{C}$ defined on an open subset $U$ of $\mathbb{C}$ is holomorphic on $U$ if it is complex differentiable at every point in $U$. We say that $f$ is holomorphic at $z_0$ if it is holomorphic on an [[Metric spaces#Open and closed sets|open ball]] $B_\epsilon(z_0)$ for some $\epsilon>0$. We call functions that are holomorphic on $\mathbb{C}$ entire functions.

We have shown that $e^z$ is holomorphic on $\mathbb{C}$, that is it is an entire function. One can build $\cos,\sin,\cosh,\sinh$ from linear combinations and compositions of $e^z$, making these functions entire as well. Note that some functions may be differentiable on a given set, but not holomorphic anywhere as no open ball can be found contained fully within the set.

Being differentiable on an open set if not enough to be called holomorphic. Consider the set $U=(-1,0)\cup(0,1)$. $U$ is an open set since it is a union of two open sets. Consider the function $f(x)=\begin{cases}-1&x\in(-1,0)\\1&x\in(0,1)\end{cases}$, which is differentiable with $f'(x)=0$ however $f$ is not a constant function.

# Paths and connectedness:

A path or curve from $z\in \mathbb{C}$ to $w\in\mathbb{C}$ is a continuous function $\gamma:[0,1]\mapsto\mathbb{C}$ with $\gamma(0)=z$ and $\gamma(1)=w$. We call the path closed if $z=w$. A path is called continuously differentiable ($C^1$) if its real and imaginary parts are continuously differentiable on $[0,1]$:$$\Huge \gamma'(t)=(\Re(\gamma(t)))'+i(\Im(\gamma(t)))'$$We call a subset $U\subseteq\mathbb{C}$ is $C^1$ path connected if for every pair of points $z,w\in U$ there exists a $C^1$ path from $z$ to $w$ such that $\gamma(t)\in U$ for all $t\in[0,1]$. In general paths can be defined from an interval $[a,b]$, for instant let $\gamma_1:[a,b]\mapsto X$ then define $\gamma:[0,1]\mapsto X$ as:$$\Huge \gamma(t)=\gamma_1\left(\frac{t-a}{b-a}\right)$$Conversely for $\gamma:[0,1]\mapsto X$ define $\gamma_1:[a,b]\mapsto X$:$$\Huge \gamma_1(t)=\gamma((b-a)t+a)$$Note that in general, path connected means the existence of a path between any two points. Also all open balls are path connected. We can then define a domain.

A domain $D$ is an open path connected subset of $\mathbb{C}$. For example, all open balls , $\mathbb{C}^*$, and $\mathbb{H}_R$ (the right hand side of $\mathbb{C}$) are all domains. Note that $\{z\in\mathbb{C}:|z|\neq1\}$ is not a domain, as there exists no path from a point $z_1\in\mathbb{C}$ with $|z_1|<1$ to a point $z_2\in\mathbb{C}$ with $|z_2|>1$, despite the set being open.

Let $f:D\mapsto\mathbb{C}$ be holomorphic on a domain $D\subseteq\mathbb{C}$. If $f'(z)=0$ for every $z\in D$, then $f$ is constant on $D$. To prove this, we need to define the chain rule.

Let $U\subseteq\mathbb{C}$ be an open set $f:U\mapsto\mathbb{C}$ be a holomorphic function on $\mathbb{C}$ and $\gamma:[0,1]\mapsto U$ be a $C^1$ path, then for $t_0\in[0,1]$ we have:$$\Huge (f\circ\gamma)'(t_0)=f'(\gamma(t_0))\gamma'(t_0)$$It is enough to show that for any $z_1,z_2\in D$ we have $f(z_1)=f(z_2)$. Since $D$ is a domain, there exists some $\gamma:[0,1]\mapsto D$ such that $\gamma(0)=z_1$ and $\gamma(1)=z_2$. Since $\gamma$ is $C^1$ and $f$ is holomorphic we have $f\circ\gamma:[0,1]\mapsto D$ is differentiable and $f(z_1)=f(\gamma(0)),f(z_2)=g(\gamma(1))$. By the chain rule we have:$$\Huge (f(\gamma(t)))'=f'(\gamma(t))\gamma'(t)=0$$For all $t\in[0,1]$. So $\Re(f(\gamma(t)))$ is differentiable and $\Re(f(\gamma(t)))'=0$ for all $t\in[0,1]$. Therefore $\Re(f(\gamma(t))):[0,1]\mapsto\Re$ so by previous theorems, $\Re(f(\gamma(t)))$ is constant. Then we have $\Re(f(z_1))=\Re(f(\gamma(0)))=\Re(f(\gamma(1)))=\Re(f(z_2))$, similarly one can show the imaginary parts of $f$ are constant, so we have that $f$ is constant as $z_1,z_2$ are arbitrary.

## Angle preservation and conformism:
Given a path $\gamma:[0,1]\mapsto\mathbb{C}$ that is differentiable at some $t_0\in[0,1]$, the notion of a tangent vector to $\gamma(t_0)$ can be talked about, analogous to $\Re^2$:![[tangent path]]
We say that a real differentiable map $f:D\mapsto\mathbb{C}$ on a domain $D\subseteq\mathbb{C}$ is conformal at $z_0$ if it preserves the angle and orientation between any two tangent vectors at $z_0$. This is the same as saying that the angle and orientation between any two $C^1$ curves passing through $z_0$. 

Let $f$ be a holomorphic map at $z_0$. If $f'(z_0)\neq0$ then $f$ is conformal at $z_0$. To prove this, let $\gamma:[0,1]\mapsto D$ be a $C^1$ path such that $\gamma(t_0)=z_0$ for some $t_0\in[0,1]$. The tangent vector to $\gamma$ at $z_0=\gamma(t_0)$ is given by $\gamma'(t_0)$. Then $f\circ\gamma:[0,1]\mapsto\mathbb{C}$ is a differentiable curve such that $f(\gamma(t_0))=f(z_0)$. By the chain rule we have:$$\Huge (f(\gamma(t)))'\vert_{t=t_0}=f'(\gamma(t_0))\gamma'(t_0)=f'(z_0)\gamma'(t_0)$$This implies that the tangent vector of $f\circ\gamma$ at $t_0$ is the tangent vector $\gamma'(t_0)$ scaled by $|f'(z_0)|\neq0$ and rotated by $\text{Arg}(f'(z_0))$. Since the scaling and rotation do not depend on $\gamma$ (uniform in $\gamma$), the angle between curves remains fixed as well as the orientation. This has a corollary where any conformal map will map orthogonal grids in the $(x,y)$ plane to orthogonal grids.

Let $D$ be a domain. If $f$ is conformal at $z_0\in D$ then $f$ is complex differentiable at $z_0$ and $f'(z_0)\neq0$. Therefore if $f$ is conformal on $D$, then $f$ is holomorphic on $D$ and $f'(z)\neq0$ for all $z\in D$. That is, $f$ is conformal on $D$ if and only if $f$ is holomorphic with $f'(z)\neq0$ for all $z\in D$.

## Biholomorphic:
Let $D$ and $D'$ be domains. We say that the map $f:D\mapsto D'$ is biholomorphic if $f$ is holomorphic, a bijection, and the inverse $f^{-1}:D'\mapsto D$ is also holomorphic. A biholomorphic map $f$ is called a biholomorphism. When such an $f$ exists, we call $D,D'$ biholomorphic and write $f:D\tilde{\rightarrow}D'$.

The map $f(z)=az+b$ for $a\in\mathbb{C}^*$ and $b\in\mathbb{C}$ is a biholomorphism. Since $a\neq0$ we can write it's inverse as $f^{-1}(z)=\frac{1}{a}-\frac{b}{a}$, $f(z)$ is also holomorphic. So the existence of this inverse with the holomorphicity of $f(z)$ makes the map biholomorphic.

The map $f(z)=e^z$ is not a biholomorphism between $\mathbb{C}$ and $\mathbb{C}^*$ since despite it being holomorphic, it is not injective. Note that restricting the domain to $\{z\in\mathbb{C}:-\pi<\Im(z)<\pi\}$ we see that $e^z$ becomes bijective, with an inverse function of $\text{Log}$. However $\text{Log}$ is not continuous on this set, so we still do not have biholomorphism. Further restricting the domain to $\{z\in\mathbb{C}:-\pi<\Im(z)<\pi\}=\mathbb{C}\setminus\Re_{\leq0}$, the inverse becomes continuous and holomorphic, so the map $e^z$ becomes biholomorphic on this set.

## Automorphisms:
Let $D\subset\mathbb{C}$ be a domain. The set of all biholomorphic maps $f:D\tilde{\rightarrow}D$ from $D$ to itself forms a group under composition. This is called the automorphism group of $D$, denoted as $\text{Aut}(D)$. 