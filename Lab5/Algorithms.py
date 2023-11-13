import PriorityQueue
import numpy as np
import random
import DisjointSet


def primMST(graph):
    pass


def kruskalMST(g):
    n = len(g)
    ds = DisjointSet.DisjointSet()
    for i in range(n):
        ds.makeSet(i)
    e = []
    for i in range(n):
        for j in range(i+1, n):
            if g[i][j] != 0:
                e.append((i, j, g[i][j]))
    e.sort(key=lambda x: x[2])  # sort based on weight, or e[2]
    mst = []
    for ed in e:
        u, v, w = ed
        if ds.findSet(u) != ds.findSet(v):
            mst.append((u, v, w))
            ds.union(u, v)
    return mst


def getRandomGraph(n, m, maxWeight):
    a = np.zeros((n, n), dtype=int)
    count = 0
    i = random.randint(0, n)
    j = random.randint(0, n)
    while count < m:
        if i == j or a[i][j] == maxWeight:
            continue
        a[i][j] += 1
        a[j][i] += 1
        count += 1
        i = random.randint(0, n)
        j = random.randint(0, n)
    return a


def graph2DisjointSets(a):
    ds = DisjointSet.DisjointSet()
    for i in range(len(a)):
        ds.makeSet(i)
    return ds
