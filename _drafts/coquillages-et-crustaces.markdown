---
title: "Coquillages et crustacés"
---


<div id="observablehq-3655884b">
  <div class="observablehq-widgets"></div>
  <div class="observablehq-renderer"></div>
</div>
<script type="module">
  import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";
  import define from "https://api.observablehq.com/@lgarcin/coquillages-et-crustaces.js?v=3";
  (new Runtime).module(define, name => {
    if (name === "widgets") return Inspector.into("#observablehq-3655884b .observablehq-widgets")();
    if (name === "renderer") return Inspector.into("#observablehq-3655884b .observablehq-renderer")();
  });
</script>

## Surface de la coquille

### Equations paramétriques d'un tore

Pour générer la surface de la coquille, on part d'une forme simple, à savoir un tore. Un tore est engendré par la rotation d'un "petit" cercle de rayon $r$ le long d'un "grand" cercle de rayon $R$. La surface du tore est donc engendrée par deux paramètres $\te$ et $\va$ :

* $\te$ désigne la "position" le long du grand cercle ;
* $\va$ désigne la "position" le long du petit cercle.

![Tore](/tikz/tore.svg)

On obtient donc un paramétrage de la surface du tore en coordonnées cyclindriques.

$$
\begin{aligned}
r(\te,\va)&=R+r\cos\va\\
z(\te,\va)&=r\sin\va
\end{aligned}
$$

### Equations paramétriques de la coquille

On fait ensuite varier le rayon $R$ linéairement en fonction de l'angle $\te$ pour créer une espèce de spirale toroïdale et on ajoute également une fonction linéaire de $\te$ à l'altitude pour "allonger" le coquillage.

$$
\begin{aligned}
r(\te,\va)&=a\te+r\cos\va\\
z(\te,\va)&=b\te+r\sin\va
\end{aligned}
$$

On récupère les coordonnées cartésiennes :

$$
\begin{aligned}
x(\te,\va)&=r(\te,\va)\cos\te=(a\te+r\cos\va)\cos\te\\
y(\te,\va)&=r(\te,\va)\sin\te=(a\te+r\cos\va)\sin\te\\
z(\te,\va)&=b\te+r\sin\va
\end{aligned}
$$

## Calcul des normales

Afin de procéder à l'éclairage de la surface, la bibliothèque de rendu 3D a besoin de connaître les normales à la surface.

En notant $\mathbf{p}=(x,y,z)$, on sait que les vecteurs $\frac{\partial\mathbf p}{\partial\te}$ et $\frac{\partial\mathbf p}{\partial\va}$ sont des vecteurs directeurs du plan tangent à la surface en un point. On obtient donc un vecteur normal à la surface à l'aide du produit vectoriel $\frac{\partial\mathbf p}{\partial\te}\wedge\frac{\partial\mathbf p}{\partial\va}$.

Les calculs étant assez laborieux, on peut les confier à Python et plus particulèrement à la bibliothèque de calcul formel `sympy`.

```python
from sympy import *
from sympy.physics.vector import *

# Création d'un référentiel 3D
N = ReferenceFrame('N')

# Déclaration de variables
ϕ, θ, a, b, r = symbols('ϕ θ a b r')

# Définition du vecteur position
P=(a*θ+r*cos(ϕ))*cos(θ)*N.x+(a*θ+r*cos(ϕ))*sin(θ)*N.y+(b*θ+r*sin(ϕ))*N.z

# Produit vectoriel des dérivées partielles
diff(P,θ,N).cross(diff(P,ϕ,N)).simplify()
```

On obtient le vecteur normal suivant.

$$
\begin{pmatrix}
&&r\left(b\sin\te\sin\va+\left(a\sin\te+\left(a\te+r\cos\va\right)\cos\te\right)\cos\va\right)\\
&&-r\left(b\sin\va\cos\te + \left(a\cos\te-\left(a\te+r\cos\va\right) \sin\te\right)\cos\va\right)\\
&&r\left(a\te+r\cos\va\right)\sin\va
\end{pmatrix}
$$

## Création de la texture
