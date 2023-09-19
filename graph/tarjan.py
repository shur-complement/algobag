# Tarjan's algorithm for Strongly Connected Components
# https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
# Time: O(|V| + |E|)
# Space: O(|V| * (2+5w))

def tarjan(adjList, numVertices):
    V = numVertices
    index = [None] * numVertices
    lowlink = [None] * numVertices
    onStack = [False] * numVertices
    idx = 0
    S = []

    def strongconnect(v, out):
        nonlocal idx
        # set the depth index for v to the smallest unused index
        index[v] = idx
        lowlink[v] = idx
        idx += 1
        S.append(v)
        onStack[v] = True

        # consider successors of v
        E = adjList[v]
        for w in E:
            if not index[w]:
                # successor w has not yet been visited, recurse
                strongconnect(w, out)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif onStack[w]:
                # successor w is in stack, therefore in current SCC
                lowlink[v] = min(lowlink[v], index[w])

        # If v is a root node, pop the stack and generate an SCC
        if lowlink[v] == index[v]:
            scc = set()
            w = None
            while w != v:
                w = S.pop()
                onStack[w] = False
                scc.add(w)
            out.append(scc)

    out = []
    for i in range(V):
        if index[i] == None:
            strongconnect(i, out)
    return out

if __name__ == "__main__":

    from collections import defaultdict

    g1 = defaultdict(list)
    g1[0] = [1]
    g1[1] = [2]
    g1[2] = [3,4]
    g1[3] = [0]
    g1[4] = [2]
    res = tarjan(g1, 5)
    print(res)

    g2 = defaultdict(list)
    g2[0] = [2,3]
    g2[1] = [0]
    g2[2] = [1]
    g2[3] = [4]
    res = tarjan(g2, 5)
    print(res)
