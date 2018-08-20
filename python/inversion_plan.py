from numpy import meshgrid, linspace, cos, sin, pi, ones, logspace
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import figure
from matplotlib.animation import FuncAnimation, writers


def generate_plane(z):
    Zp = z * ones((n, n))
    return Zp


def generate_sphere(z):
    n = x ** 2 + y ** 2 + z ** 2
    Xi = x / n
    Yi = y / n
    Zi = z / n
    return Xi, Yi, Zi


def update(i):
    ax.cla()
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.view_init(-10 + i / frames * 20, i / frames * 180)
    ax.scatter([0], [0], [0], color='red')
    z = -2 + i * 4 / frames
    Zp = generate_plane(z)
    ax.plot_surface(Xp, Yp, Zp, alpha=.5, color='blue')
    Xi, Yi, Zi = generate_sphere(z)
    ax.plot_surface(Xi, Yi, Zi, alpha=.5, color='green')


fig = figure()
ax = fig.gca(projection='3d')

n = 50
x = linspace(-2, 2, n)
y = linspace(-2, 2, n)
Xp, Yp = meshgrid(x, y)

r = logspace(-2, 2, n)
p = linspace(0, 2 * pi, n)
R, P = meshgrid(r, p)
x, y = R * cos(P), R * sin(P)

frames = 100
ani = FuncAnimation(fig, update, frames=frames, interval=100, repeat=True)
Writer = writers['ffmpeg']
writer = Writer(fps=20, metadata=dict(artist='Laurent Garcin'), bitrate=18000)
ani.save('inversion_plan.mp4', writer=writer)
