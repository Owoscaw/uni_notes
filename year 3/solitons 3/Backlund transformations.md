
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

We take the vacuum solution $u_0=0$ and we know $u_1,u_2$ as kink/anti-kink solutions, so we can write the doubly transformed $u_3$ as:$$$$