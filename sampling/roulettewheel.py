# Algorithms for sampling from a discrete distribution
# with replacement

from random import random, randrange

# Roulette-wheel selection via stochastic acceptance
# https://arxiv.org/abs/1109.3627
class Stochastic:
    def __init__(self, w):
        self.w_max = max(w)
        self.K = len(w)
        self.w = w

    def sample(self):
        while True:
            i = randrange(0, self.K)
            wi = self.w[i]
            if random() < wi/self.w_max:
                return i

# https://en.wikipedia.org/wiki/Fitness_proportionate_selection
class LinearSearch:
    def __init__(self, w):
        s = sum(w)
        w[0] /= s
        for i in range(1, len(w)):
            w[i] = w[i-1] + w[i]/s
        self.cdf = w

    def sample(self):
        p = random()
        for i in range(len(self.cdf)):
            if self.cdf[i] > p:
                return i

# https://en.wikipedia.org/wiki/Fitness_proportionate_selection
class BinarySearch:
    def __init__(self, w):
        s = sum(w)
        w[0] /= s
        for i in range(1, len(w)):
            w[i] = w[i-1] + w[i]/s
        self.cdf = w

    def sample(self):
        p = random()
        lo, hi = 0, len(self.cdf)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.cdf[mid] < p:
                lo = mid + 1
            else:
                hi = mid
        return lo

if __name__ == "__main__":
    from collections import Counter

    weights = [0.1, 0.1, 0.4, 0.2]

    stochastic = Stochastic(weights)
    linear = LinearSearch(weights)
    binary = BinarySearch(weights)

    print(Counter([stochastic.sample() for _ in range(1000)]))
    print(Counter([linear.sample() for _ in range(1000)]))
    print(Counter([binary.sample() for _ in range(1000)]))
