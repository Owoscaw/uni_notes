
# Position operator:

We have [[QM linear algebra#Orthonormal basis expansion|previously considered]] an observable $\hat O$ and understood that knowing its possible outcomes gives the spectrum $w_i$ of its eigenvalues, which leads to a complete basis. We now consider the generalisation of this notion to a continuous spectrum of eigenvalues, forming an infinite dimensional Hilbert space. Consider a discretuum of possible $x$ values labelled $i$ on a finite interval. We have a Hermitian position operator $\hat x$ with its discrete spectrum $x_i$ and corresponding eigenbasis $|x_i\rangle$, so we write:$$\Huge \hat x |x_i\rangle=x_i |x_i\rangle$$where $i=1,\dots,N$ and the total interval length is expressed as $L=N\delta x$. We can then form a complete basis such that any state is written as:$$\Huge\begin{align*}
|\psi\rangle&=\sum_{i=0}^N c_i |x_i\rangle\\
&=\sum_{i=0}^N \langle x_i|\psi\rangle |x_i\rangle
\end{align*}$$The probability of finding the particle in the $i$th position is then $P_i=|c_i|^2$. This makes sense physically as:
> Orthonormality insists if a particle is measured in box $i$, then after measurement it is in state $|\psi\rangle=|x_i\rangle$. The probability of measuring the particle immediately afterwards in some box $x_j$ with $i\neq j$ should be zero. This is imposed by $|\langle \psi|j\rangle|^2=|\langle i|j\rangle|^2=0$

Now we can use this model to generalise to infinite dimensional Hilbert spaces. We begin with the system defined discretely with each $i$-eigenstate corresponding to measuring the particle in the $i$th of $N$ boxes. As the probability summed over all boxes is unitary, the value of $P_i=|\psi_i|^2$ in the discrete case would scale to zero as $1/N$ $N\to\infty$, as the probability of being in any single block scales to zero. Therefore we compromise, since $\delta x$ scales as $1/N$ by using probability per unit $x$ ($|\psi_i|^2/\delta x$). In the limit as $N\to\infty$ this becomes a probability density:$$\Huge|\psi(x_i)|^2=\frac{|\psi_i|^2}{\delta x}$$![[Generalisation to infinite dimensional Hilbert spaces 2025-11-20 22.02.30.excalidraw]]Measurement of $\hat x$ can also be written as the expectation value of the projection operator onto the state:$$\Huge\begin{align*}
P(x_i)&=\langle \psi|\hat P_{x_i}|\psi\rangle\\
\hat P_{x_i}&=|x_i\rangle \langle x_i|\\
\implies P(x_i)&=\langle \psi|x_i\rangle \langle x_i|\psi\rangle=|c_i|^2
\end{align*}$$By extension, the probability to find the particle between $x_i$ and $x_{i+h}$ is:$$\Huge P([x_i,x_{i+h}])=\sum_{j=i}^{i+h}P(x_j)=\sum_{j=i}^{i+h}|c_j|^2$$We wish to go to the continuous limit, using a the definition of a wave function for the probability density. That is, we note that the height of the histograms $P_i/\delta x$. This remains roughly constant as $\delta x\to 0$, so we define a rescaled projection operator onto the $i$-th box:$$\Huge\hat\Pi_{x_i}=\frac{1}{\delta x}|x_i\rangle \langle x_i|$$such that $\langle\Pi_{x_i}\rangle$ remains constant as $N\to\infty$. The probability to find the particle between $x_i$ and $x_{i+h}$ can be trivially rewritten as:$$\Huge P([x_i,x_{i+h}])=\delta x\sum_{j=i}^{i+h}\langle\hat\Pi_{x_i}\rangle$$While the number of boxes between $x=a,b$ will go to infinity with $N$, the interval remains finite. The compromise we make is that the object we have to integrate is not the original $\psi(x_i)$ of the discrete system, but a probability-density wave function:$$\Huge\langle\hat\Pi_{x_i}\rangle=\frac{1}{\delta x}\langle \psi|x_i\rangle\langle x_i|\psi\rangle$$We can therefore identify a continuous wave function which also remains roughly constant in the infinite $N$ limit:$$\Huge\langle x|\psi\rangle=\frac{1}{\sqrt{\delta x}}\langle x_i|\psi\rangle=\psi(x)$$We can express this continuum limit entirely in terms of the basis vectors as:$$\Huge\frac{1}{\sqrt{\delta x}}|x_i\rangle\rightarrow |x\rangle$$The probability of finding the particle between $x=a,b$ then becomes the integral:$$\Huge P([a,b])\rightarrow\int_a^b \langle \psi|x\rangle \langle x|\psi\rangle dx$$
# Other relations:

Using the change in basis, we can derive the continuous forms of the other relations. The identity would become:$$\Huge \hat{\mathbb{I}}=\sum_{i=1}^N |x_i\rangle \langle x_i|=\delta x\sum_{i=1}^N\frac{1}{\delta x}|x_i\rangle \langle x_i|\to\int_{-\infty}^\infty |x\rangle \langle x|dx$$By inserting copies of $\hat{\mathbb{I}}$ we can write the wave function in the $|x\rangle$ basis:$$\Huge |\psi\rangle=\int |x\rangle \langle x|\psi\rangle dx=\int\psi(x) |x\rangle dx$$The inner product between two eigenstates becomes:$$\Huge \langle \psi_1|\psi_2\rangle=\int \langle \psi_1|x\rangle \langle x|\psi_2\rangle dx=\int\psi_1^*(x)\psi_2^*(x)dx$$And a normalised eigenstate will obey:$$\Huge \langle \psi|\psi\rangle=\int \langle \psi|x\rangle \langle x|\psi\rangle dx=\int|\psi(x)|^2dx=1$$
## Eigenstates of $|x\rangle$:
We use the identity operator to discern what should happen for the inner products between eigenstates with different $x$ values $(x,x')$. Consider inserting an identity in $\langle x|\psi\rangle$:$$\Huge \langle x|\psi\rangle=\int \langle x|x'\rangle \langle x'|\psi\rangle dx'$$This identifies the inner product as a generalised function called the [[Electromagnetism#Vector calculus and Dirac delta|Dirac delta]] function:$$\Huge f(x)=\int\delta(x-x')f(x')dx'$$By inspection we identify the inner product of position eigenstates as:$$\Huge \langle x'|x\rangle=\delta(x-x')$$Note that this implies that a position eigenstate $|x\rangle$ cannot be normalised in the sense that it obeys our integral requirement. Instead we call this "norm one" it is scales by $1$ with the delta function. In fact this is obvious by our scaling definition, which dictates that the discrete norm $1/\delta x\to\infty$. Given this relation and inner product, we now write the matrix form of the position operator $\hat x$:$$\Huge x_{x'x}=\langle x'|\hat x |x\rangle=x \langle x'|x\rangle=x\delta(x-x')$$Likewise we can write the operator as an expansion, which becomes a double integral:$$\Huge\begin{align*}
\hat x&=\iint x_{x'x}|x'\rangle \langle x|dx\,dx'\\
&=\iint x\delta(x-x') |x'\rangle \langle x|dx\,dx'
\end{align*}$$Since the $\delta$-definition always collapses $x'$ to $x$ when the integral is performed, we can actually perform an integral once to define:$$\Huge\hat x=\int x |x\rangle \langle x|dx$$We check that this machinery actually works by finding $\hat x |x''\rangle$:$$\Huge \begin{align*}
\hat x |x''\rangle&=\int x |x\rangle \langle x|x''\rangle dx\\
&=\int x |x\rangle\delta(x-x'')dx\\
&=x''|x''\rangle
\end{align*}$$as required. This is the continuous equivalent of [[Operators and Measurement#Spectral Decomposition|spectral decomposition]], which we use to extend this for any function of $\hat x$:$$\Huge f(\hat x)=\int f(x) |x\rangle \langle x|dx$$Finally, we can calculate things like the expectation as follows:$$\Huge\begin{align*}
\langle\hat x\rangle&=\langle \psi|\hat x |\psi\rangle=\langle \psi|\hat x\hat{\mathbb{I}}|\psi\rangle\\
&=\langle \psi|\hat x\int |x'\rangle \langle x'|dx'|\psi\rangle\\
&=\int x|\psi(x)|^2dx
\end{align*}$$
We summarise:

| object                     | discrete relation                             | continuous relation                                                |
| -------------------------- | --------------------------------------------- | ------------------------------------------------------------------ |
| $\|i\rangle$               | $\frac{1}{\sqrt{\delta x}}\|x_i\rangle$       | $\|x\rangle$                                                       |
| $\|\psi\rangle$            | $\sum_ic_i\|x_i\rangle$                       | $\int\|x\rangle\langle x\|\psi\rangle dx=\int\psi(x)\|x\rangle dx$ |
| $\hat{\mathbb{I}}$         | $\sum_i\|x_i\rangle\langle x_i\|$             | $\int\|x\rangle\langle x\|dx$                                      |
| $f(\hat x)$                | $\sum_if(x_i)\|x_i\rangle\langle x_i\|$       | $\int f(x)\|x\rangle\langle x\|dx$                                 |
| $\langle f(\hat x)\rangle$ | $\sum_i f(x_i)\|\langle x_i\|\psi\rangle\|^2$ | $\int f(x)\|\psi(x)\|^2dx$                                         |
| $\langle i\|j\rangle$      | $\langle x_i\|x_j\rangle=\delta_{ij}$         | $\langle x'\|x\rangle=\delta(x-x')$                                |
# Momentum operator:

We now move on to the momentum operator, returning to the notion of [[Hamiltonian Formalism#Hamiltonian flows|Hamiltonian flows]]. We saw that it was possible to induce a flow in the phase space with an operator $\Phi_f^{(\epsilon)}$ with:$$\Huge \Phi_f^{(\epsilon)}=g+\epsilon\{g,f\}$$where $f=f(x,p),g=g(x,p)$ are some functions on the phase space. If we choose $f(x,p)=p$ then for infinitesimal $\epsilon$ we have:$$\Huge\begin{align*}
\Phi_f^{(\epsilon)}(g)&=g+\epsilon\{g,p\}\\
&=g+\epsilon\partial_xg\\
&=g(x+\epsilon,p)
\end{align*}$$Thus in classical mechanics, momentum is the generator of translations in $x$ through its Poisson bracket. We can write this as:$$\Huge \frac{dg}{d\epsilon}=\{g,p\}=\partial_xg$$Then for non-infinitesimal $\epsilon$ we can write this as a mapping of the function $g$:$$\Huge g\rightarrow e^{\epsilon\{\cdot,p\}}g=e^{\epsilon\partial_x}g$$We can then use the correspondence principle to get the expectation values of a quantum system, where $\hat g=g(\hat x,\hat p)$:$$\Huge \frac{d\langle\hat g\rangle}{d\epsilon}=-\frac{i}{\hbar}\langle[\hat g,\hat p]\rangle=\langle\partial_x\hat g\rangle$$The expectation of an operator that is described by a function on $\hat x$ is shifted by a change in the wave function as follows:$$\Huge \langle\hat g\rangle=\langle \psi|\hat g |\psi\rangle\rightarrow \langle \psi'|\hat g |\psi'\rangle$$where $|\psi'\rangle$ is the wavefunction transformed through $\epsilon$:$$\Huge |\psi'\rangle=|\psi\rangle+\epsilon \frac{d |\psi\rangle}{d\epsilon}$$Here, we are assuming $\hat g$ is an operator with no explicit $\epsilon$-dependence. It does not change under $\epsilon$ transformations, but the transformation in the expectation value of $\hat g$ is caused by a change in the wavefunction. To find such transformation, we consider the $\epsilon$ derivative of the expectation value:$$\Huge\begin{align*}
\frac{d}{d\epsilon}\langle\hat g\rangle&=\frac{d \langle \psi|}{d\epsilon}\hat g |\psi\rangle+ \langle \psi|\hat g \frac{d |\psi\rangle}{d\epsilon}\\
&=\frac{i}{\hbar} \langle \psi|\hat p\hat g |\psi\rangle-\frac{i}{\hbar}\langle \psi|\hat g\hat p |\psi\rangle
\end{align*}$$Since $\hat p$ is an observable we have $\hat p^\dagger=\hat p$ and therefore the above is satisfied by a single ODE of the wavefunction:$$\Huge\implies \frac{d |\psi\rangle}{d\epsilon}=-\frac{i}{\hbar}\hat p |\psi\rangle$$which is solved, giving a wavefunction of form:$$\Huge |\psi\rangle\rightarrow |\psi'\rangle=e^{-i\epsilon\hat p/\hbar}|\psi\rangle$$Note that $g$ is not present in this form, showing that a transformation on $|\psi\rangle$ will produce the required change in expectation for ANY operator.

So far, everything is in terms of the generic operator $\hat p$, so we ask of the form of such operator. We know that:$$\Huge -\frac{i}{\hbar} \langle \psi|[\hat g,\hat p]|\psi\rangle=\langle \psi|\partial_{\hat x}\hat g |\psi\rangle$$We proceed by inserting identity operators in the $x$-eigenbasis:$$\begin{align*}
-\frac{i}{\hbar}\int \langle \psi|\hat g |x\rangle \langle x|\hat p |\psi\rangle-\langle \psi|\hat p |x\rangle \langle x|\hat g |\psi\rangle dx&=\int \langle \psi|x\rangle \langle x|\partial_{\hat x}\hat g |\psi\rangle\\
\implies-\frac{i}{\hbar}\int g(\langle \psi|x\rangle \langle x|\hat p |\psi\rangle-\langle \psi|\hat p |x\rangle \langle x|\psi\rangle)dx&=\int \langle \psi|x\rangle\partial_x g \langle x|\psi\rangle dx\\
&=-\int g(\langle \psi|x\rangle\partial_x \langle x|\psi\rangle+\partial_x \langle \psi|x\rangle \langle x|\psi\rangle)dx
\end{align*}$$where we used integration by parts and the assumption that $\psi$ vanishes at $\pm\infty$. We can solve this by inferring a differential equation that is satisfied by the wave function in the $x$ basis:$$\Huge \langle x|\hat p |\psi\rangle=-i\hbar \partial_x \langle \psi|x\rangle$$We see that the action of $\hat p$ on $|\psi\rangle$ "pulls out" the derivative operator from the braket, so $\hat p$ cannot be the derivative operator by itself. To solve this we must find an operator that pulls the derivative out of the braket. We write $\hat p$ in the general form as an operator expansion:$$\Huge\hat p=\iint p_{xx'}|x'\rangle \langle x|dx'\,dx$$We can get the coefficients $p_{xx'}$ by observing:$$\Huge p_{xx'}= \langle x|\hat p |x'\rangle=-i\hbar\partial_x \langle x|x'\rangle\implies p_{xx'}=-i\hbar\partial_x\delta(x-x')$$That is, the matrix elements of $\hat p$ are derivatives of the delta function. We can then write the operator as the double integral over these elements with multiplying operators:$$\Huge\hat p=-i\hbar\iint |x\rangle \langle x'|\partial_x\delta(x-x')dx\,dx'$$We check that this acts as we expect on the wavefunction:$$\Huge\begin{align*}
 \langle x|\hat p |\psi\rangle&=-i\hbar\iint \langle x|x''\rangle \langle x'|\partial_{x''}\delta(x''-x') |\psi\rangle\,dx''dx'\\
&=-i\hbar\int\partial_x\delta(x-x') \langle x'|\psi\rangle dx
\end{align*}$$To evaluate this we must first write the delta function derivative as:$$\Huge \partial_x\delta(x-x')=\delta'(x-x')=-\partial_{x'}\delta(x-x')$$So we get:$$\Huge\begin{align*}
\implies \langle x|\hat p |\psi\rangle&=i\hbar\int\partial_{x'}\delta(x-x') \langle x'|\psi\rangle dx'\\
&=-i\hbar\int\delta(x-x')\partial_{x'} \langle x'|\psi\rangle dx'\\
&=-i\hbar\partial_x \langle x|\psi\rangle
\end{align*}$$where we used integration by parts and the general property of the delta function. 

Given the factor of $i$, it is natural to be concerned about the hermiticity of $\hat p$. We saw that $p_{xx'}$ is antisymmetric:$$\Huge p_{xx'}=-p_{x'x}$$therefore $p_{x'x}$ is purely imaginary and we have $p^*_{xx'}=p_{x'x}$ and hence $\hat p=\hat p^\dagger$, the momentum operator is indeed an observable.

We also wish to check the usual commutation relations involving $\hat x,\hat p$:$$\Huge\begin{align*}
\hat x\hat p&=i\hbar\iint \hat x |x\rangle \langle x'|\partial_{x'}\delta(x-x')dx\,dx'\\
&=-i\hbar\iint x\delta(x-x') |x\rangle\partial_{x'} \langle x'|dx\,dx'\\
&=-i\hbar\int |x\rangle x\partial_x \langle x|dx\\
\hat p\hat x&=i\hbar\iint |x\rangle \langle x'|\hat x\partial_{x'}\delta(x-x')dx\,dx'\\
&=i\hbar\iint |x\rangle \langle x'|x'\partial_{x'}\delta(x-x')dx\,dx'\\
&=-i\hbar\iint\delta(x-x') |x\rangle\partial_{x'}x' \langle x'|dx\,dx'\\
&=-i\hbar\int |x\rangle\partial_x x \langle x|dx\\
&=-i\hbar\int |x\rangle \langle x|dx-i\hbar\int |x\rangle x\partial_x \langle x|dx\\
&=-i\hbar\hat{\mathbb{I}}-i\hbar\int |x\rangle x\partial_x \langle x|dx\\
\implies [\hat x,\hat p]&=i\hbar\hat{\mathbb{I}}
\end{align*}$$