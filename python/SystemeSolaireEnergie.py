import numpy as np
from bokeh.plotting import figure, show
from embed import embed_fig


class Astre():
    def __init__(self, pos, vitesse, masse):
        self._pos = pos
        self._vitesse = vitesse
        self._acceleration = np.array([[0., 0., 0.]])
        self._masse = masse

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos

    @property
    def vitesse(self):
        return self._vitesse

    @vitesse.setter
    def vitesse(self, vitesse):
        self._vitesse = vitesse

    @property
    def acceleration(self):
        return self._acceleration

    @acceleration.setter
    def acceleration(self, acceleration):
        self._acceleration = acceleration

    @property
    def masse(self):
        return self._masse


def init(perihelie, masse, vitesse, inclinaison, noeud, argument):
    inclinaison = np.radians(inclinaison)
    noeud = np.radians(noeud)
    argument = np.radians(argument)
    R1 = np.matrix([[np.cos(argument), -np.sin(argument), 0],
                    [np.sin(argument), np.cos(argument), 0], [0, 0, 1]])
    R2 = np.matrix(
        [[1, 0, 0], [0, np.cos(inclinaison), -np.sin(inclinaison)], [0, np.sin(inclinaison), np.cos(inclinaison)]])
    R3 = np.matrix([[np.cos(noeud), -np.sin(noeud), 0],
                    [np.sin(noeud), np.cos(noeud), 0], [0, 0, 1]])
    return Astre(pos=R3 @ R2 @ R1 @ np.array([perihelie, 0, 0]),
                 vitesse=R3 @ R2 @ R1 @ np.array([0, vitesse, 0]), masse=masse)


G = 6.7e-11
astres = []

soleil = Astre(pos=np.array([[0., 0., 0.]]),
               vitesse=np.array([[0., 0., 0.]]), masse=2.0e30)
astres.append(soleil)
mercure = init(4.7e10, 3.3e23, 5.9e4, 7, 48, 29)
astres.append(mercure)
venus = init(1.1e11, 4.9e24, 3.5e4, 3.4, 77, 55)
astres.append(venus)
terre = init(1.5e11, 6.0e24, 3.0e4, 0, 175, 288)
astres.append(terre)
mars = init(2.1e11, 6.4e23, 2.6e4, 1.8, 49, 286)
astres.append(mars)
jupiter = init(7.4e11, 1.9e27, 1.3e4, 1.3, 100.6, 275.1)
astres.append(jupiter)
saturne = init(1.3e12, 5.6e26, 1.0e4, 2.5, 113.7, 338.7)
astres.append(saturne)
uranus = init(2.7e12, 8.7e25, 7.1e3, 0.8, 74.0, 96.5)
astres.append(uranus)
neptune = init(4.4e12, 1.0e26, 5.5e3, 1.77, 131.7, 273.2)
astres.append(neptune)

dt = 1e5
t = 0

x = []
y1 = []
y2 = []
y3 = []
for i in range(20000):
    Ec = 0
    Ep = 0
    for p in astres:
        Ec += .5 * p.masse * np.linalg.norm(p.vitesse) ** 2
        p.pos += p.vitesse * dt
    for p in astres:
        p.acceleration = np.array([[0., 0., 0.]])
        for q in astres:
            if q is not p:
                p.acceleration += G * (q.pos - p.pos) * \
                    q.masse / np.linalg.norm(q.pos - p.pos) ** 3
                Ep -= .5 * G * p.masse * q.masse / \
                    np.linalg.norm(q.pos - p.pos)
    for p in astres:
        p.vitesse += p.acceleration * dt
    t += dt
    if i % 100 == 0:
        x.append(t)
        y1.append(Ec)
        y2.append(Ep)
        y3.append(Ec + Ep)

p = figure(title="Evolution de l'énergie : méthode d'Euler asymétrique",
           plot_width=600, plot_height=400)

p.line(x, y1, line_width=2, legend='Energie cinétique', line_color='red')
p.line(x, y2, line_width=2, legend='Energie potentielle', line_color='green')
p.line(x, y3, line_width=2, legend='Energie totale', line_color='blue')
p.legend.location = 'center_left'

embed_fig(p, "energie1.js")


x = []
y1 = []
y2 = []
y3 = []
for i in range(20000):
    Ec = 0
    Ep = 0
    for p in astres:
        p.acceleration = np.array([[0., 0., 0.]])
        for q in astres:
            if q is not p:
                p.acceleration += G * (q.pos - p.pos) * \
                    q.masse / np.linalg.norm(q.pos - p.pos) ** 3
                Ep -= .5 * G * p.masse * q.masse / \
                    np.linalg.norm(q.pos - p.pos)
    for p in astres:
        Ec += .5 * p.masse * np.linalg.norm(p.vitesse) ** 2
        p.pos += p.vitesse * dt
    for p in astres:
        p.vitesse += p.acceleration * dt
    t += dt
    if i % 100 == 0:
        x.append(t)
        y1.append(Ec)
        y2.append(Ep)
        y3.append(Ec + Ep)

p = figure(title="Evolution de l'énergie : méthode d'Euler classique",
           plot_width=600, plot_height=400)

p.line(x, y1, line_width=2, legend='Energie cinétique', line_color='red')
p.line(x, y2, line_width=2, legend='Energie potentielle', line_color='green')
p.line(x, y3, line_width=2, legend='Energie totale', line_color='blue')
p.legend.location = 'center_left'

embed_fig(p, "energie2.js")
