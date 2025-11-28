
In classical mechanics, the simple harmonic oscillator (SHO) has associated Hamiltonian:$$\Huge H=\frac{p^2}{2m}+\frac{m\omega^2 x^2}{2}\rightarrow\frac{\hat p^2}{2m}+\frac{m\omega^2\hat x^2}{2}$$where we have [[Canonical quantisation of classical systems|quantised]] the system by replacing variables $x,p$ with operators $\hat x,\hat p$.


# Positive definite:

We propose that an operator $\hat B$ that is defined as the sum of squares of [[Operators and Measurement|observable operators]] will have positive definite ($\geq0$) expectation value:
> Consider $\hat B=\hat A^2$ where $\hat A=\hat A^\dagger$:$$\Huge\langle\hat B\rangle= \langle \psi|\hat A^2 |\psi\rangle=\langle \psi|\hat A^\dagger\hat A |\psi\rangle=|\hat A |\psi\rangle|^2\geq0$$
> This is clearly also true if $\hat B$ is the sum of the square of many Hermitian operators.

What this means for our SHO is that $\langle\hat H\rangle\geq0$ and therefore all energy eigenvalues are greater than or equal to $0$.

# Ladder operators:

We define the Ladder operator:$$\Huge \hat a=\frac{1}{\sqrt{2m\hbar\omega}}(m\omega\hat x+i\hat p)$$and proceed by rewriting our operators in terms of it:$$\Huge\hat x=\sqrt{\frac{\hbar}{2m\omega}}(\hat a+\hat a^\dagger),\,\,\hat p=-i\sqrt{\frac{\hbar m\omega}{2}}(\hat a-\hat a^\dagger)$$This makes our commutation relation:$$\Huge\begin{align*}
i\hbar=[\hat x,\hat p]&=-\frac{i\hbar}{2}[\hat a+\hat a^\dagger,\hat a-\hat a^\dagger]\\
&=-\frac{i\hbar}{2}(-[\hat a,\hat a^\dagger]+[\hat a^\dagger,\hat a])\\
&=\frac{i\hbar}{2}([\hat a,\hat a^\dagger]+[\hat a,\hat a^\dagger])=i\hbar[\hat a,\hat a^\dagger]\\
\implies[\hat a,\hat a^\dagger]&=1
\end{align*}$$Now we write the Hamiltonian in terms of $\hat a,\hat a^\dagger$:$$\Huge\begin{align*}
H&=\frac{\hat p^2}{2m}+\frac{m\omega^2}{2}\hat x^2\\
&=\frac{\hbar \omega}{4}(-(\hat a-\hat a^\dagger)^2)+\frac{\hbar\omega}{4}(\hat a+\hat a^\dagger)^2\\
&=\frac{\hbar\omega}{4}(-\hat a^2-(\hat a^\dagger)^2+\hat a^2+(\hat a^\dagger)^2+\hat a\hat a^\dagger+\hat a^\dagger\hat a+\hat a\hat a^\dagger+\hat a^\dagger\hat a)\\
&=\frac{\hbar\omega}{2}(\hat a\hat a^\dagger+\hat a^\dagger\hat a)\\
&=\frac{\hbar\omega}{2}(2\hat a^\dagger\hat a+1)=\hbar\omega\left(\hat a^\dagger\hat a+\frac{1}{2}\right)
\end{align*}$$