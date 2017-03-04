---
layout: "post"
title: "Dualité"
published: true
---


La dualité est le lien qui existe entre un $\mathbb{K}$-espace vectoriel $E$ et son espace dual $$E^*$$. On rappelle que $$E^*$$ est l'espace vectoriel des formes linéaires sur $E$.

## Base duale
---

**Définition [Base duale]**
Soient $E$ un espace de dimension finie et une base $(e_1,\dots,e_n)$ de $E$. Pour tout $$i\in[\![1,n]\!]$$, on note $$e_i^*$$ l'unique forme linéaire sur $E$ telle que $$e_i^*(e_j)=\delta_{i,j}$$ pour tout $$j\in[\![1,n]\!]$$.<br/>
La famille $$(e_1^*,\dots,e_n^*)$$ est une base de $E^*$ appelée **base duale** de la base $(e_1,\dots,e_n)$.

*Preuve.*
Puisque $$\mathop{\mathrm{dim}}E^*=\mathop{\mathrm{dim}}E=n$$, il suffit de montrer que cette famille est libre. Si l'on se donne $$(\lambda_1,\dots,\lambda_n)\in\mathbb{K}^n$$ tel que $$\sum_{i=1}^n\lambda_ie_i^*=0$$, on obtient $$\lambda_j=0$$ pour chaque $$j\in[\![1,n]\!]$$ en évaluant l'égalité précédente en $$e_j$$. &#x2b1b;

## Orthogonalité
---

**Définition [Orthogonalité]** Soit $E$ un espace vectoriel.<br/>
Si $A$ est une partie de $E$, on appelle **orthogonal** de $A$ le sous-espace vectoriel de $$E^*$$ suivant

$$A^\circ=\left\{\varphi\in E^*,\;\forall x\in A,\;\varphi(x)=0\right\}$$

Si $B$ est une partie de $$E^*$$, on appelle **orthogonal** de $B$ le sous-espace vectoriel de $E$ suivant

$${}^\circ B=\left\{x\in E,\;\forall\varphi\in B,\;\varphi(x)=0\right\}$$

_Remarque._ On a de manière évidente $${}^\circ(A^\circ)\subset A$$ et $$({}^\circ B)^\circ\subset B$$.


**Proposition [Dimension de l'orthogonal]** Soit $F$ un sous-espace vectoriel d'un espace vectoriel $E$ de dimension finie. Alors $\mathop{\mathrm{dim}}F^\circ=\mathop{\mathrm{dim}}E-\mathop{\mathrm{dim}}F$.<br/>
Soit $G$ un sous-espace vectoriel de $$E^*$$, alors $$\mathop{\mathrm{dim}}{}^\circ G=\mathop{\mathrm{dim}}E-\mathop{\mathrm{dim}}G$$.

## Grassmannienne
---

**Définition [Grassmannienne]** On appelle **grassmannienne** d'un espace vectoriel $E$ l'ensemble de ses sous-espaces vectoriels ayant une dimension donnée $k$ : on la notera $G_k(E)$. On notera $G(E)$ l'ensemble de tous les sous-espaces vectoriels de $E$ i.e. $$G(E)=\bigcup_{k\in\mathbb{N}}G_k(E)$$.

**Proposition** Soit $E$ un espace vectoriel de dimension finie $n$. L'application qui à un sous-espace vectoriel de $E$ associe son orthogonal est une bijection de $G(E)$ sur $$G(E^*)$$. De plus, elle induit une bijection de $G_k(E)$ sur $$G_{n-k}(E^*)$$ pour tout $$k\in[\![0,n]\!]$$.

*Preuve.* Notons $\Phi$ l'application en question. Puisque $$G(E)=\bigsqcup_{k=0}^nG_k(E)$$ et $$G(E^*)=\bigsqcup_{k=0}^nG_{n-k}(E^*)$$, il suffit de montrer que pour chaque
