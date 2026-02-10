
Our linearised governing equations for the [[Instability#The Rayleigh-Taylor instability|Rayleigh-Taylor instability]] are given by:$$\Huge\begin{align*}
\underline{\nabla}^2\phi_1&=\underline{\nabla}^2\phi_2=0\\
\phi_1,\phi_2&\rightarrow0,\,\,z\to\pm\infty\\
\frac{\partial \eta}{\partial t}&=\frac{\partial \phi_1}{\partial z}=\frac{\partial \phi_2}{\partial z},\,\,z=0\\
\rho_1\frac{\partial \phi_1}{\partial t}+\rho_1g\eta&=\rho_2\frac{\partial \phi_2}{\partial }+\rho_2g\eta,\,\,z=0
\end{align*}$$Which we solve to find:$$\Huge\begin{align*}
\phi_1(x,z,t)&=Ae^{-kz}e^{i(kx-\omega t)}\\
\phi_2(x,z,t)&=Ae^{kz}e^{i(kx-\omega t)}\\
\eta(x,t)&=\frac{kA}{i\omega}e^{i(kx-\omega t)}\\
\omega&=\pm i\sqrt{\frac{\rho_1-\rho_2}{\rho_1+\rho_2}}gk
\end{align*}$$And so we get two cases:
> $\omega\in\Re$, which implies:$$\Huge \frac{\rho_1-\rho_2}{\rho_1+\rho_2}>0\implies\rho_1>\rho_2$$
> $\omega\notin\Re$, which implies:$$\Huge \frac{\rho_1-\rho_2}{\rho_1+\rho_2}<0\implies\rho_1<\rho_2$$