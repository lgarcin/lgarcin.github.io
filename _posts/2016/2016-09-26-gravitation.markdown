---
title: "Méthode d'Euler et gravitation"
---

### Description du problème

On considère un système de corps de masses $m_i$ et de positions $\\mathbf{r}\_i$ soumis à la gravitation. D'après le principe fondamental de la dynamique

$$
\ddot{\mathbf{r}}_i=\sum_{j\neq i}\frac{Gm_j}{\|\mathbf{r}_j-\mathbf{r}_i\|^3}(\mathbf{r}_j-\mathbf{r}_i)
$$

Dans le cas où le système est formé de deux corps, on sait résoudre explicitement ce système d'équations différentielles. Dans le cas contraire, on est obligé de faire appel à des méthodes de résolution approchée : on emploiera ici la méthode d'Euler qui est une méthode bien connue de résolution numérique d'équations différentielles par discrétisation du temps.

On sait par ailleurs que la force gravitationnelle dérive d'un potentiel : plus précisément, l'énergie potentielle du système est :

$$
E_p=\frac{1}{2}\sum_{i\neq j}\frac{Gm_im_j}{\|\mathbf{r}_j-\mathbf{r}_i\|}
$$

Le facteur $\\frac{1}{2}$ provient du fait que chaque paire de corps intervient deux fois dans la somme. Enfin, il est clair que l'énergie cinétique du système est :

$$
E_c=\frac{1}{2}\sum_im_i\|\dot{\mathbf{r}}_i\|^2
$$

L'énergie totale du système est $E=E_p+E_c$.

### La méthode d'Euler

On se contente d'exposer cette méthode dans le cadre des équations différentielles autonomes puisque celles de notre problème sont bien de ce type : l'accélération dépend uniquement de la position et pas du temps.

Pour résoudre de manière approchée le système de Cauchy

$$
\left\lbrace\begin{aligned}y'&=f(y)\\y(t_0)&=y_0\end{aligned}\right.
$$

on fixe un intervalle de temps $\Delta t$ et on calcule des valeurs approchées $y_n$ de $y$ aux temps $t_n=t_0+n\Delta t$ en utilisant la relation de récurrence

$$
y_{n+1}=y_n+f(y_n)\Delta t
$$

Evidemment, l'erreur d'approximation augmente avec $n$ puisqu'on utilise à chaque fois une valeur approchée pour calculer l'approximation suivante.

En posant $\mathbf{R}=(\mathbf{r}_i)_i$, le système différentiel de notre problème peut s'écrire sous la forme $\ddot{\mathbf{R}}=f(\mathbf{R})$ et on se ramène classiquement à une équation différentielle d'ordre 1 en posant $y=(\mathbf{R},\dot{\mathbf{R}})$. La méthode d'Euler décrite précédemment nous amène alors à calculer des valeurs approchées de $\mathbf{R}$ en utilisant les relations de récurrence

$$
\left\lbrace\begin{aligned}\mathbf{R}_{n+1}&=\dot{\mathbf{R}}_n\Delta t\\\dot{\mathbf{R}}_{n+1}&=f(\mathbf{R}_n)\Delta t\end{aligned}\right.
$$

Malheureusement, cette méthode n'est pas stable numériquement : l'erreur augmente très rapidement avec $n$. On utilise donc une variante de la méthode d'Euler appelée méthode d'Euler _asymétrique_. Cette méthode est adaptée aux systèmes conservatifs comme celui que nous étudions (la force gravitationnelle dérive d'un potentiel). Le schéma de récurrence est alors le suivant.

$$
\left\lbrace\begin{aligned}\mathbf{R}_{n+1}&=\dot{\mathbf{R}}_n\Delta t\\\dot{\mathbf{R}}_{n+1}&=f(\mathbf{R}_{n+1})\Delta t\end{aligned}\right.
$$

Méthode d'Euler classique :

- on calcule les accélérations à partir des positions au temps $t_n$ ;
- on calcule les positions au temps $t\_{n+1}$ à partir des vitesses aux temps $t_n$ ;
- on calcule les vitesses au temps $t\_{n+1}$ à partir des accélérations précédemment calculées.

Méthode d'Euler asymétrique :

- on calcule les positions au temps $t\_{n+1}$ à partir des vitesses au temps $t_n$ ;
- on calcule les accélérations à partir de ces nouvelles positions ;
- on calcule les vitesses au temps $t\_{n+1}$ à partir de ces accélérations.

### Implémentation

On utilise la bibliothèque [VPython](https://vpython.org/) qui permet d'animer des scènes 3D. La dernière version de cette bibliothèque ne peut être utilisée que dans une application [notebook Jupyter](https://jupyter.org/).

### Modélisation du système solaire

Grâce à Wikipédia, on récupère les [paramètres orbitaux](https://fr.wikipedia.org/wiki/M%C3%A9canique_spatiale#Param.C3.A8tres_orbitaux) des différentes planètes permettant de placer ces dernières par rapport au Soleil. On fait démarrer la simulation avec toutes les planètes à leurs périhélies, ce qui est une configuration exceptionelle mais qui a bien dû se produire une fois depuis la création du système solaire.

<button type="button" class="btn btn-info" data-toggle="collapse" data-target="#systeme">Code Python</button>

```python
from vpython import *

def init(perihelie,masse,vitesse,rayon,couleur,inclinaison,noeud,argument):
    p=vector(perihelie,0,0)
    a=p.rotate(radians(noeud),vector(0,0,1))
    p=a.rotate(radians(argument),vector(0,0,1))
    p=p.rotate(radians(inclinaison),a)
    s=sphere(pos=p,radius=log10(rayon)*1e9,color=couleur,make_trail=True)
    s.masse=masse
    v=vector(0,vitesse,0)
    a=v.rotate(radians(noeud),vector(0,0,1))
    v=a.rotate(radians(argument),vector(0,0,1))
    v=v.rotate(radians(inclinaison),a)
    s.vitesse=v
    return s

G=6.7e-11

astres=[]
soleil=sphere(pos=vector(0,0,0),radius=log10(7e8)*1e9,color=color.yellow)
soleil.masse=2.0e30
soleil.vitesse=vector(0,0,0)
astres.append(soleil)
mercure=init(4.7e10,3.3e23,5.9e4,2.4e6,color.orange,7,48,29)
astres.append(mercure)
venus=init(1.1e11,4.9e24,3.5e4,6.1e6,color.white,3.4,77,55)
astres.append(venus)
terre=init(1.5e11,6.0e24,3.0e4,6.4e6,color.blue,0,175,288)
astres.append(terre)
mars=init(2.1e11,6.4e23,2.6e4,3.4e6,color.red,1.8,49,286)
astres.append(mars)
jupiter=init(7.4e11,1.9e27,1.3e4,7.0e7,color.cyan,1.3,100.6,275.1)
astres.append(jupiter)
saturne=init(1.3e12,5.6e26,1.0e4,5.8e7,color.cyan,2.5,113.7,338.7)
astres.append(saturne)
uranus=init(2.7e12,8.7e25,7.1e3,2.5e7,color.cyan,0.8,74.0,96.5)
astres.append(uranus)
neptune=init(4.4e12,1.0e26,5.5e3,2.4e7,color.blue,1.77,131.7,273.2)
astres.append(neptune)

dt=1e4

while True:
    rate(100)
    for p in astres:
        p.pos+=p.vitesse*dt
    for p in astres:
        acceleration=vector(0,0,0)
        for q in astres:
            if q is not p:
                acceleration+=G*(q.pos-p.pos)*q.masse/(q.pos-p.pos).mag**3
        p.vitesse+=acceleration*dt
```
{: .collapse #systeme }

<video controls>
<source src="/images/2016/10/SystemeSolaire.mp4" type="video/mp4">
<source src="/images/2016/10/SystemeSolaire.webm" type="video/webm">
</video>

Le calcul de l'énergie montre que tout se passe bien : l'énergie totale du système reste constante.

<div>
<script src="/js/energie1.js" id="dfe57dee-8347-4371-b9ff-a1c1c39b71a1"></script>
</div>

A titre de comparaison, la vidéo suivante montre les trajectoires obtenues en employant la méthode d'Euler classique et non la méthode d'Euler asymétrique.

<video controls>
<source src="/images/2016/10/Foirage.mp4" type="video/mp4">
<source src="/images/2016/10/Foirage.webm" type="video/webm">
</video>

On remarque d'ailleurs que l'énergie totale du système ne se conserve pas.

<div>
<script src="/js/energie2.js" id="2d75a072-ccf6-4ad7-b422-5bf8058a3fb6"></script>
</div>

### Création d'un système solaire

On place un grand nombre de corps avec des positions et des vitesses aléatoires et on les soumet à la force de gravitation. On considère que tous les chocs entre ces corps sont [parfaitement inélastiques](https://fr.wikipedia.org/wiki/Collision_parfaitement_in%C3%A9lastique) : les astres entrant en collision fusionnent alors pour donner une nouvelle planète tout en conservant la quantité de mouvement totale.

<button type="button" class="btn btn-info" data-toggle="collapse" data-target="#formation">Code Python</button>

```python
from random import normalvariate, uniform
from vpython import sphere, vector, rate

def merge(l):
    pos = vector(0, 0, 0)
    vel = vector(0, 0, 0)
    s = 0
    for b in l:
        s = s + b.mass
        pos += b.mass * b.pos
        vel += b.mass * b.velocity
    rad = s ** (1. / 3)
    ball = sphere(pos=pos / s, radius=rad, make_trail=True, retain=50)
    ball.trail_radius = ball.radius / 3
    ball.velocity = vel / s
    ball.mass = s
    ball.radius = rad
    return ball

ballList = []
n = 100
G = 100
dt = .005
dpos = 10
dvel = 5
rad = .5

for i in range(n):
    x = normalvariate(0, dpos)
    y = normalvariate(0, dpos)
    z = normalvariate(0, dpos)
    vx = uniform(-dvel, dvel)
    vy = uniform(-dvel, dvel)
    vz = uniform(-dvel, dvel)
    ball = sphere(pos=vector(x, y, z), radius=rad, make_trail=True, retain=50)
    ball.trail_radius = ball.radius / 3
    ball.velocity = vector(vx, vy, vz)
    ball.mass = ball.radius ** 3
    ballList.append(ball)

while True:
    rate(50)
    l = len(ballList)
    for b in ballList:
        b.pos += b.velocity * dt
    collisions = [set([b]) for b in ballList]
    copyList = list(ballList)
    for b1 in ballList:
        copyList.remove(b1)
        for b2 in copyList:
            d = (b1.pos - b2.pos).mag2
            c = G * d ** (-3. / 2) * dt
            b1.velocity += c * b2.mass * (b2.pos - b1.pos)
            b2.velocity += c * b1.mass * (b1.pos - b2.pos)
            if d < (b1.radius + b2.radius) ** 2:
                p1 = next(p for p in collisions if b1 in p)
                p2 = next(p for p in collisions if b2 in p)
                if p1 is not p2:
                    collisions.append(p1.union(p2))
                    collisions.remove(p1)
                    collisions.remove(p2)
    for c in collisions:
        if len(c) > 1:
            ballList.append(merge(c))
            for b in c:
                ballList.remove(b)
                b.visible = False
                b.clear_trail()
```
{: .collapse #formation }

<video controls>
<source src="/images/2016/10/Gravity.mp4" type="video/mp4">
<source src="/images/2016/10/Gravity.webm" type="video/webm">
</video>

 On assiste à la formation d'un "soleil" autour duquel gravitent des "planètes".
