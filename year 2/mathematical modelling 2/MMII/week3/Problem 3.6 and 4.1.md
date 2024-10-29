
# Problem 3.6:

$\Delta T$ is likely to reach $1.5$ in the year $2056$

The parameter $a$ represents the amount of temperature the Earth will change by without the effects of time

The parameter $b$ represents the increased amount of temperature the Earth will change by due to the human influences that year

![[Figure_1.png]]

# Problem 4.1:

$$\Huge \frac{d N}{dt}=R_0N\exp{(-R_1N)}-\frac{Y}{2}\left(1+\tanh \left(\frac{N-N_h}{K}\right) \right)$$
Require $R_0N=\hat N$ and $-R_1N=-\hat R_1\hat N$. This implies $N=\frac{1}{R_0}\hat N$ and $R_1=\frac{\hat R_1\hat N}{N}=\frac{\hat R_1\hat N}{\frac{1}{R_0}\hat N}=R_0\hat R_1$. So we have the first two changes of variables, $N=\frac{1}{R_0}\hat N$ and $R_1=R_0\hat R_1$. 

Now $\frac{d}{dt}(N)=\frac{d}{dt}(\frac{1}{R_0}\hat N)=\frac{1}{R_0}\frac{d\hat N}{dt}$. We require that this is equal to $\frac{d\hat N}{d\hat t}$ so let $t=(1/R_)$  