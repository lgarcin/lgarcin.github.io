---
layout: "post"
title: "Pentagone régulier"
published: true
---

On sait que les images des racines <script type="math/tex">n^\text{èmes}</script> de l'unité forment un polygone régulier. On expose dans ce post la construction du pentagone régulier.


### Calcul de <script type="math/tex">\cos\frac{2\pi}{5}</script>

Il suffit de faire un tour par les complexes. En posant <script type="math/tex">\omega=e^\frac{2i\pi}{5}</script>, on a clairement <script type="math/tex">1+\omega+\omega^2+\omega^3+\omega^4=\frac{\omega^5-1}{\omega-1}=0</script>.
Or <script type="math/tex">\omega+\omega^4=\omega+\frac{1}{\omega}=2\cos\frac{2\pi}{5}</script> et <script type="math/tex">\omega^2+\omega^3=\omega^2+\frac{1}{\omega^2}=2\cos\frac{4\pi}{5}=2(2\cos^2\frac{2\pi}{5}-1)</script>. Il s'ensuit que <script type="math/tex">\cos\frac{2\pi}{5}</script> est racine du polynôme <script type="math/tex">4X^2+2X-1</script>. Puisque <script type="math/tex">\cos\frac{2\pi}{5}</script> est positif, <script type="math/tex">\cos\frac{2\pi}{5}=\frac{\sqrt5-1}{4}</script>.

### Construction d'un repère orthonormé et du cercle trigonométrique.

On se donne deux points <script type="math/tex">A</script> et <script type="math/tex">B</script> du plan et l'on convient que <script type="math/tex">AB=1</script>. On peut alors tracer le cercle <script type="math/tex">\mathscr{C}</script> de centre <script type="math/tex">A</script> passant par <script type="math/tex">B</script>. On note <script type="math/tex">C</script> le point d'intersection du cercle <script type="math/tex">\mathscr{C}</script> et de la droite <script type="math/tex">(AB)</script>. On peut tracer la médiatrice du segment <script type="math/tex">[AC]</script> à l'aide d'un compas. On note <script type="math/tex">D</script> et <script type="math/tex">E</script> les points d'intersection du cercle <script type="math/tex">\mathscr{C}</script> et de cette médiatrice.

![repere](/images/2016/09/pentagone1.png)

### Construction de <script type="math/tex">\cos\frac{2\pi}{5}</script>

Dans un premier temps, on construit le milieu <script type="math/tex">F</script> du segment <script type="math/tex">[AC]</script>. On trace alors le cercle <script type="math/tex">\Gamma</script> de centre <script type="math/tex">F</script> passant par <script type="math/tex">D</script>. Le théorème de Pythagore permet d'affirmer que <script type="math/tex">FD=\frac{\sqrt5}{2}</script>. Notons <script type="math/tex">G</script> le point d'intersection du cercle <script type="math/tex">\Gamma</script> et du segment <script type="math/tex">[AB]</script>. Il est évident que que <script type="math/tex">AG=\frac{\sqrt5-1}{2}</script>. On trace alors la médiatrice du segment <script type="math/tex">[AG]</script> qui coupe le segment <script type="math/tex">[AB]</script> en un point <script type="math/tex">H</script> ainsi que le cercle <script type="math/tex">\mathscr{C}</script> en des points <script type="math/tex">I</script> et <script type="math/tex">J</script>. On a alors bien <script type="math/tex">AH=\frac{\sqrt5-1}{4}=\cos\frac{2\pi}{5}</script>.

![cosinus](/images/2016/09/pentagone2.png)

### Construction du pentagone régulier

Puisque le cercle <script type="math/tex">\mathscr{C}</script> a pour rayon 1, les angles <script type="math/tex">\widehat{BAI}</script> et <script type="math/tex">\widehat{BAJ}</script> ont pour mesure <script type="math/tex">\frac{2\pi}{5}</script>. Il ne reste alors plus qu'à tracer les cercles de centre <script type="math/tex">I</script> et <script type="math/tex">J</script> passant par <script type="math/tex">B</script> : ceux-ci coupent le cercle <script type="math/tex">\mathscr{C}</script> en des points <script type="math/tex">K</script> et <script type="math/tex">L</script>. Le pentagone <script type="math/tex">BIKLJ</script> est alors régulier.

![pentagone](/images/2016/09/pentagone3.png)

### Pour aller plus loin

On peut se demander s'il existe des procédés de construction à la règle et au compas d'autres polygones réguliers. Par exemple, une telle construction de l'heptadécagone<sup>[1](#heptadecagone)</sup> régulier a été proposée par le prince des mathématiciens, Carl-Friedrich Gauß, à l'âge de 19 ans. Dans la foulée, ce dernier a prouvé que tout polygone dont le nombre de côtés est le produit d'une puissance de 2 et de nombres premiers de Fermat<sup>[2](#fermat)</sup> distincts est constructible à la règle et au compas. L'heptadécagone régulier est effectivement constructible à la règle et au compas puisque <script type="math/tex">17=2^{2^2}+1</script> est un nombre premier de Fermat. La réciproque de ce résultat est également vraie et a été prouvée ultérieurement par Wantzel.

<a name="heptadecagone">1</a> Un heptadécagone est un polygone à 17 côtés.

<a name="fermat">2</a> Un nombre de Fermat est un nombre de la forme <script type="math/tex">2^{2^n}+1</script> où <script type="math/tex">n</script> est un entier naturel. Tous les nombres de Fermat ne sont pas premiers.

### Animation Geogebra

<iframe scrolling="no" src="https://www.geogebra.org/material/iframe/id/EBBhzYnJ/width/800/height/1000/border/888888/sri/true/sdz/true" width="800px" height="1000px" style="border:0px;"> </iframe>
