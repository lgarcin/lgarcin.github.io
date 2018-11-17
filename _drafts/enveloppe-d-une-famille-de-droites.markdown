---
layout: "post"
title: "Enveloppe d'une famille de droites"
published: true
---

Blabla sur les vidéos


On note $z(t)$ l'affixe du point $M(t)$ en lequel la droite $\cD(t)$ est tangente à la courbe $\cC$ .

<!-- Faire un dessin -->

Puisque les vecteurs $\overrightarrow{A(t)M(t)}$ et $\overrightarrow{A(t)B(t)}$ sont colinéaires,

$$
(z-e_1)\conj{(e_r-e_1)}=\conj{(z-e_1)}(e_r-e_1)
$$

ou encore

$$
z(e_{-r}-e_{-1})-\conj{z}(e_r-e_1)=e_{1-r}-e_{r-1}
$$

D'autre part, les vecteurs $\overrightarrow{M'(t)}$ et $\overrightarrow{A(t)B(t)}$ sont colinéaires.

$$
z'\conj{(e_r-e_1)}=\conj{z'}(e_r-e_1)=\conj{z}'(e_r-e_1)
$$

ou encore

$$
z'(e_{-r}-e_{-1})=\conj{z}'(e_r-e_1)
$$


En dérivant la relation

$$
z'(e_{-r}-e_{-1})-\conj{z}'(e_r-e_1)-iz(re_{-r}-e_{-1})-i\conj{z}(re_r-e_1)
=i(1-r)e_{1-r}-i(r-1)e_{r-1}
$$

Mais en vertu de la relation et après simplification

$$
z(re_{-r}-e_{-1})+\conj{z}(re_r-e_1)=(r-1)(e_{r-1}+e_{1-r})
$$

Pour récapituler, on obtient le système

$$
\left\{\begin{align*}
z(e_{-r}-e_{-1})-\conj{z}(e_r-e_1)&=e_{1-r}-e_{r-1}\\
z(re_{-r}-e_{-1})+\conj{z}(re_r-e_1)&=(r-1)(e_{r-1}+e_{1-r})
\end{align*}\right.
$$




$$
z(t)=\frac{1}{r+1}\left(re^{it}+e^{irt}\right)
$$
