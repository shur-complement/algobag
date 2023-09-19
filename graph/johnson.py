# Finding All the Elementary Circuits of a Directed Graph (Johnson 1975)
# https://epubs.siam.org/doi/10.1137/0204007
#
# Time: O((V+E)(C+1))
# Space: O(V+E)
# where V is num vertices, E is num edges, C is num elementary circuits

from collections import defaultdict

def find_elementary_circuits(adjList):
    cycles = []
    blocked = defaultdict(bool)
    B = defaultdict(list)
    stack = []

    def unblock(node):
        blocked[node] = False
        Bnode = B[node]
        while Bnode:
            w = Bnode.pop()
            if blocked[w]:
                unblock(w)

    def findCycles(v, s, adjList) -> bool:
        f = False
        stack.append(v)
        blocked[v] = True
        for w in adjList[v]:
            # found cycle
            if w == s:
                cycle = []
                for index in stack:
                    cycle.append(index)
                cycles.append(cycle)
                f = True
            elif not blocked[w]:
                if findCycles(w, s, adjList):
                    f = True
        if f:
            unblock(v)
        else:
            for w in adjList[v]:
                if v not in B[w]:
                    B[w].append(v)
        stack.remove(v)
        return f

    sccs = strongly_connected_components(adjList)
    for component in sccs:
        Ak = defaultdict(list)
        for n in component:
            Ak[n] = adjList[n]
            blocked[n] = False
            B[n] = []
        s = min(Ak)
        findCycles(s, s, Ak)

    return cycles

# Tarjan's Strongly Connected Components
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


g = defaultdict(list)
g.update({
    0: [1],
    1: [2],
    2: [3],
    3: [0],
    10: [11],
    11: [12],
    12: [10]
})

circuits = find_elementary_circuits(g)
print(circuits)

