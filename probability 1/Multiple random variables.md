Given two [[Random variables|random variables]] $X,Y$ both defined on $\Omega$, that is $X:\Omega\mapsto X(\Omega)$ and $Y:\Omega\mapsto Y(\Omega)$. Then $(X,Y):\Omega\mapsto(X,Y)(\Omega)$, defined as:$$\Huge (X,Y)(\omega):=(X(\omega),Y(\omega))$$
Here, $W=X,Y$ is called a bivariate random variable. This interacts with [[Probability definition|probability]] in the following manner:$$\large \mathbb{P}(\{X=x,Y=x\})=\mathbb{P}(\{\omega:X(\omega)=x,Y(\omega)=y\})=\mathbb{P}(\{\omega:X(\omega)=x\}\cap\{\omega:Y(\omega)=y\})$$
So we get:$$\Huge \mathbb{P}(\{X=x,Y=y\})=\mathbb{P}((X=x)\cap(Y=y))$$
Two random variables $X$ and $Y$ on the same sample space $\Omega$ are independent if:$$\Huge \mathbb{P}(X\in A, Y\in B)=\mathbb{P}(X\in A)\mathbb{P}(Y\in B)$$

# Jointly distributed discrete random variables:

Let $(X,Y)$ be a bivariate discrete random variable, with:$$\Huge \mathbb{P}((X,Y)\in\mathcal{Z})=1$$
Where $\mathcal{Z}\subseteq(X,Y)(\Omega)$. The joint [[Random variables#Discrete random variables|PMF]] is defined as:$$\Huge p_{X,Y}(x,y)=\mathbb{P}(X=x,Y=y),\,\text{for}\,\,(x,y)\in\mathcal{Z}$$
Each variable's PMF can be given in terms of the joint PMF:$$\Huge p_X(x)=\sum_{y\in\mathcal{Y}}p_{X,Y}(x,y),\,\,p_Y(y)=\sum_{x\in\mathcal{X}}p_{X,Y}(x,y),\,\forall x\in\mathcal{X},\,\forall y\in\mathcal{Y}$$
This also leads to the definition:$$\Huge \mathbb{P}((X,Y)\in A)=\sum_{(x,y)\in A}p_{X,Y}(x,y),\,\sum_{(x,y)\in\mathcal{Z}}p_{X,Y}(x,y)=1$$
## [[Conditional probability]] on multiple random variables:

Let $X$ and $Y$ be discrete random variables, then the conditional probability mass function of $X$ given $Y$ is defined as:$$\Huge p_{X|Y}(x|y)=\mathbb{P}(X=x|Y=y)=\frac{\mathbb{P}(X=x,Y=y)}{\mathbb{P}(Y=y)}=\frac{p_{X,Y}(x,y)}{p_Y(y)}$$
Given $p_Y(y)>0$. The definition for the conditional probability mass function of $Y$ given $X$ is defined similarly.

## [[Probability definition#Partitions|Partition theorem]] on multiple random variables:

Let $X$ and $Y$ be discrete random variables, then then:$$\Huge p_X(x)=\sum_{y\in\mathcal{Y}}p_{X|Y}(x|y)p_Y(y)$$
Since:$$\Huge p_X(x)=\mathbb{P}(X=x)=\sum_{y\in\mathcal{Y}}P(X=x|Y=y)\mathbb{P}(Y=y)=\sum_{y\in\mathcal{Y}}p_{X|Y}(x|y)p_Y(y)$$
## [[Conditional probability#Independence|Independece]] on multiple random variables:

Given two independent discrete random variables, $X$ and $Y$:$$\Huge p_{X|Y}(x|y)=p_X(x)$$
Then we also have, that if $X$ and $Y$ are independent $\iff$:
$$\Huge p_{X,Y}(x,y)=p_X(x)p_Y(y)$$$$\Huge p_{X|Y}(x|y)=p_X(x),\,p_{Y|X}(y|x)=p_Y(y)$$