# Boruvka's Algorithm
# https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm
# Find the minimum spanning tree in a graph
# Time: O(E log V)
# Space: O(V)

# Disjoint Set using Rem's algorithm
class RemDisjointSet:
    def __init__(self, N):
        self.parent = list(range(0, N))

    def find(self, u):
        p = self.parent
        while True:
            v = p[u]
            if v == u:
                return u
            w = p[v]
            if w == v:
                return v
            p[u] = w
            u = w

    def unite(self, u, v):
        p = self.parent
        x = p[u]
        y = p[v]
        while True:
            if x == y: return False
            elif x < y:
                p[v] = x
                if v == y: return True
                v = y
                y = p[v]
            else:
                p[u] = y
                if u == x: return True
                u = x
                x = p[u]

class EdgeList:
    def __init__(self):
        self.num_nodes = 0
        self.edges = []

    def add(self, u, v, weight):
        self.edges.append((u, v, weight))
        self.num_nodes = max(self.num_nodes, u+1, v+1)

def boruvka(g: EdgeList) -> (float, EdgeList):
    """
    finds the minimum spanning tree given an edge list.
    Returns the minimum spanning tree and its weight
    """

    mst_weight = 0
    out = EdgeList()

    N = g.num_nodes
    uf = RemDisjointSet(N)
    mst_size = 0

    while mst_size < N-1:
        min_weight_edge = [None] * g.num_nodes
        min_weight_edge_w = [None] * g.num_nodes

        # for each edge
        for i in range(len(g.edges)):
            u, v, w = g.edges[i]

            u_root = uf.find(u)
            v_root = uf.find(v)

            # same component? skip
            if u_root == v_root: continue

            if not min_weight_edge_w[u_root] or min_weight_edge_w[u_root] > w:
                min_weight_edge[u_root] = (u, v)
                min_weight_edge_w[u_root] = w

            if not min_weight_edge_w[v_root] or min_weight_edge_w[v_root] > w:
                min_weight_edge[v_root] = (u, v)
                min_weight_edge_w[v_root] = w

        # for each component whose cheapest edge exists
        # add the edge to MST
        for node in range(g.num_nodes):
            edge_weight = min_weight_edge_w[node]
            if edge_weight:
                u,v = min_weight_edge[node]
                if uf.unite(u, v):
                    mst_weight += edge_weight
                    mst_size += 1
                    out.add(u, v, edge_weight)

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
