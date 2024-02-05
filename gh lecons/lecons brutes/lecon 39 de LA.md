! L39 : Exemples de résolutions d'équations (méthodes exactes, méthodes approchées)

Prérequis : Notion de dérivée, définition de la fonction $x \mapsto \exp(x)$.

# Équations polynomiales de degré 2 et plus

Définition : [...].

Théorème : ($\Delta$, $\alpha$, $\beta$, solution(s) en fonction de $\Delta$, ne pas traiter $\Delta < 0$).

Applications :

1. 1ère spé Barbazo p76exo110 : trajectoire d'un solide (avec $\tan$).
2. Autour de l'équation $24x^3-26x^2+9x-1=0$.
    
    Question préliminaire : Montrer que $\forall x \leq 0, P(x) < 0$.
    
    1. En sachant que $\frac{1}{2}$ est solution, résoudre l'équation (Tle expertes ou approfondissement de Tle ens spécialité).
    2. Proposition : Si $\frac{p}{q}$ (sous forme irréductible) est racine de $P=a_nX^n+ \cdots + a_1 X + a_0$ alors $p \mid a_0$ et $q \mid a_n$ (approfondissement écrit dans le BOO en Tle exp). Résoudre l'équation en sachant cela.
    3. TVI.
    4. Corollaire (admis) : [Polynôme de degré impair (non constant) admet une racine réelle].
    
    Application à la résolution de $24x^3-26x^2+9x-1=0$ : on admet qu'au moins une racine est absolument inférieure égale à $24+26+9+1=60$ (voir développement sur majoration racine polynôme). Utiliser l'encadrement alors obtenu pour les méthodes de résolutions approchées qui suivent (cela permet de se donner des bornes de recherches).
    
    **Méthode approchée n°1** : par balayage (expliquer le concept, implé Python, rq attention donne première solution, inconvénient très approximatif).
    
    **Méthode approchée n°2** : par dichotomie (même rqs, attention converge vers UNE solution).
    
3. Autour de $x^2-2=0$.
    
    **Méthode approchée n°3** : de Newton (c.f. développement associé).

# Équations différentielles

Définition : [...].

Théorème : Solutions de $y'=ay$ ($x \mapsto Ce^{ax}$).

Théorème : Solutions de $y'=ay+b$ ($x \mapsto Ce^{ax}-\frac{b}{a}$).

Théorème : Solutions de $y'=ay+f$ ($x \mapsto Ce^{ax}+g(x)$ où $g$ sol part).

Exemple : Exercice bidon.

Application : Étude de $y'=y^2$. (\todo : changer si tjrs pas trouvé de rédaction d'ici là)

Méthode approchée : Méthode d'Euler à travers un exercice (dans Barbazo Tle spé) et application à $y'=y^2$.