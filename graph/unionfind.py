# Disjoint Set 
# Stores a partition of a set into disjoint subsets

class UnionFindBySize:
    def __init__(n):
        self.parent = list(range(0,n))
        self.size = [1]*n

    def find(self, u):
        p = self.parent
        if p[u] != u:
            p[u] = self.find(p[u])
            return p[u]
        else:
            return u

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v: return

        s = self.size
        p = self.parent

        if s[u] < s[y]:
            u,v = v,u

        p[v] = u
        s[u] = s[u] + s[v]
