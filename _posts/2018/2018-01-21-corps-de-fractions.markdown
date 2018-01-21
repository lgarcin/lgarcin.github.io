---
layout: post
title: Corps des fractions d'un anneau
published: true
---

La construction du corps $\dQ$ des rationnels n'est pas au programme de MPSI mais on comprend intuitivement comment il est construit à partir de l'anneau $\dZ$ des entiers relatifs. De la même manière, on peut construir le corps $\dK(X)$ des fractions rationnelles à coefficients dans $\mathbb{K}$ à partir de l'anneau $\dK[X]$ des polynômes à coefficients dans $\dK$.

De manière générale, on peut construire un corps à partir de tout anneau commutatif intègre $(A,+,\times)$. L'idée est de s'inspirer très fortement de la notion intuitive que l'on a des fractions d'entiers.

Dans un premier temps, on va considérer une fraction d'éléments de $A$ comme un couple de $A\times A^\star$ où $A^\star=A\setminus\\{0\\}$. Pour un tel couple $(x,y)\in A\times A^\star$, $x$ désigne en quelque sorte le numérateur et $y$ le dénominateur.

On peut munir $A\times A^\star$ de deux lois que l'on notera encore $+$ et $\times$ :

* $(a,b)+(c,d)=(a\times d+b\times c,b\times d)$
* $(a,b)\times(c,d)=(a\times c,b\times d)$

Si les couples $(a,b)$ et $(c,d)$ sont notés $\frac{a}{b}$ et $\frac{c}{d}$, les égalités précédentes deviennent :

* $\frac{a}{b}+\frac{c}{d}=\frac{a\times d+b\times c}{b\times d}$
* $\frac{a}{b}\times\frac{c}{d}=\frac{a\times c}{b\times d}$

Ceci concorde avec la manière d'additionner et de multiplier les rationnels.

On vérifie que ces deux nouvelles lois $+$ et $\times$ sont internes (c'est ici qu'intervient l'intégrité : le produit de deux dénominateurs non nuls est non nul) et que la commutativité et l'associativité des lois initiales $+$ et $\times$ de l'anneau $A$ se transmettent à ces deux nouvelles lois.

On vérifie sans peine que les couples $(0_A,1_A)$ et $(1_A,1_A)$ son respectivement neutres pour les lois $+$ et $\times$. Malheureusement,

* tout élément de $A\times A^\star$ n'admet pas forcément d'opposé pour cette nouvelle loi $+$ : on ne peut donc pas garantir la structure de groupe de $(A\times A^\star,+)$ ;
* la distributivité de $\times$ sur $+$ n'est pas non plus assurée ce qui poserait alors problème pour la structure d'anneau ;
* on perd également l'inversibilité des éléments non nuls, ce qui exclut la structure de corps.

Par exemple, lorsque $A=\dZ$,

$$
\begin{align*}
(1,2)\times\left((3,4)+(5,6)\right)=(1,2)\times(38,24)&=(38,48)\\
(1,2)\times(3,4)+(1,2)\times(5,6)=(3,8)+(5,12)&=(76,96)
\end{align*}
$$

La loi $\times$ n'est donc pas distributive sur la loi $+$. Néanmoins, on sait pertinemment que les deux fractions $\frac{38}{48}$ et $\frac{76}{96}$ sont égales. Il faudrait donc trouver un moyen d'*identifier* ces deux fractions. De manière générale, lorsque $(a,b,c,d)\in\dZ\times\dZ^\star\times\dZ\times\dZ^\star$, l'égalité des fractions $\frac{a}{b}$ et $\frac{c}{d}$ équivaut à $ad=cb$. On s'inspire de cette idée pour *identifier* des couples de $A\times A^\star$ lorsque $A$ est un anneau quelconque.

On introduit donc la relation binaire $\sim$ sur $A\times A^\star$ définie par

$$
(a,b)\sim(c,d)\iff a\times d=c\times b
$$

On vérifie que la relation $\sim$ est une relation d'équivalence.

* La réflexivité est évidente.
* La symétrie découle de la commutativité de la loi $\times$.
* La transitivité provient essentiellement de l'intégrité de l'anneau $A$ et mérite d'être détaillée.

On se donne donc trois couples $(a,b)$, $(c,d)$ et $(e,f)$ de $A\times A^\star$ tels que $(a,b)\sim(c,d)$ et $(c,d)\sim(e,f)$. Par définition, $a\times d=c\times b$ et $c\times f=e\times d$. En multipliant ces égalités respectivement par $f$ et $b$, on obtient $a\times d\times f=c\times b\times f$ et $c\times f\times b=e\times d\times b$. Puisque la loi $\times$ est commutative sur $A$,

$$
a\times d\times f=c\times b\times f=c\times f\times b=e\times d\times b
$$

A nouveau par commutativité, $a\times f\times d=e\times b\times d$ ou encore $(a\times f-e\times b)\times d=0_A$. Or $d\neq 0_A$ donc, par intégrité de $A$, $a\times f=e\times d$ i.e. $(a,b)\sim(e,f)$.

La relation $\sim$ permet alors d'*identifier* les couples de $A\times A^\star$ appartenant à une même classe d'équivalence.

Il s'agit donc maintenant de montrer que les lois $+$ et $\times$ sont compatibles avec la relation d'équivalence $\sim$, autrement dit que la classe d'équivalence d'une somme et d'un produit ne dépend que des classes d'équivalence des opérandes. En clair, il s'agit de montrer que si $(a,b)\sim(a',b')$ et $(c,d)\sim(c',d')$, alors $(a,b)+(c,d)\sim(a',b')+(c',d')$ et $(a,b)\times(c,d)\sim(a',b')\times(c',d')$. C'est un peu fastidieux et laissé en exercice au lecteur.

Ceci permet alors de munir l'ensemble des classes d'équivalences de $A\times A^\star$ pour la relation $\sim$ de deux lois que l'on notera à nouveau $+$ et $\times$ : si $x$ et $y$ sont deux classes d'équivalences, on note $x+y$ la classe d'équivalence de $(a,b)+(c,d)$ et $x\times y$ la classe d'équivalence de $(a,b)\times(c,d)$ où $(a,b)\in x$ et $(c,d)\in y$. Ces deux classes d'équivalence $x+y$ et $x\times y$ sont bien définies puisque les classes d'équivalence de $(a,b)+(c,d)$ et $(a,b)\times(c,d)$ ne dépendent que des classes d'équivalence de $(a,b)$ et $(c,d)$, c'est-à-dire $x$ et $y$.

Si on note classiquement $(A\times A^\star)/\sim$ l'ensemble des classes d'équivalence de $A\times A^\star$ pour la relation $\sim$, on vérifie que $((A\times A^\star)/\sim,+,\times)$ est un corps appelé **corps des fractions** de l'anneau $A$. Voici les points à vérifier dont on ne détaillera pas les preuves.

* La commutativité et l'associativité des lois $+$ et $\times$ sur $(A\times A^\star)/\sim$ proviennent de la commutativité des lois $+$ et $\times$ sur $A\times A^\star$.
* On vérifie la distributivité de $\times$ sur $+$.
* Les classes d'équivalence de $(0_A,1_A)$ et $(1_A,1_A)$ sont respectivement neutres pour la loi $+$ et $\times$.
* L'opposé de la classe d'équivalence d'un élément $(a,b)\in A\times A^\star$ est alors la classe d'équivalence de $(-a,b)$.
* Les éléments non nuls de $(A\times A^\star)/\sim$ sont les classes d'équivalence de couples de la forme $(a,b)\in(A^\star)^2$ et on vérifie qu'une telle classe d'équivalence est inversible d'inverse la classe d'équivalence de $(b,a)$.

On peut alors *identifier* les éléments de $A$ à des éléments de $(A\times A^\star)/\sim$ : il suffit de montrer que l'application qui à $a\in A$ associe la classe d'équivalence de $(a,1_A)$ est injective.
