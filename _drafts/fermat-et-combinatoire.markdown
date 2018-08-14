---
layout: "post"
title: "Petit théorème de Fermat, combinatoire et action de groupe"
published: true
---

On propose dans cet article une preuve alternative du petit théorème de Fermat via des considérations combinatoires. On en profitera pour introduire la notion d'action de groupe, primordiale en théorie des groupes.

# Introduction naïve

On s'intéresse aux nombres de façons de colorier les sommets d'un polygone régulier à $n$ côtés à l'aide de $p$ couleurs. Evidemment, le nombre total de coloriages possibles est $n^p$ (on peut colorier de $n$ façons chacun des $p$ côtés). Un coloriage étant donné, on s'intéresse aux nouveaux coloriages obtenus en faisant subir au polygone une rotation d'angle un multiple de $\frac{2\pi}{p}$.

Clairement, si tous les sommets du polygone initial sont de même couleur, on n'obtient aucun nouveau coloriage en faisant tourner le polygone.

Dans le cas général, pour revenir au coloriage initial par rotation (non égale à l'identité), il faut que le coloriage initial possède un motif "périodique", la période étant nécessairement un diviseur de $p$. Notamment, lorsque $p$ est premier, les "périodes" possibles ne peuvent qu'être égales à $1$ (coloriage uniforme) ou $p$ (coloriage non uniforme).

Lorsque $p$ est premier (ici $p=7$), on ne retrouvera jamais le coloriage initial par rotation (à moins que le coloriage soit uniforme).
<div>
<script src="/js/polygones1.js" id="d36553d5-ff01-4bac-aa06-cd28044879d3"></script>
</div>

Lorsque $p$ n'est pas premier (ici $p=6$), on peut retrouver le coloriage initial par rotation si le motif est "périodique" (la "période" ici est $3$).
<div>
<script src="/js/polygones2.js" id="9b757310-2181-4bf7-b827-0a5a151b9c21"></script>
</div>

Puisque l'on dipose de $n$ couleurs, il existe exactement $n$ coloriages uniformes. De plus, chaque rotation d'angle $\frac{2k\pi}{p}$ avec $k\in\lb0,p-1\rb$ appliquée à un coloriage non uniforme donne un coloriage différent. En regroupant les coloriages non uniformes en "paquets" de coloriages différant d'une rotation d'un angle multiple de $\frac{2\pi}{p}$, on en déduit que le nombre de coloriages non uniformes est un multiple de $p$. Le nombre total de coloriages étant égal à $n^p$, on en déduit que $n^p\equiv n[p]$.

# Une relation d'équivalence

On propose maintenant une formalisation plus rigoureuse de l'approche précédente.

Pour $n\in\dN$, on notera $\dN_n$ l'ensemble des entiers compris entre $1$ et $n$ ($\dN_n=\emptyset$ lorsque $n=0$). On notera également $A_{p,n}$ l'ensemble des applications de $\dN_p$ dans $\dN_n$. Pour faire le lien avec l'approche précédente, les éléments de $A_{p,n}$ sont des coloriages : un coloriage n'est en effet qu'une manière d'associer une couleur à chacun des sommets.

Faire subir une rotation d'angle $\frac{2\pi}{p}$ à notre polygone régulier revient en fait à permuter circulairement ses sommets. On note donc $c$ le cycle $(1,2,\dots,p)$. On munit l'ensemble $A_{p,n}$ de la relation d'équivalence suivante[^equivalence] :

$$
\forall(f,g)\in A_{p,n},\;f\sim g\iff\exists k\in\dZ,\;f=g\circ c^k
$$

Il est évident que les classes d'équivalence des fonctions constantes sont des singletons. En effet, si $f$ est constante, $f\circ c^k=f$ pour tout $k\in\dZ$.

On suppose maintenant $p$ _premier_. Le fait que $p$ soit premier entraîne que les classes d'équivalence d'une application non constante sont exactement de cardinal $p$. Plus précisément, on va montrer que la classe d'équivalence de $f\in A_{p,n}$ est

$$
C(f)=\left\{f\circ c^r,\;r\in\lb0,p-1\rb\right\}
$$

les éléments étant bien deux à deux distincts. L'inclusion de la droite vers la gauche est évidente. Réciproquement, si l'on se donne $g\in C(f)$, il existe $k\in\dZ$ tel que $g=f\circ c^k$. Puisque $c^p$ est l'identité, en notant $r$ le reste de la division euclidienne de $k$ par $p$, on a bien $g=f\circ c^r$ avec $r\in\lb0,p-1\rb$.

Il ne reste plus qu'à montrer que les éléments sont bien deux à deux distincts. On peut raisonner par l'absurde : on suppose qu'il existe $(r,s)\in\lb0,p-1\rb^2$ tel que $r\neq s$ et $f\circ c^r=f\circ c^s$. En posant $t=r-s$, on a donc $f\circ c^t=f$ et $t\in\lb-p+1,p-1\rb\setminus\{0\}$ ; $t$ est donc premier avec $p$ car $p$ est premier. Il existe donc $(u,v)\in\dZ^2$ tel que $ut+vp=1$. Puisque $f\circ c^t=f$, on obtient successivement $f\circ c^{ut}=f$, puis $f\circ c^{1-vp}=f$ et enfin $f\circ c=f$ puisque $c^p$ est l'identité. Il est alors clair que $f$ est constante.

Récapitulons :
* Les classes d'équivalence des applications constantes sont des singletons. Il existe $n$ telles classes d'équivalences (autant que d'applications constantes).
* Les autres classes d'équivalence sont toutes de cardinal $p$. Notons $q$ leur nombre.

On sait que les classes d'équivalence forment une partition de $A_{p,n}$ qui est lui-même de cardinal $n^p$. On en déduit que $n^p=n+qp$ et donc que $n^p\equiv n[p]$. Ceci reste évidemment vrai lorsque $n$ est un entier négatif.

# Action de groupe

Le bon cadre pour interpréter le raisonnement précédent est celui d'**action de groupe**.

---
**Définition [Action de groupe]** Soit $G$ un groupe et $X$ un ensemble. On appelle **action de groupe** toute application

$$
\begin{align*}
  G\times X&\to E\\
  (g,x)&\mapsto g\cdot x
\end{align*}
$$

vérifiant les conditions suivantes :

* $\forall x\in X,\;e\cdot x=x$ où $e$ désigne l'élément neutre de $G$ ;
* $\forall(g,h,x)\in G^2\times X,\;g\cdot(h\cdot x)=(gh)\cdot x$.

---

On dit alors que le groupe $G$ _agit_ ou _opère_ sur l'ensemble $E$. Dans notre exemple précédent, le sous-groupe $\langle c\rangle$ du groupe symétrique $S_p$ engendré par le cycle $c=(1,2,\dots,p)$ agit sur l'ensemble $A_{p,n}$ des applications de $\dN_p$ dans $\dN_n$, l'action étant définie par

$$
\begin{align*}
\langle c\rangle\times A_{p,n}&\to A_{p,n}\\
(\sigma,f)&\mapsto f\circ\sigma
\end{align*}
$$

### Orbites

Les classes d'équivalence de notre exemple précédent sont en fait ce que l'on appelle des **orbites** pour l'action de groupe.

---
**Définition [Orbite]** Soit $G$ un groupe opérant sur un ensemble $X$. On appelle **orbite** d'un élément $x$ de $X$ la partie $\omega(x)$ de $X$ définie par

$$
\omega(x)=\{g\cdot x,\;g\in G\}
$$

---

Si l'on définit la relation d'équivalence $\sim$ par

$$
\forall(x,y)\in X^2,\;x\sim y\iff\exists g\in G,\;y=g\cdot x
$$

l'orbite de $x\in X$ n'est autre que sa classe d'équivalence pour la relation $\sim$. On en déduit notamment la proposition suivante.

---
**Proposition** Les orbites d'une action d'un groupe $G$ sur un ensemble $X$ forment une partition de $X$.

---

On peut donner un exemple qui justifie l'appellation d'orbite. Si l'on considère l'action naturelle du groupe $SO_2(\dR)$ sur $\dR^2$

$$
\begin{align*}
SO_2(\dR)\times\dR^2&\to\dR^2\\
(R,x)&\mapsto Rx
\end{align*}
$$

alors l'orbite d'un vecteur $x_0\in\dR^2$ est le cercle

$$
\left\{x\in\dR^2,\;\|x\|=\|x_0\|\right\}
$$

### Action d'un sous-groupe sur un groupe

Il faut maintenant parler d'un exemple fondamental d'action de groupe : un sous-groupe $H$ d'un groupe $G$ peut agir sur $G$ par multiplication à gauche ou à droite. Plus précisément, les deux actions de groupe sont

$$
\begin{aligned}
H\times G&\to G\\
(h,x)&\mapsto hx
\end{aligned}
\qquad\text{et}\qquad
\begin{aligned}
H\times G&\to G\\
(h,x)&\mapsto xh
\end{aligned}
$$

Les orbites d'un élément $x$ de $G$ pour chacune de ces deux actions de groupe sont alors respectivement $xH$ et $Hx$ [^distingue]. L'ensemble de ces orbites est classiquement noté $G/H$ et il est aisé de voir que si $H$ est fini, toutes les orbites ont même cardinal que $H$ (en effet, les applications $h\mapsto hx$ et $h\mapsto xh$ réalisent des bijection de $H$ sur $Hx$ et $xH$ respectivement). Comme les orbites forment une partition de $G$, on en déduit que $\card(G/H)=\card(G)/\card(H)$ [^lagrange].

Dans la suite, on considérera des actions à droite.

### Stabilisateur

On va maintenant établir un lien entre l'orbite d'un élément et un objet appelé **stabilisateur**.

---
**Définition [Stabilisateur]** Soit $G$ un groupe opérant sur un ensemble $X$. On appelle **stabilisateur** d'un élément $x$ de $X$ l'ensemble

$$
\stab(x)=\{g\in G,\;g\cdot x=x\}
$$

C'est un sous-groupe de $G$.

---

Dans notre exemple, le stabilisateur d'une application constante est évidemment $\langle c\rangle$ en entier tandis que le stabilisateur d'une application non constante est réduit à l'identité. En effet, le stabilisateur d'une application $f$ est un sous-groupe de $\langle c\rangle$. Son ordre divise l'ordre de $\langle c\rangle$, à savoir le nombre premier $p$ : il vaut donc $1$ ou $p$. Ainsi le stabilisateur de $f$ est soit $\langle c\rangle$ en entier, soit réduit à l'identité. Dans le premier cas, le stabilisateur de $f$ contient $c$ et donc $c\cdot f=f\circ c=f$, ce qui prouve aisément que $f$ est constante. Réciproquement, si $f$ est constante, il est clair que son stabilisateur est $\langle c\rangle$.

On retourne maintenant au cas général.

---

**Proposition** Soit $G$ un ensemble opérant sur un ensemble $X$. Alors pour tout $x\in X$, il existe une bijection de $G/\stab(x)$ sur $\omega(x)$.

---

On en déduit notamment que, si $G$ est d'ordre fini,

$$
\card(G/\stab(x))=\card(G)/\card(\stab(x))=\card(\omega(x))
$$

En particulier, le cardinal d'une orbite divise le cardinal du groupe.

Il s'agit maintenant de prouver ce résultat. On peut en fait expliciter une bijection $\phi$ de $G/\stab(x)$ sur $\omega(x)$. On pose pour $C\in G/\stab(x)$, $\phi(C)=g\cdot x$ où $g$ est un élément de $C$.
* Il faut déjà montrer que cette application est bien définie, autrement dit que si $g_1$ et $g_2$ appartiennent à une même classe de $G/\stab(x)$, $g_1\cdot x=g_2\cdot x$. Puisque $g_1$ et $g_2$ appartiennent à la même classe, il existe $g\in\stab(x)$ tel que $g_2=g_1g$. Ainsi $g_2\cdot x=(g_1g)\cdot x=g_1\cdot (g\cdot x)=g_1\cdot x$.
* Il faut également montrer que $\phi$ est surjective sur $\omega(x)$. Si l'on se donne $y\in\omega(x)$, il existe $g\in G$ tel que $y=g\cdot x$. En notant $C$ la classe de $g$, on a bien $y=\phi(C)$.
* Enfin, il faut montrer l'injectivité de $\phi$. Notons $C_1$ et $C_2$ deux classes de $G/\stab(x)$ ainsi que $g_1$ et $g_2$ des éléments respectifs de ces classes. Supposons que $\phi(C_1)=\phi(C_2)$ i.e. $g_1\cdot x=g_2\cdot x$. On a donc $(g_2^{-1}g_1)\cdot x=x$ et donc $g_2^{-1}g_1\in\stab(x)$. Ainsi $g_1\in g_2\stab(x)=c_2$, puis $C_1=C_2$.

On peut alors revenir une dernière fois à l'exemple traité initialement. Les cardinaux des orbites divisent le cardinal de $\langle c\rangle$, à savoir $p$ qui est premier : ces cardinaux valent donc tous $1$ ou $p$.

Si $f$ est une application constante de $A_{p,n}$, son orbite est évidemment de cardinal $1$. Réciproquement, si $f$ est une application dont l'orbite est de cardinal $1$, alors $c\cdot f=f\circ c=f$. On prouve alors facilement que $f$ est constante.

Finalement, l'orbite de chaque application constante est de cardinal $1$ et il existe $n$ telles orbites tandis que les orbites des applications non constantes sont de cardinal $p$. Comme $A_{p,n}$ est de cardinal $n^p$ et que les orbites forment une partition de cet ensemble, $n^p\equiv n[p]$.

# Variantes

On aurait pu établir le petit théorème de Fermat en utilisant d'autres actions de groupe.

---

Par exemple, on peut utiliser le groupe additif $\dF_p=\dZ/p\dZ$. En effet, si on note maintenant $B_{p,n}$ l'ensemble des applications de $\dF_p$ dans $\dN_n$, il suffit d'introduire l'action de groupe

$$
\begin{align*}
\dF_p\times B_{p,n}&\to B_{p,n}\\
(x,f)&\mapsto f\circ\tau_x
\end{align*}
$$

où $\tau_x$ désigne la translation $y\in\dF_p\mapsto x+y$. On laisse la preuve de la suite au lecteur.

---

On aurait aussi pu utiliser l'action d'un autre groupe cyclique d'ordre $p$, à savoir le groupe $\dU_p$ des racines $p^\text{èmes}$ de l'unité. On le fait alors agir sur l'ensemble $C_{p,n}$ des applications de $\dU_p$ dans $\dN_n$ de la manière suivante

$$
\begin{align*}
\dU_p\times C_{p,n}&\to C_{p,n}\\
(\zeta,f)&\mapsto f\circ\tau_\zeta
\end{align*}
$$

où $\tau_\zeta$ désigne l'application $z\in\dU_p\mapsto\zeta z$. Là aussi, le lecteur saura se ramener à l'étude du premier exemple.

---

De manière générale, si $G_p$ désigne un groupe cyclique d'ordre $p$ [^ordre_premier], on peut le faire agir sur l'ensemble $\dN_n^{G_p}$ des applications de $G_p$ dans $\dN_n$ via l'action de groupe suivante

$$
\begin{align*}
G_p\times\dN_n^{G_p}&\to\dN_n^{G_p}\\
(\alpha,f)&\mapsto f\circ\tau_\alpha
\end{align*}
$$

où $\tau_\alpha$ désigne l'application $\beta\in G_p\mapsto\alpha\beta$. A nouveau, le stabilisateur d'un élément $f$ de $\dN_n^{G_p}$ est un sous-groupe de $G_p$. Son ordre divise donc $p$. Or $p$ est premier donc le stabilisateur de $f$ est d'ordre $1$ ou $p$.

Si $f$ est constante, son orbite est évidemment de cardinal $1$. Réciproquement, si l'orbite de $f$ est de cardinal $1$, alors $f\circ\tau_\alpha=f$, ce qui permet de prouver que $f(\alpha^k)=f(\alpha)$ pour tout $k\in\dZ$, et, comme $\alpha$ engendre $G_p$, $f(\beta)=f(\alpha)$ pour tout $\beta\in G_p$. L'application $f$ est donc bien constante.

Finalement, l'orbite de chaque application constante est de cardinal $1$ et il existe $n$ telles orbites tandis que les orbites des applications non constantes sont de cardinal $p$. Comme $\dN_n^{G_p}$ est de cardinal $n^p$ et que les orbites forment une partition de cet ensemble, $n^p\equiv n[p]$.

# Bémol

Cette preuve du petit théorème de Fermat est relativement élégante et nous a permis d'introduire un concept-clé de la théorie des groupes, à savoir l'action de groupe.

Néanmoins, cette preuve n'est pas vraiment "efficace" lorsqu'on la compare à la preuve "classique". On se permet de rappeler celle-ci pour mettre en exergue sa briéveté. On sait que les inversibles de l'anneau $\dF_p$ forment un groupe. Lorsque $p$ est premier, $\dF_p$ est un corps (il s'agit essentiellement du théorème de Bézout) de sorte que le groupe des inversibles est $\dF_p^\star$ ($\dF_p$ privé de l'élément nul). Ce groupe est donc d'ordre $p-1$. Ainsi pour tout $x\in\dF_p^\star$, $x^{p-1}=1$. En termes d'entiers, pour tout entier $n$ premier avec $p$, $n^{p-1}\equiv1[p]$. On en déduit quasi immédiatement que $n^p\equiv n[p]$ pour tout entier $n$.

---

#### Notes

  [^equivalence]: On laisse le soin au lecteur de vérifier qu'il s'agit bien d'une relation d'équivalence.
  [^lagrange]: On a donc en particulier démontré le théorème de Lagrange : l'ordre d'un sous-groupe divise l'ordre d'un groupe.
  [^distingue]: Attention, les ensembles $xH$ et $Hx$ ne coïncident pas forcément. Si $xH=Hx$ pour tout $x\in G$, on dit que $H$ est un sous-groupe **distingué** de $G$.
  [^ordre_premier]: Un groupe $G_p$ d'ordre premier $p$ est forcément cyclique. En effet, l'ordre d'un élément divise l'ordre du groupe et vaut nécessairement $1$ ou $p$. Or le seul élément d'ordre $1$ est l'élément neutre (qui est unique) et $G_p$ contient plus d'un élément (car $p>1$). Il contient forcément un élément d'ordre $p$ : il est donc cyclique.
