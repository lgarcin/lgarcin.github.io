---
layout: post
title: Suite logistique
published: false
---

### Introduction

La suite logistique est un système dynamique discret permettant de modéliser l'évolution d'une population. Plus précisément, on considère la suite $(u_n)$ vérifiant la relation de récurrence suivante :

$$
\forall n\in\mathbb{N},\;u_{n+1}=r\cdot u_n\cdot(1-u_n)
$$

Le terme $u_n$ ne représente pas à proprement parler la population mais une fraction d'une population maximale donnée. Pour que la suite $(u_n)$ reste à valeurs dans $[0,1]$, on s'aperçoit qu'il faut choisir $r$ dans $[0,4]$.

---

### Simulation

L'animation GeoGebra suivante représente les termes de cette suite.

<iframe scrolling="no" src="https://www.geogebra.org/material/iframe/id/SzST75DK/width/800/height/700/border/888888/sri/true/sdz/true" width="800px" height="700px" style="border:0px;">
</iframe>

Il est en particulier intéressant de prendre l'indice $k$ du premier terme représenté de l'ordre de $50$ pour avoir une idée du comportement asymptotique de cette suite. Pour plus de précision, on peut faire varier le paramètre $r$ à l'aide des flèches directionnelles : il se passe des choses intéressantes pour $r\in[3,4]$.

---

### Comportement asymptotique

* Lorsque $r\in[0,1]$, on voit clairement que $(u_n)$ converge vers $0$.
* Lorsque $r\in[1,2]$,


 %% Version continue équa diff
