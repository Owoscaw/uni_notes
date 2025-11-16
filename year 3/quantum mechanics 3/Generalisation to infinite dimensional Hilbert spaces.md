
# Position operator:

We have [[QM linear algebra#Orthonormal basis expansion|previously considered]] an observable $\hat O$ and understood that knowing its possible outcomes gives the spectrum $w_i$ of its eigenvalues, which leads to a complete basis. We now consider the generalisation of this notion to a continuous spectrum of eigenvalues, forming an infinite dimensional Hilbert space. Consider a discretuum of possible $x$ values labelled $i$ on a finite interval. We have a Hermitian position operator $\hat x$ with its discrete spectrum $x_i$ and corresponding eigenbasis $|x_i\rangle$, so we write:$$\Huge \hat x |x_i\rangle=x_i |x_i\rangle$$where $i=1,\dots,N$ and the total interval length is expressed as $L=N\delta x$. We can then form a complete basis such that any state is written as:$$\Huge\begin{align*}
|\psi\rangle&=\sum_{i=0}^N c_i |x_i\rangle\\
&=\sum_{i=0}^N \langle x_i|\psi\rangle |x_i\rangle
\end{align*}$$The probability of finding the particle in the $i$th position is then $P_i=|c_i|^2$
  