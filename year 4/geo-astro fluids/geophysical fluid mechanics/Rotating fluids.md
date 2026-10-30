
Consider a fluid in two different frames:$$\Large\begin{aligned}
I&:&\{\underline{e}_1,\underline{e}_2,\underline{e}_3\}\\
R&:&\{\hat{\underline{e}}_1,\hat{\underline{e}}_2,\hat{\underline{e}}_3\}
\end{aligned}$$Here, $R$ is rotating with angular velocity $\underline{\Omega}$ relative to $I$. Defining $\left(\frac{d}{dt}\right)_I$ as the time derivative in the inertial frame $I$, we see that:$$\Large\begin{aligned}
\left(\frac{d\underline{e}_i}{dt}\right)_I&=0\\
\left(\frac{d\hat{\underline{e}}_i}{dt}\right)_I&\neq0 
\end{aligned}$$
Now consider a vector of constant length $\underline{C}$ rotating relative to the inertial frame with angular velocity $\underline{\Omega}$. Over a small interval of time $\delta t$, $\underline{C}$ rotates through an angle of $\delta\lambda$:![[Rotating fluids 2026-10-30 16.37.41.excalidraw]]It is clear that the change in $\underline{C}$, $\delta\underline{C}$ is then given by:$$\Large\begin{aligned}
\delta\underline{C}&=|\underline{C}|\sin(\gamma)\delta\lambda\underline{e}_n\\
&=|\underline{C}||\underline{\Omega}|\sin\gamma\,\delta t\underline{e}_n\\
&=\underline{\Omega}\times\underline{C}\,\delta t\\
\implies\left(\frac{d\underline{C}}{dt}\right)_I&=\underline{\Omega}\times\underline{C}
\end{aligned}$$This holds for any constant magnitude vector in the inertial frame. 

Let us consider a general vector with changing magnitude:$$\Large\underline{B}=B_1(t)\hat{\underline{e}}_1+B_2(t)\hat{\underline{e}}_2+B_3(t)\hat{\underline{e}}_3$$Since we define the vector in our rotating frame, it follows that:$$\Large \left(\frac{d\underline{B}}{dt}\right)_R=\frac{dB_i}{dt}\hat{\underline{e}}_i$$In the inertial frame, we have:$$\Large\begin{aligned}
\left(\frac{d\underline{B}}{dt}\right)_I&=\frac{d}{dt}(B_i(t)\hat{\underline{e}}_i)\\
&=\frac{dB_i}{dt}\hat{\underline{e}}_i+B_i\left(\frac{d\hat{\underline{e}}_i}{dt}\right)_I
\end{aligned}$$