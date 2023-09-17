# Kruskal's Algorithm
# https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
# Time: O(E log V)
# Space: O(E + V)
# Find the minimum spanning tree in a graph

class DisjointSet:
    def __init__(self, N):
        # create n singletons
        self.parent = list(range(0, N))
        self.size = [1] * N

    def find(self, u):
        # find with path splitting
        p = self.parent
        while u != p[u]:
            z = p[u]
            p[u] = p[p[u]]
            u = z
        return u

    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x,y = y,x
        self.parent[y] = x
        self.size[x] = self.size[x] + self.size[y]

class EdgeList:
    def __init__(self):
        self.num_nodes = 0
        self.edges = []

    def add(self, u, v, weight):
        self.edges.append((u, v, weight))
        self.num_nodes = max(self.num_nodes, u+1, v+1)

    def sort_by_weight(self):
        self.edges.sort(key=lambda x: x[2])

def kruskal(g: EdgeList) -> (float, EdgeList):
    """
    Finds the minimum spanning tree given an edge list.
    Returns the minimum spanning tree and its weight
    """

    mst_weight = 0
    out = EdgeList()

    N = g.num_nodes
    uf = DisjointSet(N)

    # order the edges by weight, increasing
    # so we can remove an edge with minimum weight from S
    g.sort_by_weight()

    for (u,v,w) in g.edges:
        u_root = uf.find(u)
        v_root = uf.find(v)
        if u_root != v_root:
            mst_weight += w
            out.add(u, v, w)
            uf.union(u_root, v_root)

    return mst_weight, out

def run_example(edges):
    g = EdgeList()
    for e in edges:
        g.add(*e)

    mst_weight, mst = kruskal(g)
    print("weight: ", mst_weight)
    for edge in mst.edges:
        print(edge)
    print("")

if __name__ == "__main__":

    run_example([
        (0, 1, 4),
        (0, 6, 7),
        (1, 6, 11),
        (1, 7, 20),
        (1, 2, 9),
        (2, 3, 6),
        (2, 4, 2),
        (3, 4, 10),
        (3, 5, 5.01),
        (4, 5, 15),
        (4, 7, 1),
        (4, 8, 5),
        (5, 8, 12),
        (6, 7, 1.1),
        (7, 8, 3),
    ])

    run_example([
        (0, 1, 8),
        (0, 2, 5),
        (1, 2, 9),
        (1, 3, 11),
        (2, 3, 15),
        (2, 4, 10),
        (3, 4, 7),
    ])

    run_example([
        (0,1,10),
        (1,3,15),
        (2,3,4),
        (2,0,6),
        (0,3,5),
    ])

    run_example([
        (0,1,1),
        (1,2,2),
        (2,3,5),
        (3,0,4),
        (0,2,3),
    ])

    run_example([
        (0,1,7),
        (1,2,6),
        (2,3,2),
        (3,4,4),
        (4,0,1),
        (4,1,5),
        (4,2,3),
    ])
