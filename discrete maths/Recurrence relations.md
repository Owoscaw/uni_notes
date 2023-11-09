A student has a flight of $n$ stairs to climb, and can either climb $1$ or $2$ stairs at a time, how many distinct ways are there to climb $n$ stairs? Call the solution $f_n$. It is obvious to set $f_0=1$, and it follows that the sum of elements in $f_n$ must equal $n$.

Considering $f_n$, taking $1$ step from $f_{n-1}$ will lead to $f_n$. Similarly, taking $2$ steps from $f_{n-2}$ will lead to $f_n$,. These two sets will be disjoint, so it can be argued that:$$\Huge f_n=f_{n-1}+f_{n-2}$$
It also makes sense to define $f_1=1$, as there is one way to traverse to step one. This gives all the conditions to find $f_2$, which then allows for $f_3$, ect.
