# Problem 7.1:

Assuming that the charged particle is a proton, we have that $q=1.602\times10^{-19}C$ and $m=1.672\times10^{-27}kg$. Then, assuming $B=1$ tesla:$$\Huge \nu=\frac{qB_z}{2\pi m}=\frac{1.602\times 10^{-19}\times 1}{2\pi\times1.672\times10^{-27}}\approx1.525\times10^7hz$$Now we compute the speed of the proton, assuming it has an initial kinetic energy of $100$ keV. We have:$$\Huge\begin{align}
\frac{mv^2}{2}&=q\times10^3\text{eV}\\
v^2&=\frac{2q\times10^3\text{eV}}{m}\\
v&=\sqrt{\frac{2q\times10^3\text{eV}}{m}}=\sqrt{\frac{2\times1.602\times10^{-19}C\times10^3\text{eV}}{1.672\times10^{-27}kg}}\\
&\approx4.378\times10^5ms^{-1}
\end{align}$$The radius of the proton's trajectory can then be calculated, using the fact that the norm of the speed vector is given by:$$\Huge\begin{align}
V&=2\pi R\nu\\
R&=\frac{V}{2\pi\nu}=\frac{4.378\times10^5ms^{-1}}{2\pi\times1.525\times10^7hz}\\
&\approx4.569\times10^{-3}m=4.569\,mm
\end{align}$$

# Problem 7.2:

We have $m\ddot x=q(E_x+\dot yB_z)$ and $m\ddot y=q(E_y-\dot xB_z)$. We must rearrange these equations so that each contains the derivatives of only one variable. To do this, we first solve for $(\dot x,\dot y)$:$$\Huge \dot y=\frac{m\ddot x-qE_x}{qB_z},\,\,\dot x=\frac{m\ddot y-qE_y}{qB_z}$$Now substituting these into each other gives:$$\Huge\begin{align}
m\frac{d }{dt}\left(\frac{m\ddot y-qE_y}{qB_z}\right)&=q(E_x+\dot yB_z)\\
\frac{m^2}{qB_z}\dddot y&=q(E_x+\dot yB_z)\\
\dddot y&=\frac{q^2B_z(E_x+\dot yB_z)}{m^2}\\
&=\left(\frac{q}{m}\right)^2B_zE_x+\left(\frac{qB_z}{m}\right)^2\dot y
\end{align}$$Similarly, one can show that:$$\Huge \dddot x=\left(\frac{q}{m}\right)^2B_zE_y-\left(\frac{qB_z}{m}\right)^2\dot x$$So our equations now only involve constants and derivatives of the same variable. We proceed by denoting $\underline g(t)=\begin{pmatrix}-v_x\\v_y\end{pmatrix}=\begin{pmatrix}-\dot x\\\dot y\end{pmatrix}$. Our system of equations then becomes:$$\Huge \ddot v_x=\left(\frac{q}{m}\right)^2B_zE_y+\left(\frac{qB_z}{m}\right)^2(-v_x),\,\,\ddot v_y=\left(\frac{q}{m}\right)^2B_zE_x+\left(\frac{qB_z}{m}\right)^2v_y$$Which can be written as:$$\Huge \frac{d \underline g(t)}{dt}=\left(\frac{q}{m}\right)^2B_z\begin{pmatrix}E_y\\E_x\end{pmatrix}+\left(\frac{qB_z}{m}\right)^2\underline g(t)$$So, finally, we get the following first order ODEs:$$\Huge\begin{align}
\frac{d v_x}{dt}&=\left(\frac{q}{m}\right)^2B_zE_y-\left(\frac{qB_z}{m}\right)^2v_x\\
\frac{d v_y}{dt}&=\left(\frac{q}{m}\right)^2B_zE_x+\left(\frac{qB_z}{m}\right)^2v_y\\
\frac{dx}{dt}&=v_x\\
\frac{dy}{dt}&=v_y
\end{align}$$As required.