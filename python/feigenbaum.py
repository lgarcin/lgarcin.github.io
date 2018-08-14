from numpy import linspace
from matplotlib.pyplot import scatter, show, xlim, ylim


def f(r, x):
    return r * x * (1 - x)


def feigenbaum(r1, r2, nb, N):
    r_range = linspace(r1, r2, nb)
    x = []
    y = []
    for r in r_range:
        u = .1
        for _ in range(N):
            u = f(r, u)
        for _ in range(N):
            u = f(r, u)
            x.append(r)
            y.append(u)
    scatter(x, y, marker='.', s=1)
    xlim(r1, r2)
    ylim(0, 1)
    show()


feigenbaum(3.82, 3.86, 10000, 500)
