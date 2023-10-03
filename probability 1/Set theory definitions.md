A set is an unordered collection of objects. Any object can be a part of a set, even other sets. A set is defined in the following manner:
$$\Huge A:=\{elements\}$$
The outcomes of the set $A$ are called the elements of $A$. The empty set, $\emptyset$, is defined as the set with no elements:
$$\Huge \emptyset:=\{\}$$
For two sets, $A$ and $B$, if $A$ is a subset of $B$, the following is true:
$$\Huge A\subseteq B,\,\,\forall x\in A,\,\,x\in B$$
Every element in set $A$ is also in set $B$.

The power set of $A$ is a set consisting of all subsets of $A$, denoted as $2^A$:
$$\Huge 2^A:=\left\{B:B\subseteq A\right\}$$

# Set operations:

## Union:
The union operator represents the collection of sample points from two sets, $A$ and $B$:
$$\Huge A\cup B=\left\{\omega:\omega\in A\,\,or\,\,\omega\in B\right\}$$
The union of multiple sets can be written as:
$$\Large \bigcup^n_{i=1}A_i=A_1\cup A_2\cup\dots\cup A_n=\left\{\omega\in\Omega:\omega\in A_i\,\,for\,\,i\in\{1,\dots,n\}\right\}$$
## Intersect:
The intersect operator represents the collection of sample points that are in both sets $A$ and $B$:
$$\Huge A\cap B=\left\{\omega:\omega\in A\,\,and\,\,\omega\in B\right\}$$
## Complement:
The complement of a set is the collection of sample points that are not in a given set:
$$\Huge A^{'}=\left\{\omega:\omega\notin A\right\}$$
Note that:
$$\Huge A\cup A^{'}=\emptyset$$
## Set difference:
The set difference between two sets is the collection of sample points that are in one set but not the other:
$$\Huge A\setminus B=\left\{\omega:\omega\in A\,\,and\,\,\omega\notin B\right\}=A\cap B^{'}$$
## Subset:
One set is a subset of another if every one of a set's elements are contained within another set:
$$\Huge A\subseteq B=\left\{\omega:\omega\in A\in B\right\}$$