# The Walker-Vose Alias method
# Samples in O(1) at a cost of O(N) preprocessing
# https://en.wikipedia.org/wiki/Alias_method

from random import random, randrange

class AliasMethod:
    def __init__(self, weights):
        prob, alias = self._build(weights)
        self.size = len(weights)
        self.probability = prob
        self.alias = alias

    def sample(self):
        k = randrange(0, self.size)
        i = k if (random() < self.probability[k]) else self.alias[k]
        return i

    def _build(self, weights):
        N = len(weights)

        normProb = [0.0 for _ in range(N)]
        Large = [0 for _ in range(N)]
        Small = [0 for _ in range(N)]

        sum_ = sum(weights)

        for k in range(N):
            normProb[k] = weights[k] * N / sum_

        prob = [0.0 for _ in range(N)]
        alias = [0 for _ in range(N)]
        numSmall = 0
        numLarge = 0
        for k in range(N-1, -1, -1):
            if normProb[k] < 1.0:
                Small[numSmall] = k
                numSmall += 1
            else:
                Large[numLarge] = k
                numLarge += 1

        while numSmall and numLarge:
            numSmall -= 1
            cur_small = Small[numSmall]

            numLarge -= 1
            cur_large = Large[numLarge]

            prob[cur_small] = normProb[cur_small]
            alias[cur_small] = cur_large
            normProb[cur_large] = normProb[cur_large] + normProb[cur_small] - 1
            if normProb[cur_large] < 1:
                Small[numSmall] = cur_large
                numSmall += 1
            else:
                Large[numLarge] = cur_large
                numLarge += 1

        while numLarge:
            numLarge -= 1
            prob[Large[numLarge]] = 1

        while numSmall:
            numSmall -= 1
            prob[Small[numSmall]] = 1

        return prob, alias

if __name__ == "__main__":
    from collections import Counter

    weights = [0.1, 0.1, 0.4, 0.2]
    alias = AliasMethod(weights)
    print(Counter([alias.sample() for _ in range(1000)]))
