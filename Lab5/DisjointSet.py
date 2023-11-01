class DisjointSet:
    def __init__(self):
        self.dict = dict()

    def makeSet(self, v):
        self.dict[v] = v

    def findSet(self, v):
        return self.dict[v]

    def union(self, v, u):
        for e in self.dict:
            if self.dict[e] == v:
                self.dict[e] = u
