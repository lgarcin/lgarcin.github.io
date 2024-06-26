---
title: Inversion et théorème de Ptolémée
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


On peut le vérifier à l'aide de l'applet suivante. L'image d'une droite $(AB)$ du plan par l'inversion de centre $\Omega$ est bien un cercle passant par $\Omega$ dans le cas général et une droite si $(AB)$ passe par $\Omega$.

<iframe scrolling="no" title="Inversion d'une droite" src="https://www.geogebra.org/material/iframe/id/c85ujr64/width/700/height/400/border/888888/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/true/rc/false/ld/false/sdz/true/ctl/false" width="700px" height="400px" style="border:0px;"> </iframe>

Les points $A$, $B$ et $\Omega$ peuvent être déplacés.


La vidéo suivante montre l'image (en vert) d'un plan mobile (en bleu) par une inversion dont le centre est représenté par un point rouge.

<video controls>
<source src="/images/2018/08/inversion_plan.mp4" type="video/mp4">
</video>

L'image du plan est bien une sphère passant par le centre de l'inversion sauf lorsque le plan passe lui-même par le centre de l'inversion.

<button type="button" class="btn btn-info" data-toggle="collapse" data-target="#inversion-plan">Code Python</button>

```python
from numpy import meshgrid, linspace, cos, sin, pi, ones, logspace
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import figure
from matplotlib.animation import FuncAnimation, writers


def generate_plane(z):
    Zp = z * ones((n, n))
    return Zp


def generate_sphere(z):
    n = x ** 2 + y ** 2 + z ** 2
    Xi = x / n
    Yi = y / n
    Zi = z / n
    return Xi, Yi, Zi


def update(i):
    ax.cla()
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.view_init(-10 + i / frames * 20, i / frames * 180)
    ax.scatter([0], [0], [0], color='red')
    z = -2 + i * 4 / frames
    Zp = generate_plane(z)
    ax.plot_surface(Xp, Yp, Zp, alpha=.5, color='blue')
    Xi, Yi, Zi = generate_sphere(z)
    ax.plot_surface(Xi, Yi, Zi, alpha=.5, color='green')


fig = figure()
ax = fig.gca(projection='3d')

n = 50
x = linspace(-2, 2, n)
y = linspace(-2, 2, n)
Xp, Yp = meshgrid(x, y)

r = logspace(-2, 2, n)
p = linspace(0, 2 * pi, n)
R, P = meshgrid(r, p)
x, y = R * cos(P), R * sin(P)

frames = 100
ani = FuncAnimation(fig, update, frames=frames, interval=100, repeat=True)
Writer = writers['ffmpeg']
writer = Writer(fps=20, metadata=dict(artist='Laurent Garcin'), bitrate=18000)
ani.save('inversion_plan.mp4', writer=writer)
```
{: .collapse #inversion-plan }


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

A nouveau, on peut vérifier que l'image du cercle de rayon $[AB]$ par l'inversion de centre $\Omega$ est bien un cercle dans le cas général et une droite si le cercle de rayon $[AB]$ passe par $\Omega$.

<iframe scrolling="no" title="Inversion d'un cercle" src="https://www.geogebra.org/material/iframe/id/jwjcnx5d/width/700/height/400/border/888888/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/true/rc/false/ld/false/sdz/true/ctl/false" width="700px" height="400px" style="border:0px;"> </iframe>

Les points $A$, $B$ et $\Omega$ peuvent encore être déplacés.


La vidéo qui suit montre l'image (en vert) d'une sphère mobile (en bleu) par une inversion dont le centre est représenté par un point rouge.

<video controls>
<source src="/images/2018/08/inversion_sphere.mp4" type="video/mp4">
</video>

On constate bien que l'image de la sphère mobile est bien une sphère sauf lorsqu'elle passe par le centre de l'inversion, auquel cas c'est un plan.

<button type="button" class="btn btn-info" data-toggle="collapse" data-target="#inversion-sphere">Code Python</button>

```python
from numpy import meshgrid, linspace, cos, sin, pi
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import figure
from matplotlib.animation import FuncAnimation, writers


def generate_sphere(X):
    n = X ** 2 + Y ** 2 + Z ** 2
    Xi = X / n
    Yi = Y / n
    Zi = Z / n
    return Xi, Yi, Zi


def update(i):
    ax.cla()
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.scatter([0], [0], [0], color='red')
    X = X0 - 3 + 6 * i / frames
    ax.plot_surface(X, Y, Z, alpha=.5, color='blue')
    Xi, Yi, Zi = generate_sphere(X)
    ax.plot_surface(Xi, Yi, Zi, alpha=.5, color='green')


fig = figure()
ax = fig.gca(projection='3d')

n = 50
frames = 100

r = 1
p = linspace(0, 2 * pi, n)
t = linspace(-pi / 2, pi / 2)
P, T = meshgrid(p, t)
X0, Y, Z = r * cos(P) * cos(T), r * sin(P) * cos(T), r * sin(T)

ani = FuncAnimation(fig, update, frames=frames, interval=100, repeat=True)
Writer = writers['ffmpeg']
writer = Writer(fps=20, metadata=dict(artist='Laurent Garcin'), bitrate=18000)
ani.save('inversion_sphere.mp4', writer=writer)
```
{: .collapse #inversion-sphere }

# Inégalité de Ptolémée

On se place maintenant dans le cas où $\mathcal{E}$ est un _plan_ affine euclidien.

- L'image d'une droite $\mathcal{D}$ par l'inversion de centre $\Omega$ est donc un cercle passant par $\Omega$ si $\mathcal{D}$ ne passe pas par $\Omega$ et $\mathcal{D}$ elle-même sinon.
- De même, l'image d'un cercle $\mathcal{C}$ par l'inversion de centre $\Omega$ est un cercle ne passant pas par $\Omega$ si $\mathcal{C}$ ne passe pas par $\Omega$ et une droite ne passant pas par $\Omega$ sinon.

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

## <a name="egalite"></a> Cas d'égalité

Le cas d'égalité dans l'inégalité précédente se produit si et seulement si $A'C'=A'B'+B'C'$ autrement dit si et seulement si $A'$, $B'$ et $C'$ sont alignés dans cet ordre.

#### Cas de cocyclicité

Si $A'$, $B'$ et $C'$ sont alignés dans cet ordre mais non alignés avec $D$, alors leurs images par l'inversion de centre $D$, à savoir les points $A$, $B$ et $C$ (car l'inversion est une involution), sont placées sur un cercle $\mathcal{C}$ passant par $D$. De plus, l'inversion de centre $D$ est continue sur $\mathcal{E}\setminus\{D\}$ donc l'image d'une partie connexe par arcs est connexe par arcs. Notamment l'image de $[A'C']$ par l'inversion de centre $D$ est une partie connexe par arcs du cercle $\mathcal{C}$. Comme l'inversion de centre $D$ est également injective[^arc_cercle], il s'agit de l'arc du cercle $\mathcal{C}$ d'extrémités $A$ et $C$ ne contenant pas $D$ ($D$ n'est pas dans l'image de l'inversion). Puisque $B'$ appartient à $[A'C']$, $B$ appartient à cet arc de cercle. Finalement, $A$, $B$, $C$ et $D$ sont cocycliques dans cet ordre.

Réciproquement, supposons que $A$, $B$, $C$, $D$ soient cocycliques dans cet ordre. Alors $A'$, $B'$ et $C'$ sont alignés et le même argument de connexité et d'injectivité que précédemment montre qu'ils sont alignés dans cet ordre.

<iframe scrolling="no" title="Théorème de Ptolémée" src="https://www.geogebra.org/material/iframe/id/nspxn7sh/width/700/height/500/border/888888/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="700px" height="500px" style="border:0px;"> </iframe>

#### Cas d'alignement

Si les points $A'$, $B'$ et $C'$ sont alignés dans cet ordre avec $D$ sur une droite $\mathcal{D}$, alors leurs images, à savoir les points $A$, $B$ et $C$, sont également alignées sur cette même droite $\mathcal{D}$. Remarquons alors que les points $A$, $B$ et $C$ sont tous sur la même demi-droite issue de $D$ et alignés dans cet ordre. En effet, si $A$ et $B$ étaient par exemple sur une même demi-droite issue de $D$ et $C$ sur l'autre demi-droite issue de $D$, $A'$ et $B'$ resteraient sur la même demi-droite issue de $D$, mais dans un ordre inverse, et $C'$ resterait également sur la même demi-droite issue de $D$ : les points $A'$, $B'$ et $C'$ seraient alors alignés sur la même droite mais pas dans cet ordre.

Evidemment, puisque l'inversion de centre $D$ est une involution, la réciproque est égalemement vraie : si $A$,$B$ et $C$ sont alignés dans cet ordre sur une même demi-droite issue de $D$, alors il en est de même des points $A'$, $B'$ et $C'$.

<iframe scrolling="no" title="Théorème de Ptolémée" src="https://www.geogebra.org/material/iframe/id/pwm4grxe/width/700/height/300/border/888888/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="700px" height="300px" style="border:0px;"> </iframe>

#### Conclusion

Finalement, le cas d'égalité dans l'inégalité de Ptolémée ne se produit que dans les deux cas suivants :

* $A$, $B$, $C$ et $D$ sont cocycliques dans cet ordre ;

* $A$, $B$, $C$, $D$ sont alignés dans l'ordre $A-B-C-D$ ou $D-A-B-C$.

<!-- Dispositif de Peaucellier-Lipkin : faire une animation GeoGebra -->


# Point à l'infini

On peut regrouper les équations d'hyperplan et d'hypersphère en une seule équation générique.

$$
\alpha\Omega M^2+\overrightarrow{\Omega M}\cdot\vec n=k
$$

avec $\alpha$, $\vec n$ et $k$ non tous trois nuls. Lorsque $\alpha=0$, on retrouve une équation d'hyperplan et lorsque $\alpha\neq0$, une équation d'hypersphère.


En notant $M'$ l'image du point $M$ par l'inversion de centre $\Omega$, cette équation équivaut à

$$
k\Omega M'^2-\overrightarrow{\Omega M'}\cdot\vec n=\alpha
$$

On retrouve bien le fait que l'image d'un hyperplan/hypersphère est bien un hyperplan/hypersphère.

On peut même aller plus loin dans ce rapprochement entre hypersphères et hyperplans. En effet, un hyperplan peut-être vu comme un cas particulier d'hypersphère quitte à rajouter à l'espace affine $\mathcal{E}$ un **point à l'infini** : un hyperplan est alors une hypersphère de rayon infini passant par ce point à l'infini.

En notant $\infty$ ce point à l'infini, on peut étendre l'inversion $I_\Omega$ de centre $\Omega\in\mathcal{E}$ -- a priori définie sur $\mathcal{E}\setminus\{\Omega\}$ -- en une involution de $\hat{\mathcal{E}}=\mathcal{E}\sqcup\{\infty\}$ en posant $I_\Omega(\Omega)=\infty$ et $I_\Omega(\infty)=\Omega$. Encore mieux, en munissant $\hat{\mathcal{E}}$ d'une topologie adéquate [^alexandrov], toute inversion est alors **continue**. Les arguments de connexité utilisés précédemment fonctionnent alors encore : les images de points alignés ou cocycliques dans un certain ordre restent alignés ou cocycliques dans ce même odre -- y compris lorsque l'un des points ou son image est le point à l'infini.

La preuve du [cas d'égalité](#egalite) dans l'inégalité de Ptolémée se trouve alors simplifiée. Si $A'$, $B'$ et $C'$ sont alignés dans cet ordre, on peut également affirmer que $A'$, $B'$, $C'$ et $\infty$ sont également "alignés dans cet ordre". Leurs images par l'inversion de centre $D$, à savoir les points $A$, $B$, $C$ et $D$ sont alors cocycliques ou alignés dans cet ordre[^ordre]. L'inversion de centre $D$ étant une involution, la réciproque est quasi-automatique.

---

##### Notes

  [^arc_cercle]: Plus précisément, la composée de l'application $t\in[0,1]\mapsto(1-t)A+tB$ (chemin décrivant le segment $[AB]$) par l'inversion de centre $D$ est injective : elle ne prend donc qu'une fois les valeurs $A'$ et $B'$, respectivement en $0$ et $1$.

  [^alexandrov]: On ajoute à la topologie de $\mathcal{E}$ les parties obtenues comme complémentaires de compacts de $\mathcal{E}$, auxquelles on adjoint le point $\infty$ : muni de cette topologie, l'espace $\hat{\mathcal{E}}$ porte le nom de _compactifié d'Alexandrov_ de $\mathcal{E}$. Comme son nom l'indique, il est bien compact.

  [^ordre]: Il faut néanmoins remarquer que toute droite se "referme à l'infini" en un cercle : dire que $A$, $B$, $C$, $D$ sont alignés sur une droite _dans cet ordre_ signifie que les ponts $A$, $B$, $C$ et $D$ sont alignés au sens usuel dans l'ordre $A-B-C-D$ ou $D-A-B-C$.


<!-- TODO Rajouter des dessins -->
