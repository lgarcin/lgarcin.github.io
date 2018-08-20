from scipy.integrate import odeint
from numpy import array, linspace, meshgrid, sqrt, cos, sin, exp
from matplotlib.pyplot import figure, plot, grid, legend, xlabel, ylabel, show, xlim, ylim, subplot, gca, quiver
from matplotlib.animation import FuncAnimation, writers
from numpy import vectorize


def f(x1, x2):
    return exp(cos(x1) / 2) * sin(x2 ** 2 / 20), 2 * cos(x1 ** 2 / 5)
    # mu = 1
    # return mu * (x1 - x1 ** 3 / 3 - x2), x1 / mu
    # return x1 / 5 + x2 * 5, -x1 * 5 + x2 / 5  # spirale
    # return -x2, x1  # cercle


def diff(X, t=0):
    return [*f(X[0], X[1])]


t = linspace(0, 30, 2000)
X0 = array([1, 0])

X = odeint(diff, X0, t)
x1_sol, x2_sol = X.T

x1_min, x1_max, x2_min, x2_max = min(
    x1_sol), max(x1_sol), min(x2_sol), max(x2_sol)
x1_range, x2_range = x1_max - x1_min, x2_max - x2_min
x1_min, x1_max, x2_min, x2_max = x1_min - .1 * x1_range, x1_max + .1 * \
    x1_range, x2_min - .1 * x2_range, x2_max + .1 * x2_range
x, y = meshgrid(linspace(x1_min, x1_max, 20), linspace(x2_min, x2_max, 20))
dx, dy = vectorize(f)(x, y)

fig = figure(figsize=(10, 5))

subplot(121)
grid()
xlim([min(t), max(t)])
ylim([min(x1_min, x2_min), max(x1_max, x2_max)])
p1, = plot([], [], 'r-', label="$x$")
p2, = plot([], [], 'b-', label="$y$")
legend()

subplot(122)
grid()
gca().set_aspect('equal', adjustable='box')
xlim([x1_min, x1_max])
ylim([x2_min, x2_max])
xlabel("$x$")
ylabel("$y$")
p3, = plot([], [], 'g-')
p4, = plot([], [], 'go')
quiver(x, y, dx, dy)


def animate(i):
    p1.set_data(t[:i], x1_sol[:i])
    p2.set_data(t[:i], x2_sol[:i])
    p3.set_data(x1_sol[:i], x2_sol[:i])
    p4.set_data(x1_sol[i], x2_sol[i])
    return p1, p2, p3, p4


ani = FuncAnimation(fig, animate, range(len(t)), interval=10, blit=True)
Writer = writers['ffmpeg']
writer = Writer(fps=100, metadata=dict(artist='Laurent Garcin'), bitrate=18000)
ani.save('test.mp4', writer=writer)

show()
