
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

Firstly, we rewrite the sine-Gordon equation by changing variables to [[year 3/solitons 3/Conservation laws#Relativistic field equations|light-cone]] coordinates:$$\Huge x_+=\frac{1}{2}(t+x),\,\,x_-=\frac{1}{2}(t-x)$$Recall we found the form of the derivative operator:$$\Huge\frac{\partial^2}{\partial x_+\partial x_-}=\frac{\partial^2}{\partial t^2}-\frac{\partial^2}{\partial x^2}$$making the sine-Gordon equation:$$\Huge u_{+-}=-\sin u$$We then define the BT:$$\Huge\begin{align*}
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