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
\end{align}$$For $i\in\{1,\dots,n\}$ and $j\in\{1,\dots,m\}$. For a scalar field, the derivative matrix becomes:$$\Huge J_f=(\underline{\nabla}f)^T$$Where [[Differential operators|$\underline{\nabla}$]] represents the gradient operator. 

We can use the derivative matrix to find a linear approximation near $\underline x=(2,-1,3)$ for $\underline f:\Re^3\mapsto\Re^2$ given by $\underline f(x,y,z)=\begin{pmatrix}xy^2-x^2z\\3xy+z^3\end{pmatrix}$:$$\Huge\begin{align}
J_{\underline f}&=\begin{pmatrix}\frac{\partial \underline f}{\partial x}&\frac{\partial \underline f}{\partial y}&\frac{\partial \underline f}{\partial z}\end{pmatrix}=\begin{pmatrix}y^2-2xz&2xy&-x^2\\3y&3x&3z^2\end{pmatrix}\\
\underline f(\underline x+\underline h)&\simeq\underline f(\underline x)+J_{\underline f}(\underline x)\underline h\\
&=\underline f(2,-1,3)+\begin{pmatrix}-10-11h_1-4h_2-4h_3\\21-3h_1+6h_2+27h_3\end{pmatrix}
\end{align}$$This is called the linearisation of $\underline f$ around the point $\underline x$.

# Continuous differentiability:

The existance of $J_{\underline f}$ does not imply that $\underline f$ is differentiable. We show this in an example:

The scalar field $f:\Re^2\to\Re$ with $f(x,y)=x^{\frac{1}{3}}y^{\frac{1}{3}}$ is not differentiable at $(0,0)$. We consider whether $J_{\underline f}$ exists at $(0,0)$ using the limit definition:$$\Huge \frac{\partial f}{\partial x}(0,0)=\lim_{h\to 0}\frac{f(h,0)-f(0,0)}{h}=\lim_{h\to0}\frac{h^{\frac{1}{3}}\cdot0-0}{h}=0$$And, varying the $y$ coordinate gives:$$\Huge \frac{\partial f}{\partial y}(0,0)=\lim_{h\to0}\frac{f(0,h)-f(0,0)}{h}=\lim_{h\to0}\frac{h^{\frac{1}{3}}\cdot0-0}{h}=0$$So we have that $J_{f}(0,0)=(0,0)$ indeed exists. To disprove differentiability we need to find some sequence $\underline h\to\underline 0$ where the remainder does not vanish at a fast enough rate. We try a diagonal path to the origin defined as $\underline h=h(\underline e_1+\underline e_2)$, this becomes:$$\Huge\begin{align}
\lim_{\underline h\to\underline 0}\frac{\underline R(\underline h)}{\underline h}&=\lim_{\underline h\to\underline 0}\frac{1}{|\underline h|}(f(h_1,h_2)-f(0,0)-J_{\underline f}\underline h)\\
&=\lim_{ h\to 0}\frac{1}{\sqrt{2}|h|}(h^{\frac{1}{3}}h^{\frac{1}{3}}-0-(0,0)\underline h)\\
&=\lim_{h\to 0}\frac{1}{\sqrt{2}|h|}(h^{\frac{2}{3}}-0)\\
&=\lim_{h\to0}\frac{h^\frac{2}{3}}{\sqrt{2}|h|}\to\infty
\end{align}$$Such limit does not exists, so $f$ is not differentiable at $(0,0)$.

A function $\underline f:\Re^n\mapsto\Re^m$ is called continuously differentiable ($C^1$) at $\underline x\in\Re^n$ if all of its partial derivatives $\frac{\partial f_i}{\partial f_j}$ exists and are continuous at $\underline x$.

If $\underline f:\Re^n\mapsto\Re^m$ is $C^1$ near $\underline x\in\Re^n$, then $\underline f$ is differentiable at $\underline x$. We prove this in the case where $f:\Re^2\mapsto\Re$ as the method is analogous:

Differentiability at $\underline x$ requires:$$\Huge\begin{align}
f(\underline x+\underline h)&\simeq f(\underline x)+\begin{pmatrix}\frac{\partial f}{\partial x}(\underline x)&\frac{\partial f}{\partial y}(\underline x)\end{pmatrix}\begin{pmatrix}h_1\\h_2\end{pmatrix}\\
&\simeq f(\underline x)+h_1\frac{\partial f}{\partial x}(\underline x)+h_2\frac{\partial f}{\partial y}(\underline x)
\end{align}$$The existence of such derivatives at $\underline x$ implies that $f(\underline x+h_1\underline e_1)\simeq f(\underline x)+h_1\frac{\partial f}{\partial x}(\underline x)$ and similarly for $f(x+h_2\underline e_2)$. This implies that:$$\Huge\begin{align}
f(\underline x+\underline h)&\simeq f(\underline x+h_1\underline e_1)+h_2\frac{\partial f}{\partial y}(\underline x+h_1\underline e_1)\\
&\simeq f(\underline x)+h_1\frac{\partial f}{\partial x}+h_2\frac{\partial f}{\partial y}(\underline x+h_1\underline e_1)
\end{align}$$For this to be equal to the differentiability requirement we require that:$$\Huge h_1\to0\implies\frac{\partial f}{\partial y}(\underline x+h_1\underline e_1)\to\frac{\partial f}{\partial y}(\underline x)$$Which requires $\frac{\partial f}{\partial y}$ to be continuous.

We illustrate with the previous example. Consider that $f(x,y)=x^{\frac{1}{3}}y^{\frac{1}{3}}$ is not $C^1$ at $(0,0)$. We saw previously that $J_f=(0,0)$ so for $x,y\neq0,0$ consider:$$\Huge J_f(x,y)=\begin{pmatrix}\frac{\partial f}{\partial x}&\frac{\partial f}{\partial y}\end{pmatrix}=\begin{pmatrix}\frac{1}{3}x^{-\frac{2}{3}}y^{\frac{1}{3}}&\frac{1}{3}x^{\frac{1}{3}}y^{-\frac{2}{3}}\end{pmatrix}\implies\text{continuous}$$Notice at $(0,y)$:$$\Huge \frac{\partial f}{\partial x}(0,y)=\lim_{h\to0}\frac{f(h,y)-f(0,y)}{h}=\lim_{h\to0}\frac{h^\frac{1}{3}y^\frac{1}{3}-0}{h}=y^{\frac{1}{3}}\lim_{h\to0}h^{-\frac{2}{3}}\to\infty$$One can show that the limit at $(x,0)$ does not exists as well. Therefore $J_f$ does not exists for $x=0$ or $y=0$. There is no open neighborhood around $(0,0)$ where $J_f$ exists, so $f$ is not $C^1$ by definition.

We ask where $f(x,y)=y|x-2|$ is continuously differentiable. For $x>2$ observe:$$\Huge f(x,y)=y(x-2)\implies\frac{\partial f}{\partial x}=y,\,\,\frac{\partial f}{\partial y}=x-2$$And for $x<2$:$$\Huge f(x,y)=-y(x-2)\implies\frac{\partial f}{\partial x}=y,\,\,\frac{\partial f}{\partial y}=2-x$$For $x=2$ we use the limit definition:$$\large \frac{\partial f}{\partial x}(2,y)=\lim_{h\to0}\frac{f(2+h,y)-f(2,y)}{h}=\lim_{h\to0}\frac{y|h|-0}{h}=y\lim_{h\to0}\frac{|h|}{h}\to\text{DNE}$$This limit does not exist for $y\neq0$ so $J_f$ does not exist for $\{x=2,y\neq0\}$:![[continuously diff]]
By the above theorem, $f$ is differentiable everywhere except $x=2$. For $(2,y)$ with $y\neq0$ $J_f$ does not exist, so $f$ cannot be differentiable. For $(2,0)$ we have $J_f=(0,0)$ so we must check the remainder term:$$\Huge\begin{align}
\lim_{\underline h\to\underline 0}\frac{R(\underline h)}{|\underline h|}&=\lim_{\underline h\to\underline 0}\frac{1}{|\underline h|}\left(f(2+h_1,h_2)-f(2,0)-\begin{pmatrix}0&0\end{pmatrix}\begin{pmatrix}h_1\\h_2\end{pmatrix}\right)\\\\
&=\lim_{\underline h\to\underline 0}\frac{h_2|h_1|}{\sqrt{h_1^2+h_2^2}}\leq\lim_{\underline h\to\underline 0}\frac{|\underline h|^2}{|\underline h|}=\lim_{\underline h\to\underline 0}|\underline h|=0
\end{align}$$And since all terms are positive, we get that the limit is $0$ by the squeezing theorem and that $f$ is indeed differentiable at $\{x\neq0\}\cup\{(2,0)\}$.

# Chain rule:


If $\underline g:\Re^k\mapsto\Re^n$ is differentiable at $\underline x\in\Re^k$ and $\underline f:\Re^n\mapsto\Re^m$ is differentiable at $\underline g(\underline x)\in\Re^n$ then:$$\Huge J_{\underline f\circ\underline g}(\underline x)=J_{\underline f}(\underline g(\underline x))J_{\underline g}(\underline x)$$Which is a product of two matrices. Note if $n=m=k=1$ this reduces to:$$\Huge (f\circ g)'(x)=f'(g(x))g'(x)$$The one dimensional chain rule:
![[domains]]

The proof of this follows for any $\underline h\in\Re^k$ that:$$\Huge\begin{align}\\
(\underline f\circ\underline g)(\underline x+\underline h)&=\underline f(\underline g(\underline x+\underline h))\\
&=\underline f(\underline g(\underline x)+J_{\underline g}(\underline x)\underline h+\underline R_{\underline g}(\underline h))\\
&=\underline f(\underline g(\underline x))+J_{\underline f}(\underline g(\underline x))\underline {\tilde h}+R_{\underline f}(\underline {\tilde h})\\
&=\underline f(\underline g(\underline x))+J_{\underline f}(\underline g(\underline x))J_{\underline g}(\underline x)\underline h+J_{\underline f}(\underline g(\underline x))\underline R_{\underline g}(\underline g)+\underline R_{\underline f}(\underline {\tilde h})
\end{align}$$
Where the two terms on the right vanish since $\underline R_\underline g(\underline g)\to0$ and $\underline R_\underline f(\underline {\tilde h})\to 0$ when $\underline h\to0$. So we have that the composition has a derivative equal to the one proposed.

Take the example of $\underline f(u,v)=\begin{pmatrix}u^2+v^2\\uv\end{pmatrix}$ and $\underline g(x,y)=\begin{pmatrix}2x-y\\y-x\end{pmatrix}$. We aim to find $J_{\underline f\circ\underline g}(x,y)$ with such vector fields. We have that $g:\Re^2\mapsto\Re^2$ and $f:\Re^2\mapsto\Re^2$ so $m=n=k=2$ and we can find such composition. First we compute individual derivative matrices:$$\Huge\begin{align}
J_\underline g(x,y)&=\begin{pmatrix}\frac{\partial g_1}{\partial x}&\frac{\partial g_1}{\partial y}\\\frac{\partial g_2}{\partial x}&\frac{\partial g_2}{\partial y}\end{pmatrix}=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}\\
J_\underline f(u,v)&=\begin{pmatrix}\frac{\partial f_1}{\partial u}&\frac{\partial f_1}{\partial v}\\\frac{\partial f_2}{\partial u}&\frac{\partial f_2}{\partial v}\end{pmatrix}=\begin{pmatrix}2u&2v\\v&u\end{pmatrix}
\end{align}$$So the chain rule give the composition:$$\Huge\begin{align}
J_{\underline f\circ\underline g}(x,y)&=J_\underline f(\underline g(x,y))J_\underline g(x,y)=\begin{pmatrix}2g_1&2g_2\\g_2&g_1\end{pmatrix}\begin{pmatrix}2&-1\\-1&1\end{pmatrix}\\
&=\begin{pmatrix}4g_1-2g_2&-2g_1+2g_2\\-g_1+2g_2&g_1-g_2\end{pmatrix}\\
&=\begin{pmatrix}10x-6y&-6x+4y\\-4x+3y&3x-2y\end{pmatrix}
\end{align}$$One can check that the upper left component matches:$$\Huge\begin{align}
\underline f\circ\underline g(x,y)&=\begin{pmatrix}(2x-y)^2+(y-x)^2\\(2x-y)(y-x)\end{pmatrix}\\
\frac{\partial }{\partial x}(\underline f\circ\underline g)_{11}&=2(2)(2x-y)-2(y-x)\\
&=10x-6y
\end{align}$$Which indeed matches the computed matrix.

We can use this theorem to obtain the chain rule formula used in the proof of [[Integral theorems#Fundamental theorem of line integrals|the fundamental theorem of line integrals]]:$$\Huge \frac{d f}{dt}=\frac{\partial f}{\partial x}\frac{d x}{dt}+\frac{\partial f}{\partial y}\frac{d y}{dt}+\frac{\partial f}{\partial z}\frac{d z}{dt}$$Where $\underline x(t):\Re\mapsto\Re^3$ is a parametrised curve and $f(\underline x):\Re^3\mapsto\Re$ is a scalar field. We have $k=m=1$ and $n=3$, so the composition maps from $\Re\mapsto\Re^3\mapsto\Re$, that is $f \circ\underline x:\Re\mapsto\Re$. The matrix then has a single component:$$\Huge
\begin{align} J_{f\circ\underline x}&=\begin{pmatrix}\frac{d (f\circ\underline x)}{dt}\end{pmatrix}=J_\underline f(\underline x(t))J_\underline x(t)=\\
&=\begin{pmatrix}\frac{\partial f}{\partial x}&\frac{\partial f}{\partial y}&\frac{\partial f}{\partial z}\end{pmatrix}_{\underline x(t)}\begin{pmatrix}\frac{d x}{dt}\\\frac{d y}{dt}\\\frac{d z}{dt}\end{pmatrix}\\
&=\frac{d f}{dt}
\end{align}$$Where $J_f(\underline x(t))\in M_{1\times 3}(\Re)$ and $J_\underline x(t)\in M_{3\times 1}(\Re)$.

We can also use this theorem to obtain the chain rule formula used in the proof of [[Surface and volume integrals#Changing variables|independent surface integral parametrisations]]. Where we used:$$\Huge\begin{align}
\frac{\partial \underline x}{\partial u}&=\frac{\partial \underline x}{\partial \mu}\frac{\partial \mu}{\partial u}+\frac{\partial \underline x}{\partial \nu}\frac{\partial \nu}{\partial u}\\
\frac{\partial \underline x}{\partial v}&=\frac{\partial \underline x}{\partial \mu}\frac{\partial \mu}{\partial v}+\frac{\partial \underline x}{\partial \nu}\frac{\partial \nu}{\partial v}
\end{align}$$Where $\underline x(\mu,\nu):\Re^2\mapsto\Re^3$ is a parametrisation of a surface, related to some alternative parametrisation $\underline x(u,v)$ by a change of coordinates that maps $(\mu,\nu)=\underline g(u,v):\Re^2\mapsto\Re^2$. Here, $n=k=2$ and $m=3$ which makes $J_{\underline x\circ\underline g}(u,v)\in M_{3\times 2}$ given by:$$\Huge\begin{align}
J_{\underline x\circ\underline g}(u,v)&=\begin{pmatrix}\frac{\partial x}{\partial u}&\frac{\partial x}{\partial v}\\\frac{\partial y}{\partial u}&\frac{\partial y}{\partial v}\\\frac{\partial z}{\partial u}&\frac{\partial z}{\partial v}\end{pmatrix}=J_\underline x(\underline g(u,v))J_\underline g(u,v)\\
&=\begin{pmatrix}\frac{\partial x}{\partial \mu}&\frac{\partial x}{\partial \nu}\\\frac{\partial y}{\partial \mu}&\frac{\partial y}{\partial \nu}\\\frac{\partial z}{\partial \mu}&\frac{\partial z}{\partial \nu}\end{pmatrix}\begin{pmatrix}\frac{\partial \mu}{\partial u}&\frac{\partial u}{\partial v}\\\frac{\partial \nu}{\partial u}&\frac{\partial \nu}{\partial v}\end{pmatrix}\\
&=\begin{pmatrix}\frac{\partial x}{\partial \mu}\frac{\partial \mu}{\partial u}+\frac{\partial x}{\partial \nu}\frac{\partial \nu}{\partial u}&\frac{\partial x}{\partial \mu}\frac{\partial \mu}{\partial v}+\frac{\partial x}{\partial \nu}\frac{\partial \nu}{\partial v}\\\frac{\partial y}{\partial \mu}\frac{\partial \mu}{\partial u}+\frac{\partial y}{\partial \nu}\frac{\partial \nu}{\partial u}&\frac{\partial y}{\partial \mu}\frac{\partial \mu}{\partial v}+\frac{\partial y}{\partial \nu}\frac{\partial \nu}{\partial v}\\\frac{\partial z}{\partial \mu}\frac{\partial \mu}{\partial u}+\frac{\partial z}{\partial \nu}\frac{\partial \nu}{\partial u}&\frac{\partial z}{\partial \mu}\frac{\partial \mu}{\partial v}+\frac{\partial z}{\partial \nu}\frac{\partial \nu}{\partial v}\end{pmatrix}\\
&=\begin{pmatrix}\frac{\partial x}{\partial u}&\frac{\partial x}{\partial v}\\\frac{\partial y}{\partial u}&\frac{\partial y}{\partial v}\\\frac{\partial z}{\partial u}&\frac{\partial z}{\partial v}\end{pmatrix}=\begin{pmatrix}\frac{\partial \underline x}{\partial u}&\frac{\partial \underline x}{\partial v}\end{pmatrix}
\end{align}$$And we get the correct component of $J_{\underline x\circ\underline g}(u,v)_{11}$ as required. 

# Inverse functions:

A function $\underline f:\Re^n\mapsto\Re^n$ has an inverse $\underline f^{-1}$ if and only if for all $\underline x\in\Re^n$ we have:
>$(\underline f^{-1}\circ\underline f)(\underline x)=\underline x$
>$(\underline f\circ\underline f^{-1})(\underline x)=\underline x$

Take $\underline f(x,y)=\begin{pmatrix}x-y\\x+2y\end{pmatrix}$ for example:$$\Huge \underline f=\begin{pmatrix}1&-1\\1&2\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}\implies\underline f^{-1}=\begin{pmatrix}1&-1\\1&2\end{pmatrix}^{-1}\begin{pmatrix}x\\y\end{pmatrix}$$Note that the matrix here is the derivative matrix $J_{\underline f}$ so we have that:$$\Huge J_{\underline f^{-1}}=(J_{\underline f})^{-1}$$We propose that this holds even for non-linear functions. That is to say if $\underline f:\Re^n\mapsto\Re^n$ has an inverse and both $\underline f$ and it's inverse are differentiable then:$$\Huge J_{\underline f^{-1}}(\underline y)=(J_{\underline f})^{-1}(\underline x)$$Where $\underline y=\underline f(\underline x)$. To prove this, observe:$$\Huge\begin{align}
(\underline f^{-1}\circ\underline f)(\underline x)=\underline x&\implies J_{\underline f^{-1}\circ\underline f}(\underline x)=I_n\\
&\implies J_{\underline f^{-1}}(\underline f(\underline x))J_{\underline f}(\underline x)=I_n\\
&\implies J_{\underline f^{-1}}(\underline y)J_{\underline f}(\underline x)=I_n\\
(\underline f\circ\underline f^{-1})(\underline y)=\underline y&\implies J_{\underline f\circ\underline f^{-1}}(\underline y)=I_n\\
&\implies J_{\underline f}(\underline f^{-1}(\underline y))J_{\underline f^{-1}}(\underline y)=I_n\\
&\implies J_{\underline f}(\underline x)J_{\underline f^{-1}}(\underline y)=I_n\\
\implies (J_{\underline f})^{-1}(\underline x)|&=J_{\underline f^{-1}}(\underline y)
\end{align}$$
We can use this to find the linearisation of $\underline f^{-1}$ around the point $\underline y=f(2,1)$ when:$$\Huge\begin{align}
\underline f(u,v)&=\begin{pmatrix}u^2+v^2\\uv\end{pmatrix}\\
\implies J_{\underline f}&=\begin{pmatrix}\frac{\partial f_1}{\partial u}&\frac{\partial f_1}{\partial v}\\\frac{\partial f_2}{\partial u}&\frac{\partial f_2}{\partial v}\end{pmatrix}=\begin{pmatrix}2u&2v\\v&u\end{pmatrix}\\
\implies J_{\underline f^{-1}}(\underline y)&=(J_{\underline f})^{-1}(2,1)\\
&=\frac{1}{2(u^2-v^2)}\begin{pmatrix}u&-2v\\-v&2u\end{pmatrix}\vert_{(2,1)}\\
&=\frac{1}{6}\begin{pmatrix}2&-2\\-1&4\end{pmatrix}
\end{align}$$This allows for the reconstruction of the linearisation of $\underline f^{-1}$ even though the full nonlinear function is unknown:$$\Huge\begin{align}
\underline f^{-1}(\underline y+\underline h)&\approx\underline f^{-1}(\underline y)+J_{\underline f^{-1}}(\underline y)\underline h\\
&\approx\begin{pmatrix}2\\1\end{pmatrix}+(J_{\underline f})^{-1}
\underline h\\
&\approx\begin{pmatrix}2\\1\end{pmatrix}+\frac{1}{6}\begin{pmatrix}2&-2\\-1&4\end{pmatrix}\begin{pmatrix}h_1\\h_2\end{pmatrix}
\end{align}$$

## Inverse function theorem (diffeomorphisms):
Let $\underline f:\Re^n\mapsto\Re^n$ be a $C^1$ function. Then $\underline f$ has a local differentiable inverse near $\underline y=\underline f(\underline x)$ if and only if it has an invertible derivative matrix $J_{\underline f}(\underline x)$ at the point $\underline x$. This can be proven by showing that the remainder terms tend to zero faster than linear order.

A function $\underline f:\Re^n\mapsto\Re^n$ satisfying this condition is called a local diffeomorphism. A diffeomorphism is called orientation preserving if $\det(J_{\underline f}(\underline x))>0$ and orientation reversing if $\det(J_{\underline f}(\underline x))<0$.

We can ask where the function $\underline f(r,\theta)=\begin{pmatrix}r\cos\theta\\r\sin\theta\end{pmatrix}$ for $r\in[0,\infty),\theta\in[0,2\pi]$ is a local diffeomorphism:$$\Huge\begin{align}
J_{\underline f}(r,\theta)&=\begin{pmatrix}\frac{\partial f_1}{\partial r}&\frac{\partial f_1}{\partial \theta}\\\frac{\partial f_2}{\partial r}&\frac{\partial f_2}{\partial \theta}\end{pmatrix}=\begin{pmatrix}\cos\theta&-r\sin\theta\\\sin\theta&r\cos\theta\end{pmatrix}\\
&\implies\det(J_{\underline f}(r,\theta))=r\cos^2\theta+r\sin^2\theta=r
\end{align}$$So this function is a diffeomorphism for $r>0$ but not at $r=0$. The function is also said to be orientation preserving for $r\neq0$:![[orientation preservation]]Note that one can see $\underline f$ fails to be bijective at $r=0$ as every point in the domain is mapped to $f_1=f_2=0$. The inverse function is given by:$$\Huge \underline f^{-1}(f_1,f_2)=\begin{pmatrix}\sqrt{f_1^2+f_2^2}\\\arctan(f_2/f_1)\end{pmatrix}$$One can check that the partial derivatives agree.

# Implicit functions:

Given a $C^1$ function $\underline F:\Re^{n+m}\mapsto\Re^m$, let $\underline x\in\Re^n$ and $\underline y\in\Re^m$. Solutions to the system of $m$ equations $\underline F(\underline x,\underline y)=\underline 0$ near a solution point $(\underline x,\underline y)=(\underline x_{\underline a},\underline y_{\underline a})=\underline a\in\Re^{n+m}$ can be written as an implicit function $\underline y=\underline y(\underline x)$ if:$$\Huge \begin{vmatrix}\frac{\partial \underline F}{\partial y_1}(\underline a)&\frac{\partial \underline F}{\partial y_2}(\underline a)&\dots&\frac{\partial \underline F}{\partial y_m}(\underline a)\end{vmatrix}\neq0$$Since $\underline F$ is differentiable, we have that near $\underline a$ the linearisation holds:$$\Huge\underline F(\underline x,\underline y)\simeq\underline F(\underline a)+J_{\underline F}(\underline a)\begin{pmatrix}\underline x-\underline x_a\\\underline y-\underline y_a\end{pmatrix}$$By definition we have $\underline F(\underline a)=\underline 0$ so:$$\begin{align}\\
\large J_{\underline F}(\underline a)\begin{pmatrix}\underline x-\underline x_a\\\underline y-\underline y_a\end{pmatrix}\simeq\underline 0&\implies\begin{pmatrix}\frac{\partial \underline F}{\partial x_1}&\dots&\frac{\partial \underline F}{\partial x_n}&\frac{\partial \underline F}{\partial y_1}&\dots&\frac{\partial \underline F}{\partial y+m}\end{pmatrix}_{\underline a}\begin{pmatrix}\underline x-\underline x_a\\\underline y-\underline y_a\end{pmatrix}\simeq\underline 0\\
&\iff\begin{pmatrix}\frac{\partial \underline F}{\partial x_1}&\dots&\frac{\partial \underline F}{\partial x_n}\end{pmatrix}_{\underline a}(\underline x-\underline x_a)+\begin{pmatrix}\frac{\partial \underline F}{\partial y_1}&\dots&\frac{\partial \underline F}{\partial y_m}\end{pmatrix}_{\underline a}(\underline y-\underline y_a)\\
&\iff\underline y\simeq\underline y_a-\begin{pmatrix}\frac{\partial \underline F}{\partial y_1}&\dots&\frac{\partial \underline F}{\partial y_m}\end{pmatrix}_{\underline a}^{-1}\begin{pmatrix}\frac{\partial \underline F}{\partial x_1}&\dots&\frac{\partial \underline F}{\partial x_n}\end{pmatrix}_{\underline a}(\underline x-\underline x_a)
\end{align}$$The right hand side is a function only of $\underline x$, and is well defined is the associated $y$ matrix is invertible. Note that this reduces to the single variable derivative formula:$$\Huge y'=-\frac{\frac{\partial f}{\partial x}}{\frac{\partial f}{\partial y}}$$For $n=m=1$.

Take the following simultaneous equations satisfied by $(u,v,w)$:$$\Huge\begin{align}
uv^2+v^2w^3+u^5w^4-1&=0\\
u^2w+u^2v^2+v^2w^5+1&=0
\end{align}$$As example. We ask if $u,v$ can be expressed as a function of $w$ near $\underline a=(u,v,w)=(1,1,-1)$. We have two equations and two dependent variables implying $m=2$. We have one independent variable $w$ so $n=1$. Therefore $\underline x=\begin{pmatrix}w\end{pmatrix}$ and $\underline y=\begin{pmatrix}u\\w\end{pmatrix}$ with:$$\large \underline F(\underline x,\underline y)=\begin{pmatrix}uv^2+v^2w^3+u^5w^4-1\\u^2w+u^2v^3+v^4w^5+1\end{pmatrix},\,\,\underline F(1,1,-1)=\begin{pmatrix}1-1+1-1\\-1+1-1+1\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}$$So the theorem applies.