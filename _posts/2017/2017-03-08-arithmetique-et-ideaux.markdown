---
layout: post
title: Arithmétique et idéaux
published: true
---

## Arithmétique dans un anneau

Si $(A,+,\times)$ est un anneau commutatif, on peut définir une relation de divisibilité de la même manière que dans l'anneau $\dZ$ des entiers relatifs ou l'anneau $\dK[X]$ des polynômes à coefficients dans un corps $\dK$ : on dit que $a\in A$ divise $b\in A$ s'il existe $c\in A$ tel que $b=ac$.

## Notion d'idéal

La seule sous-structure d'anneau au programme de MPSI est la structure de sous-anneau. Mais ce n'est pas la structure adaptée pour faire de l'arithmétique dans un anneau.

**Définition [Idéal]** On appelle **idéal** d'un anneau commutatif $(A,+,\times)$ toute partie $I$ de $A$ telle que :

* $I$ est un sous-groupe de $(A,+)$ ;
* $I$ est *absorbant* : $\forall(a,x)\in A\times I,\;ax\in I$.

Dans le cas particulier de $\dZ$, on vérifie aisément que les idéaux sont en fait les sous-groupes de $\dZ$.

La structure d'idéal est plus *riche* que celle de sous-anneau. Par exemple, le seul sous-anneau de $\dZ$ est $\dZ$ lui-même tandis qu'il possède une infinité d'idéaux. Par ailleurs, le noyau d'un morphisme d'anneaux n'est même pas un sous-anneau mais ... un idéal.

On laisse le lecteur vérifier un résultat qui nous sera utile dans la suite, à savoir que la somme et l'intersection de deux (ou plus) idéaux d'un anneau est encore un idéal de cet anneau.

## Idéaux principaux

Notamment, les ensembles $xA=\lbrace ax,\;a\in A\rbrace $ sont des idéaux de $A$ appelés *idéaux principaux*. La relation de divisibilité se traduit alors aisément à l'aide des idéaux principaux : $x$ divise $y$ si et seulement si $yA\subset xA$.

Un anneau dont tous les idéaux sont principaux est appelé un *anneau principal*.

## Division euclidienne

L'existence d'une division euclidienne dans $\dZ$ et $\dK[X]$ garantit que tous leurs idéaux sont principaux : ce sont donc des anneaux principaux.

Traitons par exemple le cas de $\dK[X]$. Donnons-nous un idéal $I$ de $\dK[X]$. Si $I=\lbrace 0\rbrace $, $I$ est évidemment principal. Sinon, il contient un polynôme non nul de degré minimal : notons-le $P$. On a évidemment $P\dK[X]\subset I$ d'après la propriété d'absorption. Soit alors $A\in\dK[X]$. On écrit alors la division euclidienne de $A$ par $P$ : $A=PQ+R$ avec $\deg R<\deg P$. Alors $R=A-PQ\in I$ donc $R=0$ par minimalité du degré de $P$. Ainsi $A=PQ\in P\dK[X]$. Finalement, $I=P\dK[X]$ est principal.

## PGCD et PPCM dans un anneau principal

L'existence du PGCD de deux (ou plus) éléments d'un anneau est garantie si l'anneau est principal (donc en particulier dans le cas de $\dZ$ ou $\dK[X]$).

Soit en effet deux éléments $x$ et $y$ d'un anneau principal $A$. Alors $xA+yA$ est une somme d'idéaux donc un idéal. Comme tous les idéaux de $A$ sont principaux, il existe $d\in A$ tel que $xA+yA=dA$. Mais alors $xA\subset dA$ et $yA\subset dA$ donc $d$ divise $x$ et $y$. De plus, si $\delta$ est un diviseur commun de $x$ et $y$, alors $xA\subset \delta A$ et $yA\subset \delta A$ donc $dA=xA+yA\subset\delta A$ de sorte que $\delta$ divise $d$. On a bien montré que $d$ était un PGCD de $x$ et $y$.

De même, l'existence d'un PPCM est à nouveau garantie si l'anneau est principal.

Si l'on se donne deux éléments $x$ et $y$ d'un anneau principal $A$, alors $xA\cap yA$ est une intersection d'idéaux donc un idéal. Comme tous les idéaux de $A$ sont principaux, il existe $m\in A$ tel que $xA\cap yA=mA$. Mais alors $mA\subset xA$ et $mA\subset yA$ donc $m$ est un mutiple $x$ et $y$. De plus, si $\mu$ est un multiple commun de $x$ et $y$, alors $\mu A\subset xA$ et $\mu A\subset yA$ donc $\mu A\subset xA\cap yA=mA$ de sorte que $m$ divise $\mu$. On a bien montré que $m$ était un PPCM de $x$ et $y$.
