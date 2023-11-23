
# Definition and interpretation:

When an experiment is repeated $n$ times, $x_1, x_2, \dots, x_n$ is the sample, then the sample mean is given by:$$\Huge \frac{1}{n}\sum_{i=1}^nx_i$$
Intuitively, the limit of the sample mean as $n\to\infty$ should converge. This value is called the expectation of the experiment.

For any real valued [[Random variables|random variable]], $X$, the expectation denoted as $\mathbb{E}(X)$ is defined as:$$\Huge \mathbb{E}(X):=\begin{cases}{\displaystyle\sum_{x\in\mathcal{X}}x\,p(x)}&\text{if}\,\,X\,\,\text{is discrete}\\{\displaystyle\int_{-\infty}^\infty x\,f(x)dx}&\text{if}\,\,X\,\,\text{is continuous}\end{cases}$$
Where $p(x)$ is the [[Random variables#Discrete random variables|PMF]] of $X$, and $f(x)$ is the [[Random variables#Continuous random variables|PDF]] of $X$. Example: $X\sim U(a, b)$, then:$$\Huge f_X(x)=\frac{1}{b-a}\,\,\forall x\in[a,b]$$$$\Huge \mathbb{E}(X)=\int_{-\infty}^\infty xf(x)dx=\frac{1}{b-a}\int_a^bxdx=\frac{a+b}{2}$$
For $Z\sim\mathcal{N}(0,1)$, then:$$\Huge \mathbb{E}(Z)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty ze^{-\frac{z^2}{2}}dz=0,\,\text{Since}\,ze^{-\frac{z^2}{2}}\,\text{is odd}$$

# Expectations of functions of random variables:

The low of the Unconscious Statistician (LOTUS) states that for a random variable $X:\Omega\mapsto\Re$ and a function $g:X(\Omega)\mapsto \Re$:$$\Huge \mathbb{E}(g(X))=\begin{cases}\displaystyle{\sum_{x\in\mathcal X} g(x)p(x)}&\text{if}\,X\,\text{is discrete}\\\displaystyle{\int_{-\infty}^\infty g(x)f(x)}&\text{if}\,X\,\text{is continuous}\end{cases}$$
Where $p(x)$ is the PMF and $f(x)$ is the PDF of $X$. This is proven in the discrete case by considering the following:$$\large p_{g(X)}(y)=\mathbb{P}(g(X)=y)=\sum_{x\in\mathcal{X}}\mathbb{P}(g(X)=y|X=x)\mathbb{P}(X=x)=\sum_{x\in\mathcal{X}:g(x)=y}p(x)$$$$\Huge \mathbb{P}(g(X)=y|X=x)=\begin{cases}1&\text{if}\,y=g(x)\\0&\text{elsewhere}\end{cases}=1_{\{g(X)=y\}}$$$$\large \mathbb{E}(g(X)=\sum_{y\in g(\mathcal{X})}yp_{g(X)}(y)=\sum_{y\in g(\mathcal{X})}y\left(\sum_{x\in\mathcal X:g(x)=y}p(x)\right)=\sum_{y\in g(\mathcal{X})}\left(\sum_{x\in\mathcal{X}:g(x)=y}yp(x)\right)$$$$\Huge =\sum_{x\in\mathcal{X}}\left(\sum_{y\in g(\mathcal X):y=g(x)}yp(x)\right)=\sum_{x\in\mathcal X}\left(\sum_{y\in g(\mathcal x):y=g(x)}y\right)p(x)=\sum_{x\in\mathcal X}g(x)p(x)$$
So we have the above definition for the discrete case. Now for multiple random variables, $X$ and $Y$ that take values $\mathcal X$ and $\mathcal Y$, and any function $\mathcal X\times\mathcal Y\mapsto\Re$:$$\Huge \mathbb{E}(g(X,Y))=\begin{cases}\displaystyle{\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y}g(x,y)p(x,y)}&\text{if}\,X,Y\,\text{are discrete}\\\displaystyle{\iint_{\Re^2}g(x,y)f(x,y)}&\text{if}\,X,Y\,\text{are continuous}\end{cases}$$
# Linearity of Expectation:

Let $X$ be a random variable, taking real values. Now let $\alpha,\beta\in\Re$:$$\Huge \mathbb{E}(\alpha X+\beta Y)=\alpha\mathbb{E}(X)+\beta\mathbb{E}(Y)$$
This implies:
>$\mathbb{E}(\alpha X+\beta)=\alpha\mathbb{E}(X)+\beta$
>$\mathbb{E}(X+Y)=\mathbb{E}(X)+\mathbb{E}(Y)$
>$$\Huge \mathbb{E}\left(\sum_{i=1}^n X_i\right)=\sum_{i=1}^n\mathbb{E}(X_i)$$

For the discrete case, this is proven by:$$\Huge \mathbb{E}(g(X,Y))=\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y}(x+y)p(x,y)=\sum_{x\in\mathcal X}x\sum_{y\in\mathcal Y}p(x,y)+\sum_{y\in\mathcal Y}y\sum_{x\in\mathcal X}p(x,y)$$$$\Huge =\sum_{x\in\mathcal X}xp_X(x)+\sum_{y\in\mathcal Y}yp_Y(y)=\mathbb{E}(X)+\mathbb{E}(Y)$$

# Variance and Co-Variance:

The variance of a random variable $X$ is defined as:$$\Huge var(X)=\mathbb{E}[(X-\mathbb{E}(X))^2]$$
And the standard deviation of $X$ is defined as:$$\Huge sd(X)=\sqrt{var(x)}$$
By LOTUS, we have:$$\Huge var(X)=\begin{cases}\displaystyle{\sum_{x\in\mathcal X}(x-\mathbb{E}(x))^2p(x)}&\text{if}\,X\,\text{is discrete}\\\displaystyle{\int_{-\infty}^\infty(x-\mathbb{E}(x))^2f(x)dx}&\text{if}\,X\,\text{is continuous}\end{cases}$$
The co-variance between two random variables $X$ and $Y$ is defined by:$$\Huge cov(X,Y)=\mathbb{E}[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])]=cov(Y,X)$$
This gives the result:$$\Huge cov(X,X)=var(X)$$
The interpretation of this is:
> $cov(X,Y)>0$ implies that both $X>\mathbb{E}[X]$ and $Y>\mathbb{E}[Y]$, they are positively correlated
> $cov(X,Y)<0$ implies the opposite, they are negatively correlated
> $cov(X,Y)=0$ implies they are uncorrelated

By LOTUS we have:$$\Huge cov(X,Y)=\begin{cases}\displaystyle{\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y}}(x-\mathbb{E}[x])(y-\mathbb{E}[y])p(x,y)&\text{if}\,X,Y\,\text{are discrete}\\\displaystyle{\iint_{\Re^2}(x-\mathbb{E}[x])(y-\mathbb{E}[y])dydx}&\text{if}\,X,Y\,\text{are continuous}\end{cases}$$
It immediately follows that for $\alpha,\beta,\gamma,\delta\in\Re$:$$\Huge var(\alpha+\beta X)=\beta^2var(X)$$$$\Huge cov(\alpha+\beta X,\gamma+\delta Y)=\beta\delta cov(X,Y)$$$$\Huge cov(X+Y,Z)=cov(X,Z)+cov(Y,Z)$$
$$\Huge cov(X,Y+Z)=cov(X,Y)+cov(X,Z)$$
These results come from the linearity of expectation. This can also be used to obtain an alternative formula for variance:$$\large var(X)=\mathbb E[(X-\mathbb E[X])^2]=\mathbb E[X^2-2X\mathbb E[X]+(\mathbb E[X])^2]=\mathbb E[X^2]-2\mathbb E[X]\mathbb E[X]+(\mathbb E[X])^2$$$$\Huge var(X)=\mathbb E[X^2]-(\mathbb E[X])^2$$
For any real valued random variables $X$ and $Y$:$$\large cov(X,Y)=\mathbb E[(X-\mathbb E[X])(Y-\mathbb E[Y])]=\mathbb E[XY-X\mathbb E[Y]-Y\mathbb E[X]+\mathbb E[X]\mathbb E[Y]]$$$$\Huge cov(X,Y)=\mathbb E[XY]-2\mathbb E[X]\mathbb E[Y]+\mathbb E[X]\mathbb E[Y]=\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]$$
Similarly, we also get:$$\Huge var(X+Y)=cov(X+Y,X+Y)=cov(X+Y,X)+cov(X+Y,Y)$$$$ var(X+Y)=cov(X,X)+cov(Y,X)+cov(X,Y)+cov(Y,Y)=var(X)+var(Y)+2cov(X,Y)$$
This implies the general case, where:$$\Huge var\left(\sum_{i=1}^nX_i\right)=\sum_{i=1}^nvar(X_i)+2\sum_{i=1}^{n-1}\sum_{j=i+1}^ncov(X_i,X_j)$$

# Conditional expectation:

Note that the expectation of an [[Random variables#Indicator random variables|indicator random variable]], $1_A$ is given by:$$\Huge \mathbb E[1_A]=1\times\mathbb P(\omega\in A)+0\times\mathbb P(\omega\in A^c)=\mathbb P(\omega\in A)=\mathbb P(A)$$
Now let $X$ be a real valued random variable, the conditional expectance of $X$ given an event $A\subseteq\Omega$ is given by:$$\Huge \mathbb E[X|A]=\frac{\mathbb E[X1_A]}{\mathbb P(A)},\,\,\text{for}\,\,\mathbb P(A)>0$$This comes from the formula for [[Conditional probability#Bayes' theorem|conditional probability]]:$$\Huge \mathbb P(A\cap B)=\mathbb E[1_{A\cap B}]=\mathbb E[1_A\cdot1_B]=\mathbb P(B)\mathbb P(A|B)$$
For the general case, we get:$$\Huge \mathbb E[X|A]=\sum_{x\in\mathcal X}x\mathbb P(X=x|A)$$
This is proven by letting $Y=X1_A$, then for $x\neq 0$ we get:$$\Huge \mathbb P(Y=1)=\mathbb P(\{X=x\}\cap A)=$$