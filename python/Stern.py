import matplotlib.pyplot as plt
import networkx as nx
from timeit import Timer


def mediante(r1, r2):
    return tuple(map(sum, zip(r1, r2)))


def delta(r1, r2):
    return r2[0] * r1[1] - r1[0] * r2[1]


def sternSuite(n):
    u = [(0, 1), (1, 0)]
    for _ in range(n):
        v = [mediante(r1, r2) for (r1, r2) in zip(u[1:], u[:-1])]
        w = [None] * (len(u) + len(v))
        w[::2] = u
        w[1::2] = v
        u = w
    return u


def sternBis(x):
    a = (0, 1)
    b = (1, 0)
    c = (1, 1)
    l = [c]
    while c != x:
        if delta(c, x) > 0:
            a = c
        else:
            b = c
        c = mediante(a, b)
        l.append(c)
    return l


def sternEncadre(x):
    p, q = x
    r, u, v, rr, uu, vv = p, 1, 0, q, 0, 1
    while rr != 0:
        k = r // rr
        r, u, v, rr, uu, vv = rr, uu, vv, r - k * rr, u - k * uu, v - k * vv
    p, q = p // r, q // r
    a, d = -v % p, -u % q
    b, c = (1 + a * q) // p, (1 + d * p) // q
    return (a, b), (c, d)


def sternPere(x):
    r1, r2 = sternEncadre(x)
    return r1 if sum(r1) > sum(r2) else r2


def sternLignee(x):
    a = x
    l = [x]
    while a != (1, 1):
        a = sternPere(a)
        l.append(a)
    return list(reversed(l))


def sternGraph(n):
    u = [(0, 1), (1, 1), (1, 0)]
    G = nx.Graph()
    G.add_nodes_from([-2, -1, 0])
    G.add_edges_from([(-2, 0), (-1, 0)])
    i = 1
    pos = {-2: [-2 ** (n - 1), 1], -1: [3 * 2 ** (n - 1), 1], 0: [2 ** (n - 1), 0]}
    labels = {-2: r'$\frac{0}{1}$', -1: r'$\frac{1}{0}$', 0: r'$\frac{1}{1}$'}
    for k in range(n):
        v = [mediante(r1, r2) for (r1, r2) in zip(u[1:], u[:-1])]
        G.add_nodes_from(range(i, i + len(v)))
        for x in range(len(v)):
            pos[i + x] = [-2 ** (n - 1) + (2 * x + 1) * 2 ** (n - k - 1), -k - 1]
            labels[i + x] = r'$\frac{' + str(v[x][0]) + '}{' + str(v[x][1]) + '}$'
        G.add_edges_from([(j, (j - 1) // 2) for j in range(i, i + len(v))])
        i += len(v)
        w = [None] * (len(u) + len(v))
        w[::2] = u
        w[1::2] = v
        u = w
    return G, pos, labels

plt.figure(figsize=(15, 10))
plt.axis('off')
G, pos, labels = sternGraph(5)
nodes = nx.draw_networkx_nodes(G, pos,node_size=800,node_color='w')
nodes.set_edgecolor('w')
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, labels, font_size=18)
plt.savefig('stern.png',bbox_inches='tight')
plt.show()

# print(Timer("sternLignee((13, 55))", globals=globals()).timeit())
# print(Timer("sternBis((13, 55))", globals=globals()).timeit())
