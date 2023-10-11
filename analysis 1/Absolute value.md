Let $a\in\Re$. The absolute value of $a$ is defined as follows:
$$\Huge |a|=\begin{cases}a&\text{if}&a\geq0\\-a&\text{if}&a<0\end{cases}$$
$$\Huge |\cdot|:\Re\mapsto[0,\infty)$$
The following are consequences of this definition, letting $a,b,c,d\in\Re$ and using [[Axiom definitions|axiom definitions]]:
>$0\leq|a|=|-a|$. Proof:
>By definition, $0\leq|a|$. If $a<0$, then $-a>0$ so $|-a|=a=|a|$. If $a>0$, then $-a<0$, so $|-a|=-(-a)=a=|a|$. If $a=0$, then $-a=0$ and $|a|=0=|-a|$. Over the defined intervals, $a\in\Re$ satisfies $|a|=|-a|$.
>
>$|a|\leq c\iff -c\leq a\leq c$. Proof:
>If $c<0$, both statements are false and there is no contradiction, so we assume $c\geq 0$. 
>
>Assume $|a|\leq c$. If $a\geq 0$, then $a\leq c$. Since $-c\leq 0$, $a\geq -c$. Combining these statements, we get $-c\leq a\leq c$ in the case of $a\geq 0$. If $a<0$, we have $-a>0$ and therefore $-a\geq 0$. It follows that $-a\leq c$, so we get $0\leq -a\leq c$. From this we also get $-c\leq a$, and since $a<0$ we get $-c\leq a\leq c$. Therefore assuming $|a|\leq c$, we have shown $-c\leq a\leq c$ for all cases of $a\in\Re$. That is to say, $|a|\leq c\implies -c\leq a\leq c$.
>
>Assume $-c\leq a\leq c$. If $a\geq0$ we have $|a|=a\leq c$, if $a<0$ we use $-c\leq a$ to give $|a|=-a\leq c$. This completes the statement, showing that $-c\leq a\leq c\implies |a|\leq c$.
>
>Since these two assumptions imply each other, they must be logically equivalent. That is to say $|a|\leq c\iff -c\leq a\leq c$ 