
Most problems evolve continuously with time, so instead of finite difference equations, we aim to solve differential equations that take the general form:$$\Huge \frac{d N}{dt}=F(t,N)$$One such model is the Schaefer Model:$$\Huge \frac{d N}{dt}=RN\left(1-\frac{N}{K}\right)-Y(t)$$Where $R$ is the rate at which a population increases, $K$ is the saturation population, and $Y(t)$ is some function describing the rate of population decrease, i.e. how many fish are caught. This model has $3$ parameters. 

# Parameter reduction

The amount of parameters can be reduced with a method called parameter rescaling, where each parameter is rewritten as a product of suitable parameters and constants. For example, letting $N=K\hat N,t=\frac{\hat t}{R},Y(t)=KR\hat Y(t)$ we get:$$\Huge KR \frac{d \hat N}{dt}=RK\hat N(1-\hat N)-KR\hat Y(t)$$$$\Huge \frac{d \hat N(\hat t)}{d \hat t}=\hat N(\hat t)(1-\hat N(\hat t))-\hat Y(t)$$Now the model only depends on $\hat Y(\hat t)$. These parameter and functions are now dimensionless. Reversing the change of variables makes the model dimension-full.

# Euler method:

To solve an equation in general form, we consider the [[Taylor series#Taylor's theorem|Taylor expansion]] of $N(t)$ at time $t_0$:$$\large N(t_0+dt)=N(t_0)+dt\frac{dN}{dt}(t_0)+\mathcal{O}((dt)^2)=N(t_0)+dtF(t_0,N(t_0))+\mathcal{O}((dt)^2)$$Ignoring terms quadratic in $dt$, we see that:$$\Huge N_i=N(t_0+idt)$$Knowing $N_0=N(t_0)$, we can solve the general equation recursively:$$\Huge N_{i+1}\approx N_i+dtF(t_i,N(t_i))$$Where $dt$ is the integration time step. Practically, taking a small value for $dt$ results in high accuracy, but slow runtime. Conversely, taking a large value for $dt$ results in poor accuracy but fast runtime.

# Lotka-Voltera model:

Some models have several populations for example:$$\Huge \frac{d N}{dt}=N(t)(a-bP(t)),\,\,\frac{d P}{dt}=P(t)(cN(t)-d)$$The method for numerically solving these is the same, however instead of thinking of $N$ as a scalar, the tuple $(N,P)$ needs to be thought of as a vector and solved for accordingly.