---
layout: "post"
title: "Inversion et inégalité de Ptolémée"
published: true
---

# Définition d'une inversion

On considère un espace affine euclidien $E$.

> Si $\Omega$ est un point de $E$, on appelle **inversion de centre $\Omega$** l'application qui à un point $M$ de $E$ distinct de $\Omega$ associe le point $M'$ tel que le vecteur $\overrightarrow{\Omega M'}$ soit colinéaire et de même sens que le vecteur $\overrightarrow{\Omega M}$ et de norme inverse de celle de $\overrightarrow{\Omega M}$.

Autrement dit,

$$
\overrightarrow{\Omega M'}=\frac{\overrightarrow{\Omega M}}{\Omega M^2}
$$

L'inversion de centre $\Omega$ est donc l'application

$$
M\in E\setminus\{\Omega\}\mapsto\Omega+\frac{\overrightarrow{\Omega M}}{\Omega M^2}
$$

On constate immédiatement que l'inversion de centre $\Omega$ est une permutation de $E\setminus{\Omega}$ puisque c'est clairement une _involution_.

### Formulation complexe

Dans le cas où $E$ est le **plan complexe** $\mathbb{C}$ muni de sa structure euclidienne ususelle, l'inversion de centre $\omega$ est tout simplement l'application

$$
z\in\mathbb{C}\setminus\{\omega\}\mapsto\omega+\frac{z-\omega}{|z-\omega|^2}=\frac{1}{\overline{z-\omega}}
$$

# Hypersphères et hyperplans

On rappelle qu'un **hyperplan** affine est un sous-espace affine dont la direction est un hyperplan vectoriel, c'est-à-dire le noyau d'une forme linéaire. Si $E$ est de dimension $2$, un hyperplan affine est une droite affine et si $E$ est de dimension $3$, un hyperplan affine est un plan affine.

On appelle **hypersphère** de centre $O\in E$ et de rayon $R\in\mathbb{R}_+$ l'ensemble des points équidistants situés à une distance $R$ de $0$, c'est-à-dire

$$
\left\{M\in E,\;OM=R\right\}
$$

A noter que, si $E$ est de dimension $2$, alors une hypersphère est un cercle et, si $E$ est de dimension $3$, alors une hypersphère est une sphère.

### Equation d'un hyperplan

Un hyperplan affine $\mathcal{H}$ passant par un point $O$ et de vecteur normal $\vec n$ est l'ensemble des points $M$ de $E$ vérifiant $\overrightarrow{OM}\cdot\vec n=0$. Ceci équivaut à $\overrightarrow{\Omega M}\cdot\vec n=k$ avec $k=\overrightarrow{\Omega O}\cdot\vec n$.

Réciproquement, si $k\in\mathbb{R}$ et $\vec n$ est un vecteur non nul, l'ensemble $\mathcal{H}$ des points $M$ de $E$ vérifiant $\overrightarrow{\Omega M}\cdot\vec n=k$ est bien un hyperplan de $E$. En effet, la forme linéaire $\varphi\colon\vec u\mapsto\vec u\cdot\vec n$ est non nulle puisque $\vec n$ ne l'est pas : elle est donc surjective. Il existe donc un vecteur $\vec u$ tel que $\vec u\cdot\vec n=k$. On vérifie alors aisément qu'en posant $O=\Omega+\vec u$, $\mathcal{H}=O+\operatorname{Ker}\varphi$.

> Les ensembles d'équations $\overrightarrow{\Omega M}\cdot\vec n=k$, avec $\vec n$ un vecteur non nul et $k\in\mathbb{R}$, sont exactement les hyperplans affines de $E$.

### Equation d'une hypersphère

L'hypersphère $\mathcal{S}$ de centre $O$ et de rayon $R$ est l'ensemble des points $M$ vérifiant $OM^2=R^2$. En remarquant que $\overrightarrow{OM}=\overrightarrow{O\Omega}+\overrightarrow{\Omega M}$, ceci se réécrit via une identité remarquable

$$
O\Omega^2+2\overrightarrow{O\Omega}\cdot\overrightarrow{\Omega M}+\Omega M^2=R^2
$$

ou encore

$$
\Omega M^2+\overrightarrow{\Omega M}\cdot\vec n=k
$$

en posant $\vec n=2\overrightarrow{O\Omega}$ et $k=R^2-O\Omega^2$.

Réciproquement, si $k\in\mathbb{R}$ et $\vec n$ est un vecteur, l'ensemble $\mathcal{S}$ des points $M$ de $E$ vérifiant

$$
\Omega M^2+\overrightarrow{\Omega M}\cdot\vec n=k
$$

est bien une hypersphère. En effet, en posant $O=\Omega-\frac{1}{2}\vec n$ et $R^2=k+\frac{1}{4}\|\vec n\|^2$, l'équation précédente devient $OM^2=R^2$.

<!-- Problème : $R^2<0$ -->

> Les ensembles d'équations $\Omega M^2+\overrightarrow{\Omega M}\cdot\vec n=k$, avec $\vec n$ un vecteur et $k\in\mathbb{R}$, sont exactement les hypersphères de $E$.


# Image des hyperplans et des hypersphères par une inversion

Il est à peu près évident qu'un hyperplan est invariant par une inversion dont le centre appartient à cet hyperplan.

De même, on montre facilement que l'image d'une hypersphère de centre $\Omega$ et de rayon $R$ non nul par l'inversion de centre $\Omega$ est l'hypersphère de centre $\Omega$ et de rayon $1/R$.


Le phénomène est en fait plus général. L'image d'un hyperplan par une inversion de centre n'appartenant pas à cet hyperplan est une hypersphère.

On peut du moins s'en convaincre en dimension $2$, à l'aide d'un script Python. On utilise la formulation en termes de complexes d'une inversion.

```python
from numpy import linspace, logspace, concatenate
from matplotlib.pyplot import plot, show, axis, xlim, ylim, grid, legend
vec = 3 + 1j
pt = 1 + 1j
l = logspace(-10, 1, 1000)
l = concatenate((-l[::-1], l))
droite = vec * l + pt
image = 1. / droite.conjugate()
axis('equal')
xlim([-1, 2])
ylim([-1, 2])
grid()
plot(droite.real, droite.imag, label='droite')
plot(image.real, image.imag, label='image')
legend()
show()
```

```python
from numpy import linspace, exp, pi
from matplotlib.pyplot import plot, show, axis, xlim, ylim, grid, legend
centre = 1 + 1j
rayon = 2
cercle = centre + rayon * exp(1j * linspace(-pi, pi, 1000))
image = 1. / cercle.conjugate()
axis('equal')
xlim([-1, 2])
ylim([-2, 4])
grid()
plot(cercle.real, cercle.imag, label='cercle')
plot(image.real, image.imag, label='image')
legend()
show()
```

```python
from numpy import linspace, exp, pi, sqrt
from matplotlib.pyplot import plot, show, axis, xlim, ylim, grid, legend
centre = 1 + 1j
rayon = sqrt(2)
cercle = centre + rayon * exp(1j * linspace(-pi + pi/4, pi + pi/4, 1000))
image = 1. / cercle.conjugate()
axis('equal')
xlim([-1, 2])
ylim([-2, 4])
grid()
plot(cercle.real, cercle.imag, label='cercle')
plot(image.real, image.imag, label='image')
legend()
show()
```


<!-- Dispositif de Peaucellier-Lipkin : faire une animation GeoGebra -->
