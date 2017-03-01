---
layout: "post"
title: "Systèmes différentiels"
published: true
---

# Champ de vecteurs

On appelle **champ de vecteurs** une application de $\mathbb{R}^n$ dans $\mathbb{R}^n$. Les éléments de l'ensemble de départ sont vus comme des **points** tandis que les éléments de l'ensembles d'arrivée sont vus comme des **vecteurs**.

Par exemple, en physique, les champs électrique et magnétiques sont des champs de vecteur : à tout point de l'espace sont associés deux vecteurs $\overrightarrow{E}$ et $\overrightarrow{B}$.

En dimension $2$ ou $3$, on peut visualiser un champ de vecteurs $f$ en dessinant le vecteur $f(X)$ en tout point $X$.

Voici par exemple ce que donne la représentation du champ de vecteurs $f\colon(x,y)\in\mathbb{R}^2\mapsto(-y,x)$.

![Champ de vecteurs](/images/2017/03/champ1.png)

Maintenant une représentation d'un champ de vecteur un peu plus complexe $f\colon(x,y)\in\mathbb{R}^2\mapsto(\sin(x\cdot y/10),\cos(x\cdot /10))$.

![Champ de vecteurs](/images/2017/03/champ2.png)

## Application aux systèmes différentiels

De manière générale, un système différentiel autonome peut s'écrire sous la forme $X'=f(X)$ où

* $X=(x_1,\dots,x_n)$ est une application de classe $\mathcal{C}^1$ sur $\mathbb{R}$ à valeurs dans $\mathbb{R}^n$ ;

* $f$ est une application continue de $\mathbb{R}^n$ dans $\mathbb{R}^n$, c'est-à-dire un champ de vecteurs.

Voici par exemple le système différentiel en dimension 2 associé au champ de vecteurs $f\colon(x,y)\mapsto(-y,x)$ :

$$
\left\{\begin{align*}x'&=-y\\y'&=x\end{align*}\right.
$$

Dans le cas où $f$ est un endomorphisme de $\mathbb{R}^n$, on parle de système différentiel **linéaire**. On sait alors résoudre explicitement un tel système. Dans le cas où $f$ n'est pas linéaire, le **thèorème de Cauchy-Lipschitz** garantit l'existence d'une solution et son unicité si l'on fournit des conditions initiales (à condition que $f$ soit suffisamment régulier) mais ce n'est pas notre propos. On préfère ici expliquer comment prévoir l'évolution d'une solution d'un système linéaire à partir de la représentation graphique du champ de vecteurs.

Une application $X$ solution du système peut être vue comme une **courbe paramétrée** à valeurs dans $\mathbb{R}^n$. A chaque instant $t$, le vecteur vitesse $X'(t)$ est égal à $f(X(t))$, c'est-à-dire que la trajectoire de $X$ est "guidée" par le champ de vecteurs.


<video controls>
<source src="/images/2017/03/toto.mp4" type="video/mp4">
</video>
