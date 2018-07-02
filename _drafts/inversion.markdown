---
layout: "post"
title: "Inversion et théorème de Ptolémée"
published: true
---

# Définition d'une inversion

On considère un espace affine euclidien $\mathcal{E}$.

> Si $\Omega$ est un point de $\mathcal{E}$, on appelle **inversion de centre $\Omega$** l'application qui à un point $M$ de $\mathcal{E}$ distinct de $\Omega$ associe le point $M'$ tel que le vecteur $\overrightarrow{\Omega M'}$ soit colinéaire et de même sens que le vecteur $\overrightarrow{\Omega M}$ et de norme inverse de celle de $\overrightarrow{\Omega M}$.

Autrement dit,

$$
\overrightarrow{\Omega M'}=\frac{\overrightarrow{\Omega M}}{\Omega M^2}
$$

L'inversion de centre $\Omega$ est donc l'application

$$
M\in \mathcal{E}\setminus\{\Omega\}\mapsto\Omega+\frac{\overrightarrow{\Omega M}}{\Omega M^2}
$$

On constate immédiatement que l'inversion de centre $\Omega$ est une permutation de $\mathcal{E}\setminus{\Omega}$ puisque c'est clairement une _involution_.

On remarque également que si $M$ et $N$ sont de points de $\mathcal{E}$ distincts de $\Omega$ et $M'$ et $N'$ leurs images respectives par l'inversion de centre $\Omega$, alors

$$
\begin{align*}
M'N'^2&=\left(\overrightarrow{\Omega N'}-\overrightarrow{\Omega M'}\right)^2\\
&=\Omega M'^2+\Omega N'^2-2\overrightarrow{\Omega M'}\cdot\overrightarrow{\Omega N'}\\
&=\frac{1}{\Omega M^2}+\frac{1}{\Omega N^2}-2\frac{\overrightarrow{\Omega M}\cdot\overrightarrow{\Omega N}}{\Omega M^2\cdot\Omega N^2}\\
&=\frac{\Omega M^2+\Omega N^2-2\overrightarrow{\Omega M}\cdot\overrightarrow{\Omega N}}{\Omega M^2\cdot\Omega N^2}\\
&=\frac{\left(\overrightarrow{\Omega N}-\overrightarrow{\Omega M}\right)^2}{\Omega M^2\cdot\Omega N^2}\\
&=\frac{MN^2}{\Omega M^2\cdot\Omega N^2}
\end{align*}
$$

et donc

$$
M'N'=\frac{MN}{\Omega M\cdot\Omega N}
$$

### Formulation complexe

Dans le cas où $\mathcal{E}$ est le **plan complexe** $\mathbb{C}$ muni de sa structure euclidienne ususelle, l'inversion de centre $\omega$ est tout simplement l'application

$$
z\in\mathbb{C}\setminus\{\omega\}\mapsto\omega+\frac{z-\omega}{|z-\omega|^2}=\frac{1}{\overline{z-\omega}}
$$

# Hypersphères et hyperplans

On rappelle qu'un **hyperplan** affine est un sous-espace affine dont la direction est un hyperplan vectoriel, c'est-à-dire le noyau d'une forme linéaire. Si $\mathcal{E}$ est de dimension $2$, un hyperplan affine est une droite affine et si $\mathcal{E}$ est de dimension $3$, un hyperplan affine est un plan affine.

On appelle **hypersphère** de centre $O\in \mathcal{E}$ et de rayon $R\in\mathbb{R}_+$ l'ensemble des points équidistants situés à une distance $R$ de $0$, c'est-à-dire

$$
\left\{M\in \mathcal{E},\;OM=R\right\}
$$

A noter que, si $\mathcal{E}$ est de dimension $2$, alors une hypersphère est un cercle et, si $\mathcal{E}$ est de dimension $3$, alors une hypersphère est une sphère.

### Equation d'un hyperplan

Un hyperplan affine $\mathcal{H}$ contenant un point $O$ et de vecteur normal $\vec n$ est l'ensemble des points $M$ de $\mathcal{E}$ vérifiant $\overrightarrow{OM}\cdot\vec n=0$. Ceci équivaut à $\overrightarrow{\Omega M}\cdot\vec n=k$ avec $k=\overrightarrow{\Omega O}\cdot\vec n$.

Réciproquement, si $k\in\mathbb{R}$ et $\vec n$ est un vecteur non nul, l'ensemble $\mathcal{H}$ des points $M$ de $\mathcal{E}$ vérifiant $\overrightarrow{\Omega M}\cdot\vec n=k$ est bien un hyperplan de $\mathcal{E}$. En effet, la forme linéaire $\varphi\colon\vec u\mapsto\vec u\cdot\vec n$ est non nulle puisque $\vec n$ ne l'est pas : elle est donc surjective. Il existe donc un vecteur $\vec u$ tel que $\vec u\cdot\vec n=k$. On vérifie alors aisément qu'en posant $O=\Omega+\vec u$, $\mathcal{H}=O+\operatorname{Ker}\varphi$.

> Les ensembles d'équations $\overrightarrow{\Omega M}\cdot\vec n=k$, avec $\vec n$ un vecteur non nul et $k\in\mathbb{R}$, sont exactement les hyperplans affines de $\mathcal{E}$.

On peut remarquer que si $k=0$, l'hyperplan affine contient le point $\Omega$.

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

Réciproquement, si $k\in\mathbb{R}$ et $\vec n$ est un vecteur, l'ensemble $\mathcal{S}$ des points $M$ de $\mathcal{E}$ vérifiant

$$
\Omega M^2+\overrightarrow{\Omega M}\cdot\vec n=k
$$

est bien une hypersphère. En effet, en posant $O=\Omega-\frac{1}{2}\vec n$ et $R^2=k+\frac{1}{4}\|\vec n\|^2$, l'équation précédente devient $OM^2=R^2$.

<!-- Problème : $R^2<0$ -->

> Les ensembles d'équations $\Omega M^2+\overrightarrow{\Omega M}\cdot\vec n=k$, avec $\vec n$ un vecteur et $k\in\mathbb{R}$, sont exactement les hypersphères de $\mathcal{E}$.

On peut remarquer que si $k=0$, l'hypersphère contient le point $\Omega$.

# Image des hyperplans affines et des hypersphères par une inversion

Dans tout ce paragraphe, on note $M'$ l'image d'un point $M$ distinct de $\Omega$ par l'inversion de centre $\Omega$.

## Image d'un hyperplan affine

On se donne un hyperplan affine $\mathcal{H}$ de $\mathcal{E}$. Il existe donc un réel $k$ et un vecteur non nul $\vec n$ tel que $\mathcal{H}$ soit l'ensemble des points $M$ tels que $\overrightarrow{\Omega M}\cdot\vec n=k$.

Ainsi, pour tout point $M$ distinct de $\Omega$,

$$
\begin{align*}
M\in\mathcal{H}&\iff\overrightarrow{\Omega M}\cdot\vec n=k\\
&\iff\frac{\overrightarrow{\Omega M}}{\Omega M^2}\cdot\vec n=\frac{k}{\Omega M^2}\\
&\iff\overrightarrow{\Omega M'}\cdot\vec n=k\Omega M'^2
\end{align*}
$$

Si $k=0$, $\mathcal{H}$ est l'hyperplan affine contenant $\Omega$ et de vecteur normal $\vec n$ et son image par l'inversion de centre $\Omega$ est ce même hyperplan affine $\mathcal{H}$.

Si $k\neq0$, $\mathcal{H}$ est un hyperplan affine ne contenant pas $\Omega$ et son image par l'inversion de centre $\Omega$ est l'ensemble des points $M'$ tels que

$$
\Omega M'^2+\overrightarrow{\Omega M'}\cdot\left(-\frac{1}{k}\vec n\right)=0
$$

c'est-à-dire une hypersphère contenant $\Omega$.

<!-- Hyperplans et hypersphères privés de $\Omega$ -->


## Image d'une hypersphère

On se donne une hypersphère $\mathcal{S}$ de $\mathcal{E}$. Il existe donc un réel $k$ et un vecteur $\vec n$ tel que $\mathcal{S}$ soit l'ensemble des points $M$ tels que $\Omega M^2+\overrightarrow{\Omega M}\cdot\vec n=k$.

Ainsi, pour tout point $M$ distinct de $\Omega$,

$$
\begin{align*}
M\in\mathcal{S}&\iff\Omega M^2+\overrightarrow{\Omega M}\cdot\vec n=k\\
&\iff1+\frac{\overrightarrow{\Omega M}}{\Omega M^2}\cdot\vec n=\frac{k}{\Omega M^2}\\
&\iff1+\overrightarrow{\Omega M'}\cdot\vec n=k\Omega M'^2
\end{align*}
$$

Si $k=0$, $\mathcal{S}$ est une hypersphère contenant $\Omega$ et son image par l'inversion de centre $\Omega$ est un hyperplan affine ne contenant pas $\Omega$.

Si $k\neq0$, $\mathcal{S}$ est une hypersphère ne contenant pas $\Omega$ et son image par l'inversion de centre $\Omega$ est l'ensemble des points $M'$ tels que

$$
\Omega M'^2+\overrightarrow{\Omega M'}\cdot\left(-\frac{1}{k}\vec n\right)=\frac{1}{k}
$$

c'est-à-dire une hypersphère ne contenant pas $\Omega$.

<!-- Hyperplans et hypersphères privés de $\Omega$ -->


## Simulation

On peut se convaincre de ces résultats à l'aide de [scripts Python][bc821efa].

Il s'agit en fait de *notebooks* [Jupyter][aab9dd5e] éditables.


# Inégalité de Ptolémée

On se place maintenant dans le cas où $\mathcal{E}$ est un *plan* affine euclidien.

* L'image d'une droite $\mathcal{D}$ par l'inversion de centre $\Omega$ est donc un cercle passant par $\Omega$ si $\mathcal{D}$ ne passe pas par $\Omega$ et $\mathcal{D}$ elle-même sinon.
* De même, l'image d'un cercle $\mathcal{C}$ par l'inversion de centre $\Omega$ est un cercle ne passant pas par $\Omega$ si $\mathcal{C}$ ne passe pas par $\Omega$ et une droite ne passant pas par $\Omega$ sinon.

On considère quatre points $A$, $B$, $C$ et $D$ deux à deux distincts de l'espace affine $\mathcal{E}$. On note $A'$, $B'$ et $C'$ les images des points $A$, $B$ et $C$ par l'inversion de centre $D$.

Remarquons que

$$
\begin{align*}
A'B'&=\frac{AB}{AD\cdot BD}
&
B'C'&=\frac{BC}{BD\cdot CD}
&
A'C'&=\frac{AC}{AD\cdot CD}
\end{align*}
$$

Par inégalité triangulaire

$$
\frac{AC}{AD\cdot CD}=A'C'\leq A'B'+B'C'=\frac{AB}{AD\cdot BD}+\frac{BC}{BD\cdot CD}
$$

ou encore

$$
AC\cdot BD\leq AB\cdot CD+AD\cdot BC
$$

## Cas d'égalité

Le cas d'égalité dans l'inégalité précédente se produit si et seulement si $A'C'=A'B'+B'C'$ autrement dit si et seulement si $A'$, $B'$ et $C'$ sont alignés dans cet ordre.

#### Cas de cocyclicité

Si $A'$, $B'$ et $C'$ sont alignés dans cet ordre mais non alignés avec $D$, alors leurs images par l'inversion de centre $D$, à savoir les points $A$, $B$ et $C$ (car l'inversion est une involution), sont placées sur un cercle $\mathcal{C}$ passant par $D$. De plus, l'inversion de centre $D$ est continue sur $\mathcal{E}\setminus\{D\}$ donc l'image d'une partie connexe par arcs est connexe par arcs. Notamment l'image de $[A'C']$ par l'inversion de centre $D$ est une partie connexe par arcs du cercle $\mathcal{C}$. Comme l'inversion de centre $D$ est également injective[^arc_cercle], il s'agit de l'arc du cercle $\mathcal{C}$ d'extrémités $A$ et $C$ ne contenant pas $D$ ($D$ n'est pas dans l'image de l'inversion). Puisque $B'$ appartient à $[A'C']$, $B$ appartient à cet arc de cercle. Finalement, $A$, $B$, $C$ et $D$ sont cocycliques dans cet ordre.

Réciproquement, supposons que $A$, $B$, $C$, $D$ soient cocycliques dans cet ordre. Alors $A'$, $B'$ et $C'$ sont alignés et le même argument de connexité et d'injectivité que précédemment montre qu'ils sont alignés dans cet ordre.

#### Cas d'alignement

Si les points $A'$, $B'$ et $C'$ sont alignés dans cet ordre avec $D$ sur une droite $\mathcal{D}$, alors leurs images, à savoir les points $A$, $B$ et $C$, sont également alignées sur cette même droite $\mathcal{D}$. Remarquons alors que les points $A$, $B$ et $C$ sont tous sur la même demi-droite issue de $D$ et alignés dans cet ordre.

Evidemment, puisque l'inversion de centre $D$ est une involution, la réciproque est égalemement vraie : si $A$,$B$ et $C$ sont alignés dans cet ordre sur une même demi-droite issue de $D$, alors il en est de même des points $A'$, $B'$ et $C'$.


#### Conclusion

Finalement, le cas d'égalité dans l'inégalité de Ptolémée ne se produit que dans les deux cas suivants :

* $A$, $B$, $C$ et $D$ sont cocycliques dans cet ordre ;

* $A$, $B$, $C$, $D$ sont alignés dans l'ordre $A-B-C-D$ ou $D-A-B-C$.

<!-- Dispositif de Peaucellier-Lipkin : faire une animation GeoGebra -->


# Points à l'infini

Intuitivement, un hyperplan affine peut être vu comme une sphère de rayon infini. Les hyperplans affines peuvent alors être vus comme des cas particuliers d'hypersphères.

Notamment, on peut donner une équation générique d'hyperplan/hypersphère :

$$
\alpha\Omega M^2+\overrightarrow{\Omega M}\cdot\vec n=k
$$

avec $\alpha$, $\vec n$ et $k$ non tous trois nuls. En notant $M'$ l'image du point $M$ par l'inversion de centre $\Omega$, cette équation équivaut à

$$
k\Omega M'^2-\overrightarrow{\Omega M'}\cdot\vec n=\alpha
$$

On retrouve bien le fait que l'image d'un hyperplan/hypersphère est bien un hyperplan/hypersphère.





<!-- Hyperplan = hypersphère de rayon infini : ça explique les deux ordres dans le cas d'alignement -->
<!-- Blabla sur compactifié d'Alexandrov -->


---

##### Notes

  [bc821efa]: https://www.kaggle.com/lgarcin/inversion/edit "Inversion"

  [aab9dd5e]: http://jupyter.org/ "Jupyter"

  [^arc_cercle]: Plus précisément, la composée de l'application $t\in[0,1]\mapsto(1-t)A+tB$ (chemin décrivant le segment $[AB]$) par l'inversion de centre $D$ est injective : elle ne prend donc qu'une fois les valeurs $A'$ et $B'$, respectivement en $0$ et $1$.
