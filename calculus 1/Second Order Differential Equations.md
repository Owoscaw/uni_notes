
# Linear constant coefficient ODEs:

The general form of a second order constant coefficient linear ODE is:$$\Huge \alpha_2y''+\alpha_1y'+\alpha_0=\phi(x)$$
## Linear constant coefficient homogeneous ODEs:

Where $\alpha_2\neq0$, $\alpha_1,\alpha_0$ are constants, and $\phi(x)$ is an arbitrary function of $x$. If $\phi(x)=0$, then the ODE is homogeneous. If this has two solutions $y_1(x)$ and $y_2(x)$, then so is the arbitrary linear combination:$$\Huge y(x)=Ay_1(x)+By_2(x)$$
This is because:$$\Huge \alpha_2y''+\alpha_1y'+\alpha_0=\alpha_2(Ay''+By'')+\alpha_1(Ay'+By')+(Ay+By)$$
Collecting terms shows:$$\Huge A(\alpha_2y''+\alpha_1y'+\alpha_0)+B(\alpha_2y''+\alpha_1y'+\alpha_0)=0$$$$\Huge A(0)+B(0)=0\,\text{is true}$$
The general solution to this differential equation will have two arbitrary constants, as it is second order. If $y_1$ and $y_2$ are any two independent particular solutions, then $y=Ay_1+By_2$ is a general solution, with $A$ and $B$ representing these two arbitrary constants. Solutions can be found by looking for a solution with $y=e^{\lambda x}$. Substituting this, we get:$$\Huge \alpha_2\lambda^2e^{\lambda x}+\alpha_1\lambda e^{\lambda x}+\alpha_0e^{\lambda x}=0$$
Since $e^{\lambda x}$ will never have any zeros, we can divide through by it to get the characteristic (auxiliary) equation:$$\Huge \alpha_2\lambda^2+\alpha_1\lambda+\alpha_0=0$$
This will either have one, two, or zero solutions depending on $\alpha_2,\alpha_1,\alpha_0$:
> If the equation has two real roots, $\lambda_1$ and $\lambda_2$, then solutions are $y_1=e^{\lambda_1x}$ and $y_2=e^{\lambda_2x}$. Then the general solution becomes:$$\Huge y=Ae^{\lambda_1x}+Be^{\lambda_2x}$$
> If the equation has one real root, then the auxiliary equation is of form $\alpha_1^2-4\alpha_2\alpha_0=0$. In this case, we get $\alpha_2(\lambda+\frac{\alpha_1}{2\alpha_2})^2=0$ for the auxiliary equation, so the double root is $\lambda=-\frac{\alpha_1}{2\alpha_2}$. We have one solution $y_1=e^{\lambda_1x}$, however also $y_2=xe^{\lambda_1x}$ is also a solution. So the general solution becomes:$$\Huge y=Ae^{\lambda x}+Bxe^{\lambda x}$$
> If the equation has two complex conjugate solutions, that is $\lambda_1=a+bi$ and $\lambda_2=a-bi$, then we have two solution $y_1=e^{ax+bix}=e^{ax}e^{ibx}$ and $y_2=e^{ax-bix}=e^{ax}e^{-bix}$. These suck because they are complex functions, and we want real solutions. Since any linear combination of these gives a solution, consider:$$\Huge Y_1=\frac{1}{2}(y_1+y_2)=\frac{1}{2}e^{ax}(e^{i(bx)}+e^{-i(bx)})=e^{ax}cos(bx)$$$$\Huge Y_2=\frac{1}{2}(y_1-y_2)=\frac{1}{2}e^{ax}(e^{i(bx)}-e^{-i(bx)})=e^{ax}sin(bx)$$These are two independent real solutions, so the general solution can be expressed as a linear combination of both, that is:$$\Huge y=e^{ax}(Acos(bx)+Bsin(bx))$$With arbitrary real constants $A$ and $B$, with real $a,b$ satisfying $\lambda=a\pm bi$ for the auxiliary equation.

## Inhomogeneous case, $\phi(x)\neq 0$:

A general solution to this will contain two arbitrary constants. The general solution takes form:$$\Huge y=y_{CF}+y_{PI}$$
Where $y_{CF}$ is the complementary function, equivalent to the general solution to the associated homogeneous ODE above. Then $y_{PI}$ is known as the particular integral. We have $y'=y_{CF}'+y_{PI}'$, and $y''=y_{CF}''+y_{PI}''$, so subtituting we get:$$\Huge \alpha_2(y_{CF}''+y_{PI}'')+\alpha_1(y_{CF}'+y_{PI}')+\alpha_0(y_{CF}+y_{PI})=\phi(x)$$$$\Huge (\alpha_2y_{CF}''+\alpha_1y_{CF}'+\alpha_0y)+(\alpha_2y_{PI}''+\alpha_1y_{PI}'+\alpha_0y_{PI})=0+\phi(x)=\phi(x)$$When $\phi(x)$ takes the form of a polynomial, exponential, trigonometric function, or a sum/product of these, we can apply the method of undetermined coefficients (guessing):

| Term in $\phi(x)$ | Form of $y_{PI}$                    |
| ----------------- | ----------------------------------- |
| $e^{\gamma x}$    | $a_1e^{\gamma x}$                   |
| $x^n$             | $a_0+a_1x+\dots+a_nx^n$             |
| $cos(\gamma x)$   | $a_1cos(\gamma x)+a_2sin(\gamma x)$ |
| $sin(\gamma x)$   | $a_1cos(\gamma x)+a_2sin(\gamma x)$ |

