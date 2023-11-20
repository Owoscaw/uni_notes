
# Definition and interpretation:

When an experiment is repeated $n$ times, $x_1, x_2, \dots, x_n$ is the sample, then the sample mean is given by:$$\Huge \frac{1}{n}\sum_{i=1}^nx_i$$
Intuitively, the limit of the sample mean as $n\to\infty$ should converge. This value is called the expectation of the experiment.

For any real valued [[Random variables|random variable]], $X$, the expectation denoted as $\mathbb{E}(X)$ is defined as:$$\Huge \mathbb{E}(X):=\begin{cases}{\displaystyle\sum_{x\in\mathcal{X}}x\,p(x)}&\text{if}\,\,X\,\,\text{is discrete}\\{\displaystyle\int_{-\infty}^\infty x\,f(x)dx}&\text{if}\,\,X\,\,\text{is continuous}\end{cases}$$
Where $p(x)$ is the [[Random variables#Discrete random variables|PMF]] of $X$, and $f(x)$ is the [[Random variables#Continuous random variables|PDF]] of $X$. Example: $X\sim U(a, b)$, then:$$\Huge f_X(x)=\frac{1}{b-a}\,\,\forall x\in[a,b]$$$$\Huge \mathbb{E}(X)=\int_{-\infty}^\infty xf(x)dx=\frac{1}{b-a}\int_a^bxdx=\frac{a+b}{2}$$
For $Z\sim\mathcal{N}(0,1)$, then:$$\Huge \mathbb{E}(Z)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty ze^{-\frac{z^2}{2}}dz=0,\,\text{Since}\,ze^{-\frac{z^2}{2}}\,\text{is odd}$$

# Expectations of functions of random variables:

The low of the Unconscious Statistician (LOTUS) states that for a random variable $X:\Omega\mapsto\Re$ and a function $g:X(\Omega)\mapsto \Re$:$$\Huge \mathbb{E}(g(X))=\begin{cases}\displaystyle{\sum g(x)p(x)}&\text{if}\,X\,\text{is discrete}\\\displaystyle{\int g(x)f(x)}&\text{if}\,X\,\text{is continuous}\end{cases}$$
Where $p(x)$ is the PMF and $f(x)$ is the PDF of $X$. This is proven in the discrete case by considering the following:$$\Huge \mathbb{P}(g(X)=y|X=x)=\begin{cases}1&\text{if}\,y=g(x)\\0&\text{elsewhere}\end{cases}=1_{\{g(X)=y\}}$$
$$\Huge \mathbb{P}(g(X)=y)=\$$