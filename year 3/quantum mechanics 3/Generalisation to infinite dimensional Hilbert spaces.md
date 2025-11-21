
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

