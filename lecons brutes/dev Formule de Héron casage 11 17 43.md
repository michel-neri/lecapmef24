! Développement : Formule de Héron

Proposition : Soit $\Delta$ un triangle de côtés de mesures $a$, $b$ et $c$. Alors $\mathscr A(\Delta) =  \sqrt{p(p-a)(p-b)(p-c)}$, où $p=\frac{a+b+c}{3}$.

*Preuve*

\underline{Lemme} : $\mathscr A (\Delta) = \frac{1}{2}bc \sin \alpha$.

*Preuve du lemme*

$\sin \alpha = \frac{h}{b} \implies h = b \sin \alpha$, on conclut avec $\mathscr A(\Delta) = \frac{1}{2}\text{base} \times \text{hauteur}$. La preuve fonctionne même lorsque le pied de la hauteur associée à $\gamma$ sort du triangle.

*Preuve principale*

Le théorème d'Al-Kashi donne $b^2+c^2=a^2-2bc\cos \alpha$ . Donc $\cos \alpha = \frac{a^2-b^2-c^2}{2bc}$. Le lemme donne $\mathscr A(\Delta) = \frac{1}{2} bc \sin \alpha = \frac{1}{2} bc \sqrt{(1-\cos \alpha)(1+\cos \alpha)}$. La dernière égalité vient de $\sin \alpha = \sqrt{1-\cos^2 \alpha}$. Remplacer ensuite $\cos \alpha$ par ce que donne le théorème d'Al-Kashi, ne jamais développer, factoriser avec la troisième identité remarquable et conclure.

Application : à inventer en live.