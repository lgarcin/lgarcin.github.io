'''
Created on 21 mai 2012

@author: Laurent
'''
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

input()

while True:
    rate(100)
    li = len(ballList)
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
    if li != len(ballList):
        print(len(ballList))
