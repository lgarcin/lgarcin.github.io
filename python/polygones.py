from bokeh.plotting import figure
from numpy import cos, sin, pi
from bokeh.colors import HSL
from numpy import array
from embed import embed_fig


class Polygon:
    def __init__(self, sides, colors):
        self._sides = sides
        self._xs = array([cos(2 * k * pi / sides) for k in range(sides)])
        self._ys = array([sin(2 * k * pi / sides) for k in range(sides)])
        self._colors = colors

    def rotate(self):
        self._colors = [self._colors[-1]] + self._colors[:-1]

    def translate(self):
        self._xs = array(self._xs + 2.5)

    def draw(self):
        p.patch(self._xs, self._ys, fill_color=None)
        p.circle(self._xs, self._ys, color=self._colors, size=6)


p = figure(plot_width=700, plot_height=250, match_aspect=True)
p.axis.visible = False
p.grid.visible = False
sides = 7
colors = [HSL(int(k / sides * 255), 1., .5) for k in range(sides // 3)]
colors = colors * 3 + [colors[0]]
poly = Polygon(sides, colors)
for _ in range(sides):
    poly.draw()
    poly.rotate()
    poly.translate()
embed_fig(p, "polygones1.js")

p = figure(plot_width=700, plot_height=250, match_aspect=True)
p.axis.visible = False
p.grid.visible = False
sides = 6
colors = [HSL(int(k / sides * 255), 1., .5) for k in range(sides // 2)] * 2
poly = Polygon(sides, colors)
for _ in range(sides):
    poly.draw()
    poly.rotate()
    poly.translate()
embed_fig(p, "polygones2.js")
