# Tarjan's algorithm for Strongly Connected Components
# https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
# Time: O(|V| + |E|)
# Space: O(|V| * (2+5w))

class Tarjan:
    def __init__(self, adjList, numVertices):
        self.V = numVertices
        self.adjList = adjList

    def scc(self):
        self.index = [None] * (self.V)
        self.lowlink = [None] * (self.V)
        self.onStack = [False] * (self.V)
        self.idx = 0
        self.S = []
        out = []
        for i in range(self.V):
            if self.index[i] == None:
                self._strongconnect(i, out)
        return out

    def _strongconnect(self, v, out):
        # set the depth index for v to the smallest unused index
        self.index[v] = self.idx
        self.lowlink[v] = self.idx
        self.idx += 1
        self.S.append(v)
        self.onStack[v] = True

        # consider successors of v
        E = self.adjList[v]
        for w in E:
            if not self.index[w]:
                # successor w has not yet been visited, recurse
                self._strongconnect(w, out)
                self.lowlink[v] = min(self.lowlink[v], self.lowlink[w])
            elif self.onStack[w]:
                # successor w is in stack, therefore in current SCC
                self.lowlink[v] = min(self.lowlink[v], self.index[w])

        # If v is a root node, pop the stack and generate an SCC
        if self.lowlink[v] == self.index[v]:
            scc = set()
            w = None
            while w != v:
                w = self.S.pop()
                self.onStack[w] = False
                scc.add(w)
            out.append(scc)

if __name__ == "__main__":

    from collections import defaultdict

    g1 = defaultdict(list)
    g1[0] = [1]
    g1[1] = [2]
    g1[2] = [3,4]
    g1[3] = [0]
    g1[4] = [2]
    res = Tarjan(g1, 5).scc()
    print(res)

    g2 = defaultdict(list)
    g2[0] = [2,3]
    g2[1] = [0]
    g2[2] = [1]
    g2[3] = [4]
    res = Tarjan(g2, 5).scc()
    print(res)
