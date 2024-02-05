! Développement : majoration des racines d'un polynôme

Ce développement est simple à caler dans une leçon / exercice où l'on parle de racines de polynômes.

Proposition : Soit $P=X^n+a_{n-1}X^{n-1}+ \cdots + a_0 \in \C[X]$.

On pose $A=|a_{n-1}|+\cdots + |a_0|$.

Soit $z$ une racine de $P$.

Alors $z \leq \max \ens{1,A}$.

*Solution* : (on suppose $n \geq 1$, sinon l'énoncé est trivial à analyser)

On a les égalité suivantes :

$$
\begin{align}
	0 &= z^n+a_{n-1}z^{n-1}+\cdots + a_0 \\\\
	z^n &= -a_{n-1}z^{n-1} - \cdots - a_0 \\\\
	|z|^n & \leq \left|a_{n-1} \right| \cdot |z|^{n-1} + \cdots + \left| a_0 \right|
\end{align}	
$$

Si $A=\left| a_{n-1}\right| + \cdots + |a_0| \leq 1$ alors les $|a_k|$ sont tous $\leq 1$ (par l'absurde). Aussi :

$$
\begin{align}
    |z|^n & \leq \left|a_{n-1} \right| \cdot |z|^{n-1} + \left| a_0 \right| \\\\
          & \leq |z|^{n-1} + \cdots + 1 \\\\
          & = \frac{1-|z|^n}{1-|z|}
\end{align}
$$

Cela revient à dire que

$$
    0 \leq \frac{1-|z|^n}{1-|z|} - |z|^n
         = \frac{1-|z|^n - |z|^n + |z|^{n+1}}{1-|z|}
         = \frac{1-2|z|^n + |z|^{n+1}}{1-|z|}
$$

Alors si $|z|>1$, $1-2|z|^n+|z|^{n+1} > 0$ (factoriser par $|z|^n$ et distinguer les cas $|z|=1$ et $|z| \geq 2$) et $1-|z|<0$, autrement dit la fraction est strictement négative ce qui est absurde car elle majore aussi $0$, et donc $|z|<1$.

Sinon si $1 \leq \left| a_{n-1}\right| + \cdots + |a_0| = A$, supposons par l'absurde que $|a_0|+\cdots+|a_{n-1}|<z$ et alors ($\times |z|^{n-1}$)

$$
    |a_0|\cdot|z|^{n-1}+\cdots+|a_{n-1}|\cdot|z|^{n-1} < & |z|^n
$$

C'est absurde car comme montré précédemment $|z|^n \leq |a_0|+\cdots+|a_{n-1}| \cdot |z|^{n-1}$ or terme par terme on peut montrer que $|a_k| \cdot |z|^k \leq |a_{n-1}| \cdot |z|^{k-1}$ (incohérence avec les bouts des chaînes de minoration / majoration).