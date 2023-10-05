Statements can either be true or false, and they must state something. Statements can be ruled true or false based off of axioms that we define ourselves.

Given that $A$ and $B$ are statements:
> $A\,\,and\,\,B$ is a statement that is true when both statements are true.
> $A\,\,or\,\,B$ is a statement that is true when either statement is true.
> $not\,\,\,A$ is a statement that is true when $A$ is false, and false when $A$ is true.

All of these statements are new statements that have been derived from other statements, $A$ and $B$. Often, we need to write that if $A$ is true, $B$ is true. This is written as $A\implies B$. The new statement $A\implies B$ is only false when $A$ is true and $B$ is not true.

This can be shown by considering two statements:
$$\Huge A:\,\,a=b\,,\,\,\,B:a^2=b^2$$
$B$ can be true when $A$ is false, i.e. $1^2=(-1)^2$, but the whole statement is true when $A$ is true. Whenever $A$ is true, $a$ will equal $b$, so $a^2=b^2$. In this case, $B$ is true whenever $A$ is true, so:
$$\Huge A\implies B$$
If $A$ and $B$ are statements, $A$ is logically equivalent to $B$ when both $A$ implies $B$ and $B$ implies $A$:
$$\Huge A\implies B,\,\,B\implies A,\,\,A\iff B$$

# Conditional statements:

Often, statements will depend on a variable, $x$. This is to say that a conditional statement's truth depends on $x$:
$$\Huge A(x)$$
$A(x)$ is true for some $x$ and false for other $x$. A conditional statement can become a statement by using the quantifiers "for all" and "there exists", $\forall$ and $\exists$.

# Sets:

Sets are a way to sort objects and incorporate them into mathematical statements. A set $X$ is a collection of objects. We write $a\in X$ if $a$ is an object that is described in $X$. We write $a\notin X$ if the object $a$ is not included in the set $X$. A set consisting of objects $x$ for which $A(x)$ is true is described as:
$$\Huge X=\left\{x:A(x)\right\}$$
In a set, the order of elements and how many times a single element appears does not matter. There are 4 main [[Set theory definitions|set operations]] that can be used to describe the intersection, union, complement, or difference of sets.

Given two objects, $a$ and $b$, there is another object $(a,b)$ that is an ordered pair of $a$ and $b$. The order of objects in this pair matters, any other order is a new ordered pair. This is to say:
$$\Huge(a_1,b_1)=(a_2,b_2)$$
if an only if
$$\Huge a_1=a_2\,\,\,and\,\,\,b_1=b_2$$

## Cartesian product:

The cartesian product of two sets, $X$ and $Y$ is given by:
$$\Huge X\times Y=\left\{(x,y):x\in X,\,y\in Y\right\}$$
Where $(x,y)$ is the ordered pair between every element in $X$ and every element in $Y$.

# Formal definition of a function

A function can therefore be described as the complete set of ordered pairs $(x,y)$. Let $X$ and $Y$ be sets. The function $f$ is a subset of the cartesian product of $X\times Y$:
$$\Huge f\subset X\times Y$$
This is defined such that for every $x\in X$, there is exactly one $y\in Y$ such that $(x,y)\in f$. $f:X\mapsto Y$ defines a function, while $f(x)$ defines the unique element of set $Y$ such that $(x,f(x))\in f$. $X$ is the [[Functions, Domain and Range|domain]] of $f$, while $Y$ is the [[Functions, Domain and Range|co-domain]]. Every $x\in X$ is assigned exactly one $f(x)\in Y$.

In the case where a function is not naturally defined at a point, for example $\frac{1}{x}$, the problematic values must be removed in order for it to be a proper function. The following is not a valid function:
$$\Huge f:\Re\mapsto \Re:x\mapsto\frac{1}{x}$$
Whereas the following is a valid function:
$$\Huge f:\Re\setminus\{0\}\mapsto\Re:x\mapsto\frac{1}{x}$$

# Images and Pre-images:

Let a function map set $X$ to $Y$:
$$\Huge f:X\mapsto Y$$
Given that $A\subset X$, the image of $A$ is defined as:
$$\Huge f(A)=\left\{f(a)\in Y:a\in A\right\}\subset Y$$
That is the image of $A$ is the set that represents every element in $A$, having undergone the function $f$. $A$ will always be a subset of $Y$. For $B\subset Y$, the pre-image of $B$ is defined as:
$$\Huge f^{-1}(B)=\left\{x\in X:f(x)\in B\right\} \subset X$$
That is the pre-image of $B$ would be the set used to map, under $f$, to the set $B$. $B$ will always be a subset of $X$.

Using the same function $f$, and defining sets $A,B\subset X$, the following is true:
>$$\Huge f(A\cap B)\subset f(A)\cap f(B)$$
>$$\Huge f(A\cup B)=f(A)\cup f(B)$$
>$$\Huge f(X\setminus A)\supset f(X)\setminus f(A)$$

Assuming $C,D\subset Y$:
>$$\Huge f^{-1}(C\cap D)=f^{-1}(C)\cap f^{-1}(D)$$
>$$\Huge f^{-1}(C\cup D)=f^{-1}(C)\cup f^{-1}(D)$$
>$$\Huge f^{-1}(Y\setminus C)=X\setminus f^{-1}(C)$$

All statements above can be proven by considering a general element in each set.