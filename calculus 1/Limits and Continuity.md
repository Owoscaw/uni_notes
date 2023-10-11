
# Limits:

A function, $f$, has a limit, $L$, at a point $x=a$ if $f(x)$ is always close to $L$ whenever $x$ is close to $a$. More precisely, if there is an acceptable error $\epsilon \in\Re$, $\epsilon > 0$, between $f(x)$ and $L$, then the following is required:
$$\Huge |f(x)-L|<\epsilon$$
This is true for all $x$ on some interval around $x=a$ such that $x$ is "close" to $a$. More precisely, if there is a distance $\delta\in\Re$, $\delta >0$ between $x$ and $a$, then the following is required:
$$\Huge |x-a|<\delta$$
Combining the above requirements, a limit can be precisely defined:
$$\Huge \forall\,\epsilon>0\,\exists\,\delta>0:|f(x)-L|<\epsilon\,\,when\,\,0<|x-a|<\delta$$
That is:
$$\Huge \lim_{x\to a}f(x)=a$$
It is not required that $f(a)$ is equal to $L$ or that $f(a)$ is defined, as we are looking at the tendency of the function as $x$ gets arbitrarily close to $a$. $f(x)$ is no more than $\pm\epsilon$ away from $L$ when $x$ is no more than $\pm\delta$ away from $a$. If there is no such $L$, then the limit does not exist.

# Continuity:

A function, $f$, is continuous at a point $a$ if the following are satisfied:
> $f(a)$ exists
> $\lim_{x\to a}f(x)$ exists
> $\lim_{x\to a}f(x)=f(a)$