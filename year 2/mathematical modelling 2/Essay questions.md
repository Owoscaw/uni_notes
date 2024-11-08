
# Question 1
$$\Huge\begin{align}
T_i&=S_i+I_i+R_i+F_i\\
T_{i+1}&=S_{i+1}+I_{i+1}+R_{i+1}+F_{i+1}\\
&=(S_i-\Delta I_i)+(I_i+\Delta I_i-\Delta I_{i-d})\\&+(R_i+(1-K_f)\Delta I_{i-d})+(F_i+K_f\Delta I_{i-d})\\
&=S_i+I_i+R_i+F_i\\
&+(\Delta I_i-\Delta I_i+\Delta I_{i-d}-\Delta I_{i-d}+K_f\Delta I_{i-d}-K_f\Delta I_{i-d})\\
&=S_i+I_i+R_i+F_i=T_i
\end{align}$$
# Question 2

As $R$ is decreased from $3$ to $2$ we see that the infected population peaks later on in the model and to a lesser degree. At $R=1,0.9$ we see that the infected population peaks very early on and to a much lesser degree than $R=3,2$.

# Question 3

Assuming $d<0$ and both $P_{\text{Inc}}(d),P_{R}(d)$ are zero for $d\notin[0,N]$ we have:$$\Huge P_r(d)=\sum_{n=0}^dP_{\text{Inc}}(n)P_R(d-n)$$Here, $n$ would need to range from $0$ to $d<0$, so the term $P_\text{Inc}(n)$ will be zero for every value in the sum, making the whole expression $0$. 

Since both $P_\text{Inc}(d)$ and $P_R(d)$ are only non-zero on the interval $d\in[0,N]$ we require $n\leq N,d-n\leq N$, as for any value greater than $N$ one of the terms in the sum will be zero:$$\Huge\begin{align}
n\leq N&\implies N+n\leq2N\\d-n\leq N&\implies d\leq N+n\leq2N
\end{align}$$So take $d=2N$ as the greatest value of $d$ for which $P_r(d)$ is non-zero. This corresponds to:$$\Huge P_r(2N)=\sum_{n=0}^{2N}P_\text{Inc}(n)P_R(2N-n)$$This sum only has one non-zero term, when $n=N$. Note that each term in the sum is positive, since they follow a gamma distribution, therefore for all $d$ we have $P_r(d)\geq0$. We know that $P_r(d)=0$ for $d\notin[0,2N]$:$$\Huge\begin{align}
\sum_{d=0}^\infty P_r(d)&=
\end{align}$$

# Question 4

We assume $I_i=A\exp(\lambda i)$:
$$\begin{align}
I_{i+1}&=I_i+R(I_{i-d}-I_{i-d-1})\\A\exp(\lambda(i+1))&=A\exp(\lambda i)+R(A\exp(\lambda(i-d))-A\exp(\lambda(i-d-1)))\\
A\exp(\lambda(i+1))-A\exp(\lambda i)&=R(A\exp(\lambda(i-d))-A\exp(\lambda(i-d-1)))\\
R&=\frac{A\exp(\lambda i+\lambda)-A\exp(\lambda i)}{A\exp(\lambda i-\lambda d)-A\exp(\lambda i-\lambda d-\lambda)}\\
&=\frac{A\exp(\lambda i)(\exp(\lambda)-1)}{A\exp(\lambda i)(\exp(-\lambda d)-\exp(-\lambda d-\lambda))}\\
&=\frac{\exp(\lambda)-1}{\exp(-\lambda d)-\exp(-\lambda d-\lambda)}\\
&=\frac{\exp(\lambda)-1}{\exp(-\lambda d)(1-\exp(-\lambda))}\times\frac{\exp(\lambda)}{\exp(\lambda)}\\&=\frac{\exp(\lambda)(\exp(\lambda)-1)}{\exp(-\lambda d)(\exp(\lambda)-1)}\\
&=\frac{\exp(\lambda)}{\exp(-\lambda d)}\times\frac{\exp(\lambda d)}{\exp(\lambda d)}\\
&=\frac{\exp(\lambda(d+1))}{1}=\exp(\lambda(d+1))
\end{align}$$
The program estimates $\lambda_\text{UK}\approx0.294$ and $\lambda_\text{Brazil}\approx0.0793$. Taking $d=6.5$ we get:$$\Huge\begin{align}
R_\text{UK}&\approx\exp(0.29(6.5+1))\approx8.80\\
R_\text{Brazil}&\approx\exp(0.0793(6.5+1))\approx1.81
\end{align}$$
# Question 5