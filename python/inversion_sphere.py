from numpy import meshgrid, linspace, cos, sin, pi
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import figure
from matplotlib.animation import FuncAnimation, writers


def generate_sphere(X):
    n = X ** 2 + Y ** 2 + Z ** 2
    Xi = X / n
    Yi = Y / n
    Zi = Z / n
    return Xi, Yi, Zi


def update(i):
    ax.cla()
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.scatter([0], [0], [0], color='red')
    X = X0 - 3 + 6 * i / frames
    ax.plot_surface(X, Y, Z, alpha=.5, color='blue')
    Xi, Yi, Zi = generate_sphere(X)
    ax.plot_surface(Xi, Yi, Zi, alpha=.5, color='green')


fig = figure()
ax = fig.gca(projection='3d')

n = 50
frames = 100

r = 1
p = linspace(0, 2 * pi, n)
t = linspace(-pi / 2, pi / 2)
P, T = meshgrid(p, t)
X0, Y, Z = r * cos(P) * cos(T), r * sin(P) * cos(T), r * sin(T)

ani = FuncAnimation(fig, update, frames=frames, interval=100, repeat=True)
Writer = writers['ffmpeg']
writer = Writer(fps=20, metadata=dict(artist='Laurent Garcin'), bitrate=18000)
ani.save('inversion_sphere.mp4', writer=writer)
