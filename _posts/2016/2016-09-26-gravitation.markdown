---
layout: "post"
title: "Méthode d'Euler et gravitation"
published: false
---

La méthode d'Euler est une méthode bien connue de résolution approchée d'équations différentielles.

### Modélisation du système solaire

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

scene=display()

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

while 1:
    rate(100)
    for p in astres:
        p.pos+=p.vitesse*dt
        p.acceleration=vector(0,0,0)
        for q in astres:
            if q is not p:
                p.acceleration+=G*(q.pos-p.pos)*q.masse/(q.pos-p.pos).mag**3
        p.vitesse+=p.acceleration*dt
```
{: .collapse #systeme }

<iframe width="560" height="315" src="https://www.youtube.com/embed/Aher_TlxUcw" frameborder="0" allowfullscreen></iframe>


### Création d'un système solaire

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
dt = .01
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
    rate(100)
    l = len(ballList)
    for b in ballList:
        b.pos += vector(b.velocity) * dt
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

<iframe width="560" height="315" src="https://www.youtube.com/embed/yvYEz-txv3A" frameborder="0" allowfullscreen></iframe>
