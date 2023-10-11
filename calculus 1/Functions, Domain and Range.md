A function $f$ is defined to be a correspondence between two sets, the domain $D$ and the codomain $C$. Each element of $D$ is assigned to one and only one element in $C$. If this is not satisfied, then the mapping is not a function.

When $x\in D$, $f(x)$ is used to denote the assigned element in $C$. This is the value of $f$ for the input $x$, otherwise known as the image of $x$ under the function $f$:
$$\Huge f:D\mapsto C:x\mapsto f(x)$$$$\Huge \forall x\in D,\,\,f(x)\in C$$
The range of $f$ is the collection of all images produced by its mapping. That is to say:
$$\Huge Ran\,\,f=\left\{f(x):x\in D\right\}$$
$$\Huge Ran\,\,f\subseteq Codom\,\,f$$

# Graphs:

The graph of a function is the set of all [[Definition of the reals|real]] ordered pairs, $(x,y)\in\Re^2:x\in\,Dom\,\,f$, $y=f(x)$. Domains are often restricted to an interval $[a,b]$, so that they can be sketched. When necessary, a shaded circle is used to represent a point included in the set, while an open circle is used to represent a point excluded from the set.

# Even and Odd functions:

A function is even if:
$$\Huge f(x)=f(-x)\,\,\forall x\in Dom\,\,f$$
A function is odd if:
$$\Huge f(x)=-f(-x)\,\,\forall x\in Dom\,\,f$$
Every function can be written of its odd and even parts, that is:
$$\Huge f(x)=f_{even}(x)+f_{odd}(x)$$
Where:
$$\Huge f_{even}(x)=\frac{1}{2}(f(x)+f(-x))$$
$$\Huge f_{odd}(x)=\frac{1}{2}(f(x)-f(-x))$$
Note that $f(x)=0$ is both even and odd.

# Piecewise Functions:

Some functions are defined piecewise, having different expressions for different intervals over its domain:
$$\Huge f(x)=\begin{cases}g(x)&a\leq x\leq b\\h(x)&b<x\leq c\end{cases}$$
Where $Dom\,\,f=[a,c]$.

A step function is constant on each piece (piecewise constant). The following is the basic step function, known as the Heaviside step function:
$$\Huge H(x)=\begin{cases}0&x<0\\1&x>0\end{cases}$$
Here, $H(x)$ is undefined for $x=0$, that is $Dom\,H(x)=\Re\setminus \{0\}$.

# Function operations:

Given two function, $f,g$, and a constant $c\in\Re$ the following are function operations:
> Sum $(f+g)$:$$\Huge (f+g)(x)=f(x)+g(x),\,\,Dom\,(f+g)=Dom\,f\cap Dom\,g$$
> Difference $(f-g)$:$$\Huge (f-g)(x)=f(x)-g(x),\,\,Dom\,(f-g)=Dom\,f\cap Dom\,g$$
> Product $(fg)$:$$\Huge (fg)(x)=f(x)g(x),\,\,Dom\,f\cap Dom\,g$$
> Ratio $\left(\frac{f}{g}\right)$:$$\Huge \left(\frac{f}{g}\right)=\frac{f(x)}{g(x)},\,\,Dom\,\left(\frac{f}{g}\right)=\left(Dom\,f\cap Dom\,g\right)\setminus\{x:g(x)=0\}$$
> Composition $(f\circ g)$:$$\Huge (f\circ g)=f(g(x)),\,\,Dom\,(f\circ g)=\left\{x\in Dom\,g:g(x)\in Dom\,f\right\}$$
> Scalar multiplication $(cf)$:$$\Huge (cf)(x)=cf(x),\,\,Dom\,(cf)=Dom\,f$$

Note that in general, $f\circ g\neq g\circ f$. Linear combinations of functions $f,g$ can be defined as:$$\large (af+bg)(x)=af(x)+bf(g),\,\,Dom\,(af+bg)=Dom\,f\cap Dom\,g,\,\,\forall a,b\in\Re$$
# Inverse functions:

## Surjectivity:

A function, $f:D\mapsto C$ is surjective if $Ran\,f=C$, that is:$$\Huge \forall y\in C,\,\,\exists x\in D:f(x)=y$$
Every element in the co-domain is an image of an element in the domain.

## Injectivity:

A function, $f:D\mapsto C$ is injective if $\forall x_1,x_2\in D$ with $x_1\neq x_2$, then $f(x_1)\neq f(x_2)$. This is to say that for any two inputs, the same output will not be seen. Note that even functions can never be injective.

## Bijectivity:

If a function is both surjective and injective, then it can be said to be bijective. Only bijective functions can be defined to have an inverse:$$\large \left(f^{-1}\circ f\right)(x)=x=\left(f\circ f^{-1}\right)(x),\,\,Dom\,f^{-1}=Ran\,f,\,\,Ran\,f^{-1}=Dom\,f$$