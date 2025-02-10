
A homomorphism of [[Basics of groups|group]]s is a map $\varphi:G\rightarrow G'$ between two groups, $G$ and $G'$ such that:$$\Huge \varphi(g_1g_2)=\varphi(g_1)\varphi(g_2)\,\,\forall g_1,g_2\in G$$
An isomorphism of groups is a homomorphism of groups that is bijective. Groups $G,G'$ are isomorphic to each other if there exists an isomorphism between them, in such case we write:$$\Huge G\cong G'$$

The kernel of a group homomorphism is the set:$$\Huge \ker\varphi=\{g\in G:\varphi(g)=e\}$$The image of a group is the set:$$\Huge \text{im }\varphi=\{\varphi(g):g\in G\}$$
Given a group homomorphism $\varphi:G\rightarrow G'$, the kernel $\ker\varphi$ is then a normal [[Basics of groups#Subgroups|subgroup]] of $G$.

Let $N$ be a normal subgroup of $G$. Then we define the quotient group of $G$ with respect to $N$ as the group induced from $G$ on the cosets:$$\Huge G/N=\{gN:g\in G\}$$with the group operation:$$\Huge g_1N\cdot g_2N=g_1g_2N$$To show that this is well defined, we aim to show that for $g_1N=h_1N,g_2N=h_2N$ we have $g_1g_2N=h_1h_2N$. We have that $g_1\in h_1N\implies g_1=h_1n_1$ for some $n_1\in N$. Similarly we have $g_2=h_2n_2$ for some $n_2\in N$. Then:$$\Huge\begin{align}
g_1g_2N&=h_1n_1h_2n_2N\\
&=h_1h_2\tilde n_1n_2N\\
&=h_1h_2N
\end{align}$$So the operation is well defined.