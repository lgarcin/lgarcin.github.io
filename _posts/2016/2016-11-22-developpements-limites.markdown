---
title: "Développements limités"
---

Parce qu'un dessin vaut parfois mieux qu'un long discours...

<video controls>
<source src="/images/2016/11/dl.mp4" type="video/mp4">
<source src="/images/2016/11/dl.webm" type="video/webm">
</video>

En ce qui concerne les détails techniques, l'animation a été effectuée à l'aide de Python.

* Les développements limités ont été calculés à l'aide de la bibliothèque de calcul formel [sympy][e389fe0d].

* Le tracé a été effectué à l'aide de la bibliothèque [matplotlib][5f2fb8f4].

* Le film a été généré à l'aide de l'utilitaire [ffmpeg][5e3f970c].

  [e389fe0d]: https://docs.sympy.org/latest/index.html "sympy"
  [5f2fb8f4]: https://matplotlib.org/ "matplotlib"
  [5e3f970c]: https://www.ffmpeg.org/ "ffmpeg"

Voilà le code pour ceux qui veulent s'amuser avec.

```python
from sympy import Symbol, exp, sin, cos, series, lambdify
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()

x = Symbol('x')
# Fonction dont on va calculer les DL
f = exp((sin(x) - cos(x)) / 4) / (x ** 2 + 10)
xdata = np.linspace(-10, 10, 200)
ydata = lambdify(x, f, "numpy")(xdata)
y0 = lambdify(x, f, "numpy")(0)
orders = 10
yydata = []

# Calcul des DL
for o in range(orders):
    dl = series(f, x, 0, o + 1).removeO()
    if o == 0:
        yydata.append([y0] * len(xdata))
    else:
        yydata.append(lambdify(x, dl, "numpy")(xdata))

func, = plt.plot(xdata, ydata, color="b")
dl, = plt.plot([], [], color="g")
point, = plt.plot([], [], color="r", marker='.', markersize=10)

legend_func = plt.text(-9, 0.10, r"", {'color': 'b', 'fontsize': 16})
legend_dl = plt.text(-9, 0.08, r"", {'color': 'g', 'fontsize': 16})


def init():
    func.set_data([], [])
    dl.set_data([], [])
    point.set_data([], [])
    legend_func.set_text(r"")
    legend_dl.set_text(r"")
    return [func, dl, point, legend_func, legend_dl]

# Fonction d'animation
def animate(i):
    num = i % len(xdata)
    o = i // len(xdata)
    func.set_data(xdata, ydata)
    dl.set_data(xdata[:num], yydata[o][:num])
    point.set_data([0], [y0])
    legend_func.set_text("Graphe de la fonction")
    legend_dl.set_text("DL à l'ordre " + str(o))
    return [func, dl, point, legend_func, legend_dl]

# Création de l'animation
ani = animation.FuncAnimation(fig, animate, np.arange(orders * len(xdata)),
      interval=10, repeat_delay=200, blit=True, init_func=init)
# Sauvegarde du film au format MPEG-4
Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Laurent Garcin'), bitrate=1800)
ani.save('dl.mp4', writer=writer)
plt.show()
```
