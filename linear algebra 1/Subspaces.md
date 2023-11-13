
A subspace, $U$, of [[Vector space definitions|$\Re^n$]] is a subset, $U\subseteq\Re^n$ that satisfies:
> $\underline 0\in U$, existence of the origin
> If $\underline u,\underline v\in U$, then $\underline u+\underline v\in U$, closure under addition
> If $\underline v\in U$ and $\lambda\in\Re$, then $\lambda\underline v\in U$, closure under scalar multiplication

Trivial examples of subspaces are $\{\underline 0\}\subseteq\Re^n$, and $\Re^n\subseteq\Re^n$. [[Lines in R3|Lines]] and [[Planes in R3|planes]] are examples of subspaces, they can be defined in any vector space, not just $\Re^2$ or $\Re^3$.

## Homogeneous systems:

Given [[Matrix definition|$A\in M_{m\times n}(\Re)$]], then the solution set is homogeneous to the system $A\underline x=\underline 0$:$$\Huge U=\left\{\underline x\in\Re^n:A\underline x=\underline 0\right\}\subseteq\Re^n$$ 
To prove this, we show solutions in $U$ satisfy all conditions for a subspace:
>Let $\underline u,\underline v\in U$, then:$$\Huge A(\underline u+\underline v)=A\underline u+A\underline v=\underline 0+\underline 0=\underline 0,\,\text{therefore}\,\,\underline u+\underline v\in U$$
>Let $\underline u\in U,\lambda\in\Re$:$$\Huge A(\lambda\underline u)=\lambda(A\underline u)=\lambda\underline 0=\underline 0,\,\text{therefore}\,\,\lambda\underline u\in U$$
>Also note $A\underline 0=\underline 0$, so $\underline 0\in U$, the subspace is not empty.

## Inhomogeneous systems:

The solution to an inhomogeneous system $A\underline x=\underline b$, where $\underline b=0$ is an affine subspace, the solution set is of form:$$\Huge \underline c+U:=\left\{\underline c+\underline u:\underline u\in U\right\}$$
# Spanning sets:

If $\underline u_1,\dots,\underline u_k\in\Re^n$, then $\lambda_1\underline u_1,\dots,\lambda_k\underline u_k\in\Re^n$ is called a linear combination of $\underline u_1,\dots,\underline u_k$. Given $\underline u_1,\dots,\underline u_k\in\Re^n$, then the span of $\underline u_1,\dots,\underline u_k$ is:$$\Huge span(\underline u_1,\dots,\underline u_k):=\{\lambda_1\underline u_1+\dots+\lambda_k\underline u_k:\lambda_1,\dots,\lambda_k\in\Re\}$$
If $U=span(\underline u_1,\dots,\underline u_k)$, then we say $U$ is spanned by $\{\underline u_1,\dots,\underline u_k\}$, the spanning set of $U$. Given all of this, $U\subseteq\Re^n$, that is $U$ is a subspace of $\Re^n$. To prove this, we show it satisfies all closure and non-empty requirements:
> Suppose $\lambda_1,\dots,\lambda_k,\mu_1,\dots,\mu_k,\lambda\in\Re$, then:$$\large \left(\lambda_1\underline u_1+\dots+\lambda_k\underline u_k\right)+\left(\mu_1\underline u_1+\dots+\mu_k\underline u_k\right)=(\lambda_1+\mu_1)\underline u_1+\dots+(\lambda_k+\mu_k)\underline u_k$$ So we have closure under addition.
> $$\Huge \lambda\left(\lambda_1\underline u_1+\dots+\lambda_k\underline u_k\right)=(\lambda\lambda_1)\underline u_1+\dots+(\lambda\lambda_k)\underline u_k$$So we have closure under scalar multiplication.$$\Huge \underline 0=0\underline u_1+\dots+0\underline u_k$$
> Also $0\in span(\underline u_1,\dots,\underline u_k)$, so the span is not empty. All properties are satisfied, therefore the span must be a subspace.

Suppose $\underline u_1,\dots,\underline u_k\in\Re^n$ with:$$\Huge \underline u_i=\begin{pmatrix}u_{1i}\\u_{2i}\\\vdots\\u_{ni}\end{pmatrix}$$
From this, we form the matrix $A=(\underline u_1\,\dots\,\underline u_k)$:$$\Huge A=\begin{pmatrix}u_{11}&u_{12}&\dots&u_{1k}\\u_{21}&u_{22}&\dots&u_{2k}\\\vdots&\vdots&\ddots&\vdots\\u_{n1}&u_{n2}&\dots&u_{nk}\end{pmatrix}$$
Let $\underline\lambda\in\Re^k$, then the following:$$\Huge A\underline\lambda=\begin{pmatrix}\lambda_1u_{11}+\lambda_2u_{12}+\dots+\lambda_ku_{1k}\\\lambda_1u_{21}+\lambda_2u_{22}+\dots+\lambda_ku_{2k}\\\vdots\\\lambda_1u_{n1}+\lambda_2u_{n2}+\dots+\lambda_ku_{nk}\end{pmatrix}=\lambda_1\begin{pmatrix}u_{11}\\u_{21}\\\vdots\\u_{n1}\end{pmatrix}+\dots+\lambda_k\begin{pmatrix}u_{1k}\\u_{2k}\\\vdots\\u_{nk}\end{pmatrix}$$$$\Huge A\underline\lambda=\lambda_1\underline u_1+\dots+\lambda_k\underline u_k$$
This is equivalent to $span(\underline u_1,\dots,\underline u_k)$, so we write:$$\large span(\underline u_1,\dots,\underline u_k)=\left\{A\underline\lambda:\underline\lambda\in\Re^k\right\}=\left\{\underline b\in\Re^n:A\underline\lambda=\underline b\,\text{has a solution}\,\underline\lambda\in\Re^k\right\}$$

Suppose $U=span(\underline u_1,\dots,\underline u_k)\subseteq\Re^n$ and that $u_1\in span(\underline u_2,\dots,\underline u_k)$, then:$$\Huge U=span(\underline u_2,\dots,\underline u_k)$$
This is proven as follows. Set $V=span(\underline u_2,\dots,\underline u_k)$. First we show that $V\subseteq U$ then $U\subseteq V$:
> If $\underline v\in V$. then $\underline v=\lambda_2\underline u_2+\dots+\lambda_k\underline u_k$ for some $\lambda_i\in\Re$, then also $v=0\cdot\underline u_1+\lambda_2\underline u_2+\dots+\lambda_k\underline u_k$, so $\underline v\in U$, then we have $V\subseteq U$.
> Suppose $\underline u\in U$, then $\underline u=\lambda_1\underline u_1+\dots+\lambda_k\underline u_k$ for some $\lambda_i\in\Re$. Since $\underline u_1\in span(\underline u_2,\dots,\underline u_k)$, we also have $\underline u_1=\mu_2\underline u_2+\dots+\mu_k\underline u_k$ for some $\mu_i\in\Re$, then we get:$$\large\underline u=\lambda_1(\mu_2\underline u_2+\dots+\mu_k\underline u_k)+\dots+\lambda_k\underline u_k=(\lambda_1\mu_2+\lambda_2)\underline u_2+\dots+(\lambda_1\mu_k+\lambda_k)\underline u_k$$This is a linear combination of $\underline u_2,\dots,\underline u_k$, so $\underline u\in V$, and we get $U\subseteq V$. 
> Since both sets subset each other, we can say that they are equal, as required.

# Linear independence:

$\underline u_1,\dots,\underline u_k\in\Re^n$ are linearly independent if and only if:$$\Huge \lambda_1\underline u_1+\dots+\lambda_k\underline u_k=\underline 0$$
Has a single unique solution that is $\lambda_1=\dots=\lambda_k=0$. Set $A=\begin{pmatrix}\underline u_1&\dots&\underline u_k\end{pmatrix}\in M_{n\times k}(\Re)$ and $\underline\lambda$ be a column vector of all coefficients, then we have shown that $A\underline\lambda=\lambda_1\underline u_1+\dots+\lambda_k\underline u_k=span(\underline u_1,\dots,\underline u_k)$. So we can then say the set $\{\underline u_1,\dots,\underline u_k\}$ is linearly independent if and only if $A\underline\lambda=\underline 0$ has one unique solution $\underline\lambda=\underline 0$, as this is equivalent to saying that the span of the set has this trivial solution only, as the definition above.

A pair of non-zero vectors $\underline u,\underline v\in\Re^n$ are linearly dependent if and only if one of $\underline u$ or $\underline v$ is a multiple of the other, that is they are colinear. This is proven by showing the implication both ways:
> If $\underline u=\lambda\underline v$, then $1\underline u+(-\lambda)\underline v=\underline 0$, so $$