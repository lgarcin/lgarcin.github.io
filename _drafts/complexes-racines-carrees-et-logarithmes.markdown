---
layout: "post"
title: "Complexes, racines carrées et logarithmes"
published: true
---

Il est difficile de faire comprendre aux étudiants que l'emploi des symboles $\sqrt{\phantom{z}}$ et $\ln$ pose problème lorsque l'on manipule des complexes. Je vais tenter de m'expliquer dans ce court article.

Essentiellement, le problème provient du fait que toute notation en mathématiques doit être définie de manière **unique**. Ainsi $\sqrt x$ et $\ln(x)$ doit définir un **unique** objet. Une autre façon de voir les choses est de penser à la racine carrée ou au logarithme en tant qu'**applications** : on sait qu'une application associe à un élément une **unique** image. Voyons pourquoi cela se révèle problématique pour les complexes.

## Racine carrée

Le symbole $\sqrt{\phantom{x}}$ est parfaitement défini pour les réels positifs. En effet, si $x$ est un réel positif, on sait qu'il existe **deux** réels opposés dont le carré vaut $x$ (un seul si $x$ est nul). Mais parmi ces deux réels, l'un d'entre eux seulement est **positif**. C'est à celui-ci qu'on fait référence lorsque l'on parle de **la** racine carrée de $x$.

En ce qui concerne les complexes, la situation initiale est la même : si $z$ est un complexe, il existe deux complexes opposés dont le carré vaut $z$ (un seul si $z$ est nul). Néanmoins, on ne peut pas privilégier l'un par rapport à l'autre : contrairement au cas réel, parler de complexe **positif** n'a aucun sens. Ceci provient du fait qu'il n'existe pas *a priori* de relation d'ordre sur $\mathbb C$ comme il en existe sur $\mathbb R$.

On peut néanmoins définir une relation d'ordre total sur $\mathbb C$, à savoir l'ordre **lexicographique**. Pour comparer deux complexes, on compare d'abord leurs parties réelles puis, si celles-ci sont égales, on compare leurs parties imaginaires. Par exemple, $2+3i\leq5-4i$ car $2\leq 5$ et $1-2i\leq1+4i$ car $-2\leq4$.

L'ordre lexicographique permet alors de parler de complexe *positif*, c'est-à-dire plus grand que $0$ : il s'agit de complexes dont la partie réelle est strictement positive ou dont la partie réelle est nulle et la partie imaginaire positive. On vérifie alors aisément que lorsque deux complexes sont opposés, l'un est toujours *positif* tandis que l'autre est *négatif*.

On pourrait alors définir **la** racine carrée d'un complexe $z$ comme l'unique complexe *positif* dont le carré vaut $z$. Ainsi on pourrait par exemple écrire que $\sqrt{3-4i}=2-i$ car $(2-i)^2=3-4i$ et $2-i\geq0$. La racine carrée d'un complexe ainsi définie est donc toujours *positive*.

Malheureusement, l'ordre lexicographique sur $\mathbb C$ n'est pas *compatible* avec la multiplication[^1]. Par exemple, si l'on pose $z_1=1+i$ et $z_2=2+5i$, alors $z_1$ et $z_2$ sont positifs mais le produit $z_1z_2=-3+7i$ ne l'est plus. On en déduit notamment que la racine carré d'un produit n'est pas toujours le produit des racines carrées[^2]. C'est pour cette raison que l'on évite d'employer le symbole $\sqrt{\phantom{z}}$ pour des complexes.


## Logarithme


[^1]: Le lecteur vérifiera que l'ordre lexicographique est compatible avec l'addition, autrement dit que pour tout triplet $(x,y,z)\in\mathbb C^3$, si $x\leq y$, alors $x+z\leq y+z$.

[^2]: Néanmoins si $z_1$ et $z_2$ sont deux complexes, on peut affirmer que les complexes $\sqrt{z_1z_2}$ et $\sqrt{z_1}\sqrt{z_2}$ sont **égaux ou opposés**.
