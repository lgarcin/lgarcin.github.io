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

Si $u_0\in\{0,1\}$, il est clair que la suite $(u_n)$ est nulle à partir du rang $1$ quelle que soit la valeur de $r$. On suppose donc $u_0\in]0,1[$ dans la suite.

* Lorsque $r\in[0,1]$, on voit clairement que $(u_n)$ converge vers $0$.
* Lorsque $r\in]1,3]$, la suite $(u_n)$ converge vers un point fixe non nul de $f$ (elle est mononotone à partir d'un certain rang si $r\in]1,2]$ tandis que les suites $(u_{2n})$ et $(u_{2n+1})$ sont adjacentes à partir d'un certain rang lorsque $r\in]2,3]$).


 %% Version continue équa diff
