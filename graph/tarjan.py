# Tarjan's algorithm for Strongly Connected Components
# https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
# Time: O(|V| + |E|)
# Space: O(|V| * (2+5w))

def strongly_connected_components(adjList):
    idx = 0
    stack = []
    lowlink = {}
    index = {}
    out = []

    def strongconnect(v):
        nonlocal idx
        # set the depth index for this node to the smallest unused index
        index[v] = idx
        lowlink[v] = idx
        idx += 1
        stack.append(v)

        successors = adjList.get(v, [])
        for w in successors:
            if w not in lowlink:
                # Successor has not yet been visited; recurse on it
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in stack:
                # the successor is in the stack and hence in the current strongly connected component (SCC)
                lowlink[v] = min(lowlink[v], index[w])

        # If `node` is a root node, pop the stack and generate an SCC
        if lowlink[v] == index[v]:
            scc = []
            while True:
                successor = stack.pop()
                scc.append(successor)
                if successor == v: break
            out.append(scc)

    for node in adjList:
        if node not in lowlink:
            strongconnect(node)
    return out

if __name__ == "__main__":

    from collections import defaultdict

    g1 = defaultdict(list)
    g1[0] = [1]
    g1[1] = [2]
    g1[2] = [3,4]
    g1[3] = [0]
    g1[4] = [2]
    res = strongly_connected_components(g1)
    print(res)

    g2 = defaultdict(list)
    g2[0] = [2,3]
    g2[1] = [0]
    g2[2] = [1]
    g2[3] = [4]
    res = strongly_connected_components(g2)
    print(res)
