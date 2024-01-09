
A particle on the $x$ axis can have its position described by a function $x(t)$ where $t$ denotes time. The velocity of this particle can be described by the time derivative of it's position, that is $v(t)=\dot x$. Here, $\cdot$ denotes $\frac{d}{dt}$. Similarly, the acceleration of the particle is described by the time derivative of it's velocity, $\ddot x(t)$.

The particle also has a property, mass ($m>0$). Then the momentum of this particle is given by $p=m\dot x$. When a force $F$ is applied, then $x(t)$ satisfied the equation of motion:$$\Huge \dot p=F=\frac{d}{dt}\left(m\dot x\right)=m\ddot x=ma$$Where $a$ is the acceleration of the particle. Unless otherwise stated, mass is assumed to be constant. The force applied is not always a constant function, so the more general case is given as:$$\Huge m\ddot x=F(t,x,\dot x)$$This cannot explicitly be solved in general, so special cases are focused on. 

## Motion under gravity:

Close to the surface of a planet, considering vertical motion then the force has magnitude $|F|=mg$, where $g$ is a constant depending on the planet. Taking the case where $x$ is the upwards direction under gravity, we have:$$\Huge F=-mg=m\ddot x\implies\ddot x=-g$$This has initial conditions $x(0)=0$ and $\dot x(0)=u$. Integrating twice wrt to $t$ gets:$$\Huge x=-\frac{1}{2}gt^2+ut+0$$This can be used in many problems relating to motion under gravity.

# Cases $F=F(t)$ and $F=F(\dot x)$:

## $F=F(t)$:

For a constant force, integrating wrt $t$ twice gives the solution. For example consider a unit mass particle lying at rest at $x=0$. A force $F=e^{-t}$ is applied at $t=0$. We have $\ddot x=e^{-t}$. Integrating this gives $\dot x=-e^{-t}+c_1$, then $x=e^{-t}+c_1t+c_2$. Applying initial conditions shows that $c_1=1$ and $c_2=-1$. Therefore the solution to this example is $x=e^{-t}+t-1$.

## $F=F(\dot x)$:

With this case, we have $m\ddot x=F(\dot x)$. This is a non-linear [[Second Order Differential Equations#Linear constant coefficient ODEs|differential equation]]. Renaming $v=\dot x$, we get $m\dot v=F(v)$. This is now a [[First order differential equations#Separable ODEs|seperable first order differential equation]]. Separating variables to get $v(t)$ and then integrating wrt $t$ gives the solution in the form $x(t)$.