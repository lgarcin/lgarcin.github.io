from sympy import Symbol, exp, sin, cos, series, lambdify
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#plt.rcParams['animation.ffmpeg_path'] = "C:/ffmpeg/bin/ffmpeg.exe"

fig = plt.figure()

x = Symbol('x')
f = exp((sin(x) - cos(x)) / 4) / (x ** 2 + 10)
xdata = np.linspace(-10, 10, 200)
ydata = lambdify(x, f, "numpy")(xdata)
y0 = lambdify(x, f, "numpy")(0)
orders = 10
yydata = []

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


def animate(i):
    num = i % len(xdata)
    o = i // len(xdata)
    func.set_data(xdata, ydata)
    dl.set_data(xdata[:num], yydata[o][:num])
    point.set_data([0], [y0])
    legend_func.set_text("Graphe de la fonction")
    legend_dl.set_text("DL à l'ordre " + str(o))
    return [func, dl, point, legend_func, legend_dl]


ani = animation.FuncAnimation(fig, animate, np.arange(orders * len(xdata)), interval=10, repeat_delay=200, blit=True,
                              init_func=init)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Laurent Garcin'), bitrate=1800)
ani.save('dl.mp4', writer=writer)
plt.show()
