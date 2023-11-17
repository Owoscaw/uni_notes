
# Definition and interpretation:

When an experiment is repeated $n$ times, $x_1, x_2, \dots, x_n$ is the sample, then the sample mean is given by:$$\Huge \frac{1}{n}\sum_{i=1}^nx_i$$
Intuitively, the limit of the sample mean as $n\to\infty$ should converge. This value is called the expectation of the experiment.

For any real valued [[Random variables|random variable]], $X$, the expectation denoted as $\mathbb{E}(X)$ is defined as:$$\Huge \mathbb{E}(X):=\begin{cases}{\displaystyle\sum_{x\in\mathcal{X}}x\,p(x)}&\text{if}\,\,X\,\,\text{is discrete}\\{\displaystyle\int_{-\infty}^\infty x\,f(x)dx}&\text{if}\,\,X\,\,\text{is continuous}\end{cases}$$
Where $p(x)$ is the [[Random variables#Discrete random variables|PMF]] of $X$, and $f(x)$ is the [[Random variables#Continuous random variables|PDF]] of $X$. Example: $X\sim U(a, b)$, then:$$\Huge f_X(x)=\frac{1}{b-a}\,\,\forall x\in[a,b]$$$$\Huge \mathbb{E}(X)=\int_{-\infty}^\infty xf(x)dx=\frac{1}{b-a}\int_a^bxdx$$
