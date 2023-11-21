
# Linear constant coefficient ODEs:

The general form of a second order constant coefficient linear ODE is:$$\Huge \alpha_2y''+\alpha_1y'+\alpha_0=\phi(x)$$
Where $\alpha_2\neq0$, $\alpha_1,\alpha_0$ are constants, and $\phi(x)$ is an arbitrary function of $x$. If $\phi(x)=0$, then the ODE is homogeneous. If this has two solutions $y_1(x)$ and $y_2(x)$, then so is the arbitrary linear combination:$$\Huge y(x)=Ay_1(x)+By_2(x)$$
This is because:$$\Huge \alpha_2y''+\alpha_1y'+\alpha_0=\alpha_2(Ay''+By'')+\alpha_1(Ay'+By')+(Ay+By)$$
Collecting terms shows:$$\Huge A(\alpha_2y''+\alpha_1y'+\alpha_0)+B(\alpha_2y''+\alpha_1y'+\alpha_0)=0$$$$\Huge A(0)+B(0)=0\,\text{is true}$$
The general solution to this differential equation will have two arbitrary constants, as it is second order. If $y_1$ and $y_2$ are any two independent particular solutions, then $y=Ay_1+By_2$ is a general solution, with $A$ and $B$ representing these two arbitrary constants. Solutions can be found by looking for a solution with $y=e^{\lambda x}$. Substituing this, we get:$$\Huge \alpha_2\lambda^2e^{\lambda x}+\alpha_1\lambda e^{\lambda x}+\alpha_0e^{\lambda x}=0$$
Since $e^{\lambda x}$ will never have any zeros, we can divide through by it to get the characteristic (auxiliary) equation:$$\Huge \alpha_2\lambda^2+\alpha_1\lambda+\alpha_0=0$$
This will either have one, two, or zero solutions depending on $\alpha_2,\alpha_1,\alpha_0$:
> If the equation has two real roots, $\lambda_1$ and $\lambda_2$, then solutions are $y_1=e^{\lambda_1x}$ and $y_2=e^{\lambda_2x}$