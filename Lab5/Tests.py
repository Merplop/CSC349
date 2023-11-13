import Algorithms
import PriorityQueue
import timeit

def main():
    tests()


def tests():
    prim_times = {}
    kruskal_times = {}
    densities = [0.1, 0.25, 0.5, 0.66, 0.75]

    for v in range(10, 1000, 10):
        for dens in range(len(densities)):
            prim_times[v] = []
            kruskal_times[v] = []
            for reps in range(20):
                g = Algorithms.getRandomGraph(v, int(v*(v-1)*dens/2), 20)
                print("Graph: ", g)
                print("Kruskal's:", Algorithms.kruskalMST(g))
                print("Prim's:", Algorithms.primMST(g))
    #            ds = Algorithms.graph2DisjointSets(g)
    #            prim_time = timeit.timeit(lambda: Algorithms.primMST(g), number=2)
    #            kruskal_time = timeit.timeit(lambda: Algorithms.kruskalMST(g), number=2)
    #            prim_times[v][dens].append(prim_time)
    #            kruskal_times[v][dens].append(kruskal_time)



if __name__ == "__main__":
    main()
