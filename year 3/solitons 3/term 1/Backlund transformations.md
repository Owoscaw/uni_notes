
We have previously constructed solutions for moving solitons as [[Travelling Waves#The Basic properties of Solitons The KdV equation KdV soliton|travelling waves]] by reducing a PDE into multiple ODEs. Now that we aim to describe the solution for multiple colliding solitons, we must use a different method. In these cases, it will not be possible to reduce the PDE into ODEs, so we introduce the method known as the Backlund transformation.

There are two main uses of the Backlund transformation:
> To generate solutions of a more complex PDE using a simpler PDE
> To generate new solutions of a given PDE from already known solutions of the same PDE


# Definition:

Consider two functions $u,v$ with two differential equations $P[u]=0,Q[v]=0$ where $P,Q$ are two differential operators. If there is a pair of relations, $R_1[u,v]=0,R_2[u,v]=0$, between $u,v$ such that:
> If $P[u]=0$ then the relations can be solved for $v$, giving a solution of $Q[v]=0$
> If $Q[v]=0$ then the relations can be solved for $u$, giving a solution of $P[u]=0$

Then the relations are called a Backlund transformation (BT). Furthermore if $P=Q$, then the relations are called an auto-Backlund transformation (a-BT). This is useful if the relation is easier to solve than either differential equation, which can be used to generate solutions to the differential equations.
> $P[u]=0,Q[v]=0$ are known as integrability conditions
> $R_1[u,v]=0,R_2[u,v]=0$ can be integrated for $v,u$ if the integrability condition $P[u]=0,Q[v]=0$ respectively are satisfied
> 

## Simple example:
Take the two dimensional Laplace operator $P=Q=\partial_x^2+\partial_y^2$ and the Backlund transformation $R_1[u,v]=u_x-v_y=0,R_2[u,v]=u_y+v_x=0$. We can check that these are valid integrability conditions by differentiating them wrt $x,y$ and summing/subtracting:$$\Huge\begin{align*}
0=\partial_xR_1+\partial_yR_2&=u_{xx}-v_{yx}+v_{xy}+u_{yy}=u_{xx}+u_{yy}\\
0=-\partial_yR_1+\partial_xR_2&=-u_{xy}+v_{yy}+u_{yx}+v_{xx}=u_{xx}+u_{yy}
\end{align*}$$Therefore the relations imply the differential operator, showing that it is an auto-Backlund transformation.

$v(x,y)=2xy$ solves the Laplace equation, we can use the a-BT to find another solution, $u$, of the same equation:$$\Huge\begin{cases}u_x=v_y=2x \\
u_y=-v_x=-2y\end{cases}\implies\begin{cases}u=x^2+f(y) \\
f'(y)=-2y\end{cases}\implies f(y)=-y^2+C$$so we find that $u(x,y)=x^2-y^2+C$ for some constant $C$ is another solution. Note that the equations $R_1[u,v]=R_2[u,v]=0$ are simply the [[Complex differentiation#Cauchy-Riemann equations|C-R equations]] for the holomorphic function $w=u+iv$ of the complex variable $z=x+iy$. In our example, $w(z)=z^2+C$. Two functions $u,v$ that solve the Laplace equation are often called harmonic conjugates.

# Backlund transformations for [[Travelling Waves#The sine-Gordon equation|sine-Gordon]]:

Firstly, we rewrite the sine-Gordon equation by changing variables to [[year 3/solitons 3/term 1/Conservation laws#Relativistic field equations|light-cone]] coordinates:$$\Huge x_+=\frac{1}{2}(t+x),\,\,x_-=\frac{1}{2}(t-x)$$Recall we found the form of the derivative operator:$$\Huge\frac{\partial^2}{\partial x_+\partial x_-}=\frac{\partial^2}{\partial t^2}-\frac{\partial^2}{\partial x^2}$$making the sine-Gordon equation:$$\Huge u_{+-}=-\sin u$$We then define the BT:$$\Huge\begin{align*}
\partial_+(u-v)&=\frac{2}{a}\sin\left(\frac{1}{2}(u+v)\right)\\
\partial_-(u+v)&=-2a\sin\left(\frac{1}{2}(u-v)\right)
\end{align*}$$with $a\in\Re$ a constant parameter. To check that this is valid, we differentiate the first expression wrt $x_-$ and the second wrt $x_+$:$$\Huge\begin{align*}
\partial_-\partial_+(u-v)&=\frac{2}{a}\cos\left(\frac{1}{2}(u+v)\right)\partial_-\left(\frac{1}{2}(u+v)\right)\\
&=-\frac{1}{a}\cos\left(\frac{1}{2}(u+v)\right)2a\sin\left(\frac{1}{2}(u-v)\right)\\
&=-2\cos\left(\frac{1}{2}(u+v)\right)\sin\left(\frac{1}{2}(u-v)\right)\\
&=\sin v-\sin u\\
\partial_+\partial_-(u+v)&=-2a\cos\left(\frac{1}{2}(u-v)\right)\partial_+\left(\frac{1}{2}(u-v)\right)\\
&=-a\cos\left(\frac{1}{2}(u-v)\right)\frac{2}{a}\sin\left(\frac{1}{2}(u+v)\right)\\
&=-2\cos\left(\frac{1}{2}(u-v)\right)\sin\left(\frac{1}{2}(u+v)\right)\\
&=-\sin u-\sin v
\end{align*}$$We can then eliminate either $u,v$:$$\Huge u_{+-}=-\sin u,\,\,v_{+-}=-\sin v$$Therefore we have an a-BT for $u,v$.

## sine-Gordon kink example:
We start with the simplest solution to the sine-Gordon equation, $v=0$. This makes the BT:$$\Huge\begin{align*}
\partial_+u&=\frac{2}{a}\sin\left(\frac{u}{2}\right)\\
\partial_-u&=-2a\sin\left(\frac{u}{2}\right)
\end{align*}$$which we solve through separation of variables:$$\Huge\begin{align*}
\int\frac{du}{\sin\left(\frac{u}{2}\right)}&=\frac{2}{a}\int dx_+\\
2\log\left(\tan\left(\frac{u}{4}\right)\right)+f(x_-)&=\frac{2}{a}x_+\\
\int\frac{du}{\sin\left(\frac{u}{2}\right)}
&=-2a\int dx_-\\
2\log\left(\tan\left(\frac{u}{4}\right)\right)+g(x_+)&=-2ax_-
\end{align*}$$Where $f,g$ are constants of integration. We find these by:$$\Huge \frac{2}{a}x_++2ax_-=f(x_-)-g(x_+)$$which we can rearrange to get all $x_+,x_-$ variables on each side of the equation, making them constant. For convenience we write such constant as $-2C$:$$\Huge\begin{align*}
g(x_+)&=-\frac{2}{a}x_+-2C\\
f(x_-)&=2ax_--2C\\
\implies2\log(\tan(\frac{u}{4}))&=\frac{2}{a}x_+-2ax_-+2C\\
\implies u&=4\arctan\left(e^{\frac{1}{a}x_+-ax_-+C}\right)
\end{align*}$$Which is a rather non-trivial solution, found from the trivial solution $v=0$. However we are not done yet, we must convert back from light-cone coordinates to $(x,t)$ coordinates:$$\Huge\begin{align*}
\frac{1}{a}x_+-ax_-&=\frac{1}{a}\left(\frac{1}{2}(t+x)\right)-a\left(\frac{1}{2}(t-x)\right)\\
&=\left(\frac{1}{2a}+\frac{a}{2}\right)x+\left(\frac{1}{2a}-\frac{a}{2}\right)t\\
&=\frac{1+a^2}{2a}\left(x-\frac{a^2-1}{a^2+1}t\right)
\end{align*}$$Defining $v=\frac{a^2-1}{a^2+1}$ we immediately see that this is a travelling wave solution. Using this definition of $v$, one can show that $\frac{1+a^2}{2a}=\frac{\text{sign }a}{\sqrt{1-v^2}}=\epsilon\gamma$ where $\gamma=\frac{1}{\sqrt{1-v^2}}$ is the Lorentz factor. This makes the solution we found from the trivial solution:$$\Huge u(x,t)=4\arctan(e^{\epsilon\gamma(x-vt-x_0)})$$Then for the different values of $a$ we get:
> $a<-1$ corresponds to a right moving anti-kink
> $-1<a<0$ corresponds to a left moving anti-kink
> $0<a<1$ corresponds to a left moving kink
> $a>1$ corresponds to a right moving kink

Therefore our BT creates either a kink or anti-kink from the "vacuum solution" $v=0$, without losing any options through the variation of $a$.

# Theorem of permutability:

Consider applying a Backlund transformation twice with parameters $a_1,a_2$ in two possible orders:![[Backlund transformations 2025-11-24 13.27.21.excalidraw]]The final results $u_3,u_4$ will look like $u_0$ but with two added solitons with parameters $a_1,a_2$. The theorem of permutability then dictates:

For any $u_1,u_2$, the integration constants in the second Backlund transformations, which generate $u_3,u_4$, can be arranged so that $u_3=u_4$. That is to say, $a_1,a_2$ can be made to commute:![[Backlund transformations 2025-11-24 13.29.59.excalidraw]]
We hope to be able to get rid of all derivatives in the Backlund transformations and obtain an algebraic expression for $u_0,u_1,u_2,u_3$. First consider the $\partial_+$ parts of the transformations, on the upper branch:$$\Huge\begin{align*}
(u_1-u_0)_+&=\frac{2}{a_1}\sin\left(\frac{u_1+u_0}{2}\right)\\
(u_3-u_1)_+&=\frac{2}{a_2}\sin\left(\frac{u_3+u_1}{2}\right)\\
\implies(u_3-u_0)_+&=\frac{2}{a_1}\sin\left(\frac{u_1+u_0}{2}\right)+\frac{2}{a_2}\sin\left(\frac{u_3+u_1}{2}\right)
\end{align*}$$Then for the lower route we simply swap $a_1\leftrightarrow a_2$ and $u_1\leftrightarrow u_2$ to get:$$\Huge (u_3-u_0)_+=\frac{2}{a_2}\sin\left(\frac{u_2+u_0}{2}\right)+\frac{2}{a_1}\sin\left(\frac{u_3+u_2}{2}\right)$$Equating these two expressions gives the following algebraic relation:$$\large \frac{1}{a_1}\sin\left(\frac{u_1+u_0}{2}\right)+\frac{1}{a_2}\sin\left(\frac{u_3+u_1}{2}\right)=\frac{1}{a_2}\sin\left(\frac{u_2+u_0}{2}\right)+\frac{1}{a_1}\sin\left(\frac{u_3+u_2}{2}\right)$$
This is very useful, as we can generate a $2$-soliton solution $u_3$ using two $1$-soliton solutions $u_1,u_2$ and the vacuum solution $u_0$. Iterating this leads to $n$-soliton solutions. This is one interpretation of a "nonlinear superposition principle".

To check that our procedure is consistent, we must check the $\partial_-$ part of the transformations. Using the same method we get:$$\Huge\begin{align*}
(u_0-u_3)_-&=2a_2\sin\left(\frac{u_3-u_1}{2}\right)-2a_1\sin\left(\frac{u_1-u_0}{2}\right)\\
&=2a_1\sin\left(\frac{u_3-u_2}{2}\right)-2a_2\sin\left(\frac{u_2-u_0}{2}\right)
\end{align*}$$Which gives the relation:$$\large a_2\sin\left(\frac{u_3-u_1}{2}\right)-a_1\sin\left(\frac{u_1-u_0}{2}\right)=a_1\sin\left(\frac{u_3-u_2}{2}\right)-a_2\sin\left(\frac{u_2-u_0}{2}\right)$$
We require our relations to be equivalent, so we begin by writing the $\partial_+$ relation as:$$\large\frac{1}{a_1}\left(\sin\left(\frac{u_1+u_0}{2}\right)-\sin\left(\frac{u_3+u_2}{2}\right)\right)=\frac{1}{a_2}\left(\sin\left(\frac{u_2+u_0}{2}\right)-\sin\left(\frac{u_3+u_1}{2}\right)\right)$$Then multiplying by $a_1a_2/2$ and using the sine addition rules gives:$$\Huge a_2\sin\left(\frac{u_1+u_0-u_3-u_2}{4}\right)=a_1\sin\left(\frac{u_2+u_0-u_3-u_1}{4}\right)$$
Similarly, we rearrange the $\partial_-$ expression to:$$\Huge a_1\sin\left(\frac{u_3-u_2+u_1-u_0}{4}\right)=a_2\sin\left(\frac{u_3-u_1+u_2-u_0}{4}\right)$$which agrees. We now aim to rearrange to find $u_3$ in terms of the other solutions. Letting $A=(u_0-u_3)/4$ and $B=(u_1-u_2)/4$ we have:$$\Huge\begin{align*}
a_1\sin(A-B)&=a_2\sin(A+B)\\
\implies a_1(\sin A\cos B-\sin B\cos A)&=a_2(\sin A\cos B+\sin B\cos A)
\end{align*}$$Dividing through by $\cos A\cos B$ we have:$$\Huge\begin{align*}
a_1(\tan A-\tan B)&=a_2(\tan A+\tan B)\\
\implies (a_1-a_2)\tan A&=(a_1+a_2)\tan B\\
\implies\tan\left(\frac{u_0-u_3}{4}\right)&=\frac{a_1+a_2}{a_1-a_2}\tan\left(\frac{u_1-u_2}{4}\right)\\
\implies\tan\left(\frac{u_3-u_0}{4}\right)&=\frac{a_2+a_1}{a_2-a_1}\tan\left(\frac{u_1-u_2}{4}\right)
\end{align*}$$

# Two-Soliton solution:

We take the vacuum solution $u_0=0$ and we know $u_1,u_2$ as kink/anti-kink solutions, so we can write the doubly transformed $u_3$ as:$$\Huge\tan\left(\frac{u_3}{4}\right)=\frac{a_2+a_1}{a_2-a_1}\tan\left(\frac{u_1-2}{4}\right)=\frac{a_2+a_1}{a_2-a_1}\frac{\tan\left(\frac{u_1}{4}\right)-\tan\left(\frac{u_2}{4}\right)}{1+\tan\left(\frac{u_1}{4}\right)\tan\left(\frac{u_2}{4}\right)}$$Recalling the form of the $1$ soliton solution:$$\Huge u=4\arctan\left(e^{\frac{1}{a}x_+-ax_-+C}\right)$$we introduce:$$\Huge \theta_i=\frac{x_+}{a_i}-a_ix_-+c_i=\epsilon_i\gamma_i(x-\bar x_i-v_it)$$which makes the single soliton solutions look like:$$\Huge \tan\left(\frac{u_i}{4}\right)=e^{\theta_i}$$Here, $\bar x_{1,2}$ are the centers of the two solitons at $t=0$. Using these forms, we can write the $2$-soliton solution as:$$\Huge \tan\left(\frac{u_3}{4}\right)=\mu\frac{e^{\theta_1}-e^{\theta_2}}{1+e^{\theta_1+\theta_2}},\,\,\mu =\frac{a_2+a_1}{a_2-a_1}$$
Note that if both solitons have the same velocity $v_1=v_2$ then:$$\Huge \frac{a_1^2-1}{a_1^2+1}=\frac{a_2^2-1}{a_2^2+1}\implies a_1=\pm a_2$$then $\mu=0$ or $\infty$, so the $2$-soliton solution breaks down.

# Asymptotics of multisoliton solutions:

We move on to study this $2$-soliton sine-Gordon solution, however out methodology applies for other solutions with different amount of solitons also. Our goal is to identify two solitons hidden in $u_3$ defined above that occur before and after collision. In order to keep track of solitons, we choose to follow one or the other by introducing:$$\Huge t\to \pm\infty,\,\,X_V=x-Vt$$for some appropriate constant velocity $V$. If there is a soliton moving at velocity $V$ in the original $(x,t)$ coordinates, it will appear stationary in the $(X_V,t)$ coordinates. We call such coordinates the comoving frame for this reason.

We apply this to our $2$-soliton sine-Gordon solution. First we apply our coordinate change to the $\theta_i$ definition:$$\Huge\begin{align*}
\theta_i&=\epsilon_i\gamma_i(x-Vt+Vt-v_it-\bar x_i)\\
&=\epsilon_i\gamma_i(X_V-(v_i-V)t-\bar x_i)
\end{align*}$$where the term $v_i-V$ is known as relative velocity.

For each soliton we now have three cases for the $t\to\pm\infty$ limit:

| Case    | $t\to-\infty$                  | $t\to+\infty$                  |
| ------- | ------------------------------ | ------------------------------ |
| $V<v_i$ | $\theta_i\to+\epsilon_i\infty$ | $\theta_i\to-\epsilon_i\infty$ |
| $V=v_i$ | $\theta_i$ infinite            | $\theta_i$ infinite            |
| $V>v_i$ | $\theta_i\to-\epsilon_i\infty$ | $\theta_i\to+\epsilon_i\infty$ |
Recall that $\epsilon_i=\pm1$ and $\gamma_i>0$ does not affect the sign of $\theta_i$ in the limit. This tells us that if $V\neq v_1,v_2$ then $\theta_1,\theta_2\to\pm\infty$ as $|t|\to\infty$. This implies that:$$\Huge \tan\left(\frac{u}{4}\right)=\mu\frac{e^{\theta_1}-e^{\theta_2}}{1+e^{\theta_1+\theta_2}}\to\pm \infty\text{ or }0$$Which implies that $u/4$ tends to an integer multiple of $\pi/2$ (and therefore $u\to2\pi n$).

If instead $V=v_1$ or $v_2$ we must be more careful in the limit. Consider the case with $a_1,a_2>0$ and $a_1\neq a_2$. We take WLOG:$$\Huge a_2>a_1>0\implies v_2>v_1,\,\,\epsilon_1=\epsilon_2=1,\,\,\mu >0$$
## $V=v_1$:
First considering $V=v_1$, we are "riding" the slower soliton. The comoving frame exponents read:$$\Huge\begin{align*}
\theta_1&=\gamma_1(x-v_1t-\bar x_1)=\gamma_1(X_{v_1}-\bar x_1)\\
\theta_2&=\gamma_2(x-v_2t-\bar x_2)=\gamma_2(X_{v_1}-(v_2-v_1)t-\bar x_2)
\end{align*}$$
So we see that $\theta_1$ stays finite, however $\theta_2\to\mp\infty$ as $t\to\pm\infty$ with $X_{v_1}$ fixed. We now consider each limit:
> $t\to+\infty$ causes $\theta_2\to-\infty$ and therefore $e^{\theta_2}\to0$:$$\Huge\begin{align*}
\tan\left(\frac{u}{4}\right)&=\mu\frac{e^{\theta_1}-e^{\theta_2}}{1+e^{\theta_1+\theta_2}}\\
&\to \mu e^{\theta_1}\\
&=\mu e^{\gamma_1(X_{v_1}-\bar x_1)}\\
&=e^{\gamma_1(x-v_1t-\bar x_1+\frac{1}{\gamma_1}\log\mu)}
\end{align*}$$This is a kink, with the center moving at velocity $v_1$ along the trajectory:$$\Huge x=v_1t+\bar x_1-\frac{1}{\gamma_1}\log\left(\frac{a_2+a_1}{a_2-a_1}\right)$$The last term here is negative and represents a backwards shift in space of the slower soliton due to the faster soliton.
> Now we consider $t\to-\infty$. In this limit $\theta_2\to+\infty$ so $e^{\theta_2}\to+\infty$:$$\Huge\begin{align*}
\tan\left(\frac{u}{4}\right)&=\mu\frac{e^{\theta_1}-e^{\theta_2}}{1+e^{\theta_1+\theta_2}}\\
&=\mu\frac{e^{\theta_1-\theta_2}-1}{e^{-\theta_2}+e^{\theta_1}}\\
&\to-\mu e^{-\theta_1}
\end{align*}$$Recalling that $\tan(A\pm\pi/2)=-1/\tan A$ we have:$$\Huge\begin{align*}
\tan\left(\frac{u}{4}\pm\frac{\pi}{2}\right)&\to\mu^{-1}e^{\theta_1}\\
&=e^{\gamma_1(x-v_1t-\bar x_1-\frac{1}{\gamma_1}\log\mu)}\\
\implies u|_{t\to-\infty,X_{v_1}\text{ finite}}&\approx\pm2\pi+4\arctan e^{\gamma_1(x-v_1t-\bar x_1-\frac{1}{\gamma_1}\log\mu)}
\end{align*}$$This is a kink moving with velocity $v_1$ along:$$\Huge x=v_1t+\bar x_1+\frac{1}{\gamma}\log\left(\frac{a_2+a_1}{a_2-a_1}\right)$$where the last term is positive, representing a forward shift due to the faster soliton.

Comparing the trajectories at $t\to-\infty$ and $t\to+\infty$ we see that the collision with the faster soliton shifts the slower soliton by:$$\Huge \text{PHASE SHIFT}_\text{slower}=-\frac{2}{\gamma_1}\log\left(\frac{a_2+a_1}{a_2-a_1}\right)$$We conclude by saying that the slower kink emerges from collision with the same shape and velocity, but delayed by a finite phase shift.

## $V=v_2$:
Now we consider $V=v_2$, riding the faster soliton. The details are similar to the above, however we find that even though $a_2>0$ (kink-producing), the component of the two-soliton solution that moves with velocity $v_2$ is actually an anti-kink. The shifts have opposite signs:$$\Huge\text{PHASE SHIFT}_\text{faster}=+\frac{2}{\gamma_2}\log\left(\frac{a_2+a_1}{a_2-a_1}\right)$$
We then get the following behaviour for the kink/anti-kink solution:![[Backlund transformations 2025-11-25 14.23.19.excalidraw]]
We see that the kink/anti-kink appear to accelerate towards each other near to collision. To explore this idea, consider a kink/kink interaction:![[Backlund transformations 2025-11-25 14.30.25.excalidraw]]
This leads to the conclusion that solitons with like topological charges repel, whereas solitons with opposite topological charges attract.

# The breather:

Recall the formula for the general $2$-soliton solution:$$\Huge u=4\arctan\left(\frac{a_2+a_1}{a_2-a_1}\frac{e^{\theta_1}-e^{\theta_2}}{1+e^{\theta_1+\theta_2}}\right)$$This is a solution to the sine-Gordon equation for any value of the Backlund parameters $a_1,a_2$. Note that while these parameters can be complex, we require that $u$ must be real as it represents a physical quantity. There are two ways to achieve this:
> $a_1,a_2\in\Re$ is what we have considered thus far
> $a_2=a_1^*$ is what we will consider next. We must first check that this corresponding field $u$ is real:$$\Huge\begin{align*}
u^*&=\left(4\arctan\left(\frac{a_2+a_1}{a_2-a_1}\frac{e^{\theta_1}-e^{\theta_2}}{1+e^{\theta_1+\theta_2}}\right)\right)^*\\
&=4\arctan\left(\frac{a_2^*+a_1^*}{a_2^*-a_1^*}\frac{e^{\theta_1^*}-e^{\theta_2^*}}{1+e^{\theta_1^*+\theta_2^*}}\right)\\
&=4\arctan\left(\frac{a_1+a_2}{a_1-a_2}\frac{e^{\theta_2}-e^{\theta_1}}{1+e^{\theta_2+\theta_1}}\right)\\
&=4\arctan\left(\frac{a_2+a_1}{a_2-a_1}\frac{e^{\theta_1}-e^{\theta_2}}{1+e^{\theta_1+\theta_2}}\right)=u
\end{align*}$$

We proceed by considering the second option with some arbitrary $a_1=a_2^*=a$ with $c_1=c_2=0$:$$\Huge\begin{align*}
a_1&=a=A+iB=|a|e^{i\varphi},\,\,\theta_1=\alpha+i\beta\\
a_2&=\bar a=A-iB=|a|e^{-i\varphi},\,\,\theta_2=\alpha-i\beta
\end{align*}$$where $\alpha,\beta$ are real functions of $x,t$. Then we have:$$\Huge\begin{align*}
\tan\left(\frac{u}{4}\right)&=\frac{|a|(e^{-i\varphi}+e^{i\varphi})}{|a|(e^{-i\varphi}-e^{i\varphi})}\frac{e^{\alpha+i\beta}-e^{\alpha-i\beta}}{1+e^{2\alpha}}\\
&=\frac{2\cos\varphi}{-2i\sin\varphi}\frac{2i\sin\beta}{2\cosh\alpha}\\
&=-\frac{\cos\varphi}{\sin\varphi}\frac{\sin\beta}{\cosh\alpha}
\end{align*}$$To finish the calculation, we write $\alpha,\beta$ in terms of the coordinates $x,t$ and parameters $|a|,\varphi$:$$\Huge\begin{align*}
\alpha+i\beta&=\frac{1}{a}x^+-ax^-\\
&=\frac{a^*}{|a|^2}x^+-ax^-\\
&=\frac{A-iB}{|a|^2}x^+-(A+iB)x^-\\
\implies \alpha=\Re(\theta_1)&=\frac{A}{|a|^2}x^+-Ax^-\\
&=\frac{A}{|a|}\left(\frac{1}{|a|}x^+-|a|x^-\right)
\end{align*}$$We can show that this is equal to the following:$$\Huge \alpha=\frac{A}{|a|}\gamma(x-vt)=\cos\varphi\cdot\gamma(x-vt)$$where $v=\frac{|a|^2-1}{|a|^2+1}$ and $\gamma=\frac{1}{\sqrt{1-v^2}}=\frac{1+|a|^2}{2|a|}$. Similarly, one can show that:$$\Huge \beta=\frac{B}{|a|}\gamma(vx-t)=\sin\varphi\cdot(vx-t)$$Substituting these in for our solution gives us the breather solution:$$\Huge \tan\left(\frac{u}{4}\right)=-\cot\varphi\cdot\frac{\sin(\sin\varphi\cdot\gamma(vx-t))}{\cosh(\cos\varphi\cdot\gamma(x-vt))}$$Remarks:
> Here, the ratio of the prefactor and the denominator define an envelope function moving with group velocity $v$.
> The numerator defines a carrier wave moving at phase velocity $1/v$.

Considering $|a|=1$, the breather solution reduces to:$$\Huge \tan\left(\frac{u}{4}\right)=\cot\varphi\cdot\frac{\sin(\sin\varphi\cdot t)}{\cosh(\cos\varphi\cdot x)}$$and the field it defines looks like a bouncing (or breathing!) bound state of a kink and an anti-kink with time period $\tau=2\pi/|\sin\varphi|$:![[Backlund transformations 2025-12-04 17.43.53.excalidraw]]
One can show that this breather has energy $E_\text{breather}=16\cos\varphi$. Since a static kink and a static anti-kink have energy $E_\text{kink}=E_\text{antikink}=8$, the binding energy of the kink and the anti-kink in the breather is:$$\Huge E_\text{binding}=E_\text{breather}-E_\text{kink}-E_\text{antikink}=-16(1-\cos\varphi)$$This is negative as expected, the binding lowers the energy of the solution.

As $\varphi\to0$, the binding energy tends to $0$. It is immediate to see that this limit causes $\tau\sim1/|\varphi|\to\infty$. The spatial size of the breather also diverges, $x_\text{max}\sim-\log|\varphi|\to\infty$. In this limit, the kink/anti-kink becomes loosely bound, resulting in the solution:$$\Huge u=4\arctan(t\text{ sech}(x))$$which describes a kink and anti-kink starting infinitely far away from one another and doing half an oscillation. Since $\text{sech}(x)\approx2e^{-|x|}$ as $|x|\to\infty$, the kink and anti-kink do not follow linear trajectories as $t\to\pm\infty$. Instead they follow asymptotic trajectories, given by $|x|\sim-\log|t|$.