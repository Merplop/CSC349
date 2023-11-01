import numpy as np
import random
import DisjointSet


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
        ds.makeSet(a[i][i])
    return ds
