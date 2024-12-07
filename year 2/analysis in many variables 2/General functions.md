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
\end{align}$$And since all terms are positive, we get that the limit is $0$ by the squeezing theorem and that $f$ is indeed differentiable at this sole point along $x=2$.