## Stairs example:

A student has a flight of $n$ stairs to climb, and can either climb $1$ or $2$ stairs at a time, how many distinct ways are there to climb $n$ stairs? Call the solution $f_n$. It is obvious to set $f_0=1$, and it follows that the sum of elements in $f_n$ must equal $n$.

Considering $f_n$, taking $1$ step from $f_{n-1}$ will lead to $f_n$. Similarly, taking $2$ steps from $f_{n-2}$ will lead to $f_n$,. These two sets will be disjoint, so it can be argued that:$$\Huge f_n=f_{n-1}+f_{n-2}$$
It also makes sense to define $f_1=1$, as there is one way to traverse to step one. This gives all the conditions to find $f_2$, which then allows for $f_3$, e.c.t. Try substituting $f_n=cx^n$ as a solution:$$\Huge cx^n=cx^{n-1}+cx^{n-2}\implies cx^{n-2}(x^2-x-1)=0$$
This equation has four possible solutions, $c=0$ and $x=0$ are trivial, so we look at the quadratic that will yield two solutions $x^2-x-1=0$. This is the characteristic equation of the recurrence relation. Letting the roots of these equations be $\alpha,\beta$. Then $f_n=\alpha^n$ and $f_n=\beta^n$ are valid solutions to the equation, we also get the linear combination $f_n=c_1\alpha^n+c_2\beta^n$ as a valid solution. Using the initial conditions produces two simultaneous equations that can be solved to find $c_1$ and $c_2$. Putting all of this together gives:$$\Huge f_n=\frac{1}{\sqrt{5}}\left(\left(\frac{1+\sqrt{5}}{2}\right)^{n+1}-\left(\frac{1-\sqrt{5}}{2}\right)^{n+1}\right)$$

# General method for homogeneous linear recurrence relations:

Let $a_n$ be a sequence indexed by $n=0,1,\dots$ . We are given the following:
> Initial conditions $a_0,a_1,\dots,a_{r-1}$
> Recurrence relation:$$\Huge a_n=\sum_{i=1}^rc_ia_{n-i}$$

Where each $c_i$ are constants to be determined. This is linear and homogeneous as no term involves more than a single factor of $a_i$ and it is homogeneous as every term involves an $a_i$. Substituting $a_n=x^n$, $x\neq0$ then dividing through by $x^{n-r}$$$\Huge x^n=\sum_{i=1}^rc_ix^{n-i},\,\,x^r-\sum_{}$$