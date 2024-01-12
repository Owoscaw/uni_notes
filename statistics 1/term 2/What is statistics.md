
Statistics is the study of uncertainty. Statistics involves the mathematical representation of real world quantities and their associated uncertainties. [[Probability definition#Probability space|Probability]] is useful but not always used, statistics is also the coherent incorporation of any knowledge, information, or data into this framework.

# Frequentists vs Bayesians:

Frequentist statistics is traditional and more established. It is simple to apply but has a questionable interpretation. Bayesian statistics is more modern, powerful, but more complex. The division comes from fundamental differences in the [[Interpretations of probability|interpretation of probability]]. Frequentists hold the [[Interpretations of probability#Relative Frequency|relative frequency interpretation]] of probability. Bayesian statisticians hold the subjective interpretation of probability.

# Foundations of statistics:
## Probability:
For a sample space $\Omega$ representing the set of all possible outcomes with a collection of $\mathcal F$ of events, the probability $P(A)$ satisfies the axioms:
> $P(A)\geq 0$ for every $A\in\mathcal F$
> $P(\Omega)=1$
> For disjoint $A$ and $B$, $P(A\cup B)=P(A)+P(B)$
> Countable additivity ish

From this, you can derive:
> $0\leq P(A)\leq 1$
> $P(A^c)=1-P(A)$
> $P(\emptyset)=0$

We have that $P(A)=0\iff\text{A cannot happen}$ and $P(A)=1\iff\text{A will always happen}$, so probability can generalise pure logic. So $0<P(A)<1$ can indicate the degree of belief in the likelihood of the event $A$ occurring. The axioms of probability indicate behaviour, but do not reveal any information on how to assign $P(A)$ any value. For example in logic, if $C$ is true and $C\implies D$ then $D$ is true. This reveals no information about $C$, so an interpretation of what probability means for the real world is required.
## Interpretations of Probability:
The classical interpretation of probability is based on the assumption of equally likely events. The frequentist interpretation is based on [[Interpretations of probability#Relative Frequency|relative frequencies]] for a repeatable events. In this interpretation, an event $A$ has $P(A)$ given by:$$\Huge P(A)=\lim_{n\to\infty}\frac{n_A}{n}$$This is a nice definition, however has no analogy in the real world, as an event can never be repeated exactly the same way for an infinite number of times.