# https://en.wikipedia.org/wiki/Trie

class Trie:
    def __init__(self):
        self.trie = {}

    def add(self, seq):
        t = self.trie
        for e in seq:
            if e not in t: t[e] = {}
            t = t[e]
        t['*'] = {}

    def contains(self, seq):
        t = self.trie
        for e in seq:
            if e not in t: return False
            else: t = t[e]
        return '*' in t

    def startsWith(self, prefix):
        t = self.trie
        for e in prefix:
            if e not in t: return False
            else: t = t[e]
        return True

    def suggest(self, prefix):
        t = self.trie
        for e in prefix:
            if e not in t: return []
            else: t = t[e]

        stack = [(prefix, t)]
        out = []
        while stack:
            path, node = stack.pop()
            if '*' in node: out.append(path)
            for e in sorted(node.keys(), reverse=True):
                if e != '*': stack.append((path+e, node[e]))
        return out

if __name__ == "__main__":
    t = Trie()
    t.add("angst")
    t.add("forthcoming")
    t.add("folly")
    t.add("foolish")
    t.add("fool")
    print(t.contains("fool"))
    print(t.contains("foolish"))
    print(t.contains("foobar"))
    print(t.contains("apples"))
    print(t.contains("oranges"))
    print(t.startsWith("foo"))
    print(t.startsWith("for"))
    print(t.suggest("f"))
