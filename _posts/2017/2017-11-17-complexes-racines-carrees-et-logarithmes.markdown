---
layout: post
title: 'Complexes, racines carrées et logarithmes'
published: true
---

Il est difficile de faire comprendre aux étudiants que l'emploi des symboles $\sqrt{\phantom{z}}$ et $\ln$ pose problème lorsque l'on manipule des complexes. Je vais tenter de m'expliquer dans ce court article.

Le problème provient en partie du fait que toute notation en mathématiques doit être définie de manière **unique**. Ainsi $\sqrt x$ et $\ln(x)$ doit définir un **unique** objet. Une autre façon de voir les choses est de penser à la racine carrée ou au logarithme en tant qu'**applications** : on sait qu'une application associe à un élément une **unique** image.

On va cependant voir qu'il est possible de définir la racine carrée et le logarithme d'un complexe de manière unique mais on rencontre alors de nouveaux écueils.

## Racine carrée

Le symbole $\sqrt{\phantom{x}}$ est parfaitement défini pour les réels positifs. En effet, si $x$ est un réel positif, on sait qu'il existe **deux** réels opposés dont le carré vaut $x$ (un seul si $x$ est nul). Mais parmi ces deux réels, l'un d'entre eux seulement est **positif**. C'est à celui-ci qu'on fait référence lorsque l'on parle de **la** racine carrée de $x$.

En ce qui concerne les complexes, la situation initiale est la même : si $z$ est un complexe, il existe deux complexes opposés dont le carré vaut $z$ (un seul si $z$ est nul). Néanmoins, on ne peut pas privilégier l'un par rapport à l'autre : contrairement au cas réel, parler de complexe **positif** n'a aucun sens. Ceci provient du fait qu'il n'existe pas *a priori* de relation d'ordre sur $\mathbb C$ comme il en existe sur $\mathbb R$.

On peut néanmoins définir une relation d'ordre total sur $\mathbb C$, à savoir l'ordre **lexicographique**. Pour comparer deux complexes, on compare d'abord leurs parties réelles puis, si celles-ci sont égales, on compare leurs parties imaginaires. Par exemple, $2+3i\leq5-4i$ car $2\leq 5$ et $1-2i\leq1+4i$ car $-2\leq4$.

L'ordre lexicographique permet alors de parler de complexe *positif*, c'est-à-dire plus grand que $0$ : il s'agit de complexes dont la partie réelle est strictement positive ou dont la partie réelle est nulle et la partie imaginaire positive. On vérifie alors aisément que lorsque deux complexes sont opposés, l'un est toujours *positif* tandis que l'autre est *négatif*.

On pourrait alors définir **la** racine carrée d'un complexe $z$ comme l'unique complexe *positif* dont le carré vaut $z$[^1]. Ainsi on pourrait par exemple écrire que $\sqrt{3-4i}=2-i$ car $(2-i)^2=3-4i$ et $2-i\geq0$. La racine carrée d'un complexe ainsi définie est donc toujours *positive*.

Malheureusement, l'ordre lexicographique sur $\mathbb C$ n'est pas *compatible* avec la multiplication[^2]. Par exemple, si l'on pose $z_1=1+i$ et $z_2=2+5i$, alors $z_1$ et $z_2$ sont positifs mais le produit $z_1z_2=-3+7i$ ne l'est plus. On en déduit notamment que la racine carré d'un produit n'est pas toujours le produit des racines carrées[^3].

Cette définition de la racine carrée pose également des problèmes de continuité. Par exemple, on vérifie aisément que pour $\theta\in]-\pi,\pi]$, $\sqrt{e^{i\theta}}=e^\frac{i\theta}{2}$ tandis que pour $\theta\in]\pi,3\pi]$, $\sqrt{e^{i\theta}}=-e^\frac{i\theta}{2}$. Ainsi $\sqrt{e^{i\pi}}=i$ tandis que $\lim_{\theta\to\pi^+}\sqrt{e^{i\theta}}=-i$.

On pourra se convaincre du problème de continuité avec l'applet suivante. Déplacez le point d'affixe $z$ et regardez l'évolution du point d'affixe $\sqrt z$ lorsque le point d'affixe $z$ traverse le demi-axe des abscisses négatives.

<iframe scrolling="no" title="Racine carrée complexe" src="https://www.geogebra.org/material/iframe/id/x2XW87Eb/width/700/height/500/border/888888/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="700px" height="500px" style="border:0px;"> </iframe>

## Logarithme

On sait que tout complexe non nul admet une infinité d'antécédents par la fonction exponentielle. Plus précisément, tout complexe non nul $z$ peut se mettre sous forme exponentielle $z=re^{i\theta}$ avec $r\in\mathbb R^*_+$ le module de $z$ et $\theta\in\mathbb R$ un argument de $z$. On pourrait donc affirmer que le logarithme complexe de $z$ est $\ln(r)+i\theta$. Le problème est bien entendu que $z$ admet une infinité d'arguments et le logarithme de $z$ est ainsi mal défini.

Par contre, tout nombre complexe non nul admet un unique argument dans l'intervalle $]-\pi,\pi]$, appelé **argument principal** de $z$. On pourrait donc définir de manière unique le logarithme de $z\in\mathbb C^*$, en posant $\ln(z)=\ln(r)+i\theta$ où $r$ est le module de $z$ et $\theta$ l'argument principal de $z$. Par exemple, $\ln(\sqrt2+i\sqrt2)=\ln(2)+\frac{i\pi}{4}$.

Cependant cette définition du logarithme ne permet pas d'assurer sa propriété caractéristique pour les réels, c'est-à-dire sa capacité à transformer les produits en sommes. En effet, l'argument **principal** d'un produit n'est pas toujours la somme des arguments principaux. Par exemple,

$$
\ln(-1+i\sqrt3) = \ln(2e^\frac{2i\pi}{3})=\ln(2)+\frac{2i\pi}{3}
$$

Mais comme on utilise l'**argument principal** pour la définition du logarithme :

$$
\ln((-1+i\sqrt3)^2) = \ln(4e^\frac{4i\pi}{3})=\ln(4e^\frac{-2i\pi}{3})=\ln(4)-\frac{2i\pi}{3}
$$

Ainsi

$$
\ln((-1+i\sqrt3)^2)\neq2\ln(-1+i\sqrt3)
$$

De toute façon, il se pose à nouveau des problèmes de continuité. En effet, pour $\theta\in]-\pi,\pi]$, $\ln(e^{i\theta})=i\theta$ tandis que pour $\theta\in]\pi,3\pi]$, $\ln(e^{i\theta})=i\theta-2i\pi$. Ainsi $\ln(e^{i\pi})=i\pi$ mais $\lim_{\theta\to\pi^+}\ln(e^{i\theta})=-i\pi$.

L'applet suivante montre encore le problème de continuité lorsque le point d'affixe $z$ traverse le demi-axe des abscisses négatives.

<iframe scrolling="no" title="Logarithme complexe" src="https://www.geogebra.org/material/iframe/id/pttdmhjp/width/700/height/500/border/888888/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="700px" height="500px" style="border:0px;"> </iframe>

## Conclusion

On a vu comment définir des racines carrées et des logarithmes de complexes de manière unique mais on a vu également que cela posait ensuite des problèmes par la suite car des propriétés algébriques et de continuité des fonctions racine carrée et logarithme n'étaient plus assurées. Il était évidemment possible de définir autrement la racine carrée et le logarithme d'un complexe[^4] mais on aurait constaté qu'on retombait sur les mêmes problèmes.

D'un point de vue très pragmatique, l'emploi des symboles $\sqrt{\phantom{z}}$ pour des complexes non réels positifs et $\ln$ pour des complexes non réels strictement positifs est à proscrire lors de vos épreuves de concours.


[^1]: Cela revient à choisir pour **la** racine carrée d'un complexe $z$ non nul l'unique complexe dont le carré vaut $z$ et dont un argument appartient à l'intervalle $\left]-\frac{\pi}{2},\frac{\pi}{2}\right]$. En effet, les deux racines carrées d'un complexe non nul étant opposées, l'une et l'une seule d'entre elles possède un argument dans l'intervalle $\left]-\frac{\pi}{2},\frac{\pi}{2}\right]$, ce qui se conçoit très bien d'un point de vue géométrique.

[^2]: Le lecteur vérifiera cependant que l'ordre lexicographique est compatible avec l'addition, autrement dit que pour tout triplet $(x,y,z)\in\mathbb C^3$, si $x\leq y$, alors $x+z\leq y+z$.

[^3]: Néanmoins si $z_1$ et $z_2$ sont deux complexes, on peut affirmer que les complexes $\sqrt{z_1z_2}$ et $\sqrt{z_1}\sqrt{z_2}$ sont **égaux ou opposés**.

[^4]: On aurait par exemple plus racine carrée d'un nombre complexe $z$ l'unique complexe dont le carré vaut $z$ et dont un argumment appartient à l'intervalle $]0,\pi]$. Cela revient à modifier l'ordre lexicographique : on compare d'abord les parties imaginaires puis les parties réelles. Quant au logarithme d'un complexe $z$ non nul, on aurait pu choisir l'unique complexe dont l'exponentielle vaut $z$ et dont l'argument appartient à l'intervalle $]0,2\pi]$.
