
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


