---
layout: "post"
title: "Dualité"
published: true
---


La dualité est le lien qui existe entre un $$\dK$$-espace vectoriel $$E$$ et son espace dual $$E^*$$. On rappelle que $$E^*$$ est l'espace vectoriel des formes linéaires sur $$E$$.

## Base duale
---

**Définition [Base duale]**
Soient $$E$$ un espace de dimension finie et une base $$(e_1,\dots,e_n)$$ de $$E$$. Pour tout $$i\in[\![1,n]\!]$$, on note $$e_i^*$$ l'unique forme linéaire sur $$E$$ telle que $$e_i^*(e_j)=\delta_{i,j}$$ pour tout $$j\in\lb1,n\rb$$.<br/>
La famille $$(e_1^*,\dots,e_n^*)$$ est une base de $$E^*$$ appelée **base duale** de la base $$(e_1,\dots,e_n)$$.

*Preuve.*
Puisque $$\dim E^*=\dim E=n$$, il suffit de montrer que cette famille est libre. Si l'on se donne $$(\lambda_1,\dots,\lambda_n)\in\dK^n$$ tel que $$\sum_{i=1}^n\lambda_ie_i^*=0$$, on obtient $$\lambda_j=0$$ pour chaque $$j\in\lb1,n\rb$$ en évaluant l'égalité précédente en $$e_j$$. &#x2b1b;

Base antéduale, polynômes interpolateurs de Lagrange

## Orthogonalité
---

**Définition [Orthogonalité]** Soit $$E$$ un espace vectoriel.

* Si $$A$$ est une partie de $$E$$, on appelle **orthogonal** de $$A$$ le sous-espace vectoriel de $$E^*$$ suivant

$$A^\circ=\left\{\varphi\in E^*,\;\forall x\in A,\;\varphi(x)=0\right\}$$

* Si $$B$$ est une partie de $$E^*$$, on appelle **orthogonal** de $$B$$ le sous-espace vectoriel de $$E$$ suivant

$${}^\circ B=\left\{x\in E,\;\forall\varphi\in B,\;\varphi(x)=0\right\}$$

_Remarque._ On a de manière évidente $${}^\circ(A^\circ)\subset A$$ et $$({}^\circ B)^\circ\subset B$$.


**Proposition [Dimension de l'orthogonal]** Soit $$E$$ un espace vectoriel de dimension finie.

* Soit $$F$$ un sous-espace vectoriel de $$E$$. Alors $$\dim F^\circ=\dim E-\dim F$$.

* Soit $$G$$ un sous-espace vectoriel de $$E^*$$. Alors $$\dim {}^\circ G=\dim E-\dim G$$.

*Preuve.* Posons $$n=\dim E=\dim E^*$$ et $$p=\dim F$$. Donnons-nous une base $$(e_1,\dots,e_p)$$ de $$F$$ : on peut alors la compléter en une base $$(e_1,\dots,e_n)$$ de $$E$$.<br/>
Montrons maintenant que $$(e_{p+1}^*,\dots,e_n^*)$$ est une base de $$F^\circ$$. Par définition de la base duale, $$e_i^*(e_j)=0$$ pour tout $$(i,j)\in\lb p+1,n\rb\times\lb 1,p\rb$$ puis, $$(e_1,\dots,e_p)$$ engendrant $$F$$, $$e_i^*\in F^\circ$$ pour tout $$i\in\lb p+1,n\rb$$ par linéarité. En tant que sous-famille de la base duale $$(e_1^*,\dots,e_n^*)$$, $$(e_{p+1}^*,\dots,e_n^*)$$ est une famille **libre** de vecteurs de $$F^\circ$$.<br/>
Soit maintenant $$\varphi\in F^\circ$$. On peut décomposer $$\varphi$$ dans la base duale $$(e_1^*,\dots,e_n^*)$$ : il existe donc $$(\lambda_1,\dots,\lambda_n)\in\dK^n$$ tel que $$\varphi=\sum_{i=1}^n\lambda_i e_i^*$$. En évaluant en $$e_j$$, on obtient $$\lambda_j=0$$ pour $$j\in\lb1,p\rb$$, puisqu'alors $$e_j\in F$$. On en déduit donc que $$F^\circ\in\vect(e_{p+1}^*,\dots,e_n^*)$$. La famille $$(e_{p+1}^*,\dots,e_n^*)$$ **engendre** donc $$F^\circ$$.<br/>
Finalement, $$(e_{p+1}^*,\dots,e_n^*)$$ est une **base** de $$F^\circ$$ et $$\dim F^\circ=n-p$$. &#x2b1b;

## Grassmannienne
---

**Définition [Grassmannienne]** On appelle **grassmannienne** d'un espace vectoriel $$E$$ l'ensemble de ses sous-espaces vectoriels ayant une dimension donnée $$k$$ : on la notera $$G_k(E)$$. On notera $$G(E)$$ l'ensemble de tous les sous-espaces vectoriels de $$E$$ i.e. $$G(E)=\bigcup_{k\in\dN}G_k(E)$$.

**Proposition** Soit $$E$$ un espace vectoriel de dimension finie $$n$$. L'application qui à un sous-espace vectoriel de $$E$$ associe son orthogonal est une bijection de $$G(E)$$ sur $$G(E^*)$$. De plus, elle induit une bijection de $$G_k(E)$$ sur $$G_{n-k}(E^*)$$ pour tout $$k\in[\![0,n]\!]$$.

*Preuve.* Notons $$\Phi$$ l'application en question. Puisque $$G(E)=\bigsqcup_{k=0}^nG_k(E)$$ et $$G(E^*)=\bigsqcup_{k=0}^nG_{n-k}(E^*)$$, il suffit de montrer que pour chaque
