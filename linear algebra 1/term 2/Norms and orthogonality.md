Given a [[Vector space definitions|vector space]] over $\Re$, a norm on $V$ is a function $||\cdot||:V\mapsto\Re$ such that:
> $||a\underline v||=|a|||\underline v||$, absolute homogeneity
> $||\underline u+\underline v||\leq||\underline u||+||\underline v||$, triangle inequality
> $||\underline v||=0\iff\underline v=\underline0$, separation of points

Using absolute homogeneity, observe that $||-\underline v||=||\underline v||$, making the triangle inequality:$$\Huge ||\underline v+(-\underline v)||=||0\cdot\underline v||=0\leq||\underline v||+||-\underline v||=2||\underline v||$$So we get that $||\underline v||\geq0$, non-negativity. When $V$ has an [[Inner product spaces|inner product]], there is a special norm induced by the inner product. In the real case, let $\{V,(\cdot,\cdot)\}$ be a real inner product space, then we let the norm induced by $(\cdot,\cdot)$ be defined by:$$\Huge ||\underline v||=\sqrt{(\underline v,\underline v)}\in\Re^+$$ 