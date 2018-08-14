---
layout: "post"
title: "Dualité"
published: true
---


La dualité est le lien qui existe entre un $\dK$-espace vectoriel $E$ et son espace dual $E^\star$. On rappelle que $E^\star$ est l'espace vectoriel des formes linéaires sur $E$.

## Base duale
---

Etant donné une base d'un espace vectoriel de dimension finie, il existe une manière élémentaire de contruire une base de l'espace dual à partir de celle-ci.

**Définition [Base duale]**
Soient $E$ un espace de dimension finie et une base $(e_1,\dots,e_n)$ de $E$. Pour tout $i\in\lb1,n\rb$, on note $e_i^\star$ l'unique forme linéaire sur $E$ telle que $e_i^\star(e_j)=\delta_{i,j}$ pour tout $j\in\lb1,n\rb$.<br/>
La famille $(e_1^\star,\dots,e_n^\star)$ est une base de $E^\star$ appelée **base duale** de la base $(e_1,\dots,e_n)$.

*Preuve.*
Puisque $\dim E^\star=\dim E=n$, il suffit de montrer que cette famille est libre. Si l'on se donne $(\lambda_1,\dots,\lambda_n)\in\dK^n$ tel que $\sum_{i=1}^n\lambda_ie_i^\star=0$, on obtient $\lambda_j=0$ pour chaque $j\in\lb1,n\rb$ en évaluant l'égalité précédente en $e_j$. &#x2b1b;

<!-- Donner un exemple -->

Les éléments de la base duale portent aussi le nom de _formes linéaires coordonnées_. Si l'espace $E$ est de dimension infinie et possède une base $(e_i)_{i\in I}$, on peut encore construire la famille des formes coordonnées $(e_i^\star)_{i\in I}$ mais cette famille n'est plus forcément une base de $E^\star$. On prouve aisément comme précédemment que cette famille est libre mais on ne peut plus utiliser l'argument de dimension pour en conclure que c'est une base.

Par exemple, les formes linéaires coordonnées associées à la base canonique de $\dK[X]$ sont les formes linéaires $\va_k\colon P\in\dK[X]\mapsto\frac{P^{(k)}(0)}{k!}$. Ces formes linéaires ne forment pas une base du dual de $\dK[X]$. En effet, la forme linéaire $P\in\dK[X]\mapsto$

**Définition [Base antéduale]**

Base antéduale, polynômes interpolateurs de Lagrange

## Orthogonalité
---

**Définition [Orthogonalité]** Soit $E$ un espace vectoriel.

* Si $A$ est une partie de $E$, on appelle **orthogonal** de $A$ le sous-espace vectoriel de $E^\star$ suivant

$$
A^\circ=\left\lbrace \varphi\in E^\star,\;\forall x\in A,\;\varphi(x)=0\right\rbrace
$$

* Si $B$ est une partie de $E^\star$, on appelle **orthogonal** de $B$ le sous-espace vectoriel de $E$ suivant

$$
{}^\circ B=\left\lbrace x\in E,\;\forall\varphi\in B,\;\varphi(x)=0\right\rbrace
$$

_Remarque._ On a de manière évidente ${}^\circ(A^\circ)\subset A$ et $({}^\circ B)^\circ\subset B$.


**Proposition [Dimension de l'orthogonal]** Soit $E$ un espace vectoriel de dimension finie.

* Soit $F$ un sous-espace vectoriel de $E$. Alors $\dim F^\circ=\dim E-\dim F$.

* Soit $G$ un sous-espace vectoriel de $E^\star$. Alors $\dim {}^\circ G=\dim E-\dim G$.

*Preuve.* Posons $n=\dim E=\dim E^\star$ et $p=\dim F$. Donnons-nous une base $(e_1,\dots,e_p)$ de $F$ : on peut alors la compléter en une base $(e_1,\dots,e_n)$ de $E$.<br/>
Montrons maintenant que $(e_{p+1}^\star,\dots,e_n^\star)$ est une base de $F^\circ$. Par définition de la base duale, $e_i^\star(e_j)=0$ pour tout $(i,j)\in\lb p+1,n\rb\times\lb 1,p\rb$ puis, $(e_1,\dots,e_p)$ engendrant $F$, $e_i^\star\in F^\circ$ pour tout $i\in\lb p+1,n\rb$ par linéarité. En tant que sous-famille de la base duale $(e_1^\star,\dots,e_n^\star)$, $(e_{p+1}^\star,\dots,e_n^\star)$ est une famille **libre** de vecteurs de $F^\circ$.<br/>
Soit maintenant $\varphi\in F^\circ$. On peut décomposer $\varphi$ dans la base duale $(e_1^\star,\dots,e_n^\star)$ : il existe donc $(\lambda_1,\dots,\lambda_n)\in\dK^n$ tel que $\varphi=\sum_{i=1}^n\lambda_i e_i^\star$. En évaluant en $e_j$, on obtient $\lambda_j=0$ pour $j\in\lb1,p\rb$, puisqu'alors $e_j\in F$. On en déduit donc que $F^\circ\in\vect(e_{p+1}^\star,\dots,e_n^\star)$. La famille $(e_{p+1}^\star,\dots,e_n^\star)$ **engendre** donc $F^\circ$.<br/>
Finalement, $(e_{p+1}^\star,\dots,e_n^\star)$ est une **base** de $F^\circ$ et $\dim F^\circ=n-p$. &#x2b1b;

## Grassmannienne
---

**Définition [Grassmannienne]** On appelle **grassmannienne** d'un espace vectoriel $E$ l'ensemble de ses sous-espaces vectoriels ayant une dimension donnée $k$ : on la notera $G_k(E)$. On notera $G(E)$ l'ensemble de tous les sous-espaces vectoriels de $E$ i.e. $G(E)=\bigcup_{k\in\dN}G_k(E)$.

**Proposition** Soit $E$ un espace vectoriel de dimension finie $n$. L'application qui à un sous-espace vectoriel de $E$ associe son orthogonal est une bijection de $G(E)$ sur $G(E^\star)$. De plus, elle induit une bijection de $G_k(E)$ sur $G_{n-k}(E^\star)$ pour tout $k\in\lb0,n\rb$.

*Preuve.* Notons $\Phi$ l'application en question. Puisque $G(E)=\bigsqcup_{k=0}^nG_k(E)$ et $G(E^\star)=\bigsqcup_{k=0}^nG_{n-k}(E^\star)$, il suffit de montrer que pour chaque
