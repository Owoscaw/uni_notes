Given two [[Random variables|random variables]] $X,Y$ both defined on $\Omega$, that is $X:\Omega\mapsto X(\Omega)$ and $Y:\Omega\mapsto Y(\Omega)$. Then $(X,Y):\Omega\mapsto(X,Y)(\Omega)$, defined as:$$\Huge (X,Y)(\omega):=(X(\omega),Y(\omega))$$
Here, $W=X,Y$ is called a bivariate random variable. This interacts with [[Probability definition|probability]] in the following manner:$$\large \mathbb{P}(\{X=x,Y=x\})=\mathbb{P}(\{\omega:X(\omega)=x,Y(\omega)=y\})=\mathbb{P}(\{\omega:X(\omega)=x\}\cap\{\omega:Y(\omega)=y\})$$
So we get:$$\Huge \mathbb{P}(\{X=x,Y=y\})=\mathbb{P}((X=x)\cap(Y=y))$$
Two random variables $X$ and $Y$ on the same sample space $\Omega$ are independent if:$$\Huge \mathbb{P}(X\in A, Y\in B)=\mathbb{P}(X\in A)\mathbb{P}(Y\in B)$$

# Jointly distributed discrete random variables:

Let $(X,Y)$ be a bivariate random variable, with:$$\Huge \mathbb{P}((X,Y)\in\mathcal{Z})=1$$
Where $\mathcal{Z}\subseteq(X,Y)(\Omega)$. The joint [[Random variables#Discrete random variables|PMF]] 