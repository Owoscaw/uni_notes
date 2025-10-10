
# Motivating examples:

1. The group $U(1)$ derives its name from unitary complex $1\times1$ matrices. Acting with $g$ on a complex number $c$ we define a map:$$\Huge z\rightarrow gz,\,\,g\in U(1),\,\,z\in\mathbb{C}$$where we require that the inner form $|z|^2$ remains unchanged as:$$\Huge |z|^2=\bar zz\rightarrow\bar z\bar ggz=|g|^2|z|^2$$which implies that $g$ is a complex number of modulus one ($|g|^2=1$), therefore we can write $g=e^{i\varphi}$. Hence $U(1)$ is the group of complex numbers of unit modulus with multiplication as the group operation. We can prove this using the definition of a group. $g=1$ acts as the identity element for this group. The product of two complex numbers with unit modulus also has unit modulus, so we satisfy $x,y\in G\implies x\circ y\in G$. Complex numbers are associative under multiplication, so we satisfy associativity automatically. For $g=e^{i\varphi}$ we write $g^{-1}=e^{-i\varphi}$ and we see that $g\circ g^{-1}=e^{i\varphi}e^{-i\varphi}=e^0=1$, satisfying the inverse requirement for a group. Hence $U(1)$ is indeed a group under multiplication.
2. We saw that a map from $\Re$ to $U(1)$ by writing $g=e^{i\varphi}$ is not an isomorphism. That is, we cannot simply do calculus on $\Re$ and map that to $U(1)$, this is an example of a manifold.
3. When $\varphi\to0$ we can approximate the exponential map to linear order to get:$$\Huge z\rightarrow(1+i\varphi)z$$Note that this approximation is tangent to $U(1)$ at $g=1$. We can try to reconstruct finite elements of $U(1)$ by repeated infinitesimal transformations. Considering $(1+i\varphi/n)^n$ as our map, we see that as $n\to\infty$ the map is reconstructed. More formally:$$\Huge\begin{align}
\lim_{n\to\infty}(1+i\varphi/n)^n&=\lim_{n\to\infty}\sum_{k=0}^n\frac{(i\varphi)^k}{n^k}{n\choose k}\\
&=\lim_{n\to\infty}\sum_{k=0}^n\frac{(i\varphi)^k}{n^k}\frac{n!}{(n-k)!k!}\\
&=\lim_{n\to\infty}\sum_{k=0}^n\frac{(i\varphi)^k}{k!}=e^{i\varphi}
\end{align}$$where we have used the fact that the term $\frac{n!}{(n-k)!n^k}$ will tend to one in the limiting case.

