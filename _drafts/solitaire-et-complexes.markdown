---
layout: "post"
title: "Solitaire et complexes"
published: true
---

L'article qui suit est très inspiré de l'article [A Solitaire Game and its Relation to a Finite Field](http://alexandria.tue.nl/repository/freearticles/598441.pdf) de N. G. de Bruijn. J'ai choisi de remplacer l'utilisation du corps $\dF_4$ par l'anneau $\dZ[j]$ qui est sans doute plus familier des étudiants de première année.

Le jeu du solitaire est un jeu sur plateau bien connu :

### Solitaire anglais

<div>
    <iframe width="380" height="380" frameBorder="0" src="/js/solitaire_english.html"></iframe>
</div>

### Solitaire français

<div>
    <iframe width="380" height="380" frameBorder="0" src="/js/solitaire_french.html"></iframe>
</div>

### Mouvements

<div>
<svg height="200" width="210">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5"
      markerWidth="10" markerHeight="10"
      orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" />
  </marker>
</defs>
    <rect x="0" y="0" width="210" height="200" fill="none" stroke-width="1" stroke="black" rx="10" ry="10"/>
    <circle cx="30" cy="60" r="20" stroke="black" stroke-width="3" fill="blue" />
    <circle cx="100" cy="60" r="20" stroke="black" stroke-width="3" fill="green" />
    <circle cx="170" cy="60" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <path d="M30 40 C 50 00, 150 00, 170 40" stroke="black" fill="transparent" marker-end="url(#arrow)" />
    <circle cx="30" cy="170" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <circle cx="100" cy="170" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <circle cx="170" cy="170" r="20" stroke="black" stroke-width="3" fill="green" />
    <path d="M 90 100 l 0 20 l -10 00 l 20 20 l 20 -20 l -10 00 l 00 -20 z"/>
</svg>

<svg height="200" width="210">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5"
      markerWidth="10" markerHeight="10"
      orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" />
  </marker>
</defs>
    <rect x="0" y="0" width="210" height="200" fill="none" stroke-width="1" stroke="black" rx="10" ry="10"/>
    <circle cx="30" cy="60" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <circle cx="100" cy="60" r="20" stroke="black" stroke-width="3" fill="green" />
    <circle cx="170" cy="60" r="20" stroke="black" stroke-width="3" fill="blue" />
    <path d="M30 40 C 50 00, 150 00, 170 40" stroke="black" fill="transparent" marker-start="url(#arrow)" />
    <circle cx="30" cy="170" r="20" stroke="black" stroke-width="3" fill="green" />
    <circle cx="100" cy="170" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <circle cx="170" cy="170" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <path d="M 90 100 l 0 20 l -10 00 l 20 20 l 20 -20 l -10 00 l 00 -20 z"/>
</svg>
</div>

<div>
<svg height="200" width="210">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5"
      markerWidth="10" markerHeight="10"
      orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" />
  </marker>
</defs>
    <rect x="0" y="0" width="210" height="200" fill="none" stroke-width="1" stroke="black" rx="10" ry="10"/>
    <circle cx="60" cy="30" r="20" stroke="black" stroke-width="3" fill="blue" />
    <circle cx="60" cy="100" r="20" stroke="black" stroke-width="3" fill="green" />
    <circle cx="60" cy="170" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <path d="M40 30 C 00 50, 00 150, 40 170" stroke="black" fill="transparent" marker-end="url(#arrow)" />
    <circle cx="170" cy="30" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <circle cx="170" cy="100" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <circle cx="170" cy="170" r="20" stroke="black" stroke-width="3" fill="green" />
    <path d="M 100 90 l 20 0 l 0 -10 l 20 20 l -20 20 l 00 -10 l -20 00 z"/>
</svg>

<svg height="200" width="210">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5"
      markerWidth="10" markerHeight="10"
      orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" />
  </marker>
</defs>
    <rect x="0" y="0" width="210" height="200" fill="none" stroke-width="1" stroke="black" rx="10" ry="10"/>
    <circle cx="60" cy="30" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <circle cx="60" cy="100" r="20" stroke="black" stroke-width="3" fill="green" />
    <circle cx="60" cy="170" r="20" stroke="black" stroke-width="3" fill="blue" />
    <path d="M40 30 C 00 50, 00 150, 40 170" stroke="black" fill="transparent" marker-start="url(#arrow)" />
    <circle cx="170" cy="30" r="20" stroke="black" stroke-width="3" fill="green" />
    <circle cx="170" cy="100" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <circle cx="170" cy="170" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <path d="M 100 90 l 20 0 l 0 -10 l 20 20 l -20 20 l 00 -10 l -20 00 z"/>
</svg>
</div>

## L'anneau $\dZ[j]$

On rappelle que $j$ est une **racine cubique** de l'unité et que, par conséquent,

$$
j^3=0 \qquad\text{et}\qquad 1+j+j^2=0
$$

On considère alors l'ensemble suivant.

$$
\dZ[j]=\left\{a+bj,\;(a,b)\in\dZ^2\right\}
$$

On prouve aisément que $\dZ[j]$ est un **anneau** pour les lois usuelles. Comme $j$ et $j^{-1}=-1-j$ appartiennent à $\dZ[j]$, $j^n$ appartient également à $\dZ[j]$ pour tout $n\in\dZ$. Plus précisément :

-   si $n\equiv0[3]$, $j^n=1$ ;
-   si $n\equiv1[3]$, $j^n=j$ ;
-   si $n\equiv2[3]$, $j^n=j^2=-1-j$.

On peut notamment définir une fonction Python calculant les coordonnées de $j^n$ dans la base $(1,j)$.

```python
def coord(n):
    if n % 3 == 0:
        return (1, 0)
    if n % 3 == 1:
        return (0, 1)
    if n % 3 == 2:
        return (-1, -1)
```


On dira que $u\in\dZ[j]$ et $v\in\dZ[j]$ sont congrus modulo 2 et on notera $u\equiv v[2]$ s'il existe $w\in\dZ[j]$ tel que $u=v+2w$. De manière équivalente, $u=a+bj$ et $v=c+d$ sont congrus modulo 2 si $a\equiv c[2]$ et $b\equiv d[2]$ (au sens de la congruence usuelle sur les entiers).

## Deux invariants

$$
\begin{align}
A(S)&=\sum_{(k,\ell)\in S}j^{k+l}
&
B(S)&=\sum_{(k,\ell)\in S}j^{k-l}
\end{align}
$$

```python
def A(S):
    c = [coord(k + l) for k, l in S]
    return sum(a for a, b in c), sum(b for a, b in c)


def B(S):
    c = [coord(k - l) for k, l in S]
    return sum(a for a, b in c), sum(b for a, b in c)
```

Nous allons d'abord regarder l'effet sur $A(S)$ et $B(S)$ d'un mouvement d'un pion vers la droite. Supposons que $(k_0,\ell_0)$ et $(k_0+1,\ell_0)$ appartiennent à $S$ mais que $(k_0+2,\ell_0)$ n'appartienne pas à $S$. Si cette dernière position figure sur le tableau de jeu, on peut déplacer le pion en position $(k_0,\ell_0)$ vers la position $(k_0+2,\ell_0)$. Notons $S'$ la configuration ainsi obtenue. Si on récapitule :

* un pion a disparu en $(k_0,\ell_0)$ ;
* un pion a disparu en $(k_0+1,\ell_0)$ ;
* un pion est apparu en $(k_0+2,\ell_0)$.

<svg height="230" width="310">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5"
      markerWidth="10" markerHeight="10"
      orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" />
  </marker>
</defs>
    <circle cx="30" cy="60" r="20" stroke="black" stroke-width="3" fill="green" />
    <circle cx="140" cy="60" r="20" stroke="black" stroke-width="3" fill="green" />
    <circle cx="250" cy="60" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <circle cx="30" cy="200" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <circle cx="140" cy="200" r="20" stroke="black" stroke-width="3" fill="transparent" />
    <circle cx="250" cy="200" r="20" stroke="black" stroke-width="3" fill="green" />
    <path d="M30 40 C 50 00, 230 00, 250 40" stroke="black" fill="transparent" marker-end="url(#arrow)" />
    <path d="M 130 120 l 0 20 l -10 00 l 20 20 l 20 -20 l -10 00 l 00 -20 z"/>
    <foreignObject x="0" y="80" width="160" height="160">
    <div>
      $(k_0,\ell_0)$
    </div>
    </foreignObject>
    <foreignObject x="90" y="80" width="160" height="160">
    <div>
      $(k_0+1,\ell_0)$
    </div>
    </foreignObject>
    <foreignObject x="210" y="80" width="160" height="160">
    <div>
      $(k_0+2,\ell_0)$
    </div>
    </foreignObject>
</svg>

Finalement,

$$
\begin{align}
A(S')&=A(S)-j^{k_0+\ell_0}-j^{k_0+1+\ell_0}+j^{k_0+2+\ell_0}\\
&=A(S)+j^{k_0+\ell_0}(j^2-j-1)\\
&=A(S)+2j^{k_0+\ell_0+2}\\
&\equiv A(S)[2]\\[2em]
B(S')&=B(S)-j^{k_0-\ell_0}-j^{k_0+1-\ell_0}+j^{k_0+2-\ell_0}\\
&=B(S)+j^{k_0-\ell_0}(j^2-j-1)\\
&=B(S)+2j^{k_0-\ell_0+2}\\
&\equiv B(S)[2]
\end{align}
$$

On laisse le lecteur vérifier qu'il en est de même lors du mouvement d'un pion vers la gauche, le haut ou le bas. Finalement, la classe de congruence modulo 2 de $A(S)$ et $B(S)$ reste la même tout au long d'une partie.

## Positions finales gagnantes possibles

Notons $P$ l'ensemble des positions possibles et $S$ la configuration initiale, c'est-à-dire l'ensemble des positions initiales des pions. Si le joueur a gagné, il ne reste plus qu'un pion sur le plateau en une certaine position $(k,\ell)\in P$. D'après ce qui précéde, cette position finale doit vérifier $$A(\{(k,\ell)\})\equiv A(S)[2]$$ et $$B(\{(k,\ell)\})\equiv B(S)[2]$$. On constate alors qu'il existe assez peu de positions finales possibles.

### A l'aide de Python

```python
def possible(S, P):
    def mod(t): return t[0] % 2, t[1] % 2
    A0 = mod(A(S))
    B0 = mod(B(S))
    return [(k, l) for k, l in P
        if mod(A([(k, l)])) == A0 and mod(B([(k, l)])) == B0]
```

#### Solitaire anglais

```python
S = [(k, l) for k in range(-3, 4) for l in range(-3, 4)
     if (abs(k) <= 1 or abs(l) <= 1) and (k, l) != (0, 0)]
P = S + [(0, 0)]

print(possible(S, P))
```

Les positions gagnantes finales possibles sont $(-3, 0), (0, -3), (0, 3), (3, 0), (0, 0)$.

#### Solitaire français

```python
S = [(k, l) for k in range(-3, 4) for l in range(-3, 4)
     if (abs(k) + abs(l) <= 4) and (k, l) != (0, 1)]
P = S + [(0, 1)]

print(possible(S, P))
```

Les positions gagnantes finales possibles sont $(-3, -1), (0, -1), (0, 2), (3, -1)$.

### A la main

On peut également déterminer les positions gagnantes finales possibles "à la main".

Pour calculer les valeurs de $A$ et $B$ pour la configuration initiale, on peut remarquer que trois pions consécutifs disposés horizontalement ou verticalement ont une contribution nulle aux sommes définissant $A$ et $B$ puisque $1+j+j^2=0$.

#### Solitaire anglais

$A(S)=B(S)=-1\equiv1[2]$

Une éventuelle position finale gagnante $(k,\ell)\in P$ doit donc vérifier $j^{k+\ell}\equiv1[2]$ et $j^{k-\ell}\equiv1[2]$. Or on rappelle que

-   si $n\equiv0[3]$, $j^n=1\equiv1[2]$ ;
-   si $n\equiv1[3]$, $j^n=j\not\equiv1[2]$ ;
-   si $n\equiv2[3]$, $j^n=j^2=-1-j\not\equiv1[2]$.

On en déduit que $k+\ell\equiv0[3]$ et $k-\ell\equiv0[3]$, puis que $2k\equiv0[3]$ et $2\ell\equiv0[3]$ et enfin que $k\equiv0[3]$ et $\ell\equiv0[3]$. Mais, puisque $(k,\ell)\in P$, les seules possibilités sont $(-3, 0), (0, -3), (0, 3), (3, 0), (0, 0)$.

#### Solitaire français

$A(S)=1-j\equiv1+j[2]$ et $B(S)=2+j\equiv j[2]$

-   si $n\equiv0[3]$, $j^n=1\equiv1[2]$ ;
-   si $n\equiv1[3]$, $j^n=j\equiv j[2]$ ;
-   si $n\equiv2[3]$, $j^n=j^2=-1-j\equiv1+j[2]$.

On doit donc avoir $k+\ell\equiv2[3]$ et $k-\ell\equiv1[3]$. Ainsi $2k\equiv0[3]$ et $2\ell\equiv1[3]$. Puisque $2\equiv-1[3]$, $k\equiv0[3]$ et $\ell\equiv-1[3]$. A nouveau, puisque $(k,\ell)\in P$, les seules possibilités sont $(-3, -1), (0, -1), (0, 2), (3, -1)$.
