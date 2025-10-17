In order for a car traveling at $v\text{ms}^{-1}$ to come to complete rest at a maximal rate of deceleration $a_\text{max}$, we require:$$\Huge \frac{0-v}{\Delta t}=-a_\text{max}\implies\Delta t=\frac{v}{a_\text{max}}$$The car will take $\Delta t$ time to stop, given as above. To find the distance the car travels in this time, observe:$$\Huge \ddot x=-a_\text{max}\implies \dot x=-a_\text{max}t+v\implies x=\int_{t_0}^{t_1}-a_\text{max}t+v\,dt$$Now we are interested in the distance travelled between $t_0=0$ and $t_1=\Delta t$:$$\Huge\begin{align}
\Delta x&=\int_{0}^{\Delta t}-a_\text{max}t+v\,dt\\
&=\left[-\frac{1}{2}a_\text{max}t^2+vt\right]_{0}^{\Delta t}\\
&=-\frac{1}{2}a_\text{max}(\Delta t)^2+v\Delta t\\
&=-\frac{1}{2}a_\text{max}\frac{v^2}{a_\text{max}^2}+\frac{v^2}{a_\text{max}}\\&=\frac{v^2}{2a_\text{max}}
\end{align}$$Assuming the cars are spaced $\Delta x$ apart, we can compute the flow past a fixed point on the road:$$\Huge\begin{align}
q&=\frac{v_0}{\Delta L}=\frac{v_0}{\Delta x+l_c}\\
&=\frac{v_0}{\frac{v_0^2}{2a_\text{max}}+l_c}\\
&=\frac{2v_0a_\text{max}}{v_0^2+2l_ca_\text{max}}
\end{align}$$Setting $a_\text{max}=5\text{ms}^{-2}$ and $l_c=5\text{m}$ we can plot $q$ as a function of $v_0$:![[8.1.png]]