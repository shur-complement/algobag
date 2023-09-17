# Boruvka's Algorithm
# https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm
# Find the minimum spanning tree in a graph
# Time: O(E log V)
# Space: O(V)

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

def boruvka(g):
    """
    Finds the minimum spanning tree given an edge list.
    Returns the minimum spanning tree and its weight
    """

    mst_weight = 0
    out = EdgeList()

    N = g.num_nodes
    uf = DisjointSet(N)

    while N > 1:
        min_weight_edge = [None] * g.num_nodes
        # for each edge
        for i in range(len(g.edges)):
            u, v, w = g.edges[i]
            u_root = uf.find(u)
            v_root = uf.find(v)

            # u and v must be in different components
            if u_root == v_root: continue

            if not min_weight_edge[u_root] or min_weight_edge[u_root][2] > w:
                min_weight_edge[u_root] = (u, v, w)

            if not min_weight_edge[v_root] or min_weight_edge[v_root][2] > w:
                min_weight_edge[v_root] = (u, v, w)

        # for each component whose cheapest edge is not None
        # add its cheapest edge to MST
        for node in range(g.num_nodes):
            if min_weight_edge[node]:
                u, v, w = min_weight_edge[node]

                u_root = uf.find(u)
                v_root = uf.find(v)

                if u_root == v_root: continue

                mst_weight += w
                out.add(u, v, w)
                uf.union(u, v)
                N -= 1

    return mst_weight, out

def run_example(edges):
    g = EdgeList()
    for e in edges:
        g.add(*e)

    mst_weight, mst = boruvka(g)
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
