import numpy as np

class PriorityQueue:


    def __init__(self):
        self.heap = []
        self.nodeDict = {}

    def init_list(self, v, s):
        self.heap = [(l, sys.maxsize) for l in v]
        self.nodeDict = {l: {"i": i, "parent": None} for i, (l, _) in enumerate(self.heap)}
        si = self.nodeDict[s]["i"]
        self.heap[si] = (s,0)

    def insert(self, x):
        n = len(self.heap)
        if n == 0:
            self.heap.append(x)
        else:
            self.heap.append(x)
            for i in range((size//2)-1,-1,-1):
                self.heapify(n, i)


    def findMin(self):
        return self.heap[0]


    def deleteMin(self):
        if len(self.heap) == 0:
            return None
        min = self.heap[0]
        popped = self.heap.pop()
        if len(self.heap) != 0:
            self.heap[0] = popped
            self.nodes[popped[0]]["i"] = 0
        self.heapify(0)
        self.nodeDict.pop(min[0])
        return min


    def decreaseKey(self, label, newKey):
        if label not in self.nodes:
            return
        i = self.nodeDict[label]["i"]
        if newKey < self.heap[index][1]:
            self.heap[i] = (label, newKey)
            self.percolateUp(i)


    def percolateUp(self, i):
        while i > 0:
            parent = (i-1)//2
            if self.heap[parent][1] > self.heap[i][1]:
                self.heap[i],self.heap[parent] = self.heap[parent],self.heap[i]
                self.nodeDict[self.heap[i][0]]["i"] = i
                self.nodeDict[self.heap[parent][0]]["i"] = parent
                i = parent
            else:
                return


    def heapify(self, n, i):
        min = i
        left = 2*i+1
        right = 2*i+2
        if left < len(self.heap) and self.heap[left][1] < self.heap[min][1]:
            min = left
        if right < len(self.heap) and self.heap[right][1] < self.heap[min][1]:
            min = right
        if min != i:
            self.heap[i],self.heap[min] = self.heap[min],self.heap[i]
            self.nodeDict[self.heap[i][0]]["i"]
            self.nodeDict[self.heap[i][0]]["i"]
            self.heapify(n, min)
