---
title: Newton et Babylone
---

#### Méthode de Newton

Un algorithme bien connu de résolution d'une équation du type $f(x)=0$ où $f$ est une fonction d'une variable réelle à valeurs réelles est la méthode de **Newton**.

Elle consiste à construire une suite $(u_n)$ par récurrence en posant $u_{n+1}=u_n-\frac{f(u_n)}{f'(u_n)}$ pour tout $n\in\dN$. On comprend très bien géométriquement pourquoi cette méthode fonctionne : $u_{n+1}$ est l'abscisse du point d'intersection de la tangente à la courbe de $f$ au point d'abscisse $u_n$ avec l'axe des abscisses.

Enfin, un petit dessin vaut mieux qu'un long discours. En Python, s'il vous plait.

<iframe src="https://repl.it/HpGe/71?lite=true" width="100%" height="800" frameborder="0"></iframe>

On peut montrer que, sous conditions, la suite $(u_n)$ converge vers une solution de l'équation $f(x)=0$ et que cette convergence est **quadratique** : si $\ell$ est la limite de $(u_n)$, alors il existe $k\in[0,1[$ tel que $u_n-\ell=O(k^{2^n})$. C'est nettement mieux que la méthode par dichotomie où la convergence est linéaire : plus précisément $u_n-\ell=O(1/2^n)$ dans ce cas.

#### Algorithme babylonien

Un cas particulier de la méthode de Newton est connu depuis l'antiquité et consiste en l'extraction d'une racine carrée. En effet, extraire la racine carrée d'un réel positif $a$ consiste à résoudre l'équation $f(x)=0$ où $f(x)=x^2-a$. La méthode de Newton donne alors la relation de récurrence :

$$
u_{n+1}=\frac{1}{2}\left(u_n+\frac{a}{u_n}\right)
$$

#### Application à des équations à inconnues complexes ou matricielles

Ce qui est plus surprenant, c'est que cela marche encore pour les complexes.
<iframe src="https://repl.it/HowB/1?lite=true" width="100%" height="600" frameborder="0"></iframe>

Encore plus surprenant, ça marche pour les matrices.
<iframe src="https://repl.it/Hvfh/8?lite=true" width="100%" height="600" frameborder="0"></iframe>
