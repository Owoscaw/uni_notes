A function $\underline f:\Re^n\mapsto\Re^m$ is [[Differentiable Functions|differentiable]] at a point $\underline x\in\Re^n$ if there exists an $m\times n$ [[Matrix definition|matrix]] $M\in M_{m\times n}(\Re)$ and a map $\underline R:\Re^n\mapsto\Re^m$ such that:$$\Huge \underline f(\underline x+\underline h)=\underline f(\underline x)+M\underline h+\underline R(\underline h)$$Such that for all $\underline h\in\Re^n$:$$\Huge \lim_{\underline h\to\underline 0}\frac{\underline R(\underline h)}{|\underline h|}=\underline 0$$That is to say that $\underline f$ is differentiable at a point if locally, it behaves like some linear map. If such a matrix $M$ exists, it is called the total derivative of $\underline f$. Take for example the vector field $\underline f:\Re^2\mapsto\Re^2$ with $\underline f(x,y)=(x-y)\underline e_1+(x+2y)\underline e_2$ at the point $\underline x=(2,1)$. For any $\underline h\in\Re^2$:$$\Huge\begin{align} 
\underline f(\underline x+\underline h)&=f(2+h_1,1+h_2)\\
&=\begin{pmatrix}2+h_1-(1+h_2)\\2+h_1+2(1+h_2)\end{pmatrix}\\
&=\begin{pmatrix}1\\4\end{pmatrix}+\begin{pmatrix}h_1-h_2\\h_1+2h_2\end{pmatrix}\\
&=\begin{pmatrix}1\\4\end{pmatrix}+\begin{pmatrix}1&-1\\1&2\end{pmatrix}\underline h
\end{align}$$So a matrix $M=\begin{pmatrix}1&-1\\1&2\end{pmatrix}$ exists and $\underline R(\underline h)=\underline 0$ so the remainder condition is satisfied and the vector field is differentiable at $(2,1)$.

If $\underline f:\Re^n\mapsto\Re^m$ is differentiable, then the derivative $M$ is given by the Jacobian matrix:$$\Huge J_{\underline f}=\begin{pmatrix}\underline{\frac{\partial \underline f}{\partial x_1}}&\dots&\underline{\frac{\partial \underline f}{\partial x_n}}\end{pmatrix}=\begin{pmatrix}\frac{\partial f_1}{\partial x_1}&\frac{\partial f_1}{\partial x_2}&\dots&\frac{\partial f_1}{\partial x_n}\\\frac{\partial f_2}{\partial x_1}&\frac{\partial f_2}{\partial x_2}&\dots&\frac{\partial f_2}{\partial x_n}\\\vdots&\vdots&\ddots&\vdots\\\frac{\partial f_m}{\partial x_1}&\frac{\partial f_m}{\partial x_2}&\dots&\frac{\partial f_m}{\partial x_n}\end{pmatrix}$$To prove this, suppose that $\underline h=h\underline e_j$ for some cartesian [[Vector space definitions#Zero vector and Standard Basis vectors|basis]] vector $\underline e_j$. Then since $\underline f$ is differentiable at $\underline x$:$$\Huge\begin{align}
\lim_{\underline h\to\underline 0}\frac{\underline R(\underline h)}{|\underline h|}=0&\iff\lim_{\underline h\to\underline 0}\frac{1}{|\underline h|}(\underline f(\underline x+h\underline e_j)-\underline f(\underline x)-M(h\underline e_j))=0\\
&\iff\lim_{h\to 0}\frac{1}{h}(\underline f(\underline x+h\underline e_j)-\underline f(\underline x))-\lim_{h\to 0}M\underline e_j=0\\
&\iff\frac{\partial \underline f}{\partial x_j}(\underline x)-M\underline e_j=0\\
&\iff M_{ij}=\frac{\partial f_i}{\partial x_j}
\end{align}$$For $i\in\{1,\dots,n\}$ and $j\in\{1,\dots,m\}$


