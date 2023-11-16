Given two [[Random variables|random variables]] $X,Y$ both defined on $\Omega$, that is $X:\Omega\mapsto X(\Omega)$ and $Y:\Omega\mapsto Y(\Omega)$. Then $(X,Y):\Omega\mapsto(X,Y)(\Omega)$, defined as:$$\Huge (X,Y)(\omega):=(X(\omega),Y(\omega))$$
Here, $W=X,Y$ is called a bivariate random variable. This interacts with [[Probability definition|probability]] in the following manner:$$\large \mathbb{P}(\{X=x,Y=x\})=\mathbb{P}(\{\omega:X(\omega)=x,Y(\omega)=y\})=\mathbb{P}(\{\omega:X(\omega)=x\}\cap\{\omega:Y(\omega)=y\})$$
So we get:$$\Huge \mathbb{P}(\{X=x,Y=y\})=\mathbb{P}((X=x)\cap(Y=y))$$
Two random variables $X$ and $Y$ on the same sample space $\Omega$ are independent if:$$\Huge \mathbb{P}(X\in A, Y\in B)=\mathbb{P}(X\in A)\mathbb{P}(Y\in B)$$

# Jointly distributed discrete random variables:

Let $(X,Y)$ be a bivariate discrete random variable, with:$$\Huge \mathbb{P}((X,Y)\in\mathcal{Z})=1$$
Where $\mathcal{Z}\subseteq(X,Y)(\Omega)$. The joint [[Random variables#Discrete random variables|PMF]] is defined as:$$\Huge p_{X,Y}(x,y)=\mathbb{P}(X=x,Y=y),\,\text{for}\,\,(x,y)\in\mathcal{Z}$$
Each variable's PMF can be given in terms of the joint PMF:$$\Huge p_X(x)=\sum_{y\in\mathcal{Y}}p_{X,Y}(x,y),\,\,p_Y(y)=\sum_{x\in\mathcal{X}}p_{X,Y}(x,y),\,\forall x\in\mathcal{X},\,\forall y\in\mathcal{Y}$$
This also leads to the definition:$$\Huge \mathbb{P}((X,Y)\in A)=\sum_{(x,y)\in A}p_{X,Y}(x,y),\,\sum_{(x,y)\in\mathcal{Z}}p_{X,Y}(x,y)=1$$
## [[Conditional probability]]:

Let $X$ and $Y$ be discrete random variables, then the conditional probability mass function of $X$ given $Y$ is defined as:$$\Huge p_{X|Y}(x|y)=\mathbb{P}(X=x|Y=y)=\frac{\mathbb{P}(X=x,Y=y)}{\mathbb{P}(Y=y)}=\frac{p_{X,Y}(x,y)}{p_Y(y)}$$
Given $p_Y(y)>0$. The definition for the conditional probability mass function of $Y$ given $X$ is defined similarly.

## [[Probability definition#Partitions|Partition theorem]]:

Let $X$ and $Y$ be discrete random variables, then then:$$\Huge p_X(x)=\sum_{y\in\mathcal{Y}}p_{X|Y}(x|y)p_Y(y)$$
Since:$$\Huge p_X(x)=\mathbb{P}(X=x)=\sum_{y\in\mathcal{Y}}P(X=x|Y=y)\mathbb{P}(Y=y)=\sum_{y\in\mathcal{Y}}p_{X|Y}(x|y)p_Y(y)$$
## [[Conditional probability#Independence|Independence]]:

Given two independent discrete random variables, $X$ and $Y$:$$\Huge p_{X|Y}(x|y)=p_X(x)$$
Then we also have, that if $X$ and $Y$ are independent $\iff$:
$$\Huge p_{X,Y}(x,y)=p_X(x)p_Y(y),\,\forall x\in\mathcal{X},\,\forall y\in\mathcal{Y}$$$$\Huge p_{X|Y}(x|y)=p_X(x),\,p_{Y|X}(y|x)=p_Y(y),\,\forall x\in\mathcal{X},\,\forall y\in\mathcal{Y},\,p_X(x),p_Y(y)>0$$
This is proven as follows, by the definition of independence we have:$$\large p_{X,Y}(x,y)=\mathbb{P}(X\in A,Y\in B)=\sum_{x\in A}\sum_{y\in B}p_{X,Y}(x,y)=\left(\sum_{x\in A}p_X(x)\right)\left(\sum_{y\in B}p_Y(y)\right)$$$$\Huge \implies p_{X,Y}(x,y)=\mathbb{P}(X\in A)\mathbb{P}(Y\in B)=p_X(x)p_Y(y)$$

# Jointly distributed continuous random variables:

Continuous random variables $X:\Omega\mapsto\Re$ and $Y:\Omega\mapsto\Re$ are jointly continuous if $\exists f:\Re^2\mapsto[0,\infty)$ such that:$$\large \mathbb{P}(X\in[a,b],Y\in[c,d])=\int_a^b\int_c^df(x,y)dxdy,\,a<b,\,c<d,\,\forall[a,b]\times[c,d]\subseteq\Re^2$$
If $B=[a,b]\times[c,d]$ is a nice [[Integration#Double integrals|region]], then the integral can be written as:$$\Huge f_{X,Y}(x,y)=\mathbb{P}((X,Y)\in B)=\iint_Bf(x,y)dxdy$$
The interpretation of the function $f(x,y)$ is:
$$\Huge \mathbb{P}(X\in[x,x+dx],Y\in[y,y+dy])=f(x,y)dxdy$$
When integrating over the entire plane in $\Re^2$, that is to say $B=[-\infty,\infty]\times[-\infty,\infty]=\Re^2$, then we get:$$\Huge \mathbb{P}((X,Y)\in\Re^2)=\iint_{\Re^2}f(x,y)dxdy=\int_{-\infty}^\infty\int_{-\infty}^\infty f(x,y)dxdy=1$$
