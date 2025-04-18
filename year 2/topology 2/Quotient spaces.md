
Let $X$ be a set and $\sim$ an equivalence relation on $X$. We define $X/\sim$ to be the set of equivalence classes of $\sim$. For $x\in X$ we write:$$\Huge [x]=\{y\in X:y\sim x\},\,\,X/\sim=\{[x]:x\in X\}$$We also define the surjective map:$$\Huge \pi:X\rightarrow X/\sim,\,\,x\mapsto[x]$$which takes elements of $x$ to their equivalence class. Take for example $X=\Re^3$ and define the equivalence relation $(x_1,y_1,z_1)\sim(x_2,y_2,z_2)\iff z_1=z_2$, then $[(a,b,c)]=\{(x,y,z)\in\Re^3:z=c\}$. The elements of $\Re^3/\sim$ are therefore the planes with constant $z$ coordinate, the horizontal planes. Therefore the map $\pi:\Re^3\rightarrow\Re^3/\sim$ sends any point to the horizonal plane it is in.

Suppose that $X$ is a [[Topological spaces#Topologies|topological space]] and $\sim$ is an equivalence relation on $X$. Then we give $X/\sim$ the quotient topology defined as:$$\Huge U\subseteq X/\sim\text{ is open}\iff \pi^{-1}(U)\text{ is open in }X$$We call $X/\sim$ with such topology a quotient space and the map $\pi$ a quotient map. We propose that this defines a topology on $X$.

The topology on $X/\sim$ is the largest such that $\pi$ is continuous. To prove this, note that the definition of a topology on $X/\sim$ ensures $\pi$ is continuous and that adding any extra open sets in $X/\sim$ would make $\pi$ discontinuous.

Suppose that $X$ is a space with equivalence relation $\sim$ and $Y$ is some other space. Then a map $f:X/\sim\rightarrow Y$ is continuous if and only if $f\circ\pi:X\rightarrow Y$ is continuous. Note that both $f,\pi$ are continuous, so $f\circ\pi$ is also continuous. To prove the converse, let $U\subseteq Y$ be open, then if $f\circ\pi$ is continuous we have $\pi^{-1}(f^{-1}(U))=(f\circ\pi)^{-1}(U)$ is open in $X$. Now by the definition of the topology on $X/\sim$ we have $f^{-1}(U)$ is open in $X/\sim$ as required.

Consider $\Re$ with its standard topology and the equivalence relation defined by $x\sim y\iff x-y\in\mathbb{Z}$. Then $\Re/\sim$ is [[Topological spaces#Homeomorphisms|homeomorphic]] to the circle $S^1$. This is the same as coiling an infinite rope into a circle. We start the proof by defining the map $\exp:\Re\rightarrow S^1\subseteq\mathbb{C}$ by $\exp(t)=e^{2\pi it}$. We look for a corresponding map $\overline\exp:\Re/\sim\rightarrow S^1$ defined as $\overline\exp([t])=\exp(t)$. We must first check that this is well defined:$$ [s]=[t]\iff s-t=k\in\mathbb{Z}\iff\overline\exp([s])=e^{2\pi is}=e^{2\pi i(k+t)}=e^{2\pi ik}e^{2\pi it}=e^{2\pi it}=\overline\exp([t])$$so we see this map is well defined and bijective. So we know that the maps:$$\Huge\begin{align}
\Re\rightarrow^{\pi}&\Re/\sim\rightarrow^{\overline\exp}S^1\\
\Re&\rightarrow^{\exp}S^1
\end{align}$$are the same, that is $\overline\exp\circ\pi=\exp$. We have that $\overline\exp$ is a continuous bijection and since $S^1$ belongs to $\Re^2$ which is a metric space and therefore Hausdorff, so $S^1$ is Hausdorff. Notice that all of $\Re$ is not necessary to make $\Re/\sim$, that is $\pi([-a,a])=\Re/\sim$ and since $[-a,a]$ is compact and $\pi$ is continuous we have that $\Re/\sim$ is compact. Now we have a Hausdorff space $S^1$ and a compact space $\Re/\sim$ with a continuous bijection between them, so this map ($\overline\exp$) is a homeomorphism as required.

If $A\subseteq X$ then define the equivalence relation $\sim$ by $x\sim y$ if and only if $x=y$ or $x,y\in A$. Then we define $X/A$ to be $X/\sim$.

The $n$-sphere $S^n$ is homeomorphic to $D^n/S^{n-1}$. Note that the closed $n$-ball $D^n$ lives in $\Re^n$ with $S^{n-1}$ is its boundary. In the quotient space, this is reduced to a point. First notice that any point in $D^n$ can be written as $t\cdot\varphi$ where $0\leq t\leq 1$ and $\varphi$ is a point in $S^{n-1}\subseteq\Re^n$. We then define:$$\Huge\begin{align}
f&:D^n\rightarrow S^n\subseteq\Re^{n+1}\\
f(t\cdot\varphi)&=(\cos(\pi t),\varphi\sin(\pi t))\in\Re\times\Re^n=\Re^{n+1}
\end{align}$$so we have that:$$\Huge\begin{align}
f(0\cdot\varphi)&=(1,\underline 0)\\
f(1/2\cdot\varphi)&=(0,\varphi)\\
f(1\cdot\varphi)&=(-1,\underline 0)
\end{align}$$where $\underline 0,\varphi$ are vectors in $\Re^n$. Now we aim to find a map $\bar f:D^n/S^{n-1}\rightarrow S^n$, defined by $\bar f([t\cdot\varphi])=f(t\cdot\varphi)$. We now show that it is both well defined and injective as follows, assume $t_1\cdot\varphi_1\neq t_2\cdot\varphi_2$:$$\large\begin{align}
[t_1\cdot\varphi_1]=[t_2\cdot\varphi_2]\iff t_1\cdot\varphi_1,t_2\cdot\varphi_2\in S^{n-1}&\iff t_1=1=t_2\\
&\iff f(t_1\cdot\varphi_1)=(-1,\underline 0)=f(t_2\cdot\varphi_2)\\
&\iff \bar f([t_1\cdot\varphi_1])=\bar f([t_2\cdot\varphi_2])
\end{align}$$It is also easy to see that $f$ is surjective (and therefore $\bar f$). We know that:$$\Huge\begin{align}
D^n\rightarrow^\pi D^n/S^{n-1}&\rightarrow^{\bar f}S^n\\
D^n\rightarrow^fS^n&
\end{align}$$are the same maps, that is $\bar f\circ\pi=f$ and since $f$ is continuous, so is $\bar f$. $S^n$ is Hausdorff as it belongs to $\Re^{n+1}$. $D^n\subseteq\Re^n$ is closed and bounded and therefore is compact, so $D^n/S^{n-1}$ is compact as $\pi$ is continuous. We have the required conditions to call $\bar f$ a homeomorphism.
 